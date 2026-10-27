# generic_harness

A harness for running Claude Code (and, optionally, API lanes) as an autonomous research lead on a
large proof or exploration project in mathematics or theoretical physics. It was distilled from a
running project where one lead agent, many subagents and hundreds of API lanes attacked a frozen list
of open items for two weeks under a demanding pair of co-authors. Everything project-specific has been
removed. What remains is the operating method.

## What it is for

The point of the harness is a way of working, not the scripts:

- **Autonomy.** The lead never idles on a pending decision. It picks the most useful feasible default,
  starts it, and tells you that you can redirect. It holds only for the short list of decisions you
  reserve (money, keys, settings, a final theorem's statement).
- **Defaults when you are away.** Before asking you anything, the lead states the project goal to
  itself and checks whether the goal or the methodology already answers the question. Most questions
  die there. The ones that survive arrive in a plain, short form with a recommendation and a default.
- **Truth first, numbers first.** Before proving, say what you believe is true and why, and get a
  number that could have come out wrong. No proof round without numerical evidence.
- **Prove, never reduce.** A result "derived given X" closes nothing unless X is already of record.
- **Strict closing and a frozen ledger.** Items are numbered once and never renumbered. CLOSED means
  the owner is done and every remaining input is owned elsewhere. The open count leads every status.
- **Analyze every landing.** A landed result is read for what it showed: refill aimed at that, re-locate
  the failing step, close a refuted route on the record, keep the truth word with its evidence.
- **Honest reporting.** Progress as x of y. Every item in Done / Open algorithmic / Open mathematics /
  Now. No difficulty framing, no forecasts, no "basically done" while anything is open. A self-check of
  pointed questions runs before every status.

## Quick start (nothing to configure)

Start by typing your problem, or by pointing at a problem spec file. The lead writes the goal and the
first items from it and gets going. Conservative defaults are assumed for everything else: one agent,
no API keys, no local heavy compute, no scheduler, no channel, strict no-deletes. They work on any
machine with Claude Code alone. From then on the lead keeps a short wish list of things that would
help (more agents, an API key, local cores or a GPU, scheduler use, a chat channel) and asks for one
per status, with its default, until you say yes, no, "ask me later", or "stop asking". It never blocks
on an unanswered request.

1. Copy `CLAUDE.md`, `METHODOLOGY.md`, `SELF_CHECK.md` and `RESOURCES.md` into your project root
   (or symlink this directory as `harness/`). Put the project name in `CLAUDE.md`; leave the rest.
   Optionally write a problem spec (`templates/PROBLEM_SPEC.md` shows the shape); otherwise you will
   just type the problem.
2. Optionally point your Claude Code memory directory at `memory/` (or copy its files in) so the lead
   starts with the lessons already learned.
3. Check the model and reasoning effort your Claude Code session runs with; they are set in Claude
   Code, not in the harness. Then start it in the project root. The lead asks, in one message, only the
   questions that apply, each with a default: how many agents may run at once including itself (1);
   whether an API key exists for parallel lanes (no); whether it may use this machine's spare CPU/GPU
   for heavier numerics (light checks only); whether to prepare scheduler scripts for you, submit them
   itself, or neither (neither). It also states its own model and effort and that subagents get
   `STRONGEST_MODEL` and `EFFORT` through the Agent tool's parameters. Answer or not; it writes the
   answers into `RESOURCES.md`, says which capabilities it detected, and starts on the first item that
   needs no held decision. It never assumes local heavy compute or scheduler use.

Have more? Edit `RESOURCES.md` any time (or copy the closest `resource_profiles/*.md` over it): more
subagents, an Anthropic API key for parallel lanes (`tools/README.md`), a chat channel or a batch
scheduler (`optional/README.md`). The lead picks the new values up at its next status.

## Directory map

| path | what |
|---|---|
| `METHODOLOGY.md` | the rules of proof, review, bookkeeping, autonomy, communication and hygiene; cited by number |
| `SELF_CHECK.md` | the pointed questions the lead asks itself before every status, landing and staffing decision |
| `RESOURCES.md` | your resource profile; every resource-dependent rule reads its parameters from here |
| `resource_profiles/` | four worked profiles: single agent; subagents; account plus API; cluster with a co-author |
| `CLAUDE.md` | the lead's briefing, to copy into a project root and fill in |
| `ONBOARDING_TEMPLATE.md` | how a fresh lead takes over a running project |
| `templates/` | `GOAL.md`, `LEDGER.md`, `STATE_LOG.md` skeletons |
| `briefs/` | spawn prompts for owners, provers, review lenses, coordinator, closer, editor, successor; a shared safety header |
| `memory/` | the lead's persistent-memory seed set (about forty lessons) with its index and a README |
| `tools/` | the API lane runner (direct Anthropic API), audit and summary scripts, a versioned backup, a status-post builder |
| `optional/` | plug-ins: a Discord bridge with hooks, the batch-queue pattern, the launch registry |

## How the harness scales

The methodology names roles. How each role is realized depends on your profile. Nothing in the
method needs more than one agent to be meaningful.

| role | one agent (`MAX_CONCURRENT_AGENTS = 1`, the default) | subagents | subagents + API lanes |
|---|---|---|---|
| lead | you, between items | the main session | the main session |
| owner of an item | the hat you wear while on that item | one persistent subagent per open item | same |
| prove lanes on a piece | fresh passes by you, task written out first, one route per pass | spare subagents when the cap allows | `LANES_PER_PIECE` API lanes, refilled on landing |
| review pair | two fresh-context passes: A (break it), then B (rebuild) without A's notes | two fresh subagents | two API lanes (A, B); local reviewers on the assembled argument |
| coordinator (census) | you, at every status | a fresh subagent per round, or the lead | same |
| dedicated prover on an open-mathematics input | the input becomes your next item with a named route | one persistent subagent per input | same, plus lanes |
| status | a block in the terminal and `STATE_LOG.md` | same, or a channel | same |

What does not change across profiles: the order of work (pin the object, quote the consumer, truth
first, numbers first, prove in full, split only under the six criteria), the closing rule, the review
standard, the self-check, and the communication rules.

## What to customize

- `RESOURCES.md`: everything resource-dependent lives here, and every value has a working default.
  Change a value, tell the lead, and the lead records the change with its time.
- `CLAUDE.md`: the goal paragraph and the layout of your record.
- `METHODOLOGY.md` section 0 tells the lead to add every method instruction you give as a numbered
  rule the same turn. Expect the file to grow with your project; rules are never renumbered.
- `briefs/`: the `{{PLACEHOLDERS}}` are substituted at spawn; the shared header is the safety contract.
- `FORBIDDEN_SOURCES` in `RESOURCES.md`: anything you want derived independently rather than read.

## What is optional

- `tools/api_lanes/lanes.py` needs the `anthropic` Python package and an API key. Without a key, set
  `LANES_PER_PIECE: 0` and the method falls back to subagents or to your own fresh passes.
- `optional/discord_bridge/` needs a bot token and a channel. Without it, `CHANNEL: terminal`.
- `optional/batch_queue/` is for a shared scheduler where you (not the agent) submit jobs.
- `optional/launch_registry/` matters only when several agents launch API lanes concurrently.

## Caveats

- Token-count marks for hand-overs (`HANDOVER_ASK_AT` and friends) depend on the harness version and
  the model's context; treat the defaults as starting points and read the counts the harness reports.
- Model ids change. The methodology says "your strongest model"; `RESOURCES.md` holds the id.
- The method was tuned on a proof programme with a long chain of named inputs. For an exploration
  project with no fixed theorem, keep the ledger (of questions), the truth-first and numbers-first
  gates, the review pairs and the reporting rules; the closing rule becomes "answered with evidence of
  stated kind".

## Acknowledgements

Thanks to Alfredo Guevara and Alfredo's agents for the previous versions of the harness.
