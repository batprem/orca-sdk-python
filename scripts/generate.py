#!/usr/bin/env python3
"""Generate ``src/orca_sdk/_generated.py`` from the Orca CLI command schema.

The schema comes from ``orca agent-context --json`` and is vendored at
``src/orca_sdk/data/agent-context.json``. The schema lists flag *names* but not
whether a flag takes a value, so that is inferred from each command's usage
string and, when available, from the per-command ``--help`` output (a dump of
``orca <cmd> --help`` for every command, separated by ``== orca <cmd> --help``
header lines).

Usage::

    python scripts/generate.py [--schema PATH] [--help-dump PATH] [--check]

``--check`` exits non-zero if the generated file is out of date.
"""

from __future__ import annotations

import argparse
import json
import keyword
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SCHEMA = ROOT / "src" / "orca_sdk" / "data" / "agent-context.json"
DEFAULT_HELP = Path("/workspace/orca-cli-help.txt")
DEFAULT_FLAG_TYPES = ROOT / "src" / "orca_sdk" / "data" / "flag-types.json"
OUTPUT = ROOT / "src" / "orca_sdk" / "_generated.py"

# Flags handled by the client itself rather than exposed per method.
CLIENT_FLAGS = {"help", "json", "pairing-code", "environment"}
ROUTING_FLAGS = {"pairing-code", "environment"}

# Python names reserved on generated classes / clients.
RESERVED_ATTRS = {"run_command", "with_options", "close", "aclose", "binary", "config"}


def rejects_routing(raw: dict) -> bool:
    """Commands documented as rejecting --environment/--pairing-code (host-local)."""
    return any("rejected rather than ignored" in n and "--environment" in n for n in raw.get("notes", []))


# Positional args that the usage marks as required in one form but optional in
# another (e.g. ``emulator permissions reset`` takes no package).
OPTIONAL_POSITIONAL_OVERRIDES = {
    ("emulator", "permissions"): {"package", "permission"},
    ("search",): {"query"},  # ``orca search --index-status`` takes no query
}

# Value hints for flags that no usage string or help line types.
VALUE_FLAG_FALLBACK = {"precheck-timeout": "<seconds>", "dispatch-capability": "<token>"}

# Commands that read from stdin even without a ``*-stdin`` flag.
STDIN_COMMANDS = {("speech", "openai-key", "set")}

VALUE_TOKEN = re.compile(r"^(<[^>]*>|'<[^>]*>'|[\w.:-]+(\|[\w.:<>-]+)+|<[^>]*>\|\w+)")
INT_HINTS = re.compile(r"^<(n|ms|seconds|number|port|lines|pixels|x|y|w|h|epoch|lat|lon)>$")


def snake(name: str) -> str:
    out = re.sub(r"[^0-9a-zA-Z_]", "_", name).strip("_")
    if keyword.iskeyword(out) or out in {"self", "stdin"}:
        out += "_"
    if out[0].isdigit():
        out = "_" + out
    return out


def camel(parts: list[str]) -> str:
    return "".join(p[:1].upper() + p[1:] for part in parts for p in re.split(r"[-_]", part))


@dataclass
class Flag:
    name: str
    takes_value: bool
    repeatable: bool = False
    int_like: bool = False
    required: bool = False

    @property
    def py(self) -> str:
        return snake(self.name)


@dataclass
class Positional:
    name: str
    optional: bool
    variadic: bool = False

    @property
    def py(self) -> str:
        return snake(self.name)


@dataclass
class Command:
    path: list[str]
    summary: str
    usage: str
    notes: list[str]
    examples: list[str]
    flags: list[Flag]
    positionals: list[Positional]
    supports_json: bool
    supports_remote: bool
    passthrough: bool
    stdin: bool

    @property
    def method(self) -> str:
        return snake(self.path[-1])


@dataclass
class Group:
    path: list[str]
    children: dict[str, Group] = field(default_factory=dict)
    command: Command | None = None


def parse_help_dump(path: Path | None) -> dict[str, dict[str, str | None]]:
    """Map ``"worktree create"`` -> {flag: value-hint-or-""} from a help dump."""
    if path is None or not path.exists():
        return {}
    result: dict[str, dict[str, str | None]] = {}
    current: dict[str, str | None] | None = None
    in_options = False
    for line in path.read_text().splitlines():
        header = re.match(r"^== orca (.*?) ?--help$", line)
        if header:
            current = result.setdefault(header.group(1).strip(), {})
            in_options = False
            continue
        if current is None:
            continue
        if line.strip() == "Options:":
            in_options = True
            continue
        if in_options:
            m = re.match(r"^\s+--([\w-]+)(?:[\s=]+(\S+))?", line)
            if m:
                # None: listed without a value hint or description (ambiguous).
                hint = m.group(2)
                current[m.group(1)] = None if hint is None else (hint if VALUE_TOKEN.match(hint) else "")
            elif line and not line.startswith(" "):
                in_options = False
    return result


