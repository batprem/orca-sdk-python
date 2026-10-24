"""Typed command wrappers generated from ``orca agent-context --json``.

DO NOT EDIT: regenerate with ``python scripts/generate.py``.
Schema version 1, 287 commands.
"""

from __future__ import annotations

from collections.abc import Sequence
from functools import cached_property
from typing import Any

from ._resource import Scalar, _AsyncResource, _AsyncRoot, _Resource, _SyncRoot

__all__ = ["OrcaCommands", "AsyncOrcaCommands", "COMMANDS"]

#: Metadata for every command: (path, supports --json, flags that take a value, boolean flags).
COMMANDS: dict[str, dict[str, Any]] = {
    "account add": {'json': True, 'remote': True, 'value_flags': ['agent', 'integration', 'label'], 'bool_flags': [], 'positionals': []},
    "account list": {'json': True, 'remote': False, 'value_flags': ['agent'], 'bool_flags': [], 'positionals': []},
    "account rm": {'json': True, 'remote': True, 'value_flags': ['account', 'agent'], 'bool_flags': [], 'positionals': []},
    "account select": {'json': True, 'remote': True, 'value_flags': ['account', 'agent'], 'bool_flags': [], 'positionals': []},
    "agent hooks off": {'json': True, 'remote': True, 'value_flags': ['page'], 'bool_flags': [], 'positionals': []},
    "agent hooks on": {'json': True, 'remote': True, 'value_flags': ['page'], 'bool_flags': [], 'positionals': []},
    "agent hooks prepare-codex": {'json': True, 'remote': True, 'value_flags': ['page'], 'bool_flags': [], 'positionals': []},
    "agent hooks status": {'json': True, 'remote': True, 'value_flags': ['page'], 'bool_flags': [], 'positionals': []},
    "agent launch": {'json': True, 'remote': True, 'value_flags': ['agent', 'effort', 'model', 'page', 'prompt', 'retry-launch', 'surface', 'worktree'], 'bool_flags': ['focus'], 'positionals': []},
    "agent-context": {'json': True, 'remote': True, 'value_flags': [], 'bool_flags': [], 'positionals': []},
    "artifacts delete": {'json': True, 'remote': True, 'value_flags': ['api-url'], 'bool_flags': [], 'positionals': ['id']},
    "artifacts list": {'json': True, 'remote': True, 'value_flags': ['api-url', 'cursor'], 'bool_flags': [], 'positionals': []},
    "artifacts share": {'json': True, 'remote': True, 'value_flags': ['api-url'], 'bool_flags': [], 'positionals': ['file']},
    "artifacts unshare": {'json': True, 'remote': True, 'value_flags': ['api-url'], 'bool_flags': [], 'positionals': ['file']},
    "artifacts update": {'json': True, 'remote': True, 'value_flags': ['api-url'], 'bool_flags': [], 'positionals': ['file']},
    "automations create": {'json': True, 'remote': True, 'value_flags': ['base-branch', 'day', 'extra-agent-args', 'host', 'missed-run-grace-minutes', 'name', 'precheck', 'precheck-timeout', 'project', 'project-host-setup', 'prompt', 'provider', 'repo', 'schedule', 'source-context', 'time', 'timezone', 'trigger', 'workspace', 'workspace-mode'], 'bool_flags': ['disabled', 'enabled', 'fresh-session', 'reuse-session'], 'positionals': []},
    "automations edit": {'json': True, 'remote': True, 'value_flags': ['base-branch', 'day', 'extra-agent-args', 'host', 'missed-run-grace-minutes', 'name', 'precheck', 'precheck-timeout', 'project', 'project-host-setup', 'prompt', 'provider', 'repo', 'schedule', 'source-context', 'time', 'timezone', 'trigger', 'workspace', 'workspace-mode'], 'bool_flags': ['disabled', 'enabled', 'fresh-session', 'reuse-session'], 'positionals': ['id']},
    "automations list": {'json': True, 'remote': True, 'value_flags': [], 'bool_flags': [], 'positionals': []},
    "automations remove": {'json': True, 'remote': True, 'value_flags': [], 'bool_flags': [], 'positionals': ['id']},
    "automations run": {'json': True, 'remote': True, 'value_flags': [], 'bool_flags': [], 'positionals': ['id']},
    "automations runs": {'json': True, 'remote': True, 'value_flags': ['cursor', 'id', 'limit'], 'bool_flags': [], 'positionals': []},
    "automations show": {'json': True, 'remote': True, 'value_flags': [], 'bool_flags': [], 'positionals': ['id']},
    "back": {'json': True, 'remote': True, 'value_flags': ['page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "browser identity get": {'json': True, 'remote': True, 'value_flags': ['page'], 'bool_flags': [], 'positionals': []},
    "browser identity set": {'json': True, 'remote': True, 'value_flags': ['mode', 'page'], 'bool_flags': ['reset'], 'positionals': []},
    "capture start": {'json': True, 'remote': True, 'value_flags': ['page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "capture stop": {'json': True, 'remote': True, 'value_flags': ['page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "check": {'json': True, 'remote': True, 'value_flags': ['element', 'page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "claude-teams": {'json': False, 'remote': False, 'value_flags': [], 'bool_flags': [], 'positionals': []},
    "clear": {'json': True, 'remote': True, 'value_flags': ['element', 'page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "click": {'json': True, 'remote': True, 'value_flags': ['element', 'page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "clipboard read": {'json': True, 'remote': True, 'value_flags': ['page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "clipboard write": {'json': True, 'remote': True, 'value_flags': ['page', 'text', 'worktree'], 'bool_flags': [], 'positionals': []},
    "computer capabilities": {'json': True, 'remote': True, 'value_flags': [], 'bool_flags': [], 'positionals': []},
    "computer click": {'json': True, 'remote': True, 'value_flags': ['app', 'click-count', 'element-index', 'modifiers', 'mouse-button', 'session', 'window-id', 'window-index', 'worktree', 'x', 'y'], 'bool_flags': ['no-screenshot', 'restore-window'], 'positionals': []},
    "computer drag": {'json': True, 'remote': True, 'value_flags': ['app', 'from-element-index', 'from-x', 'from-y', 'session', 'to-element-index', 'to-x', 'to-y', 'window-id', 'window-index', 'worktree'], 'bool_flags': ['no-screenshot', 'restore-window'], 'positionals': []},
    "computer get-app-state": {'json': True, 'remote': True, 'value_flags': ['app', 'session', 'window-id', 'window-index', 'worktree'], 'bool_flags': ['no-screenshot', 'restore-window'], 'positionals': []},
    "computer hotkey": {'json': True, 'remote': True, 'value_flags': ['app', 'key', 'session', 'window-id', 'window-index', 'worktree'], 'bool_flags': ['no-screenshot', 'restore-window'], 'positionals': []},
    "computer list-apps": {'json': True, 'remote': True, 'value_flags': [], 'bool_flags': [], 'positionals': []},
    "computer list-windows": {'json': True, 'remote': True, 'value_flags': ['app'], 'bool_flags': [], 'positionals': []},
    "computer paste-text": {'json': True, 'remote': True, 'value_flags': ['app', 'session', 'text', 'window-id', 'window-index', 'worktree'], 'bool_flags': ['no-screenshot', 'restore-window', 'text-stdin'], 'positionals': []},
    "computer perform-secondary-action": {'json': True, 'remote': True, 'value_flags': ['action', 'app', 'element-index', 'session', 'window-id', 'window-index', 'worktree'], 'bool_flags': ['no-screenshot', 'restore-window'], 'positionals': []},
    "computer permissions": {'json': True, 'remote': True, 'value_flags': ['id'], 'bool_flags': [], 'positionals': []},
    "computer press-key": {'json': True, 'remote': True, 'value_flags': ['app', 'key', 'session', 'window-id', 'window-index', 'worktree'], 'bool_flags': ['no-screenshot', 'restore-window'], 'positionals': []},
    "computer scroll": {'json': True, 'remote': True, 'value_flags': ['app', 'direction', 'element-index', 'pages', 'session', 'window-id', 'window-index', 'worktree', 'x', 'y'], 'bool_flags': ['no-screenshot', 'restore-window'], 'positionals': []},
    "computer set-value": {'json': True, 'remote': True, 'value_flags': ['app', 'element-index', 'session', 'value', 'window-id', 'window-index', 'worktree'], 'bool_flags': ['no-screenshot', 'restore-window', 'value-stdin'], 'positionals': []},
    "computer type-text": {'json': True, 'remote': True, 'value_flags': ['app', 'session', 'text', 'window-id', 'window-index', 'worktree'], 'bool_flags': ['no-screenshot', 'restore-window', 'text-stdin'], 'positionals': []},
    "console": {'json': True, 'remote': True, 'value_flags': ['limit', 'page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "cookie delete": {'json': True, 'remote': True, 'value_flags': ['domain', 'name', 'page', 'url', 'worktree'], 'bool_flags': [], 'positionals': []},
    "cookie get": {'json': True, 'remote': True, 'value_flags': ['page', 'url', 'worktree'], 'bool_flags': [], 'positionals': []},
    "cookie set": {'json': True, 'remote': True, 'value_flags': ['domain', 'expires', 'name', 'page', 'path', 'sameSite', 'value', 'worktree'], 'bool_flags': ['httpOnly', 'secure'], 'positionals': []},
    "dblclick": {'json': True, 'remote': True, 'value_flags': ['element', 'page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "diagnostics memory": {'json': True, 'remote': True, 'value_flags': [], 'bool_flags': [], 'positionals': []},
    "dialog accept": {'json': True, 'remote': True, 'value_flags': ['page', 'text', 'worktree'], 'bool_flags': [], 'positionals': []},
    "dialog dismiss": {'json': True, 'remote': True, 'value_flags': ['page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "download": {'json': True, 'remote': True, 'value_flags': ['page', 'path', 'selector', 'worktree'], 'bool_flags': [], 'positionals': []},
    "drag": {'json': True, 'remote': True, 'value_flags': ['from', 'page', 'to', 'worktree'], 'bool_flags': [], 'positionals': []},
    "emulator attach": {'json': True, 'remote': True, 'value_flags': ['worktree'], 'bool_flags': ['focus'], 'positionals': ['device']},
    "emulator ax": {'json': True, 'remote': True, 'value_flags': ['device', 'emulator', 'worktree'], 'bool_flags': [], 'positionals': []},
    "emulator button": {'json': True, 'remote': True, 'value_flags': ['device', 'emulator', 'worktree'], 'bool_flags': [], 'positionals': ['name']},
    "emulator devices": {'json': True, 'remote': True, 'value_flags': ['worktree'], 'bool_flags': [], 'positionals': []},
    "emulator exec": {'json': True, 'remote': True, 'value_flags': ['command', 'device', 'emulator', 'worktree'], 'bool_flags': [], 'positionals': []},
    "emulator gesture": {'json': True, 'remote': True, 'value_flags': ['device', 'emulator', 'worktree'], 'bool_flags': [], 'positionals': ['points']},
    "emulator install": {'json': True, 'remote': True, 'value_flags': ['device', 'emulator', 'worktree'], 'bool_flags': ['reinstall'], 'positionals': ['path']},
    "emulator kill": {'json': True, 'remote': True, 'value_flags': ['device', 'emulator', 'worktree'], 'bool_flags': [], 'positionals': []},
    "emulator launch": {'json': True, 'remote': True, 'value_flags': ['activity', 'device', 'emulator', 'worktree'], 'bool_flags': [], 'positionals': ['package']},
    "emulator list": {'json': True, 'remote': True, 'value_flags': ['worktree'], 'bool_flags': [], 'positionals': []},
    "emulator logcat": {'json': True, 'remote': True, 'value_flags': ['device', 'emulator', 'lines', 'worktree'], 'bool_flags': [], 'positionals': []},
    "emulator permissions": {'json': True, 'remote': True, 'value_flags': ['device', 'emulator', 'worktree'], 'bool_flags': [], 'positionals': ['op', 'package', 'permission']},
    "emulator rotate": {'json': True, 'remote': True, 'value_flags': ['device', 'emulator', 'worktree'], 'bool_flags': [], 'positionals': ['orientation']},
    "emulator shutdown": {'json': True, 'remote': True, 'value_flags': ['device', 'emulator', 'worktree'], 'bool_flags': [], 'positionals': []},
    "emulator tap": {'json': True, 'remote': True, 'value_flags': ['device', 'emulator', 'worktree'], 'bool_flags': [], 'positionals': ['x', 'y']},
    "emulator type": {'json': True, 'remote': True, 'value_flags': ['device', 'emulator', 'worktree'], 'bool_flags': [], 'positionals': ['text']},
    "environment add": {'json': True, 'remote': False, 'value_flags': ['name', 'page', 'pairing-code'], 'bool_flags': [], 'positionals': []},
    "environment cancel-stop": {'json': True, 'remote': False, 'value_flags': ['environment', 'page'], 'bool_flags': [], 'positionals': []},
    "environment forget": {'json': True, 'remote': False, 'value_flags': ['environment', 'page'], 'bool_flags': ['yes'], 'positionals': []},
    "environment list": {'json': True, 'remote': False, 'value_flags': ['page'], 'bool_flags': [], 'positionals': []},
    "environment recover": {'json': True, 'remote': False, 'value_flags': ['environment', 'page'], 'bool_flags': ['accept-changed-state', 'yes'], 'positionals': []},
    "environment rm": {'json': True, 'remote': False, 'value_flags': ['environment', 'page'], 'bool_flags': [], 'positionals': []},
    "environment rollback": {'json': True, 'remote': False, 'value_flags': ['environment', 'page'], 'bool_flags': [], 'positionals': []},
    "environment show": {'json': True, 'remote': False, 'value_flags': ['environment', 'page'], 'bool_flags': [], 'positionals': []},
    "environment status": {'json': True, 'remote': False, 'value_flags': ['environment', 'page'], 'bool_flags': [], 'positionals': []},
    "environment stop": {'json': True, 'remote': False, 'value_flags': ['environment', 'page'], 'bool_flags': ['yes'], 'positionals': []},
    "environment update": {'json': True, 'remote': False, 'value_flags': ['environment', 'page'], 'bool_flags': ['force'], 'positionals': []},
    "eval": {'json': True, 'remote': True, 'value_flags': ['expression', 'page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "exec": {'json': True, 'remote': True, 'value_flags': ['page', 'worktree'], 'bool_flags': ['command'], 'positionals': []},
    "file diff": {'json': True, 'remote': True, 'value_flags': ['worktree'], 'bool_flags': ['focus', 'staged'], 'positionals': ['path']},
    "file open": {'json': True, 'remote': True, 'value_flags': ['column', 'line', 'worktree'], 'bool_flags': ['focus'], 'positionals': ['path']},
    "file open-changed": {'json': True, 'remote': True, 'value_flags': ['mode', 'worktree'], 'bool_flags': ['focus'], 'positionals': []},
    "fill": {'json': True, 'remote': True, 'value_flags': ['element', 'page', 'value', 'worktree'], 'bool_flags': [], 'positionals': []},
    "find": {'json': True, 'remote': True, 'value_flags': ['action', 'locator', 'page', 'text', 'value', 'worktree'], 'bool_flags': [], 'positionals': []},
    "focus": {'json': True, 'remote': True, 'value_flags': ['element', 'page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "forward": {'json': True, 'remote': True, 'value_flags': ['page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "full-screenshot": {'json': True, 'remote': True, 'value_flags': ['format', 'page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "geolocation": {'json': True, 'remote': True, 'value_flags': ['accuracy', 'latitude', 'longitude', 'page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "get": {'json': True, 'remote': True, 'value_flags': ['element', 'page', 'what', 'worktree'], 'bool_flags': [], 'positionals': []},
    "goto": {'json': True, 'remote': True, 'value_flags': ['page', 'url', 'worktree'], 'bool_flags': [], 'positionals': []},
    "highlight": {'json': True, 'remote': True, 'value_flags': ['page', 'selector', 'worktree'], 'bool_flags': [], 'positionals': []},
    "host list": {'json': True, 'remote': False, 'value_flags': ['page'], 'bool_flags': [], 'positionals': []},
    "host name": {'json': True, 'remote': True, 'value_flags': ['name', 'page'], 'bool_flags': [], 'positionals': []},
    "hover": {'json': True, 'remote': True, 'value_flags': ['element', 'page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "inserttext": {'json': True, 'remote': True, 'value_flags': ['page', 'text', 'worktree'], 'bool_flags': [], 'positionals': []},
    "intercept disable": {'json': True, 'remote': True, 'value_flags': ['page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "intercept enable": {'json': True, 'remote': True, 'value_flags': ['page', 'patterns', 'worktree'], 'bool_flags': [], 'positionals': []},
    "intercept list": {'json': True, 'remote': True, 'value_flags': ['page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "is": {'json': True, 'remote': True, 'value_flags': ['element', 'page', 'what', 'worktree'], 'bool_flags': [], 'positionals': []},
    "jira assignee clear": {'json': True, 'remote': True, 'value_flags': ['site'], 'bool_flags': [], 'positionals': ['key']},
    "jira assignee list": {'json': True, 'remote': True, 'value_flags': ['query', 'site'], 'bool_flags': [], 'positionals': ['key']},
    "jira assignee set": {'json': True, 'remote': True, 'value_flags': ['site', 'to-id'], 'bool_flags': [], 'positionals': ['key']},
    "jira comment add": {'json': True, 'remote': True, 'value_flags': ['body', 'body-file', 'site'], 'bool_flags': [], 'positionals': ['key']},
    "jira comment list": {'json': True, 'remote': True, 'value_flags': ['site'], 'bool_flags': [], 'positionals': ['key']},
    "jira connection": {'json': True, 'remote': True, 'value_flags': [], 'bool_flags': [], 'positionals': []},
    "jira create": {'json': True, 'remote': True, 'value_flags': ['body', 'body-file', 'fields-json', 'project', 'site', 'title', 'type', 'user-field'], 'bool_flags': [], 'positionals': []},
    "jira issue": {'json': True, 'remote': True, 'value_flags': ['site'], 'bool_flags': [], 'positionals': ['key']},
    "jira label add": {'json': True, 'remote': True, 'value_flags': ['label', 'site'], 'bool_flags': [], 'positionals': ['key']},
    "jira label rm": {'json': True, 'remote': True, 'value_flags': ['label', 'site'], 'bool_flags': [], 'positionals': ['key']},
    "jira label set": {'json': True, 'remote': True, 'value_flags': ['label', 'site'], 'bool_flags': [], 'positionals': ['key']},
    "jira list": {'json': True, 'remote': True, 'value_flags': ['filter', 'limit', 'site'], 'bool_flags': [], 'positionals': []},
    "jira priority clear": {'json': True, 'remote': True, 'value_flags': ['site'], 'bool_flags': [], 'positionals': ['key']},
    "jira priority list": {'json': True, 'remote': True, 'value_flags': ['site'], 'bool_flags': [], 'positionals': []},
    "jira priority set": {'json': True, 'remote': True, 'value_flags': ['site', 'to-id'], 'bool_flags': [], 'positionals': ['key']},
    "jira project fields": {'json': True, 'remote': True, 'value_flags': ['project', 'site', 'type'], 'bool_flags': [], 'positionals': []},
    "jira project list": {'json': True, 'remote': True, 'value_flags': ['site'], 'bool_flags': [], 'positionals': []},
    "jira project types": {'json': True, 'remote': True, 'value_flags': ['project', 'site'], 'bool_flags': [], 'positionals': []},
    "jira search": {'json': True, 'remote': True, 'value_flags': ['limit', 'site'], 'bool_flags': [], 'positionals': ['jql']},
    "jira status list": {'json': True, 'remote': True, 'value_flags': ['site'], 'bool_flags': [], 'positionals': ['key']},
    "jira status set": {'json': True, 'remote': True, 'value_flags': ['site', 'to', 'to-id'], 'bool_flags': [], 'positionals': ['key']},
    "keypress": {'json': True, 'remote': True, 'value_flags': ['key', 'page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "linear assignee clear": {'json': True, 'remote': True, 'value_flags': ['workspace'], 'bool_flags': ['current'], 'positionals': ['id']},
    "linear assignee set": {'json': True, 'remote': True, 'value_flags': ['to-id', 'workspace'], 'bool_flags': ['current', 'me'], 'positionals': ['id']},
    "linear attach": {'json': True, 'remote': True, 'value_flags': ['title', 'url', 'workspace', 'write-id'], 'bool_flags': ['current'], 'positionals': ['id']},
    "linear comment add": {'json': True, 'remote': True, 'value_flags': ['body', 'body-file', 'reply-to', 'workspace', 'write-id'], 'bool_flags': ['current'], 'positionals': ['id']},
    "linear comment delete": {'json': True, 'remote': True, 'value_flags': ['workspace'], 'bool_flags': [], 'positionals': ['id']},
    "linear comment edit": {'json': True, 'remote': True, 'value_flags': ['body', 'body-file', 'workspace'], 'bool_flags': [], 'positionals': ['id']},
    "linear create": {'json': True, 'remote': True, 'value_flags': ['assignee', 'body', 'body-file', 'due-date', 'estimate', 'label', 'parent', 'priority', 'project', 'state', 'team', 'title', 'workspace', 'write-id'], 'bool_flags': ['parent-current'], 'positionals': []},
    "linear due-date clear": {'json': True, 'remote': True, 'value_flags': ['workspace'], 'bool_flags': ['current'], 'positionals': ['id']},
    "linear due-date set": {'json': True, 'remote': True, 'value_flags': ['to', 'workspace'], 'bool_flags': ['current'], 'positionals': ['id']},
    "linear estimate clear": {'json': True, 'remote': True, 'value_flags': ['workspace'], 'bool_flags': ['current'], 'positionals': ['id']},
    "linear estimate set": {'json': True, 'remote': True, 'value_flags': ['to', 'workspace'], 'bool_flags': ['current'], 'positionals': ['id']},
    "linear issue": {'json': True, 'remote': True, 'value_flags': ['depth', 'workspace'], 'bool_flags': ['activity', 'attachments', 'children', 'comments', 'current', 'full', 'relations'], 'positionals': ['id']},
    "linear label add": {'json': True, 'remote': True, 'value_flags': ['label', 'workspace'], 'bool_flags': ['current'], 'positionals': ['id']},
    "linear label remove": {'json': True, 'remote': True, 'value_flags': ['label', 'workspace'], 'bool_flags': ['current'], 'positionals': ['id']},
    "linear label set": {'json': True, 'remote': True, 'value_flags': ['label', 'workspace'], 'bool_flags': ['current'], 'positionals': ['id']},
    "linear list": {'json': True, 'remote': True, 'value_flags': ['filter', 'limit', 'team', 'workspace'], 'bool_flags': [], 'positionals': []},
    "linear list-issues": {'json': True, 'remote': True, 'value_flags': ['assignee', 'created-at', 'cursor', 'cycle', 'delegate', 'label', 'limit', 'order-by', 'parent-id', 'priority', 'project', 'query', 'release', 'state', 'team', 'updated-at', 'workspace'], 'bool_flags': ['include-archived'], 'positionals': []},
    "linear priority clear": {'json': True, 'remote': True, 'value_flags': ['workspace'], 'bool_flags': ['current'], 'positionals': ['id']},
    "linear priority set": {'json': True, 'remote': True, 'value_flags': ['to', 'workspace'], 'bool_flags': ['current'], 'positionals': ['id']},
    "linear project list": {'json': True, 'remote': True, 'value_flags': ['limit', 'query', 'workspace'], 'bool_flags': [], 'positionals': []},
    "linear relation add": {'json': True, 'remote': True, 'value_flags': ['related', 'type', 'workspace'], 'bool_flags': ['current'], 'positionals': ['id']},
    "linear relation remove": {'json': True, 'remote': True, 'value_flags': ['related', 'type', 'workspace'], 'bool_flags': ['current'], 'positionals': ['id']},
    "linear save-issue": {'json': True, 'remote': True, 'value_flags': ['assignee', 'body', 'body-file', 'description', 'due-date', 'estimate', 'label', 'parent-id', 'priority', 'project', 'state', 'team', 'title', 'workspace', 'write-id'], 'bool_flags': ['current'], 'positionals': ['id']},
    "linear search": {'json': True, 'remote': True, 'value_flags': ['limit', 'workspace'], 'bool_flags': [], 'positionals': ['query']},
    "linear status set": {'json': True, 'remote': True, 'value_flags': ['to', 'workspace'], 'bool_flags': ['current'], 'positionals': ['id']},
    "linear team labels": {'json': True, 'remote': True, 'value_flags': ['team', 'workspace'], 'bool_flags': [], 'positionals': []},
    "linear team list": {'json': True, 'remote': True, 'value_flags': ['workspace'], 'bool_flags': [], 'positionals': []},
    "linear team members": {'json': True, 'remote': True, 'value_flags': ['team', 'workspace'], 'bool_flags': [], 'positionals': []},
    "linear team states": {'json': True, 'remote': True, 'value_flags': ['team', 'workspace'], 'bool_flags': [], 'positionals': []},
    "mouse down": {'json': True, 'remote': True, 'value_flags': ['button', 'page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "mouse move": {'json': True, 'remote': True, 'value_flags': ['page', 'worktree', 'x', 'y'], 'bool_flags': [], 'positionals': []},
    "mouse up": {'json': True, 'remote': True, 'value_flags': ['button', 'page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "mouse wheel": {'json': True, 'remote': True, 'value_flags': ['dx', 'dy', 'page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "network": {'json': True, 'remote': True, 'value_flags': ['limit', 'page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "open": {'json': True, 'remote': True, 'value_flags': [], 'bool_flags': [], 'positionals': []},
    "open-url": {'json': True, 'remote': True, 'value_flags': ['page', 'url', 'worktree'], 'bool_flags': [], 'positionals': []},
    "orchestration ask": {'json': True, 'remote': True, 'value_flags': ['dispatch-capability', 'from', 'options', 'question', 'resume', 'retry-request', 'run', 'timeout-ms', 'to'], 'bool_flags': [], 'positionals': []},
    "orchestration check": {'json': True, 'remote': True, 'value_flags': ['ack', 'retry-request', 'run', 'terminal', 'timeout-ms', 'types'], 'bool_flags': ['all', 'format', 'peek', 'unread', 'wait'], 'positionals': []},
    "orchestration coordinator-start": {'json': True, 'remote': True, 'value_flags': ['from', 'max-concurrent', 'poll-interval-ms', 'spec', 'worktree'], 'bool_flags': [], 'positionals': []},
    "orchestration coordinator-stop": {'json': True, 'remote': True, 'value_flags': [], 'bool_flags': [], 'positionals': []},
    "orchestration dispatch": {'json': True, 'remote': True, 'value_flags': ['from', 'retry-request', 'run', 'task', 'to'], 'bool_flags': ['dry-run', 'inject', 'return-preamble'], 'positionals': []},
    "orchestration dispatch-show": {'json': True, 'remote': True, 'value_flags': ['from', 'task'], 'bool_flags': ['preamble'], 'positionals': []},
    "orchestration gate-create": {'json': True, 'remote': True, 'value_flags': ['from', 'options', 'question', 'retry-request', 'task'], 'bool_flags': [], 'positionals': []},
    "orchestration gate-list": {'json': True, 'remote': True, 'value_flags': ['from', 'run', 'status', 'task'], 'bool_flags': [], 'positionals': []},
    "orchestration gate-resolve": {'json': True, 'remote': True, 'value_flags': ['from', 'id', 'resolution', 'retry-request'], 'bool_flags': [], 'positionals': []},
    "orchestration inbox": {'json': True, 'remote': True, 'value_flags': ['limit', 'terminal'], 'bool_flags': ['full'], 'positionals': []},
    "orchestration reply": {'json': True, 'remote': True, 'value_flags': ['body', 'from', 'id', 'retry-request', 'run'], 'bool_flags': [], 'positionals': []},
    "orchestration request-show": {'json': True, 'remote': True, 'value_flags': ['request'], 'bool_flags': [], 'positionals': []},
    "orchestration reset": {'json': True, 'remote': True, 'value_flags': ['retry-request'], 'bool_flags': ['all', 'messages', 'tasks'], 'positionals': []},
    "orchestration run-create": {'json': True, 'remote': True, 'value_flags': ['from', 'objective', 'retry-request'], 'bool_flags': [], 'positionals': []},
    "orchestration run-current": {'json': True, 'remote': True, 'value_flags': ['from'], 'bool_flags': [], 'positionals': []},
    "orchestration run-list": {'json': True, 'remote': True, 'value_flags': ['cursor', 'limit'], 'bool_flags': [], 'positionals': []},
    "orchestration run-show": {'json': True, 'remote': True, 'value_flags': ['id'], 'bool_flags': [], 'positionals': []},
    "orchestration run-use": {'json': True, 'remote': True, 'value_flags': ['from', 'id', 'retry-request'], 'bool_flags': ['takeover-legacy'], 'positionals': []},
    "orchestration send": {'json': True, 'remote': True, 'value_flags': ['body', 'dispatch-capability', 'dispatch-id', 'files-modified', 'from', 'outcome', 'payload', 'phase', 'priority', 'report-path', 'retry-request', 'run', 'subject', 'task-id', 'thread-id', 'to', 'type'], 'bool_flags': [], 'positionals': []},
    "orchestration task-create": {'json': True, 'remote': True, 'value_flags': ['deps', 'display-name', 'from', 'parent', 'retry-request', 'run', 'spec', 'task-title'], 'bool_flags': [], 'positionals': []},
    "orchestration task-list": {'json': True, 'remote': True, 'value_flags': ['from', 'run', 'status'], 'bool_flags': ['brief', 'ready'], 'positionals': []},
    "orchestration task-update": {'json': True, 'remote': True, 'value_flags': ['from', 'id', 'result', 'retry-request', 'run', 'status'], 'bool_flags': [], 'positionals': []},
    "orchestration worker-abandon": {'json': True, 'remote': True, 'value_flags': ['dispatch', 'retry-request'], 'bool_flags': [], 'positionals': []},
    "orchestration worker-list": {'json': True, 'remote': True, 'value_flags': ['cursor', 'limit', 'run', 'terminal-state'], 'bool_flags': ['include-remote'], 'positionals': []},
    "orchestration worker-read": {'json': True, 'remote': True, 'value_flags': ['cursor', 'dispatch', 'limit', 'source'], 'bool_flags': [], 'positionals': []},
    "orchestration worker-release": {'json': True, 'remote': True, 'value_flags': ['dispatch', 'retry-request'], 'bool_flags': [], 'positionals': []},
    "orchestration worker-retain": {'json': True, 'remote': True, 'value_flags': ['dispatch', 'retry-request'], 'bool_flags': [], 'positionals': []},
    "orchestration worker-show": {'json': True, 'remote': True, 'value_flags': ['dispatch'], 'bool_flags': [], 'positionals': []},
    "orchestration worker-start": {'json': True, 'remote': True, 'value_flags': ['agent', 'base-branch', 'comment', 'deps', 'display-name', 'effort', 'from', 'model', 'name', 'on', 'parent', 'repo', 'retry-of', 'retry-request', 'run', 'setup', 'spec', 'task', 'task-title', 'terminal', 'timeout-ms', 'worktree'], 'bool_flags': [], 'positionals': []},
    "orchestration worker-stop": {'json': True, 'remote': True, 'value_flags': ['dispatch', 'retry-request'], 'bool_flags': [], 'positionals': []},
    "pdf": {'json': True, 'remote': True, 'value_flags': ['page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "profile state exports": {'json': True, 'remote': True, 'value_flags': ['page', 'profile-id'], 'bool_flags': [], 'positionals': []},
    "profile state rollback": {'json': True, 'remote': True, 'value_flags': ['backup', 'page', 'profile-id', 'revision'], 'bool_flags': ['current-json', 'current-sqlite', 'latest-json'], 'positionals': []},
    "project list": {'json': True, 'remote': True, 'value_flags': [], 'bool_flags': [], 'positionals': []},
    "project setup-clone": {'json': True, 'remote': True, 'value_flags': ['destination', 'display-name', 'host', 'project', 'url'], 'bool_flags': [], 'positionals': []},
    "project setup-create": {'json': True, 'remote': True, 'value_flags': ['display-name', 'git-username', 'host', 'kind', 'method', 'path', 'project', 'setup-id', 'state', 'worktree-base-path'], 'bool_flags': [], 'positionals': []},
    "project setup-delete": {'json': True, 'remote': True, 'value_flags': ['host', 'setup'], 'bool_flags': ['force'], 'positionals': []},
    "project setup-existing-folder": {'json': True, 'remote': True, 'value_flags': ['display-name', 'host', 'kind', 'path', 'project'], 'bool_flags': [], 'positionals': []},
    "project setup-update": {'json': True, 'remote': True, 'value_flags': ['display-name', 'git-username', 'host', 'kind', 'method', 'path', 'setup', 'state', 'worktree-base-path'], 'bool_flags': [], 'positionals': []},
    "project setups": {'json': True, 'remote': True, 'value_flags': ['host', 'project'], 'bool_flags': [], 'positionals': []},
    "reference add": {'json': True, 'remote': True, 'value_flags': ['reference-site', 'worktree'], 'bool_flags': [], 'positionals': ['url']},
    "reference find": {'json': True, 'remote': True, 'value_flags': ['limit', 'repo', 'worktree'], 'bool_flags': ['include-archived'], 'positionals': ['query']},
    "reference list": {'json': True, 'remote': True, 'value_flags': ['worktree'], 'bool_flags': [], 'positionals': []},
    "reference remove": {'json': True, 'remote': True, 'value_flags': ['key', 'worktree'], 'bool_flags': [], 'positionals': ['url']},
    "reload": {'json': True, 'remote': True, 'value_flags': ['page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "repo add": {'json': True, 'remote': True, 'value_flags': ['path'], 'bool_flags': [], 'positionals': []},
    "repo list": {'json': True, 'remote': True, 'value_flags': [], 'bool_flags': [], 'positionals': []},
    "repo search-refs": {'json': True, 'remote': True, 'value_flags': ['limit', 'query', 'repo'], 'bool_flags': [], 'positionals': []},
    "repo set": {'json': True, 'remote': True, 'value_flags': ['external-worktree-visibility', 'repo'], 'bool_flags': [], 'positionals': []},
    "repo set-base-ref": {'json': True, 'remote': True, 'value_flags': ['ref', 'repo'], 'bool_flags': [], 'positionals': []},
    "repo show": {'json': True, 'remote': True, 'value_flags': ['repo'], 'bool_flags': [], 'positionals': []},
    "screenshot": {'json': True, 'remote': True, 'value_flags': ['format', 'page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "scroll": {'json': True, 'remote': True, 'value_flags': ['amount', 'direction', 'page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "scrollintoview": {'json': True, 'remote': True, 'value_flags': ['element', 'page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "search": {'json': True, 'remote': True, 'value_flags': ['agent', 'cursor', 'limit', 'path', 'scope', 'since', 'sort'], 'bool_flags': ['debug', 'fresh', 'index-status'], 'positionals': ['query']},
    "select": {'json': True, 'remote': True, 'value_flags': ['element', 'page', 'value', 'worktree'], 'bool_flags': [], 'positionals': []},
    "select-all": {'json': True, 'remote': True, 'value_flags': ['element', 'page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "serve": {'json': True, 'remote': True, 'value_flags': ['page', 'pairing-address', 'port', 'project-root'], 'bool_flags': ['force', 'grant-desktop-control', 'mobile-pairing', 'no-pairing', 'recipe-json', 'supervise'], 'positionals': []},
    "serve restore resume": {'json': True, 'remote': True, 'value_flags': ['page'], 'bool_flags': [], 'positionals': []},
    "serve service install": {'json': True, 'remote': True, 'value_flags': ['command', 'page', 'pairing-address', 'port'], 'bool_flags': ['dry-run'], 'positionals': []},
    "serve service status": {'json': True, 'remote': True, 'value_flags': ['page'], 'bool_flags': [], 'positionals': []},
    "serve service uninstall": {'json': True, 'remote': True, 'value_flags': ['page'], 'bool_flags': [], 'positionals': []},
    "set credentials": {'json': True, 'remote': True, 'value_flags': ['page', 'pass', 'user', 'worktree'], 'bool_flags': [], 'positionals': []},
    "set device": {'json': True, 'remote': True, 'value_flags': ['name', 'page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "set headers": {'json': True, 'remote': True, 'value_flags': ['headers', 'page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "set media": {'json': True, 'remote': True, 'value_flags': ['color-scheme', 'page', 'reduced-motion', 'worktree'], 'bool_flags': [], 'positionals': []},
    "set offline": {'json': True, 'remote': True, 'value_flags': ['page', 'state', 'worktree'], 'bool_flags': [], 'positionals': []},
    "skills get": {'json': True, 'remote': True, 'value_flags': ['reference'], 'bool_flags': ['full', 'references'], 'positionals': ['topic']},
    "skills install": {'json': True, 'remote': True, 'value_flags': ['agent', 'skill'], 'bool_flags': ['all', 'dry-run', 'local'], 'positionals': []},
    "skills installed": {'json': True, 'remote': True, 'value_flags': [], 'bool_flags': [], 'positionals': []},
    "skills list": {'json': True, 'remote': True, 'value_flags': [], 'bool_flags': [], 'positionals': []},
    "skills share": {'json': True, 'remote': True, 'value_flags': ['bundle-name', 'release-notes', 'skill'], 'bool_flags': [], 'positionals': []},
    "skills update": {'json': True, 'remote': True, 'value_flags': ['agent', 'skill'], 'bool_flags': ['all', 'dry-run', 'local'], 'positionals': []},
    "snapshot": {'json': True, 'remote': True, 'value_flags': ['page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "speech openai-key clear": {'json': True, 'remote': True, 'value_flags': [], 'bool_flags': [], 'positionals': []},
    "speech openai-key set": {'json': True, 'remote': True, 'value_flags': [], 'bool_flags': [], 'positionals': []},
    "speech openai-key status": {'json': True, 'remote': True, 'value_flags': [], 'bool_flags': [], 'positionals': []},
    "status": {'json': True, 'remote': True, 'value_flags': [], 'bool_flags': [], 'positionals': []},
    "storage local clear": {'json': True, 'remote': True, 'value_flags': ['page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "storage local get": {'json': True, 'remote': True, 'value_flags': ['key', 'page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "storage local set": {'json': True, 'remote': True, 'value_flags': ['key', 'page', 'value', 'worktree'], 'bool_flags': [], 'positionals': []},
    "storage session clear": {'json': True, 'remote': True, 'value_flags': ['page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "storage session get": {'json': True, 'remote': True, 'value_flags': ['key', 'page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "storage session set": {'json': True, 'remote': True, 'value_flags': ['key', 'page', 'value', 'worktree'], 'bool_flags': [], 'positionals': []},
    "tab close": {'json': True, 'remote': True, 'value_flags': ['index', 'page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "tab create": {'json': True, 'remote': True, 'value_flags': ['profile', 'url', 'worktree'], 'bool_flags': [], 'positionals': []},
    "tab current": {'json': True, 'remote': True, 'value_flags': ['worktree'], 'bool_flags': [], 'positionals': []},
    "tab list": {'json': True, 'remote': True, 'value_flags': ['worktree'], 'bool_flags': ['show-profile'], 'positionals': []},
    "tab profile clone": {'json': True, 'remote': True, 'value_flags': ['page', 'profile', 'worktree'], 'bool_flags': [], 'positionals': []},
    "tab profile create": {'json': True, 'remote': True, 'value_flags': ['label', 'scope'], 'bool_flags': [], 'positionals': []},
    "tab profile delete": {'json': True, 'remote': True, 'value_flags': ['profile'], 'bool_flags': [], 'positionals': []},
    "tab profile list": {'json': True, 'remote': True, 'value_flags': [], 'bool_flags': [], 'positionals': []},
    "tab profile set": {'json': True, 'remote': True, 'value_flags': ['page', 'profile', 'worktree'], 'bool_flags': [], 'positionals': []},
    "tab profile show": {'json': True, 'remote': True, 'value_flags': ['page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "tab profile use-default": {'json': True, 'remote': True, 'value_flags': ['page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "tab show": {'json': True, 'remote': True, 'value_flags': ['page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "tab switch": {'json': True, 'remote': True, 'value_flags': ['index', 'page', 'worktree'], 'bool_flags': ['focus'], 'positionals': []},
    "terminal close": {'json': True, 'remote': True, 'value_flags': ['terminal', 'worktree'], 'bool_flags': ['all', 'tab'], 'positionals': []},
    "terminal create": {'json': True, 'remote': True, 'value_flags': ['command', 'shell', 'title', 'worktree'], 'bool_flags': ['focus'], 'positionals': []},
    "terminal list": {'json': True, 'remote': True, 'value_flags': ['limit', 'worktree'], 'bool_flags': ['include-visual-layouts'], 'positionals': []},
    "terminal read": {'json': True, 'remote': True, 'value_flags': ['cursor', 'limit', 'terminal'], 'bool_flags': ['screen'], 'positionals': []},
    "terminal rename": {'json': True, 'remote': True, 'value_flags': ['terminal', 'title'], 'bool_flags': [], 'positionals': []},
    "terminal send": {'json': True, 'remote': True, 'value_flags': ['retry-request', 'terminal', 'text', 'wait-submit'], 'bool_flags': ['enter', 'interrupt'], 'positionals': []},
    "terminal set-pane-title": {'json': True, 'remote': True, 'value_flags': ['terminal', 'title'], 'bool_flags': [], 'positionals': []},
    "terminal show": {'json': True, 'remote': True, 'value_flags': ['terminal'], 'bool_flags': [], 'positionals': []},
    "terminal split": {'json': True, 'remote': True, 'value_flags': ['command', 'direction', 'terminal'], 'bool_flags': [], 'positionals': []},
    "terminal switch": {'json': True, 'remote': True, 'value_flags': ['terminal'], 'bool_flags': [], 'positionals': []},
    "terminal wait": {'json': True, 'remote': True, 'value_flags': ['for', 'terminal', 'timeout-ms'], 'bool_flags': [], 'positionals': []},
    "terminal-daemon restart": {'json': True, 'remote': True, 'value_flags': ['page'], 'bool_flags': ['yes'], 'positionals': []},
    "terminal-daemon status": {'json': True, 'remote': True, 'value_flags': ['page'], 'bool_flags': [], 'positionals': []},
    "type": {'json': True, 'remote': True, 'value_flags': ['input', 'page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "uncheck": {'json': True, 'remote': True, 'value_flags': ['element', 'page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "upload": {'json': True, 'remote': True, 'value_flags': ['element', 'files', 'page', 'worktree'], 'bool_flags': [], 'positionals': []},
    "viewport": {'json': True, 'remote': True, 'value_flags': ['height', 'page', 'scale', 'width', 'worktree'], 'bool_flags': ['mobile'], 'positionals': []},
    "vm recipe doctor": {'json': True, 'remote': True, 'value_flags': ['page', 'repo-path'], 'bool_flags': ['connect', 'provision'], 'positionals': ['recipe-id']},
    "wait": {'json': True, 'remote': True, 'value_flags': ['fn', 'load', 'page', 'selector', 'state', 'text', 'timeout', 'url', 'worktree'], 'bool_flags': [], 'positionals': []},
    "worktree create": {'json': True, 'remote': True, 'value_flags': ['agent', 'base-branch', 'comment', 'effort', 'gitlab-issue', 'gitlab-mr', 'host', 'issue', 'linear-issue', 'model', 'name', 'parent-worktree', 'pr', 'project', 'project-host-setup', 'prompt', 'reference', 'reference-site', 'repo', 'retry-launch', 'setup', 'surface'], 'bool_flags': ['activate', 'no-parent', 'run-hooks'], 'positionals': []},
    "worktree current": {'json': True, 'remote': True, 'value_flags': [], 'bool_flags': [], 'positionals': []},
    "worktree list": {'json': True, 'remote': True, 'value_flags': ['limit', 'repo'], 'bool_flags': [], 'positionals': []},
    "worktree ps": {'json': True, 'remote': True, 'value_flags': ['limit'], 'bool_flags': [], 'positionals': []},
    "worktree rm": {'json': True, 'remote': True, 'value_flags': ['worktree'], 'bool_flags': ['allow-failed-archive-hook', 'force', 'run-hooks'], 'positionals': []},
    "worktree set": {'json': True, 'remote': True, 'value_flags': ['comment', 'display-name', 'gitlab-issue', 'gitlab-mr', 'issue', 'linear-issue', 'parent-worktree', 'pr', 'workspace-status', 'worktree'], 'bool_flags': ['no-parent', 'read', 'unread'], 'positionals': []},
    "worktree show": {'json': True, 'remote': True, 'value_flags': ['worktree'], 'bool_flags': [], 'positionals': []},
}

class AccountResource(_Resource):
    """Commands under ``orca account``."""

    def add(
        self,
        *,
        agent: Scalar | None = None,
        label: Scalar | None = None,
        integration: Scalar | None = None,
    ) -> Any:
        """Add a managed agent account by signing in on this Orca host.

        CLI: ``orca account add [--agent claude|codex|opencode|devin] [--label <name>] [--integration <id>] [--json]``

        Notes:
            Runs the agent login (`claude login` / `codex login`) in this terminal, then registers the account with the local Orca runtime.
            Codex uses device authorization so the browser can complete sign-in from a different machine.
            OpenCode 2 uses `opencode auth login --standalone` in private XDG directories. Devin uses `devin auth login --force-manual-token-flow`.
            Use --integration <id> to skip the OpenCode integration picker; --label names the saved OpenCode or Devin profile.
            OpenCode and Devin profiles apply to new explicit host agent launches. Direct SSH relay and Windows-hosted WSL selection are not supported; run the command on a headless Orca runtime on that host.
            Sign in with the account you want to add (e.g. use a private/incognito browser window for a second account).
            --agent defaults to claude. Requires the Orca runtime to be running on this machine.

        Examples:
            orca account add
            orca account add --agent codex
        """
        return self._client._invoke("account add", [], [("agent", agent), ("label", label), ("integration", integration)], json=True, remote=True)

    def list(
        self,
        *,
        agent: Scalar | None = None,
    ) -> Any:
        """List managed agent accounts on this Orca host.

        CLI: ``orca account list [--agent opencode|devin] [--json]``

        Notes:
            Lists the accounts on this machine. `--environment` / `--pairing-code` are rejected rather than ignored; run it on the host whose accounts you want to see.

        Examples:
            orca account list
        """
        return self._client._invoke("account list", [], [("agent", agent)], json=True, remote=False)

    def rm(
        self,
        *,
        agent: Scalar,
        account: Scalar,
    ) -> Any:
        """Remove a managed OpenCode or Devin profile and its private data.

        CLI: ``orca account rm --agent opencode|devin --account <id> [--json]``

        Notes:
            Deletes credentials and conversation data in the managed profile. Stop its running agents first. System credentials are never removed.
        """
        return self._client._invoke("account rm", [], [("agent", agent), ("account", account)], json=True, remote=True)

    def select(
        self,
        *,
        agent: Scalar,
        account: Scalar,
    ) -> Any:
        """Select an OpenCode or Devin profile for new agent launches.

        CLI: ``orca account select --agent opencode|devin --account <id|system> [--json]``
        """
        return self._client._invoke("account select", [], [("agent", agent), ("account", account)], json=True, remote=True)

class AgentHooksResource(_Resource):
    """Commands under ``orca agent hooks``."""

    def off(
        self,
        *,
        page: Scalar | None = None,
    ) -> Any:
        """Disable Orca-managed agent status hooks and remove local hook entries.

        CLI: ``orca agent hooks off [--json]``

        Examples:
            orca agent hooks off
        """
        return self._client._invoke("agent hooks off", [], [("page", page)], json=True, remote=True)

    def on(
        self,
        *,
        page: Scalar | None = None,
    ) -> Any:
        """Enable Orca-managed agent status hooks.

        CLI: ``orca agent hooks on [--json]``

        Examples:
            orca agent hooks on
        """
        return self._client._invoke("agent hooks on", [], [("page", page)], json=True, remote=True)

    def prepare_codex(
        self,
        *,
        page: Scalar | None = None,
    ) -> Any:
        """Prepare a WSL pane's Orca-managed Codex home before a shell launch.

        CLI: ``orca agent hooks prepare-codex``
        """
        return self._client._invoke("agent hooks prepare-codex", [], [("page", page)], json=True, remote=True)

    def status(
        self,
        *,
        page: Scalar | None = None,
    ) -> Any:
        """Show whether Orca-managed agent status hooks are enabled.

        CLI: ``orca agent hooks status [--json]``

        Examples:
            orca agent hooks status
            orca agent hooks status --json
        """
        return self._client._invoke("agent hooks status", [], [("page", page)], json=True, remote=True)

class AgentResource(_Resource):
    """Commands under ``orca agent``."""

    @cached_property
    def hooks(self) -> AgentHooksResource:
        """``orca agent hooks`` commands."""
        return AgentHooksResource(self._client)

    def launch(
        self,
        *,
        agent: Scalar,
        worktree: Scalar | None = None,
        prompt: Scalar | None = None,
        model: Scalar | None = None,
        effort: Scalar | None = None,
        surface: Scalar | None = None,
        focus: bool = False,
        retry_launch: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Start an agent in an existing workspace, as a chat or a terminal.

        CLI: ``orca agent launch --agent <id> [--worktree <selector>] [--prompt <text>] [--model <id>] [--effort <level>] [--surface chat|terminal] [--focus] [--retry-launch <operationId>] [--json]``

        Notes:
            Starts the agent the way a new agent tab does: as a chat when your Chat UI setting is on and the agent and host support it, otherwise as a terminal. The result says which (`outcome.kind`) and why (`receipt.detail`).
            --surface chat|terminal picks for this launch instead of your setting. --surface terminal always runs the agent CLI; --surface chat is refused when Orca can establish before starting anything that this agent cannot open as a chat there. If support cannot be checked, the launch can fall back to a terminal. If chat becomes unavailable after creating a workspace, Orca keeps the workspace, setup and default tabs, then opens a terminal; the receipt explains the fallback.
            --worktree defaults to the native folder workspace or worktree containing the current directory. For a new checkout with its agent, use `orca worktree create --agent`.
            --model takes a provider model id and --effort a reasoning effort for that model; --effort requires --model. They apply to either surface.
            The tab opens without switching focus; pass --focus to switch to it.
            If the launch reply is lost, re-issue the same command from the same directory on the same host with --retry-launch <operationId> from the error. Never retry as a fresh launch; older hosts require inspecting the workspace first.

        Examples:
            orca agent launch --agent codex --json
            orca agent launch --agent codex --model gpt-6-astra --effort high --prompt "Write the design doc" --json
            orca agent launch --agent claude --worktree path:/projects/myapp --focus
        """
        return self._client._invoke("agent launch", [], [("agent", agent), ("worktree", worktree), ("prompt", prompt), ("model", model), ("effort", effort), ("surface", surface), ("focus", focus), ("retry-launch", retry_launch), ("page", page)], json=True, remote=True)

class ArtifactsResource(_Resource):
    """Commands under ``orca artifacts``."""

    def delete(
        self,
        id: Scalar,
        *,
        api_url: Scalar | None = None,
    ) -> Any:
        """Delete an artifact owned by the signed-in Orca account.

        CLI: ``orca artifacts delete <id> [--api-url <url>] [--json]``
        """
        return self._client._invoke("artifacts delete", [id], [("api-url", api_url)], json=True, remote=True)

    def list(
        self,
        *,
        api_url: Scalar | None = None,
        cursor: Scalar | None = None,
    ) -> Any:
        """List artifacts owned by the signed-in Orca account.

        CLI: ``orca artifacts list [--cursor <cursor>] [--api-url <url>] [--json]``
        """
        return self._client._invoke("artifacts list", [], [("api-url", api_url), ("cursor", cursor)], json=True, remote=True)

    def share(
        self,
        file: Scalar,
        *,
        api_url: Scalar | None = None,
    ) -> Any:
        """Share an HTML or Markdown file with your Orca account.

        CLI: ``orca artifacts share <file> [--api-url <url>] [--json]``

        Examples:
            orca artifacts share ./report.html
            orca artifacts share ./notes.md --json
        """
        return self._client._invoke("artifacts share", [file], [("api-url", api_url)], json=True, remote=True)

    def unshare(
        self,
        file: Scalar,
        *,
        api_url: Scalar | None = None,
    ) -> Any:
        """Delete the artifact associated with a previously shared file.

        CLI: ``orca artifacts unshare <file> [--api-url <url>] [--json]``
        """
        return self._client._invoke("artifacts unshare", [file], [("api-url", api_url)], json=True, remote=True)

    def update(
        self,
        file: Scalar,
        *,
        api_url: Scalar | None = None,
    ) -> Any:
        """Update a file previously shared from this Orca profile.

        CLI: ``orca artifacts update <file> [--api-url <url>] [--json]``
        """
        return self._client._invoke("artifacts update", [file], [("api-url", api_url)], json=True, remote=True)

class AutomationsResource(_Resource):
    """Commands under ``orca automations``."""

    def create(
        self,
        *,
        name: Scalar,
        prompt: Scalar,
        provider: Scalar,
        trigger: Scalar,
        extra_agent_args: Scalar | None = None,
        precheck: Scalar | None = None,
        precheck_timeout: int | str | None = None,
        repo: Scalar | None = None,
        workspace: Scalar | None = None,
        project: Scalar | None = None,
        host: Scalar | None = None,
        project_host_setup: Scalar | None = None,
        source_context: Scalar | None = None,
        workspace_mode: Scalar | None = None,
        base_branch: Scalar | None = None,
        schedule: Scalar | None = None,
        time: Scalar | None = None,
        day: Scalar | None = None,
        timezone: Scalar | None = None,
        enabled: bool = False,
        disabled: bool = False,
        missed_run_grace_minutes: int | str | None = None,
        reuse_session: bool = False,
        fresh_session: bool = False,
    ) -> Any:
        """Create a scheduled Orca automation.

        CLI: ``orca automations create --name <name> --trigger <preset|cron|rrule> --prompt <text> --provider <agent> [--precheck <command>] [--repo <selector>|--workspace <selector>|--project <id-or-name> [--host <host>]|--project-host-setup <id>] [--json]``

        Notes:
            Trigger accepts hourly, daily, weekdays, weekly, a 5-field cron expression, or an RRULE string.
            When --repo is omitted, the CLI uses the enclosing Orca worktree when one can be resolved from cwd.
            Use --project, or --project-host-setup, to run on a specific project host setup. --project takes the project id or the display name from `orca project list`, and --host is only needed when the project is set up on more than one host.
            --host takes local, ssh:<target-id>, runtime:<environment-id>, or the bare host name `orca host list` prints for any of them.
            Use --source-context with a JSON TaskSourceContext when task/provider data should come from a specific host/account; pass null on edit to clear it.
            Use --workspace to run in an existing worktree; otherwise the automation creates a new worktree per run.
            Use --precheck to run a bounded command before scheduled runs; exit code 0 continues, anything else records a skipped run.
            Use --reuse-session only with existing-workspace automations to submit later runs to the previous live automation session when it is still available. Use --fresh-session to disable reuse.
            Use --extra-agent-args="--model opus --effort high" to add arguments after the host's default agent Arguments on each fresh run. Only model, effort, and a few safe options are accepted (Claude, Codex, CodeBuddy, Cursor, Grok, OMP); extras cannot be combined with --reuse-session. On edit, --extra-agent-args= clears them.

        Examples:
            orca automations create --name "Daily review" --trigger daily --prompt "Review open changes" --provider codex
            orca automations create --name "Weekday triage" --trigger "0 9 * * 1-5" --prompt "Triage issues" --provider claude --repo my-repo
            orca automations create --name "PR review" --trigger hourly --precheck "gh pr list --json number -q .[0].number" --prompt "Review requested PRs" --provider codex
            orca automations create --name "Docs pass" --trigger daily --prompt "Tidy the docs" --provider claude --extra-agent-args="--model opus --effort high --add-dir docs"
        """
        return self._client._invoke("automations create", [], [("name", name), ("prompt", prompt), ("provider", provider), ("extra-agent-args", extra_agent_args), ("precheck", precheck), ("precheck-timeout", precheck_timeout), ("repo", repo), ("workspace", workspace), ("project", project), ("host", host), ("project-host-setup", project_host_setup), ("source-context", source_context), ("workspace-mode", workspace_mode), ("base-branch", base_branch), ("trigger", trigger), ("schedule", schedule), ("time", time), ("day", day), ("timezone", timezone), ("enabled", enabled), ("disabled", disabled), ("missed-run-grace-minutes", missed_run_grace_minutes), ("reuse-session", reuse_session), ("fresh-session", fresh_session)], json=True, remote=True)

    def edit(
        self,
        id: Scalar,
        *,
        name: Scalar | None = None,
        prompt: Scalar | None = None,
        provider: Scalar | None = None,
        extra_agent_args: Scalar | None = None,
        precheck: Scalar | None = None,
        precheck_timeout: int | str | None = None,
        repo: Scalar | None = None,
        workspace: Scalar | None = None,
        project: Scalar | None = None,
        host: Scalar | None = None,
        project_host_setup: Scalar | None = None,
        source_context: Scalar | None = None,
        workspace_mode: Scalar | None = None,
        base_branch: Scalar | None = None,
        trigger: Scalar | None = None,
        schedule: Scalar | None = None,
        time: Scalar | None = None,
        day: Scalar | None = None,
        timezone: Scalar | None = None,
        enabled: bool = False,
        disabled: bool = False,
        missed_run_grace_minutes: int | str | None = None,
        reuse_session: bool = False,
        fresh_session: bool = False,
    ) -> Any:
        """Edit an Orca automation.

        CLI: ``orca automations edit <id> [--name <name>] [--trigger <preset|cron|rrule>] [--json]``

        Examples:
            orca automations edit 2f9e... --disabled
            orca automations edit --id 2f9e... --trigger "30 * * * *" --json
            orca automations edit 2f9e... --extra-agent-args=
        """
        return self._client._invoke("automations edit", [id], [("name", name), ("prompt", prompt), ("provider", provider), ("extra-agent-args", extra_agent_args), ("precheck", precheck), ("precheck-timeout", precheck_timeout), ("repo", repo), ("workspace", workspace), ("project", project), ("host", host), ("project-host-setup", project_host_setup), ("source-context", source_context), ("workspace-mode", workspace_mode), ("base-branch", base_branch), ("trigger", trigger), ("schedule", schedule), ("time", time), ("day", day), ("timezone", timezone), ("enabled", enabled), ("disabled", disabled), ("missed-run-grace-minutes", missed_run_grace_minutes), ("reuse-session", reuse_session), ("fresh-session", fresh_session)], json=True, remote=True)

    def list(
        self,
    ) -> Any:
        """List scheduled Orca automations.

        CLI: ``orca automations list [--json]``

        Examples:
            orca automations list
            orca automations list --json
        """
        return self._client._invoke("automations list", [], [], json=True, remote=True)

    def remove(
        self,
        id: Scalar,
    ) -> Any:
        """Remove an Orca automation and its run history.

        CLI: ``orca automations remove <id> [--json]``

        Examples:
            orca automations remove 2f9e...
            orca automations remove --id 2f9e... --json
        """
        return self._client._invoke("automations remove", [id], [], json=True, remote=True)

    def run(
        self,
        id: Scalar,
    ) -> Any:
        """Run an Orca automation now.

        CLI: ``orca automations run <id> [--json]``

        Notes:
            Use the full automation UUID from orca automations list; shortened prefixes are not accepted.
            A queued or dispatching run has been accepted but may not have a workspace or terminal yet. Use orca automations runs --id <automation-id> to follow its progress.

        Examples:
            orca automations run 497bafa9-5a97-4f85-9e48-2b211b8f31fa
            orca automations run --id 497bafa9-5a97-4f85-9e48-2b211b8f31fa --json
        """
        return self._client._invoke("automations run", [id], [], json=True, remote=True)

    def runs(
        self,
        *,
        id: Scalar | None = None,
        limit: int | str | None = None,
        cursor: Scalar | None = None,
    ) -> Any:
        """List automation run history.

        CLI: ``orca automations runs [--id <automation-id>] [--limit <n>] [--cursor <cursor>] [--json]``

        Notes:
            Without --limit or --cursor, reads the whole history in pages, so a large history from a paired server still fits in its replies.
            With --limit or --cursor, prints one page (newest first, at most 100 runs) and its nextCursor; pass that as --cursor for the next page.

        Examples:
            orca automations runs
            orca automations runs --id 2f9e... --json
            orca automations runs --limit 20 --json
        """
        return self._client._invoke("automations runs", [], [("id", id), ("limit", limit), ("cursor", cursor)], json=True, remote=True)

    def show(
        self,
        id: Scalar,
    ) -> Any:
        """Show one Orca automation.

        CLI: ``orca automations show <id> [--json]``

        Examples:
            orca automations show 2f9e...
            orca automations show --id 2f9e... --json
        """
        return self._client._invoke("automations show", [id], [], json=True, remote=True)

class BrowserIdentityResource(_Resource):
    """Commands under ``orca browser identity``."""

    def get(
        self,
        *,
        page: Scalar | None = None,
    ) -> Any:
        """Show the browser identity configured on this Orca host.

        CLI: ``orca browser identity get [--json]``
        """
        return self._client._invoke("browser identity get", [], [("page", page)], json=True, remote=True)

    def set(
        self,
        *,
        mode: Scalar,
        reset: bool = False,
        page: Scalar | None = None,
    ) -> Any:
        """Choose the browser identity for every page on this Orca host.

        CLI: ``orca browser identity set --mode <clean|native> [--reset] [--json]``
        """
        return self._client._invoke("browser identity set", [], [("mode", mode), ("reset", reset), ("page", page)], json=True, remote=True)

class BrowserResource(_Resource):
    """Commands under ``orca browser``."""

    @cached_property
    def identity(self) -> BrowserIdentityResource:
        """``orca browser identity`` commands."""
        return BrowserIdentityResource(self._client)

class CaptureResource(_Resource):
    """Commands under ``orca capture``."""

    def start(
        self,
        *,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Start capturing console and network events.

        CLI: ``orca capture start [--worktree <selector>] [--json]``
        """
        return self._client._invoke("capture start", [], [("worktree", worktree), ("page", page)], json=True, remote=True)

    def stop(
        self,
        *,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Stop capturing console and network events.

        CLI: ``orca capture stop [--worktree <selector>] [--json]``
        """
        return self._client._invoke("capture stop", [], [("worktree", worktree), ("page", page)], json=True, remote=True)

class ClipboardResource(_Resource):
    """Commands under ``orca clipboard``."""

    def read(
        self,
        *,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Read clipboard contents.

        CLI: ``orca clipboard read [--worktree <selector>] [--json]``
        """
        return self._client._invoke("clipboard read", [], [("worktree", worktree), ("page", page)], json=True, remote=True)

    def write(
        self,
        *,
        text: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Write text to clipboard.

        CLI: ``orca clipboard write --text <text> [--worktree <selector>] [--json]``
        """
        return self._client._invoke("clipboard write", [], [("text", text), ("worktree", worktree), ("page", page)], json=True, remote=True)

class ComputerResource(_Resource):
    """Commands under ``orca computer``."""

    def capabilities(
        self,
    ) -> Any:
        """Show computer-use provider capabilities.

        CLI: ``orca computer capabilities [--json]``
        """
        return self._client._invoke("computer capabilities", [], [], json=True, remote=True)

    def click(
        self,
        *,
        app: Scalar,
        worktree: Scalar | None = None,
        session: Scalar | None = None,
        window_id: Scalar | None = None,
        window_index: int | str | None = None,
        restore_window: bool = False,
        no_screenshot: bool = False,
        element_index: int | str | None = None,
        x: int | str | None = None,
        y: int | str | None = None,
        click_count: int | str | None = None,
        mouse_button: Scalar | None = None,
        modifiers: Scalar | None = None,
    ) -> Any:
        """Click an app element or window coordinate, optionally with modifiers.

        CLI: ``orca computer click --app <app> (--element-index <n> | --x <x> --y <y>) [--window-id <id> | --window-index <n>] [--click-count <n>] [--mouse-button <left|right|middle>] [--modifiers <modifier-chord>] [--restore-window] [--no-screenshot] [--json]``
        """
        return self._client._invoke("computer click", [], [("worktree", worktree), ("session", session), ("app", app), ("window-id", window_id), ("window-index", window_index), ("restore-window", restore_window), ("no-screenshot", no_screenshot), ("element-index", element_index), ("x", x), ("y", y), ("click-count", click_count), ("mouse-button", mouse_button), ("modifiers", modifiers)], json=True, remote=True)

    def drag(
        self,
        *,
        app: Scalar,
        worktree: Scalar | None = None,
        session: Scalar | None = None,
        window_id: Scalar | None = None,
        window_index: int | str | None = None,
        restore_window: bool = False,
        no_screenshot: bool = False,
        from_element_index: int | str | None = None,
        to_element_index: int | str | None = None,
        from_x: int | str | None = None,
        from_y: int | str | None = None,
        to_x: int | str | None = None,
        to_y: int | str | None = None,
    ) -> Any:
        """Drag between app elements or window coordinates.

        CLI: ``orca computer drag --app <app> (--from-element-index <n> --to-element-index <n> | --from-x <x> --from-y <y> --to-x <x> --to-y <y>) [--window-id <id> | --window-index <n>] [--restore-window] [--no-screenshot] [--json]``
        """
        return self._client._invoke("computer drag", [], [("worktree", worktree), ("session", session), ("app", app), ("window-id", window_id), ("window-index", window_index), ("restore-window", restore_window), ("no-screenshot", no_screenshot), ("from-element-index", from_element_index), ("to-element-index", to_element_index), ("from-x", from_x), ("from-y", from_y), ("to-x", to_x), ("to-y", to_y)], json=True, remote=True)

    def get_app_state(
        self,
        *,
        app: Scalar,
        worktree: Scalar | None = None,
        session: Scalar | None = None,
        window_id: Scalar | None = None,
        window_index: int | str | None = None,
        restore_window: bool = False,
        no_screenshot: bool = False,
    ) -> Any:
        """Capture a compact accessibility snapshot of an app.

        CLI: ``orca computer get-app-state --app <name|bundle|pid:N> [--window-id <id> | --window-index <n>] [--worktree <selector> | --session <id>] [--restore-window] [--no-screenshot] [--json]``
        """
        return self._client._invoke("computer get-app-state", [], [("worktree", worktree), ("session", session), ("app", app), ("window-id", window_id), ("window-index", window_index), ("restore-window", restore_window), ("no-screenshot", no_screenshot)], json=True, remote=True)

    def hotkey(
        self,
        *,
        app: Scalar,
        key: Scalar,
        worktree: Scalar | None = None,
        session: Scalar | None = None,
        window_id: Scalar | None = None,
        window_index: int | str | None = None,
        restore_window: bool = False,
        no_screenshot: bool = False,
    ) -> Any:
        """Press a platform-aware key combination.

        CLI: ``orca computer hotkey --app <app> --key <key-combo> [--window-id <id> | --window-index <n>] [--restore-window] [--no-screenshot] [--json]``
        """
        return self._client._invoke("computer hotkey", [], [("worktree", worktree), ("session", session), ("app", app), ("window-id", window_id), ("window-index", window_index), ("restore-window", restore_window), ("no-screenshot", no_screenshot), ("key", key)], json=True, remote=True)

    def list_apps(
        self,
    ) -> Any:
        """List running apps available to computer-use.

        CLI: ``orca computer list-apps [--json]``
        """
        return self._client._invoke("computer list-apps", [], [], json=True, remote=True)

    def list_windows(
        self,
        *,
        app: Scalar,
    ) -> Any:
        """List windows for an app available to computer-use.

        CLI: ``orca computer list-windows --app <name|bundle|pid:N> [--json]``
        """
        return self._client._invoke("computer list-windows", [], [("app", app)], json=True, remote=True)

    def paste_text(
        self,
        *,
        app: Scalar,
        worktree: Scalar | None = None,
        session: Scalar | None = None,
        window_id: Scalar | None = None,
        window_index: int | str | None = None,
        restore_window: bool = False,
        no_screenshot: bool = False,
        text: Scalar | None = None,
        text_stdin: bool = False,
        stdin: str | bytes | None = None,
    ) -> Any:
        """Paste exact text at the current app focus.

        CLI: ``orca computer paste-text --app <app> (--text <text> | --text-stdin) [--window-id <id> | --window-index <n>] [--restore-window] [--no-screenshot] [--json]``
        """
        return self._client._invoke("computer paste-text", [], [("worktree", worktree), ("session", session), ("app", app), ("window-id", window_id), ("window-index", window_index), ("restore-window", restore_window), ("no-screenshot", no_screenshot), ("text", text), ("text-stdin", text_stdin)], json=True, remote=True, stdin=stdin)

    def perform_secondary_action(
        self,
        *,
        app: Scalar,
        element_index: int | str,
        action: Scalar,
        worktree: Scalar | None = None,
        session: Scalar | None = None,
        window_id: Scalar | None = None,
        window_index: int | str | None = None,
        restore_window: bool = False,
        no_screenshot: bool = False,
    ) -> Any:
        """Perform an advertised secondary accessibility action.

        CLI: ``orca computer perform-secondary-action --app <app> --element-index <n> --action <name> [--window-id <id> | --window-index <n>] [--restore-window] [--no-screenshot] [--json]``
        """
        return self._client._invoke("computer perform-secondary-action", [], [("worktree", worktree), ("session", session), ("app", app), ("window-id", window_id), ("window-index", window_index), ("restore-window", restore_window), ("no-screenshot", no_screenshot), ("element-index", element_index), ("action", action)], json=True, remote=True)

    def permissions(
        self,
        *,
        id: Scalar | None = None,
    ) -> Any:
        """Open computer-use permission setup.

        CLI: ``orca computer permissions [--id <accessibility|screenshots>] [--json]``
        """
        return self._client._invoke("computer permissions", [], [("id", id)], json=True, remote=True)

    def press_key(
        self,
        *,
        app: Scalar,
        key: Scalar,
        worktree: Scalar | None = None,
        session: Scalar | None = None,
        window_id: Scalar | None = None,
        window_index: int | str | None = None,
        restore_window: bool = False,
        no_screenshot: bool = False,
    ) -> Any:
        """Press a single key such as Return or Escape.

        CLI: ``orca computer press-key --app <app> --key <key> [--window-id <id> | --window-index <n>] [--restore-window] [--no-screenshot] [--json]``
        """
        return self._client._invoke("computer press-key", [], [("worktree", worktree), ("session", session), ("app", app), ("window-id", window_id), ("window-index", window_index), ("restore-window", restore_window), ("no-screenshot", no_screenshot), ("key", key)], json=True, remote=True)

    def scroll(
        self,
        *,
        app: Scalar,
        direction: Scalar,
        worktree: Scalar | None = None,
        session: Scalar | None = None,
        window_id: Scalar | None = None,
        window_index: int | str | None = None,
        restore_window: bool = False,
        no_screenshot: bool = False,
        element_index: int | str | None = None,
        x: int | str | None = None,
        y: int | str | None = None,
        pages: int | str | None = None,
    ) -> Any:
        """Scroll an app element or window coordinate.

        CLI: ``orca computer scroll --app <app> (--element-index <n> | --x <x> --y <y>) --direction <up|down|left|right> [--window-id <id> | --window-index <n>] [--pages <n>] [--restore-window] [--no-screenshot] [--json]``
        """
        return self._client._invoke("computer scroll", [], [("worktree", worktree), ("session", session), ("app", app), ("window-id", window_id), ("window-index", window_index), ("restore-window", restore_window), ("no-screenshot", no_screenshot), ("element-index", element_index), ("x", x), ("y", y), ("direction", direction), ("pages", pages)], json=True, remote=True)

    def set_value(
        self,
        *,
        app: Scalar,
        element_index: int | str,
        worktree: Scalar | None = None,
        session: Scalar | None = None,
        window_id: Scalar | None = None,
        window_index: int | str | None = None,
        restore_window: bool = False,
        no_screenshot: bool = False,
        value: Scalar | None = None,
        value_stdin: bool = False,
        stdin: str | bytes | None = None,
    ) -> Any:
        """Set the value of a settable app element.

        CLI: ``orca computer set-value --app <app> --element-index <n> (--value <text> | --value-stdin) [--window-id <id> | --window-index <n>] [--restore-window] [--no-screenshot] [--json]``
        """
        return self._client._invoke("computer set-value", [], [("worktree", worktree), ("session", session), ("app", app), ("window-id", window_id), ("window-index", window_index), ("restore-window", restore_window), ("no-screenshot", no_screenshot), ("element-index", element_index), ("value", value), ("value-stdin", value_stdin)], json=True, remote=True, stdin=stdin)

    def type_text(
        self,
        *,
        app: Scalar,
        worktree: Scalar | None = None,
        session: Scalar | None = None,
        window_id: Scalar | None = None,
        window_index: int | str | None = None,
        restore_window: bool = False,
        no_screenshot: bool = False,
        text: Scalar | None = None,
        text_stdin: bool = False,
        stdin: str | bytes | None = None,
    ) -> Any:
        """Type literal text at the current app focus.

        CLI: ``orca computer type-text --app <app> (--text <text> | --text-stdin) [--window-id <id> | --window-index <n>] [--restore-window] [--no-screenshot] [--json]``
        """
        return self._client._invoke("computer type-text", [], [("worktree", worktree), ("session", session), ("app", app), ("window-id", window_id), ("window-index", window_index), ("restore-window", restore_window), ("no-screenshot", no_screenshot), ("text", text), ("text-stdin", text_stdin)], json=True, remote=True, stdin=stdin)

class CookieResource(_Resource):
    """Commands under ``orca cookie``."""

    def delete(
        self,
        *,
        name: int | str,
        domain: Scalar | None = None,
        url: Scalar | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Delete a cookie by name.

        CLI: ``orca cookie delete --name <n> [--domain <d>] [--url <u>] [--worktree <selector>] [--json]``
        """
        return self._client._invoke("cookie delete", [], [("name", name), ("domain", domain), ("url", url), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def get(
        self,
        *,
        url: Scalar | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Get cookies for the active tab (optionally filter by URL).

        CLI: ``orca cookie get [--url <url>] [--worktree <selector>] [--json]``
        """
        return self._client._invoke("cookie get", [], [("url", url), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def set(
        self,
        *,
        name: int | str,
        value: Scalar,
        domain: Scalar | None = None,
        path: Scalar | None = None,
        secure: bool = False,
        httpOnly: bool = False,
        sameSite: Scalar | None = None,
        expires: int | str | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Set a cookie.

        CLI: ``orca cookie set --name <n> --value <v> [--domain <d>] [--path <p>] [--secure] [--httpOnly] [--sameSite <s>] [--expires <epoch>] [--worktree <selector>] [--json]``
        """
        return self._client._invoke("cookie set", [], [("name", name), ("value", value), ("domain", domain), ("path", path), ("secure", secure), ("httpOnly", httpOnly), ("sameSite", sameSite), ("expires", expires), ("worktree", worktree), ("page", page)], json=True, remote=True)

class DiagnosticsResource(_Resource):
    """Commands under ``orca diagnostics``."""

    def memory(
        self,
    ) -> Any:
        """Collect a memory snapshot for Orca and managed terminals.

        CLI: ``orca diagnostics memory [--json]``

        Notes:
            Runs the same host process sweep used by the Resource Usage popover, so call it when you need a point-in-time diagnostic rather than a cheap heartbeat.

        Examples:
            orca diagnostics memory --json
        """
        return self._client._invoke("diagnostics memory", [], [], json=True, remote=True)

class DialogResource(_Resource):
    """Commands under ``orca dialog``."""

    def accept(
        self,
        *,
        text: Scalar | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Accept a browser dialog.

        CLI: ``orca dialog accept [--text <text>] [--worktree <selector>] [--json]``
        """
        return self._client._invoke("dialog accept", [], [("text", text), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def dismiss(
        self,
        *,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Dismiss a browser dialog.

        CLI: ``orca dialog dismiss [--worktree <selector>] [--json]``
        """
        return self._client._invoke("dialog dismiss", [], [("worktree", worktree), ("page", page)], json=True, remote=True)

class EmulatorResource(_Resource):
    """Commands under ``orca emulator``."""

    def attach(
        self,
        device: Scalar | None = None,
        *,
        worktree: Scalar | None = None,
        focus: bool = False,
    ) -> Any:
        """Attach/start helper for a device and make it active for the worktree.

        CLI: ``orca emulator attach [device] [--worktree <selector>] [--focus] [--json]``
        """
        return self._client._invoke("emulator attach", [device], [("worktree", worktree), ("focus", focus)], json=True, remote=True)

    def ax(
        self,
        *,
        device: Scalar | None = None,
        emulator: Scalar | None = None,
        worktree: Scalar | None = None,
    ) -> Any:
        """Dump the accessibility tree (Android uiautomator; iOS serve-sim AX, frames 0..1).

        CLI: ``orca emulator ax [--device <id>] [--worktree <selector>] [--json]``
        """
        return self._client._invoke("emulator ax", [], [("device", device), ("emulator", emulator), ("worktree", worktree)], json=True, remote=True)

    def button(
        self,
        name: Scalar,
        *,
        device: Scalar | None = None,
        emulator: Scalar | None = None,
        worktree: Scalar | None = None,
    ) -> Any:
        """Hardware button (home, side_button, etc.).

        CLI: ``orca emulator button <name> [--device <id>] [--worktree <selector>] [--json]``
        """
        return self._client._invoke("emulator button", [name], [("device", device), ("emulator", emulator), ("worktree", worktree)], json=True, remote=True)

    def devices(
        self,
        *,
        worktree: Scalar | None = None,
    ) -> Any:
        """List all emulator devices/AVDs across iOS and Android.

        CLI: ``orca emulator devices [--worktree <selector>] [--json]``
        """
        return self._client._invoke("emulator devices", [], [("worktree", worktree)], json=True, remote=True)

    def exec(
        self,
        *,
        command: Scalar,
        device: Scalar | None = None,
        emulator: Scalar | None = None,
        worktree: Scalar | None = None,
    ) -> Any:
        """Raw passthrough (e.g. orca emulator exec --command "tap 0.5 0.7" or "ca-debug blended on").

        CLI: ``orca emulator exec --command <cmd> [--device <id>] [--worktree <selector>] [--json]``
        """
        return self._client._invoke("emulator exec", [], [("command", command), ("device", device), ("emulator", emulator), ("worktree", worktree)], json=True, remote=True)

    def gesture(
        self,
        points: Scalar,
        *,
        device: Scalar | None = None,
        emulator: Scalar | None = None,
        worktree: Scalar | None = None,
    ) -> Any:
        """Send a multi-point gesture sequence.

        CLI: ``orca emulator gesture '<json>' [--device <id>] [--worktree <selector>] [--json]``
        """
        return self._client._invoke("emulator gesture", [points], [("device", device), ("emulator", emulator), ("worktree", worktree)], json=True, remote=True)

    def install(
        self,
        path: Scalar,
        *,
        device: Scalar | None = None,
        emulator: Scalar | None = None,
        worktree: Scalar | None = None,
        reinstall: bool = False,
    ) -> Any:
        """Install an APK onto the target Android device.

        CLI: ``orca emulator install <apkPath> [--reinstall] [--device <id>] [--json]``
        """
        return self._client._invoke("emulator install", [path], [("device", device), ("emulator", emulator), ("worktree", worktree), ("reinstall", reinstall)], json=True, remote=True)

    def kill(
        self,
        *,
        device: Scalar | None = None,
        emulator: Scalar | None = None,
        worktree: Scalar | None = None,
    ) -> Any:
        """Stop helper for device.

        CLI: ``orca emulator kill [--device <id>] [--worktree <selector>] [--json]``
        """
        return self._client._invoke("emulator kill", [], [("device", device), ("emulator", emulator), ("worktree", worktree)], json=True, remote=True)

    def launch(
        self,
        package: Scalar,
        *,
        device: Scalar | None = None,
        emulator: Scalar | None = None,
        worktree: Scalar | None = None,
        activity: Scalar | None = None,
    ) -> Any:
        """Launch an Android app by package (and optional activity).

        CLI: ``orca emulator launch <package> [--activity <name>] [--device <id>] [--json]``
        """
        return self._client._invoke("emulator launch", [package], [("device", device), ("emulator", emulator), ("worktree", worktree), ("activity", activity)], json=True, remote=True)

    def list(
        self,
        *,
        worktree: Scalar | None = None,
    ) -> Any:
        """List available/running emulators (Orca-managed + raw serve-sim).

        CLI: ``orca emulator list [--worktree <selector>] [--json]``
        """
        return self._client._invoke("emulator list", [], [("worktree", worktree)], json=True, remote=True)

    def logcat(
        self,
        *,
        device: Scalar | None = None,
        emulator: Scalar | None = None,
        worktree: Scalar | None = None,
        lines: int | str | None = None,
    ) -> Any:
        """Capture a one-shot logcat dump from the Android device.

        CLI: ``orca emulator logcat [--lines <n>] [--device <id>] [--worktree <selector>] [--json]``
        """
        return self._client._invoke("emulator logcat", [], [("device", device), ("emulator", emulator), ("worktree", worktree), ("lines", lines)], json=True, remote=True)

    def permissions(
        self,
        op: Scalar,
        package: Scalar | None = None,
        permission: Scalar | None = None,
        *,
        device: Scalar | None = None,
        emulator: Scalar | None = None,
        worktree: Scalar | None = None,
    ) -> Any:
        """Grant/revoke an Android runtime permission, or reset all runtime grants.

        CLI: ``orca emulator permissions <grant|revoke> <package> <permission> [--device <id>] [--json]``
        """
        return self._client._invoke("emulator permissions", [op, package, permission], [("device", device), ("emulator", emulator), ("worktree", worktree)], json=True, remote=True)

    def rotate(
        self,
        orientation: Scalar,
        *,
        device: Scalar | None = None,
        emulator: Scalar | None = None,
        worktree: Scalar | None = None,
    ) -> Any:
        """Rotate device.

        CLI: ``orca emulator rotate <orientation> [--device <id>] [--worktree <selector>] [--json]``
        """
        return self._client._invoke("emulator rotate", [orientation], [("device", device), ("emulator", emulator), ("worktree", worktree)], json=True, remote=True)

    def shutdown(
        self,
        *,
        device: Scalar | None = None,
        emulator: Scalar | None = None,
        worktree: Scalar | None = None,
    ) -> Any:
        """Stop helper and shut down the simulator device.

        CLI: ``orca emulator shutdown [--device <id>] [--emulator <id>] [--worktree <selector>] [--json]``
        """
        return self._client._invoke("emulator shutdown", [], [("device", device), ("emulator", emulator), ("worktree", worktree)], json=True, remote=True)

    def tap(
        self,
        x: Scalar,
        y: Scalar,
        *,
        device: Scalar | None = None,
        emulator: Scalar | None = None,
        worktree: Scalar | None = None,
    ) -> Any:
        """Tap at normalized 0..1 coords (preferred for single taps).

        CLI: ``orca emulator tap <x> <y> [--device <id>] [--worktree <selector>] [--json]``
        """
        return self._client._invoke("emulator tap", [x, y], [("device", device), ("emulator", emulator), ("worktree", worktree)], json=True, remote=True)

    def type(
        self,
        text: Scalar,
        *,
        device: Scalar | None = None,
        emulator: Scalar | None = None,
        worktree: Scalar | None = None,
    ) -> Any:
        """Type text (US ASCII only).

        CLI: ``orca emulator type <text> [--device <id>] [--worktree <selector>] [--json]``
        """
        return self._client._invoke("emulator type", [text], [("device", device), ("emulator", emulator), ("worktree", worktree)], json=True, remote=True)

class EnvironmentResource(_Resource):
    """Commands under ``orca environment``."""

    def add(
        self,
        *,
        pairing_code: Scalar,
        name: Scalar,
        page: Scalar | None = None,
    ) -> Any:
        """Save a remote Orca runtime environment from a pairing code.

        CLI: ``orca environment add --name <name> --pairing-code <code> [--json]``

        Examples:
            orca environment add --name work-laptop --pairing-code orca://pair?code=...
        """
        return self._client._invoke("environment add", [], [("pairing-code", pairing_code), ("name", name), ("page", page)], json=True, remote=False)

    def cancel_stop(
        self,
        *,
        environment: Scalar,
        page: Scalar | None = None,
    ) -> Any:
        """Withdraw a managed Orca server stop that orcad has not acted on yet.

        CLI: ``orca environment cancel-stop --environment <selector> [--json]``

        Notes:
            --environment names a managed Orca server this machine deployed over SSH (see `orca environment list`); it is a selector here, not a routing flag.
            Runs on this machine’s Orca desktop app, the same action as Settings > Orca on your SSH hosts. A runtime without the SSH registry (headless `orca serve`) refuses it.
        """
        return self._client._invoke("environment cancel-stop", [], [("environment", environment), ("page", page)], json=True, remote=False)

    def forget(
        self,
        *,
        environment: Scalar,
        yes: bool = False,
        page: Scalar | None = None,
    ) -> Any:
        """Unlink a managed Orca server whose SSH host is gone, without stopping it.

        CLI: ``orca environment forget --environment <selector> --yes [--json]``

        Notes:
            Removes the server from this machine without contacting its host, so the SSH host can then be removed. Use it when the host was deleted or can never be reached again. Requires --yes.
            Nothing on the host is stopped: if it comes back, orcad may still be running there, and connecting to it again relinks it.
            --environment names a managed Orca server this machine deployed over SSH (see `orca environment list`); it is a selector here, not a routing flag.
            Runs on this machine’s Orca desktop app, the same action as Settings > Orca on your SSH hosts. A runtime without the SSH registry (headless `orca serve`) refuses it.

        Examples:
            orca environment forget --environment build-box --yes
        """
        return self._client._invoke("environment forget", [], [("environment", environment), ("yes", yes), ("page", page)], json=True, remote=False)

    def list(
        self,
        *,
        page: Scalar | None = None,
    ) -> Any:
        """List saved Orca runtime environments.

        CLI: ``orca environment list [--json]``

        Notes:
            Answers from this machine’s pairing store. --environment and --pairing-code are rejected rather than ignored, because there is no other host that could answer.
        """
        return self._client._invoke("environment list", [], [("page", page)], json=True, remote=False)

    def recover(
        self,
        *,
        environment: Scalar,
        accept_changed_state: bool = False,
        yes: bool = False,
        page: Scalar | None = None,
    ) -> Any:
        """Finish or undo a managed Orca server’s interrupted update, rollback or stop.

        CLI: ``orca environment recover --environment <selector> [--accept-changed-state --yes] [--json]``

        Notes:
            When a rejected build changed profile state, recover refuses rather than restart the previous build over it. --accept-changed-state --yes restores the prelaunch snapshot instead, the same as Restore in Settings > Orca on your SSH hosts; what the rejected build changed is discarded.
            --environment names a managed Orca server this machine deployed over SSH (see `orca environment list`); it is a selector here, not a routing flag.
            Runs on this machine’s Orca desktop app, the same action as Settings > Orca on your SSH hosts. A runtime without the SSH registry (headless `orca serve`) refuses it.

        Examples:
            orca environment recover --environment build-box
            orca environment recover --environment build-box --accept-changed-state --yes
        """
        return self._client._invoke("environment recover", [], [("environment", environment), ("accept-changed-state", accept_changed_state), ("yes", yes), ("page", page)], json=True, remote=False)

    def rm(
        self,
        *,
        environment: Scalar,
        page: Scalar | None = None,
    ) -> Any:
        """Remove one saved Orca runtime environment.

        CLI: ``orca environment rm --environment <selector> [--json]``
        """
        return self._client._invoke("environment rm", [], [("environment", environment), ("page", page)], json=True, remote=False)

    def rollback(
        self,
        *,
        environment: Scalar,
        page: Scalar | None = None,
    ) -> Any:
        """Roll a managed Orca server back to its previous version.

        CLI: ``orca environment rollback --environment <selector> [--json]``

        Notes:
            --environment names a managed Orca server this machine deployed over SSH (see `orca environment list`); it is a selector here, not a routing flag.
            Runs on this machine’s Orca desktop app, the same action as Settings > Orca on your SSH hosts. A runtime without the SSH registry (headless `orca serve`) refuses it.
        """
        return self._client._invoke("environment rollback", [], [("environment", environment), ("page", page)], json=True, remote=False)

    def show(
        self,
        *,
        environment: Scalar,
        page: Scalar | None = None,
    ) -> Any:
        """Show one saved Orca runtime environment.

        CLI: ``orca environment show --environment <selector> [--json]``
        """
        return self._client._invoke("environment show", [], [("environment", environment), ("page", page)], json=True, remote=False)

    def status(
        self,
        *,
        environment: Scalar,
        page: Scalar | None = None,
    ) -> Any:
        """Show a managed Orca server’s active version, terminals and pending work.

        CLI: ``orca environment status --environment <selector> [--json]``

        Notes:
            --environment names a managed Orca server this machine deployed over SSH (see `orca environment list`); it is a selector here, not a routing flag.
            Runs on this machine’s Orca desktop app, the same action as Settings > Orca on your SSH hosts. A runtime without the SSH registry (headless `orca serve`) refuses it.

        Examples:
            orca environment status --environment build-box
        """
        return self._client._invoke("environment status", [], [("environment", environment), ("page", page)], json=True, remote=False)

    def stop(
        self,
        *,
        environment: Scalar,
        yes: bool = False,
        page: Scalar | None = None,
    ) -> Any:
        """Stop a managed Orca server and unlink it from this machine (decommission).

        CLI: ``orca environment stop --environment <selector> --yes [--json]``

        Notes:
            Stops orcad on the SSH host and, once the host proves it exited, removes the server from this machine. Its terminals end. Requires --yes.
            If the host cannot prove orcad exited, the server stays linked and the refusal says why; nothing is removed on a guess. For a host that is gone for good, use `orca environment forget`.
            If this server is the default host for new projects, choose another one first. `orca environment cancel-stop` withdraws a stop orcad has not acted on yet.
            --environment names a managed Orca server this machine deployed over SSH (see `orca environment list`); it is a selector here, not a routing flag.
            Runs on this machine’s Orca desktop app, the same action as Settings > Orca on your SSH hosts. A runtime without the SSH registry (headless `orca serve`) refuses it.

        Examples:
            orca environment stop --environment build-box --yes
        """
        return self._client._invoke("environment stop", [], [("environment", environment), ("yes", yes), ("page", page)], json=True, remote=False)

    def update(
        self,
        *,
        environment: Scalar,
        force: bool = False,
        page: Scalar | None = None,
    ) -> Any:
        """Update a managed Orca server to this build’s version.

        CLI: ``orca environment update --environment <selector> [--force] [--json]``

        Notes:
            Without --force, an update that would restart over running terminals is deferred and reported, not applied.
            --environment names a managed Orca server this machine deployed over SSH (see `orca environment list`); it is a selector here, not a routing flag.
            Runs on this machine’s Orca desktop app, the same action as Settings > Orca on your SSH hosts. A runtime without the SSH registry (headless `orca serve`) refuses it.

        Examples:
            orca environment update --environment build-box
        """
        return self._client._invoke("environment update", [], [("environment", environment), ("force", force), ("page", page)], json=True, remote=False)

class FileResource(_Resource):
    """Commands under ``orca file``."""

    def diff(
        self,
        path: Scalar,
        *,
        staged: bool = False,
        worktree: Scalar | None = None,
        focus: bool = False,
    ) -> Any:
        """Open a file diff as a tab in its worktree without changing your view; --focus brings you to it.

        CLI: ``orca file diff <path> [--staged] [--worktree <selector>] [--focus] [--json]``

        Notes:
            The file opens as a tab in that worktree without changing what you are looking at, even in the worktree on screen. --focus brings you to it; agents should pass --focus only when the user asked to see the file.
            Diffs default to unstaged changes. Pass --staged to open the staged source-control diff.
            The path may be relative to the selected worktree or an absolute path inside that worktree.

        Examples:
            orca file diff src/App.tsx
            orca file diff --path package.json --staged --worktree branch:feature
        """
        return self._client._invoke("file diff", [path], [("staged", staged), ("worktree", worktree), ("focus", focus)], json=True, remote=True)

    def open(
        self,
        path: Scalar,
        *,
        line: int | str | None = None,
        column: int | str | None = None,
        worktree: Scalar | None = None,
        focus: bool = False,
    ) -> Any:
        """Open a file as a tab in its worktree without changing your view; --focus brings you to it.

        CLI: ``orca file open <path> [--line <n> [--column <n>]] [--worktree <selector>] [--focus] [--json]``

        Notes:
            --line and --column use 1-based positions; --column requires --line. Without --focus, the position is applied when you select the file. Markdown opens in source view for positioning. Older hosts open the file without positioning.
            The file opens as a tab in that worktree without changing what you are looking at, even in the worktree on screen. --focus brings you to it; agents should pass --focus only when the user asked to see the file.
            The path may be relative to the selected worktree or an absolute path inside that worktree. When --worktree is omitted, local CLI calls infer the current Orca worktree from cwd.
            A server with no app window (`orca serve`, orcad) cannot open tabs, so this fails with renderer_unavailable and opens nothing.

        Examples:
            orca file open src/App.tsx
            orca file open src/App.tsx --line 42 --column 7 --focus
            orca file open --path docs/readme.md --worktree active --focus
        """
        return self._client._invoke("file open", [path], [("line", line), ("column", column), ("worktree", worktree), ("focus", focus)], json=True, remote=True)

    def open_changed(
        self,
        *,
        mode: Scalar | None = None,
        worktree: Scalar | None = None,
        focus: bool = False,
    ) -> Any:
        """Open all git-changed files as tabs without changing your view; --focus brings you to them.

        CLI: ``orca file open-changed [--mode edit|diff|both] [--worktree <selector>] [--focus] [--json]``

        Notes:
            The files open as tabs in that worktree without changing what you are looking at, even in the worktree on screen. --focus brings you to them; agents should pass --focus only when the user asked to see the files.
            For v1, changed files come from git status for the selected worktree.
            The default mode is diff. Edit mode skips deleted files because there is no file to open.

        Examples:
            orca file open-changed
            orca file open-changed --mode both
            orca file open-changed --mode diff --worktree active
        """
        return self._client._invoke("file open-changed", [], [("mode", mode), ("worktree", worktree), ("focus", focus)], json=True, remote=True)

class HostResource(_Resource):
    """Commands under ``orca host``."""

    def list(
        self,
        *,
        page: Scalar | None = None,
    ) -> Any:
        """List every machine this Orca host can target, and how to name each one.

        CLI: ``orca host list [--json]``

        Notes:
            Answers "what can I target and what do I pass" in one place: this machine, the SSH targets registered on it, and the Orca servers paired with it.
            The three kinds are reached differently. A paired Orca server is a connection, selected with --environment <name>. An SSH target is a machine the connected Orca host reaches, selected with --host ssh:<id>. Passing one where the other belongs is the most common way to get an empty or missing-host answer.
            Commands that take --host also accept any name this list prints, such as --host "this machine" or --host <ssh-target-name>. A name two hosts share is refused with the exact flag for each.
            SSH rows include the detected remote platform after that target has connected (linux, darwin, or win32); disconnected or older targets report platform unknown.
            SSH rows also include whether the target is currently connected and its lifecycle status when known.
            Paired-server rows come from the pairing store and report platform unknown; ask one server directly with `orca host name --environment <name>`.
            SSH targets are read from this machine's own Orca runtime, so this lists that machine's targets and not another server's. Run `orca host list` on the other machine to see the targets registered there.
            --environment and --pairing-code are rejected rather than ignored: paired servers come from this machine’s pairing store, so a routed answer would describe two machines at once.

        Examples:
            orca host list
            orca host list --json
        """
        return self._client._invoke("host list", [], [("page", page)], json=True, remote=False)

    def name(
        self,
        *,
        name: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Show or set the name this Orca runtime reports to connected clients.

        CLI: ``orca host name [--name <name>] [--json]``

        Notes:
            With --name, updates the answering runtime over its authenticated connection. Use an empty value to return to the detected computer name.
            Without --name, prints the name and platform the answering runtime reports.

        Examples:
            orca host name
            orca host name --name build-server
        """
        return self._client._invoke("host name", [], [("name", name), ("page", page)], json=True, remote=True)

class InterceptResource(_Resource):
    """Commands under ``orca intercept``."""

    def disable(
        self,
        *,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Disable request interception.

        CLI: ``orca intercept disable [--worktree <selector>] [--json]``
        """
        return self._client._invoke("intercept disable", [], [("worktree", worktree), ("page", page)], json=True, remote=True)

    def enable(
        self,
        *,
        patterns: Scalar | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Enable request interception (pause matching requests).

        CLI: ``orca intercept enable [--patterns <glob,...>] [--worktree <selector>] [--json]``
        """
        return self._client._invoke("intercept enable", [], [("patterns", patterns), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def list(
        self,
        *,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """List paused (intercepted) requests.

        CLI: ``orca intercept list [--worktree <selector>] [--json]``
        """
        return self._client._invoke("intercept list", [], [("worktree", worktree), ("page", page)], json=True, remote=True)

class JiraAssigneeResource(_Resource):
    """Commands under ``orca jira assignee``."""

    def clear(
        self,
        key: Scalar,
        *,
        site: Scalar | None = None,
    ) -> Any:
        """Clear a Jira issue assignee.

        CLI: ``orca jira assignee clear <key> [--site <id>] [--json]``

        Examples:
            orca jira assignee clear ENG-123 --json
        """
        return self._client._invoke("jira assignee clear", [key], [("site", site)], json=True, remote=True)

    def list(
        self,
        key: Scalar,
        *,
        site: Scalar | None = None,
        query: Scalar | None = None,
    ) -> Any:
        """List assignable users for a Jira issue.

        CLI: ``orca jira assignee list <key> [--query <text>] [--site <id>] [--json]``

        Examples:
            orca jira assignee list ENG-123 --query alex --json
        """
        return self._client._invoke("jira assignee list", [key], [("site", site), ("query", query)], json=True, remote=True)

    def set(
        self,
        key: Scalar,
        *,
        to_id: Scalar,
        site: Scalar | None = None,
    ) -> Any:
        """Assign a Jira issue.

        CLI: ``orca jira assignee set <key> --to-id <accountId> [--site <id>] [--json]``

        Examples:
            orca jira assignee set ENG-123 --to-id 5b10a2844c20165700ede21g --json
        """
        return self._client._invoke("jira assignee set", [key], [("site", site), ("to-id", to_id)], json=True, remote=True)

class JiraCommentResource(_Resource):
    """Commands under ``orca jira comment``."""

    def add(
        self,
        key: Scalar,
        *,
        site: Scalar | None = None,
        body: Scalar | None = None,
        body_file: Scalar | None = None,
        stdin: str | bytes | None = None,
    ) -> Any:
        """Comment on a Jira issue.

        CLI: ``orca jira comment add <key> (--body <text> | --body-file <path|->) [--site <id>] [--json]``

        Examples:
            orca jira comment add ENG-123 --body "Fix is on staging"
        """
        return self._client._invoke("jira comment add", [key], [("site", site), ("body", body), ("body-file", body_file)], json=True, remote=True, stdin=stdin)

    def list(
        self,
        key: Scalar,
        *,
        site: Scalar | None = None,
    ) -> Any:
        """List comments on a Jira issue.

        CLI: ``orca jira comment list <key> [--site <id>] [--json]``

        Examples:
            orca jira comment list ENG-123 --json
        """
        return self._client._invoke("jira comment list", [key], [("site", site)], json=True, remote=True)

class JiraLabelResource(_Resource):
    """Commands under ``orca jira label``."""

    def add(
        self,
        key: Scalar,
        *,
        label: Scalar | Sequence[Scalar],
        site: Scalar | None = None,
    ) -> Any:
        """Add labels to a Jira issue.

        CLI: ``orca jira label add <key> --label <name>... [--site <id>] [--json]``

        Examples:
            orca jira label add ENG-123 --label backend --json
        """
        return self._client._invoke("jira label add", [key], [("site", site), ("label", label)], json=True, remote=True)

    def rm(
        self,
        key: Scalar,
        *,
        label: Scalar | Sequence[Scalar],
        site: Scalar | None = None,
    ) -> Any:
        """Remove labels from a Jira issue.

        CLI: ``orca jira label rm <key> --label <name>... [--site <id>] [--json]``

        Examples:
            orca jira label rm ENG-123 --label backend --json
        """
        return self._client._invoke("jira label rm", [key], [("site", site), ("label", label)], json=True, remote=True)

    def set(
        self,
        key: Scalar,
        *,
        label: Scalar | Sequence[Scalar],
        site: Scalar | None = None,
    ) -> Any:
        """Replace the labels on a Jira issue.

        CLI: ``orca jira label set <key> --label <name> [--label <name>...] [--site <id>] [--json]``

        Examples:
            orca jira label set ENG-123 --label backend --label p1 --json
        """
        return self._client._invoke("jira label set", [key], [("site", site), ("label", label)], json=True, remote=True)

class JiraPriorityResource(_Resource):
    """Commands under ``orca jira priority``."""

    def clear(
        self,
        key: Scalar,
        *,
        site: Scalar | None = None,
    ) -> Any:
        """Clear a Jira issue priority.

        CLI: ``orca jira priority clear <key> [--site <id>] [--json]``

        Examples:
            orca jira priority clear ENG-123 --json
        """
        return self._client._invoke("jira priority clear", [key], [("site", site)], json=True, remote=True)

    def list(
        self,
        *,
        site: Scalar | None = None,
    ) -> Any:
        """List Jira priorities.

        CLI: ``orca jira priority list [--site <id>] [--json]``

        Examples:
            orca jira priority list --json
        """
        return self._client._invoke("jira priority list", [], [("site", site)], json=True, remote=True)

    def set(
        self,
        key: Scalar,
        *,
        to_id: Scalar,
        site: Scalar | None = None,
    ) -> Any:
        """Set a Jira issue priority.

        CLI: ``orca jira priority set <key> --to-id <priorityId> [--site <id>] [--json]``

        Examples:
            orca jira priority set ENG-123 --to-id 2 --json
        """
        return self._client._invoke("jira priority set", [key], [("site", site), ("to-id", to_id)], json=True, remote=True)

class JiraProjectResource(_Resource):
    """Commands under ``orca jira project``."""

    def fields(
        self,
        *,
        project: Scalar,
        type: Scalar,
        site: Scalar | None = None,
    ) -> Any:
        """List create fields for a Jira project and issue type.

        CLI: ``orca jira project fields --project <idOrKey> --type <id> [--site <id>] [--json]``

        Examples:
            orca jira project fields --project ENG --type 10001 --json
        """
        return self._client._invoke("jira project fields", [], [("site", site), ("project", project), ("type", type)], json=True, remote=True)

    def list(
        self,
        *,
        site: Scalar | None = None,
    ) -> Any:
        """List Jira projects.

        CLI: ``orca jira project list [--site <id>] [--json]``

        Examples:
            orca jira project list --json
        """
        return self._client._invoke("jira project list", [], [("site", site)], json=True, remote=True)

    def types(
        self,
        *,
        project: Scalar,
        site: Scalar | None = None,
    ) -> Any:
        """List Jira issue types for a project.

        CLI: ``orca jira project types --project <idOrKey> [--site <id>] [--json]``

        Examples:
            orca jira project types --project ENG --json
        """
        return self._client._invoke("jira project types", [], [("site", site), ("project", project)], json=True, remote=True)

class JiraStatusResource(_Resource):
    """Commands under ``orca jira status``."""

    def list(
        self,
        key: Scalar,
        *,
        site: Scalar | None = None,
    ) -> Any:
        """List available transitions for a Jira issue.

        CLI: ``orca jira status list <key> [--site <id>] [--json]``

        Examples:
            orca jira status list ENG-123 --json
        """
        return self._client._invoke("jira status list", [key], [("site", site)], json=True, remote=True)

    def set(
        self,
        key: Scalar,
        *,
        site: Scalar | None = None,
        to: Scalar | None = None,
        to_id: Scalar | None = None,
    ) -> Any:
        """Transition a Jira issue.

        CLI: ``orca jira status set <key> (--to <name> | --to-id <transitionId>) [--site <id>] [--json]``

        Examples:
            orca jira status set ENG-123 --to "In Review"
            orca jira status set ENG-123 --to-id 31 --json
        """
        return self._client._invoke("jira status set", [key], [("site", site), ("to", to), ("to-id", to_id)], json=True, remote=True)

class JiraResource(_Resource):
    """Commands under ``orca jira``."""

    @cached_property
    def assignee(self) -> JiraAssigneeResource:
        """``orca jira assignee`` commands."""
        return JiraAssigneeResource(self._client)

    @cached_property
    def comment(self) -> JiraCommentResource:
        """``orca jira comment`` commands."""
        return JiraCommentResource(self._client)

    @cached_property
    def label(self) -> JiraLabelResource:
        """``orca jira label`` commands."""
        return JiraLabelResource(self._client)

    @cached_property
    def priority(self) -> JiraPriorityResource:
        """``orca jira priority`` commands."""
        return JiraPriorityResource(self._client)

    @cached_property
    def project(self) -> JiraProjectResource:
        """``orca jira project`` commands."""
        return JiraProjectResource(self._client)

    @cached_property
    def status(self) -> JiraStatusResource:
        """``orca jira status`` commands."""
        return JiraStatusResource(self._client)

    def connection(
        self,
    ) -> Any:
        """List saved Jira site connections.

        CLI: ``orca jira connection [--json]``

        Notes:
            Reports saved connections, not verified Jira access or agent MCP authentication.
        """
        return self._client._invoke("jira connection", [], [], json=True, remote=True)

    def create(
        self,
        *,
        project: Scalar,
        type: Scalar,
        title: Scalar,
        site: Scalar | None = None,
        body: Scalar | None = None,
        body_file: Scalar | None = None,
        fields_json: Scalar | None = None,
        user_field: Scalar | Sequence[Scalar] | None = None,
        stdin: str | bytes | None = None,
    ) -> Any:
        """Create a Jira issue.

        CLI: ``orca jira create --project <idOrKey> --type <issueTypeId> --title <text> [--body <text> | --body-file <path|->] [--fields-json <json>] [--user-field <key>...] [--site <id>] [--json]``

        Examples:
            orca jira create --project ENG --type 10001 --title "Fix login redirect" --json
        """
        return self._client._invoke("jira create", [], [("site", site), ("project", project), ("type", type), ("title", title), ("body", body), ("body-file", body_file), ("fields-json", fields_json), ("user-field", user_field)], json=True, remote=True, stdin=stdin)

    def issue(
        self,
        key: Scalar,
        *,
        site: Scalar | None = None,
    ) -> Any:
        """Read a Jira issue.

        CLI: ``orca jira issue <key> [--site <id>] [--json]``

        Examples:
            orca jira issue ENG-123
            orca jira issue ENG-123 --json
        """
        return self._client._invoke("jira issue", [key], [("site", site)], json=True, remote=True)

    def list(
        self,
        *,
        site: Scalar | None = None,
        filter: Scalar | None = None,
        limit: int | str | None = None,
    ) -> Any:
        """List Jira issues for task triage.

        CLI: ``orca jira list [--filter assigned|reported|all|done] [--limit <n>] [--site <id>] [--json]``

        Examples:
            orca jira list --filter assigned --limit 10 --json
        """
        return self._client._invoke("jira list", [], [("site", site), ("filter", filter), ("limit", limit)], json=True, remote=True)

    def search(
        self,
        jql: Scalar,
        *,
        site: Scalar | None = None,
        limit: int | str | None = None,
    ) -> Any:
        """Search Jira issues with JQL.

        CLI: ``orca jira search <jql> [--limit <n>] [--site <id>] [--json]``

        Examples:
            orca jira search "project = ENG AND status = 'In Progress'"
            orca jira search "assignee = currentUser() AND updated >= -1d" --json
        """
        return self._client._invoke("jira search", [jql], [("site", site), ("limit", limit)], json=True, remote=True)

class LinearAssigneeResource(_Resource):
    """Commands under ``orca linear assignee``."""

    def clear(
        self,
        id: Scalar | None = None,
        *,
        current: bool = False,
        workspace: Scalar | None = None,
    ) -> Any:
        """Clear a Linear issue assignee.

        CLI: ``orca linear assignee clear [<id>] [--current] [--workspace <id>] [--json]``

        Examples:
            orca linear assignee clear ENG-123 --json
        """
        return self._client._invoke("linear assignee clear", [id], [("current", current), ("workspace", workspace)], json=True, remote=True)

    def set(
        self,
        id: Scalar | None = None,
        *,
        current: bool = False,
        me: bool = False,
        to_id: Scalar | None = None,
        workspace: Scalar | None = None,
    ) -> Any:
        """Assign a Linear issue.

        CLI: ``orca linear assignee set [<id>] [--current] (--me | --to-id <userId>) [--workspace <id>] [--json]``

        Examples:
            orca linear assignee set --current --me --json
        """
        return self._client._invoke("linear assignee set", [id], [("current", current), ("me", me), ("to-id", to_id), ("workspace", workspace)], json=True, remote=True)

class LinearCommentResource(_Resource):
    """Commands under ``orca linear comment``."""

    def add(
        self,
        id: Scalar | None = None,
        *,
        current: bool = False,
        body: Scalar | None = None,
        body_file: Scalar | None = None,
        reply_to: Scalar | None = None,
        write_id: Scalar | None = None,
        workspace: Scalar | None = None,
        stdin: str | bytes | None = None,
    ) -> Any:
        """Add a comment to a Linear issue.

        CLI: ``orca linear comment add [<id>] [--current] (--body <text> | --body-file <path|->) [--reply-to <commentId>] [--write-id <uuid>] [--workspace <id>] [--json]``

        Notes:
            Use --body-file - to read multiline comment bodies from stdin.

        Examples:
            orca linear comment add ENG-123 --body "Implementation is ready for review."
            orca linear comment add --current --body-file - --json
        """
        return self._client._invoke("linear comment add", [id], [("current", current), ("body", body), ("body-file", body_file), ("reply-to", reply_to), ("write-id", write_id), ("workspace", workspace)], json=True, remote=True, stdin=stdin)

    def delete(
        self,
        id: Scalar,
        *,
        workspace: Scalar | None = None,
    ) -> Any:
        """Delete a Linear comment.

        CLI: ``orca linear comment delete <commentId> [--workspace <id>] [--json]``

        Notes:
            Comment ids come from `comment add` output or `orca linear issue <id> --comments --json`.

        Examples:
            orca linear comment delete <commentId> --json
        """
        return self._client._invoke("linear comment delete", [id], [("workspace", workspace)], json=True, remote=True)

    def edit(
        self,
        id: Scalar,
        *,
        body: Scalar | None = None,
        body_file: Scalar | None = None,
        workspace: Scalar | None = None,
        stdin: str | bytes | None = None,
    ) -> Any:
        """Replace the body of a Linear comment.

        CLI: ``orca linear comment edit <commentId> (--body <text> | --body-file <path|->) [--workspace <id>] [--json]``

        Notes:
            Comment ids come from `comment add` output or `orca linear issue <id> --comments --json`.
            Linear only lets a comment be edited by its author.

        Examples:
            orca linear comment edit <commentId> --body "Updated: ready for review."
            orca linear comment edit <commentId> --body-file - --json
        """
        return self._client._invoke("linear comment edit", [id], [("body", body), ("body-file", body_file), ("workspace", workspace)], json=True, remote=True, stdin=stdin)

class LinearDueDateResource(_Resource):
    """Commands under ``orca linear due-date``."""

    def clear(
        self,
        id: Scalar | None = None,
        *,
        current: bool = False,
        workspace: Scalar | None = None,
    ) -> Any:
        """Clear a Linear issue due date.

        CLI: ``orca linear due-date clear [<id>] [--current] [--workspace <id>] [--json]``

        Examples:
            orca linear due-date clear ENG-123 --json
        """
        return self._client._invoke("linear due-date clear", [id], [("current", current), ("workspace", workspace)], json=True, remote=True)

    def set(
        self,
        id: Scalar | None = None,
        *,
        to: Scalar,
        current: bool = False,
        workspace: Scalar | None = None,
    ) -> Any:
        """Set a Linear issue due date.

        CLI: ``orca linear due-date set [<id>] [--current] --to <yyyy-mm-dd> [--workspace <id>] [--json]``

        Examples:
            orca linear due-date set --current --to 2026-06-30 --json
        """
        return self._client._invoke("linear due-date set", [id], [("current", current), ("to", to), ("workspace", workspace)], json=True, remote=True)

class LinearEstimateResource(_Resource):
    """Commands under ``orca linear estimate``."""

    def clear(
        self,
        id: Scalar | None = None,
        *,
        current: bool = False,
        workspace: Scalar | None = None,
    ) -> Any:
        """Clear a Linear issue estimate.

        CLI: ``orca linear estimate clear [<id>] [--current] [--workspace <id>] [--json]``

        Examples:
            orca linear estimate clear ENG-123 --json
        """
        return self._client._invoke("linear estimate clear", [id], [("current", current), ("workspace", workspace)], json=True, remote=True)

    def set(
        self,
        id: Scalar | None = None,
        *,
        to: int | str,
        current: bool = False,
        workspace: Scalar | None = None,
    ) -> Any:
        """Set a Linear issue estimate.

        CLI: ``orca linear estimate set [<id>] [--current] --to <number> [--workspace <id>] [--json]``

        Examples:
            orca linear estimate set --current --to 3 --json
        """
        return self._client._invoke("linear estimate set", [id], [("current", current), ("to", to), ("workspace", workspace)], json=True, remote=True)

class LinearLabelResource(_Resource):
    """Commands under ``orca linear label``."""

    def add(
        self,
        id: Scalar | None = None,
        *,
        label: Scalar,
        current: bool = False,
        workspace: Scalar | None = None,
    ) -> Any:
        """Add labels to a Linear issue.

        CLI: ``orca linear label add [<id>] [--current] --label <labelId-or-exact-name>... [--workspace <id>] [--json]``

        Examples:
            orca linear label add --current --label Bug --json
        """
        return self._client._invoke("linear label add", [id], [("current", current), ("label", label), ("workspace", workspace)], json=True, remote=True)

    def remove(
        self,
        id: Scalar | None = None,
        *,
        label: Scalar,
        current: bool = False,
        workspace: Scalar | None = None,
    ) -> Any:
        """Remove labels from a Linear issue.

        CLI: ``orca linear label remove [<id>] [--current] --label <labelId-or-exact-name>... [--workspace <id>] [--json]``

        Examples:
            orca linear label remove --current --label Bug --json
        """
        return self._client._invoke("linear label remove", [id], [("current", current), ("label", label), ("workspace", workspace)], json=True, remote=True)

    def set(
        self,
        id: Scalar | None = None,
        *,
        label: Scalar,
        current: bool = False,
        workspace: Scalar | None = None,
    ) -> Any:
        """Replace labels on a Linear issue.

        CLI: ``orca linear label set [<id>] [--current] --label <labelId-or-exact-name>... [--workspace <id>] [--json]``

        Examples:
            orca linear label set ENG-123 --label Bug --json
        """
        return self._client._invoke("linear label set", [id], [("current", current), ("label", label), ("workspace", workspace)], json=True, remote=True)

class LinearPriorityResource(_Resource):
    """Commands under ``orca linear priority``."""

    def clear(
        self,
        id: Scalar | None = None,
        *,
        current: bool = False,
        workspace: Scalar | None = None,
    ) -> Any:
        """Clear a Linear issue priority.

        CLI: ``orca linear priority clear [<id>] [--current] [--workspace <id>] [--json]``

        Examples:
            orca linear priority clear ENG-123 --json
        """
        return self._client._invoke("linear priority clear", [id], [("current", current), ("workspace", workspace)], json=True, remote=True)

    def set(
        self,
        id: Scalar | None = None,
        *,
        to: Scalar,
        current: bool = False,
        workspace: Scalar | None = None,
    ) -> Any:
        """Set a Linear issue priority.

        CLI: ``orca linear priority set [<id>] [--current] --to none|low|medium|high|urgent [--workspace <id>] [--json]``

        Examples:
            orca linear priority set --current --to high --json
        """
        return self._client._invoke("linear priority set", [id], [("current", current), ("to", to), ("workspace", workspace)], json=True, remote=True)

class LinearProjectResource(_Resource):
    """Commands under ``orca linear project``."""

    def list(
        self,
        *,
        query: Scalar | None = None,
        limit: int | str | None = None,
        workspace: Scalar | None = None,
    ) -> Any:
        """List connected Linear projects.

        CLI: ``orca linear project list [--query <text>] [--limit <n>] [--workspace <id>|all] [--json]``

        Examples:
            orca linear project list --query launch --json
            orca linear project list --workspace all --json
        """
        return self._client._invoke("linear project list", [], [("query", query), ("limit", limit), ("workspace", workspace)], json=True, remote=True)

class LinearRelationResource(_Resource):
    """Commands under ``orca linear relation``."""

    def add(
        self,
        id: Scalar | None = None,
        *,
        related: Scalar,
        type: Scalar,
        current: bool = False,
        workspace: Scalar | None = None,
    ) -> Any:
        """Add a Linear issue relation.

        CLI: ``orca linear relation add [<id>] [--current] --related <issue> --type blocks|blocked-by|related|duplicate-of [--workspace <id>] [--json]``

        Examples:
            orca linear relation add ENG-1 --related ENG-2 --type blocks --json
            orca linear relation add --current --related ENG-2 --type blocked-by --json
        """
        return self._client._invoke("linear relation add", [id], [("current", current), ("related", related), ("type", type), ("workspace", workspace)], json=True, remote=True)

    def remove(
        self,
        id: Scalar | None = None,
        *,
        related: Scalar,
        type: Scalar,
        current: bool = False,
        workspace: Scalar | None = None,
    ) -> Any:
        """Remove a Linear issue relation.

        CLI: ``orca linear relation remove [<id>] [--current] --related <issue> --type blocks|blocked-by|related|duplicate-of [--workspace <id>] [--json]``

        Examples:
            orca linear relation remove ENG-1 --related ENG-2 --type related --json
        """
        return self._client._invoke("linear relation remove", [id], [("current", current), ("related", related), ("type", type), ("workspace", workspace)], json=True, remote=True)

class LinearStatusResource(_Resource):
    """Commands under ``orca linear status``."""

    def set(
        self,
        id: Scalar | None = None,
        *,
        to: Scalar,
        current: bool = False,
        workspace: Scalar | None = None,
    ) -> Any:
        """Set a Linear issue status.

        CLI: ``orca linear status set [<id>] [--current] --to <state> [--workspace <id>] [--json]``

        Examples:
            orca linear status set ENG-123 --to "In Review"
            orca linear status set --current --to Done --json
        """
        return self._client._invoke("linear status set", [id], [("current", current), ("to", to), ("workspace", workspace)], json=True, remote=True)

class LinearTeamResource(_Resource):
    """Commands under ``orca linear team``."""

    def labels(
        self,
        *,
        team: Scalar,
        workspace: Scalar | None = None,
    ) -> Any:
        """List Linear team labels.

        CLI: ``orca linear team labels --team <key|id> [--workspace <id>] [--json]``

        Examples:
            orca linear team labels --team ENG --json
        """
        return self._client._invoke("linear team labels", [], [("team", team), ("workspace", workspace)], json=True, remote=True)

    def list(
        self,
        *,
        workspace: Scalar | None = None,
    ) -> Any:
        """List connected Linear teams.

        CLI: ``orca linear team list [--workspace <id>|all] [--json]``

        Examples:
            orca linear team list --workspace all --json
        """
        return self._client._invoke("linear team list", [], [("workspace", workspace)], json=True, remote=True)

    def members(
        self,
        *,
        team: Scalar,
        workspace: Scalar | None = None,
    ) -> Any:
        """List Linear team members.

        CLI: ``orca linear team members --team <key|id> [--workspace <id>] [--json]``

        Examples:
            orca linear team members --team ENG --json
        """
        return self._client._invoke("linear team members", [], [("team", team), ("workspace", workspace)], json=True, remote=True)

    def states(
        self,
        *,
        team: Scalar,
        workspace: Scalar | None = None,
    ) -> Any:
        """List Linear team workflow states.

        CLI: ``orca linear team states --team <key|id> [--workspace <id>] [--json]``

        Examples:
            orca linear team states --team ENG --json
        """
        return self._client._invoke("linear team states", [], [("team", team), ("workspace", workspace)], json=True, remote=True)

class LinearResource(_Resource):
    """Commands under ``orca linear``."""

    @cached_property
    def assignee(self) -> LinearAssigneeResource:
        """``orca linear assignee`` commands."""
        return LinearAssigneeResource(self._client)

    @cached_property
    def comment(self) -> LinearCommentResource:
        """``orca linear comment`` commands."""
        return LinearCommentResource(self._client)

    @cached_property
    def due_date(self) -> LinearDueDateResource:
        """``orca linear due-date`` commands."""
        return LinearDueDateResource(self._client)

    @cached_property
    def estimate(self) -> LinearEstimateResource:
        """``orca linear estimate`` commands."""
        return LinearEstimateResource(self._client)

    @cached_property
    def label(self) -> LinearLabelResource:
        """``orca linear label`` commands."""
        return LinearLabelResource(self._client)

    @cached_property
    def priority(self) -> LinearPriorityResource:
        """``orca linear priority`` commands."""
        return LinearPriorityResource(self._client)

    @cached_property
    def project(self) -> LinearProjectResource:
        """``orca linear project`` commands."""
        return LinearProjectResource(self._client)

    @cached_property
    def relation(self) -> LinearRelationResource:
        """``orca linear relation`` commands."""
        return LinearRelationResource(self._client)

    @cached_property
    def status(self) -> LinearStatusResource:
        """``orca linear status`` commands."""
        return LinearStatusResource(self._client)

    @cached_property
    def team(self) -> LinearTeamResource:
        """``orca linear team`` commands."""
        return LinearTeamResource(self._client)

    def attach(
        self,
        id: Scalar | None = None,
        *,
        url: Scalar,
        current: bool = False,
        title: Scalar | None = None,
        write_id: Scalar | None = None,
        workspace: Scalar | None = None,
    ) -> Any:
        """Attach a link to a Linear issue.

        CLI: ``orca linear attach [<id>] [--current] --url <url> [--title <title>] [--write-id <uuid>] [--workspace <id>] [--json]``

        Examples:
            orca linear attach ENG-123 --url https://example.com/review/123 --title "PR/MR link"
            orca linear attach --current --url https://example.com/review/123 --json
        """
        return self._client._invoke("linear attach", [id], [("current", current), ("url", url), ("title", title), ("write-id", write_id), ("workspace", workspace)], json=True, remote=True)

    def create(
        self,
        *,
        title: Scalar,
        body: Scalar | None = None,
        body_file: Scalar | None = None,
        team: Scalar | None = None,
        project: Scalar | None = None,
        state: Scalar | None = None,
        assignee: Scalar | None = None,
        priority: Scalar | None = None,
        estimate: int | str | None = None,
        due_date: Scalar | None = None,
        label: Scalar | None = None,
        parent: Scalar | None = None,
        parent_current: bool = False,
        write_id: Scalar | None = None,
        workspace: Scalar | None = None,
        stdin: str | bytes | None = None,
    ) -> Any:
        """Create a Linear issue.

        CLI: ``orca linear create --title <title> [--body <text> | --body-file <path|->] [--team <key|id>] [--project <projectId-or-exact-name>] [--state <stateId|exact-name>] [--assignee me|<userId>] [--priority none|low|medium|high|urgent] [--estimate <number>] [--due-date <yyyy-mm-dd>] [--label <labelId-or-exact-name>]... [--parent <id> | --parent-current] [--write-id <uuid>] [--workspace <id>] [--json]``

        Notes:
            Use --body-file - to read multiline issue bodies from stdin.

        Examples:
            orca linear create --title "Investigate flaky login" --team ENG --project "Launch"
            orca linear create --title "Follow-up bug" --parent-current --body-file - --json
        """
        return self._client._invoke("linear create", [], [("title", title), ("body", body), ("body-file", body_file), ("team", team), ("project", project), ("state", state), ("assignee", assignee), ("priority", priority), ("estimate", estimate), ("due-date", due_date), ("label", label), ("parent", parent), ("parent-current", parent_current), ("write-id", write_id), ("workspace", workspace)], json=True, remote=True, stdin=stdin)

    def issue(
        self,
        id: Scalar | None = None,
        *,
        current: bool = False,
        comments: bool = False,
        children: bool = False,
        depth: int | str | None = None,
        attachments: bool = False,
        relations: bool = False,
        activity: bool = False,
        full: bool = False,
        workspace: Scalar | None = None,
    ) -> Any:
        """Read Linear issue context for agents.

        CLI: ``orca linear issue [<id>] [--current] [--comments] [--children] [--depth <n>] [--attachments] [--relations] [--activity] [--full] [--workspace <id>] [--json]``

        Examples:
            orca linear issue ENG-123
            orca linear issue --current --comments
            orca linear issue https://linear.app/acme/issue/ENG-123 --full --json
        """
        return self._client._invoke("linear issue", [id], [("current", current), ("comments", comments), ("children", children), ("depth", depth), ("attachments", attachments), ("relations", relations), ("activity", activity), ("full", full), ("workspace", workspace)], json=True, remote=True)

    def list(
        self,
        *,
        filter: Scalar | None = None,
        team: Scalar | None = None,
        limit: int | str | None = None,
        workspace: Scalar | None = None,
    ) -> Any:
        """List Linear issues for task triage.

        CLI: ``orca linear list [--filter assigned|created|all|completed|open] [--team <key|id>] [--limit <n>] [--workspace <id>|all] [--json]``

        Examples:
            orca linear list --filter assigned --limit 10 --json
        """
        return self._client._invoke("linear list", [], [("filter", filter), ("team", team), ("limit", limit), ("workspace", workspace)], json=True, remote=True)

    def list_issues(
        self,
        *,
        team: Scalar | None = None,
        cycle: Scalar | None = None,
        label: Scalar | None = None,
        limit: int | str | None = None,
        query: Scalar | None = None,
        state: Scalar | None = None,
        cursor: Scalar | None = None,
        order_by: Scalar | None = None,
        project: Scalar | None = None,
        release: Scalar | None = None,
        assignee: Scalar | None = None,
        delegate: Scalar | None = None,
        parent_id: Scalar | None = None,
        priority: Scalar | None = None,
        created_at: Scalar | None = None,
        updated_at: Scalar | None = None,
        include_archived: bool = False,
        workspace: Scalar | None = None,
    ) -> Any:
        """List Linear issues with MCP-compatible filters.

        CLI: ``orca linear list-issues [--team <team>] [--cycle <cycle>] [--label <label>] [--limit <n>] [--query <text>] [--state <state>] [--cursor <cursor>] [--order-by createdAt|updatedAt] [--project <project>] [--release <release>] [--assignee <user|me|null>] [--delegate <user|me|null>] [--parent-id <issue|null>] [--priority <0-4>] [--created-at <datetime|duration>] [--updated-at <datetime|duration>] [--include-archived] [--workspace <id>|all] [--json]``

        Notes:
            Omitting --limit returns every match (result.meta.limit is null); --limit <n> caps the read.
            JSON sets result.truncated when a cap held results back; text prints truncated: showing N.
            Reuse --cursor from the previous page. Issued cursors bind the workspace; raw Linear cursors still need --workspace.
            --priority is 0=none, 1=urgent, 2=high, 3=medium, 4=low. JSON includes priorityLabel on each issue.

        Examples:
            orca linear list-issues --team ENG --state started --assignee me --json
            orca linear list-issues --query auth --updated-at -P7D --json
            orca linear list-issues --assignee me --priority 1 --limit 100 --json
            orca linear list-issues --cursor <cursor> --json
        """
        return self._client._invoke("linear list-issues", [], [("team", team), ("cycle", cycle), ("label", label), ("limit", limit), ("query", query), ("state", state), ("cursor", cursor), ("order-by", order_by), ("project", project), ("release", release), ("assignee", assignee), ("delegate", delegate), ("parent-id", parent_id), ("priority", priority), ("created-at", created_at), ("updated-at", updated_at), ("include-archived", include_archived), ("workspace", workspace)], json=True, remote=True)

    def save_issue(
        self,
        id: Scalar | None = None,
        *,
        current: bool = False,
        team: Scalar | None = None,
        title: Scalar | None = None,
        description: Scalar | None = None,
        body: Scalar | None = None,
        body_file: Scalar | None = None,
        state: Scalar | None = None,
        assignee: Scalar | None = None,
        priority: Scalar | None = None,
        estimate: Scalar | None = None,
        due_date: Scalar | None = None,
        label: Scalar | None = None,
        project: Scalar | None = None,
        parent_id: Scalar | None = None,
        write_id: Scalar | None = None,
        workspace: Scalar | None = None,
        stdin: str | bytes | None = None,
    ) -> Any:
        """Create or update a Linear issue.

        CLI: ``orca linear save-issue [<id>] [--current] [--team <key|id>] [--title <title>] [--description <text> | --body-file <path|->] [--state <state>] [--assignee me|<user>|null] [--priority none|low|medium|high|urgent] [--estimate <number>|null] [--due-date <yyyy-mm-dd>|null] [--label <label>...] [--project <project>|null] [--parent-id <issue>|null] [--write-id <uuid>] [--workspace <id>] [--json]``

        Notes:
            Without <id> or --current, creates an issue and requires --team and --title.
            Labels replace the complete label set, matching Linear MCP save_issue semantics.
            Use the literal null to clear assignee, estimate, due date, project, or parent.

        Examples:
            orca linear save-issue --team ENG --title "Fix auth" --priority high --json
            orca linear save-issue ENG-123 --title "Fix OAuth callback" --assignee me --json
            orca linear save-issue --current --project null --due-date null --json
        """
        return self._client._invoke("linear save-issue", [id], [("current", current), ("team", team), ("title", title), ("description", description), ("body", body), ("body-file", body_file), ("state", state), ("assignee", assignee), ("priority", priority), ("estimate", estimate), ("due-date", due_date), ("label", label), ("project", project), ("parent-id", parent_id), ("write-id", write_id), ("workspace", workspace)], json=True, remote=True, stdin=stdin)

    def search(
        self,
        query: Scalar,
        *,
        limit: int | str | None = None,
        workspace: Scalar | None = None,
    ) -> Any:
        """Search connected Linear workspaces.

        CLI: ``orca linear search <query> [--limit <n>] [--workspace <id>|all] [--json]``

        Examples:
            orca linear search "auth bug"
            orca linear search ENG --workspace all --json
        """
        return self._client._invoke("linear search", [query], [("limit", limit), ("workspace", workspace)], json=True, remote=True)

class MouseResource(_Resource):
    """Commands under ``orca mouse``."""

    def down(
        self,
        *,
        button: Scalar | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Press mouse button.

        CLI: ``orca mouse down [--button <left|right|middle>] [--worktree <selector>] [--json]``
        """
        return self._client._invoke("mouse down", [], [("button", button), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def move(
        self,
        *,
        x: int | str,
        y: int | str,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Move mouse to x,y coordinates.

        CLI: ``orca mouse move --x <n> --y <n> [--worktree <selector>] [--json]``
        """
        return self._client._invoke("mouse move", [], [("x", x), ("y", y), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def up(
        self,
        *,
        button: Scalar | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Release mouse button.

        CLI: ``orca mouse up [--button <left|right|middle>] [--worktree <selector>] [--json]``
        """
        return self._client._invoke("mouse up", [], [("button", button), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def wheel(
        self,
        *,
        dy: int | str,
        dx: int | str | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Scroll wheel.

        CLI: ``orca mouse wheel --dy <n> [--dx <n>] [--worktree <selector>] [--json]``
        """
        return self._client._invoke("mouse wheel", [], [("dy", dy), ("dx", dx), ("worktree", worktree), ("page", page)], json=True, remote=True)

class OrchestrationResource(_Resource):
    """Commands under ``orca orchestration``."""

    def ask(
        self,
        *,
        to: Scalar | None = None,
        run: Scalar | None = None,
        question: Scalar | None = None,
        resume: Scalar | None = None,
        dispatch_capability: Scalar | None = None,
        options: Scalar | None = None,
        timeout_ms: int | str | None = None,
        from_: Scalar | None = None,
        retry_request: Scalar | None = None,
    ) -> Any:
        """Ask the coordinator a question and block until answered.

        CLI: ``orca orchestration ask (--question <text> | --resume <message_id>) [--to <run:id>] [--run <run_id>] [--options <csv>] [--timeout-ms <n>] [--from <handle>] [--retry-request <id>] [--json]``

        Notes:
            From an active Dispatch, a new question defaults to its owning Run mailbox.
            Timeout leaves the question pending; resume with the original message ID.
        """
        return self._client._invoke("orchestration ask", [], [("to", to), ("run", run), ("question", question), ("resume", resume), ("dispatch-capability", dispatch_capability), ("options", options), ("timeout-ms", timeout_ms), ("from", from_), ("retry-request", retry_request)], json=True, remote=True)

    def check(
        self,
        *,
        terminal: Scalar | None = None,
        run: Scalar | None = None,
        ack: Scalar | None = None,
        unread: bool = False,
        peek: bool = False,
        all: bool = False,
        types: Scalar | None = None,
        format: bool = False,
        wait: bool = False,
        timeout_ms: int | str | None = None,
        retry_request: Scalar | None = None,
    ) -> Any:
        """Check this agent's messages.

        CLI: ``orca orchestration check [--terminal <handle>] [--run <run_id>] [--ack <delivery_id>] [--unread | --peek | --all] [--types <type,...>] [--format] [--wait] [--timeout-ms <n>] [--retry-request <id>] [--json]``

        Notes:
            On Windows PowerShell, quote comma-separated type filters, e.g. --types "worker_done,escalation".
            --types is the wake condition for --wait; a returned Delivery is always the whole FIFO batch, so it is never filtered by type. Without --wait it has no effect on consuming checks. Only --peek and --all filter their rows.
            --format renders the returned rows as local text only; it never writes to another terminal.
            A bound Run replays the same Delivery until --ack or all its messages are marked read, even with --types; process every message before acknowledging.
        """
        return self._client._invoke("orchestration check", [], [("terminal", terminal), ("run", run), ("ack", ack), ("unread", unread), ("peek", peek), ("all", all), ("types", types), ("format", format), ("wait", wait), ("timeout-ms", timeout_ms), ("retry-request", retry_request)], json=True, remote=True)

    def coordinator_start(
        self,
        *,
        spec: Scalar,
        from_: Scalar | None = None,
        poll_interval_ms: int | str | None = None,
        max_concurrent: int | str | None = None,
        worktree: Scalar | None = None,
    ) -> Any:
        """Retired: load the current orchestration skill.

        CLI: ``orca orchestration coordinator-start --spec <text> [--from <handle>] [--poll-interval-ms <n>] [--max-concurrent <n>] [--worktree <selector>] [--json]``

        Notes:
            This command performs no effects and returns the exact `skills get orchestration --full` recovery action.
            Use the lightweight Run, Task, and worker-start primitives described by the current skill.
        """
        return self._client._invoke("orchestration coordinator-start", [], [("spec", spec), ("from", from_), ("poll-interval-ms", poll_interval_ms), ("max-concurrent", max_concurrent), ("worktree", worktree)], json=True, remote=True)

    def coordinator_stop(
        self,
    ) -> Any:
        """Retired: load the current orchestration skill.

        CLI: ``orca orchestration coordinator-stop [--json]``

        Notes:
            This command performs no effects and returns the exact `skills get orchestration --full` recovery action.
        """
        return self._client._invoke("orchestration coordinator-stop", [], [], json=True, remote=True)

    def dispatch(
        self,
        *,
        task: Scalar,
        to: Scalar,
        from_: Scalar | None = None,
        run: Scalar | None = None,
        inject: bool = False,
        dry_run: bool = False,
        return_preamble: bool = False,
        retry_request: Scalar | None = None,
    ) -> Any:
        """Dispatch a task to a terminal.

        CLI: ``orca orchestration dispatch --task <task_id> --to <handle> [--from <handle>] [--run <run_id>] [--inject] [--dry-run] [--return-preamble] [--retry-request <id>] [--json]``
        """
        return self._client._invoke("orchestration dispatch", [], [("task", task), ("to", to), ("from", from_), ("run", run), ("inject", inject), ("dry-run", dry_run), ("return-preamble", return_preamble), ("retry-request", retry_request)], json=True, remote=True)

    def dispatch_show(
        self,
        *,
        task: Scalar,
        preamble: bool = False,
        from_: Scalar | None = None,
    ) -> Any:
        """Show dispatch context for a task.

        CLI: ``orca orchestration dispatch-show --task <task_id> [--preamble] [--from <handle>] [--json]``
        """
        return self._client._invoke("orchestration dispatch-show", [], [("task", task), ("preamble", preamble), ("from", from_)], json=True, remote=True)

    def gate_create(
        self,
        *,
        task: Scalar,
        question: Scalar,
        options: Scalar | None = None,
        from_: Scalar | None = None,
        retry_request: Scalar | None = None,
    ) -> Any:
        """Create a decision gate blocking a task.

        CLI: ``orca orchestration gate-create --task <task_id> --question <text> [--options <json_array>] [--from <handle>] [--retry-request <id>] [--json]``
        """
        return self._client._invoke("orchestration gate-create", [], [("task", task), ("question", question), ("options", options), ("from", from_), ("retry-request", retry_request)], json=True, remote=True)

    def gate_list(
        self,
        *,
        task: Scalar | None = None,
        status: Scalar | None = None,
        run: Scalar | None = None,
        from_: Scalar | None = None,
    ) -> Any:
        """List decision gates.

        CLI: ``orca orchestration gate-list [--task <task_id>] [--status <status>] [--run <run_id>] [--from <handle>] [--json]``

        Notes:
            --run inspects a named Run without binding; otherwise gates are scoped to the caller.
        """
        return self._client._invoke("orchestration gate-list", [], [("task", task), ("status", status), ("run", run), ("from", from_)], json=True, remote=True)

    def gate_resolve(
        self,
        *,
        id: Scalar,
        resolution: Scalar,
        from_: Scalar | None = None,
        retry_request: Scalar | None = None,
    ) -> Any:
        """Resolve a pending decision gate.

        CLI: ``orca orchestration gate-resolve --id <gate_id> --resolution <text> [--from <handle>] [--retry-request <id>] [--json]``
        """
        return self._client._invoke("orchestration gate-resolve", [], [("id", id), ("resolution", resolution), ("from", from_), ("retry-request", retry_request)], json=True, remote=True)

    def inbox(
        self,
        *,
        limit: int | str | None = None,
        terminal: Scalar | None = None,
        full: bool = False,
    ) -> Any:
        """Show messages across (or for) recipients.

        CLI: ``orca orchestration inbox [--limit <n>] [--terminal <handle>] [--full] [--json]``
        """
        return self._client._invoke("orchestration inbox", [], [("limit", limit), ("terminal", terminal), ("full", full)], json=True, remote=True)

    def reply(
        self,
        *,
        id: Scalar,
        body: Scalar,
        run: Scalar | None = None,
        from_: Scalar | None = None,
        retry_request: Scalar | None = None,
    ) -> Any:
        """Reply to a message.

        CLI: ``orca orchestration reply --id <msg_id> --body <text> [--run <run_id>] [--from <handle>] [--retry-request <id>] [--json]``
        """
        return self._client._invoke("orchestration reply", [], [("id", id), ("body", body), ("run", run), ("from", from_), ("retry-request", retry_request)], json=True, remote=True)

    def request_show(
        self,
        *,
        request: Scalar,
    ) -> Any:
        """Ask whether one orchestration mutation request already took effect.

        CLI: ``orca orchestration request-show --request <request_id> [--json]``

        Notes:
            Read-only: it never starts, retries, or settles anything, so it is safe to run after any lost response.
            completed means the mutation landed and --retry-request replays the recorded outcome instead of starting a second one. pending means the original mutation is still running or Orca restarted before recording its outcome; wait for a live original command, otherwise replay with --retry-request.
            absent means this runtime holds no receipt for that request under your caller identity: it never arrived, it failed before recording anything, or the receipt was pruned. Absent is not proof that nothing happened.
        """
        return self._client._invoke("orchestration request-show", [], [("request", request)], json=True, remote=True)

    def reset(
        self,
        *,
        all: bool = False,
        tasks: bool = False,
        messages: bool = False,
        retry_request: Scalar | None = None,
    ) -> Any:
        """Reset one explicit orchestration state scope.

        CLI: ``orca orchestration reset (--all | --tasks | --messages) [--retry-request <id>] [--json]``
        """
        return self._client._invoke("orchestration reset", [], [("all", all), ("tasks", tasks), ("messages", messages), ("retry-request", retry_request)], json=True, remote=True)

    def run_create(
        self,
        *,
        objective: Scalar,
        from_: Scalar | None = None,
        retry_request: Scalar | None = None,
    ) -> Any:
        """Create and bind a lightweight orchestration Run.

        CLI: ``orca orchestration run-create --objective <text> [--from <handle>] [--retry-request <id>] [--json]``

        Notes:
            A Run is a namespace and home inbox. It never schedules or places workers.
            --retry-request is only for exact recovery after an unknown mutation result.
        """
        return self._client._invoke("orchestration run-create", [], [("objective", objective), ("from", from_), ("retry-request", retry_request)], json=True, remote=True)

    def run_current(
        self,
        *,
        from_: Scalar | None = None,
    ) -> Any:
        """Show the Run bound to this coordinator.

        CLI: ``orca orchestration run-current [--from <handle>] [--json]``
        """
        return self._client._invoke("orchestration run-current", [], [("from", from_)], json=True, remote=True)

    def run_list(
        self,
        *,
        limit: int | str | None = None,
        cursor: Scalar | None = None,
    ) -> Any:
        """List lightweight orchestration Runs.

        CLI: ``orca orchestration run-list [--limit <n>] [--cursor <cursor>] [--json]``
        """
        return self._client._invoke("orchestration run-list", [], [("limit", limit), ("cursor", cursor)], json=True, remote=True)

    def run_show(
        self,
        *,
        id: Scalar,
    ) -> Any:
        """Show one lightweight orchestration Run.

        CLI: ``orca orchestration run-show --id <run_id> [--json]``
        """
        return self._client._invoke("orchestration run-show", [], [("id", id)], json=True, remote=True)

    def run_use(
        self,
        *,
        id: Scalar,
        from_: Scalar | None = None,
        takeover_legacy: bool = False,
        retry_request: Scalar | None = None,
    ) -> Any:
        """Bind this coordinator to an existing Run.

        CLI: ``orca orchestration run-use --id <run_id> [--from <handle>] [--takeover-legacy] [--retry-request <id>] [--json]``

        Notes:
            --takeover-legacy must run in the live coordinator agent terminal it binds; it preserves existing worker assignments.
        """
        return self._client._invoke("orchestration run-use", [], [("id", id), ("from", from_), ("takeover-legacy", takeover_legacy), ("retry-request", retry_request)], json=True, remote=True)

    def send(
        self,
        *,
        subject: Scalar,
        to: Scalar | None = None,
        run: Scalar | None = None,
        from_: Scalar | None = None,
        body: Scalar | None = None,
        type: Scalar | None = None,
        priority: Scalar | None = None,
        thread_id: Scalar | None = None,
        payload: Scalar | None = None,
        task_id: Scalar | None = None,
        dispatch_id: Scalar | None = None,
        dispatch_capability: Scalar | None = None,
        retry_request: Scalar | None = None,
        outcome: Scalar | None = None,
        files_modified: Scalar | None = None,
        report_path: Scalar | None = None,
        phase: Scalar | None = None,
    ) -> Any:
        """Send an inter-agent message.

        CLI: ``orca orchestration send --subject <text> [--to <run:id|dispatch:id|legacy_handle>] [--run <run_id>] [--from <handle>] [--body <text>] [--type <type>] [--priority <level>] [--thread-id <id>] [--payload <json>] [--task-id <id>] [--dispatch-id <id>] [--outcome <succeeded|failed>] [--files-modified <csv>] [--report-path <path>] [--phase <text>] [--retry-request <id>] [--json]``

        Notes:
            Valid --type values: status, dispatch, worker_done, merge_ready, escalation, handoff, decision_gate, question, heartbeat.
            To answer a worker question, use orchestration reply --id <msg_id> --body <text> with the same Orca CLI executable.
            Group addresses (@all, @idle, @codex, ...) reach the live Dispatches of your own Run; a sender in no Run must use run:<id> or dispatch:<id>. @worktree:<id> names one workspace.
            Run groups exclude their owning coordinator; send to run:<id> to raise something with yours. Nested coordinators receive group mail in their child Run mailbox; @worktree:<id> includes workspace coordinators.
            On Windows PowerShell, quote group addresses such as --to "@all" or --to "@worktree:<id>".
            worker_done and heartbeat are exact-Dispatch signals and cannot target groups; omit --to to use the Dispatch's Run mailbox.
            worker_done requires --outcome succeeded or --outcome failed.
            From an active Dispatch, an omitted recipient defaults to its owning Run mailbox.
            Use --to dispatch:<id> for attempt-specific coordinator guidance; Orca durably relays it to a connected worker server.
            A worker_done with the active task/dispatch IDs completes that task only from the dispatched pane. When stable pane identity is unavailable, the sender handle must exactly match the dispatch assignee; injected preambles include the correct --from value.
            Prefer --task-id/--dispatch-id/etc. over raw --payload JSON in worker commands; PowerShell strips JSON quotes easily.
        """
        return self._client._invoke("orchestration send", [], [("to", to), ("run", run), ("from", from_), ("subject", subject), ("body", body), ("type", type), ("priority", priority), ("thread-id", thread_id), ("payload", payload), ("task-id", task_id), ("dispatch-id", dispatch_id), ("dispatch-capability", dispatch_capability), ("retry-request", retry_request), ("outcome", outcome), ("files-modified", files_modified), ("report-path", report_path), ("phase", phase)], json=True, remote=True)

    def task_create(
        self,
        *,
        spec: Scalar,
        task_title: Scalar | None = None,
        display_name: Scalar | None = None,
        deps: Scalar | None = None,
        parent: Scalar | None = None,
        run: Scalar | None = None,
        from_: Scalar | None = None,
        retry_request: Scalar | None = None,
    ) -> Any:
        """Create an orchestration task.

        CLI: ``orca orchestration task-create --spec <text> [--task-title <text>] [--display-name <text>] [--deps <json_array>] [--parent <task_id>] [--run <run_id>] [--from <handle>] [--retry-request <id>] [--json]``
        """
        return self._client._invoke("orchestration task-create", [], [("spec", spec), ("task-title", task_title), ("display-name", display_name), ("deps", deps), ("parent", parent), ("run", run), ("from", from_), ("retry-request", retry_request)], json=True, remote=True)

    def task_list(
        self,
        *,
        status: Scalar | None = None,
        ready: bool = False,
        brief: bool = False,
        run: Scalar | None = None,
        from_: Scalar | None = None,
    ) -> Any:
        """List orchestration tasks.

        CLI: ``orca orchestration task-list [--status <status>] [--ready] [--brief] [--run <run_id>] [--from <handle>] [--json]``

        Notes:
            --brief collapses whitespace and caps each spec at 160 characters.
        """
        return self._client._invoke("orchestration task-list", [], [("status", status), ("ready", ready), ("brief", brief), ("run", run), ("from", from_)], json=True, remote=True)

    def task_update(
        self,
        *,
        id: Scalar,
        status: Scalar,
        result: Scalar | None = None,
        run: Scalar | None = None,
        from_: Scalar | None = None,
        retry_request: Scalar | None = None,
    ) -> Any:
        """Update a task status.

        CLI: ``orca orchestration task-update --id <task_id> --status <status> [--result <text>] [--run <run_id>] [--from <handle>] [--retry-request <id>] [--json]``

        Notes:
            Valid --status values: pending, ready, dispatched, completed, failed, blocked.
            To cancel a Task, stop or abandon its worker, then set --status failed --result cancelled; a later worker-start --retry-of reopens it.
        """
        return self._client._invoke("orchestration task-update", [], [("id", id), ("status", status), ("result", result), ("run", run), ("from", from_), ("retry-request", retry_request)], json=True, remote=True)

    def worker_abandon(
        self,
        *,
        dispatch: Scalar,
        retry_request: Scalar | None = None,
    ) -> Any:
        """Fence a worker without claiming its process stopped.

        CLI: ``orca orchestration worker-abandon --dispatch <dispatch_id> [--retry-request <id>] [--json]``

        Notes:
            Retains all possibly-live resources and performs no process or filesystem action.
        """
        return self._client._invoke("orchestration worker-abandon", [], [("dispatch", dispatch), ("retry-request", retry_request)], json=True, remote=True)

    def worker_list(
        self,
        *,
        run: Scalar | None = None,
        terminal_state: Scalar | None = None,
        include_remote: bool = False,
        cursor: Scalar | None = None,
        limit: Scalar | None = None,
    ) -> Any:
        """List supervised worker terminal resource accounting.

        CLI: ``orca orchestration worker-list [--run <run_id>] [--terminal-state <active|reclaimable|retained|release_pending|release_unknown|released>] [--include-remote] [--cursor <cursor>] [--limit <1-100>] [--json]``

        Notes:
            Terminal state is process accounting and is reported separately from Task status; a completed Task can still own a live terminal.
            Context-only Dispatches created by orchestration dispatch are included as unsupervised with terminal state retained.
            Returns at most 100 local rows, newest first, by default; --include-remote adds connected-server observations when the host supports fleet listing. Continue with the opaque page.nextCursor value unchanged.
            Without --run the list is scoped to the Run bound to the calling terminal, and to every Run when there is no binding; the receipt reports which in scope.source (flag, bound, or all).
        """
        return self._client._invoke("orchestration worker-list", [], [("run", run), ("terminal-state", terminal_state), ("include-remote", include_remote), ("cursor", cursor), ("limit", limit)], json=True, remote=True)

    def worker_read(
        self,
        *,
        dispatch: Scalar,
        source: Scalar | None = None,
        cursor: Scalar | None = None,
        limit: int | str | None = None,
    ) -> Any:
        """Read bounded output from one supervised worker.

        CLI: ``orca orchestration worker-read --dispatch <dispatch_id> [--source <auto|transcript|terminal>] [--cursor <cursor>] [--limit <n>] [--json]``

        Notes:
            The default auto source uses an exact hook-reported transcript when available and otherwise returns labeled terminal output.
            A Dispatch created by orchestration dispatch reads from its adopted terminal with worker status unsupervised.
            A returned cursor is pinned to the exact source; start a fresh read if Orca reports source_changed.
        """
        return self._client._invoke("orchestration worker-read", [], [("dispatch", dispatch), ("source", source), ("cursor", cursor), ("limit", limit)], json=True, remote=True)

    def worker_release(
        self,
        *,
        dispatch: Scalar,
        retry_request: Scalar | None = None,
    ) -> Any:
        """Release the terminal of one settled supervised worker.

        CLI: ``orca orchestration worker-release --dispatch <dispatch_id> [--retry-request <id>] [--json]``

        Notes:
            Post-completion cleanup for a settled (succeeded or failed) worker; closes only the exact coordinator-owned agent terminal of that worker.
            A settled Dispatch created by orchestration dispatch has no owned terminal resource and is reported retained without process action.
            An inspectable output archive is preserved before the terminal closes, so worker-read still returns output afterwards.
            Never closes setup terminals, configured tabs, reused or pre-existing terminals, user-taken-over terminals, or unproven identities.
            Idempotent: repeating the call reports already_released. Only release_unknown exits 1; retained, release_pending, and already_released exit 0.
        """
        return self._client._invoke("orchestration worker-release", [], [("dispatch", dispatch), ("retry-request", retry_request)], json=True, remote=True)

    def worker_retain(
        self,
        *,
        dispatch: Scalar,
        retry_request: Scalar | None = None,
    ) -> Any:
        """Keep one supervised worker terminal live for debugging.

        CLI: ``orca orchestration worker-retain --dispatch <dispatch_id> [--retry-request <id>] [--json]``

        Notes:
            Records a durable user-requested exception; a later explicit worker-release clears it and releases the terminal.
            A settled Dispatch created by orchestration dispatch has no owned terminal resource and is reported retained without process action.
            Performs no process or filesystem action.
        """
        return self._client._invoke("orchestration worker-retain", [], [("dispatch", dispatch), ("retry-request", retry_request)], json=True, remote=True)

    def worker_show(
        self,
        *,
        dispatch: Scalar,
    ) -> Any:
        """Inspect one supervised worker Dispatch.

        CLI: ``orca orchestration worker-show --dispatch <dispatch_id> [--json]``

        Notes:
            A Dispatch created by orchestration dispatch is shown as unsupervised and reports the exact adopted terminal when its identity is still provable.
            observation.agentWait names a worker parked on a prompt only a human can answer, with the evidence that proved it (hook, prompt-text, or title). Null means Orca looked and found no wait. An absent field means it never looked — an older host, an unverifiable worker identity, an unreadable pane, or an agent probe that did not answer in time — and never means the worker is not waiting. A waiting worker is healthy, not failed.
        """
        return self._client._invoke("orchestration worker-show", [], [("dispatch", dispatch)], json=True, remote=True)

    def worker_start(
        self,
        *,
        task: Scalar | None = None,
        spec: Scalar | None = None,
        task_title: Scalar | None = None,
        deps: Scalar | None = None,
        parent: Scalar | None = None,
        on: Scalar | None = None,
        worktree: Scalar | None = None,
        name: Scalar | None = None,
        repo: Scalar | None = None,
        base_branch: Scalar | None = None,
        display_name: Scalar | None = None,
        comment: Scalar | None = None,
        setup: Scalar | None = None,
        agent: Scalar | None = None,
        model: Scalar | None = None,
        effort: Scalar | None = None,
        terminal: Scalar | None = None,
        retry_of: Scalar | None = None,
        timeout_ms: int | str | None = None,
        run: Scalar | None = None,
        from_: Scalar | None = None,
        retry_request: Scalar | None = None,
    ) -> Any:
        """Start one supervised worker on the Run home or a connected Orca server.

        CLI: ``orca orchestration worker-start (--task <task_id> | --spec <text>) [--on <saved-environment>] [--worktree <current|selector|new-child|new-top-level>] (--agent <agent> | --terminal <handle>) [--task-title <text>] [--deps <json_array>] [--parent <task_id>] [--model <id>] [--effort <level>] [--name <name>] [--repo <selector>] [--base-branch <ref>] [--display-name <text>] [--comment <text>] [--setup <run|skip|inherit>] [--retry-of <dispatch_id>] [--timeout-ms <n>] [--run <run_id>] [--from <handle>] [--retry-request <id>] [--json]``

        Notes:
            Current and existing worktrees never rerun setup; a fresh agent terminal is created unless --terminal is explicit.
            When reusing --terminal, pass --worktree for that terminal; current means the coordinator worktree.
            --agent takes an Orca agent id enabled on the worker server, such as claude, codex, cursor, antigravity, muse, zcode, opencode, or opencode2.
            --model supports Claude, Codex, Cursor, Antigravity, and Muse opaque provider model ids; --effort requires --model. OMP accepts --model only; --effort is unsupported. Neither can combine with --terminal. OpenCode model selection requires an existing worktree, a verified execution-host CLI, and an available model; effort is unsupported. Other agents, including zcode, launch with the model from their own config.
            New worktrees use agent-first creation and default --setup to run. Repository start-immediately runs setup beside the agent; wait-for-setup gates agent readiness and task input.
            Creation flags (--name, --repo, --base-branch, --display-name, --comment, --setup) are rejected for current/existing worktrees. Use exact --repo on the selected server; project/host convenience routing remains on worktree create.
            How the worker runs follows the user's own setting for new agent tabs; there is no flag for it and no caller needs to ask. A dispatch the setting cannot apply to still starts, so the placement, agent, and launch options passed here are always the ones honoured.
            Drive every worker the same way whichever way it was started: the same orchestration verbs, the same handle. Mail, dispatch, worker-show, worker-read and the whole lifecycle behave identically. The start receipt records which one ran, for operators and telemetry.
            Not every worker has a terminal. Read output with worker-read --source auto or --source transcript, which always work; --source terminal is refused when there is none, and orca terminal verbs do not accept every worker handle. Nothing above needs you to know which kind you have — the orchestration verbs cover all of them.
            --on selects only the worker server; the Run and this command remain on the current Orca server.
            Remote current and new-child are invalid; discover an exact remote selector or use new-top-level.
            --retry-of needs --task naming the failed Task (--spec creates a new one) and does not inherit placement; repeat the intended --on/worktree and --agent/terminal choices.
            The call exits 0 only for ready. Failed or outcome_unknown exits 1 and JSON includes stage/failedStage, setup, effects, residualResources, and recovery commands when needed.
        """
        return self._client._invoke("orchestration worker-start", [], [("task", task), ("spec", spec), ("task-title", task_title), ("deps", deps), ("parent", parent), ("on", on), ("worktree", worktree), ("name", name), ("repo", repo), ("base-branch", base_branch), ("display-name", display_name), ("comment", comment), ("setup", setup), ("agent", agent), ("model", model), ("effort", effort), ("terminal", terminal), ("retry-of", retry_of), ("timeout-ms", timeout_ms), ("run", run), ("from", from_), ("retry-request", retry_request)], json=True, remote=True)

    def worker_stop(
        self,
        *,
        dispatch: Scalar,
        retry_request: Scalar | None = None,
    ) -> Any:
        """Fence one Dispatch and stop its supervised agent terminal.

        CLI: ``orca orchestration worker-stop --dispatch <dispatch_id> [--retry-request <id>] [--json]``

        Notes:
            A Dispatch created by orchestration dispatch is fenced without closing its unsupervised terminal process.
            Never deletes the worktree, setup terminal, configured tabs, or unrelated processes.
        """
        return self._client._invoke("orchestration worker-stop", [], [("dispatch", dispatch), ("retry-request", retry_request)], json=True, remote=True)

class ProfileStateResource(_Resource):
    """Commands under ``orca profile state``."""

    def exports(
        self,
        *,
        profile_id: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """List retained SQLite backups and JSON exports for profile-state recovery.

        CLI: ``orca profile state exports [--profile-id <id>] [--json]``
        """
        return self._client._invoke("profile state exports", [], [("profile-id", profile_id), ("page", page)], json=True, remote=True)

    def rollback(
        self,
        *,
        revision: Scalar | None = None,
        backup: Scalar | None = None,
        current_json: bool = False,
        current_sqlite: bool = False,
        latest_json: bool = False,
        profile_id: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Restore a SQLite backup or retained JSON export, or keep the current JSON or SQLite profile.

        CLI: ``orca profile state rollback (--backup <id> | --revision <revision> | --current-json | --current-sqlite | --latest-json) [--profile-id <id>] [--json]``

        Notes:
            --profile-id selects another profile without changing the active profile. Prepare each profile before installing a JSON-only build.
            Orca must be stopped. Recovery validates the selected artifact and archives the current database family, JSON, and retained recovery artifacts before replacing state.
            --backup restores SQLite authority; --revision restores a JSON export for an older compatible runtime.
            --latest-json exports the latest SQLite state and restores it as JSON before launching an older JSON-only build. The current database and recovery artifacts are archived.
            --current-json keeps the current orca-data.json, including edits from an older build. It replaces SQLite state without merging; both copies are archived. The next SQLite-capable start imports the selected JSON.
            --current-sqlite keeps the current SQLite state and discards JSON edits from an older build. The JSON is archived, then rewritten from SQLite.

        Examples:
            orca profile state exports
            orca profile state rollback --backup <id>
            orca profile state rollback --revision 1
            orca profile state rollback --latest-json
            orca profile state rollback --current-json
            orca profile state rollback --current-sqlite
        """
        return self._client._invoke("profile state rollback", [], [("revision", revision), ("backup", backup), ("current-json", current_json), ("current-sqlite", current_sqlite), ("latest-json", latest_json), ("profile-id", profile_id), ("page", page)], json=True, remote=True)

class ProfileResource(_Resource):
    """Commands under ``orca profile``."""

    @cached_property
    def state(self) -> ProfileStateResource:
        """``orca profile state`` commands."""
        return ProfileStateResource(self._client)

class ProjectResource(_Resource):
    """Commands under ``orca project``."""

    def list(
        self,
    ) -> Any:
        """List durable projects known to Orca.

        CLI: ``orca project list [--json]``

        Examples:
            orca project list
            orca project list --json
        """
        return self._client._invoke("project list", [], [], json=True, remote=True)

    def setup_clone(
        self,
        *,
        project: Scalar,
        host: Scalar,
        url: Scalar,
        destination: Scalar,
        display_name: Scalar | None = None,
    ) -> Any:
        """Make a project available on a host by cloning a repository.

        CLI: ``orca project setup-clone --project <id> --host <host> --url <clone-url> --destination <path> [--display-name <name>] [--json]``

        Notes:
            For remote runtimes, --destination must be an absolute parent directory on the remote server.
            --host takes local, ssh:<target-id>, runtime:<environment-id>, or the bare host name `orca host list` prints for any of them.
            SSH targets are cloned through the desktop UI because the desktop client owns SSH connections.

        Examples:
            orca project setup-clone --project github:stablyai/orca --host local --url https://github.com/stablyai/orca.git --destination ~/src
            orca project setup-clone --project github:stablyai/orca --host runtime:03ef704c-b180-4b10-998d-e28fbd5de9a3 --url https://github.com/stablyai/orca.git --destination /srv --json
        """
        return self._client._invoke("project setup-clone", [], [("project", project), ("host", host), ("url", url), ("destination", destination), ("display-name", display_name)], json=True, remote=True)

    def setup_create(
        self,
        *,
        project: Scalar,
        host: Scalar,
        setup_id: Scalar | None = None,
        path: Scalar | None = None,
        kind: Scalar | None = None,
        display_name: Scalar | None = None,
        worktree_base_path: Scalar | None = None,
        git_username: Scalar | None = None,
        state: Scalar | None = None,
        method: Scalar | None = None,
    ) -> Any:
        """Create independent project host setup metadata.

        CLI: ``orca project setup-create --project <id> --host <host> [--setup-id <id>] [--path <path>] [--kind git|folder] [--display-name <name>] [--worktree-base-path <path>] [--git-username <name>] [--state ready|not-set-up|setting-up|error|unsupported] [--method imported-existing-folder|cloned|provisioned] [--json]``

        Notes:
            Creates setup metadata without registering a repo compatibility record.
            --host takes local, ssh:<target-id>, runtime:<environment-id>, or the bare host name `orca host list` prints for any of them.
            Use setup-existing-folder when Orca should import and manage an actual checkout path now.

        Examples:
            orca project setup-create --project github:stablyai/orca --host runtime:03ef704c-b180-4b10-998d-e28fbd5de9a3 --state setting-up --method provisioned --json
        """
        return self._client._invoke("project setup-create", [], [("project", project), ("host", host), ("setup-id", setup_id), ("path", path), ("kind", kind), ("display-name", display_name), ("worktree-base-path", worktree_base_path), ("git-username", git_username), ("state", state), ("method", method)], json=True, remote=True)

    def setup_delete(
        self,
        *,
        setup: Scalar,
        host: Scalar | None = None,
        force: bool = False,
    ) -> Any:
        """Remove a project host setup.

        CLI: ``orca project setup-delete --setup <setup-id> [--host <host>] [--force] [--json]``

        Notes:
            Independent setups are removed directly.
            Repo-backed setups remove the registered repo compatibility record.
            Refuses while the project has open terminals or saved workspace details; --force removes it anyway.

        Examples:
            orca project setup-delete --setup github:stablyai/orca::gpu --json
        """
        return self._client._invoke("project setup-delete", [], [("setup", setup), ("host", host), ("force", force)], json=True, remote=True)

    def setup_existing_folder(
        self,
        *,
        project: Scalar,
        host: Scalar,
        path: Scalar,
        kind: Scalar | None = None,
        display_name: Scalar | None = None,
    ) -> Any:
        """Make a project available on a host by importing an existing folder.

        CLI: ``orca project setup-existing-folder --project <id> --host <host> --path <path> [--kind git|folder] [--display-name <name>] [--json]``

        Notes:
            For remote runtimes, --path must be an absolute path on the remote server.
            --host takes local, ssh:<target-id>, runtime:<environment-id>, or the bare host name `orca host list` prints for any of them.
            SSH targets are set up through the desktop UI because the desktop client owns SSH connections.

        Examples:
            orca project setup-existing-folder --project github:stablyai/orca --host local --path ~/orca
            orca project setup-existing-folder --project github:stablyai/orca --host runtime:03ef704c-b180-4b10-998d-e28fbd5de9a3 --path /home/me/orca --kind git --json
        """
        return self._client._invoke("project setup-existing-folder", [], [("project", project), ("host", host), ("path", path), ("kind", kind), ("display-name", display_name)], json=True, remote=True)

    def setup_update(
        self,
        *,
        setup: Scalar,
        host: Scalar | None = None,
        display_name: Scalar | None = None,
        path: Scalar | None = None,
        worktree_base_path: Scalar | None = None,
        git_username: Scalar | None = None,
        kind: Scalar | None = None,
        state: Scalar | None = None,
        method: Scalar | None = None,
    ) -> Any:
        """Update project host setup metadata.

        CLI: ``orca project setup-update --setup <setup-id> [--host <host>] [--display-name <name>] [--path <path>] [--worktree-base-path <path>] [--git-username <name>] [--kind git|folder] [--state ready|not-set-up|setting-up|error|unsupported] [--method legacy-repo|imported-existing-folder|cloned|provisioned] [--json]``

        Notes:
            Repo-backed setups mirror safe fields onto the repo record.
            --host picks the setup when the project is set up on more than one host under the same setup id.
            Path and availability state changes are only supported for independent setup records.

        Examples:
            orca project setup-update --setup github:stablyai/orca::gpu --display-name "GPU VM"
            orca project setup-update --setup github:stablyai/orca::gpu --path /srv/orca --state ready --json
        """
        return self._client._invoke("project setup-update", [], [("setup", setup), ("host", host), ("display-name", display_name), ("path", path), ("worktree-base-path", worktree_base_path), ("git-username", git_username), ("kind", kind), ("state", state), ("method", method)], json=True, remote=True)

    def setups(
        self,
        *,
        project: Scalar | None = None,
        host: Scalar | None = None,
    ) -> Any:
        """List project host setups.

        CLI: ``orca project setups [--project <id>] [--host <host>] [--json]``

        Notes:
            A setup means a project is available on a host at a concrete filesystem path.
            --host runtime:<environment-id> runs the command on that paired Orca server instead of filtering this runtime; unknown environment ids are rejected rather than answered with an empty list.
            Run `orca environment list` to see the environment ids that runtime:<environment-id> accepts. It matches ids only, never environment names.
            A routed --host runtime:<id> also lists that server's own local-stamped setups, because both spellings name the machine the command reached.

        Examples:
            orca project setups
            orca project setups --project github:stablyai/orca
            orca project setups --host local
            orca project setups --host runtime:03ef704c-b180-4b10-998d-e28fbd5de9a3
        """
        return self._client._invoke("project setups", [], [("project", project), ("host", host)], json=True, remote=True)

class ReferenceResource(_Resource):
    """Commands under ``orca reference``."""

    def add(
        self,
        url: str | Sequence[str],
        *,
        worktree: Scalar,
        reference_site: Scalar | None = None,
    ) -> Any:
        """Attach reviews or issues to a workspace.

        CLI: ``orca reference add <url-or-jira-key>... --worktree <selector> [--reference-site <id>] [--json]``

        Notes:
            Bare keys resolve Jira issues on the selected execution-host Jira site; use --reference-site to choose one explicitly. Other providers require full URLs.
            Existing links are unchanged; all inputs are validated and Jira keys resolved before writing. Full URLs do not require Jira lookup.

        Examples:
            orca reference add https://github.com/acme/api/pull/5123 https://linear.app/acme/issue/STA-1234 --worktree name:api
            orca reference add ENG-123 --reference-site <id> --worktree name:api
        """
        return self._client._invoke("reference add", [url], [("worktree", worktree), ("reference-site", reference_site)], json=True, remote=True)

    def find(
        self,
        query: Scalar,
        *,
        worktree: Scalar | None = None,
        repo: Scalar | None = None,
        include_archived: bool = False,
        limit: int | str | None = None,
    ) -> Any:
        """Find workspaces and agents associated with a review or issue.

        CLI: ``orca reference find <url-or-issue-key> [--worktree <selector>|--repo <selector>] [--include-archived] [--limit <n>] [--json]``

        Notes:
            Reads stored references only. Use orca search to search agent conversations.
            Issue keys search every matching source. Bare numbers and custom shorthand are unsupported.
            Returns up to 50 workspaces by default; truncated is true when more match.
            linked means recorded evidence associates that agent with the reference; workspace membership alone does not establish ownership.

        Examples:
            orca reference find STA-1234 --json
        """
        return self._client._invoke("reference find", [query], [("worktree", worktree), ("repo", repo), ("include-archived", include_archived), ("limit", limit)], json=True, remote=True)

    def list(
        self,
        *,
        worktree: Scalar,
    ) -> Any:
        """List the reviews and issues attached to a workspace.

        CLI: ``orca reference list --worktree <selector> [--json]``
        """
        return self._client._invoke("reference list", [], [("worktree", worktree)], json=True, remote=True)

    def remove(
        self,
        url: str | Sequence[str] | None = None,
        *,
        worktree: Scalar,
        key: Scalar | Sequence[Scalar] | None = None,
    ) -> Any:
        """Detach reviews or issues from a workspace.

        CLI: ``orca reference remove [<url>...] [--key <key>...] --worktree <selector> [--json]``

        Notes:
            Use full URLs, or opaque --key values from reference list for older links without URLs.
            Removing an absent link succeeds without changing the workspace.
        """
        return self._client._invoke("reference remove", [url], [("worktree", worktree), ("key", key)], json=True, remote=True)

class RepoResource(_Resource):
    """Commands under ``orca repo``."""

    def add(
        self,
        *,
        path: Scalar,
    ) -> Any:
        """Add a project to Orca by filesystem path.

        CLI: ``orca repo add --path <path> [--json]``
        """
        return self._client._invoke("repo add", [], [("path", path)], json=True, remote=True)

    def list(
        self,
    ) -> Any:
        """List repos registered in Orca.

        CLI: ``orca repo list [--json]``
        """
        return self._client._invoke("repo list", [], [], json=True, remote=True)

    def search_refs(
        self,
        *,
        repo: Scalar,
        query: Scalar,
        limit: int | str | None = None,
    ) -> Any:
        """Search branch/tag refs within a repo.

        CLI: ``orca repo search-refs --repo <selector> --query <text> [--limit <n>] [--json]``
        """
        return self._client._invoke("repo search-refs", [], [("repo", repo), ("query", query), ("limit", limit)], json=True, remote=True)

    def set(
        self,
        *,
        repo: Scalar,
        external_worktree_visibility: Scalar,
    ) -> Any:
        """Set whether non-Orca worktrees are shown for a repo.

        CLI: ``orca repo set --repo <selector> --external-worktree-visibility show|hide|inherit [--json]``

        Notes:
            show and hide override the global non-Orca worktree visibility default for this repo; inherit clears the override.
            Per-worktree visibility rules still apply.

        Examples:
            orca repo set --repo path:/path/to/repo --external-worktree-visibility show --json
        """
        return self._client._invoke("repo set", [], [("repo", repo), ("external-worktree-visibility", external_worktree_visibility)], json=True, remote=True)

    def set_base_ref(
        self,
        *,
        repo: Scalar,
        ref: Scalar,
    ) -> Any:
        """Set the repo's default base ref for future worktrees.

        CLI: ``orca repo set-base-ref --repo <selector> --ref <ref> [--json]``
        """
        return self._client._invoke("repo set-base-ref", [], [("repo", repo), ("ref", ref)], json=True, remote=True)

    def show(
        self,
        *,
        repo: Scalar,
    ) -> Any:
        """Show one registered repo.

        CLI: ``orca repo show --repo <selector> [--json]``
        """
        return self._client._invoke("repo show", [], [("repo", repo)], json=True, remote=True)

class ServeRestoreResource(_Resource):
    """Commands under ``orca serve restore``."""

    def resume(
        self,
        *,
        page: Scalar | None = None,
    ) -> Any:
        """Resume automatic terminal restores that this host paused.

        CLI: ``orca serve restore resume [--json]``

        Notes:
            After its terminal host stops unexpectedly, or while it is overloaded, Orca keeps restored agent sessions asleep instead of starting them all at once. Each one resumes when you open it.
            This clears that pause so automatic restores start again, within the normal limits. It talks to the Orca running on this machine and never starts a server.
            It also lists restores from an older Orca client that this host refused, with the command that resumes each one.

        Examples:
            orca serve restore resume
            orca serve restore resume --json
        """
        return self._client._invoke("serve restore resume", [], [("page", page)], json=True, remote=True)

class ServeServiceResource(_Resource):
    """Commands under ``orca serve service``."""

    def install(
        self,
        *,
        port: int | str | None = None,
        pairing_address: Scalar | None = None,
        command: Scalar | None = None,
        dry_run: bool = False,
        page: Scalar | None = None,
    ) -> Any:
        """Run orca serve as a per-user background service that restarts itself.

        CLI: ``orca serve service install [--port <port>] [--pairing-address <host>] [--command <path>] [--dry-run] [--json]``

        Notes:
            macOS writes a LaunchAgent; Linux writes a systemd user unit. Both run `orca serve --supervise --no-pairing` for this profile, so the server restarts with growing delays and gives up after repeated failures instead of looping.
            The service never prints a pairing link to its log. Pair clients from the desktop app, or with `orca serve` in a terminal while the service is stopped.
            On Linux the service stops at logout unless lingering is on (`loginctl enable-linger`); install reports it.
            Reinstalling replaces the unit and clears a previous give-up. --command defaults to the installed Orca app's `orca` command on PATH (`orca-ide` on Linux) and must not be a launcher tied to one Orca version. --dry-run prints the unit without installing it.
            Needs the Orca app installed on this machine. The `orca` command in an Orca terminal on an SSH host belongs to that connection's server and cannot install a service.
            Not available on Windows yet.

        Examples:
            orca serve service install
            orca serve service install --port 6768 --dry-run
        """
        return self._client._invoke("serve service install", [], [("port", port), ("pairing-address", pairing_address), ("command", command), ("dry-run", dry_run), ("page", page)], json=True, remote=True)

    def status(
        self,
        *,
        page: Scalar | None = None,
    ) -> Any:
        """Show whether this profile's orca serve service is running.

        CLI: ``orca serve service status [--json]``

        Notes:
            Reports live, exited, or unverifiable (when the service manager cannot be asked), plus why the supervisor gave up if it did.

        Examples:
            orca serve service status
            orca serve service status --json
        """
        return self._client._invoke("serve service status", [], [("page", page)], json=True, remote=True)

    def uninstall(
        self,
        *,
        page: Scalar | None = None,
    ) -> Any:
        """Stop and remove this profile's orca serve service.

        CLI: ``orca serve service uninstall [--json]``

        Notes:
            Stops the service and removes its unit file. The terminal daemon and its sessions keep running.

        Examples:
            orca serve service uninstall
        """
        return self._client._invoke("serve service uninstall", [], [("page", page)], json=True, remote=True)

class ServeResource(_Resource):
    """Commands under ``orca serve``."""

    @cached_property
    def restore(self) -> ServeRestoreResource:
        """``orca serve restore`` commands."""
        return ServeRestoreResource(self._client)

    @cached_property
    def service(self) -> ServeServiceResource:
        """``orca serve service`` commands."""
        return ServeServiceResource(self._client)

    def __call__(
        self,
        *,
        port: int | str | None = None,
        pairing_address: Scalar | None = None,
        mobile_pairing: bool = False,
        no_pairing: bool = False,
        grant_desktop_control: bool = False,
        project_root: Scalar | None = None,
        recipe_json: bool = False,
        supervise: bool = False,
        force: bool = False,
        page: Scalar | None = None,
    ) -> Any:
        """Start an Orca runtime server without opening a desktop window.

        CLI: ``orca serve [--port <port>] [--pairing-address <host>] [--mobile-pairing] [--no-pairing] [--grant-desktop-control] [--project-root <path>] [--recipe-json] [--supervise] [--force] [--json]``

        Notes:
            Runs in the foreground and prints the bound endpoint, advertised endpoint, and pairing status. Stop it with Ctrl+C.
            With --port, serve exits with an error when that port is already in use. Without it, serve uses 6768 and moves to another port when 6768 is taken.
            --pairing-address changes only the client-advertised address; use a reachable LAN, Tailscale, SSH-forward, or reverse-proxy endpoint.
            Use --recipe-json with --project-root from VM recipes to print the recipe result JSON and leave the server running.
            Use --mobile-pairing to print a mobile-scoped pairing QR/link instead of the default runtime-environment pairing link.
            A paired client cannot drive this machine's desktop (orca computer) unless the offer was created with --grant-desktop-control.
            When the web client bundle is available, the server also prints a browser URL with the pairing data embedded.
            Exits with code 3, without starting anything, when another Orca already serves this profile or cannot be shown to have stopped.
            On macOS, after Orca serve aborts at startup (it could not register with Launch Services), later runs from the same environment refuse for 30 minutes with exit code 78. Use --force to try anyway.
            --supervise is for service managers (launchd, systemd). Orca serve then restarts the server itself with growing delays instead of exiting when it stops, waits while an update replaces the app, and waits while another Orca serves this profile. After 6 failures in 15 minutes it gives up and exits with code 0 so the manager stops too, and later supervised runs refuse until a new build is installed or --force is passed. Not available on Windows yet.
            Experimental and off by default: set ORCA_TERMINAL_PROCESS_CEILING=<n> (64 or more) before the terminal host starts to have the OS cap how many processes each terminal may run (Linux, through a systemd user scope per terminal, which needs a user manager that outlives logout; Windows, through a job per terminal). `orca serve` reports the ceiling as on or off, with the reason.
            Off by default: set ORCA_TERMINAL_MEMORY_MAX=<size> (256M or more) and ORCA_TERMINAL_MEMORY_SWAP_MAX=<size> (0 for no swap) before the terminal host starts to cap the memory and swap of each terminal on Linux, through the same per-terminal systemd user scope. A terminal over its limit has its largest process OOM-killed; the host and other terminals keep running. Sizes take K, M, G or T. A limit the host cannot enforce is skipped and logged in the terminal host log. No effect on macOS or Windows.

        Examples:
            orca serve
            orca serve --json
            orca serve --project-root /workspace/repo --pairing-address wss://sandbox.example.com --recipe-json
            orca serve --port 6768 --pairing-address 100.64.1.20
            orca serve --pairing-address 100.64.1.20 --mobile-pairing
        """
        return self._client._invoke("serve", [], [("port", port), ("pairing-address", pairing_address), ("mobile-pairing", mobile_pairing), ("no-pairing", no_pairing), ("grant-desktop-control", grant_desktop_control), ("project-root", project_root), ("recipe-json", recipe_json), ("supervise", supervise), ("force", force), ("page", page)], json=True, remote=True)

class SetResource(_Resource):
    """Commands under ``orca set``."""

    def credentials(
        self,
        *,
        user: Scalar,
        pass_: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Set HTTP auth credentials.

        CLI: ``orca set credentials --user <user> --pass <pass> [--worktree <selector>] [--json]``
        """
        return self._client._invoke("set credentials", [], [("user", user), ("pass", pass_), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def device(
        self,
        *,
        name: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Emulate a device.

        CLI: ``orca set device --name <device> [--worktree <selector>] [--json]``
        """
        return self._client._invoke("set device", [], [("name", name), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def headers(
        self,
        *,
        headers: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Set extra HTTP headers.

        CLI: ``orca set headers --headers <json> [--worktree <selector>] [--json]``
        """
        return self._client._invoke("set headers", [], [("headers", headers), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def media(
        self,
        *,
        color_scheme: Scalar | None = None,
        reduced_motion: Scalar | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Set color scheme and reduced motion preferences.

        CLI: ``orca set media [--color-scheme <dark|light>] [--reduced-motion <reduce|no-preference>] [--worktree <selector>] [--json]``
        """
        return self._client._invoke("set media", [], [("color-scheme", color_scheme), ("reduced-motion", reduced_motion), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def offline(
        self,
        *,
        state: Scalar | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Toggle offline mode.

        CLI: ``orca set offline [--state <on|off>] [--worktree <selector>] [--json]``
        """
        return self._client._invoke("set offline", [], [("state", state), ("worktree", worktree), ("page", page)], json=True, remote=True)

class SkillsResource(_Resource):
    """Commands under ``orca skills``."""

    def get(
        self,
        topic: Scalar,
        *,
        full: bool = False,
        reference: Scalar | None = None,
        references: bool = False,
    ) -> Any:
        """Print a version-matched skill guide as Markdown.

        CLI: ``orca skills get <topic> [--full | --reference <name>] [--json]``

        Notes:
            Reads bundled guide content locally without contacting the Orca runtime.
            Prints the compact guide by default. Use --full to print the full guide with bundled references when provided.
            Use --reference <name> to print one bundled reference alone, which is what an action gate in the compact guide needs; --references lists the available names.
            A reference name may be given bare (recovery-and-cleanup) or as the guide spells it (references/recovery-and-cleanup.md).
            Use --json for a deterministic object containing canonical topic metadata and content.

        Examples:
            orca skills get orca-cli
            orca skills get orchestration --full
            orca skills get orchestration --references
            orca skills get orchestration --reference recovery-and-cleanup
        """
        return self._client._invoke("skills get", [topic], [("full", full), ("reference", reference), ("references", references)], json=True, remote=True)

    def install(
        self,
        *,
        skill: Scalar | None = None,
        all: bool = False,
        agent: Scalar | None = None,
        local: bool = False,
        dry_run: bool = False,
    ) -> Any:
        """Install bundled Orca skills via the community skills CLI.

        CLI: ``orca skills install [--skill <name>]... [--all] [--agent <name>[,<name>]] [--local] [--dry-run] [--json]``

        Notes:
            Reads the bundled skill registry locally without contacting the Orca runtime.
            Resolves to the same `npx skills@<pinned> add <repo>/tree/<commit> --skill <name> ...` command used by Orca Settings, pinned to the commit this Orca build was made from, plus the non-interactive flags an unattended host needs (`npx --yes` and `-y`), then runs it and forwards its output and exit code.
            Installs globally (all projects, adds --global) by default. Use --local to install into the current project instead.
            Targets the coding agents Orca detects on this host, plus the shared .agents/skills directory. Without an explicit target the skills CLI installs into every agent it knows about, which litters a host with config directories for agents it does not have.
            Use --agent <name>[,<name>...] to choose targets yourself, or --agent universal for the shared directory alone. Required when Orca detects no agent.
            Use --dry-run to print the resolved command without running it.
            With --json, the skill listing and --dry-run emit JSON; a real install streams npx's own non-JSON output live and rejects --json.
            Omit --skill and --all to list installable skill names.
            Intended for headless hosts (SSH, containers, CI) with no desktop Settings UI to copy the install command from.

        Examples:
            orca skills install
            orca skills install --skill orca-cli --skill orchestration
            orca skills install --skill orca-cli --local
            orca skills install --skill orca-cli --agent claude-code,codex
            orca skills install --all --dry-run
        """
        return self._client._invoke("skills install", [], [("skill", skill), ("all", all), ("agent", agent), ("local", local), ("dry-run", dry_run)], json=True, remote=True)

    def installed(
        self,
    ) -> Any:
        """List installed skill selectors.

        CLI: ``orca skills installed [--json]``

        Notes:
            Lists discovery IDs and names without reading skill contents into the CLI.
            Package metadata is validated when the selected skills are shared.
            Use an exact ID or an unambiguous name with `orca skills share --skill <selector>`.
        """
        return self._client._invoke("skills installed", [], [], json=True, remote=True)

    def list(
        self,
    ) -> Any:
        """List version-matched skill guides bundled with this Orca CLI.

        CLI: ``orca skills list [--json]``

        Notes:
            Reads bundled guide metadata locally without contacting the Orca runtime.
            With --json, prints a topics array of canonical names and one-line descriptions.
            Use `orca skills get <name>` for the compact guide, `--full` for its full reference package, or `orca skills install` to install skills.
        """
        return self._client._invoke("skills list", [], [], json=True, remote=True)

    def share(
        self,
        *,
        skill: Scalar,
        bundle_name: Scalar,
        release_notes: Scalar | None = None,
    ) -> Any:
        """Publish explicitly selected installed skills behind one unlisted link.

        CLI: ``orca skills share --skill <selector> [--skill <selector> ...] --bundle-name <name> [--release-notes <text>] [--json]``

        Notes:
            Requires the default-off permission in Settings → Share Skills.
            The bundle name may be human-readable; Orca converts it to a portable lowercase package name.
            Selectors are exact discovery IDs or unambiguous names from `orca skills installed`.
            Only discovered skill directories can be selected; arbitrary paths and --all are not supported.
            The resulting link is unlisted. Anyone with it can inspect and install the bundle.

        Examples:
            orca skills share --skill frontend --bundle-name "Frontend Skills"
            orca skills share --skill frontend --skill testing --bundle-name "Team Toolkit" --json
        """
        return self._client._invoke("skills share", [], [("skill", skill), ("bundle-name", bundle_name), ("release-notes", release_notes)], json=True, remote=True)

    def update(
        self,
        *,
        skill: Scalar | None = None,
        all: bool = False,
        agent: Scalar | None = None,
        local: bool = False,
        dry_run: bool = False,
    ) -> Any:
        """Update Orca skills to the version this Orca build ships.

        CLI: ``orca skills update [--skill <name>]... [--all] [--agent <name>[,<name>]] [--local] [--dry-run] [--json]``

        Notes:
            Reads the bundled skill registry locally without contacting the Orca runtime.
            Runs the same pinned `npx skills add` command as `orca skills install`, which replaces each selected skill with the copy this Orca build ships.
            Updates the global install (all projects, adds --global) by default. Use --local to update the current project instead.
            Targets the same agents as `orca skills install`, or only the shared .agents/skills directory when none is detected; use --agent to choose them yourself.
            Use --dry-run to print the resolved command without running it.
            With --json, the skill listing and --dry-run emit JSON; a real update streams npx's own non-JSON output live and rejects --json.
            Omit --skill and --all to list updatable skill names.
            Intended for headless hosts (SSH, containers, CI) with no desktop Settings UI to copy the update command from.

        Examples:
            orca skills update
            orca skills update --skill orca-cli --skill orchestration
            orca skills update --skill orca-cli --local
            orca skills update --all --dry-run
        """
        return self._client._invoke("skills update", [], [("skill", skill), ("all", all), ("agent", agent), ("local", local), ("dry-run", dry_run)], json=True, remote=True)

class SpeechOpenaiKeyResource(_Resource):
    """Commands under ``orca speech openai-key``."""

    def clear(
        self,
    ) -> Any:
        """Remove the OpenAI key cloud voice dictation uses on this host.

        CLI: ``orca speech openai-key clear [--json]``

        Examples:
            orca speech openai-key clear
        """
        return self._client._invoke("speech openai-key clear", [], [], json=True, remote=True)

    def set(
        self,
        *,
        stdin: str | bytes | None = None,
    ) -> Any:
        """Save the OpenAI key cloud voice dictation uses on this host, read from stdin.

        CLI: ``orca speech openai-key set [--json] < key-file``

        Notes:
            Reads the key from stdin so it never lands in shell history or a process list.
            The host that runs dictation seals it, so a headless `orca serve` host can use it.

        Examples:
            printf %s "$OPENAI_API_KEY" | orca speech openai-key set
            $env:OPENAI_API_KEY | orca speech openai-key set
        """
        return self._client._invoke("speech openai-key set", [], [], json=True, remote=True, stdin=stdin)

    def status(
        self,
    ) -> Any:
        """Show whether this host has an OpenAI key for cloud voice dictation.

        CLI: ``orca speech openai-key status [--json]``

        Examples:
            orca speech openai-key status --json
        """
        return self._client._invoke("speech openai-key status", [], [], json=True, remote=True)

class SpeechResource(_Resource):
    """Commands under ``orca speech``."""

    @cached_property
    def openai_key(self) -> SpeechOpenaiKeyResource:
        """``orca speech openai-key`` commands."""
        return SpeechOpenaiKeyResource(self._client)

class StorageLocalResource(_Resource):
    """Commands under ``orca storage local``."""

    def clear(
        self,
        *,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Clear all localStorage.

        CLI: ``orca storage local clear [--worktree <selector>] [--json]``
        """
        return self._client._invoke("storage local clear", [], [("worktree", worktree), ("page", page)], json=True, remote=True)

    def get(
        self,
        *,
        key: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Get a localStorage value by key.

        CLI: ``orca storage local get --key <key> [--worktree <selector>] [--json]``
        """
        return self._client._invoke("storage local get", [], [("key", key), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def set(
        self,
        *,
        key: Scalar,
        value: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Set a localStorage value.

        CLI: ``orca storage local set --key <key> --value <value> [--worktree <selector>] [--json]``
        """
        return self._client._invoke("storage local set", [], [("key", key), ("value", value), ("worktree", worktree), ("page", page)], json=True, remote=True)

class StorageSessionResource(_Resource):
    """Commands under ``orca storage session``."""

    def clear(
        self,
        *,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Clear all sessionStorage.

        CLI: ``orca storage session clear [--worktree <selector>] [--json]``
        """
        return self._client._invoke("storage session clear", [], [("worktree", worktree), ("page", page)], json=True, remote=True)

    def get(
        self,
        *,
        key: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Get a sessionStorage value by key.

        CLI: ``orca storage session get --key <key> [--worktree <selector>] [--json]``
        """
        return self._client._invoke("storage session get", [], [("key", key), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def set(
        self,
        *,
        key: Scalar,
        value: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Set a sessionStorage value.

        CLI: ``orca storage session set --key <key> --value <value> [--worktree <selector>] [--json]``
        """
        return self._client._invoke("storage session set", [], [("key", key), ("value", value), ("worktree", worktree), ("page", page)], json=True, remote=True)

class StorageResource(_Resource):
    """Commands under ``orca storage``."""

    @cached_property
    def local(self) -> StorageLocalResource:
        """``orca storage local`` commands."""
        return StorageLocalResource(self._client)

    @cached_property
    def session(self) -> StorageSessionResource:
        """``orca storage session`` commands."""
        return StorageSessionResource(self._client)

class TabProfileResource(_Resource):
    """Commands under ``orca tab profile``."""

    def clone(
        self,
        *,
        profile: Scalar,
        page: Scalar | None = None,
        worktree: Scalar | None = None,
    ) -> Any:
        """Clone a browser tab into a different browser profile.

        CLI: ``orca tab profile clone --profile <id> [--page <id>] [--worktree <selector>] [--json]``
        """
        return self._client._invoke("tab profile clone", [], [("profile", profile), ("page", page), ("worktree", worktree)], json=True, remote=True)

    def create(
        self,
        *,
        label: Scalar,
        scope: Scalar | None = None,
    ) -> Any:
        """Create a browser session profile for browser tabs.

        CLI: ``orca tab profile create --label <name> [--scope <isolated|imported>] [--json]``
        """
        return self._client._invoke("tab profile create", [], [("label", label), ("scope", scope)], json=True, remote=True)

    def delete(
        self,
        *,
        profile: Scalar,
    ) -> Any:
        """Delete a browser session profile used by browser tabs.

        CLI: ``orca tab profile delete --profile <id> [--json]``
        """
        return self._client._invoke("tab profile delete", [], [("profile", profile)], json=True, remote=True)

    def list(
        self,
    ) -> Any:
        """List browser session profiles available to browser tabs.

        CLI: ``orca tab profile list [--json]``
        """
        return self._client._invoke("tab profile list", [], [], json=True, remote=True)

    def set(
        self,
        *,
        profile: Scalar,
        page: Scalar | None = None,
        worktree: Scalar | None = None,
    ) -> Any:
        """Switch a browser tab to a different browser profile.

        CLI: ``orca tab profile set (--page <id> | --worktree <selector>) --profile <id> [--json]``
        """
        return self._client._invoke("tab profile set", [], [("profile", profile), ("page", page), ("worktree", worktree)], json=True, remote=True)

    def show(
        self,
        *,
        page: Scalar,
        worktree: Scalar | None = None,
    ) -> Any:
        """Show the browser profile bound to a tab.

        CLI: ``orca tab profile show --page <id> [--worktree <selector>] [--json]``
        """
        return self._client._invoke("tab profile show", [], [("page", page), ("worktree", worktree)], json=True, remote=True)

    def use_default(
        self,
        *,
        page: Scalar,
        worktree: Scalar | None = None,
    ) -> Any:
        """Switch a browser tab back to the default browser profile.

        CLI: ``orca tab profile use-default --page <id> [--worktree <selector>] [--json]``
        """
        return self._client._invoke("tab profile use-default", [], [("page", page), ("worktree", worktree)], json=True, remote=True)

class TabResource(_Resource):
    """Commands under ``orca tab``."""

    @cached_property
    def profile(self) -> TabProfileResource:
        """``orca tab profile`` commands."""
        return TabProfileResource(self._client)

    def close(
        self,
        *,
        index: int | str | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Close a browser tab.

        CLI: ``orca tab close [--index <n>] [--worktree <selector>] [--json]``
        """
        return self._client._invoke("tab close", [], [("index", index), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def create(
        self,
        *,
        url: Scalar | None = None,
        worktree: Scalar | None = None,
        profile: Scalar | None = None,
    ) -> Any:
        """Create a new browser tab in the current worktree.

        CLI: ``orca tab create [--url <url>] [--worktree <selector>] [--profile <id>] [--json]``
        """
        return self._client._invoke("tab create", [], [("url", url), ("worktree", worktree), ("profile", profile)], json=True, remote=True)

    def current(
        self,
        *,
        worktree: Scalar | None = None,
    ) -> Any:
        """Show the current browser tab.

        CLI: ``orca tab current [--worktree <selector|all>] [--json]``
        """
        return self._client._invoke("tab current", [], [("worktree", worktree)], json=True, remote=True)

    def list(
        self,
        *,
        worktree: Scalar | None = None,
        show_profile: bool = False,
    ) -> Any:
        """List open browser tabs.

        CLI: ``orca tab list [--worktree <selector|all>] [--show-profile] [--json]``
        """
        return self._client._invoke("tab list", [], [("worktree", worktree), ("show-profile", show_profile)], json=True, remote=True)

    def show(
        self,
        *,
        page: Scalar,
        worktree: Scalar | None = None,
    ) -> Any:
        """Show one browser tab by page id.

        CLI: ``orca tab show --page <id> [--worktree <selector>] [--json]``
        """
        return self._client._invoke("tab show", [], [("page", page), ("worktree", worktree)], json=True, remote=True)

    def switch(
        self,
        *,
        index: int | str | None = None,
        page: Scalar | None = None,
        worktree: Scalar | None = None,
        focus: bool = False,
    ) -> Any:
        """Switch the active browser tab.

        CLI: ``orca tab switch (--index <n> | --page <id>) [--worktree <selector>] [--focus] [--json]``
        """
        return self._client._invoke("tab switch", [], [("index", index), ("page", page), ("worktree", worktree), ("focus", focus)], json=True, remote=True)

class TerminalResource(_Resource):
    """Commands under ``orca terminal``."""

    def close(
        self,
        *,
        terminal: Scalar | None = None,
        tab: bool = False,
        worktree: Scalar | None = None,
        all: bool = False,
    ) -> Any:
        """Close one terminal, its whole tab, or every terminal in a workspace.

        CLI: ``orca terminal close ([--terminal <handle>] [--tab] | --worktree <selector> --all) [--json]``

        Notes:
            Without --all, closes one terminal pane/session; add --tab to close its whole tab.
            With --worktree <selector> --all, stops every terminal process owned by that workspace and durably removes its terminal tabs, layouts, and resume records.
            Use workspace Sleep when the terminals and agent sessions should resume later.

        Examples:
            orca terminal close --terminal term_abc123
            orca terminal close --terminal term_abc123 --tab --json
            orca terminal close --worktree active --all --json
        """
        return self._client._invoke("terminal close", [], [("terminal", terminal), ("tab", tab), ("worktree", worktree), ("all", all)], json=True, remote=True)

    def create(
        self,
        *,
        worktree: Scalar | None = None,
        command: Scalar | None = None,
        shell: Scalar | None = None,
        title: Scalar | None = None,
        focus: bool = False,
    ) -> Any:
        """Create a terminal session in the current worktree.

        CLI: ``orca terminal create [--worktree <selector>] [--title <name>] [--command <text>] [--shell <shell>] [--focus] [--json]``

        Notes:
            Creates a visible terminal tab without switching focus when possible; falls back to a background handle if the UI cannot adopt it. Pass --focus to switch to it.
            This creates a terminal and runs --command in it. To start an agent, use `orca agent launch` (or `orca worktree create --agent` for a new checkout), which follows your Chat UI setting.
            --shell picks the shell the terminal IS on a Windows host (cmd.exe, powershell.exe, pwsh.exe, wsl.exe, bash.exe, git-bash); --command is typed into whatever shell the host started, so `--command cmd.exe` leaves a cmd running INSIDE the default shell and exiting it drops back to that shell.
            A host that cannot apply --shell refuses the create rather than quietly spawning its default shell: macOS and Linux execution hosts spawn the login shell, terminals routed over SSH resolve their shell on the SSH host, a --shell that contradicts the project execution runtime (WSL vs Windows host) is refused, and an Orca host older than --shell is refused by the CLI.

        Examples:
            orca terminal create --json
            orca terminal create --worktree active --command "pnpm dev" --json
            orca terminal create --worktree path:/projects/myapp --title "RUNNER" --command "npm test"
            orca terminal create --worktree path:/projects/myapp --command "pnpm dev" --focus
            orca terminal create --worktree path:C:/src/app --shell cmd.exe --json
        """
        return self._client._invoke("terminal create", [], [("worktree", worktree), ("command", command), ("shell", shell), ("title", title), ("focus", focus)], json=True, remote=True)

    def list(
        self,
        *,
        worktree: Scalar | None = None,
        limit: int | str | None = None,
        include_visual_layouts: bool = False,
    ) -> Any:
        """List live Orca-managed terminals.

        CLI: ``orca terminal list [--worktree <selector>] [--limit <n>] [--include-visual-layouts] [--json]``

        Notes:
            JSON omits visualLayouts by default; pass --include-visual-layouts when machine-readable tab and pane topology is required.
        """
        return self._client._invoke("terminal list", [], [("worktree", worktree), ("limit", limit), ("include-visual-layouts", include_visual_layouts)], json=True, remote=True)

    def read(
        self,
        *,
        terminal: Scalar | None = None,
        cursor: int | str | None = None,
        limit: int | str | None = None,
        screen: bool = False,
    ) -> Any:
        """Read bounded terminal output.

        CLI: ``orca terminal read [--terminal <handle>] [--cursor <n>] [--limit <n>] [--screen] [--json]``

        Notes:
            Omit --terminal to target the active terminal in the current worktree.
            By default this returns accumulated terminal output with escape sequences stripped, not the rendered screen. Any program that repaints a line — shells, progress bars, TUIs — comes back as stacked fragments, so one `clear` keystroke by keystroke reads as `cclclecleaclear`, and spaces a prompt draws by moving the cursor are absent.
            Use --screen to read what the terminal actually renders. Prefer it whenever the answer depends on how output looks rather than what was emitted over time; the default is unsuitable for verifying rendered output.
            The result reports source: stream when it is accumulated output, screen when it is the rendered screen, and screen-unavailable when a screen was asked for but none could be rendered and the accumulated output is being returned instead. An absent source means the host predates the field.
            When present, draft is UI-only composer text excluded from tail; never treat it as terminal output or a submitted instruction.
            --screen and --cursor are mutually exclusive: a screen read is the current frame and has no history to page.
            Use --cursor with the nextCursor value from a previous read to get only new output since that read.
            Use --limit to request more retained lines for long agent responses; output reports oldestCursor when older lines were dropped.
            Useful for capturing the response to a command: read before sending, then read --cursor <prev> after waiting.

        Examples:
            orca terminal read --json
            orca terminal read --terminal term_abc123 --cursor 42 --limit 1000 --json
            orca terminal read --terminal term_abc123 --screen --json
        """
        return self._client._invoke("terminal read", [], [("terminal", terminal), ("cursor", cursor), ("limit", limit), ("screen", screen)], json=True, remote=True)

    def rename(
        self,
        *,
        terminal: Scalar | None = None,
        title: Scalar | None = None,
    ) -> Any:
        """Set or clear the title of a terminal tab.

        CLI: ``orca terminal rename [--terminal <handle>] [--title <text>] [--json]``

        Notes:
            Omit --title or pass an empty string to reset to the auto-generated title.

        Examples:
            orca terminal rename --terminal term_abc123 --title "RUNNER"
            orca terminal rename --terminal term_abc123 --json
        """
        return self._client._invoke("terminal rename", [], [("terminal", terminal), ("title", title)], json=True, remote=True)

    def send(
        self,
        *,
        terminal: Scalar | None = None,
        text: Scalar | None = None,
        enter: bool = False,
        interrupt: bool = False,
        wait_submit: int | str | None = None,
        retry_request: Scalar | None = None,
    ) -> Any:
        """Send input to a live terminal.

        CLI: ``orca terminal send [--terminal <handle>] [--text <text>] [--enter] [--interrupt] [--wait-submit <seconds>] [--retry-request <id>] [--json]``

        Notes:
            For a text-plus-Enter agent prompt, the result separates input acceptance from observed submission and turn start.
            --wait-submit only observes the accepted prompt for the requested duration; timeout returns the queued/input-accepted receipt and never resends.
            After an ambiguous transport failure, reissue the exact command with the reported --retry-request ID. The ID is bound to the prompt payload and exact terminal process incarnation.
            Older hosts accept the legacy raw input but report provider old-host and do not offer idempotent retry or submission observation.
        """
        return self._client._invoke("terminal send", [], [("terminal", terminal), ("text", text), ("enter", enter), ("interrupt", interrupt), ("wait-submit", wait_submit), ("retry-request", retry_request)], json=True, remote=True)

    def set_pane_title(
        self,
        *,
        title: Scalar,
        terminal: Scalar | None = None,
    ) -> Any:
        """Set or clear the title of one terminal pane.

        CLI: ``orca terminal set-pane-title [--terminal <handle>] --title <text> [--json]``

        Notes:
            Sets the title of ONE pane. Split panes share a tab, so terminal rename cannot address one of them; use this command for a single pane.
            Requires the running Orca desktop; headless pane title changes are not supported.
            Pass --title "" to clear the pane back to its automatic title.

        Examples:
            orca terminal set-pane-title --terminal term_abc123 --title "RUNNER"
            orca terminal set-pane-title --terminal term_abc123 --title "" --json
        """
        return self._client._invoke("terminal set-pane-title", [], [("terminal", terminal), ("title", title)], json=True, remote=True)

    def show(
        self,
        *,
        terminal: Scalar | None = None,
    ) -> Any:
        """Show terminal metadata and preview.

        CLI: ``orca terminal show [--terminal <handle>] [--json]``
        """
        return self._client._invoke("terminal show", [], [("terminal", terminal)], json=True, remote=True)

    def split(
        self,
        *,
        terminal: Scalar | None = None,
        direction: Scalar | None = None,
        command: Scalar | None = None,
    ) -> Any:
        """Split an existing terminal pane.

        CLI: ``orca terminal split [--terminal <handle>] [--direction horizontal|vertical] [--command <text>] [--json]``

        Examples:
            orca terminal split --terminal term_abc123 --direction horizontal --json
            orca terminal split --terminal term_abc123 --command "codex"
        """
        return self._client._invoke("terminal split", [], [("terminal", terminal), ("direction", direction), ("command", command)], json=True, remote=True)

    def switch(
        self,
        *,
        terminal: Scalar | None = None,
    ) -> Any:
        """Switch to a terminal tab in the UI.

        CLI: ``orca terminal switch [--terminal <handle>] [--json]``

        Notes:
            With --environment, the desktop app on this machine switches to that server's terminal; a server has no window of its own.

        Examples:
            orca terminal switch --terminal term_abc123
        """
        return self._client._invoke("terminal switch", [], [("terminal", terminal)], json=True, remote=True)

    def wait(
        self,
        *,
        for_: Scalar,
        terminal: Scalar | None = None,
        timeout_ms: int | str | None = None,
    ) -> Any:
        """Wait for a terminal condition.

        CLI: ``orca terminal wait [--terminal <handle>] --for exit|tui-idle [--timeout-ms <ms>] [--json]``
        """
        return self._client._invoke("terminal wait", [], [("terminal", terminal), ("for", for_), ("timeout-ms", timeout_ms)], json=True, remote=True)

class TerminalDaemonResource(_Resource):
    """Commands under ``orca terminal-daemon``."""

    def restart(
        self,
        *,
        yes: bool = False,
        page: Scalar | None = None,
    ) -> Any:
        """Restart a terminal daemon whose program files are gone.

        CLI: ``orca terminal-daemon restart --yes [--json]``

        Notes:
            Restarting ENDS every process running in its terminals. Agents that support resume can be resumed afterwards; shells and other jobs must be started again.
            The host re-checks that the daemon is still the one reported by status before stopping it, and refuses otherwise.

        Examples:
            orca terminal-daemon restart --yes
        """
        return self._client._invoke("terminal-daemon restart", [], [("yes", yes), ("page", page)], json=True, remote=True)

    def status(
        self,
        *,
        page: Scalar | None = None,
    ) -> Any:
        """Report whether the terminal daemon is running, its process ceiling, and whether it still has its program files.

        CLI: ``orca terminal-daemon status [--json]``

        Notes:
            The daemon is reported live, exited, or unverifiable. Orca starts a new daemon with the next terminal after one exits, so exited between a crash and that terminal is expected.
            For a live daemon it also reports the terminal process ceiling: on with its limit, or off with the reason.
            On Linux AppImage, a daemon started by an earlier Orca can outlive the files it runs from. Orca keeps it so its terminals keep running, but new terminals are not kept across restarts until it is restarted.

        Examples:
            orca terminal-daemon status --json
        """
        return self._client._invoke("terminal-daemon status", [], [("page", page)], json=True, remote=True)

class VmRecipeResource(_Resource):
    """Commands under ``orca vm recipe``."""

    def doctor(
        self,
        recipe_id: Scalar,
        *,
        repo_path: Scalar | None = None,
        provision: bool = False,
        connect: bool = False,
        page: Scalar | None = None,
    ) -> Any:
        """Validate a per-workspace environment recipe without provisioning by default.

        CLI: ``orca vm recipe doctor <recipe-id> [--repo-path <path>] [--provision|--connect] [--json]``

        Notes:
            Reads environmentRecipes from orca.yaml in the repo path, validates the selected recipe, and reports agent-friendly checks.
            This default mode is non-destructive and does not run the recipe command.
            Use --provision or --connect to run the recipe, validate its result, and run cleanup when configured.

        Examples:
            orca vm recipe doctor cloud-sandbox
            orca vm recipe doctor cloud-sandbox --repo-path /path/to/repo --json
            orca vm recipe doctor cloud-sandbox --provision --json
        """
        return self._client._invoke("vm recipe doctor", [recipe_id], [("repo-path", repo_path), ("provision", provision), ("connect", connect), ("page", page)], json=True, remote=True)

class VmResource(_Resource):
    """Commands under ``orca vm``."""

    @cached_property
    def recipe(self) -> VmRecipeResource:
        """``orca vm recipe`` commands."""
        return VmRecipeResource(self._client)

class WorktreeResource(_Resource):
    """Commands under ``orca worktree``."""

    def create(
        self,
        *,
        name: Scalar,
        repo: Scalar | None = None,
        project: Scalar | None = None,
        host: Scalar | None = None,
        project_host_setup: Scalar | None = None,
        agent: Scalar | None = None,
        prompt: Scalar | None = None,
        model: Scalar | None = None,
        effort: Scalar | None = None,
        surface: Scalar | None = None,
        retry_launch: Scalar | None = None,
        base_branch: Scalar | None = None,
        reference: Scalar | Sequence[Scalar] | None = None,
        reference_site: Scalar | None = None,
        issue: int | str | None = None,
        pr: int | str | None = None,
        linear_issue: Scalar | None = None,
        gitlab_issue: Scalar | None = None,
        gitlab_mr: Scalar | None = None,
        comment: Scalar | None = None,
        setup: Scalar | None = None,
        parent_worktree: Scalar | None = None,
        no_parent: bool = False,
        run_hooks: bool = False,
        activate: bool = False,
    ) -> Any:
        """Create a new Orca-managed worktree.

        CLI: ``orca worktree create --name <name> [--repo <selector>|--project <id-or-name> [--host <host>]|--project-host-setup <id>] [--agent <id>] [--prompt <text>] [--model <id>] [--effort <level>] [--surface chat|terminal] [--setup run|skip|inherit] [--base-branch <ref>] [--reference <url-or-jira-key>...] [--reference-site <id>] [--issue <number>] [--pr <number>] [--linear-issue <identifier-or-url>] [--gitlab-issue <number-or-url>] [--gitlab-mr <number-or-url>] [--comment <text>] [--parent-worktree <selector>] [--no-parent] [--run-hooks] [--activate] [--retry-launch <operationId>] [--json]``

        Notes:
            Repeat --reference to attach full issue or review URLs, or Jira issue keys, before setup or agent startup. Use --reference-site to choose the Jira site for keys. Other providers require full URLs. Cannot combine with legacy link flags.
            This creates a new checkout. For a fresh agent in an existing worktree, use `orca agent launch` instead.
            By default, Orca records the new worktree as a child of the caller context when it can infer one from the Orca terminal or current directory.
            If --repo is omitted, Orca infers the repo from the current Orca-managed worktree.
            Use --project to create on a ready project host setup without spelling the backing repo id. --project takes the project id or the display name from `orca project list`.
            --host is only needed when the project is set up on more than one host; with a single setup Orca uses it. When it is ambiguous the error names every host the project is set up on.
            --host takes local, ssh:<target-id>, runtime:<environment-id>, or the bare host name `orca host list` prints for any of them.
            For related work, use the inferred parent or pass --parent-worktree active, folder:<id>, or worktree:<worktreeId> to make the relationship explicit. Worktree ids are the full <repo-id>::<path> values returned by `orca worktree list --json`.
            Use --no-parent when the new worktree should be independent of the current context.
            --no-parent only affects Orca lineage; omit --base-branch to use the repo default base, or pass the default base ref explicitly for independent top-level work.
            By default this creates the worktree and its first terminal without switching the active Orca view.
            Pass --agent to start an agent with the worktree, as a chat or a terminal per your Chat UI setting, exactly as a new agent tab does; --prompt sends initial work to it. --model and --effort pick its model and reasoning effort, and --surface chat|terminal picks chat or terminal for this launch instead of your setting.
            After a lost agent launch reply, re-issue the same command from the same directory on the same host with --retry-launch <operationId> from the error. Never retry as a fresh launch; older hosts require inspecting the workspace first.
            With --agent --json, result.launch says what started: launch.outcome.kind (structured chat or terminal), launch.outcome.handle, and launch.receipt.detail for why. An Orca host older than this returns the terminal agent handle in result.agentTerminalHandle instead.
            Repo-defined setup hooks follow the repository setup policy; pass --setup run to force them.
            Pass --activate when the CLI caller intentionally wants to reveal the new worktree in the app.
            Passing --run-hooks is kept as a legacy alias for --setup run and reveals the worktree.
            Use --pr for GitHub pull requests; --gitlab-issue and --gitlab-mr write separate GitLab links. GitLab URLs must match the stored source project or remote; they cannot select a foreign project.

        Examples:
            orca worktree create --name agent-task --agent codex --prompt "hi" --json
            orca worktree create --name design --no-parent --agent codex --model gpt-6-astra --effort high --prompt "Write the design doc" --json
            orca worktree create --repo id:<repoId> --name related-task --json
            orca worktree create --project github:stablyai/orca --host runtime:03ef704c-b180-4b10-998d-e28fbd5de9a3 --name benchmark --json
            orca worktree create --repo id:<repoId> --name linear-task --linear-issue https://linear.app/stably/issue/STA-335/test-issue --json
            orca worktree create --repo id:<repoId> --name agent-task --agent codex --prompt "hi" --json
            orca worktree create --repo id:<repoId> --name folder-child --parent-worktree folder:<folderId> --json
            orca worktree create --repo id:<repoId> --name related-task --parent-worktree active --json
            orca worktree create --repo id:<repoId> --name independent-task --no-parent --json
        """
        return self._client._invoke("worktree create", [], [("repo", repo), ("project", project), ("host", host), ("project-host-setup", project_host_setup), ("name", name), ("agent", agent), ("prompt", prompt), ("model", model), ("effort", effort), ("surface", surface), ("retry-launch", retry_launch), ("base-branch", base_branch), ("reference", reference), ("reference-site", reference_site), ("issue", issue), ("pr", pr), ("linear-issue", linear_issue), ("gitlab-issue", gitlab_issue), ("gitlab-mr", gitlab_mr), ("comment", comment), ("setup", setup), ("parent-worktree", parent_worktree), ("no-parent", no_parent), ("run-hooks", run_hooks), ("activate", activate)], json=True, remote=True)

    def current(
        self,
    ) -> Any:
        """Show the Orca-managed worktree for the current directory.

        CLI: ``orca worktree current [--json]``

        Notes:
            Resolves the current shell directory to a path: selector so agents can target the enclosing Orca worktree without spelling out $PWD.

        Examples:
            orca worktree current
            orca worktree current --json
        """
        return self._client._invoke("worktree current", [], [], json=True, remote=True)

    def list(
        self,
        *,
        repo: Scalar | None = None,
        limit: int | str | None = None,
    ) -> Any:
        """List Orca-managed worktrees.

        CLI: ``orca worktree list [--repo <selector>] [--limit <n>] [--json]``

        Notes:
            Each row carries the execution host that owns it (`host=`), and the trailing `scope:` line names every host the page covers plus the ones it does not.
            A host named under `not covered` may still have workspaces; an empty answer for it is not evidence that it has none. A paired server is annotated with the `--environment` flag that reaches it; this machine and its SSH targets are reached through the same runtime, so no flag selects them.
            The row cap is shared across hosts, so a host whose rows sort last is not starved out of the page.
        """
        return self._client._invoke("worktree list", [], [("repo", repo), ("limit", limit)], json=True, remote=True)

    def ps(
        self,
        *,
        limit: int | str | None = None,
    ) -> Any:
        """Show a compact orchestration summary across worktrees.

        CLI: ``orca worktree ps [--limit <n>] [--json]``

        Notes:
            Each row carries the execution host that owns it (`host=`), and the trailing `scope:` line names every host the page covers plus the ones it does not.
            A host named under `not covered` may still have workspaces; an empty answer for it is not evidence that it has none. A paired server is annotated with the `--environment` flag that reaches it; this machine and its SSH targets are reached through the same runtime, so no flag selects them.
            The row cap is shared across hosts, so a host whose rows sort last is not starved out of the page.
        """
        return self._client._invoke("worktree ps", [], [("limit", limit)], json=True, remote=True)

    def rm(
        self,
        *,
        worktree: Scalar,
        force: bool = False,
        run_hooks: bool = False,
        allow_failed_archive_hook: bool = False,
    ) -> Any:
        """Remove a worktree from Orca and git.

        CLI: ``orca worktree rm --worktree <selector> [--force] [--run-hooks] [--allow-failed-archive-hook] [--json]``

        Notes:
            Repo-defined orca.yaml archive hooks are skipped unless --run-hooks is passed.
            With --run-hooks, a failed archive hook blocks the removal: nothing is stopped, deleted or deregistered, and the command exits non-zero with error code worktree_archive_hook_failed. --force does not waive this.
            Pass --allow-failed-archive-hook to delete anyway after the hook has run and failed; the waived failure is reported back on result.archiveHookOverride. It requires --run-hooks and is rejected without it, because with no hook running there is no failure to waive.
            For Git worktrees, removal also attempts to delete the checked-out local branch, with or without --force. Orca retains branches it knows predated the worktree and any branch whose changes it cannot prove are already merged.
        """
        return self._client._invoke("worktree rm", [], [("worktree", worktree), ("force", force), ("run-hooks", run_hooks), ("allow-failed-archive-hook", allow_failed_archive_hook)], json=True, remote=True)

    def set(
        self,
        *,
        worktree: Scalar,
        display_name: Scalar | None = None,
        issue: Scalar | None = None,
        pr: Scalar | None = None,
        linear_issue: Scalar | None = None,
        gitlab_issue: Scalar | None = None,
        gitlab_mr: Scalar | None = None,
        comment: Scalar | None = None,
        workspace_status: Scalar | None = None,
        unread: bool = False,
        read: bool = False,
        parent_worktree: Scalar | None = None,
        no_parent: bool = False,
    ) -> Any:
        """Update Orca metadata for a worktree.

        CLI: ``orca worktree set --worktree <selector> [--display-name <name>] [--issue <number|null>] [--pr <number|null>] [--linear-issue <identifier-or-url|null>] [--gitlab-issue <number-or-url|null>] [--gitlab-mr <number-or-url|null>] [--comment <text>] [--workspace-status <id>] [--unread|--read] [--parent-worktree <selector>|--no-parent] [--json]``

        Notes:
            Workspace status ids match the board columns (defaults: todo, in-progress, in-review, completed); custom statuses use their configured id.
            Pass --linear-issue null to clear the Linear issue link.
            Pass --pr null, --gitlab-issue null, or --gitlab-mr null to clear only the matching link.
            Each link flag updates its own field and leaves unrelated links unchanged. GitLab URLs must match the stored source project or remote; they cannot select a foreign project.

        Examples:
            orca worktree set --worktree active --linear-issue STA-335 --json
            orca worktree set --worktree active --linear-issue null --json
            orca worktree set --worktree active --workspace-status in-review --unread --json
        """
        return self._client._invoke("worktree set", [], [("worktree", worktree), ("display-name", display_name), ("issue", issue), ("pr", pr), ("linear-issue", linear_issue), ("gitlab-issue", gitlab_issue), ("gitlab-mr", gitlab_mr), ("comment", comment), ("workspace-status", workspace_status), ("unread", unread), ("read", read), ("parent-worktree", parent_worktree), ("no-parent", no_parent)], json=True, remote=True)

    def show(
        self,
        *,
        worktree: Scalar,
    ) -> Any:
        """Show one worktree.

        CLI: ``orca worktree show --worktree <selector> [--json]``
        """
        return self._client._invoke("worktree show", [], [("worktree", worktree)], json=True, remote=True)

class OrcaCommands(_SyncRoot):
    """All Orca CLI commands."""

    @cached_property
    def account(self) -> AccountResource:
        """``orca account`` commands."""
        return AccountResource(self._client)

    @cached_property
    def agent(self) -> AgentResource:
        """``orca agent`` commands."""
        return AgentResource(self._client)

    @cached_property
    def artifacts(self) -> ArtifactsResource:
        """``orca artifacts`` commands."""
        return ArtifactsResource(self._client)

    @cached_property
    def automations(self) -> AutomationsResource:
        """``orca automations`` commands."""
        return AutomationsResource(self._client)

    @cached_property
    def browser(self) -> BrowserResource:
        """``orca browser`` commands."""
        return BrowserResource(self._client)

    @cached_property
    def capture(self) -> CaptureResource:
        """``orca capture`` commands."""
        return CaptureResource(self._client)

    @cached_property
    def clipboard(self) -> ClipboardResource:
        """``orca clipboard`` commands."""
        return ClipboardResource(self._client)

    @cached_property
    def computer(self) -> ComputerResource:
        """``orca computer`` commands."""
        return ComputerResource(self._client)

    @cached_property
    def cookie(self) -> CookieResource:
        """``orca cookie`` commands."""
        return CookieResource(self._client)

    @cached_property
    def diagnostics(self) -> DiagnosticsResource:
        """``orca diagnostics`` commands."""
        return DiagnosticsResource(self._client)

    @cached_property
    def dialog(self) -> DialogResource:
        """``orca dialog`` commands."""
        return DialogResource(self._client)

    @cached_property
    def emulator(self) -> EmulatorResource:
        """``orca emulator`` commands."""
        return EmulatorResource(self._client)

    @cached_property
    def environment(self) -> EnvironmentResource:
        """``orca environment`` commands."""
        return EnvironmentResource(self._client)

    @cached_property
    def file(self) -> FileResource:
        """``orca file`` commands."""
        return FileResource(self._client)

    @cached_property
    def host(self) -> HostResource:
        """``orca host`` commands."""
        return HostResource(self._client)

    @cached_property
    def intercept(self) -> InterceptResource:
        """``orca intercept`` commands."""
        return InterceptResource(self._client)

    @cached_property
    def jira(self) -> JiraResource:
        """``orca jira`` commands."""
        return JiraResource(self._client)

    @cached_property
    def linear(self) -> LinearResource:
        """``orca linear`` commands."""
        return LinearResource(self._client)

    @cached_property
    def mouse(self) -> MouseResource:
        """``orca mouse`` commands."""
        return MouseResource(self._client)

    @cached_property
    def orchestration(self) -> OrchestrationResource:
        """``orca orchestration`` commands."""
        return OrchestrationResource(self._client)

    @cached_property
    def profile(self) -> ProfileResource:
        """``orca profile`` commands."""
        return ProfileResource(self._client)

    @cached_property
    def project(self) -> ProjectResource:
        """``orca project`` commands."""
        return ProjectResource(self._client)

    @cached_property
    def reference(self) -> ReferenceResource:
        """``orca reference`` commands."""
        return ReferenceResource(self._client)

    @cached_property
    def repo(self) -> RepoResource:
        """``orca repo`` commands."""
        return RepoResource(self._client)

    @cached_property
    def serve(self) -> ServeResource:
        """``orca serve`` commands."""
        return ServeResource(self._client)

    @cached_property
    def set(self) -> SetResource:
        """``orca set`` commands."""
        return SetResource(self._client)

    @cached_property
    def skills(self) -> SkillsResource:
        """``orca skills`` commands."""
        return SkillsResource(self._client)

    @cached_property
    def speech(self) -> SpeechResource:
        """``orca speech`` commands."""
        return SpeechResource(self._client)

    @cached_property
    def storage(self) -> StorageResource:
        """``orca storage`` commands."""
        return StorageResource(self._client)

    @cached_property
    def tab(self) -> TabResource:
        """``orca tab`` commands."""
        return TabResource(self._client)

    @cached_property
    def terminal(self) -> TerminalResource:
        """``orca terminal`` commands."""
        return TerminalResource(self._client)

    @cached_property
    def terminal_daemon(self) -> TerminalDaemonResource:
        """``orca terminal-daemon`` commands."""
        return TerminalDaemonResource(self._client)

    @cached_property
    def vm(self) -> VmResource:
        """``orca vm`` commands."""
        return VmResource(self._client)

    @cached_property
    def worktree(self) -> WorktreeResource:
        """``orca worktree`` commands."""
        return WorktreeResource(self._client)

    def agent_context(
        self,
    ) -> Any:
        """Print the machine-readable command schema for agents.

        CLI: ``orca agent-context [--json]``

        Notes:
            Pure local read of the command registry — works without a running Orca app, so it is safe over SSH and in headless contexts.

        Examples:
            orca agent-context --json
        """
        return self._client._invoke("agent-context", [], [], json=True, remote=True)

    def back(
        self,
        *,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Navigate back in browser history.

        CLI: ``orca back [--worktree <selector>] [--json]``
        """
        return self._client._invoke("back", [], [("worktree", worktree), ("page", page)], json=True, remote=True)

    def check(
        self,
        *,
        element: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Check a checkbox/radio by ref.

        CLI: ``orca check --element <ref> [--worktree <selector>] [--json]``
        """
        return self._client._invoke("check", [], [("element", element), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def claude_teams(
        self,
        *args: str,
    ) -> Any:
        """Start Claude Code Agent Teams in the current Orca terminal.

        CLI: ``orca claude-teams [claude args...]``

        Notes:
            Passes all following arguments through to Claude Code after enabling Agent Teams native panes.
            Must be run from inside an Orca terminal. Starts Claude Code Agent Teams in the current pane and opens teammates as native Orca splits.

        Examples:
            orca claude-teams
            orca claude-teams --resume <session-id>
        """
        return self._client._invoke("claude-teams", list(args), [], json=False, remote=False)

    def clear(
        self,
        *,
        element: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Clear an input element by ref.

        CLI: ``orca clear --element <ref> [--worktree <selector>] [--json]``
        """
        return self._client._invoke("clear", [], [("element", element), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def click(
        self,
        *,
        element: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Click a browser element by ref.

        CLI: ``orca click --element <ref> [--worktree <selector>] [--json]``
        """
        return self._client._invoke("click", [], [("element", element), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def console(
        self,
        *,
        limit: int | str | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Show captured console log entries.

        CLI: ``orca console [--limit <n>] [--worktree <selector>] [--json]``
        """
        return self._client._invoke("console", [], [("limit", limit), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def dblclick(
        self,
        *,
        element: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Double-click element by ref.

        CLI: ``orca dblclick --element <ref> [--worktree <selector>] [--json]``
        """
        return self._client._invoke("dblclick", [], [("element", element), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def download(
        self,
        *,
        selector: Scalar,
        path: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Download a file by clicking a selector.

        CLI: ``orca download --selector <ref> --path <path> [--worktree <selector>] [--json]``
        """
        return self._client._invoke("download", [], [("selector", selector), ("path", path), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def drag(
        self,
        *,
        from_: Scalar,
        to: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Drag from one element to another.

        CLI: ``orca drag --from <ref> --to <ref> [--worktree <selector>] [--json]``
        """
        return self._client._invoke("drag", [], [("from", from_), ("to", to), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def eval(
        self,
        *,
        expression: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Evaluate JavaScript in the browser page context.

        CLI: ``orca eval --expression <js> [--worktree <selector>] [--json]``
        """
        return self._client._invoke("eval", [], [("expression", expression), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def exec(
        self,
        *,
        command: bool = False,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Run any agent-browser command against the active browser tab.

        CLI: ``orca exec --command "<agent-browser command>" [--worktree <selector>] [--json]``
        """
        return self._client._invoke("exec", [], [("command", command), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def fill(
        self,
        *,
        element: Scalar,
        value: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Clear and fill a browser input by ref.

        CLI: ``orca fill --element <ref> --value <text> [--worktree <selector>] [--json]``
        """
        return self._client._invoke("fill", [], [("element", element), ("value", value), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def find(
        self,
        *,
        locator: Scalar,
        value: Scalar,
        action: Scalar,
        text: Scalar | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Find element by semantic locator and perform action.

        CLI: ``orca find --locator <type> --value <text> --action <action> [--text <text>] [--worktree <selector>] [--json]``
        """
        return self._client._invoke("find", [], [("locator", locator), ("value", value), ("action", action), ("text", text), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def focus(
        self,
        *,
        element: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Focus a browser element by ref.

        CLI: ``orca focus --element <ref> [--worktree <selector>] [--json]``
        """
        return self._client._invoke("focus", [], [("element", element), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def forward(
        self,
        *,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Navigate forward in browser history.

        CLI: ``orca forward [--worktree <selector>] [--json]``
        """
        return self._client._invoke("forward", [], [("worktree", worktree), ("page", page)], json=True, remote=True)

    def full_screenshot(
        self,
        *,
        format: Scalar | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Capture a full-page screenshot (beyond viewport).

        CLI: ``orca full-screenshot [--format <png|jpeg>] [--worktree <selector>] [--json]``
        """
        return self._client._invoke("full-screenshot", [], [("format", format), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def geolocation(
        self,
        *,
        latitude: int | str,
        longitude: int | str,
        accuracy: int | str | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Override browser geolocation.

        CLI: ``orca geolocation --latitude <lat> --longitude <lon> [--accuracy <n>] [--worktree <selector>] [--json]``
        """
        return self._client._invoke("geolocation", [], [("latitude", latitude), ("longitude", longitude), ("accuracy", accuracy), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def get(
        self,
        *,
        what: Scalar,
        element: Scalar | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Get element property (text, html, value, url, title, count, box).

        CLI: ``orca get --what <property> [--element <ref>] [--worktree <selector>] [--json]``
        """
        return self._client._invoke("get", [], [("what", what), ("element", element), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def goto(
        self,
        *,
        url: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Navigate the active browser tab to a URL.

        CLI: ``orca goto --url <url> [--worktree <selector>] [--json]``
        """
        return self._client._invoke("goto", [], [("url", url), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def highlight(
        self,
        *,
        selector: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Highlight an element by selector.

        CLI: ``orca highlight --selector <ref> [--worktree <selector>] [--json]``
        """
        return self._client._invoke("highlight", [], [("selector", selector), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def hover(
        self,
        *,
        element: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Hover over a browser element by ref.

        CLI: ``orca hover --element <ref> [--worktree <selector>] [--json]``
        """
        return self._client._invoke("hover", [], [("element", element), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def inserttext(
        self,
        *,
        text: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Insert text without key events.

        CLI: ``orca inserttext --text <text> [--worktree <selector>] [--json]``
        """
        return self._client._invoke("inserttext", [], [("text", text), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def is_(
        self,
        *,
        what: Scalar,
        element: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Check element state (visible, enabled, checked).

        CLI: ``orca is --what <state> --element <ref> [--worktree <selector>] [--json]``
        """
        return self._client._invoke("is", [], [("what", what), ("element", element), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def keypress(
        self,
        *,
        key: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Press a key (Enter, Tab, Escape, ArrowDown, etc.).

        CLI: ``orca keypress --key <name> [--worktree <selector>] [--json]``
        """
        return self._client._invoke("keypress", [], [("key", key), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def network(
        self,
        *,
        limit: int | str | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Show captured network requests.

        CLI: ``orca network [--limit <n>] [--worktree <selector>] [--json]``
        """
        return self._client._invoke("network", [], [("limit", limit), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def open(
        self,
    ) -> Any:
        """Launch Orca and wait for the runtime to be reachable.

        CLI: ``orca open [--json]``

        Examples:
            orca open
            orca open --json
        """
        return self._client._invoke("open", [], [], json=True, remote=True)

    def open_url(
        self,
        *,
        url: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Open a URL on the paired client that hosts this terminal.

        CLI: ``orca open-url --url <url> [--worktree <selector>] [--json]``
        """
        return self._client._invoke("open-url", [], [("url", url), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def pdf(
        self,
        *,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Export the active browser tab as PDF.

        CLI: ``orca pdf [--worktree <selector>] [--json]``
        """
        return self._client._invoke("pdf", [], [("worktree", worktree), ("page", page)], json=True, remote=True)

    def reload(
        self,
        *,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Reload the active browser tab.

        CLI: ``orca reload [--worktree <selector>] [--json]``
        """
        return self._client._invoke("reload", [], [("worktree", worktree), ("page", page)], json=True, remote=True)

    def screenshot(
        self,
        *,
        format: Scalar | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Capture a viewport screenshot of the active browser tab.

        CLI: ``orca screenshot [--format <png|jpeg>] [--worktree <selector>] [--json]``
        """
        return self._client._invoke("screenshot", [], [("format", format), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def scroll(
        self,
        *,
        direction: Scalar,
        amount: int | str | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Scroll the browser viewport.

        CLI: ``orca scroll --direction <up|down> [--amount <pixels>] [--worktree <selector>] [--json]``
        """
        return self._client._invoke("scroll", [], [("direction", direction), ("amount", amount), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def scrollintoview(
        self,
        *,
        element: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Scroll element into view.

        CLI: ``orca scrollintoview --element <ref> [--worktree <selector>] [--json]``
        """
        return self._client._invoke("scrollintoview", [], [("element", element), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def search(
        self,
        query: Scalar | None = None,
        *,
        scope: Scalar | None = None,
        fresh: bool = False,
        limit: int | str | None = None,
        cursor: Scalar | None = None,
        agent: Scalar | Sequence[Scalar] | None = None,
        path: Scalar | Sequence[Scalar] | None = None,
        since: Scalar | None = None,
        sort: Scalar | None = None,
        debug: bool = False,
        index_status: bool = False,
    ) -> Any:
        """Search the full text of agent sessions indexed on the selected Orca host.

        CLI: ``orca search <query> [--scope conversation|all] [--fresh] [--limit <n>] [--cursor <c>] [--agent <id>] [--path <p>] [--since <iso>] [--sort relevance|newest] [--debug] [--json]``

        Notes:
            Searches one host: this machine, or the paired Orca server named by --environment / --pairing-code. There is no all-computers search.
            In an Orca SSH terminal, the forwarded CLI searches the controlling Orca runtime by default. Use --environment / --pairing-code to select a paired server; --path only filters results on the selected runtime.
            Quote a multi-word query, or pass it as --query "<text>"; unquoted words are read as command names.
            --scope conversation searches user and assistant turns only; --scope all (the default) also searches commands and tool output.
            --fresh waits up to five seconds for the host to reconcile its index before searching, then searches anyway.
            --agent and --path may be repeated. --path is a literal execution-host path and is not expanded or resolved against the current directory.
            --since takes an ISO 8601 timestamp with an offset, for example 2026-08-01T00:00:00Z.
            --limit is per page (default 20, maximum 100). Pass the printed cursor back with --cursor to read the next page.
            A cursor belongs to one query on one host. Change the query, the filters, or the host and the cursor stops being valid.
            Resume commands and source paths are printed only for a host on this machine; a paired server withholds them.
            --json prints the runtime response envelope with the search contract answer under `result`.

        Examples:
            orca search "strict mode violation getByRole"
            orca search resolveTerminalPath --agent claude --sort newest
            orca search "kernel panic" --path /Users/me/orca --since 2026-08-01T00:00:00Z --json
            orca search "kernel panic" --limit 50 --cursor eyJ2IjoxfQ
            orca search --index-status
            orca search "flaky test" --environment build-server
        """
        return self._client._invoke("search", [query], [("scope", scope), ("fresh", fresh), ("limit", limit), ("cursor", cursor), ("agent", agent), ("path", path), ("since", since), ("sort", sort), ("debug", debug), ("index-status", index_status)], json=True, remote=True)

    def select(
        self,
        *,
        element: Scalar,
        value: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Select a dropdown option by ref.

        CLI: ``orca select --element <ref> --value <value> [--worktree <selector>] [--json]``
        """
        return self._client._invoke("select", [], [("element", element), ("value", value), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def select_all(
        self,
        *,
        element: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Select all text in an input by ref.

        CLI: ``orca select-all --element <ref> [--worktree <selector>] [--json]``
        """
        return self._client._invoke("select-all", [], [("element", element), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def snapshot(
        self,
        *,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Capture an accessibility snapshot of the active browser tab.

        CLI: ``orca snapshot [--worktree <selector>] [--json]``
        """
        return self._client._invoke("snapshot", [], [("worktree", worktree), ("page", page)], json=True, remote=True)

    def status(
        self,
    ) -> Any:
        """Show app/runtime/graph readiness.

        CLI: ``orca status [--json]``

        Notes:
            caller.orcaSessionId is this agent's Orca session ID, as Orca resolved it, when the agent runs as an Orca session; otherwise caller is omitted.

        Examples:
            orca status
            orca status --json
        """
        return self._client._invoke("status", [], [], json=True, remote=True)

    def type(
        self,
        *,
        input: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Type text at the current browser focus.

        CLI: ``orca type --input <text> [--worktree <selector>] [--json]``
        """
        return self._client._invoke("type", [], [("input", input), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def uncheck(
        self,
        *,
        element: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Uncheck a checkbox/radio by ref.

        CLI: ``orca uncheck --element <ref> [--worktree <selector>] [--json]``
        """
        return self._client._invoke("uncheck", [], [("element", element), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def upload(
        self,
        *,
        element: Scalar,
        files: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Upload files to a file input element.

        CLI: ``orca upload --element <ref> --files <path,...> [--worktree <selector>] [--json]``
        """
        return self._client._invoke("upload", [], [("element", element), ("files", files), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def viewport(
        self,
        *,
        width: int | str,
        height: int | str,
        scale: int | str | None = None,
        mobile: bool = False,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Set browser viewport size.

        CLI: ``orca viewport --width <w> --height <h> [--scale <n>] [--mobile] [--worktree <selector>] [--json]``
        """
        return self._client._invoke("viewport", [], [("width", width), ("height", height), ("scale", scale), ("mobile", mobile), ("worktree", worktree), ("page", page)], json=True, remote=True)

    def wait(
        self,
        *,
        selector: Scalar | None = None,
        timeout: int | str | None = None,
        text: Scalar | None = None,
        url: Scalar | None = None,
        load: Scalar | None = None,
        fn: Scalar | None = None,
        state: Scalar | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Wait for element, text, URL, load state, JS condition, or timeout.

        CLI: ``orca wait [--selector <sel>] [--timeout <ms>] [--text <text>] [--url <pattern>] [--load <state>] [--fn <js>] [--state <hidden|visible>] [--worktree <selector>] [--json]``
        """
        return self._client._invoke("wait", [], [("selector", selector), ("timeout", timeout), ("text", text), ("url", url), ("load", load), ("fn", fn), ("state", state), ("worktree", worktree), ("page", page)], json=True, remote=True)

class AsyncAccountResource(_AsyncResource):
    """Commands under ``orca account``."""

    async def add(
        self,
        *,
        agent: Scalar | None = None,
        label: Scalar | None = None,
        integration: Scalar | None = None,
    ) -> Any:
        """Add a managed agent account by signing in on this Orca host.

        CLI: ``orca account add [--agent claude|codex|opencode|devin] [--label <name>] [--integration <id>] [--json]``

        Notes:
            Runs the agent login (`claude login` / `codex login`) in this terminal, then registers the account with the local Orca runtime.
            Codex uses device authorization so the browser can complete sign-in from a different machine.
            OpenCode 2 uses `opencode auth login --standalone` in private XDG directories. Devin uses `devin auth login --force-manual-token-flow`.
            Use --integration <id> to skip the OpenCode integration picker; --label names the saved OpenCode or Devin profile.
            OpenCode and Devin profiles apply to new explicit host agent launches. Direct SSH relay and Windows-hosted WSL selection are not supported; run the command on a headless Orca runtime on that host.
            Sign in with the account you want to add (e.g. use a private/incognito browser window for a second account).
            --agent defaults to claude. Requires the Orca runtime to be running on this machine.

        Examples:
            orca account add
            orca account add --agent codex
        """
        return await self._client._invoke("account add", [], [("agent", agent), ("label", label), ("integration", integration)], json=True, remote=True)

    async def list(
        self,
        *,
        agent: Scalar | None = None,
    ) -> Any:
        """List managed agent accounts on this Orca host.

        CLI: ``orca account list [--agent opencode|devin] [--json]``

        Notes:
            Lists the accounts on this machine. `--environment` / `--pairing-code` are rejected rather than ignored; run it on the host whose accounts you want to see.

        Examples:
            orca account list
        """
        return await self._client._invoke("account list", [], [("agent", agent)], json=True, remote=False)

    async def rm(
        self,
        *,
        agent: Scalar,
        account: Scalar,
    ) -> Any:
        """Remove a managed OpenCode or Devin profile and its private data.

        CLI: ``orca account rm --agent opencode|devin --account <id> [--json]``

        Notes:
            Deletes credentials and conversation data in the managed profile. Stop its running agents first. System credentials are never removed.
        """
        return await self._client._invoke("account rm", [], [("agent", agent), ("account", account)], json=True, remote=True)

    async def select(
        self,
        *,
        agent: Scalar,
        account: Scalar,
    ) -> Any:
        """Select an OpenCode or Devin profile for new agent launches.

        CLI: ``orca account select --agent opencode|devin --account <id|system> [--json]``
        """
        return await self._client._invoke("account select", [], [("agent", agent), ("account", account)], json=True, remote=True)

class AsyncAgentHooksResource(_AsyncResource):
    """Commands under ``orca agent hooks``."""

    async def off(
        self,
        *,
        page: Scalar | None = None,
    ) -> Any:
        """Disable Orca-managed agent status hooks and remove local hook entries.

        CLI: ``orca agent hooks off [--json]``

        Examples:
            orca agent hooks off
        """
        return await self._client._invoke("agent hooks off", [], [("page", page)], json=True, remote=True)

    async def on(
        self,
        *,
        page: Scalar | None = None,
    ) -> Any:
        """Enable Orca-managed agent status hooks.

        CLI: ``orca agent hooks on [--json]``

        Examples:
            orca agent hooks on
        """
        return await self._client._invoke("agent hooks on", [], [("page", page)], json=True, remote=True)

    async def prepare_codex(
        self,
        *,
        page: Scalar | None = None,
    ) -> Any:
        """Prepare a WSL pane's Orca-managed Codex home before a shell launch.

        CLI: ``orca agent hooks prepare-codex``
        """
        return await self._client._invoke("agent hooks prepare-codex", [], [("page", page)], json=True, remote=True)

    async def status(
        self,
        *,
        page: Scalar | None = None,
    ) -> Any:
        """Show whether Orca-managed agent status hooks are enabled.

        CLI: ``orca agent hooks status [--json]``

        Examples:
            orca agent hooks status
            orca agent hooks status --json
        """
        return await self._client._invoke("agent hooks status", [], [("page", page)], json=True, remote=True)

class AsyncAgentResource(_AsyncResource):
    """Commands under ``orca agent``."""

    @cached_property
    def hooks(self) -> AsyncAgentHooksResource:
        """``orca agent hooks`` commands."""
        return AsyncAgentHooksResource(self._client)

    async def launch(
        self,
        *,
        agent: Scalar,
        worktree: Scalar | None = None,
        prompt: Scalar | None = None,
        model: Scalar | None = None,
        effort: Scalar | None = None,
        surface: Scalar | None = None,
        focus: bool = False,
        retry_launch: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Start an agent in an existing workspace, as a chat or a terminal.

        CLI: ``orca agent launch --agent <id> [--worktree <selector>] [--prompt <text>] [--model <id>] [--effort <level>] [--surface chat|terminal] [--focus] [--retry-launch <operationId>] [--json]``

        Notes:
            Starts the agent the way a new agent tab does: as a chat when your Chat UI setting is on and the agent and host support it, otherwise as a terminal. The result says which (`outcome.kind`) and why (`receipt.detail`).
            --surface chat|terminal picks for this launch instead of your setting. --surface terminal always runs the agent CLI; --surface chat is refused when Orca can establish before starting anything that this agent cannot open as a chat there. If support cannot be checked, the launch can fall back to a terminal. If chat becomes unavailable after creating a workspace, Orca keeps the workspace, setup and default tabs, then opens a terminal; the receipt explains the fallback.
            --worktree defaults to the native folder workspace or worktree containing the current directory. For a new checkout with its agent, use `orca worktree create --agent`.
            --model takes a provider model id and --effort a reasoning effort for that model; --effort requires --model. They apply to either surface.
            The tab opens without switching focus; pass --focus to switch to it.
            If the launch reply is lost, re-issue the same command from the same directory on the same host with --retry-launch <operationId> from the error. Never retry as a fresh launch; older hosts require inspecting the workspace first.

        Examples:
            orca agent launch --agent codex --json
            orca agent launch --agent codex --model gpt-6-astra --effort high --prompt "Write the design doc" --json
            orca agent launch --agent claude --worktree path:/projects/myapp --focus
        """
        return await self._client._invoke("agent launch", [], [("agent", agent), ("worktree", worktree), ("prompt", prompt), ("model", model), ("effort", effort), ("surface", surface), ("focus", focus), ("retry-launch", retry_launch), ("page", page)], json=True, remote=True)

class AsyncArtifactsResource(_AsyncResource):
    """Commands under ``orca artifacts``."""

    async def delete(
        self,
        id: Scalar,
        *,
        api_url: Scalar | None = None,
    ) -> Any:
        """Delete an artifact owned by the signed-in Orca account.

        CLI: ``orca artifacts delete <id> [--api-url <url>] [--json]``
        """
        return await self._client._invoke("artifacts delete", [id], [("api-url", api_url)], json=True, remote=True)

    async def list(
        self,
        *,
        api_url: Scalar | None = None,
        cursor: Scalar | None = None,
    ) -> Any:
        """List artifacts owned by the signed-in Orca account.

        CLI: ``orca artifacts list [--cursor <cursor>] [--api-url <url>] [--json]``
        """
        return await self._client._invoke("artifacts list", [], [("api-url", api_url), ("cursor", cursor)], json=True, remote=True)

    async def share(
        self,
        file: Scalar,
        *,
        api_url: Scalar | None = None,
    ) -> Any:
        """Share an HTML or Markdown file with your Orca account.

        CLI: ``orca artifacts share <file> [--api-url <url>] [--json]``

        Examples:
            orca artifacts share ./report.html
            orca artifacts share ./notes.md --json
        """
        return await self._client._invoke("artifacts share", [file], [("api-url", api_url)], json=True, remote=True)

    async def unshare(
        self,
        file: Scalar,
        *,
        api_url: Scalar | None = None,
    ) -> Any:
        """Delete the artifact associated with a previously shared file.

        CLI: ``orca artifacts unshare <file> [--api-url <url>] [--json]``
        """
        return await self._client._invoke("artifacts unshare", [file], [("api-url", api_url)], json=True, remote=True)

    async def update(
        self,
        file: Scalar,
        *,
        api_url: Scalar | None = None,
    ) -> Any:
        """Update a file previously shared from this Orca profile.

        CLI: ``orca artifacts update <file> [--api-url <url>] [--json]``
        """
        return await self._client._invoke("artifacts update", [file], [("api-url", api_url)], json=True, remote=True)

class AsyncAutomationsResource(_AsyncResource):
    """Commands under ``orca automations``."""

    async def create(
        self,
        *,
        name: Scalar,
        prompt: Scalar,
        provider: Scalar,
        trigger: Scalar,
        extra_agent_args: Scalar | None = None,
        precheck: Scalar | None = None,
        precheck_timeout: int | str | None = None,
        repo: Scalar | None = None,
        workspace: Scalar | None = None,
        project: Scalar | None = None,
        host: Scalar | None = None,
        project_host_setup: Scalar | None = None,
        source_context: Scalar | None = None,
        workspace_mode: Scalar | None = None,
        base_branch: Scalar | None = None,
        schedule: Scalar | None = None,
        time: Scalar | None = None,
        day: Scalar | None = None,
        timezone: Scalar | None = None,
        enabled: bool = False,
        disabled: bool = False,
        missed_run_grace_minutes: int | str | None = None,
        reuse_session: bool = False,
        fresh_session: bool = False,
    ) -> Any:
        """Create a scheduled Orca automation.

        CLI: ``orca automations create --name <name> --trigger <preset|cron|rrule> --prompt <text> --provider <agent> [--precheck <command>] [--repo <selector>|--workspace <selector>|--project <id-or-name> [--host <host>]|--project-host-setup <id>] [--json]``

        Notes:
            Trigger accepts hourly, daily, weekdays, weekly, a 5-field cron expression, or an RRULE string.
            When --repo is omitted, the CLI uses the enclosing Orca worktree when one can be resolved from cwd.
            Use --project, or --project-host-setup, to run on a specific project host setup. --project takes the project id or the display name from `orca project list`, and --host is only needed when the project is set up on more than one host.
            --host takes local, ssh:<target-id>, runtime:<environment-id>, or the bare host name `orca host list` prints for any of them.
            Use --source-context with a JSON TaskSourceContext when task/provider data should come from a specific host/account; pass null on edit to clear it.
            Use --workspace to run in an existing worktree; otherwise the automation creates a new worktree per run.
            Use --precheck to run a bounded command before scheduled runs; exit code 0 continues, anything else records a skipped run.
            Use --reuse-session only with existing-workspace automations to submit later runs to the previous live automation session when it is still available. Use --fresh-session to disable reuse.
            Use --extra-agent-args="--model opus --effort high" to add arguments after the host's default agent Arguments on each fresh run. Only model, effort, and a few safe options are accepted (Claude, Codex, CodeBuddy, Cursor, Grok, OMP); extras cannot be combined with --reuse-session. On edit, --extra-agent-args= clears them.

        Examples:
            orca automations create --name "Daily review" --trigger daily --prompt "Review open changes" --provider codex
            orca automations create --name "Weekday triage" --trigger "0 9 * * 1-5" --prompt "Triage issues" --provider claude --repo my-repo
            orca automations create --name "PR review" --trigger hourly --precheck "gh pr list --json number -q .[0].number" --prompt "Review requested PRs" --provider codex
            orca automations create --name "Docs pass" --trigger daily --prompt "Tidy the docs" --provider claude --extra-agent-args="--model opus --effort high --add-dir docs"
        """
        return await self._client._invoke("automations create", [], [("name", name), ("prompt", prompt), ("provider", provider), ("extra-agent-args", extra_agent_args), ("precheck", precheck), ("precheck-timeout", precheck_timeout), ("repo", repo), ("workspace", workspace), ("project", project), ("host", host), ("project-host-setup", project_host_setup), ("source-context", source_context), ("workspace-mode", workspace_mode), ("base-branch", base_branch), ("trigger", trigger), ("schedule", schedule), ("time", time), ("day", day), ("timezone", timezone), ("enabled", enabled), ("disabled", disabled), ("missed-run-grace-minutes", missed_run_grace_minutes), ("reuse-session", reuse_session), ("fresh-session", fresh_session)], json=True, remote=True)

    async def edit(
        self,
        id: Scalar,
        *,
        name: Scalar | None = None,
        prompt: Scalar | None = None,
        provider: Scalar | None = None,
        extra_agent_args: Scalar | None = None,
        precheck: Scalar | None = None,
        precheck_timeout: int | str | None = None,
        repo: Scalar | None = None,
        workspace: Scalar | None = None,
        project: Scalar | None = None,
        host: Scalar | None = None,
        project_host_setup: Scalar | None = None,
        source_context: Scalar | None = None,
        workspace_mode: Scalar | None = None,
        base_branch: Scalar | None = None,
        trigger: Scalar | None = None,
        schedule: Scalar | None = None,
        time: Scalar | None = None,
        day: Scalar | None = None,
        timezone: Scalar | None = None,
        enabled: bool = False,
        disabled: bool = False,
        missed_run_grace_minutes: int | str | None = None,
        reuse_session: bool = False,
        fresh_session: bool = False,
    ) -> Any:
        """Edit an Orca automation.

        CLI: ``orca automations edit <id> [--name <name>] [--trigger <preset|cron|rrule>] [--json]``

        Examples:
            orca automations edit 2f9e... --disabled
            orca automations edit --id 2f9e... --trigger "30 * * * *" --json
            orca automations edit 2f9e... --extra-agent-args=
        """
        return await self._client._invoke("automations edit", [id], [("name", name), ("prompt", prompt), ("provider", provider), ("extra-agent-args", extra_agent_args), ("precheck", precheck), ("precheck-timeout", precheck_timeout), ("repo", repo), ("workspace", workspace), ("project", project), ("host", host), ("project-host-setup", project_host_setup), ("source-context", source_context), ("workspace-mode", workspace_mode), ("base-branch", base_branch), ("trigger", trigger), ("schedule", schedule), ("time", time), ("day", day), ("timezone", timezone), ("enabled", enabled), ("disabled", disabled), ("missed-run-grace-minutes", missed_run_grace_minutes), ("reuse-session", reuse_session), ("fresh-session", fresh_session)], json=True, remote=True)

    async def list(
        self,
    ) -> Any:
        """List scheduled Orca automations.

        CLI: ``orca automations list [--json]``

        Examples:
            orca automations list
            orca automations list --json
        """
        return await self._client._invoke("automations list", [], [], json=True, remote=True)

    async def remove(
        self,
        id: Scalar,
    ) -> Any:
        """Remove an Orca automation and its run history.

        CLI: ``orca automations remove <id> [--json]``

        Examples:
            orca automations remove 2f9e...
            orca automations remove --id 2f9e... --json
        """
        return await self._client._invoke("automations remove", [id], [], json=True, remote=True)

    async def run(
        self,
        id: Scalar,
    ) -> Any:
        """Run an Orca automation now.

        CLI: ``orca automations run <id> [--json]``

        Notes:
            Use the full automation UUID from orca automations list; shortened prefixes are not accepted.
            A queued or dispatching run has been accepted but may not have a workspace or terminal yet. Use orca automations runs --id <automation-id> to follow its progress.

        Examples:
            orca automations run 497bafa9-5a97-4f85-9e48-2b211b8f31fa
            orca automations run --id 497bafa9-5a97-4f85-9e48-2b211b8f31fa --json
        """
        return await self._client._invoke("automations run", [id], [], json=True, remote=True)

    async def runs(
        self,
        *,
        id: Scalar | None = None,
        limit: int | str | None = None,
        cursor: Scalar | None = None,
    ) -> Any:
        """List automation run history.

        CLI: ``orca automations runs [--id <automation-id>] [--limit <n>] [--cursor <cursor>] [--json]``

        Notes:
            Without --limit or --cursor, reads the whole history in pages, so a large history from a paired server still fits in its replies.
            With --limit or --cursor, prints one page (newest first, at most 100 runs) and its nextCursor; pass that as --cursor for the next page.

        Examples:
            orca automations runs
            orca automations runs --id 2f9e... --json
            orca automations runs --limit 20 --json
        """
        return await self._client._invoke("automations runs", [], [("id", id), ("limit", limit), ("cursor", cursor)], json=True, remote=True)

    async def show(
        self,
        id: Scalar,
    ) -> Any:
        """Show one Orca automation.

        CLI: ``orca automations show <id> [--json]``

        Examples:
            orca automations show 2f9e...
            orca automations show --id 2f9e... --json
        """
        return await self._client._invoke("automations show", [id], [], json=True, remote=True)

class AsyncBrowserIdentityResource(_AsyncResource):
    """Commands under ``orca browser identity``."""

    async def get(
        self,
        *,
        page: Scalar | None = None,
    ) -> Any:
        """Show the browser identity configured on this Orca host.

        CLI: ``orca browser identity get [--json]``
        """
        return await self._client._invoke("browser identity get", [], [("page", page)], json=True, remote=True)

    async def set(
        self,
        *,
        mode: Scalar,
        reset: bool = False,
        page: Scalar | None = None,
    ) -> Any:
        """Choose the browser identity for every page on this Orca host.

        CLI: ``orca browser identity set --mode <clean|native> [--reset] [--json]``
        """
        return await self._client._invoke("browser identity set", [], [("mode", mode), ("reset", reset), ("page", page)], json=True, remote=True)

class AsyncBrowserResource(_AsyncResource):
    """Commands under ``orca browser``."""

    @cached_property
    def identity(self) -> AsyncBrowserIdentityResource:
        """``orca browser identity`` commands."""
        return AsyncBrowserIdentityResource(self._client)

class AsyncCaptureResource(_AsyncResource):
    """Commands under ``orca capture``."""

    async def start(
        self,
        *,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Start capturing console and network events.

        CLI: ``orca capture start [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("capture start", [], [("worktree", worktree), ("page", page)], json=True, remote=True)

    async def stop(
        self,
        *,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Stop capturing console and network events.

        CLI: ``orca capture stop [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("capture stop", [], [("worktree", worktree), ("page", page)], json=True, remote=True)

class AsyncClipboardResource(_AsyncResource):
    """Commands under ``orca clipboard``."""

    async def read(
        self,
        *,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Read clipboard contents.

        CLI: ``orca clipboard read [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("clipboard read", [], [("worktree", worktree), ("page", page)], json=True, remote=True)

    async def write(
        self,
        *,
        text: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Write text to clipboard.

        CLI: ``orca clipboard write --text <text> [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("clipboard write", [], [("text", text), ("worktree", worktree), ("page", page)], json=True, remote=True)

class AsyncComputerResource(_AsyncResource):
    """Commands under ``orca computer``."""

    async def capabilities(
        self,
    ) -> Any:
        """Show computer-use provider capabilities.

        CLI: ``orca computer capabilities [--json]``
        """
        return await self._client._invoke("computer capabilities", [], [], json=True, remote=True)

    async def click(
        self,
        *,
        app: Scalar,
        worktree: Scalar | None = None,
        session: Scalar | None = None,
        window_id: Scalar | None = None,
        window_index: int | str | None = None,
        restore_window: bool = False,
        no_screenshot: bool = False,
        element_index: int | str | None = None,
        x: int | str | None = None,
        y: int | str | None = None,
        click_count: int | str | None = None,
        mouse_button: Scalar | None = None,
        modifiers: Scalar | None = None,
    ) -> Any:
        """Click an app element or window coordinate, optionally with modifiers.

        CLI: ``orca computer click --app <app> (--element-index <n> | --x <x> --y <y>) [--window-id <id> | --window-index <n>] [--click-count <n>] [--mouse-button <left|right|middle>] [--modifiers <modifier-chord>] [--restore-window] [--no-screenshot] [--json]``
        """
        return await self._client._invoke("computer click", [], [("worktree", worktree), ("session", session), ("app", app), ("window-id", window_id), ("window-index", window_index), ("restore-window", restore_window), ("no-screenshot", no_screenshot), ("element-index", element_index), ("x", x), ("y", y), ("click-count", click_count), ("mouse-button", mouse_button), ("modifiers", modifiers)], json=True, remote=True)

    async def drag(
        self,
        *,
        app: Scalar,
        worktree: Scalar | None = None,
        session: Scalar | None = None,
        window_id: Scalar | None = None,
        window_index: int | str | None = None,
        restore_window: bool = False,
        no_screenshot: bool = False,
        from_element_index: int | str | None = None,
        to_element_index: int | str | None = None,
        from_x: int | str | None = None,
        from_y: int | str | None = None,
        to_x: int | str | None = None,
        to_y: int | str | None = None,
    ) -> Any:
        """Drag between app elements or window coordinates.

        CLI: ``orca computer drag --app <app> (--from-element-index <n> --to-element-index <n> | --from-x <x> --from-y <y> --to-x <x> --to-y <y>) [--window-id <id> | --window-index <n>] [--restore-window] [--no-screenshot] [--json]``
        """
        return await self._client._invoke("computer drag", [], [("worktree", worktree), ("session", session), ("app", app), ("window-id", window_id), ("window-index", window_index), ("restore-window", restore_window), ("no-screenshot", no_screenshot), ("from-element-index", from_element_index), ("to-element-index", to_element_index), ("from-x", from_x), ("from-y", from_y), ("to-x", to_x), ("to-y", to_y)], json=True, remote=True)

    async def get_app_state(
        self,
        *,
        app: Scalar,
        worktree: Scalar | None = None,
        session: Scalar | None = None,
        window_id: Scalar | None = None,
        window_index: int | str | None = None,
        restore_window: bool = False,
        no_screenshot: bool = False,
    ) -> Any:
        """Capture a compact accessibility snapshot of an app.

        CLI: ``orca computer get-app-state --app <name|bundle|pid:N> [--window-id <id> | --window-index <n>] [--worktree <selector> | --session <id>] [--restore-window] [--no-screenshot] [--json]``
        """
        return await self._client._invoke("computer get-app-state", [], [("worktree", worktree), ("session", session), ("app", app), ("window-id", window_id), ("window-index", window_index), ("restore-window", restore_window), ("no-screenshot", no_screenshot)], json=True, remote=True)

    async def hotkey(
        self,
        *,
        app: Scalar,
        key: Scalar,
        worktree: Scalar | None = None,
        session: Scalar | None = None,
        window_id: Scalar | None = None,
        window_index: int | str | None = None,
        restore_window: bool = False,
        no_screenshot: bool = False,
    ) -> Any:
        """Press a platform-aware key combination.

        CLI: ``orca computer hotkey --app <app> --key <key-combo> [--window-id <id> | --window-index <n>] [--restore-window] [--no-screenshot] [--json]``
        """
        return await self._client._invoke("computer hotkey", [], [("worktree", worktree), ("session", session), ("app", app), ("window-id", window_id), ("window-index", window_index), ("restore-window", restore_window), ("no-screenshot", no_screenshot), ("key", key)], json=True, remote=True)

    async def list_apps(
        self,
    ) -> Any:
        """List running apps available to computer-use.

        CLI: ``orca computer list-apps [--json]``
        """
        return await self._client._invoke("computer list-apps", [], [], json=True, remote=True)

    async def list_windows(
        self,
        *,
        app: Scalar,
    ) -> Any:
        """List windows for an app available to computer-use.

        CLI: ``orca computer list-windows --app <name|bundle|pid:N> [--json]``
        """
        return await self._client._invoke("computer list-windows", [], [("app", app)], json=True, remote=True)

    async def paste_text(
        self,
        *,
        app: Scalar,
        worktree: Scalar | None = None,
        session: Scalar | None = None,
        window_id: Scalar | None = None,
        window_index: int | str | None = None,
        restore_window: bool = False,
        no_screenshot: bool = False,
        text: Scalar | None = None,
        text_stdin: bool = False,
        stdin: str | bytes | None = None,
    ) -> Any:
        """Paste exact text at the current app focus.

        CLI: ``orca computer paste-text --app <app> (--text <text> | --text-stdin) [--window-id <id> | --window-index <n>] [--restore-window] [--no-screenshot] [--json]``
        """
        return await self._client._invoke("computer paste-text", [], [("worktree", worktree), ("session", session), ("app", app), ("window-id", window_id), ("window-index", window_index), ("restore-window", restore_window), ("no-screenshot", no_screenshot), ("text", text), ("text-stdin", text_stdin)], json=True, remote=True, stdin=stdin)

    async def perform_secondary_action(
        self,
        *,
        app: Scalar,
        element_index: int | str,
        action: Scalar,
        worktree: Scalar | None = None,
        session: Scalar | None = None,
        window_id: Scalar | None = None,
        window_index: int | str | None = None,
        restore_window: bool = False,
        no_screenshot: bool = False,
    ) -> Any:
        """Perform an advertised secondary accessibility action.

        CLI: ``orca computer perform-secondary-action --app <app> --element-index <n> --action <name> [--window-id <id> | --window-index <n>] [--restore-window] [--no-screenshot] [--json]``
        """
        return await self._client._invoke("computer perform-secondary-action", [], [("worktree", worktree), ("session", session), ("app", app), ("window-id", window_id), ("window-index", window_index), ("restore-window", restore_window), ("no-screenshot", no_screenshot), ("element-index", element_index), ("action", action)], json=True, remote=True)

    async def permissions(
        self,
        *,
        id: Scalar | None = None,
    ) -> Any:
        """Open computer-use permission setup.

        CLI: ``orca computer permissions [--id <accessibility|screenshots>] [--json]``
        """
        return await self._client._invoke("computer permissions", [], [("id", id)], json=True, remote=True)

    async def press_key(
        self,
        *,
        app: Scalar,
        key: Scalar,
        worktree: Scalar | None = None,
        session: Scalar | None = None,
        window_id: Scalar | None = None,
        window_index: int | str | None = None,
        restore_window: bool = False,
        no_screenshot: bool = False,
    ) -> Any:
        """Press a single key such as Return or Escape.

        CLI: ``orca computer press-key --app <app> --key <key> [--window-id <id> | --window-index <n>] [--restore-window] [--no-screenshot] [--json]``
        """
        return await self._client._invoke("computer press-key", [], [("worktree", worktree), ("session", session), ("app", app), ("window-id", window_id), ("window-index", window_index), ("restore-window", restore_window), ("no-screenshot", no_screenshot), ("key", key)], json=True, remote=True)

    async def scroll(
        self,
        *,
        app: Scalar,
        direction: Scalar,
        worktree: Scalar | None = None,
        session: Scalar | None = None,
        window_id: Scalar | None = None,
        window_index: int | str | None = None,
        restore_window: bool = False,
        no_screenshot: bool = False,
        element_index: int | str | None = None,
        x: int | str | None = None,
        y: int | str | None = None,
        pages: int | str | None = None,
    ) -> Any:
        """Scroll an app element or window coordinate.

        CLI: ``orca computer scroll --app <app> (--element-index <n> | --x <x> --y <y>) --direction <up|down|left|right> [--window-id <id> | --window-index <n>] [--pages <n>] [--restore-window] [--no-screenshot] [--json]``
        """
        return await self._client._invoke("computer scroll", [], [("worktree", worktree), ("session", session), ("app", app), ("window-id", window_id), ("window-index", window_index), ("restore-window", restore_window), ("no-screenshot", no_screenshot), ("element-index", element_index), ("x", x), ("y", y), ("direction", direction), ("pages", pages)], json=True, remote=True)

    async def set_value(
        self,
        *,
        app: Scalar,
        element_index: int | str,
        worktree: Scalar | None = None,
        session: Scalar | None = None,
        window_id: Scalar | None = None,
        window_index: int | str | None = None,
        restore_window: bool = False,
        no_screenshot: bool = False,
        value: Scalar | None = None,
        value_stdin: bool = False,
        stdin: str | bytes | None = None,
    ) -> Any:
        """Set the value of a settable app element.

        CLI: ``orca computer set-value --app <app> --element-index <n> (--value <text> | --value-stdin) [--window-id <id> | --window-index <n>] [--restore-window] [--no-screenshot] [--json]``
        """
        return await self._client._invoke("computer set-value", [], [("worktree", worktree), ("session", session), ("app", app), ("window-id", window_id), ("window-index", window_index), ("restore-window", restore_window), ("no-screenshot", no_screenshot), ("element-index", element_index), ("value", value), ("value-stdin", value_stdin)], json=True, remote=True, stdin=stdin)

    async def type_text(
        self,
        *,
        app: Scalar,
        worktree: Scalar | None = None,
        session: Scalar | None = None,
        window_id: Scalar | None = None,
        window_index: int | str | None = None,
        restore_window: bool = False,
        no_screenshot: bool = False,
        text: Scalar | None = None,
        text_stdin: bool = False,
        stdin: str | bytes | None = None,
    ) -> Any:
        """Type literal text at the current app focus.

        CLI: ``orca computer type-text --app <app> (--text <text> | --text-stdin) [--window-id <id> | --window-index <n>] [--restore-window] [--no-screenshot] [--json]``
        """
        return await self._client._invoke("computer type-text", [], [("worktree", worktree), ("session", session), ("app", app), ("window-id", window_id), ("window-index", window_index), ("restore-window", restore_window), ("no-screenshot", no_screenshot), ("text", text), ("text-stdin", text_stdin)], json=True, remote=True, stdin=stdin)

class AsyncCookieResource(_AsyncResource):
    """Commands under ``orca cookie``."""

    async def delete(
        self,
        *,
        name: int | str,
        domain: Scalar | None = None,
        url: Scalar | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Delete a cookie by name.

        CLI: ``orca cookie delete --name <n> [--domain <d>] [--url <u>] [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("cookie delete", [], [("name", name), ("domain", domain), ("url", url), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def get(
        self,
        *,
        url: Scalar | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Get cookies for the active tab (optionally filter by URL).

        CLI: ``orca cookie get [--url <url>] [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("cookie get", [], [("url", url), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def set(
        self,
        *,
        name: int | str,
        value: Scalar,
        domain: Scalar | None = None,
        path: Scalar | None = None,
        secure: bool = False,
        httpOnly: bool = False,
        sameSite: Scalar | None = None,
        expires: int | str | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Set a cookie.

        CLI: ``orca cookie set --name <n> --value <v> [--domain <d>] [--path <p>] [--secure] [--httpOnly] [--sameSite <s>] [--expires <epoch>] [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("cookie set", [], [("name", name), ("value", value), ("domain", domain), ("path", path), ("secure", secure), ("httpOnly", httpOnly), ("sameSite", sameSite), ("expires", expires), ("worktree", worktree), ("page", page)], json=True, remote=True)

class AsyncDiagnosticsResource(_AsyncResource):
    """Commands under ``orca diagnostics``."""

    async def memory(
        self,
    ) -> Any:
        """Collect a memory snapshot for Orca and managed terminals.

        CLI: ``orca diagnostics memory [--json]``

        Notes:
            Runs the same host process sweep used by the Resource Usage popover, so call it when you need a point-in-time diagnostic rather than a cheap heartbeat.

        Examples:
            orca diagnostics memory --json
        """
        return await self._client._invoke("diagnostics memory", [], [], json=True, remote=True)

class AsyncDialogResource(_AsyncResource):
    """Commands under ``orca dialog``."""

    async def accept(
        self,
        *,
        text: Scalar | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Accept a browser dialog.

        CLI: ``orca dialog accept [--text <text>] [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("dialog accept", [], [("text", text), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def dismiss(
        self,
        *,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Dismiss a browser dialog.

        CLI: ``orca dialog dismiss [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("dialog dismiss", [], [("worktree", worktree), ("page", page)], json=True, remote=True)

class AsyncEmulatorResource(_AsyncResource):
    """Commands under ``orca emulator``."""

    async def attach(
        self,
        device: Scalar | None = None,
        *,
        worktree: Scalar | None = None,
        focus: bool = False,
    ) -> Any:
        """Attach/start helper for a device and make it active for the worktree.

        CLI: ``orca emulator attach [device] [--worktree <selector>] [--focus] [--json]``
        """
        return await self._client._invoke("emulator attach", [device], [("worktree", worktree), ("focus", focus)], json=True, remote=True)

    async def ax(
        self,
        *,
        device: Scalar | None = None,
        emulator: Scalar | None = None,
        worktree: Scalar | None = None,
    ) -> Any:
        """Dump the accessibility tree (Android uiautomator; iOS serve-sim AX, frames 0..1).

        CLI: ``orca emulator ax [--device <id>] [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("emulator ax", [], [("device", device), ("emulator", emulator), ("worktree", worktree)], json=True, remote=True)

    async def button(
        self,
        name: Scalar,
        *,
        device: Scalar | None = None,
        emulator: Scalar | None = None,
        worktree: Scalar | None = None,
    ) -> Any:
        """Hardware button (home, side_button, etc.).

        CLI: ``orca emulator button <name> [--device <id>] [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("emulator button", [name], [("device", device), ("emulator", emulator), ("worktree", worktree)], json=True, remote=True)

    async def devices(
        self,
        *,
        worktree: Scalar | None = None,
    ) -> Any:
        """List all emulator devices/AVDs across iOS and Android.

        CLI: ``orca emulator devices [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("emulator devices", [], [("worktree", worktree)], json=True, remote=True)

    async def exec(
        self,
        *,
        command: Scalar,
        device: Scalar | None = None,
        emulator: Scalar | None = None,
        worktree: Scalar | None = None,
    ) -> Any:
        """Raw passthrough (e.g. orca emulator exec --command "tap 0.5 0.7" or "ca-debug blended on").

        CLI: ``orca emulator exec --command <cmd> [--device <id>] [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("emulator exec", [], [("command", command), ("device", device), ("emulator", emulator), ("worktree", worktree)], json=True, remote=True)

    async def gesture(
        self,
        points: Scalar,
        *,
        device: Scalar | None = None,
        emulator: Scalar | None = None,
        worktree: Scalar | None = None,
    ) -> Any:
        """Send a multi-point gesture sequence.

        CLI: ``orca emulator gesture '<json>' [--device <id>] [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("emulator gesture", [points], [("device", device), ("emulator", emulator), ("worktree", worktree)], json=True, remote=True)

    async def install(
        self,
        path: Scalar,
        *,
        device: Scalar | None = None,
        emulator: Scalar | None = None,
        worktree: Scalar | None = None,
        reinstall: bool = False,
    ) -> Any:
        """Install an APK onto the target Android device.

        CLI: ``orca emulator install <apkPath> [--reinstall] [--device <id>] [--json]``
        """
        return await self._client._invoke("emulator install", [path], [("device", device), ("emulator", emulator), ("worktree", worktree), ("reinstall", reinstall)], json=True, remote=True)

    async def kill(
        self,
        *,
        device: Scalar | None = None,
        emulator: Scalar | None = None,
        worktree: Scalar | None = None,
    ) -> Any:
        """Stop helper for device.

        CLI: ``orca emulator kill [--device <id>] [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("emulator kill", [], [("device", device), ("emulator", emulator), ("worktree", worktree)], json=True, remote=True)

    async def launch(
        self,
        package: Scalar,
        *,
        device: Scalar | None = None,
        emulator: Scalar | None = None,
        worktree: Scalar | None = None,
        activity: Scalar | None = None,
    ) -> Any:
        """Launch an Android app by package (and optional activity).

        CLI: ``orca emulator launch <package> [--activity <name>] [--device <id>] [--json]``
        """
        return await self._client._invoke("emulator launch", [package], [("device", device), ("emulator", emulator), ("worktree", worktree), ("activity", activity)], json=True, remote=True)

    async def list(
        self,
        *,
        worktree: Scalar | None = None,
    ) -> Any:
        """List available/running emulators (Orca-managed + raw serve-sim).

        CLI: ``orca emulator list [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("emulator list", [], [("worktree", worktree)], json=True, remote=True)

    async def logcat(
        self,
        *,
        device: Scalar | None = None,
        emulator: Scalar | None = None,
        worktree: Scalar | None = None,
        lines: int | str | None = None,
    ) -> Any:
        """Capture a one-shot logcat dump from the Android device.

        CLI: ``orca emulator logcat [--lines <n>] [--device <id>] [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("emulator logcat", [], [("device", device), ("emulator", emulator), ("worktree", worktree), ("lines", lines)], json=True, remote=True)

    async def permissions(
        self,
        op: Scalar,
        package: Scalar | None = None,
        permission: Scalar | None = None,
        *,
        device: Scalar | None = None,
        emulator: Scalar | None = None,
        worktree: Scalar | None = None,
    ) -> Any:
        """Grant/revoke an Android runtime permission, or reset all runtime grants.

        CLI: ``orca emulator permissions <grant|revoke> <package> <permission> [--device <id>] [--json]``
        """
        return await self._client._invoke("emulator permissions", [op, package, permission], [("device", device), ("emulator", emulator), ("worktree", worktree)], json=True, remote=True)

    async def rotate(
        self,
        orientation: Scalar,
        *,
        device: Scalar | None = None,
        emulator: Scalar | None = None,
        worktree: Scalar | None = None,
    ) -> Any:
        """Rotate device.

        CLI: ``orca emulator rotate <orientation> [--device <id>] [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("emulator rotate", [orientation], [("device", device), ("emulator", emulator), ("worktree", worktree)], json=True, remote=True)

    async def shutdown(
        self,
        *,
        device: Scalar | None = None,
        emulator: Scalar | None = None,
        worktree: Scalar | None = None,
    ) -> Any:
        """Stop helper and shut down the simulator device.

        CLI: ``orca emulator shutdown [--device <id>] [--emulator <id>] [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("emulator shutdown", [], [("device", device), ("emulator", emulator), ("worktree", worktree)], json=True, remote=True)

    async def tap(
        self,
        x: Scalar,
        y: Scalar,
        *,
        device: Scalar | None = None,
        emulator: Scalar | None = None,
        worktree: Scalar | None = None,
    ) -> Any:
        """Tap at normalized 0..1 coords (preferred for single taps).

        CLI: ``orca emulator tap <x> <y> [--device <id>] [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("emulator tap", [x, y], [("device", device), ("emulator", emulator), ("worktree", worktree)], json=True, remote=True)

    async def type(
        self,
        text: Scalar,
        *,
        device: Scalar | None = None,
        emulator: Scalar | None = None,
        worktree: Scalar | None = None,
    ) -> Any:
        """Type text (US ASCII only).

        CLI: ``orca emulator type <text> [--device <id>] [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("emulator type", [text], [("device", device), ("emulator", emulator), ("worktree", worktree)], json=True, remote=True)

class AsyncEnvironmentResource(_AsyncResource):
    """Commands under ``orca environment``."""

    async def add(
        self,
        *,
        pairing_code: Scalar,
        name: Scalar,
        page: Scalar | None = None,
    ) -> Any:
        """Save a remote Orca runtime environment from a pairing code.

        CLI: ``orca environment add --name <name> --pairing-code <code> [--json]``

        Examples:
            orca environment add --name work-laptop --pairing-code orca://pair?code=...
        """
        return await self._client._invoke("environment add", [], [("pairing-code", pairing_code), ("name", name), ("page", page)], json=True, remote=False)

    async def cancel_stop(
        self,
        *,
        environment: Scalar,
        page: Scalar | None = None,
    ) -> Any:
        """Withdraw a managed Orca server stop that orcad has not acted on yet.

        CLI: ``orca environment cancel-stop --environment <selector> [--json]``

        Notes:
            --environment names a managed Orca server this machine deployed over SSH (see `orca environment list`); it is a selector here, not a routing flag.
            Runs on this machine’s Orca desktop app, the same action as Settings > Orca on your SSH hosts. A runtime without the SSH registry (headless `orca serve`) refuses it.
        """
        return await self._client._invoke("environment cancel-stop", [], [("environment", environment), ("page", page)], json=True, remote=False)

    async def forget(
        self,
        *,
        environment: Scalar,
        yes: bool = False,
        page: Scalar | None = None,
    ) -> Any:
        """Unlink a managed Orca server whose SSH host is gone, without stopping it.

        CLI: ``orca environment forget --environment <selector> --yes [--json]``

        Notes:
            Removes the server from this machine without contacting its host, so the SSH host can then be removed. Use it when the host was deleted or can never be reached again. Requires --yes.
            Nothing on the host is stopped: if it comes back, orcad may still be running there, and connecting to it again relinks it.
            --environment names a managed Orca server this machine deployed over SSH (see `orca environment list`); it is a selector here, not a routing flag.
            Runs on this machine’s Orca desktop app, the same action as Settings > Orca on your SSH hosts. A runtime without the SSH registry (headless `orca serve`) refuses it.

        Examples:
            orca environment forget --environment build-box --yes
        """
        return await self._client._invoke("environment forget", [], [("environment", environment), ("yes", yes), ("page", page)], json=True, remote=False)

    async def list(
        self,
        *,
        page: Scalar | None = None,
    ) -> Any:
        """List saved Orca runtime environments.

        CLI: ``orca environment list [--json]``

        Notes:
            Answers from this machine’s pairing store. --environment and --pairing-code are rejected rather than ignored, because there is no other host that could answer.
        """
        return await self._client._invoke("environment list", [], [("page", page)], json=True, remote=False)

    async def recover(
        self,
        *,
        environment: Scalar,
        accept_changed_state: bool = False,
        yes: bool = False,
        page: Scalar | None = None,
    ) -> Any:
        """Finish or undo a managed Orca server’s interrupted update, rollback or stop.

        CLI: ``orca environment recover --environment <selector> [--accept-changed-state --yes] [--json]``

        Notes:
            When a rejected build changed profile state, recover refuses rather than restart the previous build over it. --accept-changed-state --yes restores the prelaunch snapshot instead, the same as Restore in Settings > Orca on your SSH hosts; what the rejected build changed is discarded.
            --environment names a managed Orca server this machine deployed over SSH (see `orca environment list`); it is a selector here, not a routing flag.
            Runs on this machine’s Orca desktop app, the same action as Settings > Orca on your SSH hosts. A runtime without the SSH registry (headless `orca serve`) refuses it.

        Examples:
            orca environment recover --environment build-box
            orca environment recover --environment build-box --accept-changed-state --yes
        """
        return await self._client._invoke("environment recover", [], [("environment", environment), ("accept-changed-state", accept_changed_state), ("yes", yes), ("page", page)], json=True, remote=False)

    async def rm(
        self,
        *,
        environment: Scalar,
        page: Scalar | None = None,
    ) -> Any:
        """Remove one saved Orca runtime environment.

        CLI: ``orca environment rm --environment <selector> [--json]``
        """
        return await self._client._invoke("environment rm", [], [("environment", environment), ("page", page)], json=True, remote=False)

    async def rollback(
        self,
        *,
        environment: Scalar,
        page: Scalar | None = None,
    ) -> Any:
        """Roll a managed Orca server back to its previous version.

        CLI: ``orca environment rollback --environment <selector> [--json]``

        Notes:
            --environment names a managed Orca server this machine deployed over SSH (see `orca environment list`); it is a selector here, not a routing flag.
            Runs on this machine’s Orca desktop app, the same action as Settings > Orca on your SSH hosts. A runtime without the SSH registry (headless `orca serve`) refuses it.
        """
        return await self._client._invoke("environment rollback", [], [("environment", environment), ("page", page)], json=True, remote=False)

    async def show(
        self,
        *,
        environment: Scalar,
        page: Scalar | None = None,
    ) -> Any:
        """Show one saved Orca runtime environment.

        CLI: ``orca environment show --environment <selector> [--json]``
        """
        return await self._client._invoke("environment show", [], [("environment", environment), ("page", page)], json=True, remote=False)

    async def status(
        self,
        *,
        environment: Scalar,
        page: Scalar | None = None,
    ) -> Any:
        """Show a managed Orca server’s active version, terminals and pending work.

        CLI: ``orca environment status --environment <selector> [--json]``

        Notes:
            --environment names a managed Orca server this machine deployed over SSH (see `orca environment list`); it is a selector here, not a routing flag.
            Runs on this machine’s Orca desktop app, the same action as Settings > Orca on your SSH hosts. A runtime without the SSH registry (headless `orca serve`) refuses it.

        Examples:
            orca environment status --environment build-box
        """
        return await self._client._invoke("environment status", [], [("environment", environment), ("page", page)], json=True, remote=False)

    async def stop(
        self,
        *,
        environment: Scalar,
        yes: bool = False,
        page: Scalar | None = None,
    ) -> Any:
        """Stop a managed Orca server and unlink it from this machine (decommission).

        CLI: ``orca environment stop --environment <selector> --yes [--json]``

        Notes:
            Stops orcad on the SSH host and, once the host proves it exited, removes the server from this machine. Its terminals end. Requires --yes.
            If the host cannot prove orcad exited, the server stays linked and the refusal says why; nothing is removed on a guess. For a host that is gone for good, use `orca environment forget`.
            If this server is the default host for new projects, choose another one first. `orca environment cancel-stop` withdraws a stop orcad has not acted on yet.
            --environment names a managed Orca server this machine deployed over SSH (see `orca environment list`); it is a selector here, not a routing flag.
            Runs on this machine’s Orca desktop app, the same action as Settings > Orca on your SSH hosts. A runtime without the SSH registry (headless `orca serve`) refuses it.

        Examples:
            orca environment stop --environment build-box --yes
        """
        return await self._client._invoke("environment stop", [], [("environment", environment), ("yes", yes), ("page", page)], json=True, remote=False)

    async def update(
        self,
        *,
        environment: Scalar,
        force: bool = False,
        page: Scalar | None = None,
    ) -> Any:
        """Update a managed Orca server to this build’s version.

        CLI: ``orca environment update --environment <selector> [--force] [--json]``

        Notes:
            Without --force, an update that would restart over running terminals is deferred and reported, not applied.
            --environment names a managed Orca server this machine deployed over SSH (see `orca environment list`); it is a selector here, not a routing flag.
            Runs on this machine’s Orca desktop app, the same action as Settings > Orca on your SSH hosts. A runtime without the SSH registry (headless `orca serve`) refuses it.

        Examples:
            orca environment update --environment build-box
        """
        return await self._client._invoke("environment update", [], [("environment", environment), ("force", force), ("page", page)], json=True, remote=False)

class AsyncFileResource(_AsyncResource):
    """Commands under ``orca file``."""

    async def diff(
        self,
        path: Scalar,
        *,
        staged: bool = False,
        worktree: Scalar | None = None,
        focus: bool = False,
    ) -> Any:
        """Open a file diff as a tab in its worktree without changing your view; --focus brings you to it.

        CLI: ``orca file diff <path> [--staged] [--worktree <selector>] [--focus] [--json]``

        Notes:
            The file opens as a tab in that worktree without changing what you are looking at, even in the worktree on screen. --focus brings you to it; agents should pass --focus only when the user asked to see the file.
            Diffs default to unstaged changes. Pass --staged to open the staged source-control diff.
            The path may be relative to the selected worktree or an absolute path inside that worktree.

        Examples:
            orca file diff src/App.tsx
            orca file diff --path package.json --staged --worktree branch:feature
        """
        return await self._client._invoke("file diff", [path], [("staged", staged), ("worktree", worktree), ("focus", focus)], json=True, remote=True)

    async def open(
        self,
        path: Scalar,
        *,
        line: int | str | None = None,
        column: int | str | None = None,
        worktree: Scalar | None = None,
        focus: bool = False,
    ) -> Any:
        """Open a file as a tab in its worktree without changing your view; --focus brings you to it.

        CLI: ``orca file open <path> [--line <n> [--column <n>]] [--worktree <selector>] [--focus] [--json]``

        Notes:
            --line and --column use 1-based positions; --column requires --line. Without --focus, the position is applied when you select the file. Markdown opens in source view for positioning. Older hosts open the file without positioning.
            The file opens as a tab in that worktree without changing what you are looking at, even in the worktree on screen. --focus brings you to it; agents should pass --focus only when the user asked to see the file.
            The path may be relative to the selected worktree or an absolute path inside that worktree. When --worktree is omitted, local CLI calls infer the current Orca worktree from cwd.
            A server with no app window (`orca serve`, orcad) cannot open tabs, so this fails with renderer_unavailable and opens nothing.

        Examples:
            orca file open src/App.tsx
            orca file open src/App.tsx --line 42 --column 7 --focus
            orca file open --path docs/readme.md --worktree active --focus
        """
        return await self._client._invoke("file open", [path], [("line", line), ("column", column), ("worktree", worktree), ("focus", focus)], json=True, remote=True)

    async def open_changed(
        self,
        *,
        mode: Scalar | None = None,
        worktree: Scalar | None = None,
        focus: bool = False,
    ) -> Any:
        """Open all git-changed files as tabs without changing your view; --focus brings you to them.

        CLI: ``orca file open-changed [--mode edit|diff|both] [--worktree <selector>] [--focus] [--json]``

        Notes:
            The files open as tabs in that worktree without changing what you are looking at, even in the worktree on screen. --focus brings you to them; agents should pass --focus only when the user asked to see the files.
            For v1, changed files come from git status for the selected worktree.
            The default mode is diff. Edit mode skips deleted files because there is no file to open.

        Examples:
            orca file open-changed
            orca file open-changed --mode both
            orca file open-changed --mode diff --worktree active
        """
        return await self._client._invoke("file open-changed", [], [("mode", mode), ("worktree", worktree), ("focus", focus)], json=True, remote=True)

class AsyncHostResource(_AsyncResource):
    """Commands under ``orca host``."""

    async def list(
        self,
        *,
        page: Scalar | None = None,
    ) -> Any:
        """List every machine this Orca host can target, and how to name each one.

        CLI: ``orca host list [--json]``

        Notes:
            Answers "what can I target and what do I pass" in one place: this machine, the SSH targets registered on it, and the Orca servers paired with it.
            The three kinds are reached differently. A paired Orca server is a connection, selected with --environment <name>. An SSH target is a machine the connected Orca host reaches, selected with --host ssh:<id>. Passing one where the other belongs is the most common way to get an empty or missing-host answer.
            Commands that take --host also accept any name this list prints, such as --host "this machine" or --host <ssh-target-name>. A name two hosts share is refused with the exact flag for each.
            SSH rows include the detected remote platform after that target has connected (linux, darwin, or win32); disconnected or older targets report platform unknown.
            SSH rows also include whether the target is currently connected and its lifecycle status when known.
            Paired-server rows come from the pairing store and report platform unknown; ask one server directly with `orca host name --environment <name>`.
            SSH targets are read from this machine's own Orca runtime, so this lists that machine's targets and not another server's. Run `orca host list` on the other machine to see the targets registered there.
            --environment and --pairing-code are rejected rather than ignored: paired servers come from this machine’s pairing store, so a routed answer would describe two machines at once.

        Examples:
            orca host list
            orca host list --json
        """
        return await self._client._invoke("host list", [], [("page", page)], json=True, remote=False)

    async def name(
        self,
        *,
        name: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Show or set the name this Orca runtime reports to connected clients.

        CLI: ``orca host name [--name <name>] [--json]``

        Notes:
            With --name, updates the answering runtime over its authenticated connection. Use an empty value to return to the detected computer name.
            Without --name, prints the name and platform the answering runtime reports.

        Examples:
            orca host name
            orca host name --name build-server
        """
        return await self._client._invoke("host name", [], [("name", name), ("page", page)], json=True, remote=True)

class AsyncInterceptResource(_AsyncResource):
    """Commands under ``orca intercept``."""

    async def disable(
        self,
        *,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Disable request interception.

        CLI: ``orca intercept disable [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("intercept disable", [], [("worktree", worktree), ("page", page)], json=True, remote=True)

    async def enable(
        self,
        *,
        patterns: Scalar | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Enable request interception (pause matching requests).

        CLI: ``orca intercept enable [--patterns <glob,...>] [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("intercept enable", [], [("patterns", patterns), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def list(
        self,
        *,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """List paused (intercepted) requests.

        CLI: ``orca intercept list [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("intercept list", [], [("worktree", worktree), ("page", page)], json=True, remote=True)

class AsyncJiraAssigneeResource(_AsyncResource):
    """Commands under ``orca jira assignee``."""

    async def clear(
        self,
        key: Scalar,
        *,
        site: Scalar | None = None,
    ) -> Any:
        """Clear a Jira issue assignee.

        CLI: ``orca jira assignee clear <key> [--site <id>] [--json]``

        Examples:
            orca jira assignee clear ENG-123 --json
        """
        return await self._client._invoke("jira assignee clear", [key], [("site", site)], json=True, remote=True)

    async def list(
        self,
        key: Scalar,
        *,
        site: Scalar | None = None,
        query: Scalar | None = None,
    ) -> Any:
        """List assignable users for a Jira issue.

        CLI: ``orca jira assignee list <key> [--query <text>] [--site <id>] [--json]``

        Examples:
            orca jira assignee list ENG-123 --query alex --json
        """
        return await self._client._invoke("jira assignee list", [key], [("site", site), ("query", query)], json=True, remote=True)

    async def set(
        self,
        key: Scalar,
        *,
        to_id: Scalar,
        site: Scalar | None = None,
    ) -> Any:
        """Assign a Jira issue.

        CLI: ``orca jira assignee set <key> --to-id <accountId> [--site <id>] [--json]``

        Examples:
            orca jira assignee set ENG-123 --to-id 5b10a2844c20165700ede21g --json
        """
        return await self._client._invoke("jira assignee set", [key], [("site", site), ("to-id", to_id)], json=True, remote=True)

class AsyncJiraCommentResource(_AsyncResource):
    """Commands under ``orca jira comment``."""

    async def add(
        self,
        key: Scalar,
        *,
        site: Scalar | None = None,
        body: Scalar | None = None,
        body_file: Scalar | None = None,
        stdin: str | bytes | None = None,
    ) -> Any:
        """Comment on a Jira issue.

        CLI: ``orca jira comment add <key> (--body <text> | --body-file <path|->) [--site <id>] [--json]``

        Examples:
            orca jira comment add ENG-123 --body "Fix is on staging"
        """
        return await self._client._invoke("jira comment add", [key], [("site", site), ("body", body), ("body-file", body_file)], json=True, remote=True, stdin=stdin)

    async def list(
        self,
        key: Scalar,
        *,
        site: Scalar | None = None,
    ) -> Any:
        """List comments on a Jira issue.

        CLI: ``orca jira comment list <key> [--site <id>] [--json]``

        Examples:
            orca jira comment list ENG-123 --json
        """
        return await self._client._invoke("jira comment list", [key], [("site", site)], json=True, remote=True)

class AsyncJiraLabelResource(_AsyncResource):
    """Commands under ``orca jira label``."""

    async def add(
        self,
        key: Scalar,
        *,
        label: Scalar | Sequence[Scalar],
        site: Scalar | None = None,
    ) -> Any:
        """Add labels to a Jira issue.

        CLI: ``orca jira label add <key> --label <name>... [--site <id>] [--json]``

        Examples:
            orca jira label add ENG-123 --label backend --json
        """
        return await self._client._invoke("jira label add", [key], [("site", site), ("label", label)], json=True, remote=True)

    async def rm(
        self,
        key: Scalar,
        *,
        label: Scalar | Sequence[Scalar],
        site: Scalar | None = None,
    ) -> Any:
        """Remove labels from a Jira issue.

        CLI: ``orca jira label rm <key> --label <name>... [--site <id>] [--json]``

        Examples:
            orca jira label rm ENG-123 --label backend --json
        """
        return await self._client._invoke("jira label rm", [key], [("site", site), ("label", label)], json=True, remote=True)

    async def set(
        self,
        key: Scalar,
        *,
        label: Scalar | Sequence[Scalar],
        site: Scalar | None = None,
    ) -> Any:
        """Replace the labels on a Jira issue.

        CLI: ``orca jira label set <key> --label <name> [--label <name>...] [--site <id>] [--json]``

        Examples:
            orca jira label set ENG-123 --label backend --label p1 --json
        """
        return await self._client._invoke("jira label set", [key], [("site", site), ("label", label)], json=True, remote=True)

class AsyncJiraPriorityResource(_AsyncResource):
    """Commands under ``orca jira priority``."""

    async def clear(
        self,
        key: Scalar,
        *,
        site: Scalar | None = None,
    ) -> Any:
        """Clear a Jira issue priority.

        CLI: ``orca jira priority clear <key> [--site <id>] [--json]``

        Examples:
            orca jira priority clear ENG-123 --json
        """
        return await self._client._invoke("jira priority clear", [key], [("site", site)], json=True, remote=True)

    async def list(
        self,
        *,
        site: Scalar | None = None,
    ) -> Any:
        """List Jira priorities.

        CLI: ``orca jira priority list [--site <id>] [--json]``

        Examples:
            orca jira priority list --json
        """
        return await self._client._invoke("jira priority list", [], [("site", site)], json=True, remote=True)

    async def set(
        self,
        key: Scalar,
        *,
        to_id: Scalar,
        site: Scalar | None = None,
    ) -> Any:
        """Set a Jira issue priority.

        CLI: ``orca jira priority set <key> --to-id <priorityId> [--site <id>] [--json]``

        Examples:
            orca jira priority set ENG-123 --to-id 2 --json
        """
        return await self._client._invoke("jira priority set", [key], [("site", site), ("to-id", to_id)], json=True, remote=True)

class AsyncJiraProjectResource(_AsyncResource):
    """Commands under ``orca jira project``."""

    async def fields(
        self,
        *,
        project: Scalar,
        type: Scalar,
        site: Scalar | None = None,
    ) -> Any:
        """List create fields for a Jira project and issue type.

        CLI: ``orca jira project fields --project <idOrKey> --type <id> [--site <id>] [--json]``

        Examples:
            orca jira project fields --project ENG --type 10001 --json
        """
        return await self._client._invoke("jira project fields", [], [("site", site), ("project", project), ("type", type)], json=True, remote=True)

    async def list(
        self,
        *,
        site: Scalar | None = None,
    ) -> Any:
        """List Jira projects.

        CLI: ``orca jira project list [--site <id>] [--json]``

        Examples:
            orca jira project list --json
        """
        return await self._client._invoke("jira project list", [], [("site", site)], json=True, remote=True)

    async def types(
        self,
        *,
        project: Scalar,
        site: Scalar | None = None,
    ) -> Any:
        """List Jira issue types for a project.

        CLI: ``orca jira project types --project <idOrKey> [--site <id>] [--json]``

        Examples:
            orca jira project types --project ENG --json
        """
        return await self._client._invoke("jira project types", [], [("site", site), ("project", project)], json=True, remote=True)

class AsyncJiraStatusResource(_AsyncResource):
    """Commands under ``orca jira status``."""

    async def list(
        self,
        key: Scalar,
        *,
        site: Scalar | None = None,
    ) -> Any:
        """List available transitions for a Jira issue.

        CLI: ``orca jira status list <key> [--site <id>] [--json]``

        Examples:
            orca jira status list ENG-123 --json
        """
        return await self._client._invoke("jira status list", [key], [("site", site)], json=True, remote=True)

    async def set(
        self,
        key: Scalar,
        *,
        site: Scalar | None = None,
        to: Scalar | None = None,
        to_id: Scalar | None = None,
    ) -> Any:
        """Transition a Jira issue.

        CLI: ``orca jira status set <key> (--to <name> | --to-id <transitionId>) [--site <id>] [--json]``

        Examples:
            orca jira status set ENG-123 --to "In Review"
            orca jira status set ENG-123 --to-id 31 --json
        """
        return await self._client._invoke("jira status set", [key], [("site", site), ("to", to), ("to-id", to_id)], json=True, remote=True)

class AsyncJiraResource(_AsyncResource):
    """Commands under ``orca jira``."""

    @cached_property
    def assignee(self) -> AsyncJiraAssigneeResource:
        """``orca jira assignee`` commands."""
        return AsyncJiraAssigneeResource(self._client)

    @cached_property
    def comment(self) -> AsyncJiraCommentResource:
        """``orca jira comment`` commands."""
        return AsyncJiraCommentResource(self._client)

    @cached_property
    def label(self) -> AsyncJiraLabelResource:
        """``orca jira label`` commands."""
        return AsyncJiraLabelResource(self._client)

    @cached_property
    def priority(self) -> AsyncJiraPriorityResource:
        """``orca jira priority`` commands."""
        return AsyncJiraPriorityResource(self._client)

    @cached_property
    def project(self) -> AsyncJiraProjectResource:
        """``orca jira project`` commands."""
        return AsyncJiraProjectResource(self._client)

    @cached_property
    def status(self) -> AsyncJiraStatusResource:
        """``orca jira status`` commands."""
        return AsyncJiraStatusResource(self._client)

    async def connection(
        self,
    ) -> Any:
        """List saved Jira site connections.

        CLI: ``orca jira connection [--json]``

        Notes:
            Reports saved connections, not verified Jira access or agent MCP authentication.
        """
        return await self._client._invoke("jira connection", [], [], json=True, remote=True)

    async def create(
        self,
        *,
        project: Scalar,
        type: Scalar,
        title: Scalar,
        site: Scalar | None = None,
        body: Scalar | None = None,
        body_file: Scalar | None = None,
        fields_json: Scalar | None = None,
        user_field: Scalar | Sequence[Scalar] | None = None,
        stdin: str | bytes | None = None,
    ) -> Any:
        """Create a Jira issue.

        CLI: ``orca jira create --project <idOrKey> --type <issueTypeId> --title <text> [--body <text> | --body-file <path|->] [--fields-json <json>] [--user-field <key>...] [--site <id>] [--json]``

        Examples:
            orca jira create --project ENG --type 10001 --title "Fix login redirect" --json
        """
        return await self._client._invoke("jira create", [], [("site", site), ("project", project), ("type", type), ("title", title), ("body", body), ("body-file", body_file), ("fields-json", fields_json), ("user-field", user_field)], json=True, remote=True, stdin=stdin)

    async def issue(
        self,
        key: Scalar,
        *,
        site: Scalar | None = None,
    ) -> Any:
        """Read a Jira issue.

        CLI: ``orca jira issue <key> [--site <id>] [--json]``

        Examples:
            orca jira issue ENG-123
            orca jira issue ENG-123 --json
        """
        return await self._client._invoke("jira issue", [key], [("site", site)], json=True, remote=True)

    async def list(
        self,
        *,
        site: Scalar | None = None,
        filter: Scalar | None = None,
        limit: int | str | None = None,
    ) -> Any:
        """List Jira issues for task triage.

        CLI: ``orca jira list [--filter assigned|reported|all|done] [--limit <n>] [--site <id>] [--json]``

        Examples:
            orca jira list --filter assigned --limit 10 --json
        """
        return await self._client._invoke("jira list", [], [("site", site), ("filter", filter), ("limit", limit)], json=True, remote=True)

    async def search(
        self,
        jql: Scalar,
        *,
        site: Scalar | None = None,
        limit: int | str | None = None,
    ) -> Any:
        """Search Jira issues with JQL.

        CLI: ``orca jira search <jql> [--limit <n>] [--site <id>] [--json]``

        Examples:
            orca jira search "project = ENG AND status = 'In Progress'"
            orca jira search "assignee = currentUser() AND updated >= -1d" --json
        """
        return await self._client._invoke("jira search", [jql], [("site", site), ("limit", limit)], json=True, remote=True)

class AsyncLinearAssigneeResource(_AsyncResource):
    """Commands under ``orca linear assignee``."""

    async def clear(
        self,
        id: Scalar | None = None,
        *,
        current: bool = False,
        workspace: Scalar | None = None,
    ) -> Any:
        """Clear a Linear issue assignee.

        CLI: ``orca linear assignee clear [<id>] [--current] [--workspace <id>] [--json]``

        Examples:
            orca linear assignee clear ENG-123 --json
        """
        return await self._client._invoke("linear assignee clear", [id], [("current", current), ("workspace", workspace)], json=True, remote=True)

    async def set(
        self,
        id: Scalar | None = None,
        *,
        current: bool = False,
        me: bool = False,
        to_id: Scalar | None = None,
        workspace: Scalar | None = None,
    ) -> Any:
        """Assign a Linear issue.

        CLI: ``orca linear assignee set [<id>] [--current] (--me | --to-id <userId>) [--workspace <id>] [--json]``

        Examples:
            orca linear assignee set --current --me --json
        """
        return await self._client._invoke("linear assignee set", [id], [("current", current), ("me", me), ("to-id", to_id), ("workspace", workspace)], json=True, remote=True)

class AsyncLinearCommentResource(_AsyncResource):
    """Commands under ``orca linear comment``."""

    async def add(
        self,
        id: Scalar | None = None,
        *,
        current: bool = False,
        body: Scalar | None = None,
        body_file: Scalar | None = None,
        reply_to: Scalar | None = None,
        write_id: Scalar | None = None,
        workspace: Scalar | None = None,
        stdin: str | bytes | None = None,
    ) -> Any:
        """Add a comment to a Linear issue.

        CLI: ``orca linear comment add [<id>] [--current] (--body <text> | --body-file <path|->) [--reply-to <commentId>] [--write-id <uuid>] [--workspace <id>] [--json]``

        Notes:
            Use --body-file - to read multiline comment bodies from stdin.

        Examples:
            orca linear comment add ENG-123 --body "Implementation is ready for review."
            orca linear comment add --current --body-file - --json
        """
        return await self._client._invoke("linear comment add", [id], [("current", current), ("body", body), ("body-file", body_file), ("reply-to", reply_to), ("write-id", write_id), ("workspace", workspace)], json=True, remote=True, stdin=stdin)

    async def delete(
        self,
        id: Scalar,
        *,
        workspace: Scalar | None = None,
    ) -> Any:
        """Delete a Linear comment.

        CLI: ``orca linear comment delete <commentId> [--workspace <id>] [--json]``

        Notes:
            Comment ids come from `comment add` output or `orca linear issue <id> --comments --json`.

        Examples:
            orca linear comment delete <commentId> --json
        """
        return await self._client._invoke("linear comment delete", [id], [("workspace", workspace)], json=True, remote=True)

    async def edit(
        self,
        id: Scalar,
        *,
        body: Scalar | None = None,
        body_file: Scalar | None = None,
        workspace: Scalar | None = None,
        stdin: str | bytes | None = None,
    ) -> Any:
        """Replace the body of a Linear comment.

        CLI: ``orca linear comment edit <commentId> (--body <text> | --body-file <path|->) [--workspace <id>] [--json]``

        Notes:
            Comment ids come from `comment add` output or `orca linear issue <id> --comments --json`.
            Linear only lets a comment be edited by its author.

        Examples:
            orca linear comment edit <commentId> --body "Updated: ready for review."
            orca linear comment edit <commentId> --body-file - --json
        """
        return await self._client._invoke("linear comment edit", [id], [("body", body), ("body-file", body_file), ("workspace", workspace)], json=True, remote=True, stdin=stdin)

class AsyncLinearDueDateResource(_AsyncResource):
    """Commands under ``orca linear due-date``."""

    async def clear(
        self,
        id: Scalar | None = None,
        *,
        current: bool = False,
        workspace: Scalar | None = None,
    ) -> Any:
        """Clear a Linear issue due date.

        CLI: ``orca linear due-date clear [<id>] [--current] [--workspace <id>] [--json]``

        Examples:
            orca linear due-date clear ENG-123 --json
        """
        return await self._client._invoke("linear due-date clear", [id], [("current", current), ("workspace", workspace)], json=True, remote=True)

    async def set(
        self,
        id: Scalar | None = None,
        *,
        to: Scalar,
        current: bool = False,
        workspace: Scalar | None = None,
    ) -> Any:
        """Set a Linear issue due date.

        CLI: ``orca linear due-date set [<id>] [--current] --to <yyyy-mm-dd> [--workspace <id>] [--json]``

        Examples:
            orca linear due-date set --current --to 2026-06-30 --json
        """
        return await self._client._invoke("linear due-date set", [id], [("current", current), ("to", to), ("workspace", workspace)], json=True, remote=True)

class AsyncLinearEstimateResource(_AsyncResource):
    """Commands under ``orca linear estimate``."""

    async def clear(
        self,
        id: Scalar | None = None,
        *,
        current: bool = False,
        workspace: Scalar | None = None,
    ) -> Any:
        """Clear a Linear issue estimate.

        CLI: ``orca linear estimate clear [<id>] [--current] [--workspace <id>] [--json]``

        Examples:
            orca linear estimate clear ENG-123 --json
        """
        return await self._client._invoke("linear estimate clear", [id], [("current", current), ("workspace", workspace)], json=True, remote=True)

    async def set(
        self,
        id: Scalar | None = None,
        *,
        to: int | str,
        current: bool = False,
        workspace: Scalar | None = None,
    ) -> Any:
        """Set a Linear issue estimate.

        CLI: ``orca linear estimate set [<id>] [--current] --to <number> [--workspace <id>] [--json]``

        Examples:
            orca linear estimate set --current --to 3 --json
        """
        return await self._client._invoke("linear estimate set", [id], [("current", current), ("to", to), ("workspace", workspace)], json=True, remote=True)

class AsyncLinearLabelResource(_AsyncResource):
    """Commands under ``orca linear label``."""

    async def add(
        self,
        id: Scalar | None = None,
        *,
        label: Scalar,
        current: bool = False,
        workspace: Scalar | None = None,
    ) -> Any:
        """Add labels to a Linear issue.

        CLI: ``orca linear label add [<id>] [--current] --label <labelId-or-exact-name>... [--workspace <id>] [--json]``

        Examples:
            orca linear label add --current --label Bug --json
        """
        return await self._client._invoke("linear label add", [id], [("current", current), ("label", label), ("workspace", workspace)], json=True, remote=True)

    async def remove(
        self,
        id: Scalar | None = None,
        *,
        label: Scalar,
        current: bool = False,
        workspace: Scalar | None = None,
    ) -> Any:
        """Remove labels from a Linear issue.

        CLI: ``orca linear label remove [<id>] [--current] --label <labelId-or-exact-name>... [--workspace <id>] [--json]``

        Examples:
            orca linear label remove --current --label Bug --json
        """
        return await self._client._invoke("linear label remove", [id], [("current", current), ("label", label), ("workspace", workspace)], json=True, remote=True)

    async def set(
        self,
        id: Scalar | None = None,
        *,
        label: Scalar,
        current: bool = False,
        workspace: Scalar | None = None,
    ) -> Any:
        """Replace labels on a Linear issue.

        CLI: ``orca linear label set [<id>] [--current] --label <labelId-or-exact-name>... [--workspace <id>] [--json]``

        Examples:
            orca linear label set ENG-123 --label Bug --json
        """
        return await self._client._invoke("linear label set", [id], [("current", current), ("label", label), ("workspace", workspace)], json=True, remote=True)

class AsyncLinearPriorityResource(_AsyncResource):
    """Commands under ``orca linear priority``."""

    async def clear(
        self,
        id: Scalar | None = None,
        *,
        current: bool = False,
        workspace: Scalar | None = None,
    ) -> Any:
        """Clear a Linear issue priority.

        CLI: ``orca linear priority clear [<id>] [--current] [--workspace <id>] [--json]``

        Examples:
            orca linear priority clear ENG-123 --json
        """
        return await self._client._invoke("linear priority clear", [id], [("current", current), ("workspace", workspace)], json=True, remote=True)

    async def set(
        self,
        id: Scalar | None = None,
        *,
        to: Scalar,
        current: bool = False,
        workspace: Scalar | None = None,
    ) -> Any:
        """Set a Linear issue priority.

        CLI: ``orca linear priority set [<id>] [--current] --to none|low|medium|high|urgent [--workspace <id>] [--json]``

        Examples:
            orca linear priority set --current --to high --json
        """
        return await self._client._invoke("linear priority set", [id], [("current", current), ("to", to), ("workspace", workspace)], json=True, remote=True)

class AsyncLinearProjectResource(_AsyncResource):
    """Commands under ``orca linear project``."""

    async def list(
        self,
        *,
        query: Scalar | None = None,
        limit: int | str | None = None,
        workspace: Scalar | None = None,
    ) -> Any:
        """List connected Linear projects.

        CLI: ``orca linear project list [--query <text>] [--limit <n>] [--workspace <id>|all] [--json]``

        Examples:
            orca linear project list --query launch --json
            orca linear project list --workspace all --json
        """
        return await self._client._invoke("linear project list", [], [("query", query), ("limit", limit), ("workspace", workspace)], json=True, remote=True)

class AsyncLinearRelationResource(_AsyncResource):
    """Commands under ``orca linear relation``."""

    async def add(
        self,
        id: Scalar | None = None,
        *,
        related: Scalar,
        type: Scalar,
        current: bool = False,
        workspace: Scalar | None = None,
    ) -> Any:
        """Add a Linear issue relation.

        CLI: ``orca linear relation add [<id>] [--current] --related <issue> --type blocks|blocked-by|related|duplicate-of [--workspace <id>] [--json]``

        Examples:
            orca linear relation add ENG-1 --related ENG-2 --type blocks --json
            orca linear relation add --current --related ENG-2 --type blocked-by --json
        """
        return await self._client._invoke("linear relation add", [id], [("current", current), ("related", related), ("type", type), ("workspace", workspace)], json=True, remote=True)

    async def remove(
        self,
        id: Scalar | None = None,
        *,
        related: Scalar,
        type: Scalar,
        current: bool = False,
        workspace: Scalar | None = None,
    ) -> Any:
        """Remove a Linear issue relation.

        CLI: ``orca linear relation remove [<id>] [--current] --related <issue> --type blocks|blocked-by|related|duplicate-of [--workspace <id>] [--json]``

        Examples:
            orca linear relation remove ENG-1 --related ENG-2 --type related --json
        """
        return await self._client._invoke("linear relation remove", [id], [("current", current), ("related", related), ("type", type), ("workspace", workspace)], json=True, remote=True)

class AsyncLinearStatusResource(_AsyncResource):
    """Commands under ``orca linear status``."""

    async def set(
        self,
        id: Scalar | None = None,
        *,
        to: Scalar,
        current: bool = False,
        workspace: Scalar | None = None,
    ) -> Any:
        """Set a Linear issue status.

        CLI: ``orca linear status set [<id>] [--current] --to <state> [--workspace <id>] [--json]``

        Examples:
            orca linear status set ENG-123 --to "In Review"
            orca linear status set --current --to Done --json
        """
        return await self._client._invoke("linear status set", [id], [("current", current), ("to", to), ("workspace", workspace)], json=True, remote=True)

class AsyncLinearTeamResource(_AsyncResource):
    """Commands under ``orca linear team``."""

    async def labels(
        self,
        *,
        team: Scalar,
        workspace: Scalar | None = None,
    ) -> Any:
        """List Linear team labels.

        CLI: ``orca linear team labels --team <key|id> [--workspace <id>] [--json]``

        Examples:
            orca linear team labels --team ENG --json
        """
        return await self._client._invoke("linear team labels", [], [("team", team), ("workspace", workspace)], json=True, remote=True)

    async def list(
        self,
        *,
        workspace: Scalar | None = None,
    ) -> Any:
        """List connected Linear teams.

        CLI: ``orca linear team list [--workspace <id>|all] [--json]``

        Examples:
            orca linear team list --workspace all --json
        """
        return await self._client._invoke("linear team list", [], [("workspace", workspace)], json=True, remote=True)

    async def members(
        self,
        *,
        team: Scalar,
        workspace: Scalar | None = None,
    ) -> Any:
        """List Linear team members.

        CLI: ``orca linear team members --team <key|id> [--workspace <id>] [--json]``

        Examples:
            orca linear team members --team ENG --json
        """
        return await self._client._invoke("linear team members", [], [("team", team), ("workspace", workspace)], json=True, remote=True)

    async def states(
        self,
        *,
        team: Scalar,
        workspace: Scalar | None = None,
    ) -> Any:
        """List Linear team workflow states.

        CLI: ``orca linear team states --team <key|id> [--workspace <id>] [--json]``

        Examples:
            orca linear team states --team ENG --json
        """
        return await self._client._invoke("linear team states", [], [("team", team), ("workspace", workspace)], json=True, remote=True)

class AsyncLinearResource(_AsyncResource):
    """Commands under ``orca linear``."""

    @cached_property
    def assignee(self) -> AsyncLinearAssigneeResource:
        """``orca linear assignee`` commands."""
        return AsyncLinearAssigneeResource(self._client)

    @cached_property
    def comment(self) -> AsyncLinearCommentResource:
        """``orca linear comment`` commands."""
        return AsyncLinearCommentResource(self._client)

    @cached_property
    def due_date(self) -> AsyncLinearDueDateResource:
        """``orca linear due-date`` commands."""
        return AsyncLinearDueDateResource(self._client)

    @cached_property
    def estimate(self) -> AsyncLinearEstimateResource:
        """``orca linear estimate`` commands."""
        return AsyncLinearEstimateResource(self._client)

    @cached_property
    def label(self) -> AsyncLinearLabelResource:
        """``orca linear label`` commands."""
        return AsyncLinearLabelResource(self._client)

    @cached_property
    def priority(self) -> AsyncLinearPriorityResource:
        """``orca linear priority`` commands."""
        return AsyncLinearPriorityResource(self._client)

    @cached_property
    def project(self) -> AsyncLinearProjectResource:
        """``orca linear project`` commands."""
        return AsyncLinearProjectResource(self._client)

    @cached_property
    def relation(self) -> AsyncLinearRelationResource:
        """``orca linear relation`` commands."""
        return AsyncLinearRelationResource(self._client)

    @cached_property
    def status(self) -> AsyncLinearStatusResource:
        """``orca linear status`` commands."""
        return AsyncLinearStatusResource(self._client)

    @cached_property
    def team(self) -> AsyncLinearTeamResource:
        """``orca linear team`` commands."""
        return AsyncLinearTeamResource(self._client)

    async def attach(
        self,
        id: Scalar | None = None,
        *,
        url: Scalar,
        current: bool = False,
        title: Scalar | None = None,
        write_id: Scalar | None = None,
        workspace: Scalar | None = None,
    ) -> Any:
        """Attach a link to a Linear issue.

        CLI: ``orca linear attach [<id>] [--current] --url <url> [--title <title>] [--write-id <uuid>] [--workspace <id>] [--json]``

        Examples:
            orca linear attach ENG-123 --url https://example.com/review/123 --title "PR/MR link"
            orca linear attach --current --url https://example.com/review/123 --json
        """
        return await self._client._invoke("linear attach", [id], [("current", current), ("url", url), ("title", title), ("write-id", write_id), ("workspace", workspace)], json=True, remote=True)

    async def create(
        self,
        *,
        title: Scalar,
        body: Scalar | None = None,
        body_file: Scalar | None = None,
        team: Scalar | None = None,
        project: Scalar | None = None,
        state: Scalar | None = None,
        assignee: Scalar | None = None,
        priority: Scalar | None = None,
        estimate: int | str | None = None,
        due_date: Scalar | None = None,
        label: Scalar | None = None,
        parent: Scalar | None = None,
        parent_current: bool = False,
        write_id: Scalar | None = None,
        workspace: Scalar | None = None,
        stdin: str | bytes | None = None,
    ) -> Any:
        """Create a Linear issue.

        CLI: ``orca linear create --title <title> [--body <text> | --body-file <path|->] [--team <key|id>] [--project <projectId-or-exact-name>] [--state <stateId|exact-name>] [--assignee me|<userId>] [--priority none|low|medium|high|urgent] [--estimate <number>] [--due-date <yyyy-mm-dd>] [--label <labelId-or-exact-name>]... [--parent <id> | --parent-current] [--write-id <uuid>] [--workspace <id>] [--json]``

        Notes:
            Use --body-file - to read multiline issue bodies from stdin.

        Examples:
            orca linear create --title "Investigate flaky login" --team ENG --project "Launch"
            orca linear create --title "Follow-up bug" --parent-current --body-file - --json
        """
        return await self._client._invoke("linear create", [], [("title", title), ("body", body), ("body-file", body_file), ("team", team), ("project", project), ("state", state), ("assignee", assignee), ("priority", priority), ("estimate", estimate), ("due-date", due_date), ("label", label), ("parent", parent), ("parent-current", parent_current), ("write-id", write_id), ("workspace", workspace)], json=True, remote=True, stdin=stdin)

    async def issue(
        self,
        id: Scalar | None = None,
        *,
        current: bool = False,
        comments: bool = False,
        children: bool = False,
        depth: int | str | None = None,
        attachments: bool = False,
        relations: bool = False,
        activity: bool = False,
        full: bool = False,
        workspace: Scalar | None = None,
    ) -> Any:
        """Read Linear issue context for agents.

        CLI: ``orca linear issue [<id>] [--current] [--comments] [--children] [--depth <n>] [--attachments] [--relations] [--activity] [--full] [--workspace <id>] [--json]``

        Examples:
            orca linear issue ENG-123
            orca linear issue --current --comments
            orca linear issue https://linear.app/acme/issue/ENG-123 --full --json
        """
        return await self._client._invoke("linear issue", [id], [("current", current), ("comments", comments), ("children", children), ("depth", depth), ("attachments", attachments), ("relations", relations), ("activity", activity), ("full", full), ("workspace", workspace)], json=True, remote=True)

    async def list(
        self,
        *,
        filter: Scalar | None = None,
        team: Scalar | None = None,
        limit: int | str | None = None,
        workspace: Scalar | None = None,
    ) -> Any:
        """List Linear issues for task triage.

        CLI: ``orca linear list [--filter assigned|created|all|completed|open] [--team <key|id>] [--limit <n>] [--workspace <id>|all] [--json]``

        Examples:
            orca linear list --filter assigned --limit 10 --json
        """
        return await self._client._invoke("linear list", [], [("filter", filter), ("team", team), ("limit", limit), ("workspace", workspace)], json=True, remote=True)

    async def list_issues(
        self,
        *,
        team: Scalar | None = None,
        cycle: Scalar | None = None,
        label: Scalar | None = None,
        limit: int | str | None = None,
        query: Scalar | None = None,
        state: Scalar | None = None,
        cursor: Scalar | None = None,
        order_by: Scalar | None = None,
        project: Scalar | None = None,
        release: Scalar | None = None,
        assignee: Scalar | None = None,
        delegate: Scalar | None = None,
        parent_id: Scalar | None = None,
        priority: Scalar | None = None,
        created_at: Scalar | None = None,
        updated_at: Scalar | None = None,
        include_archived: bool = False,
        workspace: Scalar | None = None,
    ) -> Any:
        """List Linear issues with MCP-compatible filters.

        CLI: ``orca linear list-issues [--team <team>] [--cycle <cycle>] [--label <label>] [--limit <n>] [--query <text>] [--state <state>] [--cursor <cursor>] [--order-by createdAt|updatedAt] [--project <project>] [--release <release>] [--assignee <user|me|null>] [--delegate <user|me|null>] [--parent-id <issue|null>] [--priority <0-4>] [--created-at <datetime|duration>] [--updated-at <datetime|duration>] [--include-archived] [--workspace <id>|all] [--json]``

        Notes:
            Omitting --limit returns every match (result.meta.limit is null); --limit <n> caps the read.
            JSON sets result.truncated when a cap held results back; text prints truncated: showing N.
            Reuse --cursor from the previous page. Issued cursors bind the workspace; raw Linear cursors still need --workspace.
            --priority is 0=none, 1=urgent, 2=high, 3=medium, 4=low. JSON includes priorityLabel on each issue.

        Examples:
            orca linear list-issues --team ENG --state started --assignee me --json
            orca linear list-issues --query auth --updated-at -P7D --json
            orca linear list-issues --assignee me --priority 1 --limit 100 --json
            orca linear list-issues --cursor <cursor> --json
        """
        return await self._client._invoke("linear list-issues", [], [("team", team), ("cycle", cycle), ("label", label), ("limit", limit), ("query", query), ("state", state), ("cursor", cursor), ("order-by", order_by), ("project", project), ("release", release), ("assignee", assignee), ("delegate", delegate), ("parent-id", parent_id), ("priority", priority), ("created-at", created_at), ("updated-at", updated_at), ("include-archived", include_archived), ("workspace", workspace)], json=True, remote=True)

    async def save_issue(
        self,
        id: Scalar | None = None,
        *,
        current: bool = False,
        team: Scalar | None = None,
        title: Scalar | None = None,
        description: Scalar | None = None,
        body: Scalar | None = None,
        body_file: Scalar | None = None,
        state: Scalar | None = None,
        assignee: Scalar | None = None,
        priority: Scalar | None = None,
        estimate: Scalar | None = None,
        due_date: Scalar | None = None,
        label: Scalar | None = None,
        project: Scalar | None = None,
        parent_id: Scalar | None = None,
        write_id: Scalar | None = None,
        workspace: Scalar | None = None,
        stdin: str | bytes | None = None,
    ) -> Any:
        """Create or update a Linear issue.

        CLI: ``orca linear save-issue [<id>] [--current] [--team <key|id>] [--title <title>] [--description <text> | --body-file <path|->] [--state <state>] [--assignee me|<user>|null] [--priority none|low|medium|high|urgent] [--estimate <number>|null] [--due-date <yyyy-mm-dd>|null] [--label <label>...] [--project <project>|null] [--parent-id <issue>|null] [--write-id <uuid>] [--workspace <id>] [--json]``

        Notes:
            Without <id> or --current, creates an issue and requires --team and --title.
            Labels replace the complete label set, matching Linear MCP save_issue semantics.
            Use the literal null to clear assignee, estimate, due date, project, or parent.

        Examples:
            orca linear save-issue --team ENG --title "Fix auth" --priority high --json
            orca linear save-issue ENG-123 --title "Fix OAuth callback" --assignee me --json
            orca linear save-issue --current --project null --due-date null --json
        """
        return await self._client._invoke("linear save-issue", [id], [("current", current), ("team", team), ("title", title), ("description", description), ("body", body), ("body-file", body_file), ("state", state), ("assignee", assignee), ("priority", priority), ("estimate", estimate), ("due-date", due_date), ("label", label), ("project", project), ("parent-id", parent_id), ("write-id", write_id), ("workspace", workspace)], json=True, remote=True, stdin=stdin)

    async def search(
        self,
        query: Scalar,
        *,
        limit: int | str | None = None,
        workspace: Scalar | None = None,
    ) -> Any:
        """Search connected Linear workspaces.

        CLI: ``orca linear search <query> [--limit <n>] [--workspace <id>|all] [--json]``

        Examples:
            orca linear search "auth bug"
            orca linear search ENG --workspace all --json
        """
        return await self._client._invoke("linear search", [query], [("limit", limit), ("workspace", workspace)], json=True, remote=True)

class AsyncMouseResource(_AsyncResource):
    """Commands under ``orca mouse``."""

    async def down(
        self,
        *,
        button: Scalar | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Press mouse button.

        CLI: ``orca mouse down [--button <left|right|middle>] [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("mouse down", [], [("button", button), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def move(
        self,
        *,
        x: int | str,
        y: int | str,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Move mouse to x,y coordinates.

        CLI: ``orca mouse move --x <n> --y <n> [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("mouse move", [], [("x", x), ("y", y), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def up(
        self,
        *,
        button: Scalar | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Release mouse button.

        CLI: ``orca mouse up [--button <left|right|middle>] [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("mouse up", [], [("button", button), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def wheel(
        self,
        *,
        dy: int | str,
        dx: int | str | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Scroll wheel.

        CLI: ``orca mouse wheel --dy <n> [--dx <n>] [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("mouse wheel", [], [("dy", dy), ("dx", dx), ("worktree", worktree), ("page", page)], json=True, remote=True)

class AsyncOrchestrationResource(_AsyncResource):
    """Commands under ``orca orchestration``."""

    async def ask(
        self,
        *,
        to: Scalar | None = None,
        run: Scalar | None = None,
        question: Scalar | None = None,
        resume: Scalar | None = None,
        dispatch_capability: Scalar | None = None,
        options: Scalar | None = None,
        timeout_ms: int | str | None = None,
        from_: Scalar | None = None,
        retry_request: Scalar | None = None,
    ) -> Any:
        """Ask the coordinator a question and block until answered.

        CLI: ``orca orchestration ask (--question <text> | --resume <message_id>) [--to <run:id>] [--run <run_id>] [--options <csv>] [--timeout-ms <n>] [--from <handle>] [--retry-request <id>] [--json]``

        Notes:
            From an active Dispatch, a new question defaults to its owning Run mailbox.
            Timeout leaves the question pending; resume with the original message ID.
        """
        return await self._client._invoke("orchestration ask", [], [("to", to), ("run", run), ("question", question), ("resume", resume), ("dispatch-capability", dispatch_capability), ("options", options), ("timeout-ms", timeout_ms), ("from", from_), ("retry-request", retry_request)], json=True, remote=True)

    async def check(
        self,
        *,
        terminal: Scalar | None = None,
        run: Scalar | None = None,
        ack: Scalar | None = None,
        unread: bool = False,
        peek: bool = False,
        all: bool = False,
        types: Scalar | None = None,
        format: bool = False,
        wait: bool = False,
        timeout_ms: int | str | None = None,
        retry_request: Scalar | None = None,
    ) -> Any:
        """Check this agent's messages.

        CLI: ``orca orchestration check [--terminal <handle>] [--run <run_id>] [--ack <delivery_id>] [--unread | --peek | --all] [--types <type,...>] [--format] [--wait] [--timeout-ms <n>] [--retry-request <id>] [--json]``

        Notes:
            On Windows PowerShell, quote comma-separated type filters, e.g. --types "worker_done,escalation".
            --types is the wake condition for --wait; a returned Delivery is always the whole FIFO batch, so it is never filtered by type. Without --wait it has no effect on consuming checks. Only --peek and --all filter their rows.
            --format renders the returned rows as local text only; it never writes to another terminal.
            A bound Run replays the same Delivery until --ack or all its messages are marked read, even with --types; process every message before acknowledging.
        """
        return await self._client._invoke("orchestration check", [], [("terminal", terminal), ("run", run), ("ack", ack), ("unread", unread), ("peek", peek), ("all", all), ("types", types), ("format", format), ("wait", wait), ("timeout-ms", timeout_ms), ("retry-request", retry_request)], json=True, remote=True)

    async def coordinator_start(
        self,
        *,
        spec: Scalar,
        from_: Scalar | None = None,
        poll_interval_ms: int | str | None = None,
        max_concurrent: int | str | None = None,
        worktree: Scalar | None = None,
    ) -> Any:
        """Retired: load the current orchestration skill.

        CLI: ``orca orchestration coordinator-start --spec <text> [--from <handle>] [--poll-interval-ms <n>] [--max-concurrent <n>] [--worktree <selector>] [--json]``

        Notes:
            This command performs no effects and returns the exact `skills get orchestration --full` recovery action.
            Use the lightweight Run, Task, and worker-start primitives described by the current skill.
        """
        return await self._client._invoke("orchestration coordinator-start", [], [("spec", spec), ("from", from_), ("poll-interval-ms", poll_interval_ms), ("max-concurrent", max_concurrent), ("worktree", worktree)], json=True, remote=True)

    async def coordinator_stop(
        self,
    ) -> Any:
        """Retired: load the current orchestration skill.

        CLI: ``orca orchestration coordinator-stop [--json]``

        Notes:
            This command performs no effects and returns the exact `skills get orchestration --full` recovery action.
        """
        return await self._client._invoke("orchestration coordinator-stop", [], [], json=True, remote=True)

    async def dispatch(
        self,
        *,
        task: Scalar,
        to: Scalar,
        from_: Scalar | None = None,
        run: Scalar | None = None,
        inject: bool = False,
        dry_run: bool = False,
        return_preamble: bool = False,
        retry_request: Scalar | None = None,
    ) -> Any:
        """Dispatch a task to a terminal.

        CLI: ``orca orchestration dispatch --task <task_id> --to <handle> [--from <handle>] [--run <run_id>] [--inject] [--dry-run] [--return-preamble] [--retry-request <id>] [--json]``
        """
        return await self._client._invoke("orchestration dispatch", [], [("task", task), ("to", to), ("from", from_), ("run", run), ("inject", inject), ("dry-run", dry_run), ("return-preamble", return_preamble), ("retry-request", retry_request)], json=True, remote=True)

    async def dispatch_show(
        self,
        *,
        task: Scalar,
        preamble: bool = False,
        from_: Scalar | None = None,
    ) -> Any:
        """Show dispatch context for a task.

        CLI: ``orca orchestration dispatch-show --task <task_id> [--preamble] [--from <handle>] [--json]``
        """
        return await self._client._invoke("orchestration dispatch-show", [], [("task", task), ("preamble", preamble), ("from", from_)], json=True, remote=True)

    async def gate_create(
        self,
        *,
        task: Scalar,
        question: Scalar,
        options: Scalar | None = None,
        from_: Scalar | None = None,
        retry_request: Scalar | None = None,
    ) -> Any:
        """Create a decision gate blocking a task.

        CLI: ``orca orchestration gate-create --task <task_id> --question <text> [--options <json_array>] [--from <handle>] [--retry-request <id>] [--json]``
        """
        return await self._client._invoke("orchestration gate-create", [], [("task", task), ("question", question), ("options", options), ("from", from_), ("retry-request", retry_request)], json=True, remote=True)

    async def gate_list(
        self,
        *,
        task: Scalar | None = None,
        status: Scalar | None = None,
        run: Scalar | None = None,
        from_: Scalar | None = None,
    ) -> Any:
        """List decision gates.

        CLI: ``orca orchestration gate-list [--task <task_id>] [--status <status>] [--run <run_id>] [--from <handle>] [--json]``

        Notes:
            --run inspects a named Run without binding; otherwise gates are scoped to the caller.
        """
        return await self._client._invoke("orchestration gate-list", [], [("task", task), ("status", status), ("run", run), ("from", from_)], json=True, remote=True)

    async def gate_resolve(
        self,
        *,
        id: Scalar,
        resolution: Scalar,
        from_: Scalar | None = None,
        retry_request: Scalar | None = None,
    ) -> Any:
        """Resolve a pending decision gate.

        CLI: ``orca orchestration gate-resolve --id <gate_id> --resolution <text> [--from <handle>] [--retry-request <id>] [--json]``
        """
        return await self._client._invoke("orchestration gate-resolve", [], [("id", id), ("resolution", resolution), ("from", from_), ("retry-request", retry_request)], json=True, remote=True)

    async def inbox(
        self,
        *,
        limit: int | str | None = None,
        terminal: Scalar | None = None,
        full: bool = False,
    ) -> Any:
        """Show messages across (or for) recipients.

        CLI: ``orca orchestration inbox [--limit <n>] [--terminal <handle>] [--full] [--json]``
        """
        return await self._client._invoke("orchestration inbox", [], [("limit", limit), ("terminal", terminal), ("full", full)], json=True, remote=True)

    async def reply(
        self,
        *,
        id: Scalar,
        body: Scalar,
        run: Scalar | None = None,
        from_: Scalar | None = None,
        retry_request: Scalar | None = None,
    ) -> Any:
        """Reply to a message.

        CLI: ``orca orchestration reply --id <msg_id> --body <text> [--run <run_id>] [--from <handle>] [--retry-request <id>] [--json]``
        """
        return await self._client._invoke("orchestration reply", [], [("id", id), ("body", body), ("run", run), ("from", from_), ("retry-request", retry_request)], json=True, remote=True)

    async def request_show(
        self,
        *,
        request: Scalar,
    ) -> Any:
        """Ask whether one orchestration mutation request already took effect.

        CLI: ``orca orchestration request-show --request <request_id> [--json]``

        Notes:
            Read-only: it never starts, retries, or settles anything, so it is safe to run after any lost response.
            completed means the mutation landed and --retry-request replays the recorded outcome instead of starting a second one. pending means the original mutation is still running or Orca restarted before recording its outcome; wait for a live original command, otherwise replay with --retry-request.
            absent means this runtime holds no receipt for that request under your caller identity: it never arrived, it failed before recording anything, or the receipt was pruned. Absent is not proof that nothing happened.
        """
        return await self._client._invoke("orchestration request-show", [], [("request", request)], json=True, remote=True)

    async def reset(
        self,
        *,
        all: bool = False,
        tasks: bool = False,
        messages: bool = False,
        retry_request: Scalar | None = None,
    ) -> Any:
        """Reset one explicit orchestration state scope.

        CLI: ``orca orchestration reset (--all | --tasks | --messages) [--retry-request <id>] [--json]``
        """
        return await self._client._invoke("orchestration reset", [], [("all", all), ("tasks", tasks), ("messages", messages), ("retry-request", retry_request)], json=True, remote=True)

    async def run_create(
        self,
        *,
        objective: Scalar,
        from_: Scalar | None = None,
        retry_request: Scalar | None = None,
    ) -> Any:
        """Create and bind a lightweight orchestration Run.

        CLI: ``orca orchestration run-create --objective <text> [--from <handle>] [--retry-request <id>] [--json]``

        Notes:
            A Run is a namespace and home inbox. It never schedules or places workers.
            --retry-request is only for exact recovery after an unknown mutation result.
        """
        return await self._client._invoke("orchestration run-create", [], [("objective", objective), ("from", from_), ("retry-request", retry_request)], json=True, remote=True)

    async def run_current(
        self,
        *,
        from_: Scalar | None = None,
    ) -> Any:
        """Show the Run bound to this coordinator.

        CLI: ``orca orchestration run-current [--from <handle>] [--json]``
        """
        return await self._client._invoke("orchestration run-current", [], [("from", from_)], json=True, remote=True)

    async def run_list(
        self,
        *,
        limit: int | str | None = None,
        cursor: Scalar | None = None,
    ) -> Any:
        """List lightweight orchestration Runs.

        CLI: ``orca orchestration run-list [--limit <n>] [--cursor <cursor>] [--json]``
        """
        return await self._client._invoke("orchestration run-list", [], [("limit", limit), ("cursor", cursor)], json=True, remote=True)

    async def run_show(
        self,
        *,
        id: Scalar,
    ) -> Any:
        """Show one lightweight orchestration Run.

        CLI: ``orca orchestration run-show --id <run_id> [--json]``
        """
        return await self._client._invoke("orchestration run-show", [], [("id", id)], json=True, remote=True)

    async def run_use(
        self,
        *,
        id: Scalar,
        from_: Scalar | None = None,
        takeover_legacy: bool = False,
        retry_request: Scalar | None = None,
    ) -> Any:
        """Bind this coordinator to an existing Run.

        CLI: ``orca orchestration run-use --id <run_id> [--from <handle>] [--takeover-legacy] [--retry-request <id>] [--json]``

        Notes:
            --takeover-legacy must run in the live coordinator agent terminal it binds; it preserves existing worker assignments.
        """
        return await self._client._invoke("orchestration run-use", [], [("id", id), ("from", from_), ("takeover-legacy", takeover_legacy), ("retry-request", retry_request)], json=True, remote=True)

    async def send(
        self,
        *,
        subject: Scalar,
        to: Scalar | None = None,
        run: Scalar | None = None,
        from_: Scalar | None = None,
        body: Scalar | None = None,
        type: Scalar | None = None,
        priority: Scalar | None = None,
        thread_id: Scalar | None = None,
        payload: Scalar | None = None,
        task_id: Scalar | None = None,
        dispatch_id: Scalar | None = None,
        dispatch_capability: Scalar | None = None,
        retry_request: Scalar | None = None,
        outcome: Scalar | None = None,
        files_modified: Scalar | None = None,
        report_path: Scalar | None = None,
        phase: Scalar | None = None,
    ) -> Any:
        """Send an inter-agent message.

        CLI: ``orca orchestration send --subject <text> [--to <run:id|dispatch:id|legacy_handle>] [--run <run_id>] [--from <handle>] [--body <text>] [--type <type>] [--priority <level>] [--thread-id <id>] [--payload <json>] [--task-id <id>] [--dispatch-id <id>] [--outcome <succeeded|failed>] [--files-modified <csv>] [--report-path <path>] [--phase <text>] [--retry-request <id>] [--json]``

        Notes:
            Valid --type values: status, dispatch, worker_done, merge_ready, escalation, handoff, decision_gate, question, heartbeat.
            To answer a worker question, use orchestration reply --id <msg_id> --body <text> with the same Orca CLI executable.
            Group addresses (@all, @idle, @codex, ...) reach the live Dispatches of your own Run; a sender in no Run must use run:<id> or dispatch:<id>. @worktree:<id> names one workspace.
            Run groups exclude their owning coordinator; send to run:<id> to raise something with yours. Nested coordinators receive group mail in their child Run mailbox; @worktree:<id> includes workspace coordinators.
            On Windows PowerShell, quote group addresses such as --to "@all" or --to "@worktree:<id>".
            worker_done and heartbeat are exact-Dispatch signals and cannot target groups; omit --to to use the Dispatch's Run mailbox.
            worker_done requires --outcome succeeded or --outcome failed.
            From an active Dispatch, an omitted recipient defaults to its owning Run mailbox.
            Use --to dispatch:<id> for attempt-specific coordinator guidance; Orca durably relays it to a connected worker server.
            A worker_done with the active task/dispatch IDs completes that task only from the dispatched pane. When stable pane identity is unavailable, the sender handle must exactly match the dispatch assignee; injected preambles include the correct --from value.
            Prefer --task-id/--dispatch-id/etc. over raw --payload JSON in worker commands; PowerShell strips JSON quotes easily.
        """
        return await self._client._invoke("orchestration send", [], [("to", to), ("run", run), ("from", from_), ("subject", subject), ("body", body), ("type", type), ("priority", priority), ("thread-id", thread_id), ("payload", payload), ("task-id", task_id), ("dispatch-id", dispatch_id), ("dispatch-capability", dispatch_capability), ("retry-request", retry_request), ("outcome", outcome), ("files-modified", files_modified), ("report-path", report_path), ("phase", phase)], json=True, remote=True)

    async def task_create(
        self,
        *,
        spec: Scalar,
        task_title: Scalar | None = None,
        display_name: Scalar | None = None,
        deps: Scalar | None = None,
        parent: Scalar | None = None,
        run: Scalar | None = None,
        from_: Scalar | None = None,
        retry_request: Scalar | None = None,
    ) -> Any:
        """Create an orchestration task.

        CLI: ``orca orchestration task-create --spec <text> [--task-title <text>] [--display-name <text>] [--deps <json_array>] [--parent <task_id>] [--run <run_id>] [--from <handle>] [--retry-request <id>] [--json]``
        """
        return await self._client._invoke("orchestration task-create", [], [("spec", spec), ("task-title", task_title), ("display-name", display_name), ("deps", deps), ("parent", parent), ("run", run), ("from", from_), ("retry-request", retry_request)], json=True, remote=True)

    async def task_list(
        self,
        *,
        status: Scalar | None = None,
        ready: bool = False,
        brief: bool = False,
        run: Scalar | None = None,
        from_: Scalar | None = None,
    ) -> Any:
        """List orchestration tasks.

        CLI: ``orca orchestration task-list [--status <status>] [--ready] [--brief] [--run <run_id>] [--from <handle>] [--json]``

        Notes:
            --brief collapses whitespace and caps each spec at 160 characters.
        """
        return await self._client._invoke("orchestration task-list", [], [("status", status), ("ready", ready), ("brief", brief), ("run", run), ("from", from_)], json=True, remote=True)

    async def task_update(
        self,
        *,
        id: Scalar,
        status: Scalar,
        result: Scalar | None = None,
        run: Scalar | None = None,
        from_: Scalar | None = None,
        retry_request: Scalar | None = None,
    ) -> Any:
        """Update a task status.

        CLI: ``orca orchestration task-update --id <task_id> --status <status> [--result <text>] [--run <run_id>] [--from <handle>] [--retry-request <id>] [--json]``

        Notes:
            Valid --status values: pending, ready, dispatched, completed, failed, blocked.
            To cancel a Task, stop or abandon its worker, then set --status failed --result cancelled; a later worker-start --retry-of reopens it.
        """
        return await self._client._invoke("orchestration task-update", [], [("id", id), ("status", status), ("result", result), ("run", run), ("from", from_), ("retry-request", retry_request)], json=True, remote=True)

    async def worker_abandon(
        self,
        *,
        dispatch: Scalar,
        retry_request: Scalar | None = None,
    ) -> Any:
        """Fence a worker without claiming its process stopped.

        CLI: ``orca orchestration worker-abandon --dispatch <dispatch_id> [--retry-request <id>] [--json]``

        Notes:
            Retains all possibly-live resources and performs no process or filesystem action.
        """
        return await self._client._invoke("orchestration worker-abandon", [], [("dispatch", dispatch), ("retry-request", retry_request)], json=True, remote=True)

    async def worker_list(
        self,
        *,
        run: Scalar | None = None,
        terminal_state: Scalar | None = None,
        include_remote: bool = False,
        cursor: Scalar | None = None,
        limit: Scalar | None = None,
    ) -> Any:
        """List supervised worker terminal resource accounting.

        CLI: ``orca orchestration worker-list [--run <run_id>] [--terminal-state <active|reclaimable|retained|release_pending|release_unknown|released>] [--include-remote] [--cursor <cursor>] [--limit <1-100>] [--json]``

        Notes:
            Terminal state is process accounting and is reported separately from Task status; a completed Task can still own a live terminal.
            Context-only Dispatches created by orchestration dispatch are included as unsupervised with terminal state retained.
            Returns at most 100 local rows, newest first, by default; --include-remote adds connected-server observations when the host supports fleet listing. Continue with the opaque page.nextCursor value unchanged.
            Without --run the list is scoped to the Run bound to the calling terminal, and to every Run when there is no binding; the receipt reports which in scope.source (flag, bound, or all).
        """
        return await self._client._invoke("orchestration worker-list", [], [("run", run), ("terminal-state", terminal_state), ("include-remote", include_remote), ("cursor", cursor), ("limit", limit)], json=True, remote=True)

    async def worker_read(
        self,
        *,
        dispatch: Scalar,
        source: Scalar | None = None,
        cursor: Scalar | None = None,
        limit: int | str | None = None,
    ) -> Any:
        """Read bounded output from one supervised worker.

        CLI: ``orca orchestration worker-read --dispatch <dispatch_id> [--source <auto|transcript|terminal>] [--cursor <cursor>] [--limit <n>] [--json]``

        Notes:
            The default auto source uses an exact hook-reported transcript when available and otherwise returns labeled terminal output.
            A Dispatch created by orchestration dispatch reads from its adopted terminal with worker status unsupervised.
            A returned cursor is pinned to the exact source; start a fresh read if Orca reports source_changed.
        """
        return await self._client._invoke("orchestration worker-read", [], [("dispatch", dispatch), ("source", source), ("cursor", cursor), ("limit", limit)], json=True, remote=True)

    async def worker_release(
        self,
        *,
        dispatch: Scalar,
        retry_request: Scalar | None = None,
    ) -> Any:
        """Release the terminal of one settled supervised worker.

        CLI: ``orca orchestration worker-release --dispatch <dispatch_id> [--retry-request <id>] [--json]``

        Notes:
            Post-completion cleanup for a settled (succeeded or failed) worker; closes only the exact coordinator-owned agent terminal of that worker.
            A settled Dispatch created by orchestration dispatch has no owned terminal resource and is reported retained without process action.
            An inspectable output archive is preserved before the terminal closes, so worker-read still returns output afterwards.
            Never closes setup terminals, configured tabs, reused or pre-existing terminals, user-taken-over terminals, or unproven identities.
            Idempotent: repeating the call reports already_released. Only release_unknown exits 1; retained, release_pending, and already_released exit 0.
        """
        return await self._client._invoke("orchestration worker-release", [], [("dispatch", dispatch), ("retry-request", retry_request)], json=True, remote=True)

    async def worker_retain(
        self,
        *,
        dispatch: Scalar,
        retry_request: Scalar | None = None,
    ) -> Any:
        """Keep one supervised worker terminal live for debugging.

        CLI: ``orca orchestration worker-retain --dispatch <dispatch_id> [--retry-request <id>] [--json]``

        Notes:
            Records a durable user-requested exception; a later explicit worker-release clears it and releases the terminal.
            A settled Dispatch created by orchestration dispatch has no owned terminal resource and is reported retained without process action.
            Performs no process or filesystem action.
        """
        return await self._client._invoke("orchestration worker-retain", [], [("dispatch", dispatch), ("retry-request", retry_request)], json=True, remote=True)

    async def worker_show(
        self,
        *,
        dispatch: Scalar,
    ) -> Any:
        """Inspect one supervised worker Dispatch.

        CLI: ``orca orchestration worker-show --dispatch <dispatch_id> [--json]``

        Notes:
            A Dispatch created by orchestration dispatch is shown as unsupervised and reports the exact adopted terminal when its identity is still provable.
            observation.agentWait names a worker parked on a prompt only a human can answer, with the evidence that proved it (hook, prompt-text, or title). Null means Orca looked and found no wait. An absent field means it never looked — an older host, an unverifiable worker identity, an unreadable pane, or an agent probe that did not answer in time — and never means the worker is not waiting. A waiting worker is healthy, not failed.
        """
        return await self._client._invoke("orchestration worker-show", [], [("dispatch", dispatch)], json=True, remote=True)

    async def worker_start(
        self,
        *,
        task: Scalar | None = None,
        spec: Scalar | None = None,
        task_title: Scalar | None = None,
        deps: Scalar | None = None,
        parent: Scalar | None = None,
        on: Scalar | None = None,
        worktree: Scalar | None = None,
        name: Scalar | None = None,
        repo: Scalar | None = None,
        base_branch: Scalar | None = None,
        display_name: Scalar | None = None,
        comment: Scalar | None = None,
        setup: Scalar | None = None,
        agent: Scalar | None = None,
        model: Scalar | None = None,
        effort: Scalar | None = None,
        terminal: Scalar | None = None,
        retry_of: Scalar | None = None,
        timeout_ms: int | str | None = None,
        run: Scalar | None = None,
        from_: Scalar | None = None,
        retry_request: Scalar | None = None,
    ) -> Any:
        """Start one supervised worker on the Run home or a connected Orca server.

        CLI: ``orca orchestration worker-start (--task <task_id> | --spec <text>) [--on <saved-environment>] [--worktree <current|selector|new-child|new-top-level>] (--agent <agent> | --terminal <handle>) [--task-title <text>] [--deps <json_array>] [--parent <task_id>] [--model <id>] [--effort <level>] [--name <name>] [--repo <selector>] [--base-branch <ref>] [--display-name <text>] [--comment <text>] [--setup <run|skip|inherit>] [--retry-of <dispatch_id>] [--timeout-ms <n>] [--run <run_id>] [--from <handle>] [--retry-request <id>] [--json]``

        Notes:
            Current and existing worktrees never rerun setup; a fresh agent terminal is created unless --terminal is explicit.
            When reusing --terminal, pass --worktree for that terminal; current means the coordinator worktree.
            --agent takes an Orca agent id enabled on the worker server, such as claude, codex, cursor, antigravity, muse, zcode, opencode, or opencode2.
            --model supports Claude, Codex, Cursor, Antigravity, and Muse opaque provider model ids; --effort requires --model. OMP accepts --model only; --effort is unsupported. Neither can combine with --terminal. OpenCode model selection requires an existing worktree, a verified execution-host CLI, and an available model; effort is unsupported. Other agents, including zcode, launch with the model from their own config.
            New worktrees use agent-first creation and default --setup to run. Repository start-immediately runs setup beside the agent; wait-for-setup gates agent readiness and task input.
            Creation flags (--name, --repo, --base-branch, --display-name, --comment, --setup) are rejected for current/existing worktrees. Use exact --repo on the selected server; project/host convenience routing remains on worktree create.
            How the worker runs follows the user's own setting for new agent tabs; there is no flag for it and no caller needs to ask. A dispatch the setting cannot apply to still starts, so the placement, agent, and launch options passed here are always the ones honoured.
            Drive every worker the same way whichever way it was started: the same orchestration verbs, the same handle. Mail, dispatch, worker-show, worker-read and the whole lifecycle behave identically. The start receipt records which one ran, for operators and telemetry.
            Not every worker has a terminal. Read output with worker-read --source auto or --source transcript, which always work; --source terminal is refused when there is none, and orca terminal verbs do not accept every worker handle. Nothing above needs you to know which kind you have — the orchestration verbs cover all of them.
            --on selects only the worker server; the Run and this command remain on the current Orca server.
            Remote current and new-child are invalid; discover an exact remote selector or use new-top-level.
            --retry-of needs --task naming the failed Task (--spec creates a new one) and does not inherit placement; repeat the intended --on/worktree and --agent/terminal choices.
            The call exits 0 only for ready. Failed or outcome_unknown exits 1 and JSON includes stage/failedStage, setup, effects, residualResources, and recovery commands when needed.
        """
        return await self._client._invoke("orchestration worker-start", [], [("task", task), ("spec", spec), ("task-title", task_title), ("deps", deps), ("parent", parent), ("on", on), ("worktree", worktree), ("name", name), ("repo", repo), ("base-branch", base_branch), ("display-name", display_name), ("comment", comment), ("setup", setup), ("agent", agent), ("model", model), ("effort", effort), ("terminal", terminal), ("retry-of", retry_of), ("timeout-ms", timeout_ms), ("run", run), ("from", from_), ("retry-request", retry_request)], json=True, remote=True)

    async def worker_stop(
        self,
        *,
        dispatch: Scalar,
        retry_request: Scalar | None = None,
    ) -> Any:
        """Fence one Dispatch and stop its supervised agent terminal.

        CLI: ``orca orchestration worker-stop --dispatch <dispatch_id> [--retry-request <id>] [--json]``

        Notes:
            A Dispatch created by orchestration dispatch is fenced without closing its unsupervised terminal process.
            Never deletes the worktree, setup terminal, configured tabs, or unrelated processes.
        """
        return await self._client._invoke("orchestration worker-stop", [], [("dispatch", dispatch), ("retry-request", retry_request)], json=True, remote=True)

class AsyncProfileStateResource(_AsyncResource):
    """Commands under ``orca profile state``."""

    async def exports(
        self,
        *,
        profile_id: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """List retained SQLite backups and JSON exports for profile-state recovery.

        CLI: ``orca profile state exports [--profile-id <id>] [--json]``
        """
        return await self._client._invoke("profile state exports", [], [("profile-id", profile_id), ("page", page)], json=True, remote=True)

    async def rollback(
        self,
        *,
        revision: Scalar | None = None,
        backup: Scalar | None = None,
        current_json: bool = False,
        current_sqlite: bool = False,
        latest_json: bool = False,
        profile_id: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Restore a SQLite backup or retained JSON export, or keep the current JSON or SQLite profile.

        CLI: ``orca profile state rollback (--backup <id> | --revision <revision> | --current-json | --current-sqlite | --latest-json) [--profile-id <id>] [--json]``

        Notes:
            --profile-id selects another profile without changing the active profile. Prepare each profile before installing a JSON-only build.
            Orca must be stopped. Recovery validates the selected artifact and archives the current database family, JSON, and retained recovery artifacts before replacing state.
            --backup restores SQLite authority; --revision restores a JSON export for an older compatible runtime.
            --latest-json exports the latest SQLite state and restores it as JSON before launching an older JSON-only build. The current database and recovery artifacts are archived.
            --current-json keeps the current orca-data.json, including edits from an older build. It replaces SQLite state without merging; both copies are archived. The next SQLite-capable start imports the selected JSON.
            --current-sqlite keeps the current SQLite state and discards JSON edits from an older build. The JSON is archived, then rewritten from SQLite.

        Examples:
            orca profile state exports
            orca profile state rollback --backup <id>
            orca profile state rollback --revision 1
            orca profile state rollback --latest-json
            orca profile state rollback --current-json
            orca profile state rollback --current-sqlite
        """
        return await self._client._invoke("profile state rollback", [], [("revision", revision), ("backup", backup), ("current-json", current_json), ("current-sqlite", current_sqlite), ("latest-json", latest_json), ("profile-id", profile_id), ("page", page)], json=True, remote=True)

class AsyncProfileResource(_AsyncResource):
    """Commands under ``orca profile``."""

    @cached_property
    def state(self) -> AsyncProfileStateResource:
        """``orca profile state`` commands."""
        return AsyncProfileStateResource(self._client)

class AsyncProjectResource(_AsyncResource):
    """Commands under ``orca project``."""

    async def list(
        self,
    ) -> Any:
        """List durable projects known to Orca.

        CLI: ``orca project list [--json]``

        Examples:
            orca project list
            orca project list --json
        """
        return await self._client._invoke("project list", [], [], json=True, remote=True)

    async def setup_clone(
        self,
        *,
        project: Scalar,
        host: Scalar,
        url: Scalar,
        destination: Scalar,
        display_name: Scalar | None = None,
    ) -> Any:
        """Make a project available on a host by cloning a repository.

        CLI: ``orca project setup-clone --project <id> --host <host> --url <clone-url> --destination <path> [--display-name <name>] [--json]``

        Notes:
            For remote runtimes, --destination must be an absolute parent directory on the remote server.
            --host takes local, ssh:<target-id>, runtime:<environment-id>, or the bare host name `orca host list` prints for any of them.
            SSH targets are cloned through the desktop UI because the desktop client owns SSH connections.

        Examples:
            orca project setup-clone --project github:stablyai/orca --host local --url https://github.com/stablyai/orca.git --destination ~/src
            orca project setup-clone --project github:stablyai/orca --host runtime:03ef704c-b180-4b10-998d-e28fbd5de9a3 --url https://github.com/stablyai/orca.git --destination /srv --json
        """
        return await self._client._invoke("project setup-clone", [], [("project", project), ("host", host), ("url", url), ("destination", destination), ("display-name", display_name)], json=True, remote=True)

    async def setup_create(
        self,
        *,
        project: Scalar,
        host: Scalar,
        setup_id: Scalar | None = None,
        path: Scalar | None = None,
        kind: Scalar | None = None,
        display_name: Scalar | None = None,
        worktree_base_path: Scalar | None = None,
        git_username: Scalar | None = None,
        state: Scalar | None = None,
        method: Scalar | None = None,
    ) -> Any:
        """Create independent project host setup metadata.

        CLI: ``orca project setup-create --project <id> --host <host> [--setup-id <id>] [--path <path>] [--kind git|folder] [--display-name <name>] [--worktree-base-path <path>] [--git-username <name>] [--state ready|not-set-up|setting-up|error|unsupported] [--method imported-existing-folder|cloned|provisioned] [--json]``

        Notes:
            Creates setup metadata without registering a repo compatibility record.
            --host takes local, ssh:<target-id>, runtime:<environment-id>, or the bare host name `orca host list` prints for any of them.
            Use setup-existing-folder when Orca should import and manage an actual checkout path now.

        Examples:
            orca project setup-create --project github:stablyai/orca --host runtime:03ef704c-b180-4b10-998d-e28fbd5de9a3 --state setting-up --method provisioned --json
        """
        return await self._client._invoke("project setup-create", [], [("project", project), ("host", host), ("setup-id", setup_id), ("path", path), ("kind", kind), ("display-name", display_name), ("worktree-base-path", worktree_base_path), ("git-username", git_username), ("state", state), ("method", method)], json=True, remote=True)

    async def setup_delete(
        self,
        *,
        setup: Scalar,
        host: Scalar | None = None,
        force: bool = False,
    ) -> Any:
        """Remove a project host setup.

        CLI: ``orca project setup-delete --setup <setup-id> [--host <host>] [--force] [--json]``

        Notes:
            Independent setups are removed directly.
            Repo-backed setups remove the registered repo compatibility record.
            Refuses while the project has open terminals or saved workspace details; --force removes it anyway.

        Examples:
            orca project setup-delete --setup github:stablyai/orca::gpu --json
        """
        return await self._client._invoke("project setup-delete", [], [("setup", setup), ("host", host), ("force", force)], json=True, remote=True)

    async def setup_existing_folder(
        self,
        *,
        project: Scalar,
        host: Scalar,
        path: Scalar,
        kind: Scalar | None = None,
        display_name: Scalar | None = None,
    ) -> Any:
        """Make a project available on a host by importing an existing folder.

        CLI: ``orca project setup-existing-folder --project <id> --host <host> --path <path> [--kind git|folder] [--display-name <name>] [--json]``

        Notes:
            For remote runtimes, --path must be an absolute path on the remote server.
            --host takes local, ssh:<target-id>, runtime:<environment-id>, or the bare host name `orca host list` prints for any of them.
            SSH targets are set up through the desktop UI because the desktop client owns SSH connections.

        Examples:
            orca project setup-existing-folder --project github:stablyai/orca --host local --path ~/orca
            orca project setup-existing-folder --project github:stablyai/orca --host runtime:03ef704c-b180-4b10-998d-e28fbd5de9a3 --path /home/me/orca --kind git --json
        """
        return await self._client._invoke("project setup-existing-folder", [], [("project", project), ("host", host), ("path", path), ("kind", kind), ("display-name", display_name)], json=True, remote=True)

    async def setup_update(
        self,
        *,
        setup: Scalar,
        host: Scalar | None = None,
        display_name: Scalar | None = None,
        path: Scalar | None = None,
        worktree_base_path: Scalar | None = None,
        git_username: Scalar | None = None,
        kind: Scalar | None = None,
        state: Scalar | None = None,
        method: Scalar | None = None,
    ) -> Any:
        """Update project host setup metadata.

        CLI: ``orca project setup-update --setup <setup-id> [--host <host>] [--display-name <name>] [--path <path>] [--worktree-base-path <path>] [--git-username <name>] [--kind git|folder] [--state ready|not-set-up|setting-up|error|unsupported] [--method legacy-repo|imported-existing-folder|cloned|provisioned] [--json]``

        Notes:
            Repo-backed setups mirror safe fields onto the repo record.
            --host picks the setup when the project is set up on more than one host under the same setup id.
            Path and availability state changes are only supported for independent setup records.

        Examples:
            orca project setup-update --setup github:stablyai/orca::gpu --display-name "GPU VM"
            orca project setup-update --setup github:stablyai/orca::gpu --path /srv/orca --state ready --json
        """
        return await self._client._invoke("project setup-update", [], [("setup", setup), ("host", host), ("display-name", display_name), ("path", path), ("worktree-base-path", worktree_base_path), ("git-username", git_username), ("kind", kind), ("state", state), ("method", method)], json=True, remote=True)

    async def setups(
        self,
        *,
        project: Scalar | None = None,
        host: Scalar | None = None,
    ) -> Any:
        """List project host setups.

        CLI: ``orca project setups [--project <id>] [--host <host>] [--json]``

        Notes:
            A setup means a project is available on a host at a concrete filesystem path.
            --host runtime:<environment-id> runs the command on that paired Orca server instead of filtering this runtime; unknown environment ids are rejected rather than answered with an empty list.
            Run `orca environment list` to see the environment ids that runtime:<environment-id> accepts. It matches ids only, never environment names.
            A routed --host runtime:<id> also lists that server's own local-stamped setups, because both spellings name the machine the command reached.

        Examples:
            orca project setups
            orca project setups --project github:stablyai/orca
            orca project setups --host local
            orca project setups --host runtime:03ef704c-b180-4b10-998d-e28fbd5de9a3
        """
        return await self._client._invoke("project setups", [], [("project", project), ("host", host)], json=True, remote=True)

class AsyncReferenceResource(_AsyncResource):
    """Commands under ``orca reference``."""

    async def add(
        self,
        url: str | Sequence[str],
        *,
        worktree: Scalar,
        reference_site: Scalar | None = None,
    ) -> Any:
        """Attach reviews or issues to a workspace.

        CLI: ``orca reference add <url-or-jira-key>... --worktree <selector> [--reference-site <id>] [--json]``

        Notes:
            Bare keys resolve Jira issues on the selected execution-host Jira site; use --reference-site to choose one explicitly. Other providers require full URLs.
            Existing links are unchanged; all inputs are validated and Jira keys resolved before writing. Full URLs do not require Jira lookup.

        Examples:
            orca reference add https://github.com/acme/api/pull/5123 https://linear.app/acme/issue/STA-1234 --worktree name:api
            orca reference add ENG-123 --reference-site <id> --worktree name:api
        """
        return await self._client._invoke("reference add", [url], [("worktree", worktree), ("reference-site", reference_site)], json=True, remote=True)

    async def find(
        self,
        query: Scalar,
        *,
        worktree: Scalar | None = None,
        repo: Scalar | None = None,
        include_archived: bool = False,
        limit: int | str | None = None,
    ) -> Any:
        """Find workspaces and agents associated with a review or issue.

        CLI: ``orca reference find <url-or-issue-key> [--worktree <selector>|--repo <selector>] [--include-archived] [--limit <n>] [--json]``

        Notes:
            Reads stored references only. Use orca search to search agent conversations.
            Issue keys search every matching source. Bare numbers and custom shorthand are unsupported.
            Returns up to 50 workspaces by default; truncated is true when more match.
            linked means recorded evidence associates that agent with the reference; workspace membership alone does not establish ownership.

        Examples:
            orca reference find STA-1234 --json
        """
        return await self._client._invoke("reference find", [query], [("worktree", worktree), ("repo", repo), ("include-archived", include_archived), ("limit", limit)], json=True, remote=True)

    async def list(
        self,
        *,
        worktree: Scalar,
    ) -> Any:
        """List the reviews and issues attached to a workspace.

        CLI: ``orca reference list --worktree <selector> [--json]``
        """
        return await self._client._invoke("reference list", [], [("worktree", worktree)], json=True, remote=True)

    async def remove(
        self,
        url: str | Sequence[str] | None = None,
        *,
        worktree: Scalar,
        key: Scalar | Sequence[Scalar] | None = None,
    ) -> Any:
        """Detach reviews or issues from a workspace.

        CLI: ``orca reference remove [<url>...] [--key <key>...] --worktree <selector> [--json]``

        Notes:
            Use full URLs, or opaque --key values from reference list for older links without URLs.
            Removing an absent link succeeds without changing the workspace.
        """
        return await self._client._invoke("reference remove", [url], [("worktree", worktree), ("key", key)], json=True, remote=True)

class AsyncRepoResource(_AsyncResource):
    """Commands under ``orca repo``."""

    async def add(
        self,
        *,
        path: Scalar,
    ) -> Any:
        """Add a project to Orca by filesystem path.

        CLI: ``orca repo add --path <path> [--json]``
        """
        return await self._client._invoke("repo add", [], [("path", path)], json=True, remote=True)

    async def list(
        self,
    ) -> Any:
        """List repos registered in Orca.

        CLI: ``orca repo list [--json]``
        """
        return await self._client._invoke("repo list", [], [], json=True, remote=True)

    async def search_refs(
        self,
        *,
        repo: Scalar,
        query: Scalar,
        limit: int | str | None = None,
    ) -> Any:
        """Search branch/tag refs within a repo.

        CLI: ``orca repo search-refs --repo <selector> --query <text> [--limit <n>] [--json]``
        """
        return await self._client._invoke("repo search-refs", [], [("repo", repo), ("query", query), ("limit", limit)], json=True, remote=True)

    async def set(
        self,
        *,
        repo: Scalar,
        external_worktree_visibility: Scalar,
    ) -> Any:
        """Set whether non-Orca worktrees are shown for a repo.

        CLI: ``orca repo set --repo <selector> --external-worktree-visibility show|hide|inherit [--json]``

        Notes:
            show and hide override the global non-Orca worktree visibility default for this repo; inherit clears the override.
            Per-worktree visibility rules still apply.

        Examples:
            orca repo set --repo path:/path/to/repo --external-worktree-visibility show --json
        """
        return await self._client._invoke("repo set", [], [("repo", repo), ("external-worktree-visibility", external_worktree_visibility)], json=True, remote=True)

    async def set_base_ref(
        self,
        *,
        repo: Scalar,
        ref: Scalar,
    ) -> Any:
        """Set the repo's default base ref for future worktrees.

        CLI: ``orca repo set-base-ref --repo <selector> --ref <ref> [--json]``
        """
        return await self._client._invoke("repo set-base-ref", [], [("repo", repo), ("ref", ref)], json=True, remote=True)

    async def show(
        self,
        *,
        repo: Scalar,
    ) -> Any:
        """Show one registered repo.

        CLI: ``orca repo show --repo <selector> [--json]``
        """
        return await self._client._invoke("repo show", [], [("repo", repo)], json=True, remote=True)

class AsyncServeRestoreResource(_AsyncResource):
    """Commands under ``orca serve restore``."""

    async def resume(
        self,
        *,
        page: Scalar | None = None,
    ) -> Any:
        """Resume automatic terminal restores that this host paused.

        CLI: ``orca serve restore resume [--json]``

        Notes:
            After its terminal host stops unexpectedly, or while it is overloaded, Orca keeps restored agent sessions asleep instead of starting them all at once. Each one resumes when you open it.
            This clears that pause so automatic restores start again, within the normal limits. It talks to the Orca running on this machine and never starts a server.
            It also lists restores from an older Orca client that this host refused, with the command that resumes each one.

        Examples:
            orca serve restore resume
            orca serve restore resume --json
        """
        return await self._client._invoke("serve restore resume", [], [("page", page)], json=True, remote=True)

class AsyncServeServiceResource(_AsyncResource):
    """Commands under ``orca serve service``."""

    async def install(
        self,
        *,
        port: int | str | None = None,
        pairing_address: Scalar | None = None,
        command: Scalar | None = None,
        dry_run: bool = False,
        page: Scalar | None = None,
    ) -> Any:
        """Run orca serve as a per-user background service that restarts itself.

        CLI: ``orca serve service install [--port <port>] [--pairing-address <host>] [--command <path>] [--dry-run] [--json]``

        Notes:
            macOS writes a LaunchAgent; Linux writes a systemd user unit. Both run `orca serve --supervise --no-pairing` for this profile, so the server restarts with growing delays and gives up after repeated failures instead of looping.
            The service never prints a pairing link to its log. Pair clients from the desktop app, or with `orca serve` in a terminal while the service is stopped.
            On Linux the service stops at logout unless lingering is on (`loginctl enable-linger`); install reports it.
            Reinstalling replaces the unit and clears a previous give-up. --command defaults to the installed Orca app's `orca` command on PATH (`orca-ide` on Linux) and must not be a launcher tied to one Orca version. --dry-run prints the unit without installing it.
            Needs the Orca app installed on this machine. The `orca` command in an Orca terminal on an SSH host belongs to that connection's server and cannot install a service.
            Not available on Windows yet.

        Examples:
            orca serve service install
            orca serve service install --port 6768 --dry-run
        """
        return await self._client._invoke("serve service install", [], [("port", port), ("pairing-address", pairing_address), ("command", command), ("dry-run", dry_run), ("page", page)], json=True, remote=True)

    async def status(
        self,
        *,
        page: Scalar | None = None,
    ) -> Any:
        """Show whether this profile's orca serve service is running.

        CLI: ``orca serve service status [--json]``

        Notes:
            Reports live, exited, or unverifiable (when the service manager cannot be asked), plus why the supervisor gave up if it did.

        Examples:
            orca serve service status
            orca serve service status --json
        """
        return await self._client._invoke("serve service status", [], [("page", page)], json=True, remote=True)

    async def uninstall(
        self,
        *,
        page: Scalar | None = None,
    ) -> Any:
        """Stop and remove this profile's orca serve service.

        CLI: ``orca serve service uninstall [--json]``

        Notes:
            Stops the service and removes its unit file. The terminal daemon and its sessions keep running.

        Examples:
            orca serve service uninstall
        """
        return await self._client._invoke("serve service uninstall", [], [("page", page)], json=True, remote=True)

class AsyncServeResource(_AsyncResource):
    """Commands under ``orca serve``."""

    @cached_property
    def restore(self) -> AsyncServeRestoreResource:
        """``orca serve restore`` commands."""
        return AsyncServeRestoreResource(self._client)

    @cached_property
    def service(self) -> AsyncServeServiceResource:
        """``orca serve service`` commands."""
        return AsyncServeServiceResource(self._client)

    async def __call__(
        self,
        *,
        port: int | str | None = None,
        pairing_address: Scalar | None = None,
        mobile_pairing: bool = False,
        no_pairing: bool = False,
        grant_desktop_control: bool = False,
        project_root: Scalar | None = None,
        recipe_json: bool = False,
        supervise: bool = False,
        force: bool = False,
        page: Scalar | None = None,
    ) -> Any:
        """Start an Orca runtime server without opening a desktop window.

        CLI: ``orca serve [--port <port>] [--pairing-address <host>] [--mobile-pairing] [--no-pairing] [--grant-desktop-control] [--project-root <path>] [--recipe-json] [--supervise] [--force] [--json]``

        Notes:
            Runs in the foreground and prints the bound endpoint, advertised endpoint, and pairing status. Stop it with Ctrl+C.
            With --port, serve exits with an error when that port is already in use. Without it, serve uses 6768 and moves to another port when 6768 is taken.
            --pairing-address changes only the client-advertised address; use a reachable LAN, Tailscale, SSH-forward, or reverse-proxy endpoint.
            Use --recipe-json with --project-root from VM recipes to print the recipe result JSON and leave the server running.
            Use --mobile-pairing to print a mobile-scoped pairing QR/link instead of the default runtime-environment pairing link.
            A paired client cannot drive this machine's desktop (orca computer) unless the offer was created with --grant-desktop-control.
            When the web client bundle is available, the server also prints a browser URL with the pairing data embedded.
            Exits with code 3, without starting anything, when another Orca already serves this profile or cannot be shown to have stopped.
            On macOS, after Orca serve aborts at startup (it could not register with Launch Services), later runs from the same environment refuse for 30 minutes with exit code 78. Use --force to try anyway.
            --supervise is for service managers (launchd, systemd). Orca serve then restarts the server itself with growing delays instead of exiting when it stops, waits while an update replaces the app, and waits while another Orca serves this profile. After 6 failures in 15 minutes it gives up and exits with code 0 so the manager stops too, and later supervised runs refuse until a new build is installed or --force is passed. Not available on Windows yet.
            Experimental and off by default: set ORCA_TERMINAL_PROCESS_CEILING=<n> (64 or more) before the terminal host starts to have the OS cap how many processes each terminal may run (Linux, through a systemd user scope per terminal, which needs a user manager that outlives logout; Windows, through a job per terminal). `orca serve` reports the ceiling as on or off, with the reason.
            Off by default: set ORCA_TERMINAL_MEMORY_MAX=<size> (256M or more) and ORCA_TERMINAL_MEMORY_SWAP_MAX=<size> (0 for no swap) before the terminal host starts to cap the memory and swap of each terminal on Linux, through the same per-terminal systemd user scope. A terminal over its limit has its largest process OOM-killed; the host and other terminals keep running. Sizes take K, M, G or T. A limit the host cannot enforce is skipped and logged in the terminal host log. No effect on macOS or Windows.

        Examples:
            orca serve
            orca serve --json
            orca serve --project-root /workspace/repo --pairing-address wss://sandbox.example.com --recipe-json
            orca serve --port 6768 --pairing-address 100.64.1.20
            orca serve --pairing-address 100.64.1.20 --mobile-pairing
        """
        return await self._client._invoke("serve", [], [("port", port), ("pairing-address", pairing_address), ("mobile-pairing", mobile_pairing), ("no-pairing", no_pairing), ("grant-desktop-control", grant_desktop_control), ("project-root", project_root), ("recipe-json", recipe_json), ("supervise", supervise), ("force", force), ("page", page)], json=True, remote=True)

class AsyncSetResource(_AsyncResource):
    """Commands under ``orca set``."""

    async def credentials(
        self,
        *,
        user: Scalar,
        pass_: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Set HTTP auth credentials.

        CLI: ``orca set credentials --user <user> --pass <pass> [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("set credentials", [], [("user", user), ("pass", pass_), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def device(
        self,
        *,
        name: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Emulate a device.

        CLI: ``orca set device --name <device> [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("set device", [], [("name", name), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def headers(
        self,
        *,
        headers: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Set extra HTTP headers.

        CLI: ``orca set headers --headers <json> [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("set headers", [], [("headers", headers), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def media(
        self,
        *,
        color_scheme: Scalar | None = None,
        reduced_motion: Scalar | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Set color scheme and reduced motion preferences.

        CLI: ``orca set media [--color-scheme <dark|light>] [--reduced-motion <reduce|no-preference>] [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("set media", [], [("color-scheme", color_scheme), ("reduced-motion", reduced_motion), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def offline(
        self,
        *,
        state: Scalar | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Toggle offline mode.

        CLI: ``orca set offline [--state <on|off>] [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("set offline", [], [("state", state), ("worktree", worktree), ("page", page)], json=True, remote=True)

class AsyncSkillsResource(_AsyncResource):
    """Commands under ``orca skills``."""

    async def get(
        self,
        topic: Scalar,
        *,
        full: bool = False,
        reference: Scalar | None = None,
        references: bool = False,
    ) -> Any:
        """Print a version-matched skill guide as Markdown.

        CLI: ``orca skills get <topic> [--full | --reference <name>] [--json]``

        Notes:
            Reads bundled guide content locally without contacting the Orca runtime.
            Prints the compact guide by default. Use --full to print the full guide with bundled references when provided.
            Use --reference <name> to print one bundled reference alone, which is what an action gate in the compact guide needs; --references lists the available names.
            A reference name may be given bare (recovery-and-cleanup) or as the guide spells it (references/recovery-and-cleanup.md).
            Use --json for a deterministic object containing canonical topic metadata and content.

        Examples:
            orca skills get orca-cli
            orca skills get orchestration --full
            orca skills get orchestration --references
            orca skills get orchestration --reference recovery-and-cleanup
        """
        return await self._client._invoke("skills get", [topic], [("full", full), ("reference", reference), ("references", references)], json=True, remote=True)

    async def install(
        self,
        *,
        skill: Scalar | None = None,
        all: bool = False,
        agent: Scalar | None = None,
        local: bool = False,
        dry_run: bool = False,
    ) -> Any:
        """Install bundled Orca skills via the community skills CLI.

        CLI: ``orca skills install [--skill <name>]... [--all] [--agent <name>[,<name>]] [--local] [--dry-run] [--json]``

        Notes:
            Reads the bundled skill registry locally without contacting the Orca runtime.
            Resolves to the same `npx skills@<pinned> add <repo>/tree/<commit> --skill <name> ...` command used by Orca Settings, pinned to the commit this Orca build was made from, plus the non-interactive flags an unattended host needs (`npx --yes` and `-y`), then runs it and forwards its output and exit code.
            Installs globally (all projects, adds --global) by default. Use --local to install into the current project instead.
            Targets the coding agents Orca detects on this host, plus the shared .agents/skills directory. Without an explicit target the skills CLI installs into every agent it knows about, which litters a host with config directories for agents it does not have.
            Use --agent <name>[,<name>...] to choose targets yourself, or --agent universal for the shared directory alone. Required when Orca detects no agent.
            Use --dry-run to print the resolved command without running it.
            With --json, the skill listing and --dry-run emit JSON; a real install streams npx's own non-JSON output live and rejects --json.
            Omit --skill and --all to list installable skill names.
            Intended for headless hosts (SSH, containers, CI) with no desktop Settings UI to copy the install command from.

        Examples:
            orca skills install
            orca skills install --skill orca-cli --skill orchestration
            orca skills install --skill orca-cli --local
            orca skills install --skill orca-cli --agent claude-code,codex
            orca skills install --all --dry-run
        """
        return await self._client._invoke("skills install", [], [("skill", skill), ("all", all), ("agent", agent), ("local", local), ("dry-run", dry_run)], json=True, remote=True)

    async def installed(
        self,
    ) -> Any:
        """List installed skill selectors.

        CLI: ``orca skills installed [--json]``

        Notes:
            Lists discovery IDs and names without reading skill contents into the CLI.
            Package metadata is validated when the selected skills are shared.
            Use an exact ID or an unambiguous name with `orca skills share --skill <selector>`.
        """
        return await self._client._invoke("skills installed", [], [], json=True, remote=True)

    async def list(
        self,
    ) -> Any:
        """List version-matched skill guides bundled with this Orca CLI.

        CLI: ``orca skills list [--json]``

        Notes:
            Reads bundled guide metadata locally without contacting the Orca runtime.
            With --json, prints a topics array of canonical names and one-line descriptions.
            Use `orca skills get <name>` for the compact guide, `--full` for its full reference package, or `orca skills install` to install skills.
        """
        return await self._client._invoke("skills list", [], [], json=True, remote=True)

    async def share(
        self,
        *,
        skill: Scalar,
        bundle_name: Scalar,
        release_notes: Scalar | None = None,
    ) -> Any:
        """Publish explicitly selected installed skills behind one unlisted link.

        CLI: ``orca skills share --skill <selector> [--skill <selector> ...] --bundle-name <name> [--release-notes <text>] [--json]``

        Notes:
            Requires the default-off permission in Settings → Share Skills.
            The bundle name may be human-readable; Orca converts it to a portable lowercase package name.
            Selectors are exact discovery IDs or unambiguous names from `orca skills installed`.
            Only discovered skill directories can be selected; arbitrary paths and --all are not supported.
            The resulting link is unlisted. Anyone with it can inspect and install the bundle.

        Examples:
            orca skills share --skill frontend --bundle-name "Frontend Skills"
            orca skills share --skill frontend --skill testing --bundle-name "Team Toolkit" --json
        """
        return await self._client._invoke("skills share", [], [("skill", skill), ("bundle-name", bundle_name), ("release-notes", release_notes)], json=True, remote=True)

    async def update(
        self,
        *,
        skill: Scalar | None = None,
        all: bool = False,
        agent: Scalar | None = None,
        local: bool = False,
        dry_run: bool = False,
    ) -> Any:
        """Update Orca skills to the version this Orca build ships.

        CLI: ``orca skills update [--skill <name>]... [--all] [--agent <name>[,<name>]] [--local] [--dry-run] [--json]``

        Notes:
            Reads the bundled skill registry locally without contacting the Orca runtime.
            Runs the same pinned `npx skills add` command as `orca skills install`, which replaces each selected skill with the copy this Orca build ships.
            Updates the global install (all projects, adds --global) by default. Use --local to update the current project instead.
            Targets the same agents as `orca skills install`, or only the shared .agents/skills directory when none is detected; use --agent to choose them yourself.
            Use --dry-run to print the resolved command without running it.
            With --json, the skill listing and --dry-run emit JSON; a real update streams npx's own non-JSON output live and rejects --json.
            Omit --skill and --all to list updatable skill names.
            Intended for headless hosts (SSH, containers, CI) with no desktop Settings UI to copy the update command from.

        Examples:
            orca skills update
            orca skills update --skill orca-cli --skill orchestration
            orca skills update --skill orca-cli --local
            orca skills update --all --dry-run
        """
        return await self._client._invoke("skills update", [], [("skill", skill), ("all", all), ("agent", agent), ("local", local), ("dry-run", dry_run)], json=True, remote=True)

class AsyncSpeechOpenaiKeyResource(_AsyncResource):
    """Commands under ``orca speech openai-key``."""

    async def clear(
        self,
    ) -> Any:
        """Remove the OpenAI key cloud voice dictation uses on this host.

        CLI: ``orca speech openai-key clear [--json]``

        Examples:
            orca speech openai-key clear
        """
        return await self._client._invoke("speech openai-key clear", [], [], json=True, remote=True)

    async def set(
        self,
        *,
        stdin: str | bytes | None = None,
    ) -> Any:
        """Save the OpenAI key cloud voice dictation uses on this host, read from stdin.

        CLI: ``orca speech openai-key set [--json] < key-file``

        Notes:
            Reads the key from stdin so it never lands in shell history or a process list.
            The host that runs dictation seals it, so a headless `orca serve` host can use it.

        Examples:
            printf %s "$OPENAI_API_KEY" | orca speech openai-key set
            $env:OPENAI_API_KEY | orca speech openai-key set
        """
        return await self._client._invoke("speech openai-key set", [], [], json=True, remote=True, stdin=stdin)

    async def status(
        self,
    ) -> Any:
        """Show whether this host has an OpenAI key for cloud voice dictation.

        CLI: ``orca speech openai-key status [--json]``

        Examples:
            orca speech openai-key status --json
        """
        return await self._client._invoke("speech openai-key status", [], [], json=True, remote=True)

class AsyncSpeechResource(_AsyncResource):
    """Commands under ``orca speech``."""

    @cached_property
    def openai_key(self) -> AsyncSpeechOpenaiKeyResource:
        """``orca speech openai-key`` commands."""
        return AsyncSpeechOpenaiKeyResource(self._client)

class AsyncStorageLocalResource(_AsyncResource):
    """Commands under ``orca storage local``."""

    async def clear(
        self,
        *,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Clear all localStorage.

        CLI: ``orca storage local clear [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("storage local clear", [], [("worktree", worktree), ("page", page)], json=True, remote=True)

    async def get(
        self,
        *,
        key: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Get a localStorage value by key.

        CLI: ``orca storage local get --key <key> [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("storage local get", [], [("key", key), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def set(
        self,
        *,
        key: Scalar,
        value: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Set a localStorage value.

        CLI: ``orca storage local set --key <key> --value <value> [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("storage local set", [], [("key", key), ("value", value), ("worktree", worktree), ("page", page)], json=True, remote=True)

class AsyncStorageSessionResource(_AsyncResource):
    """Commands under ``orca storage session``."""

    async def clear(
        self,
        *,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Clear all sessionStorage.

        CLI: ``orca storage session clear [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("storage session clear", [], [("worktree", worktree), ("page", page)], json=True, remote=True)

    async def get(
        self,
        *,
        key: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Get a sessionStorage value by key.

        CLI: ``orca storage session get --key <key> [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("storage session get", [], [("key", key), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def set(
        self,
        *,
        key: Scalar,
        value: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Set a sessionStorage value.

        CLI: ``orca storage session set --key <key> --value <value> [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("storage session set", [], [("key", key), ("value", value), ("worktree", worktree), ("page", page)], json=True, remote=True)

class AsyncStorageResource(_AsyncResource):
    """Commands under ``orca storage``."""

    @cached_property
    def local(self) -> AsyncStorageLocalResource:
        """``orca storage local`` commands."""
        return AsyncStorageLocalResource(self._client)

    @cached_property
    def session(self) -> AsyncStorageSessionResource:
        """``orca storage session`` commands."""
        return AsyncStorageSessionResource(self._client)

class AsyncTabProfileResource(_AsyncResource):
    """Commands under ``orca tab profile``."""

    async def clone(
        self,
        *,
        profile: Scalar,
        page: Scalar | None = None,
        worktree: Scalar | None = None,
    ) -> Any:
        """Clone a browser tab into a different browser profile.

        CLI: ``orca tab profile clone --profile <id> [--page <id>] [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("tab profile clone", [], [("profile", profile), ("page", page), ("worktree", worktree)], json=True, remote=True)

    async def create(
        self,
        *,
        label: Scalar,
        scope: Scalar | None = None,
    ) -> Any:
        """Create a browser session profile for browser tabs.

        CLI: ``orca tab profile create --label <name> [--scope <isolated|imported>] [--json]``
        """
        return await self._client._invoke("tab profile create", [], [("label", label), ("scope", scope)], json=True, remote=True)

    async def delete(
        self,
        *,
        profile: Scalar,
    ) -> Any:
        """Delete a browser session profile used by browser tabs.

        CLI: ``orca tab profile delete --profile <id> [--json]``
        """
        return await self._client._invoke("tab profile delete", [], [("profile", profile)], json=True, remote=True)

    async def list(
        self,
    ) -> Any:
        """List browser session profiles available to browser tabs.

        CLI: ``orca tab profile list [--json]``
        """
        return await self._client._invoke("tab profile list", [], [], json=True, remote=True)

    async def set(
        self,
        *,
        profile: Scalar,
        page: Scalar | None = None,
        worktree: Scalar | None = None,
    ) -> Any:
        """Switch a browser tab to a different browser profile.

        CLI: ``orca tab profile set (--page <id> | --worktree <selector>) --profile <id> [--json]``
        """
        return await self._client._invoke("tab profile set", [], [("profile", profile), ("page", page), ("worktree", worktree)], json=True, remote=True)

    async def show(
        self,
        *,
        page: Scalar,
        worktree: Scalar | None = None,
    ) -> Any:
        """Show the browser profile bound to a tab.

        CLI: ``orca tab profile show --page <id> [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("tab profile show", [], [("page", page), ("worktree", worktree)], json=True, remote=True)

    async def use_default(
        self,
        *,
        page: Scalar,
        worktree: Scalar | None = None,
    ) -> Any:
        """Switch a browser tab back to the default browser profile.

        CLI: ``orca tab profile use-default --page <id> [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("tab profile use-default", [], [("page", page), ("worktree", worktree)], json=True, remote=True)

class AsyncTabResource(_AsyncResource):
    """Commands under ``orca tab``."""

    @cached_property
    def profile(self) -> AsyncTabProfileResource:
        """``orca tab profile`` commands."""
        return AsyncTabProfileResource(self._client)

    async def close(
        self,
        *,
        index: int | str | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Close a browser tab.

        CLI: ``orca tab close [--index <n>] [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("tab close", [], [("index", index), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def create(
        self,
        *,
        url: Scalar | None = None,
        worktree: Scalar | None = None,
        profile: Scalar | None = None,
    ) -> Any:
        """Create a new browser tab in the current worktree.

        CLI: ``orca tab create [--url <url>] [--worktree <selector>] [--profile <id>] [--json]``
        """
        return await self._client._invoke("tab create", [], [("url", url), ("worktree", worktree), ("profile", profile)], json=True, remote=True)

    async def current(
        self,
        *,
        worktree: Scalar | None = None,
    ) -> Any:
        """Show the current browser tab.

        CLI: ``orca tab current [--worktree <selector|all>] [--json]``
        """
        return await self._client._invoke("tab current", [], [("worktree", worktree)], json=True, remote=True)

    async def list(
        self,
        *,
        worktree: Scalar | None = None,
        show_profile: bool = False,
    ) -> Any:
        """List open browser tabs.

        CLI: ``orca tab list [--worktree <selector|all>] [--show-profile] [--json]``
        """
        return await self._client._invoke("tab list", [], [("worktree", worktree), ("show-profile", show_profile)], json=True, remote=True)

    async def show(
        self,
        *,
        page: Scalar,
        worktree: Scalar | None = None,
    ) -> Any:
        """Show one browser tab by page id.

        CLI: ``orca tab show --page <id> [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("tab show", [], [("page", page), ("worktree", worktree)], json=True, remote=True)

    async def switch(
        self,
        *,
        index: int | str | None = None,
        page: Scalar | None = None,
        worktree: Scalar | None = None,
        focus: bool = False,
    ) -> Any:
        """Switch the active browser tab.

        CLI: ``orca tab switch (--index <n> | --page <id>) [--worktree <selector>] [--focus] [--json]``
        """
        return await self._client._invoke("tab switch", [], [("index", index), ("page", page), ("worktree", worktree), ("focus", focus)], json=True, remote=True)

class AsyncTerminalResource(_AsyncResource):
    """Commands under ``orca terminal``."""

    async def close(
        self,
        *,
        terminal: Scalar | None = None,
        tab: bool = False,
        worktree: Scalar | None = None,
        all: bool = False,
    ) -> Any:
        """Close one terminal, its whole tab, or every terminal in a workspace.

        CLI: ``orca terminal close ([--terminal <handle>] [--tab] | --worktree <selector> --all) [--json]``

        Notes:
            Without --all, closes one terminal pane/session; add --tab to close its whole tab.
            With --worktree <selector> --all, stops every terminal process owned by that workspace and durably removes its terminal tabs, layouts, and resume records.
            Use workspace Sleep when the terminals and agent sessions should resume later.

        Examples:
            orca terminal close --terminal term_abc123
            orca terminal close --terminal term_abc123 --tab --json
            orca terminal close --worktree active --all --json
        """
        return await self._client._invoke("terminal close", [], [("terminal", terminal), ("tab", tab), ("worktree", worktree), ("all", all)], json=True, remote=True)

    async def create(
        self,
        *,
        worktree: Scalar | None = None,
        command: Scalar | None = None,
        shell: Scalar | None = None,
        title: Scalar | None = None,
        focus: bool = False,
    ) -> Any:
        """Create a terminal session in the current worktree.

        CLI: ``orca terminal create [--worktree <selector>] [--title <name>] [--command <text>] [--shell <shell>] [--focus] [--json]``

        Notes:
            Creates a visible terminal tab without switching focus when possible; falls back to a background handle if the UI cannot adopt it. Pass --focus to switch to it.
            This creates a terminal and runs --command in it. To start an agent, use `orca agent launch` (or `orca worktree create --agent` for a new checkout), which follows your Chat UI setting.
            --shell picks the shell the terminal IS on a Windows host (cmd.exe, powershell.exe, pwsh.exe, wsl.exe, bash.exe, git-bash); --command is typed into whatever shell the host started, so `--command cmd.exe` leaves a cmd running INSIDE the default shell and exiting it drops back to that shell.
            A host that cannot apply --shell refuses the create rather than quietly spawning its default shell: macOS and Linux execution hosts spawn the login shell, terminals routed over SSH resolve their shell on the SSH host, a --shell that contradicts the project execution runtime (WSL vs Windows host) is refused, and an Orca host older than --shell is refused by the CLI.

        Examples:
            orca terminal create --json
            orca terminal create --worktree active --command "pnpm dev" --json
            orca terminal create --worktree path:/projects/myapp --title "RUNNER" --command "npm test"
            orca terminal create --worktree path:/projects/myapp --command "pnpm dev" --focus
            orca terminal create --worktree path:C:/src/app --shell cmd.exe --json
        """
        return await self._client._invoke("terminal create", [], [("worktree", worktree), ("command", command), ("shell", shell), ("title", title), ("focus", focus)], json=True, remote=True)

    async def list(
        self,
        *,
        worktree: Scalar | None = None,
        limit: int | str | None = None,
        include_visual_layouts: bool = False,
    ) -> Any:
        """List live Orca-managed terminals.

        CLI: ``orca terminal list [--worktree <selector>] [--limit <n>] [--include-visual-layouts] [--json]``

        Notes:
            JSON omits visualLayouts by default; pass --include-visual-layouts when machine-readable tab and pane topology is required.
        """
        return await self._client._invoke("terminal list", [], [("worktree", worktree), ("limit", limit), ("include-visual-layouts", include_visual_layouts)], json=True, remote=True)

    async def read(
        self,
        *,
        terminal: Scalar | None = None,
        cursor: int | str | None = None,
        limit: int | str | None = None,
        screen: bool = False,
    ) -> Any:
        """Read bounded terminal output.

        CLI: ``orca terminal read [--terminal <handle>] [--cursor <n>] [--limit <n>] [--screen] [--json]``

        Notes:
            Omit --terminal to target the active terminal in the current worktree.
            By default this returns accumulated terminal output with escape sequences stripped, not the rendered screen. Any program that repaints a line — shells, progress bars, TUIs — comes back as stacked fragments, so one `clear` keystroke by keystroke reads as `cclclecleaclear`, and spaces a prompt draws by moving the cursor are absent.
            Use --screen to read what the terminal actually renders. Prefer it whenever the answer depends on how output looks rather than what was emitted over time; the default is unsuitable for verifying rendered output.
            The result reports source: stream when it is accumulated output, screen when it is the rendered screen, and screen-unavailable when a screen was asked for but none could be rendered and the accumulated output is being returned instead. An absent source means the host predates the field.
            When present, draft is UI-only composer text excluded from tail; never treat it as terminal output or a submitted instruction.
            --screen and --cursor are mutually exclusive: a screen read is the current frame and has no history to page.
            Use --cursor with the nextCursor value from a previous read to get only new output since that read.
            Use --limit to request more retained lines for long agent responses; output reports oldestCursor when older lines were dropped.
            Useful for capturing the response to a command: read before sending, then read --cursor <prev> after waiting.

        Examples:
            orca terminal read --json
            orca terminal read --terminal term_abc123 --cursor 42 --limit 1000 --json
            orca terminal read --terminal term_abc123 --screen --json
        """
        return await self._client._invoke("terminal read", [], [("terminal", terminal), ("cursor", cursor), ("limit", limit), ("screen", screen)], json=True, remote=True)

    async def rename(
        self,
        *,
        terminal: Scalar | None = None,
        title: Scalar | None = None,
    ) -> Any:
        """Set or clear the title of a terminal tab.

        CLI: ``orca terminal rename [--terminal <handle>] [--title <text>] [--json]``

        Notes:
            Omit --title or pass an empty string to reset to the auto-generated title.

        Examples:
            orca terminal rename --terminal term_abc123 --title "RUNNER"
            orca terminal rename --terminal term_abc123 --json
        """
        return await self._client._invoke("terminal rename", [], [("terminal", terminal), ("title", title)], json=True, remote=True)

    async def send(
        self,
        *,
        terminal: Scalar | None = None,
        text: Scalar | None = None,
        enter: bool = False,
        interrupt: bool = False,
        wait_submit: int | str | None = None,
        retry_request: Scalar | None = None,
    ) -> Any:
        """Send input to a live terminal.

        CLI: ``orca terminal send [--terminal <handle>] [--text <text>] [--enter] [--interrupt] [--wait-submit <seconds>] [--retry-request <id>] [--json]``

        Notes:
            For a text-plus-Enter agent prompt, the result separates input acceptance from observed submission and turn start.
            --wait-submit only observes the accepted prompt for the requested duration; timeout returns the queued/input-accepted receipt and never resends.
            After an ambiguous transport failure, reissue the exact command with the reported --retry-request ID. The ID is bound to the prompt payload and exact terminal process incarnation.
            Older hosts accept the legacy raw input but report provider old-host and do not offer idempotent retry or submission observation.
        """
        return await self._client._invoke("terminal send", [], [("terminal", terminal), ("text", text), ("enter", enter), ("interrupt", interrupt), ("wait-submit", wait_submit), ("retry-request", retry_request)], json=True, remote=True)

    async def set_pane_title(
        self,
        *,
        title: Scalar,
        terminal: Scalar | None = None,
    ) -> Any:
        """Set or clear the title of one terminal pane.

        CLI: ``orca terminal set-pane-title [--terminal <handle>] --title <text> [--json]``

        Notes:
            Sets the title of ONE pane. Split panes share a tab, so terminal rename cannot address one of them; use this command for a single pane.
            Requires the running Orca desktop; headless pane title changes are not supported.
            Pass --title "" to clear the pane back to its automatic title.

        Examples:
            orca terminal set-pane-title --terminal term_abc123 --title "RUNNER"
            orca terminal set-pane-title --terminal term_abc123 --title "" --json
        """
        return await self._client._invoke("terminal set-pane-title", [], [("terminal", terminal), ("title", title)], json=True, remote=True)

    async def show(
        self,
        *,
        terminal: Scalar | None = None,
    ) -> Any:
        """Show terminal metadata and preview.

        CLI: ``orca terminal show [--terminal <handle>] [--json]``
        """
        return await self._client._invoke("terminal show", [], [("terminal", terminal)], json=True, remote=True)

    async def split(
        self,
        *,
        terminal: Scalar | None = None,
        direction: Scalar | None = None,
        command: Scalar | None = None,
    ) -> Any:
        """Split an existing terminal pane.

        CLI: ``orca terminal split [--terminal <handle>] [--direction horizontal|vertical] [--command <text>] [--json]``

        Examples:
            orca terminal split --terminal term_abc123 --direction horizontal --json
            orca terminal split --terminal term_abc123 --command "codex"
        """
        return await self._client._invoke("terminal split", [], [("terminal", terminal), ("direction", direction), ("command", command)], json=True, remote=True)

    async def switch(
        self,
        *,
        terminal: Scalar | None = None,
    ) -> Any:
        """Switch to a terminal tab in the UI.

        CLI: ``orca terminal switch [--terminal <handle>] [--json]``

        Notes:
            With --environment, the desktop app on this machine switches to that server's terminal; a server has no window of its own.

        Examples:
            orca terminal switch --terminal term_abc123
        """
        return await self._client._invoke("terminal switch", [], [("terminal", terminal)], json=True, remote=True)

    async def wait(
        self,
        *,
        for_: Scalar,
        terminal: Scalar | None = None,
        timeout_ms: int | str | None = None,
    ) -> Any:
        """Wait for a terminal condition.

        CLI: ``orca terminal wait [--terminal <handle>] --for exit|tui-idle [--timeout-ms <ms>] [--json]``
        """
        return await self._client._invoke("terminal wait", [], [("terminal", terminal), ("for", for_), ("timeout-ms", timeout_ms)], json=True, remote=True)

class AsyncTerminalDaemonResource(_AsyncResource):
    """Commands under ``orca terminal-daemon``."""

    async def restart(
        self,
        *,
        yes: bool = False,
        page: Scalar | None = None,
    ) -> Any:
        """Restart a terminal daemon whose program files are gone.

        CLI: ``orca terminal-daemon restart --yes [--json]``

        Notes:
            Restarting ENDS every process running in its terminals. Agents that support resume can be resumed afterwards; shells and other jobs must be started again.
            The host re-checks that the daemon is still the one reported by status before stopping it, and refuses otherwise.

        Examples:
            orca terminal-daemon restart --yes
        """
        return await self._client._invoke("terminal-daemon restart", [], [("yes", yes), ("page", page)], json=True, remote=True)

    async def status(
        self,
        *,
        page: Scalar | None = None,
    ) -> Any:
        """Report whether the terminal daemon is running, its process ceiling, and whether it still has its program files.

        CLI: ``orca terminal-daemon status [--json]``

        Notes:
            The daemon is reported live, exited, or unverifiable. Orca starts a new daemon with the next terminal after one exits, so exited between a crash and that terminal is expected.
            For a live daemon it also reports the terminal process ceiling: on with its limit, or off with the reason.
            On Linux AppImage, a daemon started by an earlier Orca can outlive the files it runs from. Orca keeps it so its terminals keep running, but new terminals are not kept across restarts until it is restarted.

        Examples:
            orca terminal-daemon status --json
        """
        return await self._client._invoke("terminal-daemon status", [], [("page", page)], json=True, remote=True)

class AsyncVmRecipeResource(_AsyncResource):
    """Commands under ``orca vm recipe``."""

    async def doctor(
        self,
        recipe_id: Scalar,
        *,
        repo_path: Scalar | None = None,
        provision: bool = False,
        connect: bool = False,
        page: Scalar | None = None,
    ) -> Any:
        """Validate a per-workspace environment recipe without provisioning by default.

        CLI: ``orca vm recipe doctor <recipe-id> [--repo-path <path>] [--provision|--connect] [--json]``

        Notes:
            Reads environmentRecipes from orca.yaml in the repo path, validates the selected recipe, and reports agent-friendly checks.
            This default mode is non-destructive and does not run the recipe command.
            Use --provision or --connect to run the recipe, validate its result, and run cleanup when configured.

        Examples:
            orca vm recipe doctor cloud-sandbox
            orca vm recipe doctor cloud-sandbox --repo-path /path/to/repo --json
            orca vm recipe doctor cloud-sandbox --provision --json
        """
        return await self._client._invoke("vm recipe doctor", [recipe_id], [("repo-path", repo_path), ("provision", provision), ("connect", connect), ("page", page)], json=True, remote=True)

class AsyncVmResource(_AsyncResource):
    """Commands under ``orca vm``."""

    @cached_property
    def recipe(self) -> AsyncVmRecipeResource:
        """``orca vm recipe`` commands."""
        return AsyncVmRecipeResource(self._client)

class AsyncWorktreeResource(_AsyncResource):
    """Commands under ``orca worktree``."""

    async def create(
        self,
        *,
        name: Scalar,
        repo: Scalar | None = None,
        project: Scalar | None = None,
        host: Scalar | None = None,
        project_host_setup: Scalar | None = None,
        agent: Scalar | None = None,
        prompt: Scalar | None = None,
        model: Scalar | None = None,
        effort: Scalar | None = None,
        surface: Scalar | None = None,
        retry_launch: Scalar | None = None,
        base_branch: Scalar | None = None,
        reference: Scalar | Sequence[Scalar] | None = None,
        reference_site: Scalar | None = None,
        issue: int | str | None = None,
        pr: int | str | None = None,
        linear_issue: Scalar | None = None,
        gitlab_issue: Scalar | None = None,
        gitlab_mr: Scalar | None = None,
        comment: Scalar | None = None,
        setup: Scalar | None = None,
        parent_worktree: Scalar | None = None,
        no_parent: bool = False,
        run_hooks: bool = False,
        activate: bool = False,
    ) -> Any:
        """Create a new Orca-managed worktree.

        CLI: ``orca worktree create --name <name> [--repo <selector>|--project <id-or-name> [--host <host>]|--project-host-setup <id>] [--agent <id>] [--prompt <text>] [--model <id>] [--effort <level>] [--surface chat|terminal] [--setup run|skip|inherit] [--base-branch <ref>] [--reference <url-or-jira-key>...] [--reference-site <id>] [--issue <number>] [--pr <number>] [--linear-issue <identifier-or-url>] [--gitlab-issue <number-or-url>] [--gitlab-mr <number-or-url>] [--comment <text>] [--parent-worktree <selector>] [--no-parent] [--run-hooks] [--activate] [--retry-launch <operationId>] [--json]``

        Notes:
            Repeat --reference to attach full issue or review URLs, or Jira issue keys, before setup or agent startup. Use --reference-site to choose the Jira site for keys. Other providers require full URLs. Cannot combine with legacy link flags.
            This creates a new checkout. For a fresh agent in an existing worktree, use `orca agent launch` instead.
            By default, Orca records the new worktree as a child of the caller context when it can infer one from the Orca terminal or current directory.
            If --repo is omitted, Orca infers the repo from the current Orca-managed worktree.
            Use --project to create on a ready project host setup without spelling the backing repo id. --project takes the project id or the display name from `orca project list`.
            --host is only needed when the project is set up on more than one host; with a single setup Orca uses it. When it is ambiguous the error names every host the project is set up on.
            --host takes local, ssh:<target-id>, runtime:<environment-id>, or the bare host name `orca host list` prints for any of them.
            For related work, use the inferred parent or pass --parent-worktree active, folder:<id>, or worktree:<worktreeId> to make the relationship explicit. Worktree ids are the full <repo-id>::<path> values returned by `orca worktree list --json`.
            Use --no-parent when the new worktree should be independent of the current context.
            --no-parent only affects Orca lineage; omit --base-branch to use the repo default base, or pass the default base ref explicitly for independent top-level work.
            By default this creates the worktree and its first terminal without switching the active Orca view.
            Pass --agent to start an agent with the worktree, as a chat or a terminal per your Chat UI setting, exactly as a new agent tab does; --prompt sends initial work to it. --model and --effort pick its model and reasoning effort, and --surface chat|terminal picks chat or terminal for this launch instead of your setting.
            After a lost agent launch reply, re-issue the same command from the same directory on the same host with --retry-launch <operationId> from the error. Never retry as a fresh launch; older hosts require inspecting the workspace first.
            With --agent --json, result.launch says what started: launch.outcome.kind (structured chat or terminal), launch.outcome.handle, and launch.receipt.detail for why. An Orca host older than this returns the terminal agent handle in result.agentTerminalHandle instead.
            Repo-defined setup hooks follow the repository setup policy; pass --setup run to force them.
            Pass --activate when the CLI caller intentionally wants to reveal the new worktree in the app.
            Passing --run-hooks is kept as a legacy alias for --setup run and reveals the worktree.
            Use --pr for GitHub pull requests; --gitlab-issue and --gitlab-mr write separate GitLab links. GitLab URLs must match the stored source project or remote; they cannot select a foreign project.

        Examples:
            orca worktree create --name agent-task --agent codex --prompt "hi" --json
            orca worktree create --name design --no-parent --agent codex --model gpt-6-astra --effort high --prompt "Write the design doc" --json
            orca worktree create --repo id:<repoId> --name related-task --json
            orca worktree create --project github:stablyai/orca --host runtime:03ef704c-b180-4b10-998d-e28fbd5de9a3 --name benchmark --json
            orca worktree create --repo id:<repoId> --name linear-task --linear-issue https://linear.app/stably/issue/STA-335/test-issue --json
            orca worktree create --repo id:<repoId> --name agent-task --agent codex --prompt "hi" --json
            orca worktree create --repo id:<repoId> --name folder-child --parent-worktree folder:<folderId> --json
            orca worktree create --repo id:<repoId> --name related-task --parent-worktree active --json
            orca worktree create --repo id:<repoId> --name independent-task --no-parent --json
        """
        return await self._client._invoke("worktree create", [], [("repo", repo), ("project", project), ("host", host), ("project-host-setup", project_host_setup), ("name", name), ("agent", agent), ("prompt", prompt), ("model", model), ("effort", effort), ("surface", surface), ("retry-launch", retry_launch), ("base-branch", base_branch), ("reference", reference), ("reference-site", reference_site), ("issue", issue), ("pr", pr), ("linear-issue", linear_issue), ("gitlab-issue", gitlab_issue), ("gitlab-mr", gitlab_mr), ("comment", comment), ("setup", setup), ("parent-worktree", parent_worktree), ("no-parent", no_parent), ("run-hooks", run_hooks), ("activate", activate)], json=True, remote=True)

    async def current(
        self,
    ) -> Any:
        """Show the Orca-managed worktree for the current directory.

        CLI: ``orca worktree current [--json]``

        Notes:
            Resolves the current shell directory to a path: selector so agents can target the enclosing Orca worktree without spelling out $PWD.

        Examples:
            orca worktree current
            orca worktree current --json
        """
        return await self._client._invoke("worktree current", [], [], json=True, remote=True)

    async def list(
        self,
        *,
        repo: Scalar | None = None,
        limit: int | str | None = None,
    ) -> Any:
        """List Orca-managed worktrees.

        CLI: ``orca worktree list [--repo <selector>] [--limit <n>] [--json]``

        Notes:
            Each row carries the execution host that owns it (`host=`), and the trailing `scope:` line names every host the page covers plus the ones it does not.
            A host named under `not covered` may still have workspaces; an empty answer for it is not evidence that it has none. A paired server is annotated with the `--environment` flag that reaches it; this machine and its SSH targets are reached through the same runtime, so no flag selects them.
            The row cap is shared across hosts, so a host whose rows sort last is not starved out of the page.
        """
        return await self._client._invoke("worktree list", [], [("repo", repo), ("limit", limit)], json=True, remote=True)

    async def ps(
        self,
        *,
        limit: int | str | None = None,
    ) -> Any:
        """Show a compact orchestration summary across worktrees.

        CLI: ``orca worktree ps [--limit <n>] [--json]``

        Notes:
            Each row carries the execution host that owns it (`host=`), and the trailing `scope:` line names every host the page covers plus the ones it does not.
            A host named under `not covered` may still have workspaces; an empty answer for it is not evidence that it has none. A paired server is annotated with the `--environment` flag that reaches it; this machine and its SSH targets are reached through the same runtime, so no flag selects them.
            The row cap is shared across hosts, so a host whose rows sort last is not starved out of the page.
        """
        return await self._client._invoke("worktree ps", [], [("limit", limit)], json=True, remote=True)

    async def rm(
        self,
        *,
        worktree: Scalar,
        force: bool = False,
        run_hooks: bool = False,
        allow_failed_archive_hook: bool = False,
    ) -> Any:
        """Remove a worktree from Orca and git.

        CLI: ``orca worktree rm --worktree <selector> [--force] [--run-hooks] [--allow-failed-archive-hook] [--json]``

        Notes:
            Repo-defined orca.yaml archive hooks are skipped unless --run-hooks is passed.
            With --run-hooks, a failed archive hook blocks the removal: nothing is stopped, deleted or deregistered, and the command exits non-zero with error code worktree_archive_hook_failed. --force does not waive this.
            Pass --allow-failed-archive-hook to delete anyway after the hook has run and failed; the waived failure is reported back on result.archiveHookOverride. It requires --run-hooks and is rejected without it, because with no hook running there is no failure to waive.
            For Git worktrees, removal also attempts to delete the checked-out local branch, with or without --force. Orca retains branches it knows predated the worktree and any branch whose changes it cannot prove are already merged.
        """
        return await self._client._invoke("worktree rm", [], [("worktree", worktree), ("force", force), ("run-hooks", run_hooks), ("allow-failed-archive-hook", allow_failed_archive_hook)], json=True, remote=True)

    async def set(
        self,
        *,
        worktree: Scalar,
        display_name: Scalar | None = None,
        issue: Scalar | None = None,
        pr: Scalar | None = None,
        linear_issue: Scalar | None = None,
        gitlab_issue: Scalar | None = None,
        gitlab_mr: Scalar | None = None,
        comment: Scalar | None = None,
        workspace_status: Scalar | None = None,
        unread: bool = False,
        read: bool = False,
        parent_worktree: Scalar | None = None,
        no_parent: bool = False,
    ) -> Any:
        """Update Orca metadata for a worktree.

        CLI: ``orca worktree set --worktree <selector> [--display-name <name>] [--issue <number|null>] [--pr <number|null>] [--linear-issue <identifier-or-url|null>] [--gitlab-issue <number-or-url|null>] [--gitlab-mr <number-or-url|null>] [--comment <text>] [--workspace-status <id>] [--unread|--read] [--parent-worktree <selector>|--no-parent] [--json]``

        Notes:
            Workspace status ids match the board columns (defaults: todo, in-progress, in-review, completed); custom statuses use their configured id.
            Pass --linear-issue null to clear the Linear issue link.
            Pass --pr null, --gitlab-issue null, or --gitlab-mr null to clear only the matching link.
            Each link flag updates its own field and leaves unrelated links unchanged. GitLab URLs must match the stored source project or remote; they cannot select a foreign project.

        Examples:
            orca worktree set --worktree active --linear-issue STA-335 --json
            orca worktree set --worktree active --linear-issue null --json
            orca worktree set --worktree active --workspace-status in-review --unread --json
        """
        return await self._client._invoke("worktree set", [], [("worktree", worktree), ("display-name", display_name), ("issue", issue), ("pr", pr), ("linear-issue", linear_issue), ("gitlab-issue", gitlab_issue), ("gitlab-mr", gitlab_mr), ("comment", comment), ("workspace-status", workspace_status), ("unread", unread), ("read", read), ("parent-worktree", parent_worktree), ("no-parent", no_parent)], json=True, remote=True)

    async def show(
        self,
        *,
        worktree: Scalar,
    ) -> Any:
        """Show one worktree.

        CLI: ``orca worktree show --worktree <selector> [--json]``
        """
        return await self._client._invoke("worktree show", [], [("worktree", worktree)], json=True, remote=True)

class AsyncOrcaCommands(_AsyncRoot):
    """All Orca CLI commands."""

    @cached_property
    def account(self) -> AsyncAccountResource:
        """``orca account`` commands."""
        return AsyncAccountResource(self._client)

    @cached_property
    def agent(self) -> AsyncAgentResource:
        """``orca agent`` commands."""
        return AsyncAgentResource(self._client)

    @cached_property
    def artifacts(self) -> AsyncArtifactsResource:
        """``orca artifacts`` commands."""
        return AsyncArtifactsResource(self._client)

    @cached_property
    def automations(self) -> AsyncAutomationsResource:
        """``orca automations`` commands."""
        return AsyncAutomationsResource(self._client)

    @cached_property
    def browser(self) -> AsyncBrowserResource:
        """``orca browser`` commands."""
        return AsyncBrowserResource(self._client)

    @cached_property
    def capture(self) -> AsyncCaptureResource:
        """``orca capture`` commands."""
        return AsyncCaptureResource(self._client)

    @cached_property
    def clipboard(self) -> AsyncClipboardResource:
        """``orca clipboard`` commands."""
        return AsyncClipboardResource(self._client)

    @cached_property
    def computer(self) -> AsyncComputerResource:
        """``orca computer`` commands."""
        return AsyncComputerResource(self._client)

    @cached_property
    def cookie(self) -> AsyncCookieResource:
        """``orca cookie`` commands."""
        return AsyncCookieResource(self._client)

    @cached_property
    def diagnostics(self) -> AsyncDiagnosticsResource:
        """``orca diagnostics`` commands."""
        return AsyncDiagnosticsResource(self._client)

    @cached_property
    def dialog(self) -> AsyncDialogResource:
        """``orca dialog`` commands."""
        return AsyncDialogResource(self._client)

    @cached_property
    def emulator(self) -> AsyncEmulatorResource:
        """``orca emulator`` commands."""
        return AsyncEmulatorResource(self._client)

    @cached_property
    def environment(self) -> AsyncEnvironmentResource:
        """``orca environment`` commands."""
        return AsyncEnvironmentResource(self._client)

    @cached_property
    def file(self) -> AsyncFileResource:
        """``orca file`` commands."""
        return AsyncFileResource(self._client)

    @cached_property
    def host(self) -> AsyncHostResource:
        """``orca host`` commands."""
        return AsyncHostResource(self._client)

    @cached_property
    def intercept(self) -> AsyncInterceptResource:
        """``orca intercept`` commands."""
        return AsyncInterceptResource(self._client)

    @cached_property
    def jira(self) -> AsyncJiraResource:
        """``orca jira`` commands."""
        return AsyncJiraResource(self._client)

    @cached_property
    def linear(self) -> AsyncLinearResource:
        """``orca linear`` commands."""
        return AsyncLinearResource(self._client)

    @cached_property
    def mouse(self) -> AsyncMouseResource:
        """``orca mouse`` commands."""
        return AsyncMouseResource(self._client)

    @cached_property
    def orchestration(self) -> AsyncOrchestrationResource:
        """``orca orchestration`` commands."""
        return AsyncOrchestrationResource(self._client)

    @cached_property
    def profile(self) -> AsyncProfileResource:
        """``orca profile`` commands."""
        return AsyncProfileResource(self._client)

    @cached_property
    def project(self) -> AsyncProjectResource:
        """``orca project`` commands."""
        return AsyncProjectResource(self._client)

    @cached_property
    def reference(self) -> AsyncReferenceResource:
        """``orca reference`` commands."""
        return AsyncReferenceResource(self._client)

    @cached_property
    def repo(self) -> AsyncRepoResource:
        """``orca repo`` commands."""
        return AsyncRepoResource(self._client)

    @cached_property
    def serve(self) -> AsyncServeResource:
        """``orca serve`` commands."""
        return AsyncServeResource(self._client)

    @cached_property
    def set(self) -> AsyncSetResource:
        """``orca set`` commands."""
        return AsyncSetResource(self._client)

    @cached_property
    def skills(self) -> AsyncSkillsResource:
        """``orca skills`` commands."""
        return AsyncSkillsResource(self._client)

    @cached_property
    def speech(self) -> AsyncSpeechResource:
        """``orca speech`` commands."""
        return AsyncSpeechResource(self._client)

    @cached_property
    def storage(self) -> AsyncStorageResource:
        """``orca storage`` commands."""
        return AsyncStorageResource(self._client)

    @cached_property
    def tab(self) -> AsyncTabResource:
        """``orca tab`` commands."""
        return AsyncTabResource(self._client)

    @cached_property
    def terminal(self) -> AsyncTerminalResource:
        """``orca terminal`` commands."""
        return AsyncTerminalResource(self._client)

    @cached_property
    def terminal_daemon(self) -> AsyncTerminalDaemonResource:
        """``orca terminal-daemon`` commands."""
        return AsyncTerminalDaemonResource(self._client)

    @cached_property
    def vm(self) -> AsyncVmResource:
        """``orca vm`` commands."""
        return AsyncVmResource(self._client)

    @cached_property
    def worktree(self) -> AsyncWorktreeResource:
        """``orca worktree`` commands."""
        return AsyncWorktreeResource(self._client)

    async def agent_context(
        self,
    ) -> Any:
        """Print the machine-readable command schema for agents.

        CLI: ``orca agent-context [--json]``

        Notes:
            Pure local read of the command registry — works without a running Orca app, so it is safe over SSH and in headless contexts.

        Examples:
            orca agent-context --json
        """
        return await self._client._invoke("agent-context", [], [], json=True, remote=True)

    async def back(
        self,
        *,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Navigate back in browser history.

        CLI: ``orca back [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("back", [], [("worktree", worktree), ("page", page)], json=True, remote=True)

    async def check(
        self,
        *,
        element: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Check a checkbox/radio by ref.

        CLI: ``orca check --element <ref> [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("check", [], [("element", element), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def claude_teams(
        self,
        *args: str,
    ) -> Any:
        """Start Claude Code Agent Teams in the current Orca terminal.

        CLI: ``orca claude-teams [claude args...]``

        Notes:
            Passes all following arguments through to Claude Code after enabling Agent Teams native panes.
            Must be run from inside an Orca terminal. Starts Claude Code Agent Teams in the current pane and opens teammates as native Orca splits.

        Examples:
            orca claude-teams
            orca claude-teams --resume <session-id>
        """
        return await self._client._invoke("claude-teams", list(args), [], json=False, remote=False)

    async def clear(
        self,
        *,
        element: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Clear an input element by ref.

        CLI: ``orca clear --element <ref> [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("clear", [], [("element", element), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def click(
        self,
        *,
        element: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Click a browser element by ref.

        CLI: ``orca click --element <ref> [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("click", [], [("element", element), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def console(
        self,
        *,
        limit: int | str | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Show captured console log entries.

        CLI: ``orca console [--limit <n>] [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("console", [], [("limit", limit), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def dblclick(
        self,
        *,
        element: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Double-click element by ref.

        CLI: ``orca dblclick --element <ref> [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("dblclick", [], [("element", element), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def download(
        self,
        *,
        selector: Scalar,
        path: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Download a file by clicking a selector.

        CLI: ``orca download --selector <ref> --path <path> [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("download", [], [("selector", selector), ("path", path), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def drag(
        self,
        *,
        from_: Scalar,
        to: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Drag from one element to another.

        CLI: ``orca drag --from <ref> --to <ref> [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("drag", [], [("from", from_), ("to", to), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def eval(
        self,
        *,
        expression: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Evaluate JavaScript in the browser page context.

        CLI: ``orca eval --expression <js> [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("eval", [], [("expression", expression), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def exec(
        self,
        *,
        command: bool = False,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Run any agent-browser command against the active browser tab.

        CLI: ``orca exec --command "<agent-browser command>" [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("exec", [], [("command", command), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def fill(
        self,
        *,
        element: Scalar,
        value: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Clear and fill a browser input by ref.

        CLI: ``orca fill --element <ref> --value <text> [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("fill", [], [("element", element), ("value", value), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def find(
        self,
        *,
        locator: Scalar,
        value: Scalar,
        action: Scalar,
        text: Scalar | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Find element by semantic locator and perform action.

        CLI: ``orca find --locator <type> --value <text> --action <action> [--text <text>] [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("find", [], [("locator", locator), ("value", value), ("action", action), ("text", text), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def focus(
        self,
        *,
        element: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Focus a browser element by ref.

        CLI: ``orca focus --element <ref> [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("focus", [], [("element", element), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def forward(
        self,
        *,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Navigate forward in browser history.

        CLI: ``orca forward [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("forward", [], [("worktree", worktree), ("page", page)], json=True, remote=True)

    async def full_screenshot(
        self,
        *,
        format: Scalar | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Capture a full-page screenshot (beyond viewport).

        CLI: ``orca full-screenshot [--format <png|jpeg>] [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("full-screenshot", [], [("format", format), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def geolocation(
        self,
        *,
        latitude: int | str,
        longitude: int | str,
        accuracy: int | str | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Override browser geolocation.

        CLI: ``orca geolocation --latitude <lat> --longitude <lon> [--accuracy <n>] [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("geolocation", [], [("latitude", latitude), ("longitude", longitude), ("accuracy", accuracy), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def get(
        self,
        *,
        what: Scalar,
        element: Scalar | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Get element property (text, html, value, url, title, count, box).

        CLI: ``orca get --what <property> [--element <ref>] [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("get", [], [("what", what), ("element", element), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def goto(
        self,
        *,
        url: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Navigate the active browser tab to a URL.

        CLI: ``orca goto --url <url> [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("goto", [], [("url", url), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def highlight(
        self,
        *,
        selector: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Highlight an element by selector.

        CLI: ``orca highlight --selector <ref> [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("highlight", [], [("selector", selector), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def hover(
        self,
        *,
        element: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Hover over a browser element by ref.

        CLI: ``orca hover --element <ref> [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("hover", [], [("element", element), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def inserttext(
        self,
        *,
        text: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Insert text without key events.

        CLI: ``orca inserttext --text <text> [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("inserttext", [], [("text", text), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def is_(
        self,
        *,
        what: Scalar,
        element: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Check element state (visible, enabled, checked).

        CLI: ``orca is --what <state> --element <ref> [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("is", [], [("what", what), ("element", element), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def keypress(
        self,
        *,
        key: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Press a key (Enter, Tab, Escape, ArrowDown, etc.).

        CLI: ``orca keypress --key <name> [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("keypress", [], [("key", key), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def network(
        self,
        *,
        limit: int | str | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Show captured network requests.

        CLI: ``orca network [--limit <n>] [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("network", [], [("limit", limit), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def open(
        self,
    ) -> Any:
        """Launch Orca and wait for the runtime to be reachable.

        CLI: ``orca open [--json]``

        Examples:
            orca open
            orca open --json
        """
        return await self._client._invoke("open", [], [], json=True, remote=True)

    async def open_url(
        self,
        *,
        url: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Open a URL on the paired client that hosts this terminal.

        CLI: ``orca open-url --url <url> [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("open-url", [], [("url", url), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def pdf(
        self,
        *,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Export the active browser tab as PDF.

        CLI: ``orca pdf [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("pdf", [], [("worktree", worktree), ("page", page)], json=True, remote=True)

    async def reload(
        self,
        *,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Reload the active browser tab.

        CLI: ``orca reload [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("reload", [], [("worktree", worktree), ("page", page)], json=True, remote=True)

    async def screenshot(
        self,
        *,
        format: Scalar | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Capture a viewport screenshot of the active browser tab.

        CLI: ``orca screenshot [--format <png|jpeg>] [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("screenshot", [], [("format", format), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def scroll(
        self,
        *,
        direction: Scalar,
        amount: int | str | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Scroll the browser viewport.

        CLI: ``orca scroll --direction <up|down> [--amount <pixels>] [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("scroll", [], [("direction", direction), ("amount", amount), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def scrollintoview(
        self,
        *,
        element: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Scroll element into view.

        CLI: ``orca scrollintoview --element <ref> [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("scrollintoview", [], [("element", element), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def search(
        self,
        query: Scalar | None = None,
        *,
        scope: Scalar | None = None,
        fresh: bool = False,
        limit: int | str | None = None,
        cursor: Scalar | None = None,
        agent: Scalar | Sequence[Scalar] | None = None,
        path: Scalar | Sequence[Scalar] | None = None,
        since: Scalar | None = None,
        sort: Scalar | None = None,
        debug: bool = False,
        index_status: bool = False,
    ) -> Any:
        """Search the full text of agent sessions indexed on the selected Orca host.

        CLI: ``orca search <query> [--scope conversation|all] [--fresh] [--limit <n>] [--cursor <c>] [--agent <id>] [--path <p>] [--since <iso>] [--sort relevance|newest] [--debug] [--json]``

        Notes:
            Searches one host: this machine, or the paired Orca server named by --environment / --pairing-code. There is no all-computers search.
            In an Orca SSH terminal, the forwarded CLI searches the controlling Orca runtime by default. Use --environment / --pairing-code to select a paired server; --path only filters results on the selected runtime.
            Quote a multi-word query, or pass it as --query "<text>"; unquoted words are read as command names.
            --scope conversation searches user and assistant turns only; --scope all (the default) also searches commands and tool output.
            --fresh waits up to five seconds for the host to reconcile its index before searching, then searches anyway.
            --agent and --path may be repeated. --path is a literal execution-host path and is not expanded or resolved against the current directory.
            --since takes an ISO 8601 timestamp with an offset, for example 2026-08-01T00:00:00Z.
            --limit is per page (default 20, maximum 100). Pass the printed cursor back with --cursor to read the next page.
            A cursor belongs to one query on one host. Change the query, the filters, or the host and the cursor stops being valid.
            Resume commands and source paths are printed only for a host on this machine; a paired server withholds them.
            --json prints the runtime response envelope with the search contract answer under `result`.

        Examples:
            orca search "strict mode violation getByRole"
            orca search resolveTerminalPath --agent claude --sort newest
            orca search "kernel panic" --path /Users/me/orca --since 2026-08-01T00:00:00Z --json
            orca search "kernel panic" --limit 50 --cursor eyJ2IjoxfQ
            orca search --index-status
            orca search "flaky test" --environment build-server
        """
        return await self._client._invoke("search", [query], [("scope", scope), ("fresh", fresh), ("limit", limit), ("cursor", cursor), ("agent", agent), ("path", path), ("since", since), ("sort", sort), ("debug", debug), ("index-status", index_status)], json=True, remote=True)

    async def select(
        self,
        *,
        element: Scalar,
        value: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Select a dropdown option by ref.

        CLI: ``orca select --element <ref> --value <value> [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("select", [], [("element", element), ("value", value), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def select_all(
        self,
        *,
        element: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Select all text in an input by ref.

        CLI: ``orca select-all --element <ref> [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("select-all", [], [("element", element), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def snapshot(
        self,
        *,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Capture an accessibility snapshot of the active browser tab.

        CLI: ``orca snapshot [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("snapshot", [], [("worktree", worktree), ("page", page)], json=True, remote=True)

    async def status(
        self,
    ) -> Any:
        """Show app/runtime/graph readiness.

        CLI: ``orca status [--json]``

        Notes:
            caller.orcaSessionId is this agent's Orca session ID, as Orca resolved it, when the agent runs as an Orca session; otherwise caller is omitted.

        Examples:
            orca status
            orca status --json
        """
        return await self._client._invoke("status", [], [], json=True, remote=True)

    async def type(
        self,
        *,
        input: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Type text at the current browser focus.

        CLI: ``orca type --input <text> [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("type", [], [("input", input), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def uncheck(
        self,
        *,
        element: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Uncheck a checkbox/radio by ref.

        CLI: ``orca uncheck --element <ref> [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("uncheck", [], [("element", element), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def upload(
        self,
        *,
        element: Scalar,
        files: Scalar,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Upload files to a file input element.

        CLI: ``orca upload --element <ref> --files <path,...> [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("upload", [], [("element", element), ("files", files), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def viewport(
        self,
        *,
        width: int | str,
        height: int | str,
        scale: int | str | None = None,
        mobile: bool = False,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Set browser viewport size.

        CLI: ``orca viewport --width <w> --height <h> [--scale <n>] [--mobile] [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("viewport", [], [("width", width), ("height", height), ("scale", scale), ("mobile", mobile), ("worktree", worktree), ("page", page)], json=True, remote=True)

    async def wait(
        self,
        *,
        selector: Scalar | None = None,
        timeout: int | str | None = None,
        text: Scalar | None = None,
        url: Scalar | None = None,
        load: Scalar | None = None,
        fn: Scalar | None = None,
        state: Scalar | None = None,
        worktree: Scalar | None = None,
        page: Scalar | None = None,
    ) -> Any:
        """Wait for element, text, URL, load state, JS condition, or timeout.

        CLI: ``orca wait [--selector <sel>] [--timeout <ms>] [--text <text>] [--url <pattern>] [--load <state>] [--fn <js>] [--state <hidden|visible>] [--worktree <selector>] [--json]``
        """
        return await self._client._invoke("wait", [], [("selector", selector), ("timeout", timeout), ("text", text), ("url", url), ("load", load), ("fn", fn), ("state", state), ("worktree", worktree), ("page", page)], json=True, remote=True)
