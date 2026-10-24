# Register a repo and set up a worktree

Checks whether a local git repo is registered with Orca and lists its worktrees. With `--apply` it registers the repo (only if needed) and creates a new independent worktree for a task.

```bash
uv run examples/register-repo-worktree/main.py ~/src/myapp --name fix-login              # dry run
uv run examples/register-repo-worktree/main.py ~/src/myapp --name fix-login --base-branch origin/main --apply
```

**SDK calls:** `repo.list()`, `worktree.list(repo="id:...")`, and with `--apply`: `repo.add(path=...)`, `worktree.create(name=..., repo="id:...", no_parent=True, base_branch=...)`

**Changes state:** only with `--apply` (registers the repo, creates a worktree and its branch).
