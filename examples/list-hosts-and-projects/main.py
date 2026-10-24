"""Inventory what Orca knows about: hosts, paired environments, projects, repos, worktrees.

    uv run examples/list-hosts-and-projects/main.py
    uv run examples/list-hosts-and-projects/main.py --limit 50

Read-only: runs `host list`, `environment list`, `project list`, `repo list`
and `worktree list`.
"""

from __future__ import annotations

import argparse
from collections import defaultdict

from orca_sdk import Orca


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--limit", type=int, default=20, help="max worktrees to list (default 20)")
    args = parser.parse_args(argv)

    orca = Orca()

    # `host list` and `environment list` only answer from this machine; on a
    # client created with environment=... they raise OrcaUsageError instead.
    print("Hosts")
    for host in orca.host.list()["hosts"]:
        print(f"  {host['name']:<24} kind={host['kind']:<8} {host.get('selector', '')}")

    environments = orca.environment.list()["environments"]
    print(f"\nPaired environments: {len(environments)}")
    for env in environments:
        print(f"  {env.get('name', env.get('id'))}")

    projects = orca.project.list()["projects"]
    print(f"\nProjects: {len(projects)}")
    for project in projects:
        print(f"  {project['displayName']:<28} {project['kind']:<7} {project['id']}")

    repos = orca.repo.list()["repos"]
    repo_names = {repo["id"]: repo["displayName"] for repo in repos}
    print(f"\nRepos: {len(repos)}")
    for repo in repos:
        print(f"  {repo['displayName']:<28} {repo['path']}")

    worktrees = orca.worktree.list(limit=args.limit)["worktrees"]
    by_repo: dict[str, list[dict]] = defaultdict(list)
    for wt in worktrees:
        by_repo[wt["repoId"]].append(wt)
    print(f"\nWorktrees (first {args.limit}): {len(worktrees)}")
    for repo_id, rows in by_repo.items():
        print(f"  {repo_names.get(repo_id, repo_id)}")
        for wt in rows:
            branch = (wt.get("branch") or "").removeprefix("refs/heads/") or "-"
            flags = " main" if wt.get("isMainWorktree") else ""
            print(f"    {wt['displayName']:<30} branch={branch:<24} host={wt.get('hostId')}{flags}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
