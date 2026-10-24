"""Checks that the generated wrappers cover the whole bundled CLI schema."""

from __future__ import annotations

import inspect
import subprocess
import sys
from pathlib import Path

import pytest

from orca_sdk import AsyncOrca, Orca
from orca_sdk.schema import COMMANDS, command_names, get_command, load_schema

ROOT = Path(__file__).resolve().parent.parent


def _resolve(client, path: list[str]):
    obj = client
    for part in path:
        obj = getattr(obj, _attr(part))
    return obj


def _attr(name: str) -> str:
    import keyword

    out = name.replace("-", "_")
    return out + "_" if keyword.iskeyword(out) else out


def _dummy_kwargs(fn) -> tuple[list, dict]:
    args, kwargs = [], {}
    for p in inspect.signature(fn).parameters.values():
        if p.default is not inspect.Parameter.empty or p.kind is p.VAR_POSITIONAL:
            continue
        if p.kind is p.KEYWORD_ONLY:
            kwargs[p.name] = "v"
        else:
            args.append("p")
    return args, kwargs


def test_schema_matches_generated_metadata():
    assert sorted(command_names()) == sorted(COMMANDS)
    assert load_schema()["commandCount"] == len(COMMANDS)


def test_get_command_and_aliases():
    assert get_command("worktree create")["summary"].startswith("Create")
    assert get_command("account remove")["command"] == "account rm"
    with pytest.raises(KeyError):
        get_command("nope")


@pytest.mark.parametrize("name", sorted(COMMANDS))
def test_every_command_builds_expected_argv(name, client, run):
    path = name.split()
    fn = _resolve(client, path)
    args, kwargs = _dummy_kwargs(fn)
    fn(*args, **kwargs)
    argv = run.args
    assert argv[: len(path)] == path
    assert ("--json" in argv) == COMMANDS[name]["json"]
    for flag in kwargs:
        # every required kwarg became a valued flag
        assert any(a.startswith("--") and a[2:].replace("-", "_") in (flag, flag.rstrip("_")) for a in argv)


@pytest.mark.parametrize("name", sorted(COMMANDS))
def test_async_mirrors_sync(name):
    path = name.split()
    sync_fn = _resolve(Orca(binary="/bin/true"), path)
    async_fn = _resolve(AsyncOrca(binary="/bin/true"), path)
    assert inspect.iscoroutinefunction(async_fn) or inspect.iscoroutinefunction(async_fn.__call__)
    assert list(inspect.signature(sync_fn).parameters) == list(inspect.signature(async_fn).parameters)


@pytest.mark.parametrize(
    "group",
    [
        "project",
        "repo",
        "worktree",
        "agent",
        "terminal",
        "automations",
        "host",
        "environment",
        "skills",
        "reference",
        "account",
        "orchestration",
        "linear",
        "jira",
        "tab",
        "emulator",
        "computer",
    ],
)
def test_resource_groups_exist(group):
    assert hasattr(Orca, group) and hasattr(AsyncOrca, group)


def test_top_level_commands_exist():
    for name in ("status", "search", "open", "agent_context", "snapshot", "goto", "is_"):
        assert callable(getattr(Orca(binary="/bin/true"), name))


def test_methods_have_docstrings():
    doc = Orca(binary="/bin/true").worktree.create.__doc__
    assert "Create a new Orca-managed worktree" in doc
    assert "orca worktree create" in doc


def test_generated_file_is_up_to_date():
    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "generate.py"), "--check"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stderr
