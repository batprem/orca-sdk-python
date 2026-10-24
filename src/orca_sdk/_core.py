"""Transport-independent pieces shared by :class:`Orca` and :class:`AsyncOrca`."""

from __future__ import annotations

import json as _json
import os
import shutil
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field, replace
from pathlib import Path
from typing import Any, Union

from ._exceptions import (
    OrcaBinaryNotFoundError,
    OrcaCommandError,
    OrcaJSONDecodeError,
    OrcaUsageError,
)
from ._resource import FlagValue, build_args

DEFAULT_BINARY = "/home/box/Applications/bin/orca"
DEFAULT_TIMEOUT = 60.0
BINARY_ENV_VAR = "ORCA_BIN"
PAIRING_CODE_ENV_VAR = "ORCA_PAIRING_CODE"

PathLike = Union[str, "os.PathLike[str]"]


class _Unset:
    def __repr__(self) -> str:
        return "NOT_GIVEN"


#: Sentinel meaning "keep the current value" in :meth:`Orca.with_options`.
NOT_GIVEN: Any = _Unset()


def find_binary(binary: PathLike | None = None) -> str:
    """Locate the ``orca`` executable.

    Order: explicit ``binary`` argument, ``$ORCA_BIN``, ``orca`` on ``$PATH``,
    then :data:`DEFAULT_BINARY`.
    """
    searched: list[str] = []
    candidates: list[str] = []
    if binary is not None:
        candidates.append(os.fspath(binary))
    else:
        env_bin = os.environ.get(BINARY_ENV_VAR)
        if env_bin:
            candidates.append(env_bin)
        on_path = shutil.which("orca")
        if on_path:
            candidates.append(on_path)
        else:
            searched.append("orca on $PATH")
        candidates.append(DEFAULT_BINARY)
    for candidate in candidates:
        resolved = shutil.which(candidate) if os.sep not in candidate else candidate
        searched.append(candidate)
        if resolved and Path(resolved).is_file() and os.access(resolved, os.X_OK):
            return str(resolved)
    raise OrcaBinaryNotFoundError(
        f"Could not find the orca CLI. Set ORCA_BIN or pass binary=... (searched: {', '.join(searched)})",
        searched,
    )


@dataclass(frozen=True)
class OrcaResponse:
    """A parsed CLI response.

    For ``--json`` commands this mirrors the ``{id, ok, result, error, _meta}``
    envelope. Commands without JSON output (or whose JSON is not an envelope)
    produce ``ok=True`` and the decoded JSON or stdout text as ``result``.
    """

    ok: bool
    result: Any
    argv: list[str]
    returncode: int
    stdout: str = ""
    stderr: str = ""
    error: dict[str, Any] | None = None
    id: str | None = None
    meta: dict[str, Any] = field(default_factory=dict)
    raw: Any = None


@dataclass(frozen=True)
class ClientConfig:
    binary: str | None
    timeout: float | None
    environment: str | None
    pairing_code: str | None
    env: Mapping[str, str] | None
    inherit_env: bool
    cwd: str | None

    def updated(self, **changes: Any) -> ClientConfig:
        return replace(self, **{k: v for k, v in changes.items() if v is not NOT_GIVEN})


@dataclass(frozen=True)
class PreparedCall:
    argv: list[str]
    env: dict[str, str] | None
    cwd: str | None
    timeout: float | None
    stdin: bytes | None
    json: bool


def make_config(
    binary: PathLike | None,
    timeout: float | None,
    environment: str | None,
    pairing_code: str | None,
    env: Mapping[str, str] | None,
    inherit_env: bool,
    cwd: PathLike | None,
) -> ClientConfig:
    return ClientConfig(
        binary=os.fspath(binary) if binary is not None else None,
        timeout=timeout,
        environment=environment,
        pairing_code=pairing_code,
        env=dict(env) if env is not None else None,
        inherit_env=inherit_env,
        cwd=os.fspath(cwd) if cwd is not None else None,
    )


