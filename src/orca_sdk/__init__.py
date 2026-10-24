"""Python SDK for the Orca CLI.

>>> from orca_sdk import Orca
>>> client = Orca()
>>> client.status()["runtime"]["state"]
'ready'
"""

from __future__ import annotations

from ._async_client import AsyncOrca
from ._client import Orca
from ._core import BINARY_ENV_VAR, DEFAULT_BINARY, DEFAULT_TIMEOUT, NOT_GIVEN, OrcaResponse, find_binary
from ._exceptions import (
    OrcaBinaryNotFoundError,
    OrcaCommandError,
    OrcaError,
    OrcaJSONDecodeError,
    OrcaTimeoutError,
    OrcaUsageError,
)
from ._version import CLI_VERSION, __version__

__all__ = [
    "BINARY_ENV_VAR",
    "CLI_VERSION",
    "DEFAULT_BINARY",
    "DEFAULT_TIMEOUT",
    "NOT_GIVEN",
    "AsyncOrca",
    "Orca",
    "OrcaBinaryNotFoundError",
    "OrcaCommandError",
    "OrcaError",
    "OrcaJSONDecodeError",
    "OrcaResponse",
    "OrcaTimeoutError",
    "OrcaUsageError",
    "__version__",
    "find_binary",
]
