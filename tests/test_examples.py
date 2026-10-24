"""Run every example under examples/ against a mocked orca subprocess.

The read-only paths must only issue read-only commands; the --apply paths are
exercised too, so the state-changing calls they build are checked without
touching a real Orca.
"""

from __future__ import annotations

import asyncio
import importlib.util
import json
import py_compile
import subprocess
from pathlib import Path
from types import ModuleType
from typing import Any

import pytest
from conftest import envelope

EXAMPLES_DIR = Path(__file__).resolve().parent.parent / "examples"
EXAMPLES = sorted(p.parent.name for p in EXAMPLES_DIR.glob("*/main.py"))

REPO_PATH = "/work/myapp"
REPO_ID = "repo-1"
AUTOMATION_ID = "497bafa9-5a97-4f85-9e48-2b211b8f31fa"

TERMINAL = {
    "handle": "term_1",
    "title": "claude task",
    "agentIdentity": "claude",
    "lastOutputAt": 1792836242000,
    "worktreeId": f"{REPO_ID}::{REPO_PATH}",
}
WORKTREE = {
    "id": f"{REPO_ID}::{REPO_PATH}",
    "repoId": REPO_ID,
    "hostId": "local",
    "path": REPO_PATH,
    "branch": "refs/heads/main",
    "displayName": "main",
    "isMainWorktree": True,
}
AUTOMATION = {
    "id": AUTOMATION_ID,
    "name": "Daily review",
    "prompt": "Review open changes",
    "agentId": "claude",
    "enabled": True,
    "rrule": "FREQ=DAILY;BYHOUR=9",
    "timezone": "UTC",
    "nextRunAt": 1792839600000,
    "lastRunAt": 1792836242791,
    "workspaceMode": "new",
}
RUN = {
    "id": "run-1",
    "automationId": AUTOMATION_ID,
    "runNumber": 3,
    "status": "completed",
    "trigger": "scheduled",
    "createdAt": 1792836230707,
    "outputSnapshot": {"format": "plain_text", "content": "All good.\nNothing changed."},
    "error": None,
}

RESPONSES: dict[str, Any] = {
    "status": {
        "target": {"kind": "local"},
        "app": {"running": True, "pid": 42},
        "runtime": {
            "state": "ready",
            "reachable": True,
            "appVersion": "1.4.237",
            "capabilities": ["agent.launch.v2"],
        },
        "graph": {"state": "ready"},
    },
    "host list": {
        "hosts": [{"kind": "local", "name": "this machine", "id": "local", "selector": "--host local"}]
    },
    "environment list": {"environments": []},
    "project list": {"projects": [{"id": f"repo:{REPO_ID}", "displayName": "myapp", "kind": "git"}]},
    "repo list": {"repos": [{"id": REPO_ID, "path": REPO_PATH, "displayName": "myapp", "kind": "git"}]},
    "worktree list": {"worktrees": [WORKTREE]},
    "worktree show": {"worktree": WORKTREE},
    "worktree ps": {
        "worktrees": [
            {
                "repo": "myapp",
                "displayName": "main",
                "status": "working",
                "agents": [{"agentType": "claude", "state": "working"}],
            }
        ],
        "totalCount": 1,
    },
    "terminal list": {"terminals": [TERMINAL]},
    "terminal read": {
        "terminal": {"handle": "term_1", "status": "running", "tail": ["hello", "world"], "nextCursor": "10"}
    },
    "terminal wait": {"satisfied": True},
    "automations list": {"automations": [AUTOMATION]},
    "automations show": {"automation": AUTOMATION},
    "automations runs": {"runs": [RUN], "nextCursor": None},
    "automations create": {"automation": {**AUTOMATION, "id": "new-auto"}},
    "automations run": {"run": {"id": "run-2", "status": "queued"}},
    "search": {
        "kind": "results",
        "hits": [
            {
                "agent": "claude",
                "sessionId": "s-1",
                "title": "Fix flaky test",
                "messageCount": 12,
                "score": 3.5,
                "evidence": {"snippet": "the [[flaky]] test", "role": "assistant"},
                "resumeCommand": "claude --resume s-1",
            }
        ],
        "page": {"cursor": "c1", "hasMore": False},
    },
    "skills installed": {
        "skills": [{"id": "a1", "name": "orca-cli", "providers": ["claude"], "sourceLabel": "user"}]
    },
    "agent launch": {
        "outcome": {"kind": "terminal", "handle": "term_2"},
        "receipt": {"detail": "terminal launch"},
    },
    "repo add": {"repo": {"id": "repo-2", "path": "/work/other"}},
    "worktree create": {
        "worktree": {"id": "repo-2::/work/other-wt", "displayName": "task", "path": "/work/other-wt"}
    },
}
SEARCH_INDEX = {"phase": "current", "messagesIndexed": 100, "sessionsByAgent": {"claude": 3}}

