---
name: effort-through-the-parameter
description: Subagent model and effort are set through the Agent tool's model and effort PARAMETERS at every spawn; "effort max" in prompt text does nothing; the main agent's model and effort are set in Claude Code and the lead states them (METHODOLOGY 4.9, 7.21)
metadata:
  type: feedback
---

Every subagent is spawned with STRONGEST_MODEL and EFFORT from RESOURCES.md passed as the Agent tool's `model` and `effort` parameters. The main agent's own model and effort are chosen in Claude Code by the user; the lead states what it is running as in its first report and asks the user to confirm.

**Why:** once, in a running project, half of forty agents spawned in a day ran at a lower effort than intended because their prompts said "effort max" while the tool parameter was left at its default; the co-author noticed from the quality of one coordinator's rulings. Audit of the effective effort showed the drift across the whole session.

**How to apply:** set the parameter at every spawn; never rely on prompt text for effort or model. Before relying on a verdict from an agent, check its effective effort where the harness exposes it. After an oversight, restart that line at the top effort and re-audit its last outputs (4.9). Refuters and checkers of highly questionable claims may run one tier lower on purpose (5.10); provers, writers and syntheses stay at the top. Related: [[launch-hygiene]], [[first-run-one-question-then-defaults]].
