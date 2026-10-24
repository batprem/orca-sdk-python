# Error and timeout handling

Triggers each kind of SDK failure on purpose, using commands that change nothing, and shows how to handle it:

1. `OrcaCommandError`: the CLI returned `ok: false` (`code`, `message`, `returncode`, `argv`, `next_steps`)
2. `run_command(..., check=False)`: inspect the error envelope without raising
3. `OrcaTimeoutError`: `with_options(timeout=...)` set too low; the CLI process is killed
4. A small retry helper that retries timeouts only, with backoff
5. `OrcaBinaryNotFoundError`: `binary=` points nowhere
6. `OrcaUsageError`: a host-local command (`host list`) on a client routed with `environment=`, raised before anything runs
7. `OrcaError` as a catch-all base class

```bash
uv run examples/error-handling/main.py
```

**Changes state:** never.
