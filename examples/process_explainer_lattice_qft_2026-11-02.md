> One project's process explainer (an existence proof in lattice quantum field theory, 2026-11-02), written by the project's owner for colleagues who formalize proofs; reproduced verbatim below, its field, models and numbers included as illustration, not as defaults of this harness (see examples/README.md).
> It illustrates METHODOLOGY.md sections G (glossary), 1.11–1.13 (ledger axes, lines, the count), 2.12–2.15 (literature grades, image readers, confirmation versus certification), 4.19–4.24 (lanes, outside provers, prover format, briefs from the source), 5.18–5.22 (the closing rule, judge loop, writers, re-reads, edit lanes), 7.24–7.25 (self-checks, two leads), 9 and 10 (memory, safety), 12 (waves), 13 (writing), 14 (the ledger as a graph; the proof-assistant view).

# Our process

## 1. What this is

This project is a proof that a quantum field theory exists. The theory is scalar quantum electrodynamics in three dimensions: a charged scalar field coupled to a photon, defined first on a lattice and then taken to the continuum. The result is a long mathematics paper, about 2,500 pages, showing that the continuum limit exists and satisfies the Osterwalder–Schrader axioms, including invariance under Euclidean rotations. Many AI agents wrote the paper under fixed written rules; humans set the direction.

The proof is organised as a dependency graph of named statements, each with explicit hypotheses and an explicit proof state, so a formalizer can take it line by line.

## 2. The harness

Our **HARNESS** is the fixed set of written rules every agent works under. This includes:

- how a statement is stated: verbatim, with every hypothesis named, copied from its source rather than paraphrased;
- how a proof is checked: by independent agents told to break it before they are allowed to confirm it;
- what counts as done: a fixed list of status words, defined once, with an explicit closing rule (section 8);
- what may never be done: no silent weakening of a hypothesis; no number in a final text that no checker confirmed; no "as above" in place of a reference; no grade raised on the strength of a single reading;
- what the paper may contain: open items appear as named hypotheses and in one final "Open problems" section. The paper carries no trace of the process itself.

The rest of this note walks through the harness: how the agents are organised, how the ledger records what is proved, how a statement moves from open to closed, and how the write-up keeps that structure.

## 3. How the agents are organised

Every agent session starts from standing written briefings: files that load before the first prompt and say

- who the session is;
- what it is for;
- what it may and may not do;
- which files are read-only for it;
- the safety rules of the shared machine: no deletions, no searches of the whole disk, one process per job.

**Two kinds of agent.** Permanent agents hold the hardest lines of the proof across days, so nobody re-derives a long argument at every step. Short-lived agents do one task and end. Each gets a brief for that task (the target quoted verbatim, the inputs it may use with their status words, the files to read, the output format, the safety rules) and knows nothing else.

**Who decides what:**

- **Humans** set the direction and the goal. The goal is written once, verbatim, and is the only fixed item; everything else is a route.
- **One lead agent** chooses the routes, keeps the ledger, writes or commissions the briefs, launches the work and rules on verdicts. It asks the humans only when a final theorem's statement or hypotheses would change.
- **A second lead agent** runs one sub-programme (here, rotation invariance) with its own ledger and its own agents. It takes audit findings and suggestions from the first lead agent, and direction only from the humans.

**Memory.** An agent's working memory is finite and periodically cleared, so nothing important lives only there:

- a memory directory of dated rules, each with its reason, written the day the lesson was learned;
- a method-notes file of every procedure that worked, with the reason it works, read before every launch;
- the append-only ledger, so the state of the proof is read from the file, never from recollection.

**Self-checks.** Every half hour the lead agent checks that everything that can run in parallel is running, within the agent and memory caps, and posts a line only if it launched something or is blocked on a decision.

## 4. Agents: the details

- **Main agent:** Claude Fable 5.1, usually at xhigh effort. It runs as a long-lived session on a shared machine with 16 cores and 32 GB of memory.
- **Local subagents:** Claude Fable 5.1 at max effort, up to about ten at a time, each from a brief.
- **API lanes:** in addition to the local agents, hundreds of direct Claude API calls for self-contained tasks, Fable 5.1 at max effort with a large output budget (about 120k tokens). A lane that hits its cap is either rebuilt with a higher cap or prompted again for the continuation of what it did answer.
- **Outside provers:** OpenAI's gpt-6-astra at max reasoning and a Google model, used for self-contained questions in parallel with the API lanes on the hardest items (section 10).
- **Caps:** memory decides how many agents run; total usage is checked before every fan-out and kept well under the machine's limit.

