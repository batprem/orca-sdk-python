# Async dashboard with concurrent calls

Uses `AsyncOrca` to run eight read-only commands at once with `asyncio.gather` and builds a one-screen dashboard from the results. It then tails the most recently active terminals, with an `asyncio.Semaphore` capping how many `orca` processes run at the same time. `return_exceptions=True` means one failing command does not take the dashboard down.

```bash
uv run examples/async-concurrent-dashboard/main.py
uv run examples/async-concurrent-dashboard/main.py --terminals 5 --concurrency 2 --timeout 10
```

**SDK calls:** `AsyncOrca` as an async context manager, `status()`, `host.list()`, `project.list()`, `repo.list()`, `worktree.ps()`, `automations.list()`, `skills.installed()`, `search(index_status=True)`, `terminal.list()`, `terminal.read()`

**Changes state:** never.
