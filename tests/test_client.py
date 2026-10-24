from __future__ import annotations

import json
import subprocess

import pytest
from conftest import envelope

from orca_sdk import (
    Orca,
    OrcaBinaryNotFoundError,
    OrcaCommandError,
    OrcaJSONDecodeError,
    OrcaTimeoutError,
    OrcaUsageError,
)


def test_status_returns_result(client, run):
    run.stdout = envelope({"runtime": {"state": "ready"}})
    assert client.status() == {"runtime": {"state": "ready"}}
    assert run.args == ["status", "--json"]
    assert run.calls[-1]["timeout"] == 60.0
    assert run.calls[-1]["stdin"] is subprocess.DEVNULL


def test_nested_group_and_flags(client, run):
    client.worktree.list(repo="name:orca", limit=5)
    assert run.args == ["worktree", "list", "--repo", "name:orca", "--limit", "5", "--json"]


def test_required_keyword_flags(client, run):
    client.repo.show(repo="id:abc")
    assert run.args == ["repo", "show", "--repo", "id:abc", "--json"]
    with pytest.raises(TypeError):
        client.repo.show()  # type: ignore[call-arg]


def test_boolean_flags_and_none_are_omitted(client, run):
    client.worktree.rm(worktree="active", force=True, run_hooks=False)
    assert run.args == ["worktree", "rm", "--worktree", "active", "--force", "--json"]


def test_repeatable_flag(client, run):
    client.worktree.create(name="t", reference=["https://x/1", "ABC-2"], no_parent=True)
    assert run.args == [
        "worktree",
        "create",
        "--name",
        "t",
        "--reference",
        "https://x/1",
        "--reference",
        "ABC-2",
        "--no-parent",
        "--json",
    ]


def test_positional_and_variadic(client, run):
    client.reference.add(["https://a", "https://b"], worktree="active")
    assert run.args == ["reference", "add", "https://a", "https://b", "--worktree", "active", "--json"]
    client.search("flaky test", limit=3)
    assert run.args == ["search", "flaky test", "--limit", "3", "--json"]
    client.skills.get("orca-cli", full=True)
    assert run.args == ["skills", "get", "orca-cli", "--full", "--json"]


def test_keyword_named_flags_get_trailing_underscore(client, run):
    client.terminal.wait(terminal="t1", for_="exit", timeout_ms=1000)
    assert run.args == [
        "terminal",
        "wait",
        "--terminal",
        "t1",
        "--for",
        "exit",
        "--timeout-ms",
        "1000",
        "--json",
    ]


def test_dash_values_are_attached(client, run):
    client.automations.edit("auto-1", extra_agent_args="--yolo")
    assert "--extra-agent-args=--yolo" in run.args


def test_command_error_from_envelope(client, run):
    run.returncode = 1
    run.stdout = envelope(
        ok=False,
        error={
            "code": "repo_not_found",
            "message": "repo_not_found",
            "data": {"nextSteps": ["orca repo list"]},
        },
    )
    with pytest.raises(OrcaCommandError) as info:
        client.repo.show(repo="nope")
    err = info.value
    assert err.code == "repo_not_found"
    assert err.message == "repo_not_found"
    assert err.returncode == 1
    assert err.request_id == "req-1"
    assert err.next_steps == ["orca repo list"]
    assert err.argv[1:3] == ["repo", "show"]


def test_ok_false_with_zero_exit_still_raises(client, run):
    run.stdout = envelope(ok=False, error={"code": "x", "message": "boom"})
    with pytest.raises(OrcaCommandError, match="boom"):
        client.status()


def test_bare_json_without_envelope(client, run):
    run.stdout = json.dumps({"name": "orca-cli", "markdown": "# hi"})
    assert client.skills.get("orca-cli") == {"name": "orca-cli", "markdown": "# hi"}


def test_invalid_json(client, run):
    run.stdout = "not json"
    with pytest.raises(OrcaJSONDecodeError) as info:
        client.status()
    assert info.value.stdout == "not json"


def test_empty_output_is_decode_error(client, run):
    run.stdout = ""
    with pytest.raises(OrcaJSONDecodeError):
        client.status()


def test_nonzero_exit_without_json(client, run):
    run.returncode = 2
    run.stdout = ""
    run.stderr = "segfault"
    with pytest.raises(OrcaCommandError) as info:
        client.status()
    assert info.value.code == "process_error"
    assert info.value.message == "segfault"


def test_non_json_command_returns_stdout(client, run):
    run.stdout = "hooks ready\n"
    response = client.run_command(["agent", "hooks", "prepare-codex"], json=False)
    assert response.result == "hooks ready\n"
    assert run.args == ["agent", "hooks", "prepare-codex"]