## 5. The ledger

The **LEDGER** (also called the register) is an append-only record of every statement in play. Nothing is deleted or rewritten; a change is a new entry that supersedes an older one.

A **ROW** is one statement. It carries its name; its named hypotheses; its status; what consumes it and in which form; and which written text is its text of record. These are three separate axes (mathematics, consumption, text), and "closed" on one says nothing about the others: a theorem can be closed as mathematics while its written text still carries provisos.

A **LINE** is a thread of rows about one obstacle. A line opens when a defect or a missing statement is found, is numbered, and closes when the statement that fills it is closed. A line can be re-opened. The **COUNT** is the number of open lines. It is computed from the list of line numbers every time it is stated, never copied from the previous count.

The status words:

- **OPEN**: no proof on record.
- **OPEN BUT ALGORITHMIC**: the argument is proved and confirmed, and what remains is a certified computation that is guaranteed to succeed by refinement (section 11). The row stays open until the computed value lands and fits, but the count says which kind of wait it is: open mathematics needs a new argument; open but algorithmic needs only the run.
- **HYPOTHESIS**: a named statement assumed without proof. It appears in the hypothesis list of every theorem that uses it.
- **CLAIM**: one agent proved it. A claim, not a result.
- **DERIVED RELATIVE TO NAMED INPUTS**: proved, given named inputs that are themselves open or hypotheses.
- **READY TO CLOSE**: two independent adversarial confirmations exist; a text of record and one closure re-read are still owed.
- **CLOSED AS AN IMPLICATION RELATIVE TO NAMED INPUTS**: proved given its inputs, written up, re-read; the row gets a number.
- **VERIFIED**: at least two adversarial confirmations that postdate the last change of the text, or a literature statement checked at its printed source.

Three rows from the paper's ledger:

**Row: the cube-slice comparison.** Named inputs: the comparison on the free lattice (proved) and the two-member cube form (graded "sketched in the literature"). Consumers: the convolution comparison and the two-slice bound, both recorded as "closed, conditional on this row". History: open (only the free-lattice form was on record) → proved by several provers and confirmed by an adversarial pair → a text of record written for the paper, with one new clause → a checker found a gap in that clause → fix, re-check → closed with a fresh pair. The same day, the two consumers lost their "conditional" mark.

**Row: the photon residual at degree minus one.** Opening status: mismatch, meaning the record proved a different form (one that needs a non-negativity condition) and the degree-minus-one case was not covered. The note on the row: six other rows rest on a theorem whose input is this one, so check that their uses avoid the uncovered case. History: mismatch → final text → one part found to have a gap → second version → another round → closed on the fourth version.

**Row: the centre count for an inserted vertex.** History: closed on record → drafted for the paper and sent for approval → a fresh pair refuted the third version (two centres instead of one for one kind of insertion) → re-opened, pending a check of the true centre counts consumer by consumer → fourth version, approved and confirmed by a pair → closed.

One line of the rotation ledger was closed one evening (count zero), withdrawn half an hour later because one objection stood unrefuted (count one), and closed the next morning after thirteen pieces of text and a chapter audit; in between, the main theorems carried the mark "conditional on this line". The status words record each step.

## 6. Literature inputs

Literature inputs, meaning results from previously published mathematics papers that the proof relies on, carry grades of their own: printed with a legible proof; printed as a sketch; or merely asserted. A printed step that the project found not to follow gets its own grade and a replacement row. Some of the project's obstacles have been of this kind: making a published input precise enough to enter the ledger, and repairing small errors found in it along the way. One rule applies throughout: no row is graded above "derived" while any of its inputs is still a hypothesis.

## 7. The graph

The ledger and its rows define a directed acyclic graph. Every row points to the rows it depends on. A theorem's hypothesis list is its set of in-edges; its consumers are its out-edges. "Closed relative to named inputs" means the node is proved given its parents. The open hypotheses and the literature statements the proof uses are the leaves.

This helps:

- Find the rows that matter most: a row with many consumers, or one that the main theorem's "conditional on" mark passes through, gets the strongest checking and a permanent agent.
- Decide what is left: the open lines are the open nodes, the leaves are what the final theorem is relative to, and both are counted, not estimated.
- Trace a refutation: when a row is refuted, every consumer that used it in that form is re-opened or re-routed to a weaker form that is proved. A "mismatch" status means the record proves one form and a consumer uses another; we resolve it by proving the consumed form or re-routing the consumer, with a mechanical check that every consumer is still implied.
## 8. How a statement gets proved

