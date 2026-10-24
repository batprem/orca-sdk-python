# Manage skills

Browses the skill guides bundled with the Orca CLI, summarises the skills installed for each agent, prints the start of one guide, and shows the exact `npx skills add` command an install would run. With `--apply` it runs the install.

```bash
uv run examples/manage-skills/main.py
uv run examples/manage-skills/main.py --topic orchestration --lines 40
uv run examples/manage-skills/main.py --install orca-cli --agent claude-code          # dry run
uv run examples/manage-skills/main.py --install orca-cli --agent claude-code --apply
```

**SDK calls:** `skills.list()`, `skills.installed()`, `skills.get(topic)`, `skills.install()` (listing), `skills.install(skill=[...], dry_run=True)`, and with `--apply`: `run_command(["skills", "install", ...], json=False)`

A real install streams npx output and rejects `--json`. That's why the example runs it with `run_command(..., json=False)` and not through the generated wrapper.

**Changes state:** only with `--apply` (writes skill files into your agents' config directories).
