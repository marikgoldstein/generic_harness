# tools/

Small scripts that implement the mechanical parts of METHODOLOGY.md. None of them names a machine:
every path comes from an argument or from `harness.env` (copy `harness.env.example`, edit, `source`
it). All are stdlib Python 3 or plain bash; only `api_lanes/lanes.py` needs the `anthropic` package.

| tool | what it does | reads from RESOURCES.md / harness.env | needed when |
|---|---|---|---|
| `harness.env.example` | the sourceable env file: HARNESS_ROOT, RECORD_DIR, WORK_DIR, LIT_DIR, LEAD_DIR, SCRATCH_DIR, LANES_DIR, POSTS_DIR, BACKUP_ROOT, NUMERICS_PYTHON, MEMORY_CAP_KB, TIMEZONES, POST_CAP_CHARS, the LANES_* caps | everything | always (copy to `harness.env`) |
| `api_lanes/lanes.py` | build / run / export / layered / census for API lanes: inlines ranged attachments with line numbers, streams each request, journals partial text, records stop_reason, exports to new file names, prints the stop-reason census | API_KEYS, STRONGEST_MODEL (LANES_MODEL), EFFORT, OUTPUT_CAP (LANES_MAX_TOKENS), ATTACHMENT_CAP, FORBIDDEN_SOURCES | API_KEYS = yes only (METHODOLOGY 4) |
| `api_lanes/pool_to_spec.py` | converts an owner's plain lane lines (`P#### — <statement> — attach a; b:lo-hi`) into a lanes.py spec and runs the PRE-CHECK: one statement per line, exactly one attach part, every attachment present, ranges inside the file's content line count, oversize files only by range, review text last, no duplicate ids or prompts | HARNESS_ROOT, ATTACHMENT_CAP, EFFORT, OUTPUT_CAP | API_KEYS = yes; every launch (METHODOLOGY 4.7, 4.11) |
| `landsum.py` | one-line summary per landed lane file (VERDICT / FINAL STATUS / most serious / READ, char count), by exact name | SHARED_FS (why globs are off by default) | any lanes or review files |
| `comms_audit.py` | one-shot audit of a lanes dir: cut markers, missing attachments, oversize prompts, void / truncated / refusal / partial / API-error counts, lost and unexported lanes; writes a report | LANES_DIR | API lanes; run once per status (METHODOLOGY 6.10) |
| `free_id_blocks.py` | free blocks of lane ids from the ledger, AGENT_IDS.md and the registry, with the ASSIGNED/RELEASED state machine | LEAD_DIR | several agents launching lanes (METHODOLOGY 4.11, 6.6) |
| `backup_versioned.sh` | versioned rsync backup (mirror + per-run versions), never deletes, flock, nice/ionice, RUNS.tsv | BACKUP_ROOT, BACKUP_SOURCES | always; every 2 h from one tracked background loop |
| `status_post.py` | stamps a status with the clock at run time, asserts the channel cap in characters, splits at `## ` boundaries into parts, writes new files | TIMEZONES, POST_CAP_CHARS, POSTS_DIR | any channel with a length cap (METHODOLOGY 7.12, 7.13) |

## Quick use

```bash
cp tools/harness.env.example tools/harness.env   # edit the paths
source tools/harness.env

# lanes (API_KEYS = yes): the owner writes plain lane lines; convert + pre-check; build; run as ONE tracked
# background job; export; read the census
python3 -I -B tools/api_lanes/pool_to_spec.py lead/pools/pool_A.txt lead/specs/pool_A.jsonl --out-dir $WORK_DIR/item03 --first-id 101 --alias RECORD=$RECORD_DIR
python3 -I -B tools/api_lanes/lanes.py build  lead/specs/pool_A.jsonl  $LANES_DIR/poolA_$(date -u +%m%d_%H%M)
python3 -I -B tools/api_lanes/lanes.py run    $LANES_DIR/poolA_<stamp> --workers 4 --stagger 5
python3 -I -B tools/api_lanes/lanes.py export $LANES_DIR/poolA_<stamp>
python3 -I -B tools/landsum.py work/item03/SEEK_P0101.md work/item03/SEEK_P0102.md

# every status
python3 -I -B tools/comms_audit.py $LANES_DIR 240 40
python3 -I -B tools/status_post.py --cap $POST_CAP_CHARS lead/inbox/status_draft.md

# before writing any brief that launches lanes
python3 -I -B tools/free_id_blocks.py --min 30 lead/AGENT_IDS.md lead/LEDGER.md lead/LAUNCH_REGISTRY.txt
```

## Conventions the tools enforce

- New files only: every writer opens with `x` or appends a version suffix; nothing is overwritten.
- Exact names: `landsum.py` and `comms_audit.py` never glob a big directory; `comms_audit.py` does one
  `readdir` of LANES_DIR and selects run dirs by their `<tag>_<mmdd>_<HHMM>` stamp.
- The clock is read at run time by the script, never passed as an argument (`status_post.py`,
  `backup_versioned.sh`, the report names in `comms_audit.py`).
- The build aborts on a cut or missing attachment; a lane that stopped at its output limit with no
  text is exported as `<out>_VOID.md`, headed "not a proof, not a verdict", and counted VOID.
- The lane runner never prints, logs or forwards the API key. Refusal fallbacks (a server-side
  re-run on another model) are OFF by default and opt-in with `--fallbacks`: a lane's model is part
  of its record, and the methodology books a refusal as a lost lane to bisect and re-issue.

## Writing a spec line

```json
{"id": "P0101", "role": "prove", "out": "/abs/work/item03/SEEK_P0101.md",
 "task": "Prove exactly, for every scale in the family with constants independent of the index: <statement>. Consumer line (quoted verbatim): <file:line> ...",
 "files": ["/abs/record/DEFINITIONS.md:120-180", "/abs/work/item03/STATEMENT_v3.md"],
 "effort": "max", "max_tokens": 64000}
```

One range per file entry; the text under review LAST (for `review` lanes); shared definitions once,
as a small attached file. Two independent lanes per piece means two spec lines with distinct methods
in the task text, never the same prompt twice (METHODOLOGY 4.2).
