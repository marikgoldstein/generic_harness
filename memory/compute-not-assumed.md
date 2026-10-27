---
name: compute-not-assumed
description: Never assume local heavy compute (cores, GPU) or scheduler use; light single-core checks are always fine; more only when the user grants it, recorded in RESOURCES.md (METHODOLOGY 8.13, 7.2)
metadata:
  type: feedback
---

Light single-core numerical checks under the memory cap and a short timeout are always allowed; they are what the numbers-first gate runs on. Anything heavier on the local machine (several cores, long runs, a GPU) and any use of a scheduler are used only when the user has said so.

**Why:** the harness is shared across very different setups: a laptop, a workstation with idle cores and a GPU, a login node of a shared cluster where heavy local compute is unwelcome and only the user may submit jobs. Assuming any of these is wrong somewhere. The user asked for a default that assumes nothing and is glad to use more when told.

**How to apply:** at first run, ask about local CPU/GPU only if spare cores or a GPU are detected, and about the scheduler only if one is detected, each with the "no" default; record the answer in RESOURCES.md (LOCAL_COMPUTE, LOCAL_CORES, BATCH_USE) with the time. With BATCH_USE "no", say in a status that a step would be a batch job and leave it there; with "recommend", prepare ONE script and a queue line and let the user submit; with "agent", submit and tell the user. Read-only scheduler queries are one-shot, never polled. Related: [[first-run-one-question-then-defaults]], [[batch-queue-one-standing-line]], [[python-caps-enforced]].