# `skills list/get/install` print bare JSON rather than the {ok, result} envelope.
BARE: dict[str, Any] = {
    "skills list": {"topics": [{"name": "orca-cli", "description": "Operate Orca."}]},
    "skills get": {"name": "orca-cli", "full": False, "markdown": "---\nname: orca-cli\n---\n# Orca CLI\n"},
}

READ_ONLY = {
    "status",
    "host list",
    "environment list",
    "project list",
    "repo list",
    "repo show",
    "worktree list",
    "worktree show",
    "worktree ps",
    "terminal list",
    "terminal read",
    "automations list",
    "automations show",
    "automations runs",
    "search",
    "skills list",
    "skills installed",
    "skills get",
    "skills install",  # only the listing and --dry-run; checked in is_read_only
}


def command_key(args: list[str]) -> str:
    if args[0] in ("status", "search"):
        return args[0]
    return " ".join(args[:2])


def is_read_only(args: list[str]) -> bool:
    key = command_key(args)
    if key == "skills install":
        return "--skill" not in args or "--dry-run" in args
    return key in READ_ONLY


def respond(args: list[str]) -> tuple[int, str]:
    """Return (returncode, stdout) for ``orca <args>``."""
    key = command_key(args)
    if key == "repo show":
        return 1, envelope(ok=False, error={"code": "repo_not_found", "message": "repo_not_found"})
    if key == "automations show" and AUTOMATION_ID not in args:
        return 1, envelope(ok=False, error={"code": "runtime_error", "message": "Automation not found."})
    if key == "worktree show" and REPO_PATH not in " ".join(args) and "active" not in args:
        return 1, envelope(ok=False, error={"code": "selector_not_found", "message": "selector_not_found"})
    if key == "search" and "--index-status" in args:
        return 0, envelope(SEARCH_INDEX)
    if key == "skills install":
        if "--dry-run" in args:
            return 0, json.dumps(
                {"command": "npx --yes skills@1.7.2 add ...", "skills": ["orca-cli"], "executed": False}
            )
        if "--json" in args:
            return 0, json.dumps({"availableSkills": ["orca-cli", "orchestration"]})
        return 0, "Installed orca-cli\n"
    if key in BARE:
        return 0, json.dumps(BARE[key])
    if key in RESPONSES:
        return 0, envelope(RESPONSES[key])
    raise AssertionError(f"unexpected orca command in example: {args}")


class FakeOrca:
    """Stands in for both subprocess.run and asyncio.create_subprocess_exec."""

    def __init__(self) -> None:
        self.calls: list[list[str]] = []

    def run(self, argv, **kwargs):
        args = list(argv[1:])
        self.calls.append(args)
        timeout = kwargs.get("timeout")
        if timeout is not None and timeout < 0.01:
            raise subprocess.TimeoutExpired(argv, timeout)
        code, out = respond(args)
        return subprocess.CompletedProcess(argv, code, out.encode(), b"")

    async def exec(self, *argv, **kwargs):
        args = list(argv[1:])
        self.calls.append(args)
        code, out = respond(args)
        return _FakeProcess(code, out)

    @property
    def commands(self) -> list[str]:
        return [command_key(args) for args in self.calls]

    def assert_read_only(self) -> None:
        changed = [args for args in self.calls if not is_read_only(args)]
        assert not changed, f"state-changing commands without --apply: {changed}"


