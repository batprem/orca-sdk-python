# Check status and readiness

Confirms the Orca app, runtime and graph are up before a script does real work. It prints the binary in use, the app version and whether a few capabilities are advertised. Use it as a pre-flight step in shell scripts.

```bash
uv run examples/check-status/main.py            # exits 0 ready / 1 not ready / 2 unreachable
uv run examples/check-status/main.py --wait 30  # poll for up to 30s until ready
uv run examples/check-status/main.py --json     # raw `orca status --json` result
```

**SDK calls:** `Orca.status()`, `Orca.binary`, `orca_sdk.CLI_VERSION`

**Changes state:** never.