Work runs in waves. In a wave every open front moves at once, and the pieces are then adjudicated together. The roles:

- A **BUILDER** turns the last adjudication into briefs: the target quoted verbatim, the allowed inputs with their status words, the attachments, the output format.
- **PROVERS** write proofs. A prover's output starts with its own status (proved, proved in a weaker form, partial, false), lists the inputs it actually used, numbers its steps, cites the input each step uses, and ends with the three steps it considers least secure. A proof by one prover is a claim.
- **REFUTERS** try to break the proof. Two refuters work on each proof, independently and in opposite orders through the text, so they are less likely to share a blind spot. Each looks for a false step, a step that uses more than its cited input states, a missing case, a constant that depends on a parameter it may not, a circularity with the target, or an unproved literature step used as if proved. Only then may it confirm. Its first line is one of four words: CONFIRMED, CONFIRMED WITH MINOR, GAP, REFUTED. A refuter may block only by exhibiting a false displayed sentence. For a GAP it must state the missing statement in a form that can become a new row.
- **READERS** check what the literature actually prints: at the page image, never from scanned text; a grade changes only when a second, blind reader agrees symbol for symbol.
- An **ADJUDICATOR** reads everything a wave produced and writes the rulings. It first lists every verdict mechanically and verbatim, and only then interprets. A verdict word is never an argument; the refuter's derivation is.
- The **LEAD** (a human-directed agent) rules in the ledger: status changes, re-routes, new lines, the next wave.
- A **WRITER** produces the **TEXT OF RECORD**: the prover's proof verbatim, with the refuters' minor corrections applied and marked, and nothing of the writer's own. Every number in a text of record is a number a refuter confirmed. (A writer once added three numerical remarks of its own; all three were false, and the re-read caught them.)
- One **CLOSURE RE-READ** checks that text as a referee would: that the corrections were applied, that the constants are the ones the proof gives, that nothing changed at statement level.
- Small fixes go through **EDIT LANES**: an agent produces byte-exact old/new replacements against the attached text, and a script applies them. Anything the agent could not place is listed for the lead to decide, never guessed.

A row is closed when a prover's text exists, two refuters with opposite work orders returned CONFIRMED or CONFIRMED WITH MINOR, a writer produced the text of record, and one closure re-read of that text returned CONFIRMED WITH MINOR or better.

We work in waves rather than one lemma at a time because the whole wave catches a wrong belief before anything is built on it. The first wave on a line produces a decomposition (named hypotheses and the implication between them); later waves prove, refute or retarget the pieces; the writers and re-reads come last. The whole structure is settled before any piece is polished.

## 9. How many checks, and how many rounds

- Two refuters per row. Each proof a prover writes for a row is read by two refuters, independently, before the row can move past "claim".
- One closure re-read of the text of record.
- At most one further re-read, and only if a hypothesis changed or constants were re-derived.
- Clerical items never cause another round: one CONFIRMED plus one CONFIRMED WITH MINOR counts as confirmed, provided neither names a false displayed sentence. The minors are collected into an edit list and applied.
- Disagreement between refuters is adjudicated, not re-run.
- A fix prescribed by a re-read at statement level is applied as a named clause ("relative to such-and-such"), never as a silent weakening.

## 10. Outside checks

Models from other providers are used as parallel provers and tie-breakers. Each receives a self-contained problem description: the definitions and the target copied word for word from the source, with none of the project's names, labels or terminology. It sees one problem, not the project. Its answer is a claim until two of our readers agree with it, and its agreement never replaces a refuter.

Every problem description is written from the source by one agent and checked against the source by a second before it is sent. The same rule applies to every brief inside the project.

## 11. Numerics and certification

Some bounds in the proof have explicit constants. For those a computation can do two different things, and the ledger keeps them apart.

- A **CONFIRMATION** is a cheap computation that checks the displayed inequality at the stated parameters: evaluate both sides and see that it holds.
- A **CERTIFICATION** is a more expensive computation that establishes the inequality over a range: a scan of the parameter set with a **Lipschitz or interval bound** controlling what happens between grid points.

The paper has both kinds: one constant is certified below a stated bound by a finite evaluation on a grid with Lipschitz control; one combinatorial census is a finite enumeration by script, run three ways with the same answer.