def prepare(
    config: ClientConfig,
    binary: str,
    args: Sequence[str],
    *,
    json: bool,
    remote: bool,
    stdin: str | bytes | None,
    timeout: float | None | Any = NOT_GIVEN,
) -> PreparedCall:
    argv = [binary, *args]
    if json and "--json" not in args:
        argv.append("--json")
    extra_env: dict[str, str] = {}
    if config.environment is not None or config.pairing_code is not None:
        if not remote:
            raise OrcaUsageError(
                f"`orca {' '.join(args[:3])}` only runs on the local host and does not accept "
                "--environment/--pairing-code; use client.with_options(environment=None, "
                "pairing_code=None)"
            )
        if config.environment is not None:
            argv += ["--environment", config.environment]
        if config.pairing_code is not None:
            # Passed via the environment so the code does not show up in `ps`.
            extra_env[PAIRING_CODE_ENV_VAR] = config.pairing_code
    env: dict[str, str] | None = None
    if config.env is not None or extra_env or not config.inherit_env:
        env = dict(os.environ) if config.inherit_env else {}
        env.update(config.env or {})
        env.update(extra_env)
    data = stdin.encode() if isinstance(stdin, str) else stdin
    return PreparedCall(
        argv=argv,
        env=env,
        cwd=config.cwd,
        timeout=config.timeout if timeout is NOT_GIVEN else timeout,
        stdin=data,
        json=json,
    )


def prepare_invoke(
    config: ClientConfig,
    binary: str,
    command: str,
    positionals: Sequence[Any],
    flags: Sequence[tuple[str, FlagValue]],
    *,
    json: bool,
    remote: bool,
    stdin: str | bytes | None = None,
) -> PreparedCall:
    return prepare(
        config,
        binary,
        build_args(command, positionals, flags),
        json=json,
        remote=remote,
        stdin=stdin,
    )


def _decode(data: bytes | str | None) -> str:
    if data is None:
        return ""
    if isinstance(data, bytes):
        return data.decode("utf-8", errors="replace")
    return data


def parse_output(
    call: PreparedCall,
    returncode: int,
    stdout_b: bytes | str | None,
    stderr_b: bytes | str | None,
    *,
    check: bool = True,
) -> OrcaResponse:
    """Turn raw process output into an :class:`OrcaResponse`, raising on failure."""
    stdout, stderr = _decode(stdout_b), _decode(stderr_b)
    argv = call.argv
    if not call.json:
        response = OrcaResponse(
            ok=returncode == 0,
            result=stdout,
            argv=argv,
            returncode=returncode,
            stdout=stdout,
            stderr=stderr,
        )
        if check and returncode != 0:
            raise _process_error(response)
        return response

    text = stdout.strip()
    if not text:
        if returncode != 0:
            response = OrcaResponse(False, None, argv, returncode, stdout, stderr)
            if check:
                raise _process_error(response)
            return response
        raise OrcaJSONDecodeError(
            "orca produced no output for a --json command",
            argv=argv,
            stdout=stdout,
            stderr=stderr,
            returncode=returncode,
        )
    try:
        payload = _json.loads(text)
    except ValueError as exc:
        if returncode != 0 and check:
            raise _process_error(OrcaResponse(False, None, argv, returncode, stdout, stderr)) from exc
        raise OrcaJSONDecodeError(
            f"could not decode orca --json output: {exc}",
            argv=argv,
            stdout=stdout,
            stderr=stderr,
            returncode=returncode,
        ) from exc

    if isinstance(payload, dict) and isinstance(payload.get("ok"), bool):
        error = payload.get("error")
        response = OrcaResponse(
            ok=payload["ok"] and returncode == 0,
            result=payload.get("result"),
            argv=argv,
            returncode=returncode,
            stdout=stdout,
            stderr=stderr,
            error=error if isinstance(error, dict) else None,
            id=payload.get("id"),
            meta=payload.get("_meta") or {},
            raw=payload,
        )
    else:
        # A few commands (e.g. `skills get`) print bare JSON rather than an envelope.
        response = OrcaResponse(
            ok=returncode == 0,
            result=payload,
            argv=argv,
            returncode=returncode,
            stdout=stdout,
            stderr=stderr,
            raw=payload,
        )
    if check and not response.ok:
        raise _command_error(response)
    return response


def _command_error(response: OrcaResponse) -> OrcaCommandError:
    if response.error is None:
        return _process_error(response)
    return OrcaCommandError(
        str(response.error.get("code") or "unknown_error"),
        str(response.error.get("message") or ""),
        data=response.error.get("data"),
        argv=response.argv,
        returncode=response.returncode,
        stdout=response.stdout,
        stderr=response.stderr,
        request_id=response.id,
    )


def _process_error(response: OrcaResponse) -> OrcaCommandError:
    message = (
        response.stderr.strip()
        or response.stdout.strip()
        or (f"orca exited with status {response.returncode}")
    )
    return OrcaCommandError(
        "process_error",
        message,
        argv=response.argv,
        returncode=response.returncode,
        stdout=response.stdout,
        stderr=response.stderr,
    )
