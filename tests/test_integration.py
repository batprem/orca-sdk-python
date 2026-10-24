"""Read-only checks against the real orca binary.

Skipped unless ORCA_INTEGRATION=1. Only commands that do not change Orca state
are run here.
"""

from __future__ import annotations

import os

import pytest

from orca_sdk import AsyncOrca, Orca, OrcaCommandError

pytestmark = [
    pytest.mark.integration,
    pytest.mark.skipif(os.environ.get("ORCA_INTEGRATION") != "1", reason="set ORCA_INTEGRATION=1"),
]


@pytest.fixture(scope="module")
def orca() -> Orca:
    return Orca(timeout=60)


def test_status(orca):
    status = orca.status()
    assert "runtime" in status and "app" in status


def test_project_list(orca):
    result = orca.project.list()
    assert isinstance(result["projects"], list)


def test_repo_and_worktree_list(orca):
    assert isinstance(orca.repo.list(), dict)
    assert isinstance(orca.worktree.list(limit=5), dict)


def test_host_and_environment_list(orca):
    assert orca.host.list() is not None
    assert orca.environment.list() is not None


def test_skills_list(orca):
    assert orca.skills.list() is not None


def test_agent_context_matches_bundled_schema(orca):
    from orca_sdk.schema import load_schema

    live = orca.agent_context()
    commands = live.get("commands", live)
    assert {" ".join(c["path"]) for c in commands} >= {" ".join(c["path"]) for c in load_schema()["commands"]}


def test_command_error_is_typed(orca):
    with pytest.raises(OrcaCommandError) as info:
        orca.repo.show(repo="id:orca-sdk-integration-test-does-not-exist")
    assert info.value.code


async def test_async_status():
    async with AsyncOrca(timeout=60) as client:
        status, projects = await client.status(), await client.project.list()
    assert "runtime" in status
    assert "projects" in projects
