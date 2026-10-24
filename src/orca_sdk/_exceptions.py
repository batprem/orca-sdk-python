"""Exception hierarchy for the Orca SDK."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

__all__ = [
    "OrcaBinaryNotFoundError",
    "OrcaCommandError",
    "OrcaError",
    "OrcaJSONDecodeError",
    "OrcaTimeoutError",
    "OrcaUsageError",
]


class OrcaError(Exception):
    """Base class for every error raised by the SDK."""


class OrcaBinaryNotFoundError(OrcaError, FileNotFoundError):
    """The ``orca`` executable could not be located."""

    def __init__(self, message: str, searched: Sequence[str] = ()) -> None:
        super().__init__(message)
        self.searched = list(searched)


class OrcaUsageError(OrcaError, ValueError):
    """The SDK was asked to build a command the CLI would reject."""


class OrcaCommandError(OrcaError):
    """The CLI ran but reported failure.

    ``code`` and ``message`` come from the JSON error envelope when there is
    one (e.g. ``repo_not_found``); otherwise ``code`` is ``"process_error"``
    and ``message`` is taken from stderr/stdout.
    """

    def __init__(
        self,
        code: str,
        message: str,
        *,
        data: Any = None,
        argv: Sequence[str] = (),
        returncode: int | None = None,
        stdout: str = "",
        stderr: str = "",
        request_id: str | None = None,
    ) -> None:
        super().__init__(f"[{code}] {message}")
        self.code = code
        self.message = message
        self.data = data
        self.argv = list(argv)
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr
        self.request_id = request_id

    @property
    def next_steps(self) -> list[str]:
        """Hints the CLI attached under ``error.data.nextSteps``, if any."""
        if isinstance(self.data, dict) and isinstance(self.data.get("nextSteps"), list):
            return [str(s) for s in self.data["nextSteps"]]
        return []


class OrcaTimeoutError(OrcaError, TimeoutError):
    """The CLI did not finish within the configured timeout and was killed."""

    def __init__(
        self,
        timeout: float,
        argv: Sequence[str] = (),
        stdout: str = "",
        stderr: str = "",
    ) -> None:
        super().__init__(f"orca command timed out after {timeout:g}s: {' '.join(argv)}")
        self.timeout = timeout
        self.argv = list(argv)
        self.stdout = stdout
        self.stderr = stderr


class OrcaJSONDecodeError(OrcaError, ValueError):
    """``--json`` output could not be parsed as JSON."""

    def __init__(
        self,
        message: str,
        *,
        argv: Sequence[str] = (),
        stdout: str = "",
        stderr: str = "",
        returncode: int | None = None,
    ) -> None:
        super().__init__(message)
        self.argv = list(argv)
        self.stdout = stdout
        self.stderr = stderr
        self.returncode = returncode
