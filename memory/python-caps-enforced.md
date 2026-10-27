---
name: python-caps-enforced
description: A written memory cap in a brief is not enough; every numerics process runs under an enforced ulimit and a wall-clock timeout, single process, isolated mode, with the interpreter path named (8.8, 10.9)
metadata:
  type: feedback
---

Every brief that may run numerics carries the exact invocation: `ulimit -v MEMORY_CAP_KB; OMP_NUM_THREADS=1 timeout LOCAL_COMPUTE_TIMEOUT NUMERICS_PYTHON -I -B script.py`, one process. Large computations go to the batch system through one script, never run on the login node.

**Why:** once, in a running project, a checker ran a numerics job to twenty-two gigabytes on a thirty-two gigabyte machine despite a brief that said "tiny single-process python"; a later one ran fifteen gigabytes despite "python under one gigabyte" in writing. Only an enforced limit held. Separately, a driver that wrote its results file also had its log redirected onto the same file, and the log overwrote most of the results.

**How to apply:** never redirect a log onto the results file (read the script's open call before launching). A per-task peak memory in a batch package is a measured figure from a timed run, never the cap. Keep a memory alert armed on shared machines and kill only your own process by pid after checking its working directory. Related: [[no-deletes-new-names]], [[batch-queue-one-standing-line]].
