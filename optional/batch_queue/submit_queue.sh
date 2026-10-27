#!/usr/bin/env bash
# submit_queue.sh QUEUE.txt : the user's one standing line.
# Submits every QUEUE line whose TAG has no SUBMITTED/done_<TAG> marker; writes SUBMITTED/<TAG> with
# the job id; appends to SUBMITTED/log_submit_queue.txt; writes the done marker. Handles cancel lines
# TAG|CANCEL|<jobid>|note through $CANCEL_CMD. Never deletes anything.
#   SUBMIT_CMD   (default: sbatch)   how to submit a script: $SUBMIT_CMD <script>, run from the package dir
#   CANCEL_CMD   (default: scancel)  how to cancel a job id
#   JOBID_REGEX  (default: [0-9]+)   how to pull the job id out of the submit command's output
set -u
Q=${1:?usage: submit_queue.sh QUEUE.txt}
QD=$(cd "$(dirname "$Q")" && pwd)
S="$QD/SUBMITTED"
mkdir -p "$S"
SUBMIT_CMD=${SUBMIT_CMD:-sbatch}
CANCEL_CMD=${CANCEL_CMD:-scancel}
JOBID_REGEX=${JOBID_REGEX:-[0-9]+}
LOG="$S/log_submit_queue.txt"
n_new=0; n_skip=0; n_bad=0
while IFS= read -r line || [ -n "$line" ]; do
  case "$line" in ''|'#'*) continue ;; esac
  nbar=$(printf '%s' "$line" | tr -cd '|' | wc -c)
  if [ "$nbar" -ne 3 ]; then echo "BAD LINE (needs exactly 3 bars): $line" | tee -a "$LOG"; n_bad=$((n_bad+1)); continue; fi
  TAG=${line%%|*}; rest=${line#*|}; DIR=${rest%%|*}; rest=${rest#*|}; SCRIPT=${rest%%|*}; NOTE=${rest#*|}
  if [ -e "$S/done_$TAG" ]; then n_skip=$((n_skip+1)); continue; fi
  TS=$(date -u +%FT%TZ)
  if [ "$DIR" = "CANCEL" ]; then
    out=$($CANCEL_CMD "$SCRIPT" 2>&1); rc=$?
    echo "$TS CANCEL $TAG jobid=$SCRIPT rc=$rc $out | $NOTE" | tee -a "$LOG"
    printf 'cancel of %s rc=%s at %s\n' "$SCRIPT" "$rc" "$TS" > "$S/$TAG"
    printf 'cancel issued %s\n' "$TS" > "$S/done_$TAG"
    n_new=$((n_new+1)); continue
  fi
  if [ ! -d "$DIR" ] || [ ! -f "$DIR/$SCRIPT" ]; then
    echo "$TS MISSING $TAG dir=$DIR script=$SCRIPT (not submitted)" | tee -a "$LOG"; n_bad=$((n_bad+1)); continue
  fi
  out=$(cd "$DIR" && $SUBMIT_CMD "$SCRIPT" 2>&1); rc=$?
  jid=$(printf '%s' "$out" | grep -oE "$JOBID_REGEX" | tail -1)
  echo "$TS SUBMIT $TAG rc=$rc jobid=${jid:-?} $out | $NOTE" | tee -a "$LOG"
  printf 'jobid=%s rc=%s at %s\nscript=%s\ndir=%s\n' "${jid:-?}" "$rc" "$TS" "$SCRIPT" "$DIR" > "$S/$TAG"
  if [ "$rc" -eq 0 ]; then printf 'submitted %s jobid=%s\n' "$TS" "${jid:-?}" > "$S/done_$TAG"; n_new=$((n_new+1)); else n_bad=$((n_bad+1)); fi
done < "$Q"
echo "submit_queue: new $n_new, skipped $n_skip (done markers), problems $n_bad; log $LOG"