def usage_flag_hints(usage: str) -> dict[str, str]:
    hints: dict[str, str] = {}
    for m in re.finditer(r"--([\w-]+)", usage):
        rest = usage[m.end() :]
        token = rest[1:].split(None, 1)[0] if rest.startswith(" ") and rest[1:].strip() else ""
        token = token.rstrip("])")
        valued = bool(VALUE_TOKEN.match(token)) and not token.startswith("-")
        if valued or m.group(1) not in hints:
            hints[m.group(1)] = token if valued else ""
    return hints


def required_flags(usage: str) -> set[str]:
    """Flags outside any ``[...]`` or ``(...)`` group in a single-form usage."""
    if "\n" in usage.strip():
        return set()  # several alternative forms; nothing is unconditionally required
    required = set()
    depth = 0
    for tok in re.findall(r"[\[\]()]|--[\w-]+", usage):
        if tok in ("[", "("):
            depth += 1
        elif tok in ("]", ")"):
            depth -= 1
        elif depth == 0:
            required.add(tok[2:])
    return required


def parse_positionals(cmd: dict) -> list[Positional]:
    names = cmd.get("positionalArgs", [])
    if not names:
        return []
    usage = cmd["usage"].splitlines()[0]
    rest = usage.split(" ", 1)[1] if " " in usage else ""
    # Drop the command path words.
    for word in cmd["path"]:
        rest = rest.split(" ", 1)[1] if rest.startswith(word) and " " in rest else rest
    # Walk tokens before options, tracking bracket depth.
    tokens = re.findall(r"\[|\]|\(|\)|'[^']*'|[^\s\[\]()]+", rest)
    depth = 0
    pos_tokens: list[tuple[str, bool]] = []
    for i, tok in enumerate(tokens):
        if tok in ("[", "("):
            depth += 1
        elif tok in ("]", ")"):
            depth -= 1
        elif tok.startswith("-") or tok in {"|", "<"}:
            continue
        elif i and tokens[i - 1].startswith("--"):
            # Values directly after a flag are not positionals.
            continue
        else:
            pos_tokens.append((tok, depth > 0))
    overrides = OPTIONAL_POSITIONAL_OVERRIDES.get(tuple(cmd["path"]), set())
    out = []
    for i, name in enumerate(names):
        optional = pos_tokens[i][1] if i < len(pos_tokens) else True
        out.append(Positional(name=name, optional=optional or name in overrides))
    if cmd.get("variadicPositional"):
        out[-1].variadic = True
    # A required positional may not follow an optional one in Python.
    seen_optional = False
    for p in out:
        if p.optional:
            seen_optional = True
        elif seen_optional:
            p.optional = True
    return out


def build_commands(
    schema: dict, help_dump: dict[str, dict[str, str | None]]
) -> tuple[list[Command], list[str]]:
    commands: list[Command] = []
    unresolved: list[str] = []
    global_hints: dict[str, str] = {}
    for raw in schema["commands"]:
        sources = [usage_flag_hints(raw["usage"]), help_dump.get(" ".join(raw["path"]), {})]
        for hints in sources:
            for name, hint in hints.items():
                if hint:
                    global_hints.setdefault(name, hint)
    for raw in schema["commands"]:
        key = " ".join(raw["path"])
        uhints = usage_flag_hints(raw["usage"])
        hhints = help_dump.get(key, {})
        repeatable = set(raw.get("repeatableFlags") or [])
        positional_names = set(raw.get("positionalArgs", []))
        required = required_flags(raw["usage"])
        flags = []
        # Where --environment/--pairing-code appear in the usage they are the
        # command's own arguments (e.g. `environment show --environment <sel>`),
        # not routing to a remote runtime.
        own_routing = {f for f in ROUTING_FLAGS if f in uhints}
        for name in raw["flags"]:
            if name in CLIENT_FLAGS and name not in own_routing:
                continue
            if name in positional_names and name not in uhints:
                # Flag alias for a positional (e.g. ``--id`` for ``<id>``).
                continue
            if name in uhints:
                hint = uhints[name]
            elif hhints.get(name) is not None:
                hint = hhints[name]
            else:
                # Not typed for this command: reuse how other commands spell it.
                hint = global_hints.get(name) or VALUE_FLAG_FALLBACK.get(name, "")
                unresolved.append(f"{key}: --{name} -> {'value' if hint else 'boolean'}")
            flags.append(
                Flag(
                    name=name,
                    takes_value=bool(hint),
                    repeatable=name in repeatable,
                    int_like=bool(INT_HINTS.match(hint)),
                    required=bool(hint) and name in required,
                )
            )
        commands.append(
            Command(
                path=raw["path"],
                summary=raw.get("summary", ""),
                usage=raw["usage"],
                notes=raw.get("notes", []),
                examples=raw.get("examples", []),
                flags=flags,
                positionals=parse_positionals(raw),
                supports_json="json" in raw["flags"],
                supports_remote="environment" in raw["flags"]
                and not own_routing
                and not rejects_routing(raw),
                passthrough=raw.get("argumentMode") == "passthrough",
                stdin=tuple(raw["path"]) in STDIN_COMMANDS
                or any(f.endswith("-stdin") or f == "body-file" for f in raw["flags"]),
            )
        )
    return commands, unresolved


