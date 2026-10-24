"""Interview the user about an app, then build it with parallel agents in separate Orca worktrees.

    uv run examples/fullstack-agent-orchestration/main.py ~/src/newapp
    uv run examples/fullstack-agent-orchestration/main.py ~/src/newapp \\
        --answers examples/fullstack-agent-orchestration/answers.json --emit plan/
    uv run examples/fullstack-agent-orchestration/main.py ~/src/newapp \\
        --answers answers.json --max-agents 3 --integrate --apply

1. Interview: asks for the app idea, features, users and auth, stack and
   deployment target (or reads them from --answers), and turns them into a
   project brief, a shared API contract and five workstreams.
2. Setup: finds the repo in `repo list` (or registers it with `repo add`) and
   creates one worktree, on its own branch, per workstream.
3. Orchestration: launches one agent per worktree with AsyncOrca, at most
   --max-agents at a time, and watches every terminal concurrently until each
   goes idle (`terminal wait --for tui-idle`), exits, fails or times out.
4. Integration (--integrate): one more worktree and agent merges the finished
   branches, reconciles them against the contract and runs the tests.

Without --apply this is a dry run: it only reads (`status`, `repo list`,
`worktree list`) and prints the plan plus every SDK call and CLI command it
would make.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import re
import shlex
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from orca_sdk import AsyncOrca, OrcaCommandError, OrcaError, OrcaTimeoutError

QUESTIONS = [
    ("name", "App name", None),
    ("idea", "What does the app do, in a sentence or two?", None),
    ("features", "Core features (one per line, empty line to finish)", None),
    (
        "users_auth",
        "Who are the users, and how do they sign in?",
        "Email and password with JWT bearer tokens",
    ),
    ("entities", "Main data entities as `name: field, field` (one per line, empty line to finish)", None),
    ("frontend", "Frontend stack", "React + TypeScript + Vite"),
    ("backend", "Backend stack", "Python FastAPI"),
    ("database", "Database", "PostgreSQL"),
    ("deployment", "Deployment target", "Docker on Fly.io, GitHub Actions for CI"),
]
LIST_KEYS = {"features", "entities"}
REQUIRED = {"name", "idea", "features"}

# key, title, directories it owns, what it does
WORKSTREAMS = [
    (
        "database",
        "Database & schema",
        ["db/"],
        "Design the schema for every entity in the contract, write migrations and seed data, "
        "and document how to start the database locally.",
    ),
    (
        "backend",
        "Backend API",
        ["backend/"],
        "Implement every endpoint in the contract exactly as specified (paths, payloads, status codes, "
        "error envelope, auth), with unit tests for each route.",
    ),
    (
        "frontend",
        "Frontend UI",
        ["frontend/"],
        "Build the UI for every feature against the contract. Put all HTTP calls in one typed API client "
        "module and read the base URL from API_BASE_URL. Mock the API in component tests.",
    ),
    (
        "tests-ci",
        "Tests & CI",
        ["tests/", ".github/"],
        "Write end-to-end and contract tests that exercise the API as specified, and a CI workflow that "
        "lints, builds and tests the backend and frontend and runs the migrations.",
    ),
    (
        "docs",
        "Docs",
        ["docs/", "README.md"],
        "Write the README (what it is, how to run it locally, how to deploy), docs/architecture.md, "
        "and docs/api.md generated from the contract, plus the deployment guide for the target.",
    ),
]


@dataclass
class Workstream:
    key: str
    title: str
    owns: list[str]
    task: str
    worktree_name: str
    prompt: str = ""
    worktree_id: str | None = None
    branch: str | None = None
    path: str | None = None
    handle: str | None = None
    state: str = "pending"
    detail: str = ""
    last_line: str = ""
    started: float | None = None
    finished: float | None = None

    @property
    def done(self) -> bool:
        return self.state in ("idle", "exited", "failed", "timeout")

    @property
    def elapsed(self) -> str:
        if self.started is None:
            return "-"
        seconds = int((self.finished or time.monotonic()) - self.started)
        return f"{seconds // 60}m{seconds % 60:02d}s"


@dataclass
class SdkCall:
    """One SDK call, renderable as Python and as the equivalent `orca` command."""

    method: str
    kwargs: dict[str, Any]
    prompt_file: str | None = None

    def python(self) -> str:
        parts = []
        for key, value in self.kwargs.items():
            if key == "prompt":
                value = f"<{self.prompt_file or 'prompt'}, {len(value)} chars>"
                parts.append(f"{key}={value}")
            elif value is not None:
                parts.append(f"{key}={value!r}")
        return f"orca.{self.method}({', '.join(parts)})"

    def shell(self) -> str:
        argv = ["orca", *self.method.split(".")]
        for key, value in self.kwargs.items():
            flag = "--" + key.rstrip("_").replace("_", "-")
            if value is None or value is False:
                continue
            if value is True:
                argv.append(flag)
            elif key == "prompt":
                source = f'"$(cat {shlex.quote(self.prompt_file)})"' if self.prompt_file else "<prompt>"
                argv += [flag, source]
            else:
                argv += [flag, shlex.quote(str(value))]
        return " ".join(argv + ["--json"])


# --- 1. interview ----------------------------------------------------------


def interview() -> dict[str, Any]:
    print("Tell me about the app. Press Enter to accept a [default].\n")
    answers: dict[str, Any] = {}
    for key, question, default in QUESTIONS:
        if key in LIST_KEYS:
            print(f"{question}:")
            items = []
            while line := input("  - ").strip():
                items.append(line)
            answers[key] = items
            continue
        suffix = f" [{default}]" if default else ""
        while True:
            answer = input(f"{question}{suffix}: ").strip() or (default or "")
            if answer or key not in REQUIRED:
                break
        answers[key] = answer
    return answers


def load_answers(path: Path) -> dict[str, Any]:
    answers = json.loads(path.read_text())
    for key, _question, default in QUESTIONS:
        answers.setdefault(key, [] if key in LIST_KEYS else default or "")
    missing = [key for key in sorted(REQUIRED) if not answers.get(key)]
    if missing:
        raise SystemExit(f"{path}: missing {', '.join(missing)}")
    return answers


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or "app"


def plural(name: str) -> str:
    if name.endswith("y") and name[-2:-1] not in "aeiou":
        return name[:-1] + "ies"
    return name if name.endswith("s") else name + "s"


def field_type(name: str) -> str:
    if name.endswith(("_at", "_date")):
        return "string (ISO 8601)"
    if name == "id" or name.endswith("_id"):
        return "string (id)"
    if name.startswith(("is_", "has_")) or name in ("done", "enabled", "active"):
        return "boolean"
    if name.endswith(("_count", "count", "quantity", "amount")):
        return "number"
    return "string"


def parse_entities(raw: list[Any]) -> list[tuple[str, dict[str, str]]]:
    """Accept `"task: title, due_date"` strings or `{"name": ..., "fields": {...}}` objects."""
    entities = []
    for item in raw:
        if isinstance(item, dict):
            fields = item.get("fields") or {}
            if isinstance(fields, list):
                fields = {f: field_type(f) for f in fields}
            entities.append((slug(item["name"]).replace("-", "_"), dict(fields)))
            continue
        name, _, rest = str(item).partition(":")
        names = [f.strip().replace(" ", "_") for f in rest.split(",") if f.strip()]
        entities.append((slug(name).replace("-", "_"), {f: field_type(f) for f in names}))
    return entities


def build_brief(answers: dict[str, Any]) -> str:
    features = "\n".join(f"- {f}" for f in answers["features"])
    return f"""# {answers["name"]}: project brief

