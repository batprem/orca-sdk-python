# List hosts and projects

An inventory of what Orca can see: the hosts you can target, paired remote environments, projects, registered repos, and worktrees grouped by repo.

```bash
uv run examples/list-hosts-and-projects/main.py
uv run examples/list-hosts-and-projects/main.py --limit 50
```

**SDK calls:** `host.list()`, `environment.list()`, `project.list()`, `repo.list()`, `worktree.list(limit=...)`

`host list` and `environment list` answer only from this machine. On a client created with `environment=` or `pairing_code=` they raise `OrcaUsageError`.

**Changes state:** never.
