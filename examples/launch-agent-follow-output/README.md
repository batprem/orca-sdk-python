# Launch an agent and follow its terminal output

Starts a coding agent (claude by default) in an existing worktree with a prompt, then tails its terminal. Each `terminal read` passes the previous `nextCursor`, so only new output is printed. At the end it calls `terminal wait --for tui-idle` and prints the rendered screen.

Without `--apply` it only shows the worktree, its live terminals and the last lines of the most recently active one.

```bash
uv run examples/launch-agent-follow-output/main.py --worktree path:$PWD                  # read-only
uv run examples/launch-agent-follow-output/main.py --worktree path:$PWD \
    --agent claude --prompt "Summarise the README" --follow 120 --apply
```

**SDK calls:** `worktree.show()`, `terminal.list()`, `terminal.read(cursor=..., screen=...)`, and with `--apply`: `agent.launch(agent=..., worktree=..., prompt=..., surface="terminal")`, `terminal.wait(for_="tui-idle", timeout_ms=...)`, `with_options(timeout=...)`

**Changes state:** only with `--apply` (opens a new agent terminal that starts working on the prompt).
