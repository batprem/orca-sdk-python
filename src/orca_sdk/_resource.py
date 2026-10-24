"""Base classes shared by the generated command wrappers."""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ._async_client import AsyncOrca
    from ._client import Orca

#: A value accepted for a flag or positional argument.
Scalar = str | int | float

FlagValue = Scalar | bool | Sequence[Scalar] | None


def build_args(
    command: str,
    positionals: Sequence[Any],
    flags: Sequence[tuple[str, FlagValue]],
) -> list[str]:
    """Turn a command path, positionals and ``(flag, value)`` pairs into argv.

    ``None`` and ``False`` values are omitted, ``True`` emits a bare flag, and a
    list/tuple value emits the flag once per item (for repeatable flags).
    A list positional (variadic) is expanded in place.
    """
    argv = command.split()
    for value in positionals:
        if value is None:
            continue
        if isinstance(value, (list, tuple)):
            argv.extend(_to_str(v) for v in value)
        else:
            argv.append(_to_str(value))
    for name, value in flags:
        if value is None or value is False:
            continue
        if value is True:
            argv.append(f"--{name}")
        elif isinstance(value, (list, tuple)):
            for item in value:
                argv += _flag(name, item)
        else:
            argv += _flag(name, value)
    return argv


def _flag(name: str, value: Any) -> list[str]:
    text = _to_str(value)
    # Values that look like flags must be attached so the CLI parser keeps them.
    if text.startswith("-"):
        return [f"--{name}={text}"]
    return [f"--{name}", text]


def _to_str(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


class _Resource:
    def __init__(self, client: Orca) -> None:
        self._client = client


class _AsyncResource:
    def __init__(self, client: AsyncOrca) -> None:
        self._client = client


class _SyncRoot:
    _client: Orca

    def __init__(self) -> None:
        self._client = self  # type: ignore[assignment]


class _AsyncRoot:
    _client: AsyncOrca

    def __init__(self) -> None:
        self._client = self  # type: ignore[assignment]
