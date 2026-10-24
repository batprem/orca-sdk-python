from __future__ import annotations

import json
import os
import stat
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import pytest


def envelope(result: Any = None, *, ok: bool = True, error: dict | None = None) -> str:
    payload: dict[str, Any] = {"id": "req-1", "ok": ok, "_meta": {"runtimeId": "rt-1"}}
    if ok:
        payload["result"] = result
    else:
        payload["error"] = error
    return json.dumps(payload)


@dataclass
class Recorder:
    """Stands in for ``subprocess.run`` and records each call."""

    stdout: str = ""
    stderr: str = ""
    returncode: int = 0
    raise_exc: BaseException | None = None
    calls: list[dict[str, Any]] = field(default_factory=list)

    def __call__(self, argv, **kwargs):
        self.calls.append({"argv": list(argv), **kwargs})
        if self.raise_exc is not None:
            raise self.raise_exc
        return subprocess.CompletedProcess(argv, self.returncode, self.stdout.encode(), self.stderr.encode())

    @property
    def argv(self) -> list[str]:
        return self.calls[-1]["argv"]

    @property
    def args(self) -> list[str]:
        """argv without the binary path."""
        return self.argv[1:]


@pytest.fixture
def fake_bin(tmp_path: Path) -> Path:
    path = tmp_path / "bin" / "orca"
    path.parent.mkdir()
    path.write_text("#!/bin/sh\nexit 0\n")
    path.chmod(path.stat().st_mode | stat.S_IXUSR)
    return path


@pytest.fixture
def run(monkeypatch: pytest.MonkeyPatch) -> Recorder:
    recorder = Recorder(stdout=envelope({}))
    monkeypatch.setattr("orca_sdk._client.subprocess.run", recorder)
    return recorder


@pytest.fixture
def client(fake_bin: Path, run: Recorder):
    from orca_sdk import Orca

    return Orca(binary=fake_bin)


@pytest.fixture(autouse=True)
def _clean_env(monkeypatch: pytest.MonkeyPatch):
    for name in ("ORCA_BIN", "ORCA_PAIRING_CODE", "ORCA_ENVIRONMENT"):
        monkeypatch.delenv(name, raising=False)
    yield
    os.environ.pop("ORCA_BIN", None)
