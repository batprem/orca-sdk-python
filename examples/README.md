# Examples

Runnable scripts showing common tasks with `orca-cli-sdk` (import name `orca_sdk`). Each one lives in its own folder with a short README. From the repository root:

```bash
uv run examples/<name>/main.py --help
```

Every example is **read-only by default**. Anything that changes Orca state (registering a repo, creating a worktree, launching an agent, creating or running an automation, installing skills) only happens when you pass `--apply`. Without it, the example prints the call it would make.

| Example | What it shows | Can change state? |
| --- | --- | --- |
| [check-status](check-status/) | Readiness check with exit codes, version and capability checks, `--wait` polling | no |
| [list-hosts-and-projects](list-hosts-and-projects/) | Hosts, paired environments, projects, repos and worktrees grouped by repo | no |
| [register-repo-worktree](register-repo-worktree/) | Find or register a repo with `repo add`, then `worktree create` | with `--apply` |
| [launch-agent-follow-output](launch-agent-follow-output/) | `agent launch` claude with a prompt, tail it with `terminal read --cursor`, `terminal wait --for tui-idle` | with `--apply` |
| [manage-automations](manage-automations/) | List, show, run history; create or run an automation | with `--apply` |
| [search-agent-sessions](search-agent-sessions/) | Full-text session search with filters, pagination and resume commands | no |
| [manage-skills](manage-skills/) | Bundled guides, installed skills, install dry run and real install through `run_command` | with `--apply` |
| [async-concurrent-dashboard](async-concurrent-dashboard/) | `AsyncOrca` with `asyncio.gather`, `return_exceptions`, a semaphore and per-command timeouts | no |
| [fullstack-agent-orchestration](fullstack-agent-orchestration/) | Interview → brief + API contract → one worktree and agent per workstream, monitored concurrently with `AsyncOrca`, optional integrator | with `--apply` |
| [error-handling](error-handling/) | Every exception type, `check=False`, timeouts with retry | no |

The examples find the `orca` binary the same way the SDK does: `$ORCA_BIN`, then `orca` on `PATH`, then the default install path. `tests/test_examples.py` runs every example's read-only path against a mocked subprocess. It also checks that none of them runs a state-changing command without `--apply`.