When the confirmation has passed and the certification is pending, the row is **CLOSED RELATIVE TO NAMED INPUTS**, and the certification is one of those inputs. The item that waits on it is counted as **OPEN BUT ALGORITHMIC**, not as open mathematics (section 5). This is still a proof in the same sense every other closed row is: nothing is hidden, and the status says exactly what was and was not checked.

A certification certifies that the displayed inequality holds at the **stated constants** for the **stated parameter set**. It does not certify uniformity in a parameter it did not scan, a reading of the print, or a hypothesis the computation assumed; those stay named. Whether a certification may ever stand in for the **second refuter** on a purely computational row is a question we have deliberately left open.

## 12. Deciding what is left and when it is done

What is left is a count, not an impression. The COUNT of open lines is recomputed from the list of line numbers at every status post and hand-off. A line is "ready to close" when the two adversarial confirmations exist and the text work is owed; it is "closed" when the closing rule of section 8 has run to the end. The main theorems carry a mark "conditional on" every line open at that moment; the mark comes off when the count reaches zero.

Zero open lines is not the end. What remains are the leaves of the graph: the named open hypotheses, if any, and the literature statements the proof uses, each graded by how much of it is printed (proof, sketch, or assertion only). The paper's final section lists them with the statement each is used for, so the reader gets the theorem, the inputs it is relative to, and nothing in between. Named hypotheses can also leave the list: one chapter of this paper carried a single named hypothesis until a class defined elsewhere was shown to cover it exactly; the citation was repointed, and the chapter now has none.

A clean build of the document is not a finished proof. Every hand-off carries the open count and the pointer to the ledger, and "final" is never said without them.

A count of zero can go back up. Once every line is closed, a fresh agent with no part in the proofs reads the finished text looking for gaps, and the writing itself turns up problems the proving did not. Either can re-open a line, and the count goes back up until that line is closed again, as in the rotation ledger example of section 5.

## 13. Writing

The ledger is formal: rows, named inputs, status words. The LaTeX is natural text. "As above", "the operator defined earlier", and a proper noun for an object defined somewhere in 2,500 pages make it hard to extract a chapter later and know which definitions it needs. We are experimenting with how to write the LaTeX so that the structure of the ledger survives in the text. This is a work in progress. The rules in force or proposed:

- **Every object is introduced in a labelled environment** (definition, convention, hypothesis) and referred to afterwards only by a cross-reference to that label. No "above", "below", "earlier" or "the usual".
- **Hypotheses are named items**, written once as labelled statements and listed per theorem, so a theorem's dependency list lives in the text and not only in the ledger.
- **Conventions sit in a conventions group** at the front of each part, with a self-test.
- **No process words in the LaTeX**: no line numbers, counts of checkers, rounds or status tags. Open items appear as named hypotheses and in one "Open problems" section.
- **A map from ledger row to theorem label** is kept beside the paper, so a row's text of record can be found from the ledger and a theorem's row can be found from the paper.
- **An extraction test** (proposed): a subset of the document is self-contained when every cross-reference target it uses lies in the subset. A script already checks labels and dangling references on the composed file; extending it to compute the reference closure of a chosen set of sections would make "can this chapter stand alone" a mechanical check rather than a reading.

Edits to the paper are staged as byte-exact old/new replacements, applied to a copy of the tree and never in place, then composed, checked for duplicate labels, dangling references and process words, and built. Every pass is logged with a checksum of the result.

## 14. Why this is Lean-amenable

The correspondences:

- a **ROW** is a `theorem` statement; its named hypotheses are its arguments; its consumers are the places the theorem is applied;
- the **LEDGER** is the project's set of declarations with their dependency graph;
- the status is the proof state: open, no proof term; claim, an unchecked proof term; closed relative to named inputs, a `sorry`-free body taking those inputs as arguments; verified, a second independent check;
- the leaves (named hypotheses, literature at the "asserted" grade) are the axioms the final theorem is relative to, and the ledger says which they are;
- the **COUNT** is the number of open goals;
- the **TEXT OF RECORD** is the frozen proof term: once closed, it changes only by byte-exact edits, each approved against the intention and the diff;
- statements are frozen before proofs: a target is quoted verbatim and may not drift while its proof is written, as a theorem's type is fixed before its body;
- a refuter's GAP must name the missing statement, which is exactly a new goal.

There is no machine-checked kernel. Inside a row, the proof steps are natural language, and they are checked by adversarial reading, not by a type checker. Two refuters can share a mistake, and literature inputs are read at the page, not formalized. "Verified" in this project means "checked twice by independent agents after the last change"; it does not mean infallible, and we keep checking.
