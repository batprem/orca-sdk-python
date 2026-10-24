"""Build a one-screen Orca dashboard by running many CLI calls concurrently with AsyncOrca.

    uv run examples/async-concurrent-dashboard/main.py
    uv run examples/async-concurrent-dashboard/main.py --terminals 5 --concurrency 3

Read-only. Fires `status`, `host list`, `project list`, `repo list`,
`worktree ps`, `automations list`, `skills installed` and
`search --index-status` at once with asyncio.gather, then reads the tail of the
busiest terminals with a semaphore capping how many CLI processes run at a time.
"""

from __future__ import annotations

import argparse
import asyncio
import time
from typing import Any

from orca_sdk import AsyncOrca, OrcaError


async def tail(orca: AsyncOrca, sem: asyncio.Semaphore, handle: str) -> list[str]:
    async with sem:
        read = await orca.terminal.read(terminal=handle, limit=3)
    return [line for line in read["terminal"].get("tail") or [] if line.strip()]


async def run(args: argparse.Namespace) -> int:
    async with AsyncOrca(timeout=args.timeout) as orca:
        started = time.perf_counter()
        calls = {
            "status": orca.status(),
            "hosts": orca.host.list(),
            "projects": orca.project.list(),
            "repos": orca.repo.list(),
            "ps": orca.worktree.ps(limit=args.worktrees),
            "automations": orca.automations.list(),
            "skills": orca.skills.installed(),
            "index": orca.search(index_status=True),
        }
        # return_exceptions keeps one failing command from sinking the dashboard.
        results = await asyncio.gather(*calls.values(), return_exceptions=True)
        data: dict[str, Any] = dict(zip(calls, results))
        elapsed = time.perf_counter() - started

        for name, value in data.items():
            if isinstance(value, OrcaError):
                print(f"! {name} failed: {value}")
                data[name] = {}
            elif isinstance(value, BaseException):
                raise value

        status = data["status"]
        runtime = status.get("runtime") or {}
        print(f"{len(calls)} commands in {elapsed:.2f}s (concurrently)\n")
        print(
            f"runtime   {runtime.get('state')} v{runtime.get('appVersion')}, graph {status.get('graph', {}).get('state')}"
        )
        print(f"hosts     {len(data['hosts'].get('hosts', []))}")
        print(
            f"projects  {len(data['projects'].get('projects', []))}, repos {len(data['repos'].get('repos', []))}"
        )
        autos = data["automations"].get("automations", [])
        print(f"automations {len(autos)} ({sum(1 for a in autos if a.get('enabled'))} enabled)")
        print(f"skills    {len(data['skills'].get('skills', []))} installed")
        print(f"sessions  {data['index'].get('sessionsByAgent', {})}")

        rows = data["ps"].get("worktrees", [])
        print(f"\nWorktrees ({len(rows)} of {data['ps'].get('totalCount', len(rows))}):")
        for row in rows:
            agents = ", ".join(f"{a.get('agentType')}:{a.get('state')}" for a in row.get("agents", [])) or "-"
            print(
                f"  {row.get('repo', ''):<22} {row.get('displayName', ''):<28} {row.get('status', ''):<9} {agents}"
            )

        terminals = (await orca.terminal.list())["terminals"]
        busiest = sorted(terminals, key=lambda t: t.get("lastOutputAt") or 0, reverse=True)[: args.terminals]
        sem = asyncio.Semaphore(args.concurrency)
        tails = await asyncio.gather(*(tail(orca, sem, t["handle"]) for t in busiest), return_exceptions=True)
        print(f"\nMost recently active terminals ({len(busiest)}):")
        for term, lines in zip(busiest, tails):
            print(f"  {term.get('title') or term['handle']}  [{term.get('agentIdentity') or 'shell'}]")
            if isinstance(lines, BaseException):
                print(f"    ! {lines}")
                continue
            for line in lines:
                print(f"    | {line[:110]}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--worktrees", type=int, default=8, help="worktree rows to show")
    parser.add_argument("--terminals", type=int, default=3, help="terminals to tail")
    parser.add_argument("--concurrency", type=int, default=4, help="max concurrent terminal reads")
    parser.add_argument("--timeout", type=float, default=30, help="per-command timeout in seconds")
    args = parser.parse_args(argv)
    return asyncio.run(run(args))


if __name__ == "__main__":
    raise SystemExit(main())
