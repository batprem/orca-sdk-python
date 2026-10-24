"""Register a local git repo with Orca and create a worktree for a new task.

    uv run examples/register-repo-worktree/main.py ~/src/myapp --name fix-login
    uv run examples/register-repo-worktree/main.py ~/src/myapp --name fix-login --apply

Without --apply this only reads (`repo list`, `worktree list`) and prints the
commands it would run. With --apply it runs `repo add` (if the path is not yet
registered) and `worktree create`.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from orca_sdk import Orca


def find_repo(orca: Orca, path: Path) -> dict[str, Any] | None:
    for repo in orca.repo.list()["repos"]:
        if Path(repo["path"]).resolve() == path:
            return repo
    return None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("path", nargs="?", default=".", help="repo path (default: current directory)")
    parser.add_argument("--name", default="sdk-example-task", help="name for the new worktree")
    parser.add_argument("--base-branch", help="base ref for the worktree (default: repo default base)")
    parser.add_argument(
        "--apply", action="store_true", help="actually register the repo and create the worktree"
    )
    args = parser.parse_args(argv)

    path = Path(args.path).expanduser().resolve()
    orca = Orca()

    repo = find_repo(orca, path)
    if repo is None:
        print(f"{path} is not registered with Orca.")
        if not args.apply:
            print(f"dry run: would call orca.repo.add(path={str(path)!r})")
    else:
        print(f"{path} is registered as {repo['displayName']!r} (id {repo['id']}, kind {repo['kind']}).")
        worktrees = orca.worktree.list(repo=f"id:{repo['id']}", limit=50)["worktrees"]
        print(f"Existing worktrees: {len(worktrees)}")
        for wt in worktrees:
            branch = (wt.get("branch") or "").removeprefix("refs/heads/") or "-"
            print(f"  {wt['displayName']:<30} {branch:<30} {wt['path']}")
        if any(wt["displayName"] == args.name for wt in worktrees):
            print(f"A worktree named {args.name!r} already exists; pick another --name.")
            return 1

    create_kwargs: dict[str, Any] = {"name": args.name, "no_parent": True}
    if args.base_branch:
        create_kwargs["base_branch"] = args.base_branch

    if not args.apply:
        repo_selector = f"id:{repo['id']}" if repo else "id:<new repo id>"
        print(f"dry run: would call orca.worktree.create(repo={repo_selector!r}, {_kwargs(create_kwargs)})")
        print("Re-run with --apply to make these changes.")
        return 0

    if repo is None:
        added = orca.repo.add(path=str(path))
        repo = added.get("repo", added) if isinstance(added, dict) else None
        if not repo or "id" not in repo:
            repo = find_repo(orca, path)
        if repo is None:
            print("repo add succeeded but the repo was not found in `repo list`")
            return 1
        print(f"Registered {path} as {repo['id']}")

    created = orca.worktree.create(repo=f"id:{repo['id']}", **create_kwargs)
    worktree = created.get("worktree", created)
    print(f"Created worktree {worktree.get('displayName', args.name)!r}")
    print(f"  id:   {worktree.get('id')}")
    print(f"  path: {worktree.get('path')}")
    return 0


def _kwargs(kwargs: dict[str, Any]) -> str:
    return ", ".join(f"{key}={value!r}" for key, value in kwargs.items())


if __name__ == "__main__":
    raise SystemExit(main())
