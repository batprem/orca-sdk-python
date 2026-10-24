# Manage scheduled automations

Lists scheduled automations with their schedules and next run times, shows one in detail, and prints recent run history with the first line of each run's output. With `--apply` it can create an automation or trigger a run now.

```bash
uv run examples/manage-automations/main.py
uv run examples/manage-automations/main.py --show <automation-uuid> --runs 10
uv run examples/manage-automations/main.py --create "Daily review" --trigger daily \
    --prompt "Review open changes" --provider claude --repo name:myapp          # dry run
uv run examples/manage-automations/main.py --run <automation-uuid> --apply
```

**SDK calls:** `automations.list()`, `automations.show(id)`, `automations.runs(id=..., limit=...)`, and with `--apply`: `automations.create(name=..., trigger=..., prompt=..., provider=..., repo=...)`, `automations.run(id)`

**Changes state:** only with `--apply`.