def build_tree(commands: list[Command]) -> Group:
    root = Group(path=[])
    for cmd in commands:
        node = root
        for i, part in enumerate(cmd.path):
            node = node.children.setdefault(part, Group(path=cmd.path[: i + 1]))
        node.command = cmd
    return root


def py_str(s: str) -> str:
    return json.dumps(s, ensure_ascii=False)


def docstring(cmd: Command, indent: str) -> list[str]:
    lines = [cmd.summary.rstrip(".") + ".", "", "CLI: ``" + cmd.usage.splitlines()[0] + "``"]
    if cmd.notes:
        lines += ["", "Notes:"] + [f"    {n}" for n in cmd.notes]
    if cmd.examples:
        lines += ["", "Examples:"] + [f"    {e}" for e in cmd.examples]
    text = "\n".join(lines).replace("\\", "\\\\").replace('"""', '\\"\\"\\"')
    body = [indent + '"""' + text.splitlines()[0]]
    body += [(indent + ln) if ln else "" for ln in text.splitlines()[1:]]
    body.append(indent + '"""')
    return body


def method_lines(cmd: Command, name: str, is_async: bool, indent: str = "    ") -> list[str]:
    params = ["self"]
    for p in cmd.positionals:
        ann = "str | Sequence[str]" if p.variadic else "Scalar"
        params.append(f"{p.py}: {ann} | None = None" if p.optional else f"{p.py}: {ann}")
    if cmd.passthrough:
        params.append("*args: str")
    kw = []
    used = {p.py for p in cmd.positionals}
    for f in cmd.flags:
        py = f.py
        if py in used:
            py += "_flag"
        used.add(py)
        f_py = py
        if f.takes_value:
            ann = "Scalar | Sequence[Scalar]" if f.repeatable else ("int | str" if f.int_like else "Scalar")
            default = "" if f.required else " | None = None"
            kw.append((f_py, f"{f_py}: {ann}{default}", f))
        else:
            kw.append((f_py, f"{f_py}: bool = False", f))
    if cmd.stdin:
        kw.append(("stdin", "stdin: str | bytes | None = None", None))
    if kw and not cmd.passthrough:
        params.append("*")
    params += [k[1] for k in kw if k[2] is not None and k[2].required]
    params += [k[1] for k in kw if k[2] is None or not k[2].required]
    ret = "Any"
    d = "async def" if is_async else "def"
    out = [f"{indent}{d} {name}("] + [f"{indent}    {p}," for p in params] + [f"{indent}) -> {ret}:"]
    out += docstring(cmd, indent + "    ")
    pos = ", ".join(p.py for p in cmd.positionals)
    pos_expr = f"[{pos}]" if pos else "[]"
    if cmd.passthrough:
        pos_expr = f"[*{pos_expr}, *args]" if pos else "list(args)"
    flag_items = ", ".join(f"({py_str(f.name)}, {py})" for py, _, f in kw if f is not None)
    call = (
        f"self._client._invoke({py_str(' '.join(cmd.path))}, {pos_expr}, [{flag_items}], "
        f"json={cmd.supports_json}, remote={cmd.supports_remote}"
        + (", stdin=stdin" if cmd.stdin else "")
        + ")"
    )
    out.append(f"{indent}    return {'await ' if is_async else ''}{call}")
    return out


