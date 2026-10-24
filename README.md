# orca-cli-sdk

A typed Python SDK for the Orca CLI, with both sync and `asyncio` clients.

- **Covers every command.** All 287 commands in Orca CLI 1.4.237 are wrapped, generated from the CLI's own schema (`orca agent-context --json`).
- **Mirrors the CLI.** `orca worktree list --limit 5` becomes `client.worktree.list(limit=5)`.
- **Uses the JSON envelope.** Commands run with `--json`, the SDK parses the `{ok, result, error}` envelope, and you get `result` back.
- **Typed exceptions.** Covers a missing binary, CLI errors (with `code`/`message`/`data`), timeouts and bad JSON.
- **No runtime dependencies.** Needs Python 3.10+.

```bash
uv add orca-cli-sdk        # or: pip install orca-cli-sdk
# import name: orca_sdk
```

## Quick start

```python
from orca_sdk import Orca

orca = Orca()

status = orca.status()
print(status["runtime"]["state"])            # "ready"

for project in orca.project.list()["projects"]:
    print(project["id"], project["displayName"])

repos = orca.repo.list()
worktrees = orca.worktree.list(repo="name:orca", limit=10)
```

### Async

```python
import asyncio
from orca_sdk import AsyncOrca

async def main() -> None:
    async with AsyncOrca() as orca:
        status, projects = await asyncio.gather(orca.status(), orca.project.list())
        print(status["graph"]["state"], len(projects["projects"]))

asyncio.run(main())
```

`AsyncOrca` has the same methods and signatures as `Orca`, but each command must be awaited. It runs the CLI with `asyncio.create_subprocess_exec`. If a command times out or is cancelled, the SDK kills the CLI process.

### Examples

[`examples/`](examples/README.md) has runnable scripts for common tasks: readiness checks, inventory, setting up worktrees, launching an agent and following its output, automations, session search, skills, concurrent async calls and error handling. They are read-only unless you pass `--apply`:

```bash
uv run examples/check-status/main.py
```

## Finding the `orca` binary

The binary is located the first time it is needed, checking in this order:

1. `Orca(binary="/path/to/orca")`
2. the `ORCA_BIN` environment variable
3. `orca` on `PATH`
4. `/home/box/Applications/bin/orca`

If none of these is an executable file, the SDK raises `OrcaBinaryNotFoundError`. `orca_sdk.find_binary()` runs the same lookup.

## Mapping CLI commands to methods

| CLI | Python |
| --- | --- |
| `orca status` | `orca.status()` |
| `orca worktree create --name t --agent codex --prompt "hi"` | `orca.worktree.create(name="t", agent="codex", prompt="hi")` |
| `orca worktree rm --worktree active --force` | `orca.worktree.rm(worktree="active", force=True)` |
| `orca terminal wait --terminal t1 --for exit --timeout-ms 60000` | `orca.terminal.wait(terminal="t1", for_="exit", timeout_ms=60000)` |
| `orca reference add <url> <url> --worktree active` | `orca.reference.add(["https://…", "https://…"], worktree="active")` |
| `orca agent hooks status` | `orca.agent.hooks.status()` |
| `orca linear team list` | `orca.linear.team.list()` |
| `orca terminal-daemon status` | `orca.terminal_daemon.status()` |
| `orca serve service status` | `orca.serve.service.status()` (`orca.serve(...)` runs `serve` itself) |

Naming rules:

- Hyphens become underscores (`setup-clone` → `setup_clone`).
- Python keywords get a trailing `_` (`--for` → `for_`, `orca is` → `orca.is_`).
- Positional arguments are positional parameters.
- Flags are keyword-only parameters.
- Flags the usage string marks as required are required keywords.

How values become arguments:

- Boolean flags take `True`.
- Repeatable flags (`--reference`, `--label`, …) take a list.
- `None`/`False` leaves the flag out.

Every method's docstring holds the CLI usage, notes and examples, so `help(orca.worktree.create)` shows what `orca worktree create --help` would.

The CLI's groups are all available, including:

- `project`, `repo`, `worktree`, `agent`, `terminal`
- `automations`, `host`, `environment`, `skills`, `reference`, `account`
- `orchestration`, `artifacts`, `file`, `tab`, `linear`, `jira`, `computer`, `emulator`, `storage`, `serve`