## Idea
{answers["idea"]}

## Core features
{features}

## Users and auth
{answers["users_auth"] or "No authentication."}

## Stack
| Layer | Choice |
| --- | --- |
| Frontend | {answers["frontend"]} |
| Backend | {answers["backend"]} |
| Database | {answers["database"]} |
| Deployment | {answers["deployment"]} |

## Repository layout
`db/` schema and migrations, `backend/` API server, `frontend/` web app,
`tests/` end-to-end and contract tests, `.github/` CI, `docs/` documentation.
Each workstream owns its directories; nobody edits another workstream's files.
"""


def build_contract(answers: dict[str, Any]) -> str:
    out = [
        "# Shared API contract",
        "",
        "Every workstream builds against this contract. Do not change it on your own: if you need a",
        "change, write it to CONTRACT_CHANGES.md in your branch and the integrator will reconcile it.",
        "",
        "- Base URL: `/api/v1`; the backend listens on port 8000; the frontend reads `API_BASE_URL`.",
        "- JSON everywhere, `snake_case` fields, ids are strings, timestamps are ISO 8601 UTC.",
        "- Lists: `GET ?limit=50&cursor=<c>` returns `{items: [...], next_cursor: string | null}`.",
        '- Errors: non-2xx with `{"error": {"code": "not_found", "message": "..."}}`; '
        "codes `validation_error` (422), `unauthorized` (401), `forbidden` (403), `not_found` (404).",
        "",
    ]
    auth = (answers.get("users_auth") or "").lower()
    if auth and not re.search(r"\b(no auth|none|anonymous)\b", auth):
        out += [
            "## Auth",
            "",
            "Send `Authorization: Bearer <access_token>` on every request except register and login.",
            "",
            "| Method | Path | Body | Response |",
            "| --- | --- | --- | --- |",
            "| POST | /auth/register | `{email, password, name}` | 201 `{user, access_token}` |",
            "| POST | /auth/login | `{email, password}` | 200 `{user, access_token}` |",
            "| GET | /auth/me | - | 200 `user` |",
            "",
            "`user`: `{id, email, name, created_at}`",
            "",
        ]
    for name, fields in parse_entities(answers.get("entities") or []):
        path = f"/{plural(name)}"
        out += [f"## {name}", ""]
        out += [f"- `{f}`: {t}" for f, t in {"id": "string (id)", **fields}.items()]
        out += [
            "",
            "| Method | Path | Body | Response |",
            "| --- | --- | --- | --- |",
            f"| GET | {path} | - | 200 list of `{name}` |",
            f"| POST | {path} | `{name}` without `id` | 201 `{name}` |",
            f"| GET | {path}/{{id}} | - | 200 `{name}` |",
            f"| PATCH | {path}/{{id}} | any `{name}` fields | 200 `{name}` |",
            f"| DELETE | {path}/{{id}} | - | 204 |",
            "",
        ]
    return "\n".join(out)


def role_prompt(ws: Workstream, brief: str, contract: str, others: list[Workstream]) -> str:
    owned = ", ".join(f"`{d}`" for d in ws.owns)
    peers = "\n".join(f"  - {o.title}: owns {', '.join(o.owns)}" for o in others if o is not ws)
    return f"""You are the {ws.title} engineer on a team of agents building the app below in parallel.
