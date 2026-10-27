# RESOURCES.md: your resource profile

You do not have to edit this file to start. The values shown are the DEFAULT profile and they work on
any machine with Claude Code alone: one agent (no subagents), no API keys, no channel, no scheduler,
strict no-deletes. On its first run the lead asks ONE question, "how many agents may run at once,
including me? (default 1)", writes your answer here, and gets rolling. Everything else is detected or
defaulted and only reported. Edit values here whenever you have more (subagents, an API key, a chat
channel, a cluster); worked examples are in `resource_profiles/`. METHODOLOGY.md, SELF_CHECK.md,
CLAUDE.md and the brief templates read these names.

Keep this file short. Every value is one line. Change a value whenever your resources change and tell
the lead; the lead records the change with its time.

## 1. People

USER: the person at the terminal            # optional: your name or handle
DECIDERS: USER                              # who may change a final theorem's statement or hypotheses
COLLABORATORS: none                         # others who may give instructions; latest word governs, the other is told
PUBLIC_NAME_POLICY: no people's names, emails or process notes in any public document

## 2. Claude access

CHECK BEFORE STARTING: the MAIN agent's model and reasoning effort are set in Claude Code itself (the
model selector and the effort setting), not in this file. Make sure they are what you want; the lead
states what it runs as in its first report. SUBAGENTS (if any) get STRONGEST_MODEL and EFFORT below,
passed as the Agent tool's `model` and `effort` PARAMETERS at every spawn; writing "effort max" in a
prompt does nothing (once, half of a project's agents silently ran at a lower effort that way).

CLAUDE_CODE: yes                            # the lead runs in Claude Code
API_KEYS: no                                # yes if you hold an Anthropic API key for the lane runner (tools/api_lanes)
STRONGEST_MODEL: default                    # default = the model this session runs; set an id only to override for subagents or lanes
REVIEW_MODEL: default                       # default = STRONGEST_MODEL; one tier down is fine for refuters of questionable claims
EFFORT: max                                 # set through the Agent tool / API parameter, never by prompt text
OUTPUT_CAP: default                         # default = the model's maximum output; lanes and persistent agents use it

## 3. Parallelism

MAX_CONCURRENT_AGENTS: 1                    # agents running at once INCLUDING the main one; 1 = you alone, no subagents. The one question asked up front.
LANES_PER_PIECE: 0                          # API prove lanes per open piece; 0 when API_KEYS = no
LANES_PER_BIG_ITEM: 0                       # standing lanes on an item far from proof (2–6 with keys); the level never decays
API_CONCURRENT_LANES: 0                     # total concurrent API lanes you allow (spend)
REVIEW_LENSES: 2                            # independent lenses per load-bearing text; with 0 subagents = two fresh passes by you

## 4. Prompt limits for lanes (only with API_KEYS = yes)

PROVE_PROMPT_CAP: 125 KB                    # a prove or read lane's whole prompt
REVIEW_PROMPT_CAP: 150 KB                   # a text review's whole prompt; the text under review attached LAST
ATTACHMENT_CAP: 55 KB                       # per attached range; larger files attached by line ranges

## 5. Compute

HOST: workstation                           # laptop | workstation | HPC login node
SHARED_FS: no                               # yes <mount paths>: then never list big dirs, never glob-poll, exact names only
BATCH_SYSTEM: none                          # none | slurm | pbs | sge | ...
LOCAL_COMPUTE: light                        # NEVER ASSUMED beyond light. light: short single-core checks under the caps; cpu: up to LOCAL_CORES cores for LOCAL_COMPUTE_TIMEOUT; cpu+gpu: the GPU too. Asked up front when spare cores or a GPU are detected.
LOCAL_CORES: 1                              # cores the lead may use at once when LOCAL_COMPUTE is cpu or cpu+gpu
BATCH_USE: no                               # NEVER ASSUMED. no: neither prepares nor submits scheduler jobs unasked; recommend: prepares ONE script + a queue line for you to submit; agent: may submit itself where the cluster allows. Asked up front when a scheduler is detected.
NUMERICS_PYTHON: python3                    # the interpreter for numerics (full path if several exist)
MEMORY_CAP_KB: 2500000                      # ulimit -v for every numerics process
LOCAL_COMPUTE_TIMEOUT: 55m                  # wall-clock cap on any local computation
SCRATCH_DIR: ./scratch                      # bulk outputs go here, never into the record tree

## 6. Communication

CHANNEL: terminal                           # terminal | discord | slack | email (optional/discord_bridge for Discord)
POST_CAP_CHARS: none                        # 1800 for Discord; measure by script before posting
STATUS_INTERVAL_MIN: 30                     # a status post every N minutes while agents or lanes are live
TIMEZONES: UTC                              # e.g. "UTC / ET"; posts give every time in each zone

## 7. Autonomy

HELD_DECISIONS: money or keys; heavy local compute (while LOCAL_COMPUTE = light); scheduler submission (while BATCH_USE is not agent); settings, hooks or config changes; a final theorem's statement or hypotheses
DEFAULT_WHEN_AWAY: decide, start, report     # the lead never idles on a pending decision (METHODOLOGY 7.1)
DELETE_POLICY: strict                       # strict: nothing of record is ever deleted or overwritten; tmp-allowed: a job's own intermediates may go
FORBIDDEN_SOURCES: none                     # files or papers no lane may read (e.g. a solution you want derived independently)

## 8. Hand-over marks (persistent subagents)

HANDOVER_ASK_AT: 450k                       # harness token count at which the lead asks for the successor onboarding
HANDOVER_SPAWN_AT: 600k                     # the lead spawns the successor regardless
ONBOARDING_V1_AT: 150k                      # the agent writes its successor's onboarding v1 by this count

## 9. Open requests (kept by the lead; METHODOLOGY 7.23)

The lead lists here what would help and needs your yes, asks for one item per status with its default,
and records your answer with the time. Answers: yes / no / later <when> / stop asking.

| request | would change | default meanwhile | status |
|---|---|---|---|
| more concurrent agents (MAX_CONCURRENT_AGENTS) | parallel owners and reviewers | 1 | unasked |
| an API key for lanes (API_KEYS) | parallel prove and review lanes | no | unasked |
| local cores or GPU (LOCAL_COMPUTE, LOCAL_CORES) | heavier numerics locally | light | unasked |
| scheduler use (BATCH_USE) | batch jobs prepared or submitted | no | unasked |
| a chat channel (CHANNEL) | status and questions reach you away from the terminal | terminal | unasked |
| removing temporaries (DELETE_POLICY) | less scratch space | strict | unasked |
