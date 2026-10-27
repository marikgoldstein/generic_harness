---
name: api-lanes-write-early-and-split
description: Long prove lanes spend their whole output budget thinking and return nothing unless told to write the result section first; narrow one lemma per lane; re-cut void or truncated lanes by the failing structure; stagger starts under the rate limit (4.3, 4.4, 4.5, 4.16)
metadata:
  type: reference
---

Every prove lane carries the write-early clause: the result section (statement, status word, the failing step or the proof skeleton) within the first quarter of the budget, then each step as it is finished, partial results by half the budget, unfinished parts written as named inputs. One lemma per lane. Give the model a visible output budget where the API allows it.

**Why:** once, in a running project, several top-effort lanes on open proofs spent the whole output budget thinking and wrote no text at all, while narrower lanes at a lower effort all finished; a first pass at high effort followed by max effort on the existing text worked better than max from the start. With a hundred concurrent lanes, a burst of starts failed on the output-tokens-per-minute limit because each lane reserves its full budget at start.

**How to apply:** a lane that ends with no text is re-cut into one sub-claim per lane, never relaunched as is; twice truncated, move the target to a local agent that writes incrementally to disk. Launch in small staggered chunks and retry the failed ones. Lenses cannot run code; numeric tables are attached as files. Persistent local agents writing long files write in parts (statement and outline first, then appends), since a single response has an output cap too. Related: [[stop-reason-census-before-verdicts]], [[launch-hygiene]], [[launch-registry-pattern]].