Each agent works in its own git worktree on its own branch; an integrator merges the branches later.

Your job: {ws.task}

Rules:
- Only create or edit files under {owned}. The other workstreams own:
{peers}
- Build against the shared API contract exactly. If it is wrong or missing something, do not
  work around it silently: describe the change in CONTRACT_CHANGES.md at the repo root (the one
  shared file) and carry on.
- Commit your work to your current branch with clear messages. Do not push, merge or rebase.
- When you are done, print a short summary of what you built and how to run or test it.

{brief}
{contract}
"""


def make_integrator(prefix: str, finished: list[Workstream], brief: str, contract: str) -> Workstream:
    integrator = Workstream("integration", "Integrator", ["*"], "", f"{prefix}-integration")
    integrator.prompt = integrator_prompt(finished, brief, contract)
    return integrator


def integrator_prompt(finished: list[Workstream], brief: str, contract: str) -> str:
    # Before setup the branch is unknown; Orca names it after the worktree.
    branches = "\n".join(f"- `{ws.branch or ws.worktree_name}` ({ws.title})" for ws in finished)
    return f"""You are the integrator. Other agents built parts of the app below on separate branches
of this repository. Merge them into your current branch, in this order:
{branches}

Then:
- Resolve conflicts, and reconcile every CONTRACT_CHANGES.md with the contract: update the
  contract and both the backend and frontend so they agree.
- Install dependencies, run the migrations, the backend tests, the frontend tests and the
  end-to-end tests. Fix what fails.
- Commit the result to your current branch. Do not push.
- Write INTEGRATION.md: what was merged, what you changed, test results, anything left to do.

