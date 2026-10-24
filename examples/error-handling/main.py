"""Handle every kind of SDK failure: CLI errors, timeouts with retry, a missing binary, routing misuse.

    uv run examples/error-handling/main.py

Read-only. Each scenario triggers a failure on purpose using commands that do
not change anything: looking up a repo and an automation that do not exist,
running `status` with an impossibly short timeout, pointing at a binary that is
not there, and calling a host-local command on a client routed to a remote
environment.
"""

from __future__ import annotations

import argparse
import time
import uuid
from collections.abc import Callable
from typing import TypeVar

from orca_sdk import (
    Orca,
    OrcaBinaryNotFoundError,
    OrcaCommandError,
    OrcaError,
    OrcaTimeoutError,
    OrcaUsageError,
)

T = TypeVar("T")


def with_retry(fn: Callable[[], T], *, attempts: int = 3, backoff: float = 0.5) -> T:
    """Retry ``fn`` on timeouts only; CLI errors are not transient, so re-raise them."""
    for attempt in range(1, attempts + 1):
        try:
            return fn()
        except OrcaTimeoutError as err:
            if attempt == attempts:
                raise
            print(f"    attempt {attempt} timed out after {err.timeout:g}s, retrying")
            time.sleep(backoff * attempt)
    raise AssertionError("unreachable")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.parse_args(argv)

    orca = Orca()
    missing = f"sdk-example-missing-{uuid.uuid4().hex[:8]}"

    print("1. The CLI reports an error -> OrcaCommandError")
    try:
        orca.repo.show(repo=f"name:{missing}")
    except OrcaCommandError as err:
        print(f"   code={err.code!r} message={err.message!r} returncode={err.returncode}")
        print(f"   argv={err.argv[1:]}")
        for step in err.next_steps:
            print(f"   next step: {step}")

    print("2. Same failure without raising: run_command(check=False)")
    resp = orca.run_command(["automations", "show", str(uuid.uuid4())], check=False)
    print(f"   ok={resp.ok} error={resp.error}")

    print("3. A command that runs too long -> OrcaTimeoutError (the CLI process is killed)")
    try:
        orca.with_options(timeout=0.001).status()
        print("   finished before the timeout")
    except OrcaTimeoutError as err:
        print(f"   {err}")

    print("4. Retrying a timeout with backoff, then succeeding with a sane timeout")
    attempts = iter([0.001, 0.001, 15.0])
    status = with_retry(lambda: orca.with_options(timeout=next(attempts)).status(), attempts=3, backoff=0.1)
    print(f"   runtime state: {status['runtime']['state']}")

    print("5. No orca executable -> OrcaBinaryNotFoundError")
    try:
        Orca(binary="/nonexistent/bin/orca").status()
    except OrcaBinaryNotFoundError as err:
        print(f"   searched: {err.searched}")

    print("6. Routing a host-local command -> OrcaUsageError, raised before anything runs")
    remote = orca.with_options(environment="build-box")
    try:
        remote.host.list()
    except OrcaUsageError as err:
        print(f"   {err}")
    hosts = remote.with_options(environment=None).host.list()["hosts"]
    print(f"   with environment=None: {len(hosts)} host(s)")

    print("7. Catch-all: every SDK exception derives from OrcaError")
    try:
        orca.worktree.show(worktree=f"path:/{missing}")
    except OrcaError as err:
        print(f"   {type(err).__name__}: {err}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
