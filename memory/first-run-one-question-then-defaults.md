---
name: first-run-one-question-then-defaults
description: On a fresh project ask, in one message, only the setup questions that apply, each with a default (max concurrent agents incl. yourself 1; API key no; local CPU/GPU light checks only; scheduler neither), state your model/effort and the subagent spawn policy, then start (METHODOLOGY 7.21, 7.22, 8.13)
metadata:
  type: feedback
---

On the first run of a project whose RESOURCES.md is absent or untouched, ask the user in ONE message only the questions that apply, each with its default: how many agents may run at once including you (1); an API key for lanes (no); if spare cores or a GPU are detected, heavier local numerics (light single-core checks only); if a scheduler is detected, prepare scripts for the user, submit yourself, or neither (neither). State the model and effort you run as and that subagents get STRONGEST_MODEL and EFFORT through the Agent tool parameters; ask the user to confirm. If no answer comes in the first turn, proceed with the defaults, write them into RESOURCES.md with the time, and say so.

**Why:** the harness is meant to run for anyone, on any machine, with Claude Code alone. A setup phase that asks about compute, channels, schedulers and models before any work starts is the headache it was built to avoid; the user asked for a default that gets rolling with the main agent and a single up-front question about concurrency.

**How to apply:** detect capabilities instead of asking about them: an API key plus the client package means lanes; a configured channel means posts go there, otherwise the status is a terminal block and the state log; a scheduler binary and a queue dir mean batch packages, otherwise local runs under the caps. Say once what was found, then work with what is there. Every other RESOURCES.md value is applied as its default and only reported; the user edits the file when they have more. Related: [[never-idle-next-useful]], [[question-filter-goal-then-method]], [[cap-soft-transient]].
