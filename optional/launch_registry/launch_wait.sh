#!/usr/bin/env bash
# launch_wait.sh REGISTRY LABEL ROLE [MAXWAIT_SECONDS=900]
# Waits until (a) >= 300 s have passed since this ROLE's own last launched/planned line (midnight-safe),
# and (b) the current minute has no live planned/launched line of another label (today's lines only;
# planned lines older than 180 s without a launched/cancelled line are stale and ignored).
# Then appends "HH:MM:SS LABEL ROLE planned (launching now)" and prints "stagger OK" + the line. Exit 0.
# Exit 2 after MAXWAIT without a free minute. Never edits a line; never touches another process.
set -u
REG=${1:?usage: launch_wait.sh REGISTRY LABEL ROLE [MAXWAIT]}
LABEL=${2:?label}; ROLE=${3:?role}; MAXWAIT=${4:-900}
OWN_GAP=300; STALE=180; AHEAD=180
[ -e "$REG" ] || : > "$REG"
secs(){ IFS=: read -r h m s <<<"$1"; echo $((10#$h*3600 + 10#$m*60 + 10#$s)); }
# today's lines = after the last backward jump of more than 12 h
today_lines(){
  awk '{ split($1,a,":"); if (a[1] ~ /^[0-9][0-9]$/ && a[2] ~ /^[0-9][0-9]$/) { s=a[1]*3600+a[2]*60+a[3]; if (NR>1 && prev-s>43200) j=NR; prev=s } } END { print (j?j:1) }' "$REG" |
  { read -r start; tail -n +"$start" "$REG"; }
}
t0=$(date +%s)
while :; do
  now=$(date -u +%H:%M:%S); nows=$(secs "$now"); minute=${now%:*}
  # (a) own floor: latest planned/launched line of this ROLE, midnight-safe
  own_last=$(today_lines | awk -v r="$ROLE" '$3==r && ($4=="launched" || $4=="planned") {print $1}' | tail -1)
  own_ok=1
  if [ -n "$own_last" ]; then
    ls=$(secs "$own_last"); [ "$ls" -gt $((nows+60)) ] && ls=$((ls-86400))
    [ $((nows-ls)) -lt "$OWN_GAP" ] && own_ok=0
  fi
  # (b) the current minute: live lines of OTHER labels
  busy=0
  while read -r ts lab role state rest; do
    [ -n "$ts" ] || continue
    [ "${ts%:*}" = "$minute" ] || continue
    [ "$lab" = "$LABEL" ] && continue
    case "$state" in
      launched) busy=1 ;;
      planned)
        # stale if older than STALE s with no launched/cancelled for the same label
        ps=$(secs "$ts"); [ "$ps" -gt $((nows+60)) ] && ps=$((ps-86400))
        if [ $((nows-ps)) -gt "$STALE" ] && ! today_lines | awk -v l="$lab" '$2==l && ($4=="launched" || $4=="cancelled")' | grep -q .; then
          : # stale, ignore
        else busy=1; fi ;;
      cancelled) ;;
    esac
  done < <(today_lines)
  if [ "$own_ok" -eq 1 ] && [ "$busy" -eq 0 ]; then
    line="$(date -u +%H:%M:%S) $LABEL $ROLE planned (launching now)"
    echo "$line" >> "$REG"
    echo "stagger OK"; echo "$line"; exit 0
  fi
  [ $(( $(date +%s) - t0 )) -ge "$MAXWAIT" ] && { echo "launch_wait: no free minute within ${MAXWAIT}s (own_ok=$own_ok busy=$busy)"; exit 2; }
  # sleep to just past the next minute boundary (or 10 s when waiting on the own floor), never beyond MAXWAIT
  if [ "$own_ok" -eq 0 ]; then nap=10; else nap=$(( 60 - 10#${now##*:} + 2 )); fi
  left=$(( MAXWAIT - ( $(date +%s) - t0 ) )); [ "$nap" -gt "$left" ] && nap=$left; [ "$nap" -lt 1 ] && nap=1
  sleep "$nap"
done
