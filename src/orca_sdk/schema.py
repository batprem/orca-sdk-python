"""Access to the bundled Orca CLI command schema (``orca agent-context --json``)."""

from __future__ import annotations

import json
from functools import lru_cache
from importlib import resources
from typing import Any

from ._generated import COMMANDS

__all__ = ["COMMANDS", "command_names", "get_command", "load_schema"]


@lru_cache(maxsize=1)
def load_schema() -> dict[str, Any]:
    """Return the schema the SDK was generated from."""
    text = resources.files("orca_sdk").joinpath("data/agent-context.json").read_text("utf-8")
    return json.loads(text)


def command_names() -> list[str]:
    """All command paths, e.g. ``["account add", ..., "worktree show"]``."""
    return [" ".join(c["path"]) for c in load_schema()["commands"]]


def get_command(name: str) -> dict[str, Any]:
    """Schema entry for one command (``"worktree create"``), including aliases."""
    wanted = name.split()
    for cmd in load_schema()["commands"]:
        if cmd["path"] == wanted or wanted in cmd.get("aliases", []):
            return cmd
    raise KeyError(name)
