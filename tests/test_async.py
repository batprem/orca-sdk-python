from __future__ import annotations

import asyncio

import pytest
from conftest import envelope

from orca_sdk import AsyncOrca, OrcaCommandError, OrcaTimeoutError, OrcaUsageError


class FakeProcess:
    def __init__(self, stdout: str, stderr: str = "", returncode: int = 0, delay: float = 0.0):
        self._out = stdout.encode()
        self._err = stderr.encode()
        self._rc = returncode
        self._delay = delay
        self.returncode: int | None = None
        self.killed = False
        self.input: bytes | None = None

    async def communicate(self, data=None):
        self.input = data
        await asyncio.sleep(self._delay)
        self.returncode = self._rc
        return self._out, self._err

    def kill(self):
        self.killed = True

    async def wait(self):
        self.returncode = -9
        return -9


@pytest.fixture
def spawn(monkeypatch):
    state = {"calls": [], "proc": FakeProcess(envelope({}))}

    async def fake_exec(*argv, **kwargs):
        state["calls"].append({"argv": list(argv), **kwargs})
        return state["proc"]

    monkeypatch.setattr("orca_sdk._async_client.asyncio.create_subprocess_exec", fake_exec)
    return state


@pytest.fixture
def aclient(fake_bin):
    return AsyncOrca(binary=fake_bin)


async def test_async_status(aclient, spawn):
    spawn["proc"] = FakeProcess(envelope({"graph": {"state": "ready"}}))
    assert await aclient.status() == {"graph": {"state": "ready"}}
    assert spawn["calls"][-1]["argv"][1:] == ["status", "--json"]


async def test_async_nested(aclient, spawn):
    await aclient.project.list()
    assert spawn["calls"][-1]["argv"][1:] == ["project", "list", "--json"]
    await aclient.agent.hooks.status()
    assert spawn["calls"][-1]["argv"][1:] == ["agent", "hooks", "status", "--json"]


async def test_async_error(aclient, spawn):
    spawn["proc"] = FakeProcess(
        envelope(ok=False, error={"code": "repo_not_found", "message": "repo_not_found"}), returncode=1
    )
    with pytest.raises(OrcaCommandError) as info:
        await aclient.repo.show(repo="x")
    assert info.value.code == "repo_not_found"


async def test_async_timeout_kills_process(aclient, spawn):
    proc = FakeProcess(envelope({}), delay=5)
    spawn["proc"] = proc
    with pytest.raises(OrcaTimeoutError):
        await aclient.with_options(timeout=0.05).status()
    assert proc.killed


async def test_async_environment_and_stdin(fake_bin, spawn):
    client = AsyncOrca(binary=fake_bin, environment="lab", pairing_code="orca://pair?y")
    await client.speech.openai_key.set(stdin="sk")
    call = spawn["calls"][-1]
    assert call["argv"][-2:] == ["--environment", "lab"]
    assert call["env"]["ORCA_PAIRING_CODE"] == "orca://pair?y"
    assert spawn["proc"].input == b"sk"
    with pytest.raises(OrcaUsageError):
        await client.account.list()


async def test_async_run_command_and_context_manager(fake_bin, spawn):
    async with AsyncOrca(binary=fake_bin) as client:
        response = await client.run_command(["status"])
    assert response.ok and response.result == {}


async def test_async_concurrent(aclient, spawn):
    results = await asyncio.gather(aclient.status(), aclient.repo.list(), aclient.host.list())
    assert results == [{}, {}, {}]
    assert len(spawn["calls"]) == 3