class _FakeProcess:
    def __init__(self, returncode: int, stdout: str) -> None:
        self._rc = returncode
        self._out = stdout.encode()
        self.returncode: int | None = None

    async def communicate(self, data=None):
        await asyncio.sleep(0)
        self.returncode = self._rc
        return self._out, b""

    def kill(self) -> None:
        pass

    async def wait(self) -> int:
        return self._rc


@pytest.fixture
def fake_orca(monkeypatch: pytest.MonkeyPatch, fake_bin: Path) -> FakeOrca:
    fake = FakeOrca()
    monkeypatch.setenv("ORCA_BIN", str(fake_bin))
    monkeypatch.setattr("orca_sdk._client.subprocess.run", fake.run)
    monkeypatch.setattr("orca_sdk._async_client.asyncio.create_subprocess_exec", fake.exec)
    monkeypatch.setattr("time.sleep", lambda _s: None)
    return fake


def load(name: str) -> ModuleType:
    path = EXAMPLES_DIR / name / "main.py"
    spec = importlib.util.spec_from_file_location(f"example_{name.replace('-', '_')}", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_examples_exist():
    assert 6 <= len(EXAMPLES) <= 10
    for name in EXAMPLES:
        assert name == name.lower() and " " not in name and "_" not in name, name
        assert (EXAMPLES_DIR / name / "README.md").is_file(), name
    index = (EXAMPLES_DIR / "README.md").read_text()
    for name in EXAMPLES:
        assert f"({name}/)" in index, f"{name} missing from examples/README.md"


@pytest.mark.parametrize("name", EXAMPLES)
def test_example_compiles_and_imports(name):
    py_compile.compile(str(EXAMPLES_DIR / name / "main.py"), doraise=True)
    module = load(name)
    assert callable(module.main)
    assert module.__doc__


# (example, argv for the read-only run, commands that must have been issued)
READ_ONLY_RUNS = [
    ("check-status", [], ["status"]),
    ("check-status", ["--json"], ["status"]),
    (
        "list-hosts-and-projects",
        [],
        ["host list", "environment list", "project list", "repo list", "worktree list"],
    ),
    ("register-repo-worktree", [REPO_PATH, "--name", "task"], ["repo list", "worktree list"]),
    ("register-repo-worktree", ["/work/unregistered", "--name", "task"], ["repo list"]),
    (
        "launch-agent-follow-output",
        ["--worktree", f"path:{REPO_PATH}"],
        ["worktree show", "terminal list", "terminal read"],
    ),
    ("manage-automations", [], ["automations list", "automations runs"]),
    ("manage-automations", ["--show", AUTOMATION_ID], ["automations show", "automations runs"]),
    (
        "manage-automations",
        ["--create", "Nightly", "--prompt", "Tidy", "--run", AUTOMATION_ID],
        ["automations list", "automations runs"],
    ),
    ("search-agent-sessions", ["flaky test", "--agent", "claude", "--pages", "2"], ["search", "search"]),
    ("manage-skills", [], ["skills list", "skills installed", "skills get", "skills install"]),
    ("manage-skills", ["--install", "orca-cli"], ["skills install", "skills install"]),
    (
        "async-concurrent-dashboard",
        [],
        ["status", "host list", "project list", "repo list", "worktree ps", "terminal list", "terminal read"],
    ),
    ("error-handling", [], ["repo show", "automations show", "status", "host list", "worktree show"]),
]


@pytest.mark.parametrize(("name", "argv", "expected"), READ_ONLY_RUNS)
def test_read_only_path(name, argv, expected, fake_orca, capsys):
    assert load(name).main(argv) == 0
    out = capsys.readouterr().out
    assert out.strip()
    for command in expected:
        assert command in fake_orca.commands, f"{name} did not run `orca {command}`"
    fake_orca.assert_read_only()
    if "dry run" in out:
        assert "--apply" in out


def test_every_example_has_a_read_only_run():
    assert {name for name, _, _ in READ_ONLY_RUNS} == set(EXAMPLES)


def test_check_status_not_ready_exit_code(fake_orca, monkeypatch):
    status = {**RESPONSES["status"], "graph": {"state": "starting"}}
    monkeypatch.setitem(RESPONSES, "status", status)
    assert load("check-status").main([]) == 1


def test_error_handling_reports_each_failure(fake_orca, capsys):
    load("error-handling").main([])
    out = capsys.readouterr().out
    assert "code='repo_not_found'" in out
    assert "ok=False" in out
    assert "timed out" in out
    assert "runtime state: ready" in out
    assert "searched:" in out
    assert "only runs on the local host" in out
    assert "OrcaCommandError: [selector_not_found]" in out


# --apply paths, against the mock only.


def test_register_repo_worktree_apply(fake_orca):
    assert load("register-repo-worktree").main(["/work/other", "--name", "task", "--apply"]) == 0
    assert fake_orca.commands[-2:] == ["repo add", "worktree create"]
    assert fake_orca.calls[-2][:4] == ["repo", "add", "--path", "/work/other"]
    assert fake_orca.calls[-1] == [
        "worktree",
        "create",
        "--repo",
        "id:repo-2",
        "--name",
        "task",
        "--no-parent",
        "--json",
    ]


def test_launch_agent_apply(fake_orca):
    argv = [
        "--worktree",
        f"path:{REPO_PATH}",
        "--prompt",
        "hi",
        "--follow",
        "0",
        "--idle-timeout",
        "5",
        "--apply",
    ]
    assert load("launch-agent-follow-output").main(argv) == 0
    launch = next(args for args in fake_orca.calls if args[:2] == ["agent", "launch"])
    assert launch[2:] == [
        "--agent",
        "claude",
        "--worktree",
        f"path:{REPO_PATH}",
        "--prompt",
        "hi",
        "--surface",
        "terminal",
        "--json",
    ]
    wait = ["terminal", "wait", "--terminal", "term_2", "--for", "tui-idle", "--timeout-ms", "5000", "--json"]
    assert wait in fake_orca.calls
    assert any(args[:4] == ["terminal", "read", "--terminal", "term_2"] for args in fake_orca.calls)


def test_manage_automations_apply(fake_orca):
    argv = [
        "--create",
        "Nightly",
        "--prompt",
        "Tidy",
        "--trigger",
        "0 2 * * *",
        "--run",
        AUTOMATION_ID,
        "--apply",
    ]
    assert load("manage-automations").main(argv) == 0
    create = next(args for args in fake_orca.calls if args[:2] == ["automations", "create"])
    assert create[2:] == [
        "--name",
        "Nightly",
        "--prompt",
        "Tidy",
        "--provider",
        "claude",
        "--trigger",
        "0 2 * * *",
        "--json",
    ]
    assert ["automations", "run", AUTOMATION_ID, "--json"] in fake_orca.calls


def test_manage_skills_apply(fake_orca):
    assert load("manage-skills").main(["--install", "orca-cli", "--agent", "claude-code", "--apply"]) == 0
    assert fake_orca.calls[-1] == ["skills", "install", "--skill", "orca-cli", "--agent", "claude-code"]


def test_manage_skills_rejects_unknown_skill(fake_orca):
    with pytest.raises(SystemExit):
        load("manage-skills").main(["--install", "not-a-skill"])
