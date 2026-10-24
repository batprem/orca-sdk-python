"""Launch an agent (e.g. claude) in a worktree with a prompt and follow its terminal output.

    uv run examples/launch-agent-follow-output/main.py --worktree path:$PWD
    uv run examples/launch-agent-follow-output/main.py --worktree path:$PWD \\
        --agent claude --prompt "Summarise the README" --apply

Without --apply this is read-only: it shows the target worktree, its live
terminals and the last lines of the most recent one, and prints the launch it
would make. With --apply it runs `agent launch --surface terminal`, then tails
the new terminal with `terminal read --cursor` and waits for the agent to go
idle with `terminal wait --for tui-idle`.
"""

from __future__ import annotations

import argparse
import time

from orca_sdk import Orca, OrcaCommandError, OrcaTimeoutError


def print_lines(lines: list[str]) -> None:
    for line in lines:
        print(f"  | {line}")


def follow(orca: Orca, handle: str, seconds: float, interval: float = 2.0) -> None:
    """Print new terminal output every ``interval`` seconds for ``seconds``."""
    cursor = None
    deadline = time.monotonic() + seconds
    while True:
        read = orca.terminal.read(terminal=handle, cursor=cursor, limit=200)["terminal"]
        print_lines(read.get("tail") or [])
        # nextCursor makes the next read return only output produced after this one.
        cursor = read.get("nextCursor", cursor)
        if read.get("status") != "running" or time.monotonic() >= deadline:
            return
        time.sleep(interval)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--worktree", default="active", help="worktree selector (default: active)")
    parser.add_argument("--agent", default="claude", help="agent id to launch (default: claude)")
    parser.add_argument("--prompt", default="Give me a one-paragraph overview of this repository.")
    parser.add_argument("--model", help="provider model id (optional)")
    parser.add_argument("--follow", type=float, default=60, metavar="SECONDS", help="how long to tail output")
    parser.add_argument(
        "--idle-timeout",
        type=float,
        default=300,
        metavar="SECONDS",
        help="how long to wait for the agent to go idle",
    )
    parser.add_argument("--apply", action="store_true", help="actually launch the agent")
    args = parser.parse_args(argv)

    orca = Orca()

    worktree = orca.worktree.show(worktree=args.worktree)["worktree"]
    print(f"Worktree {worktree['displayName']!r} at {worktree['path']}")

    terminals = orca.terminal.list(worktree=args.worktree)["terminals"]
    print(f"Live terminals: {len(terminals)}")
    for term in terminals:
        print(f"  {term['handle']}  agent={term.get('agentIdentity') or '-':<8} {term.get('title', '')}")
    if terminals:
        latest = max(terminals, key=lambda t: t.get("lastOutputAt") or 0)
        print(f"Last lines of {latest['handle']}:")
        print_lines(orca.terminal.read(terminal=latest["handle"], limit=10)["terminal"].get("tail") or [])

    if not args.apply:
        print(
            f"dry run: would call orca.agent.launch(agent={args.agent!r}, worktree={args.worktree!r}, "
            f"prompt={args.prompt!r}, model={args.model!r}, surface='terminal') and follow its output"
        )
        print("Re-run with --apply to launch.")
        return 0

    launched = orca.agent.launch(
        agent=args.agent,
        worktree=args.worktree,
        prompt=args.prompt,
        model=args.model,
        surface="terminal",
    )
    outcome = launched.get("outcome") or {}
    handle = outcome.get("handle")
    print(f"Launched {args.agent} as {outcome.get('kind')}: {handle}")
    print(f"  {(launched.get('receipt') or {}).get('detail', '')}")
    if not handle:
        return 1

    follow(orca, handle, args.follow)

    # Block until the agent's TUI goes idle (the CLI waits up to timeout_ms;
    # give the subprocess a little longer than that).
    try:
        orca.with_options(timeout=args.idle_timeout + 30).terminal.wait(
            terminal=handle, for_="tui-idle", timeout_ms=int(args.idle_timeout * 1000)
        )
        print("Agent is idle. Final screen:")
        print_lines(orca.terminal.read(terminal=handle, screen=True)["terminal"].get("tail") or [])
    except (OrcaCommandError, OrcaTimeoutError) as err:
        print(f"Agent still busy: {err}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
