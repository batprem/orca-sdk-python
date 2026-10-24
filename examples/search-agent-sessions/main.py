"""Full-text search across past agent sessions (claude, codex, cursor, ...) and print how to resume them.

    uv run examples/search-agent-sessions/main.py "flaky test"
    uv run examples/search-agent-sessions/main.py "migration" --agent claude --agent codex --sort newest
    uv run examples/search-agent-sessions/main.py "kernel panic" --since 2026-08-01T00:00:00Z --pages 3

Read-only: runs `orca search --index-status` and `orca search <query>`,
following `page.cursor` for more pages.
"""

from __future__ import annotations

import argparse

from orca_sdk import Orca


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("query", nargs="?", default="worktree", help="text to search for")
    parser.add_argument("--agent", action="append", help="only this agent (repeatable)")
    parser.add_argument("--path", action="append", help="only sessions under this host path (repeatable)")
    parser.add_argument("--since", help="ISO 8601 timestamp with offset, e.g. 2026-08-01T00:00:00Z")
    parser.add_argument("--scope", choices=["conversation", "all"], default="all")
    parser.add_argument("--sort", choices=["relevance", "newest"], default="relevance")
    parser.add_argument("--limit", type=int, default=10, help="hits per page (max 100)")
    parser.add_argument("--pages", type=int, default=1, help="how many pages to read")
    args = parser.parse_args(argv)

    orca = Orca()

    index = orca.search(index_status=True)
    by_agent = ", ".join(f"{agent}={n}" for agent, n in (index.get("sessionsByAgent") or {}).items())
    print(f"Index: {index.get('phase')}, {index.get('messagesIndexed')} messages ({by_agent or 'empty'})")

    cursor = None
    shown = 0
    for _ in range(args.pages):
        page = orca.search(
            args.query,
            agent=args.agent,
            path=args.path,
            since=args.since,
            scope=args.scope,
            sort=args.sort,
            limit=args.limit,
            cursor=cursor,
        )
        for hit in page.get("hits") or []:
            shown += 1
            evidence = hit.get("evidence") or {}
            snippet = " ".join((evidence.get("snippet") or "").split())
            print(f"\n{shown}. [{hit['agent']}] {hit.get('title') or hit['sessionId']}")
            print(f"   {hit.get('messageCount', '?')} messages, score {hit.get('score', 0):.2f}")
            if snippet:
                print(f"   {evidence.get('role', '')}: {snippet[:160]}")
            if hit.get("resumeCommand"):
                print(f"   resume: {hit['resumeCommand']}")
        info = page.get("page") or {}
        cursor = info.get("cursor")
        if not info.get("hasMore") or not cursor:
            break

    print(f"\n{shown} hit(s) for {args.query!r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
