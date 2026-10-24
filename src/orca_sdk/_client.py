"""Synchronous Orca client."""

from __future__ import annotations

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
from ._generated import OrcaCommands
from ._resource import FlagValue

__all__ = ["Orca"]


class Orca(OrcaCommands):
    """Run Orca CLI commands from Python.

    Every CLI command is available as a method mirroring its path, e.g.
    ``orca worktree list --limit 5`` is ``client.worktree.list(limit=5)`` and
    ``orca status`` is ``client.status()``. JSON-capable commands return the
    ``result`` from the CLI's ``{ok, result, error}`` envelope; failures raise
    :class:`~orca_sdk.OrcaCommandError`.

    Args:
        binary: Path to the ``orca`` executable. Defaults to ``$ORCA_BIN``,
            then ``orca`` on ``$PATH``, then ``/home/box/Applications/bin/orca``.
        timeout: Seconds before a command is killed (``None`` waits forever).
        environment: Saved remote Orca server (id or name) passed as
            ``--environment`` to every command that accepts it.
        pairing_code: ``orca://pair?...`` code for a remote runtime, passed to
            the CLI through ``$ORCA_PAIRING_CODE``.
        env: Extra environment variables for the subprocess.
        inherit_env: Start from ``os.environ`` (default) or an empty environment.
        cwd: Working directory for the subprocess; Orca infers the current
            worktree from it.
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
    def _from_config(cls, config: ClientConfig) -> Orca:
        client = cls.__new__(cls)
        OrcaCommands.__init__(client)
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
    ) -> Orca:
        """Return a copy of this client with some options changed.

        >>> client.with_options(timeout=300).terminal.wait(terminal="term_1", for_="exit")
        """
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

    def run_command(
        self,
        args: Sequence[str],
        *,
        json: bool = True,
        remote: bool = True,
        stdin: str | bytes | None = None,
        timeout: float | None = NOT_GIVEN,
        check: bool = True,
    ) -> OrcaResponse:
        """Run ``orca <args...>`` and return the parsed response.

        Use this for commands or flags the generated wrappers do not cover.
        ``--json`` is appended when ``json`` is true; ``remote`` controls
        whether the client's ``environment``/``pairing_code`` are applied.
        With ``check=False`` a failing envelope is returned instead of raised.
        """
        call = prepare(
            self._config, self.binary, list(args), json=json, remote=remote, stdin=stdin, timeout=timeout
        )
        return self._execute(call, check=check)

    def _invoke(
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
        return self._execute(call).result

    def _execute(self, call: PreparedCall, *, check: bool = True) -> OrcaResponse:
        try:
            proc = subprocess.run(
                call.argv,
                input=call.stdin,
                stdin=None if call.stdin is not None else subprocess.DEVNULL,
                capture_output=True,
                env=call.env,
                cwd=call.cwd,
                timeout=call.timeout,
                check=False,
            )
        except subprocess.TimeoutExpired as exc:
            raise OrcaTimeoutError(
                call.timeout or 0.0,
                call.argv,
                stdout=_text(exc.stdout),
                stderr=_text(exc.stderr),
            ) from exc
        except FileNotFoundError as exc:
            if exc.filename == call.argv[0]:
                raise OrcaBinaryNotFoundError(
                    f"orca binary not found: {call.argv[0]}", [call.argv[0]]
                ) from exc
            raise
        return parse_output(call, proc.returncode, proc.stdout, proc.stderr, check=check)

    def close(self) -> None:
        """No-op; present so the client can be used as a context manager."""

    def __enter__(self) -> Orca:
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()

    def __repr__(self) -> str:
        return (
            f"Orca(binary={self._config.binary or self._binary!r}, environment={self._config.environment!r})"
        )


def _text(data: bytes | str | None) -> str:
    if isinstance(data, bytes):
        return data.decode("utf-8", errors="replace")
    return data or ""