def test_timeout(client, run):
    run.raise_exc = subprocess.TimeoutExpired(["orca"], 5, output=b"partial")
    with pytest.raises(OrcaTimeoutError) as info:
        client.with_options(timeout=5).status()
    assert info.value.timeout == 5
    assert info.value.stdout == "partial"
    assert isinstance(info.value, TimeoutError)


def test_timeout_none_and_per_call(client, run):
    client.with_options(timeout=None).status()
    assert run.calls[-1]["timeout"] is None
    client.run_command(["status"], timeout=1.5)
    assert run.calls[-1]["timeout"] == 1.5


def test_binary_vanishing_raises_not_found(client, run, fake_bin):
    run.raise_exc = FileNotFoundError(2, "No such file", str(fake_bin))
    with pytest.raises(OrcaBinaryNotFoundError):
        client.status()


def test_environment_passthrough(fake_bin, run):
    client = Orca(binary=fake_bin, environment="lab-box")
    client.worktree.list()
    assert run.args == ["worktree", "list", "--json", "--environment", "lab-box"]


def test_pairing_code_goes_through_env(fake_bin, run):
    client = Orca(binary=fake_bin, pairing_code="orca://pair?x=1")
    client.status()
    assert "orca://pair?x=1" not in run.argv
    assert run.calls[-1]["env"]["ORCA_PAIRING_CODE"] == "orca://pair?x=1"


def test_remote_options_rejected_for_local_only_commands(fake_bin, run):
    client = Orca(binary=fake_bin, environment="lab-box")
    with pytest.raises(OrcaUsageError):
        client.account.list()
    assert run.calls == []
    client.with_options(environment=None).account.list()
    assert run.args == ["account", "list", "--json"]


def test_environment_selector_commands(client, run):
    client.environment.show(environment="lab-box")
    assert run.args == ["environment", "show", "--environment", "lab-box", "--json"]
    client.environment.add(name="lab", pairing_code="orca://pair?z")
    assert run.args == ["environment", "add", "--pairing-code", "orca://pair?z", "--name", "lab", "--json"]


def test_host_local_commands_reject_routing(fake_bin, run):
    client = Orca(binary=fake_bin, pairing_code="orca://pair?x")
    for call in (client.host.list, client.environment.list):
        with pytest.raises(OrcaUsageError):
            call()


def test_custom_env_and_cwd(fake_bin, run, tmp_path, monkeypatch):
    monkeypatch.setenv("KEEP_ME", "1")
    Orca(binary=fake_bin, env={"FOO": "bar"}, cwd=tmp_path).status()
    call = run.calls[-1]
    assert call["env"]["FOO"] == "bar"
    assert call["env"]["KEEP_ME"] == "1"
    assert call["cwd"] == str(tmp_path)

    Orca(binary=fake_bin, env={"FOO": "bar"}, inherit_env=False).status()
    assert run.calls[-1]["env"] == {"FOO": "bar"}

    Orca(binary=fake_bin).status()
    assert run.calls[-1]["env"] is None  # inherit untouched


def test_with_options_returns_copy(fake_bin, run):
    base = Orca(binary=fake_bin, timeout=10)
    other = base.with_options(environment="e1")
    assert base.config.environment is None and other.config.environment == "e1"
    assert other.config.timeout == 10


def test_stdin_commands(client, run):
    client.speech.openai_key.set(stdin="sk-test")
    assert run.calls[-1]["input"] == b"sk-test"
    assert run.calls[-1]["stdin"] is None


def test_run_command_raw(client, run):
    run.returncode = 1
    run.stdout = envelope(ok=False, error={"code": "invalid_argument", "message": "bad"})
    response = client.run_command(["repo", "show", "--repo", "x"], check=False)
    assert response.ok is False
    assert response.error == {"code": "invalid_argument", "message": "bad"}
    assert response.id == "req-1"
    assert response.meta == {"runtimeId": "rt-1"}
    assert run.args == ["repo", "show", "--repo", "x", "--json"]


def test_run_command_does_not_duplicate_json(client, run):
    client.run_command(["status", "--json"])
    assert run.args.count("--json") == 1


def test_group_that_is_also_a_command(client, run):
    client.serve(port=7000, no_pairing=True)
    assert run.args == ["serve", "--port", "7000", "--no-pairing", "--json"]
    client.serve.service.status()
    assert run.args == ["serve", "service", "status", "--json"]


def test_passthrough_command(client, run):
    run.stdout = ""
    client.claude_teams("--model", "opus")
    assert run.args == ["claude-teams", "--model", "opus"]


def test_context_manager(fake_bin, run):
    with Orca(binary=fake_bin) as c:
        c.status()
    assert run.args == ["status", "--json"]
