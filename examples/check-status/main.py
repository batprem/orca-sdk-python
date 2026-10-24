"""Check that Orca is running and ready before a script does real work.

    uv run examples/check-status/main.py
    uv run examples/check-status/main.py --wait 30   # poll until ready, up to 30s
    uv run examples/check-status/main.py --json      # dump the raw status result

Read-only: only runs `orca status`. Exits 0 when ready, 1 when not, 2 when the
CLI cannot be reached at all, so it works as a pre-flight step in shell scripts.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from typing import Any

from orca_sdk import CLI_VERSION, Orca, OrcaError, __version__

# Capabilities the other examples rely on; handy to check on an older host.
INTERESTING_CAPABILITIES = ("agent.launch.v2", "agent.launch.surface.v1", "runtime.automatic-work.v1")


def is_ready(status: dict[str, Any]) -> bool:
    app = status.get("app") or {}
    runtime = status.get("runtime") or {}
    graph = status.get("graph") or {}
    return bool(
        app.get("running")
        and runtime.get("state") == "ready"
        and runtime.get("reachable")
        and graph.get("state") == "ready"
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--wait", type=float, default=0, metavar="SECONDS", help="poll until ready")
    parser.add_argument("--json", action="store_true", help="print the raw status result")
    args = parser.parse_args(argv)

    orca = Orca(timeout=15)
    deadline = time.monotonic() + args.wait
    while True:
        try:
            status = orca.status()
        except OrcaError as err:
            print(f"Orca is not reachable: {err}", file=sys.stderr)
            return 2
        if is_ready(status) or time.monotonic() >= deadline:
            break
        time.sleep(1)

    if args.json:
        print(json.dumps(status, indent=2))
        return 0 if is_ready(status) else 1

    app = status.get("app") or {}
    runtime = status.get("runtime") or {}
    graph = status.get("graph") or {}
    print(f"orca-cli-sdk {__version__} (generated for Orca CLI {CLI_VERSION})")
    print(f"binary:   {orca.binary}")
    print(f"target:   {(status.get('target') or {}).get('kind', '?')}")
    print(f"app:      running={app.get('running')} pid={app.get('pid')}")
    print(
        f"runtime:  state={runtime.get('state')} reachable={runtime.get('reachable')} "
        f"version={runtime.get('appVersion')}"
    )
    print(f"graph:    state={graph.get('state')}")

    capabilities = set(runtime.get("capabilities") or [])
    print(f"capabilities: {len(capabilities)} advertised")
    for name in INTERESTING_CAPABILITIES:
        print(f"  [{'x' if name in capabilities else ' '}] {name}")

    app_version = runtime.get("appVersion")
    if app_version and app_version != CLI_VERSION:
        print(f"note: the SDK was generated for {CLI_VERSION}, the app reports {app_version}")

    ready = is_ready(status)
    print("READY" if ready else "NOT READY")
    return 0 if ready else 1


if __name__ == "__main__":
    raise SystemExit(main())
