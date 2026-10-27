#!/usr/bin/env bash
# Stop hook: post the lead's final text to the channel when the turn was STARTED by a human message.
# Turns started by a cron, a task notification or a system message stay silent (answer those with
# discord-notify yourself). Gate: the hook's cwd is under $HARNESS_ROOT. Dedupe by md5 so a flush race
# never posts the same answer twice. Needs jq.
IN=$(cat)
HERE=$(cd "$(dirname "$0")" && pwd)
ROOT=${HARNESS_ROOT:-}
CWD=$(jq -r '.cwd // empty' <<<"$IN" 2>/dev/null)
[ -n "$ROOT" ] && case "$CWD" in "$ROOT"|"$ROOT"/*) ;; *) exit 0 ;; esac
TP=$(jq -r '.transcript_path // empty' <<<"$IN")
[ -f "$TP" ] || exit 0
LOG="$HERE/stop_post_reply.log"
HF="$HERE/.stop_post_reply_last"
LAM=$(jq -r '.last_assistant_message // empty' <<<"$IN" 2>/dev/null)
# wait until the transcript stops growing (up to 20 s): long final messages lag the Stop event
for _ in $(seq 1 10); do
  S1=$(stat -c %s "$TP"); sleep 2; S2=$(stat -c %s "$TP")
  [ "$S1" = "$S2" ] && break
done
# the row that STARTED the turn decides: the last user row with text content
LASTS=$(tail -400 "$TP" | jq -rs '
  [ .[] | select(.type=="user")
        | (.message.content | if type=="string" then . else ([.[]? | select(.type=="text") | .text] | join("")) end)
        | select(length>0) ] | last // ""')
case "$LASTS" in
  "<task-notification>"*|*"task-notification"*|"[cron]"*|"[SYSTEM"*|"<system-reminder"*|"Sentinel check"*|*"status cron"*) exit 0 ;;
  *"<agent-message"*|"Another Claude session"*|*"<cross-session-message"*) exit 0 ;;
esac
REPLY=$(tail -400 "$TP" | jq -rs '
  [ .[] | select(.type=="assistant")
        | ([.message.content[]? | select(.type=="text") | .text] | join("\n"))
        | select(length>0) ] | last // ""')
[ -n "$LAM" ] && REPLY="$LAM"
[ -n "$REPLY" ] || exit 0
H=$(printf '%s' "$REPLY" | md5sum | cut -d' ' -f1)
if [ -f "$HF" ] && [ "$(cat "$HF")" = "$H" ]; then
  echo "$(date -u +%H:%M) dedupe-exit ${H:0:8}" >> "$LOG"; exit 0
fi
echo "$(date -u +%H:%M) posting ${H:0:8}" >> "$LOG"
printf '%s' "$H" > "$HF"
printf '%s' "$REPLY" | "$HERE/../discord-notify" >/dev/null 2>&1 || echo "$(date -u +%H:%M) post failed" >> "$LOG"
exit 0
