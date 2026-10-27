#!/bin/bash
# backup_versioned.sh: versioned rsync backup that never deletes.
#
#   BACKUP_ROOT=/path/to/backups backup_versioned.sh SRC1:name1 [SRC2:name2 ...]
#   or set BACKUP_SOURCES="SRC1:name1 SRC2:name2" in harness.env and call it with no args.
#
# Each source is mirrored to $BACKUP_ROOT/mirror/<name>/. Every file a run would replace is first
# moved to $BACKUP_ROOT/versions/<UTC stamp>/<name>/ (rsync --backup), so no version is ever lost.
# Never --delete; never writes into a source. flock keeps runs from overlapping; nice/ionice keep it
# polite on a shared machine. Logs: $BACKUP_ROOT/logs/; one line per run in RUNS.tsv.
#
# Schedule it from the harness's tracked background mechanism, e.g. every 2 hours:
#   while true; do bash tools/backup_versioned.sh; sleep 7200; done
# (as ONE run_in_background call; never a trailing '&'). Re-create the loop after a restart.
# Bulk numeric outputs belong under SCRATCH_DIR and are normally NOT in the source list.
set -u
: "${BACKUP_ROOT:?set BACKUP_ROOT (in harness.env or the environment)}"
STAMP=$(date -u +%Y%m%d_%H%M)
mkdir -p "$BACKUP_ROOT/mirror" "$BACKUP_ROOT/versions" "$BACKUP_ROOT/logs"
LOG="$BACKUP_ROOT/logs/backup_$STAMP.log"
exec 9>"$BACKUP_ROOT/.lock"
flock -n 9 || { echo "$(date -u +%FT%TZ) another backup is running; skipped" >> "$BACKUP_ROOT/logs/skipped.log"; exit 0; }
if [ $# -gt 0 ]; then SRCS=("$@"); else read -r -a SRCS <<< "${BACKUP_SOURCES:-}"; fi
[ ${#SRCS[@]} -gt 0 ] || { echo "no sources given (args or BACKUP_SOURCES)"; exit 2; }
RC=0
for pair in "${SRCS[@]}"; do
  src=${pair%%:*}; name=${pair##*:}
  [ -d "$src" ] || { echo "MISSING SOURCE $src" >> "$LOG"; RC=2; continue; }
  mkdir -p "$BACKUP_ROOT/mirror/$name"
  nice -n 15 ionice -c3 rsync -rlt --backup --backup-dir="$BACKUP_ROOT/versions/$STAMP/$name" \
     --exclude='.git/' --exclude='__pycache__/' --exclude='.lake/' --exclude='node_modules/' \
     --itemize-changes "$src/" "$BACKUP_ROOT/mirror/$name/" > "$LOG.$name" 2>&1
  r=$?; n=$(grep -c '^[<>c]f' "$LOG.$name" 2>/dev/null)
  echo "$(date -u +%FT%TZ) $name rc=$r files_copied=$n" >> "$LOG"
  [ $r -eq 0 ] || RC=1
done
nv=0; [ -d "$BACKUP_ROOT/versions/$STAMP" ] && nv=$(find "$BACKUP_ROOT/versions/$STAMP" -maxdepth 7 -type f 2>/dev/null | wc -l)
echo "$(date -u +%FT%TZ) done rc=$RC; versions kept this run: $nv" >> "$LOG"
echo "$STAMP rc=$RC versions=$nv" >> "$BACKUP_ROOT/logs/RUNS.tsv"
exit $RC
