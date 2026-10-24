from __future__ import annotations

import stat
from pathlib import Path

import pytest

import orca_sdk._core as core
from orca_sdk import Orca, OrcaBinaryNotFoundError, find_binary


def _exe(path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("#!/bin/sh\n")
    path.chmod(path.stat().st_mode | stat.S_IXUSR)
    return path


def test_explicit_binary_wins(tmp_path, monkeypatch):
    explicit = _exe(tmp_path / "a" / "orca")
    monkeypatch.setenv("ORCA_BIN", str(_exe(tmp_path / "b" / "orca")))
    assert find_binary(explicit) == str(explicit)


def test_env_var_before_path(tmp_path, monkeypatch):
    env_bin = _exe(tmp_path / "env" / "orca")
    path_dir = _exe(tmp_path / "path" / "orca").parent
    monkeypatch.setenv("ORCA_BIN", str(env_bin))
    monkeypatch.setenv("PATH", str(path_dir))
    assert find_binary() == str(env_bin)


def test_path_before_default(tmp_path, monkeypatch):
    on_path = _exe(tmp_path / "path" / "orca")
    monkeypatch.setenv("PATH", str(on_path.parent))
    monkeypatch.setattr(core, "DEFAULT_BINARY", str(_exe(tmp_path / "default" / "orca")))
    assert find_binary() == str(on_path)


def test_default_location(tmp_path, monkeypatch):
    default = _exe(tmp_path / "default" / "orca")
    monkeypatch.setenv("PATH", str(tmp_path / "empty"))
    monkeypatch.setattr(core, "DEFAULT_BINARY", str(default))
    assert find_binary() == str(default)


def test_env_var_pointing_nowhere_falls_through(tmp_path, monkeypatch):
    default = _exe(tmp_path / "default" / "orca")
    monkeypatch.setenv("ORCA_BIN", str(tmp_path / "missing"))
    monkeypatch.setenv("PATH", str(tmp_path / "empty"))
    monkeypatch.setattr(core, "DEFAULT_BINARY", str(default))
    assert find_binary() == str(default)


def test_not_found(tmp_path, monkeypatch):
    monkeypatch.setenv("PATH", str(tmp_path / "empty"))
    monkeypatch.setattr(core, "DEFAULT_BINARY", str(tmp_path / "nope"))
    with pytest.raises(OrcaBinaryNotFoundError) as info:
        find_binary()
    assert str(tmp_path / "nope") in info.value.searched
    assert isinstance(info.value, FileNotFoundError)


def test_non_executable_is_skipped(tmp_path, monkeypatch):
    plain = tmp_path / "orca"
    plain.write_text("")
    monkeypatch.setenv("PATH", str(tmp_path / "empty"))
    monkeypatch.setattr(core, "DEFAULT_BINARY", str(tmp_path / "nope"))
    with pytest.raises(OrcaBinaryNotFoundError):
        find_binary(plain)


def test_client_resolves_lazily(tmp_path, monkeypatch):
    monkeypatch.setenv("PATH", str(tmp_path / "empty"))
    monkeypatch.setattr(core, "DEFAULT_BINARY", str(tmp_path / "nope"))
    client = Orca()  # constructing must not fail
    with pytest.raises(OrcaBinaryNotFoundError):
        client.status()
