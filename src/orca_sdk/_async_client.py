"""Asynchronous Orca client built on :mod:`asyncio` subprocesses."""

from __future__ import annotations

import asyncio
import contextlib
import subprocess
from collections.abc import Mapping, Sequence
from typing import Any

from ._core import (
    DEFAULT_TIMEOUT,
    NOT_GIVEN,
    ClientConfig,
    OrcaResponse,
    PathLike,
    PreparedCall,
    find_binary,
    make_config,
    parse_output,
    prepare,
    prepare_invoke,
)
from ._exceptions import OrcaBinaryNotFoundError, OrcaTimeoutError
from ._generated import AsyncOrcaCommands
from ._resource import FlagValue

__all__ = ["AsyncOrca"]


class AsyncOrca(AsyncOrcaCommands):
    """Async counterpart of :class:`~orca_sdk.Orca`; every command is awaitable.

    >>> async with AsyncOrca() as client:
    ...     status = await client.status()

    Accepts the same options as :class:`~orca_sdk.Orca`.
    """

    def __init__(
        self,
        *,
        binary: PathLike | None = None,
        timeout: float | None = DEFAULT_TIMEOUT,
        environment: str | None = None,
        pairing_code: str | None = None,
        env: Mapping[str, str] | None = None,
        inherit_env: bool = True,
        cwd: PathLike | None = None,
    ) -> None:
        super().__init__()
        self._config = make_config(binary, timeout, environment, pairing_code, env, inherit_env, cwd)
        self._binary: str | None = None

    @classmethod
    def _from_config(cls, config: ClientConfig) -> AsyncOrca:
        client = cls.__new__(cls)
        AsyncOrcaCommands.__init__(client)
        client._config = config
        client._binary = None
        return client

    @property
    def binary(self) -> str:
        """Resolved path of the ``orca`` executable (located lazily)."""
        if self._binary is None:
            self._binary = find_binary(self._config.binary)
        return self._binary

    @property
    def config(self) -> ClientConfig:
        """The options this client runs commands with (timeout, environment, ...)."""
        return self._config

    def with_options(
        self,
        *,
        binary: PathLike | None = NOT_GIVEN,
        timeout: float | None = NOT_GIVEN,
        environment: str | None = NOT_GIVEN,
        pairing_code: str | None = NOT_GIVEN,
        env: Mapping[str, str] | None = NOT_GIVEN,
        inherit_env: bool = NOT_GIVEN,
        cwd: PathLike | None = NOT_GIVEN,
    ) -> AsyncOrca:
        """Return a copy of this client with some options changed."""
        config = self._config.updated(
            binary=binary,
            timeout=timeout,
            environment=environment,
            pairing_code=pairing_code,
            env=env,
            inherit_env=inherit_env,
            cwd=cwd,
        )
        return self._from_config(make_config(**vars(config)))

    async def run_command(
        self,
        args: Sequence[str],
        *,
        json: bool = True,
        remote: bool = True,
        stdin: str | bytes | None = None,
        timeout: float | None = NOT_GIVEN,
        check: bool = True,
    ) -> OrcaResponse:
        """Run ``orca <args...>``; see :meth:`orca_sdk.Orca.run_command`."""
        call = prepare(
            self._config, self.binary, list(args), json=json, remote=remote, stdin=stdin, timeout=timeout
        )
        return await self._execute(call, check=check)

    async def _invoke(
        self,
        command: str,
        positionals: Sequence[Any],
        flags: Sequence[tuple[str, FlagValue]],
        *,
        json: bool,
        remote: bool,
        stdin: str | bytes | None = None,
    ) -> Any:
        call = prepare_invoke(
            self._config, self.binary, command, positionals, flags, json=json, remote=remote, stdin=stdin
        )
        return (await self._execute(call)).result

    async def _execute(self, call: PreparedCall, *, check: bool = True) -> OrcaResponse:
        try:
            proc = await asyncio.create_subprocess_exec(
                *call.argv,
                stdin=subprocess.PIPE if call.stdin is not None else subprocess.DEVNULL,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                env=call.env,
                cwd=call.cwd,
            )
        except FileNotFoundError as exc:
            if exc.filename == call.argv[0]:
                raise OrcaBinaryNotFoundError(
                    f"orca binary not found: {call.argv[0]}", [call.argv[0]]
                ) from exc
            raise
        try:
            stdout, stderr = await asyncio.wait_for(proc.communicate(call.stdin), timeout=call.timeout)
        except asyncio.TimeoutError as exc:
            with contextlib.suppress(ProcessLookupError):
                proc.kill()
            with contextlib.suppress(Exception):
                await proc.wait()
            raise OrcaTimeoutError(call.timeout or 0.0, call.argv) from exc
        except BaseException:
            # Cancellation: don't leave the CLI running.
            with contextlib.suppress(ProcessLookupError):
                proc.kill()
            raise
        assert proc.returncode is not None
        return parse_output(call, proc.returncode, stdout, stderr, check=check)

    async def aclose(self) -> None:
        """No-op; present so the client can be used as an async context manager."""

    async def __aenter__(self) -> AsyncOrca:
        return self

    async def __aexit__(self, *exc: object) -> None:
        await self.aclose()

    def __repr__(self) -> str:
        return f"AsyncOrca(binary={self._config.binary or self._binary!r}, environment={self._config.environment!r})"