Top-level commands are methods on the client: `status`, `search`, `open`, `agent_context`, `snapshot`, `goto`, `click`, and the rest.

## Options: timeouts, env vars, remote runtimes

```python
orca = Orca(
    timeout=120,                 # seconds per command (default 60, None = no limit)
    env={"NO_COLOR": "1"},       # extra env vars for the subprocess
    inherit_env=True,            # start from os.environ (default)
    cwd="/path/to/worktree",     # Orca infers the current worktree from cwd
)

# Route every command to a saved remote Orca server (adds --environment <name>)
remote = Orca(environment="build-box")

# ...or to one reached by a pairing code (passed as $ORCA_PAIRING_CODE so it
# does not appear in the process list)
paired = Orca(pairing_code="orca://pair?...")

# Derive a client with different options; the original is unchanged
slow = orca.with_options(timeout=600)
slow.terminal.wait(terminal="term_123", for_="exit", timeout_ms=600_000)
local = remote.with_options(environment=None)
```

Some commands only run on the local host and reject routing: `account list`, `host list` and `environment list`. The `environment …` management commands also take `--environment` as a *selector* (which server to act on), not as routing. Calling any of these on a client that has `environment` or `pairing_code` set raises `OrcaUsageError` before running anything. Use `with_options(environment=None, pairing_code=None)` to call them.

```python
orca.environment.show(environment="build-box")   # selector, not routing
```

## Errors

```python
from orca_sdk import (
    OrcaError,                # base class
    OrcaBinaryNotFoundError,  # no orca executable
    OrcaCommandError,         # the CLI reported ok=false or exited non-zero
    OrcaTimeoutError,         # killed after the timeout
    OrcaJSONDecodeError,      # --json output was not valid JSON
    OrcaUsageError,           # e.g. routing a host-local command
)

try:
    orca.repo.show(repo="name:missing")
except OrcaCommandError as err:
    print(err.code)        # "repo_not_found"
    print(err.message)
    print(err.data)        # error.data from the envelope, if any
    print(err.next_steps)  # the CLI's suggested next steps
    print(err.returncode, err.argv, err.stderr)
```

If the CLI fails without printing a JSON envelope, you still get an `OrcaCommandError`, with `code == "process_error"` and the message taken from stderr.

## Raw access

`run_command` runs any argument list. It returns the full `OrcaResponse`: `ok`, `result`, `error`, `id`, `meta`, `stdout`, `stderr`, `returncode` and `argv`.

```python
resp = orca.run_command(["worktree", "ps", "--limit", "3"])
print(resp.meta["runtimeId"], resp.result)

resp = orca.run_command(["repo", "show", "--repo", "x"], check=False)  # don't raise
if not resp.ok:
    print(resp.error["code"])

orca.run_command(["claude-teams", "--help"], json=False)  # plain-text commands
```

To feed stdin, pass `stdin=` to `run_command` or to the generated methods that read stdin (for example `orca.speech.openai_key.set(stdin=key)` or `--text-stdin` commands).

The bundled schema is available at runtime:

```python
from orca_sdk.schema import load_schema, get_command, command_names
get_command("worktree create")["notes"]
```

## Development

```bash
uv sync
uv run pytest                        # unit tests (subprocess is mocked)
ORCA_INTEGRATION=1 uv run pytest     # also run read-only tests against the real orca
uv build
```

The integration tests only run read-only commands: `status`, `project list`, `repo list`, `worktree list`, `host list`, `environment list`, `skills list`, `agent-context` and a `repo show` that is expected to fail.

### Regenerating the wrappers

`src/orca_sdk/_generated.py` is generated, so don't edit it by hand. To regenerate it after an Orca upgrade:

```bash
orca agent-context --json > src/orca_sdk/data/agent-context.json
# optional, improves flag typing: a dump of `orca <cmd> --help` for every command,
# each section headed by a line `== orca <cmd> --help`
python scripts/generate.py --help-dump /path/to/orca-cli-help.txt -v
uv run pytest
```

The schema lists each command's flag names but not whether a flag takes a value. The generator works that out from the usage string, then from the `--help` text, which it caches in `data/flag-types.json`. If neither settles it, the generator uses how the same flag is written in other commands. `-v` lists the flags typed that way. `tests/test_generated.py` checks that the generated file is up to date and that every command builds its expected argv.

## License

MIT. See [LICENSE](LICENSE).