{brief}
{contract}
"""


def build_plan(answers: dict[str, Any], prefix: str) -> tuple[str, str, list[Workstream]]:
    brief, contract = build_brief(answers), build_contract(answers)
    streams = [
        Workstream(key, title, owns, task, f"{prefix}-{key}") for key, title, owns, task in WORKSTREAMS
    ]
    for ws in streams:
        ws.prompt = role_prompt(ws, brief, contract, streams)
    return brief, contract, streams


def emit(directory: Path, brief: str, contract: str, streams: list[Workstream]) -> None:
    (directory / "prompts").mkdir(parents=True, exist_ok=True)
    (directory / "brief.md").write_text(brief)
    (directory / "contract.md").write_text(contract)
    for ws in streams:
        (directory / "prompts" / f"{ws.key}.md").write_text(ws.prompt)
    print(f"Wrote brief.md, contract.md and prompts/*.md to {directory}")


# --- 2. setup --------------------------------------------------------------


async def find_repo(orca: AsyncOrca, path: Path) -> dict[str, Any] | None:
    for repo in (await orca.repo.list())["repos"]:
        if Path(repo["path"]).resolve() == path:
            return repo
    return None


async def ensure_repo(orca: AsyncOrca, path: Path, repo: dict[str, Any] | None) -> str:
    """Return the repo selector, registering the path with `repo add` if needed."""
    if repo is None:
        added = await orca.repo.add(path=str(path))
        repo = added.get("repo", added) if isinstance(added, dict) else None
        if not repo or "id" not in repo:
            repo = await find_repo(orca, path)
        if repo is None:
            raise SystemExit("repo add succeeded but the repo is not in `repo list`")
        print(f"Registered {path} as {repo['id']}")
    return f"id:{repo['id']}"


async def create_worktrees(orca: AsyncOrca, repo_selector: str, streams: list[Workstream], args) -> None:
    existing = {wt["displayName"]: wt for wt in (await orca.worktree.list(repo=repo_selector))["worktrees"]}
    # One at a time: concurrent `git worktree add` on one repo contend for the same lock.
    for ws in streams:
        if ws.worktree_name in existing:
            wt = existing[ws.worktree_name]
            print(f"  reusing worktree {ws.worktree_name}")
        else:
            created = await orca.worktree.create(**create_call(repo_selector, ws, args).kwargs)
            wt = created.get("worktree", created)
            print(f"  created worktree {ws.worktree_name} at {wt.get('path')}")
        ws.worktree_id, ws.path = wt.get("id"), wt.get("path")
        ws.branch = (wt.get("branch") or "").removeprefix("refs/heads/") or ws.worktree_name


# --- 3. orchestration ------------------------------------------------------


def create_call(repo_selector: str, ws: Workstream, args: argparse.Namespace) -> SdkCall:
    return SdkCall(
        "worktree.create",
        {"repo": repo_selector, "name": ws.worktree_name, "no_parent": True, "base_branch": args.base_branch},
    )


def launch_call(ws: Workstream, args: argparse.Namespace) -> SdkCall:
    worktree = f"id:{ws.worktree_id}" if ws.worktree_id else f"id:<id of {ws.worktree_name}>"
    prompt_file = str(Path(args.emit) / "prompts" / f"{ws.key}.md") if args.emit else None
    return SdkCall(
        "agent.launch",
        {
            "agent": args.agent,
            "worktree": worktree,
            "prompt": ws.prompt,
            "model": args.model,
            "surface": "terminal",
        },
        prompt_file=prompt_file,
    )


async def run_agent(orca: AsyncOrca, sem: asyncio.Semaphore, ws: Workstream, args) -> None:
    async with sem:
        ws.state = "launching"
        try:
            launched = await orca.agent.launch(**launch_call(ws, args).kwargs)
        except OrcaError as err:
            ws.state, ws.detail = "failed", f"launch failed: {err}"
            return
        outcome = launched.get("outcome") or {}
        ws.handle = outcome.get("handle")
        if not ws.handle or outcome.get("kind", "terminal") != "terminal":
            ws.state, ws.detail = "failed", f"no terminal handle in launch result: {outcome}"
            return
        ws.state, ws.started = "working", time.monotonic()
        await watch(orca, ws, args)
        ws.finished = time.monotonic()


async def watch(orca: AsyncOrca, ws: Workstream, args) -> None:
    """Wait for tui-idle in --poll sized slices, checking the terminal between slices."""
    # A freshly launched TUI can look idle before it picks up the prompt.
    await asyncio.sleep(args.settle)
    waiter = orca.with_options(timeout=args.poll + 30)
    deadline = (ws.started or time.monotonic()) + args.agent_timeout
    while True:
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            ws.state, ws.detail = "timeout", f"not idle after {args.agent_timeout:g}s"
            return
        try:
            slice_ms = int(max(1.0, min(args.poll, remaining)) * 1000)
            result = await waiter.terminal.wait(terminal=ws.handle, for_="tui-idle", timeout_ms=slice_ms)
            if not isinstance(result, dict) or result.get("satisfied", True):
                ws.state = "idle"
                return
        except OrcaTimeoutError:
            pass
        except OrcaCommandError as err:
            if "timeout" not in err.code.lower() and "timed out" not in err.message.lower():
                ws.state, ws.detail = "failed", str(err)
                return
        try:
            read = (await orca.terminal.read(terminal=ws.handle, limit=20))["terminal"]
        except OrcaError as err:
            ws.state, ws.detail = "failed", f"terminal read failed: {err}"
            return
        lines = [line.strip() for line in read.get("tail") or [] if line.strip()]
        ws.last_line = lines[-1][:80] if lines else ws.last_line
        if read.get("status") not in (None, "running"):
            ws.state, ws.detail = "exited", f"terminal {read.get('status')}"
            return


async def dashboard(streams: list[Workstream], every: float, stop: asyncio.Event) -> None:
    while not stop.is_set():
        print_board(streams)
        try:
            await asyncio.wait_for(stop.wait(), timeout=every)
        except asyncio.TimeoutError:
            pass


def print_board(streams: list[Workstream]) -> None:
    print(f"\n[{time.strftime('%H:%M:%S')}] agents:")
    for ws in streams:
        print(f"  {ws.key:<12} {ws.state:<10} {ws.elapsed:>7}  {ws.handle or '-':<12} {ws.last_line}")


async def orchestrate(orca: AsyncOrca, streams: list[Workstream], args) -> None:
    sem = asyncio.Semaphore(args.max_agents)
    stop = asyncio.Event()
    board = asyncio.create_task(dashboard(streams, args.status_every, stop))
    try:
        await asyncio.gather(*(run_agent(orca, sem, ws, args) for ws in streams))
    finally:
        stop.set()
        await board


# --- dry run, summary, main ------------------------------------------------


def print_plan(brief: str, streams: list[Workstream], args) -> None:
    print(brief)
    print("Workstreams:")
    for ws in streams:
        print(f"  {ws.key:<10} {ws.worktree_name:<28} owns {', '.join(ws.owns)}")
    print(
        f"\nAgent: {args.agent}, at most {args.max_agents} running at once, "
        f"each given up to {args.agent_timeout:g}s to reach tui-idle."
    )


def print_calls(title: str, calls: list[SdkCall]) -> None:
    print(f"\n{title}")
    for call in calls:
        print(f"  {call.python()}")
        print(f"    $ {call.shell()}")


def print_summary(streams: list[Workstream]) -> None:
    print("\nSummary:")
    print(f"  {'workstream':<12} {'result':<9} {'time':>7}  {'branch':<30} path")
    for ws in streams:
        print(f"  {ws.key:<12} {ws.state:<9} {ws.elapsed:>7}  {ws.branch or '-':<30} {ws.path or '-'}")
        if ws.detail:
            print(f"    {ws.detail}")


async def run(args: argparse.Namespace, answers: dict[str, Any]) -> int:
    path = Path(args.repo).expanduser().resolve()
    prefix = args.prefix or slug(answers["name"])
    brief, contract, streams = build_plan(answers, prefix)
    if args.emit:
        # The integrator prompt written here assumes every workstream finishes.
        extra = [make_integrator(prefix, streams, brief, contract)] if args.integrate else []
        emit(Path(args.emit), brief, contract, [*streams, *extra])

    async with AsyncOrca(timeout=args.timeout) as orca:
        status, repo = await asyncio.gather(orca.status(), find_repo(orca, path))
        runtime = status.get("runtime") or {}
        print(f"Orca runtime {runtime.get('state')} v{runtime.get('appVersion')}")
        existing: set[str] = set()
        if repo is None:
            print(f"{path} is not registered with Orca yet.")
        else:
            print(f"{path} is registered as {repo['displayName']!r} (id {repo['id']}).")
            rows = (await orca.worktree.list(repo=f"id:{repo['id']}"))["worktrees"]
            existing = {wt["displayName"] for wt in rows}

        if not args.apply:
            print_plan(brief, streams, args)
            repo_selector = f"id:{repo['id']}" if repo else "id:<new repo id>"
            setup_calls = [] if repo else [SdkCall("repo.add", {"path": str(path)})]
            for ws in streams:
                if ws.worktree_name in existing:
                    print(f"  note: worktree {ws.worktree_name} exists and would be reused")
                    continue
                setup_calls.append(create_call(repo_selector, ws, args))
            print_calls("Setup (one at a time):", setup_calls)
            print_calls(
                f"Agents (concurrently, max {args.max_agents}):", [launch_call(ws, args) for ws in streams]
            )
            wait = SdkCall(
                "terminal.wait",
                {"terminal": "<handle>", "for_": "tui-idle", "timeout_ms": int(args.poll * 1000)},
            )
            read = SdkCall("terminal.read", {"terminal": "<handle>", "limit": 20})
            print_calls("Monitoring, per agent, until idle or --agent-timeout:", [wait, read])
            if args.integrate:
                integrator = make_integrator(prefix, streams, brief, contract)
                calls = [create_call(repo_selector, integrator, args), launch_call(integrator, args)]
                print_calls("Integration, after every agent is idle (merging the idle branches):", calls)
            if not args.emit:
                print("\nPass --emit DIR to write the prompts out and get copy-pasteable commands.")
            print("\ndry run: nothing was created or launched. Re-run with --apply to do it.")
            return 0

        print("\nSetting up worktrees:")
        repo_selector = await ensure_repo(orca, path, repo)
        await create_worktrees(orca, repo_selector, streams, args)
        print(f"\nLaunching {len(streams)} agents ({args.agent}), at most {args.max_agents} at a time:")
        await orchestrate(orca, streams, args)

        finished = [ws for ws in streams if ws.state == "idle"]
        if args.integrate:
            if not finished:
                print("\nNo workstream finished; skipping integration.")
            else:
                integrator = make_integrator(prefix, finished, brief, contract)
                print(f"\nIntegrating {len(finished)} branches:")
                await create_worktrees(orca, repo_selector, [integrator], args)
                await orchestrate(orca, [integrator], args)
                streams = [*streams, integrator]

    print_summary(streams)
    return 0 if all(ws.state == "idle" for ws in streams) else 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("repo", nargs="?", default=".", help="target git repo (default: current directory)")
    parser.add_argument("--answers", type=Path, help="JSON file with interview answers (non-interactive)")
    parser.add_argument("--agent", default="claude", help="agent id for every workstream (default: claude)")
    parser.add_argument("--model", help="provider model id for the agents (optional)")
    parser.add_argument("--prefix", help="worktree name prefix (default: slug of the app name)")
    parser.add_argument("--base-branch", help="base ref for the worktrees (default: repo default base)")
    parser.add_argument("--max-agents", type=int, default=3, help="agents running at once (default: 3)")
    parser.add_argument(
        "--agent-timeout", type=float, default=3600, metavar="SECONDS", help="per-agent limit (default: 3600)"
    )
    parser.add_argument("--poll", type=float, default=60, metavar="SECONDS", help="tui-idle wait slice")
    parser.add_argument("--settle", type=float, default=20, metavar="SECONDS", help="grace after launch")
    parser.add_argument(
        "--status-every", type=float, default=30, metavar="SECONDS", help="dashboard interval"
    )
    parser.add_argument("--timeout", type=float, default=60, help="per-command timeout in seconds")
    parser.add_argument("--emit", metavar="DIR", help="write brief.md, contract.md and prompts/*.md here")
    parser.add_argument("--integrate", action="store_true", help="merge and test with an integrator agent")
    parser.add_argument("--apply", action="store_true", help="actually create worktrees and launch agents")
    args = parser.parse_args(argv)
    if args.max_agents < 1:
        parser.error("--max-agents must be at least 1")

    if args.answers:
        answers = load_answers(args.answers)
    elif sys.stdin.isatty():
        answers = interview()
        missing = [key for key in sorted(REQUIRED) if not answers.get(key)]
        if missing:
            parser.error(f"missing answers: {', '.join(missing)}")
    else:
        parser.error("stdin is not a terminal; pass --answers FILE")
    return asyncio.run(run(args, answers))


if __name__ == "__main__":
    raise SystemExit(main())
