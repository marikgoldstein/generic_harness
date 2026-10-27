#!/usr/bin/env bash
# queue_line_check.sh QUEUE.txt 'TAG|DIR|SCRIPT|NOTE' : verify a queue line BEFORE appending it.
# Checks: exactly 3 bars; tag not already in the queue; no SUBMITTED/done_<TAG>; dir and script exist;
# bash -n on the script; a README_<TAG>.md in the dir with a MEASURED line; no removal words in the
# package's scripts. Prints OK or the failing checks; exit 1 on any failure. Changes nothing.
set -u
Q=${1:?usage: queue_line_check.sh QUEUE.txt 'TAG|DIR|SCRIPT|NOTE'}
L=${2:?missing line}
QD=$(cd "$(dirname "$Q")" && pwd)
fail=0; say(){ echo "FAIL: $*"; fail=1; }
nbar=$(printf '%s' "$L" | tr -cd '|' | wc -c)
[ "$nbar" -eq 3 ] || say "needs exactly 3 bars, has $nbar (a bar inside the note?)"
TAG=${L%%|*}; rest=${L#*|}; DIR=${rest%%|*}; rest=${rest#*|}; SCRIPT=${rest%%|*}
[ -n "$TAG" ] || say "empty tag"
[ -f "$Q" ] && grep -q "^$TAG|" "$Q" && say "tag $TAG already in the queue"
[ -e "$QD/SUBMITTED/done_$TAG" ] && say "done marker exists for $TAG"
if [ "$DIR" = "CANCEL" ]; then
  printf '%s' "$SCRIPT" | grep -qE '^[0-9]+$' || say "cancel line needs a numeric job id, got '$SCRIPT'"
else
  [ -d "$DIR" ] || say "dir missing: $DIR"
  [ -f "$DIR/$SCRIPT" ] || say "script missing: $DIR/$SCRIPT"
  [ -f "$DIR/$SCRIPT" ] && { bash -n "$DIR/$SCRIPT" 2>/dev/null || say "bash -n fails on $SCRIPT"; }
  R="$DIR/README_$TAG.md"
  [ -f "$R" ] || say "no README_$TAG.md in the package dir"
  [ -f "$R" ] && { grep -qi 'MEASURED' "$R" || say "README has no MEASURED line (timed heaviest task, peak memory)"; }
  if [ -d "$DIR" ]; then
    hits=$(grep -rlE '(^|[[:space:];&|])rm |--delete|rmtree' "$DIR" --include='*.sh' --include='*.py' --include='*.sbatch' 2>/dev/null | head -3)
    [ -n "$hits" ] && say "removal words in: $hits"
  fi
fi
[ "$fail" -eq 0 ] && echo "OK: $TAG"
exit $fail
