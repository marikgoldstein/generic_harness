# batch_queue/: the agent prepares, the user submits

Turned on by `BATCH_SYSTEM:` anything but `none` in RESOURCES.md, with `BATCH_USE: recommend`. The
scheduler is a shared resource and submission is a check-in point: agents build complete, verified
packages and append ONE line to a queue; the user runs ONE standing line that submits everything new.
With `BATCH_USE: agent` the same package rules hold and the agent runs `submit_queue.sh` itself.
(METHODOLOGY 8.8, 2.4b, 7.8.)

## The queue line

One line per job appended to `QUEUE.txt`, four fields, exactly three bars, no bar inside the note:

    TAG|/abs/path/to/package/dir|script.sbatch|note in plain words

- `TAG`: unique, dated suffix (a reused tag is silently skipped by the done marker); also the script's
  job name where the scheduler has one.
- A cancel line for a superseded or colliding job: `TAG_CANCEL|CANCEL|<jobid>|why`. A line that
  SUPERSEDES another is appended TOGETHER with its cancel twin, or the user writes the superseded tag's
  done marker first; otherwise both run and collide on shared outputs.
- Run `queue_line_check.sh <line>` before appending (fields, tag unique, dir and script exist, `bash -n`
  clean, no done marker, the README's MEASURED line present).
- Then tell the user: "new in queue: N" plus what each job is for in plain words, and the one standing
  line. Never hand the user a second script name.

## The user's one standing line (never changes)

    bash /path/to/optional/batch_queue/submit_queue.sh /path/to/QUEUE.txt

It submits every line whose tag has no `SUBMITTED/done_<TAG>` marker, writes `SUBMITTED/<TAG>` with the
job id, appends to `SUBMITTED/log_submit_queue.txt`, and writes the done marker. Agents read the job ids
from the files, never from a scheduler query.

## Markers

- `SUBMITTED/done_<TAG>`: written by the submit script after a submission; a line whose tag has one is
  skipped forever.
- HELD: the lead writes `SUBMITTED/done_<TAG>` BEFORE the user's run with the text
  `HELD by the lead HH:MM UTC: <reason>; never submit this line`; the held line is never edited or
  removed; a replacement gets a NEW tag.
- WITHDRAWN: the same marker with `WITHDRAWN, never submitted, replaced by <TAG2>`.

## The package (one directory per job)

- `README_<TAG>.md` with, in this order: the CONSUMED THRESHOLD quoted first (file:line, direction,
  unit: the number the run must beat and where it is consumed, 2.4b); the room statement (which constant
  the lemmas deliver, the certified pieces with their error budgets, the assembly inequality); the task
  mapping; the MEASURED heaviest task (wall clock, peak resident memory, seconds per unit, from a real
  timed run, never the cap); the cost line of record = measured per-task time × count with the measured
  peak memory (planning digits are replaced by the measurement, never averaged with it); memory per CPU
  ≥ 2× the measured peak; a per-task timeout ≥ 2× the measured time; the resume pattern; the output root
  under SCRATCH_DIR.
- The scheduler script (`bash -n` clean), with a per-task timeout, writing only new names into a fresh
  output root; no deletes.
- A resumable task file with a RESULT-line guard per task: a task is skipped only if its output CONTAINS
  its RESULT line (never by file existence; a traceback or a partial file also exists).
- Byte-identical copies of the task and reducer code with their sha256 prefixes recorded.
- A reducer with its checks: FAILED must be 0; the partition check exact; digits rounded in the safe
  direction; per-shard maxima printed and inspected before any sup is consumed.
- A grep for removal words (`rm `, `--delete`, `shutil.rmtree`) returning 0 hits over every queued file.
- Superseded files left in place with a NOTE file; never queued again.

## Watching and reading

- Watch outputs by exact file name (`SUBMITTED/done_<TAG>`, the reducer's RESULT file), at most every
  5 minutes, bounded by wall clock, two watchers at most (8.7). Never poll the scheduler.
- Read-only scheduler queries (`squeue -u`, `sacct -j`, `scontrol show job`) are one-shot, for a
  specific job, never in a loop. A "running" job is tested against its done marker or one accounting
  line at every status: queue listings drop completed and halted jobs silently.
- A job that ends COMPLETED with no RESULT lines is "ended without its result", not "done": read the
  output root and the task log's failed lines before any status word moves (7.8).
- A cancel of a superseded or colliding job (if RESOURCES.md allows the agent to cancel) is preceded by
  the agent's own read of the evidence on the files and a one-shot dependency check; it is a stand-alone
  command, never in a chain; the user is told the same turn with job ids and reason. When a permission
  classifier blocks it, post the exact one-line command for the user.
- A resume job re-tests its guard files in pairs (an output present without its companion is stale) and
  renames stale companions by a logged no-clobber step; nothing deleted.
