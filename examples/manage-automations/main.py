"""Manage scheduled automations: list them, inspect one, read run history, create or run one.

    uv run examples/manage-automations/main.py
    uv run examples/manage-automations/main.py --show <automation-id>
    uv run examples/manage-automations/main.py --create "Daily review" --trigger daily \\
        --prompt "Review open changes" --provider claude --repo name:myapp --apply
    uv run examples/manage-automations/main.py --run <automation-id> --apply

Read-only by default (`automations list`, `show`, `runs`). `--create` and
`--run` only print what they would do unless --apply is given.
"""

from __future__ import annotations

import argparse
from datetime import datetime
from typing import Any

from orca_sdk import Orca


def when(ms: int | None) -> str:
    return datetime.fromtimestamp(ms / 1000).strftime("%Y-%m-%d %H:%M") if ms else "-"


def print_runs(runs: list[dict[str, Any]]) -> None:
    for run in runs:
        print(
            f"  #{run.get('runNumber', '?'):<5} {run['status']:<10} {run['trigger']:<10} {when(run.get('createdAt'))}"
        )
        snapshot = (run.get("outputSnapshot") or {}).get("content") or ""
        if snapshot:
            print(f"         {snapshot.strip().splitlines()[0][:100]}")
        if run.get("error"):
            print(f"         error: {run['error']}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--show", metavar="ID", help="show one automation and its recent runs")
    parser.add_argument("--runs", type=int, default=5, help="how many recent runs to list (default 5)")
    parser.add_argument("--create", metavar="NAME", help="create an automation with this name")
    parser.add_argument("--trigger", default="daily", help="hourly|daily|weekdays|weekly|cron|RRULE")
    parser.add_argument("--prompt", help="prompt for the new automation")
    parser.add_argument("--provider", default="claude", help="agent that runs it (default claude)")
    parser.add_argument("--repo", help="repo selector to run in (default: the enclosing worktree's repo)")
    parser.add_argument("--run", metavar="ID", help="run an automation now (full UUID)")
    parser.add_argument("--apply", action="store_true", help="actually create / run")
    args = parser.parse_args(argv)

    orca = Orca()

    automations = orca.automations.list()["automations"]
    print(f"Automations: {len(automations)}")
    for auto in automations:
        state = "on " if auto.get("enabled") else "off"
        print(
            f"  [{state}] {auto['id']}  {auto['name']:<32} agent={auto.get('agentId'):<7} "
            f"{auto.get('rrule', '')}  next={when(auto.get('nextRunAt'))}"
        )

    if args.show:
        auto = orca.automations.show(args.show)
        auto = auto.get("automation", auto)
        print(f"\n{auto['name']} ({auto['id']})")
        print(f"  prompt:    {auto.get('prompt')}")
        print(f"  workspace: {auto.get('workspaceMode')} {auto.get('workspaceId') or ''}")
        print(f"  schedule:  {auto.get('rrule')} ({auto.get('timezone')})")
        print(f"  last run:  {when(auto.get('lastRunAt'))}")
        print(f"Recent runs of {auto['name']}:")
        print_runs(orca.automations.runs(id=args.show, limit=args.runs)["runs"])
    else:
        print(f"\nLatest {args.runs} runs across all automations:")
        print_runs(orca.automations.runs(limit=args.runs)["runs"])

    if args.create:
        if not args.prompt:
            parser.error("--create needs --prompt")
        kwargs = {
            "name": args.create,
            "trigger": args.trigger,
            "prompt": args.prompt,
            "provider": args.provider,
        }
        if args.repo:
            kwargs["repo"] = args.repo
        if not args.apply:
            print(f"\ndry run: would call orca.automations.create({kwargs})")
        else:
            created = orca.automations.create(**kwargs)
            created = created.get("automation", created)
            print(f"\nCreated automation {created.get('id')} ({created.get('name')})")

    if args.run:
        if not args.apply:
            print(f"\ndry run: would call orca.automations.run({args.run!r})")
        else:
            started = orca.automations.run(args.run)
            print(f"\nQueued run: {started}")
            print(f"Follow it with: orca.automations.runs(id={args.run!r}, limit=1)")

    if (args.create or args.run) and not args.apply:
        print("Re-run with --apply to make these changes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
