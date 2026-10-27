# launch_registry/: staggering lane launches across agents

Turned on when several agents launch API lanes (`API_KEYS: yes` and more than one launcher). Each lane
reserves its whole output budget the moment it starts, so a burst of starts in the same minute trips
the rate limit and lanes fail or are refused (METHODOLOGY 4.16). A launcher cannot see another
launcher's logs, so the stagger needs ONE shared file.

## The registry

An append-only text file (`$REGISTRY`, e.g. `lead/LAUNCH_REGISTRY.txt`), one line per event:

    HH:MM:SS <label> <role> planned
    HH:MM:SS <label> <role> launched
    HH:MM:SS <label> <role> cancelled

Lines are stamped from the clock at write time, never edited. Every launcher follows the same protocol:

1. BEFORE a launch: scope the file to TODAY's lines (the lines after the last backward time jump of
   more than 12 hours, since the file spans days and lines carry only HH:MM:SS), then count the lines
   that share the current minute, `planned` or `launched`, of OTHER labels. If any, wait into the next
   minute that is free of every other line, re-read, then launch.
2. Reserve ahead at most 3 minutes with a `planned` line; a `planned` line older than 3 minutes with
   no `launched` or `cancelled` line for its label is STALE and does not block (the launcher that uses
   the minute says so in its own line).
3. Append the `launched` line THE MOMENT the launcher prints its launch time, not when it returns
   (returns come minutes later, after the lanes land); write a `planned (launching now)` line the
   instant the stagger check passes.
4. Hold at most the START minute plus one follow-on minute (for a build that spills over); cancel the
   follow-on at the print. A minute whose only lines are `cancelled` is free.
5. One launch at a time per role, at least 5 minutes after that role's OWN previous launch; waiters
   chained on each other's logs, never two waiters on one role.
6. Midnight: a logged time later than now + 60 s is YESTERDAY (subtract a day) when computing the
   role's own floor; otherwise the waiter waits forever after 00:00 UTC.
7. A waiter that prints neither "stagger OK" nor a registry line within its MAXWAIT is stuck; the role
   kills ITS OWN waiter by pid (never another role's) and starts a fresh one.
8. Every launch report quotes the registry line and the launcher's printed launch time; they must
   agree to the second.

## The waiter

`launch_wait.sh REGISTRY LABEL ROLE [MAXWAIT_SECONDS]` implements 1–6: it waits for the role's own
5-minute floor, then for a minute free of other labels' live lines, appends the `planned (launching now)`
line, prints `stagger OK` and the line, and exits 0. The caller then launches immediately and appends
its `launched` line at the launcher's print:

    ./launch_wait.sh "$REGISTRY" POOL_X_1 owner-x 900 && launch_my_lanes ... \
      && echo "$(date -u +%H:%M:%S) POOL_X_1 owner-x launched" >> "$REGISTRY"

Exit 2 means MAXWAIT passed without a free minute; report it in the status rather than launching.
With a single launcher the registry is still useful as a launch log, but the waiting is unnecessary.
