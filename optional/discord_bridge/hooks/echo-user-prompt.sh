#!/usr/bin/env bash
# UserPromptSubmit hook: mirror prompts typed in the terminal to the channel as "**$USER_LABEL:** ...",
# so the channel carries both sides. Skips prompts that came FROM the channel (a speaker prefix or
# "[discord]" within the first 16 characters), machine prompts, and agent messages. Needs jq.
IN=$(cat)
HERE=$(cd "$(dirname "$0")" && pwd)
ROOT=${HARNESS_ROOT:-}
CWD=$(jq -r '.cwd // empty' <<<"$IN" 2>/dev/null)
[ -n "$ROOT" ] && case "$CWD" in "$ROOT"|"$ROOT"/*) ;; *) exit 0 ;; esac
P=$(jq -r '.prompt // empty' <<<"$IN")
[ -n "$P" ] || exit 0
UL=${USER_LABEL:-User}
HEAD16=${P:0:16}
case "$HEAD16" in *"$UL:"*|*"[discord]"*) exit 0 ;; esac
for N in ${CHANNEL_SPEAKERS:-}; do case "$HEAD16" in *"$N:"*) exit 0 ;; esac; done
case "$P" in
  "[cron]"*|"[SYSTEM"*|"<task-notification>"*|*"task-notification"*|"Sentinel check"*|*"status cron"*) exit 0 ;;
  *"<agent-message"*|"Another Claude session"*|*"<cross-session-message"*|"<system-reminder"*|*"[Subagent hand-back]"*) exit 0 ;;
esac
[ ${#P} -gt 1500 ] && exit 0
printf '**%s:** %s' "$UL" "${P:0:1500}" | "$HERE/../discord-notify" >/dev/null 2>&1 || true
exit 0
