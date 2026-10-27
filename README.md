# generic_harness

A way of running Claude Code as an autonomous research lead on a proof or exploration project in
mathematics or theoretical physics. It was distilled from a running project and stripped of
everything specific to it. What remains is the operating method: get going on its own, decide with
sensible defaults, prove rather than reduce, check the numbers first, review every text with a fresh
pair of eyes, and report honestly.

## How to start

```bash
git clone https://github.com/marikgoldstein/generic_harness.git
cd generic_harness
claude
```

Then type your problem, or point it at a problem file (`read problem.md`; any `.md` works,
`templates/PROBLEM_SPEC.md` shows the shape). It writes the goal and the first items and goes.
For an existing project instead: `bash install.sh /path/to/project`, then `cd` there and `claude`.

It assumes minimal resources: loosely one concurrent local agent at most, no API keys, no heavy local
compute, no scheduler, no chat channel, nothing deleted. "Loosely one" means you may see more than one
agent exist, because it still runs things like a prover with a blank-context refuter, but the parallel
work stays at about one agent unless you grant more.

More generally it is conservative about resources but not shy: it keeps a short list of things that
would help (more agents, an API key, local cores or a GPU, a scheduler, a channel) and gently asks, one
at a time with its default, whether they are available and okay to use, until you say yes, no, "ask me
later", or "stop asking". It never blocks on an unanswered request.

Before you start, check the model and reasoning effort of your Claude Code session; the lead tells you
what it is running as and spawns any helpers with the model and effort set in `RESOURCES.md`.

## Where to look

- `AUTONOMY.md`: the one-page contract for how it behaves when you are not there.
- `CLAUDE.md`: the briefing it reads at every start; fill in the project name.
- `METHODOLOGY.md`: the rules, cited by number everywhere else.
- `SELF_CHECK.md`: the questions it asks itself before every status.
- `RESOURCES.md`: the resource profile with its conservative defaults, and the wish list it keeps.

Everything else is support: `briefs/` (prompts for helpers), `memory/` (lessons it starts with),
`tools/` (an API lane runner and audits, only if you have a key), `optional/` (a chat bridge, a batch
queue, a launch registry), `templates/` and `resource_profiles/` (worked examples). Each folder has
its own short README.

## Acknowledgements

Thanks to Alfredo Guevara and Alfredo's agents for the previous versions of the harness.
