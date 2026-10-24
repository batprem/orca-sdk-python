# Search agent sessions

Full-text search over past agent sessions indexed on this host (claude, codex, cursor and others). It prints a snippet and the command to resume each hit, and follows `page.cursor` to read further pages.

```bash
uv run examples/search-agent-sessions/main.py "flaky test"
uv run examples/search-agent-sessions/main.py "migration" --agent claude --agent codex --sort newest
uv run examples/search-agent-sessions/main.py "kernel panic" --since 2026-08-01T00:00:00Z --limit 50 --pages 3
```

**SDK calls:** `search(index_status=True)`, `search(query, agent=[...], path=[...], since=..., scope=..., sort=..., limit=..., cursor=...)`

**Changes state:** never.
