"""Browse Orca's bundled skill guides, see which skills are installed, and install one.

    uv run examples/manage-skills/main.py
    uv run examples/manage-skills/main.py --topic orchestration
    uv run examples/manage-skills/main.py --install orca-cli --agent claude-code --apply

Read-only by default: `skills list`, `skills installed`, `skills get`, the
installable-skill listing and `skills install --dry-run`. --apply runs the real
`skills install`, which shells out to `npx skills add`.
"""

from __future__ import annotations

import argparse
from collections import Counter

from orca_sdk import Orca


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--topic", default="orca-cli", help="guide to print (default orca-cli)")
    parser.add_argument("--lines", type=int, default=15, help="lines of the guide to print")
    parser.add_argument("--install", action="append", metavar="SKILL", help="skill to install (repeatable)")
    parser.add_argument(
        "--agent", help="install target(s), e.g. claude-code,codex (default: detected agents)"
    )
    parser.add_argument("--local", action="store_true", help="install into the current project, not globally")
    parser.add_argument("--apply", action="store_true", help="actually install")
    args = parser.parse_args(argv)

    orca = Orca()

    # `skills list` prints bare JSON rather than an envelope; the SDK returns it as-is.
    topics = orca.skills.list()["topics"]
    print(f"Bundled guides: {len(topics)}")
    for topic in topics:
        print(f"  {topic['name']:<26} {topic['description'][:80]}")

    installed = orca.skills.installed()["skills"]
    providers = Counter(p for skill in installed for p in skill.get("providers", []))
    print(
        f"\nInstalled skills: {len(installed)} ({', '.join(f'{p}={n}' for p, n in providers.most_common())})"
    )
    for skill in installed[:10]:
        print(f"  {skill['name']:<40} {skill.get('sourceLabel', '')}")
    if len(installed) > 10:
        print(f"  ... and {len(installed) - 10} more")

    guide = orca.skills.get(args.topic)
    print(f"\nFirst {args.lines} lines of the {guide['name']!r} guide:")
    for line in guide["markdown"].splitlines()[: args.lines]:
        print(f"  | {line}")

    available = orca.skills.install()["availableSkills"]
    print(f"\nInstallable Orca skills: {', '.join(available)}")

    if not args.install:
        return 0

    unknown = sorted(set(args.install) - set(available))
    if unknown:
        parser.error(f"not an installable skill: {', '.join(unknown)}")

    plan = orca.skills.install(skill=args.install, agent=args.agent, local=args.local, dry_run=True)
    print(f"\nInstall command: {plan['command']}")
    if not args.apply:
        print("dry run: nothing installed. Re-run with --apply to install.")
        return 0

    # A real install streams npx output and rejects --json, so run it through
    # run_command with json=False instead of the generated wrapper.
    cmd = ["skills", "install"]
    for name in args.install:
        cmd += ["--skill", name]
    if args.agent:
        cmd += ["--agent", args.agent]
    if args.local:
        cmd.append("--local")
    resp = orca.with_options(timeout=600).run_command(cmd, json=False)
    print(resp.stdout)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