def class_lines(group: Group, is_async: bool, emitted: list[str]) -> str:
    """Emit the class for ``group`` (children first) and return its name."""
    prefix = "Async" if is_async else ""
    cls = prefix + camel(group.path) + "Resource" if group.path else prefix + "OrcaCommands"
    child_classes = {}
    for name, child in sorted(group.children.items()):
        if child.children:
            child_classes[name] = class_lines(child, is_async, emitted)
    base = "_AsyncResource" if is_async else "_Resource"
    if not group.path:
        base = "_AsyncRoot" if is_async else "_SyncRoot"
    title = " ".join(group.path) if group.path else "orca"
    lines = [
        f"class {cls}({base}):",
        f'    """Commands under ``orca {title}``."""' if group.path else '    """All Orca CLI commands."""',
        "",
    ]
    if child_classes:
        for name, child_cls in child_classes.items():
            attr = snake(name)
            lines.append("    @cached_property")
            lines.append(f"    def {attr}(self) -> {child_cls}:")
            lines.append(f'        """``orca {" ".join(group.children[name].path)}`` commands."""')
            lines.append(f"        return {child_cls}(self._client)")
            lines.append("")
    if group.command is not None:
        lines += method_lines(group.command, "__call__", is_async)
        lines.append("")
    for name, child in sorted(group.children.items()):
        if child.command is not None and not child.children:
            attr = snake(name)
            assert group.path or attr not in RESERVED_ATTRS, attr
            lines += method_lines(child.command, attr, is_async)
            lines.append("")
    if lines[-1] == "":
        lines.pop()
    emitted.append("\n".join(lines))
    return cls


HEADER = '''"""Typed command wrappers generated from ``orca agent-context --json``.

DO NOT EDIT: regenerate with ``python scripts/generate.py``.
Schema version {schema_version}, {count} commands.
"""

from __future__ import annotations

from collections.abc import Sequence
from functools import cached_property
from typing import Any

from ._resource import Scalar, _AsyncResource, _AsyncRoot, _Resource, _SyncRoot

__all__ = ["OrcaCommands", "AsyncOrcaCommands", "COMMANDS"]

#: Metadata for every command: (path, supports --json, flags that take a value, boolean flags).
COMMANDS: dict[str, dict[str, Any]] = {commands}
'''


def render(schema: dict, help_dump: dict[str, dict[str, str | None]]) -> tuple[str, list[str]]:
    commands, unresolved = build_commands(schema, help_dump)
    tree = build_tree(commands)
    meta = {
        " ".join(c.path): {
            "json": c.supports_json,
            "remote": c.supports_remote,
            "value_flags": sorted(f.name for f in c.flags if f.takes_value),
            "bool_flags": sorted(f.name for f in c.flags if not f.takes_value),
            "positionals": [p.name for p in c.positionals],
        }
        for c in commands
    }
    meta_src = "{\n" + "".join(f"    {py_str(k)}: {v!r},\n" for k, v in meta.items()) + "}"
    parts = [
        HEADER.format(schema_version=schema.get("schemaVersion"), count=len(commands), commands=meta_src)
    ]
    for is_async in (False, True):
        emitted: list[str] = []
        class_lines(tree, is_async, emitted)
        parts += emitted
    return "\n\n".join(p.rstrip("\n") for p in parts) + "\n", unresolved


def load_flag_types(path: Path) -> dict[str, dict[str, str | None]]:
    if path.exists():
        return json.loads(path.read_text())
    return {}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    ap.add_argument("--help-dump", type=Path, default=None, help="optional `orca <cmd> --help` dump")
    ap.add_argument("--check", action="store_true", help="fail if the output is stale")
    ap.add_argument("-v", "--verbose", action="store_true", help="list flags typed by fallback")
    args = ap.parse_args()

    schema = json.loads(args.schema.read_text())
    # Help-derived flag hints are cached in data/flag-types.json so regeneration
    # does not require the multi-megabyte help dump.
    help_dump = load_flag_types(DEFAULT_FLAG_TYPES)
    if args.help_dump or (DEFAULT_HELP.exists() and not help_dump):
        help_dump = parse_help_dump(args.help_dump or DEFAULT_HELP)
        if not args.check:
            DEFAULT_FLAG_TYPES.write_text(json.dumps(help_dump, indent=1, sort_keys=True) + "\n")
    text, unresolved = render(schema, help_dump)
    if args.verbose:
        for item in unresolved:
            print("inferred:", item, file=sys.stderr)
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text() != text:
            print(f"{OUTPUT} is out of date; run scripts/generate.py", file=sys.stderr)
            return 1
        return 0
    OUTPUT.write_text(text)
    print(f"wrote {OUTPUT.relative_to(ROOT)} ({len(schema['commands'])} commands)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
