# METHODOLOGY (rules only)

How one lead agent, with whatever helpers the resource profile allows, proves a large statement by
splitting it into items, attacking every open item in parallel, reviewing every text independently,
and reporting honestly. Problem-agnostic: no field, project, person or machine is named here.
Imperative voice; every rule carries a one-line reason in parentheses where the reason is not obvious.

The parameters written in CAPITALS (REVIEW_LENSES, LANES_PER_PIECE, MAX_CONCURRENT_AGENTS, ...) are set in
`RESOURCES.md`. Rules that depend on a resource say so and give the fallback for the smallest profile
(one agent, no helpers). Nothing in this file requires more than one agent to be meaningful.

---

## 0. Keeping this file

0.1 Every method instruction the user gives goes into this file in the same turn it is given, as a
rule, without waiting for a reminder. Tell the user which rule it became. (Instructions that live only
in chat are lost at the next restart.)
0.2 Rules only. One rule per instruction. Item-specific logistics are not rules; the general lesson
behind them may be.
0.3 New versions of this file are written under the same name, with a dated changelog block at the
end. A rule once numbered is never renumbered; a retired rule is marked RETIRED in place. (Agents and
briefs cite rules by number.)
0.4 Where two rules conflict, the later-dated one governs for proof rules; for definitions, the
glossary governs.

---

## G. Glossary

GOAL: the one printed statement, with its hypotheses, that the project exists to prove. Everything
else is an item on the path to it.
ITEM: one statement on the ledger, with one owner who must prove it in full. An item's statement is
never changed; its proof may be re-cut.
LEDGER: the frozen, numbered list of items. Labels are never renumbered or reused.
CENSUS: the per-item state list (OPEN / DEPENDENT / CLOSED) with the counts. The census is kept by the
coordinator (or by the lead when there is no coordinator) and printed, never re-counted, by everyone else.
OPEN: the item's own owner still has something to prove or compute.
DEPENDENT: the item's own argument is proved and reviewed; everything it still waits on sits on
ANOTHER open item's list.
CLOSED: the item's own argument is proved and reviewed, and every remaining input is either proved or
owned by another open item. (Rule 1.4.)
NAMED INPUT: a statement an argument uses but does not prove, written out exactly, with the line that
consumes it, its owner, and its class word. A named input is never a hiding place: an input with no
owner or no exact consuming line is OPEN.
DISCHARGE LIST: an item's list of named inputs with the state of each. Nothing leaves it until proved,
printed or certified.
CLASS WORDS of an input: (a) PROVED (and reviewed); (b) NAMED READING: a reading of a printed source,
with page and line quoted; (b) NAMED COMPUTATION: a computed number with a stated error bound;
(b-alg) OPEN BUT ALGORITHMIC: proved and reviewed up to a certified computation that is guaranteed to
succeed given enough compute (only the cost is uncertain); (c) OPEN MATHEMATICS: a step with no proved
route. Statuses print algorithmic and mathematics as two separate lists.
LOCATED: an open-mathematics input whose exact failing step is named (the clause, the objects, the
line it must deliver).
ROUTE: a method expected to prove an input. A route is CLOSED when refuted; closing a route never
closes the item.
TRUTH WORD: the owner's belief about an open statement with its evidence ("expected TRUE, evidence:
numerics at three sizes, margin 40x" or "in doubt; under numbers").
CONSUMER, CONSUMER LINE, CONSUMED FORM: the later step that uses an item's conclusion; the exact line
(file:line, quoted verbatim) where it does so; the statement in exactly that form (direction, sign,
which norm, which set, which scale, which quantifiers).
CONSUMER'S OWNER: the owner of the item holding the consumer line. A prover's result enters the record
only after the consumer's owner confirms, in writing, that its form is the consumed form.
EVIDENCE: a number or model result that supports a truth word and proves nothing.
MODEL: a simplified object; results about a model are about the model.
PROPOSAL: a prover's reading, class word or form change until the consumer's owner (and the
coordinator, where the census moves) confirms it. In posts a proposal is "under review", never a result.
TEXT: a theorem file, versioned by name (v1, v2, ...), never edited in place.
ERRATUM: a cure of review findings on a text, as a new file. CORRECTING if a mathematical item changed;
CLERICAL if only wording, citations or display digits that move no bound.
LENS: one independent review of a text. PAIR: REVIEW_LENSES independent lenses on the same text (default
two: lens A tries to break it, lens B reconstructs it without seeing A).
VERDICTS of a lens: APPROVED / APPROVED_WITH_MINOR / NOT APPROVED, each blocking item classed CLERICAL
or MATHEMATICAL. VERDICTS of a prove lane: PROVED / PROVED-WEAKER (the exact weaker statement) /
REFUTED (the counterexample) / NOT PROVED (the failing step).
LANE: one independent run of a model on one exact task with its attachments. POOL: a set of prove
lanes on one statement. LANDING: a lane's output arriving.
LEAD: the orchestrating agent. OWNER: the agent that must prove one item. PROVER: an agent or lane
asked to prove one statement. COORDINATOR: the agent that keeps the census and rules on class words.
CLOSER: an agent that pre-checks an item's files before booking. EDITOR: an agent that writes the
public document, outside the proving staff. In the smallest profile one agent plays every role in turn.
MEMO: an agent's append-only state file with a TO RESUME section at its end. ONBOARDING: the file a
successor reads first.
BOOKING: the lead's entry in the ledger that a result is of record.
AXES of a ledger line (added 2026-11-02): (1) the STATUS axis, what is proved; (2) the CONSUMPTION axis, what
consumes the line and in which form; (3) the TEXT axis, which written text is the TEXT OF RECORD. "Closed" on
one axis says nothing about the others.
TEXT OF RECORD: the one written proof text a line's status rests on: the prover's proof verbatim with the
confirming lenses' minors applied and marked, and nothing else.
STATUS LADDER (optional; finer than OPEN / DEPENDENT / CLOSED, for projects that want the confirmation state
visible on the line): OPEN; HYPOTHESIS (named, no proof attempted); PRINTED / SKETCHED / ASSERTED (what the
literature gives, graded by whether the proof is printed and legible, only sketched, or only asserted);
PROVED-SINGLE (one lane or agent; a claim, not a result); DERIVED rel. {named inputs}; CLOSED-READY (two
adversarial confirmations exist; a text of record and one closure re-read are owed); CLOSED rel. {named inputs}
(numbered in the tally); VERIFIED (two adversarial confirmations postdating the last change, or a printed source
checked at the page).
REFUTER: a lens told to refute first (a false step, an over-read of an input, a missing case, a constant
depending on a parameter it may not depend on, a circularity with the target, an unprinted step smuggled in) and
to confirm only when nothing refutes. Two refuters on one text take OPPOSITE WORK ORDERS: they read the same
target from both ends.
CLOSURE RE-READ: one lens on the text of record after the writer: it checks that the minors were applied and
nothing else changed, re-reads as a referee, and rules on every item the writer stopped on.
WRITER: the agent that produces the text of record. It adds nothing of its own.
EDIT LIST: a byte-exact list of Old/New blocks against an attached text, headed `STATUS: EDITS n`, with a
`Lead decisions` section for anything the lane could not place; applied by script to a copy, never by hand and
never in place. EDIT LANE: the lane or agent that produces one.
WAVE: one round of the pipeline of section 12: a builder, then provers, refuters and readers in parallel, then
one adjudicator, then the lead's rulings, the writers, the closure re-reads and the edit lanes.
BUILDER: the agent that turns an adjudication's proposals into lane specs. ADJUDICATOR: the agent that reads
every output of a wave and writes the mechanical verdict list first, then its interpretation, the ledger deltas,
the count and the next wave's lane list.
PERMANENT AGENT: a persistent agent that holds one line across waves, with its own lanes and memo.

---

## 1. The goal and the ledger

1.1 Fix the GOAL as one printed statement with its hypotheses. Everything else is an item on the path
to it. State the goal to yourself before every decision that could be answered by it.
1.2 Keep one frozen, numbered ledger of items. Never renumber or reuse a label; splits get suffixes
(.04a); new items are appended and flagged NEW. (Progress is only countable against a frozen list.)
1.3 Give every item a line: exact statement; the consumer's sentence verbatim with its location; the
criteria for CLOSED; owner; state; named inputs with their class words.
1.4 CLOSED means, strictly: (i) the item's own argument is proved and has passed its review pair; (ii)
every remaining named input is either proved, or a printed fact with page and line quoted, or a
certified number with its error bound and room at least ten times that bound, or owned by ANOTHER open
item and on that item's list. An item whose own owner still holds any input, however well staffed, is
OPEN and prints "OPEN: own inputs left x".
1.5 DEPENDENT only if everything the item waits on sits on ANOTHER item's list. Any remaining part of
its own keeps it OPEN. (An item booked DEPENDENT on its own parts is a reduction, not progress.)
1.6 Keep a discharge list per item. Every named input stays on it until proved, printed or certified,
and has an owner and a live effort at all times. The moment an input has neither, the item prints OPEN
with no grace period.
1.7 A reduction to a new unproved statement closes nothing. Log it, do not count it, and the same owner
continues.
1.8 Every status leads with the count: "open N of M, dependent D, closed C; open algorithmic a / open
mathematics m".
1.9 When a status rule changes, re-classify every item under the new rule in the next census and print
the change with its cause.
1.10 A census move (OPEN to CLOSED, or back) is booked only when every gate is met by a file on disk,
named exactly and quoted. Correct the count the moment a rule shows it was wrong, even upward.

1.11 (added 2026-11-02) Give every ledger line its three AXES: status, consumption, text of record (glossary).
Book "closed" per axis; a line CLOSED as mathematics whose text of record still carries provisos says so. (A
closure booked from verdict tables alone turned out not to be a printable proof; the text axis makes that gap
visible on the line.)
1.12 (added 2026-11-02) Number the CLOSED tally. Every hand-over and every status carries the open counts and the
ledger's path. "0 open" on a build means the build is clean, not that the proof is finished; say which.

---

## 2. Before proving anything

2.1 PIN THE OBJECT in one line: the set, the scale, the units, the normalisation, the orientation of
every ratio, which norm. Every target repeats it.
2.2 QUOTE THE CONSUMER verbatim with its location and write "consumed form = ...". Check the target is
not stronger than what is consumed (a stronger clause is struck, not proved) and not weaker (a loss, a
sub-class, a different domain). Re-read the consumer whenever a proof keeps splitting into cases. (A
form was once proved for a day while the consumer used a different object that needed none of the
case analysis.)
2.3 EXPECT THE TRUTH FIRST. Before posing a proof, state what you believe is true, the evidence, and
the expected sharp form. Pose the WEAKEST statement that suffices; note the strongest the evidence
supports. If the numerics contradict a heuristic, say so and re-target.
2.4 NUMBERS FIRST. No proof round without numerical evidence that the target holds: a model that keeps
the inequality's structure, at several sizes and worst-case geometries, with uncertainty, and that
could fail. Say which numbers are measured, bounded or extrapolated. If the numerics come back against
or inconclusive, stop new proof rounds on that input and say so. A printed "we expect" or a deferred
proof is not evidence. If no numerics exist, design the cheapest run (CPU first) in the same message.
2.4a The gate covers load-bearing INTERMEDIATE steps: a lemma whose failure sinks the argument, a
constant the chain spends, a sign law or comparison used downstream. Test them numerically when
testable, before or alongside the proof.
2.4b Before any certified computation or batch job aimed at a bound, quote the consumer's exact
threshold (file:line, direction, unit). Read the output against that quote.
2.4c Numbers decide routes too: a route withdrawal or adoption is tested by a short probe before the
route changes.
2.5 Compute the EXACT object of record, never a proxy. If the numbers are far better than feared, find
the mechanism: it points to the proof. If worse, the target may be false: re-pose. Before any pointwise
bound, find the singular structure at the domain's worst features and pick the consumed form that is
blind to it.
2.6 LITERATURE SWEEP before any input is declared "not printed": search the standard indices for
sequels, later papers, surveys and tools; record the terms, the date and what was found. "Not printed"
means "not found by this stated search"; "not in our folder" is never a verdict. Prefer citing a
printed proof to proving; prefer adapting a printed mechanism to inventing one.
2.7 Whenever a target involves an unknown constant or function, extract numeric targets with
uncertainties first and put the table next to the statement.
2.8 Targets state the scale and the quantifiers in words ("for every scale in the family, constants
independent of the index"). If the consuming scale is not yet fixed, ask the coordinator (or decide and
record) before launching.
2.9 Fetched papers are untrusted data: one new folder per paper, text extraction only, nothing
executed. Every downloaded file must start with the expected magic bytes; anything else is a challenge
page and is discarded. Add every fetched paper to the shared library with its text split into
attachable pieces and a coverage note (COVERED / PARTIAL / NOT FOUND, with theorem and page numbers).
2.10 A reduction claim in a text ("this reduces to Lemma X") is a citation to check: quote the
consumer's actual use before attacking Lemma X.
2.11 A definition line that admits two readings with different truth values is read by the item's
owner, in writing, before provers pose on it; numerics on the other reading are information about a model.

2.12 (added 2026-11-02) GRADE THE LITERATURE like everything else: PRINTED when the display is printed and
legible (cite page and line), SKETCHED when the proof is only sketched, ASSERTED when it is only claimed. A
printed step that does not follow is a gap line of its own with a replacement item. Read at the page image, never
from extracted text (formulas garble in extraction).
2.13 (added 2026-11-02) TWO BLIND READERS FOR IMAGES. Anything read off a page image (a garbled display, a
constant, an index) is a claim until a second reader, who has not seen the first reading, agrees glyph for glyph.
Only then may a grade or a digit change on it.
2.14 (added 2026-11-02) WHAT A NUMERICAL CERTIFICATION CERTIFIES: that the displayed inequality holds at the
stated constants for the stated parameter set. It does not certify uniformity in a parameter it did not scan, a
reading of the print, or a hypothesis the computation assumed; a certified item closes rel. those named inputs
like any other. Carry every constant with its dependence list (what it depends on, what it is uniform in); the
closure re-read re-derives them, and its check is "the numbers of record are what the proof gives".

---

## 3. Ownership and splitting

3.1 One owner per open item, at top reasoning effort. Its FIRST task is to prove the item in full, as
stated, with the consumer line verbatim. Never two owners on one part. (In the single-agent profile,
"owner" is the hat you wear while on that item; the rule still fixes the order of work.)
3.2 Split only when the item is far from a proof after the owner's first full pass, and only if ALL six
criteria hold: (1) each part has its own statement written in advance and a fixed assembly; (2) parts
can run in parallel now (on inputs of record or other parts' statements, not their proofs); (3) each
part is checkable on its own; (4) no process steps as parts (checks, approvals, write-ups belong to the
part they serve); (5) the split follows the proof's structure, and case splits count only when each
case is independent; (6) each part is worth at least one agent or lane.
3.3 PROVE, NEVER REDUCE. Grades are PROVED / PROVED-WEAKER (exact statement given) / REFUTED (with the
counterexample) / NOT PROVED (the failing step). "Derived given X" is allowed only when X is already of
record. When a result comes back "derived given H1..Hn", the next step is to prove each Hi or cite it,
numbers first; a new named input is filed only after the proof routes have been tried and each
failure stated.
3.4 Big and small items. A big item (far from a proof after the first full pass) keeps a persistent
owner plus LANES_PER_BIG_ITEM parallel prove lanes. A small item gets LANES_PER_PIECE lanes per open
part and no persistent agent. The level of parallel effort an item reaches is a floor until it closes.
(Fallback without lanes: the owner itself cycles through distinct routes, one per pass, and records
each route's result before starting the next.)
3.5 Where resources allow, run an independent whole-item prover alongside the owner. Its result counts
only when every input is printed or of record; reliance on the item's own pending parts is a reduction.
3.6 Parts are mathematics only; checks and bookkeeping are never parts or pool pieces.
3.7 Add a closer to any item with many failed review rounds. It pre-checks every file (digits by its own
script, every quote opened at its line, scope and grade words) in parallel with the review; book only
when both pass.
3.8 When an item resists (about five failed rounds or six hours open), name it and separate the cause:
bookkeeping or digit slips (fix the process: script-built files, verbatim post-checks) versus open
mathematics (state the step and the staffing). Then run the numerics gate again.
3.9 Every open item has one persistent owner, resumed at every landing and never left unowned. The
owner directs the literature review for its item.
3.10 The owner is both the whole-item prover and the orchestrator of its parallel lanes: it files a lane
line for each open piece the moment the piece's statement is fixed, refills on every landing, and keeps
proving the whole item meanwhile.
3.11 DEFAULT PARALLELISM. Every open piece of every open item has LANES_PER_PIECE lanes running in
parallel at all times. A piece without lanes carries its reason in the ledger and the status, re-checked
at every landing. (Fallback: a piece without a live route carries the reason.)
3.12 Every open-mathematics input gets one persistent dedicated prover the moment lanes land GAP on a
located step; "no date" is never reported for an open input. The dedicated prover's route decision is
a ledger line within its first hour; it proves in full or BYPASSES (a consumer-side reading under which
a weaker, already proved statement suffices), and a bypass counts only on the consumer owner's written
confirmation. "Close this as soon as possible" from the user means a dedicated prover the same turn.
3.13 The lead orchestrates; owners decide strategy. The lead sends owners logistics (launches, landings
verbatim, resources, deadlines), direction and needs (priorities, closing criteria, numbers first,
prove before naming), and cross-item information marked as information. It does not prescribe proof
routes. (The owner holds the full technical picture of its item.)
3.14 The lead also does mathematics directly when it unblocks an item: short calculations, numerical
checks of a claimed bound, quick derivations, handing results to the owner as information.

---

## 4. Parallel provers and lanes

(Applies when LANES_PER_PIECE > 0, i.e. API keys or spare subagents exist. In the smallest profile,
read "lane" as "a blank-context subagent you spawn and wait on, or one fresh pass by you": write the
task line as if for a lane, then run it that way. Waiting on one helper keeps working concurrency at
one (8.2).)

4.1 POOL FORMAT: one lane = one final statement to prove exactly as written, with the pinned object,
the consumer line, the scale and quantifiers, the needed definitions attached as text (not pointers),
and the grade list. No "check X" or "reduce X" pieces in pools.
4.2 At least LANES_PER_PIECE independent lanes per piece, with distinct methods, never duplicate
prompts; refill in the same turn a lane lands, aimed at what the landed lane showed; never let a pool
sit at zero. A refill re-cuts LANDED pieces first; a NEW target passes the numerics gate before launch.
4.3 NARROW TARGETS: one lemma per lane. A broad "prove the whole theorem" lane spends its entire output
budget thinking and returns no text.
4.4 WRITE-EARLY RULE in every lane brief: the result section (statement, status word, the failing step
or the proof skeleton) within the first quarter of the budget; then each step as it is finished;
unfinished parts written as named inputs, not left silent; partial results by half the budget.
4.5 Empty or truncated twice: split by the failing structure the partial text shows, or move the target
to a local agent that writes incrementally to disk.
4.6 STOP-REASON CENSUS at every landing BEFORE reading any verdict. A lane that stopped on its output
limit, refused, or wrote no numbered finding is NOT LANDED: its summary claims are not of record; a
status line written early is a claim about the end, not a result. Compare the exported count with the
requested count. A verdict cut by a transport error is TRUNCATED, not a pass.
4.7 Check every lane's attachment count and total size against the builder's limits before launch;
dry-run every build; if a lane says "not in the excerpts", suspect the builder first. Every line a
verdict will quote must sit inside an attached range; the text under review is attached LAST and whole.
4.8 Launch as tracked background jobs that notify on exit, one lane per run so each landing is
replaced alone; never fire-and-forget; never a waiter whose own command line matches its own pattern.
4.9 Set the top reasoning effort for provers, writers and syntheses through the actual API or tool
PARAMETER, not by prompt text. Audit the effective effort before relying on a verdict. After an
oversight, raise that line and re-audit its last outputs.
4.10 REPAIR LANES carry the verdict's FULL required list, never the headline alone, and the repaired
text is diff-verified. After two failed repair rounds, hand the piece to an owner with judgement.
4.11 Owners write lane lines; one launcher launches them (the lead, or the owner from a reserved ID
block). Every lane, file and pair gets a never-reused ID; check the ID is free before launch.
4.12 Prompt size caps: prove prompts ≤ PROVE_PROMPT_CAP; text reviews ≤ REVIEW_PROMPT_CAP; attachments
ranged (file:a-b), each ≤ ATTACHMENT_CAP; shared definitions written once in the header. (Defaults in
RESOURCES.md; the point is that nothing load-bearing is cut silently.)
4.13 Lenses cannot run code. Numeric tables come from a local agent or a batch job, attached as a file
the lens can check by hand at a few points.
4.14 Drafting and literature-reading tasks go through a prover-style lane (which produces a text),
never through a review wrapper (which judges an existing text and returns "deliverable absent").
4.15 A refused lane is a lost lane: bisect its content (statement alone, then half the attachments)
rather than guessing at words; re-issue under a new ID; never relaunch as is.
4.16 Rate limits: each lane reserves its full output budget at start, so bursts of starts fail. Launch
in small chunks staggered by a minute or two, retry the failed ones, and report when a pool cannot hold
its level. With several launching agents, use a shared append-only launch registry (see
optional/launch_registry).
4.17 A lane's letter, index set, domain and rounding direction are part of its target: state the
domain on which the consumer takes the quantity; state whether a sup or an inf; state up/down rounding
for every displayed digit.
4.18 An outside prompt (a published problem statement, a question to another model) is written by a
strong-model agent from a brief, never drafted by the lead; before it goes out, one independent check
quotes the consumer line and compares direction, sign, every ratio's orientation and the units with
the prompt's target. An outside answer that makes an open step easy gets the same orientation check
before it is reported as progress. Freeze the content at a fixed time and send with an "as of" note;
later results go as a separate addendum.

4.19 (added 2026-11-02) ATTACH BY ABSOLUTE PATH, and dry-run the build from the SAME directory the runner uses;
test every attachment path for existence before the run. (A relative path passed a dry-run from one directory and
failed in the runner's; a spec that named a future file under a guessed name failed the whole build with no
output.) Never guess the name of a file a writer has yet to produce: instantiate the spec when the file exists.
4.20 (added 2026-11-02) OUTPUT-CAP FLOORS. A lane that returns no text with the stop reason "output limit" has
spent its budget on reasoning: rebuild it at a higher cap, never retry at the same one. Give edit and repair lanes
a floor well above a prover's typical need (one project used 48k, and 64k to 96k when the text was over 50 KB or
the list long).
4.21 (added 2026-11-02) ONE RUNNER PER GROUP where the runner processes its groups sequentially: several groups in
one call serialise, and the later ones sit idle. Read every landed verdict for "cut at" or "ends at line N"
phrases before ruling: a text cut by the attachment cap produces a GAP that is the builder's, not the proof's.
4.22 (added 2026-11-02) OUTSIDE MODELS. An answer from a model outside the lane system is a CLAIM until two readers
confirm it from the record text, never from the answer; it is a third voice beside a refuter pair, never a
substitute for a refuter. Packets to it carry definitions VERBATIM from the source (a lead's paraphrase misled an
outside prover twice), written by a top-effort writer and checked by a referee before sending; no identifiers,
names, paths or keys; when the record has two objects under one name, the packet says which. Check the run's
output flag (zero output; partial with reasoning at the cap) before reading its answer, and rerun with a larger
cap.

---

## 5. Review

5.1 Every load-bearing text gets a PAIR of REVIEW_LENSES independent lenses: lens A tries to break it;
lens B reconstructs it without seeing A. Both quote the consumer line and check that the closing
statement matches it. (Fallback at a cap of 1: a blank-context subagent as the lens while you wait,
one lens at a time, or two separate fresh-context passes by you, A then B, each without the other's
notes; with subagents: two fresh subagents.)
5.2 VERDICT WORDS: APPROVED / APPROVED_WITH_MINOR / NOT APPROVED, with blocking items numbered and a
"required for approval" list; the lens classes EACH blocking item CLERICAL or MATHEMATICAL. Lens
vocabulary stays inside the review files.
5.3 CLERICAL = a citation or line number, a digit or rounding that changes no conclusion and drops no
room below its criterion, wording, a stale label, a build defect, a missing retraction. MATHEMATICAL by
default = a false step, a wrong object, a missing or changed hypothesis or scope, an unproved claim, a
change in a quantity's size, a missing named input, the supply status of a named input, a false
displayed constant even when harmless, a lapsed guard clause ("pairs pending"). No "clerical by exception".
5.4 ONE-NOT RULE: one NOT whose blockers are all clerical, with the other lens approving, counts as
PASSED: fix by erratum under a new name, log it in the clerical ledger, give the erratum one diff-only
lens before the pass is booked; sweep the ledger about every ten entries and before any touched item
books CLOSED. One NOT with any mathematical blocker is NOT a pass. Both NOT with any mathematical
blocker = rejected; re-cut.
5.5 BOTH-NOT CLERICAL RULE: both lenses NOT, every blocker of both clerical, mathematics confirmed by
both: PASSED exactly as under 5.4 (erratum, ledger, one diff lens), no re-pair. Any doubt about a
classification: re-pair.
5.6 A CORRECTING finding (a mathematical item changed) means a new version under a new name and a full
re-pair; the confirmed core is carried verbatim; the surviving part is named by kind. A pair that
confirms a text's lemmas and NOTs its assembly on form items corrects the assembly only.
5.7 Classify and relay EVERY blocking item one by one; count the items in the relay against the file.
Never relay only the "most serious" line.
5.8 PARALLEL RE-REVIEW: when a review corrects an owner, resume the SAME owner with the verdict
verbatim; the owner files the fix and names it at once; the new review launches immediately; the owner
self-checks in parallel; book only if both pass.
5.9 STANDARDS BY STAGE: each piece gets one review pair; the ASSEMBLED argument gets a full pass (a
review pair plus, where available, two local reviewers who also check the bookkeeping: every input on
record or on the list, no item forgotten) at about half assembly and again at the end.
5.10 Refuters may run below the provers' effort when a claim is highly questionable (it should be easy
to break); provers, writers and syntheses stay at the top.
5.11 An independent whole read of a "closed" item, before and after booking, where resources allow.
5.12 ERRATA HYGIENE. Every anchor quoted character-exact from the line, never from memory; every digit
by script, rounded in the safe direction (upper bounds up, lower bounds and thresholds down), the
script's output line quoted; every line citation grep-verified before the lens; a withdrawal propagated
to every occurrence in the whole text; an erratum adds no sentence beyond the cure; an erratum rewrites
in full any line whose intermediates it changes. A text's status/grade/scope lines are copied by script
from the body's theorem statements, never re-worded.
5.13 CLERICAL ECONOMY. Clerical-only findings ride along with the next substantive file of that text
(no stand-alone erratum, check or relay), except when a pass is booked on a clerical-only NOT (5.4/5.5).
Owners and provers spend their turns on the mathematics.
5.14 An owner's own proof is paired BEFORE any statement of record, price or booking is written on it.
5.15 A review pair is launched only on a text that a consumer line reads (quote it in the pair
source); model results and errata to unconsumed digits get no pair until a consumer names them.
5.16 Any lattice-sum or counting formula gets a second independent enumeration before its digit books.
Any certified evaluator is cross-checked against a float evaluator at three or more sample points
spanning the domain, including one beyond the formula's domain, before a full run.
5.17 Nothing is booked on a NOT. A lens's PROPOSED constant or formula gets the numbers check before
adoption. A one-lens confirmation is not a closure.

5.18 (added 2026-11-02) CLOSURE BY ADVERSARIAL CONFIRMATION (for projects on the status ladder). A line is CLOSED
when: (i) a prover's text exists; (ii) two REFUTERS with opposite work orders returned APPROVED or
APPROVED_WITH_MINOR on it, both postdating its last change; (iii) a WRITER produced the text of record (the proof
verbatim, the refuters' minors applied and marked, nothing of the writer's own); (iv) one CLOSURE RE-READ of that
text returned APPROVED_WITH_MINOR or better. A refuter blocks only by exhibiting a false displayed sentence. Fixes
the re-read prescribes at statement level are applied as NAMED CLAUSES ("rel. (H-k)"), never as silent weakening;
a hypothesis-level change costs exactly one further re-read; an editorial change costs none and goes to an edit
lane. No line rises above DERIVED while any input is a HYPOTHESIS.
5.19 (added 2026-11-02) THE JUDGE LOOP. One APPROVED plus one APPROVED-with-clerical-fixes is a confirmation when
neither names a false displayed sentence; the clerical items become an edit list (5.4 is the pair form of the same
rule). Disagreement is ADJUDICATED, not re-run: one adjudicator writes the mechanical list of first-line verdicts
verbatim before any interpretation, and the lead rules on the ledger with that list attached; an adjudicator's
count is never carried without it (one adjudication recorded "PROVED x4" where the lanes had said REFUTED and
PARTIAL). Grade words are never arguments; a lens's derivation is. Re-reads are kept for two cases only: a
hypothesis-level change, or a text whose constants were re-derived.
5.20 (added 2026-11-02) THE WRITER ADDS NOTHING. Every number in a text of record is a number a refuter confirmed;
a writer's own parenthetical, example or remark is a defect (a writer once added three false numerical asides,
and the closure re-read caught them). The writer stops, marked "lead decision", on anything that would change the
statement, an input or a constant's dependence, and lists every minor it applied with the old and the new text.
5.21 (added 2026-11-02) A PRESCRIPTION IS A CLAIM. A lens's prescribed replacement statement is applied verbatim
but stays PROVED-SINGLE until the next re-read checks it; never promote it on the strength of the prescribing
lane. After two failed repair passes on one text, stop patching: a fresh prover from the corrected hypotheses,
then two refuters (chains of prescriptions accumulate defects; 4.10 gives the general form).
5.22 (added 2026-11-02) EDIT LANES AND TRIAGE. Before a re-read is launched on a new version, read the edit lane's
`Lead decisions`: an item "not applied: source not in the excerpts" is a GAP in waiting, so run the repair again
with the source attached, and attach every file a ruling cites when the lane is built (the ruling's words are not
enough to write the New text). After every editorial pass, one triage agent classifies every `Lead decisions`
item of every edit output against its re-read as REQUIRED / OPTIONAL / DONE before any item books at the new
version; REQUIRED items at hypothesis level become named clauses and the ledger line is amended in the same step.
An APPROVED_WITH_MINOR re-read can carry REQUIRED statement-level items: rule on each explicitly at closure, never
leave them to a wording-only lane.

---

## 6. Bookkeeping

6.1 One coordinator of record (or the lead) keeps the ledger and the definitions. Definitions of record
are appended as numbered lines, never edited in place; each new line gets a one-lens check.
6.2 Census before every status: per item its state, its named inputs with owner and live effort, and
the resource counts. Flag any item or input at zero effort and fix it in the same turn.
6.3 NO DELETES, NO OVERWRITES of anything of record: new names only; append-only logs; superseding
files carry new names and the ledger says which governs; outputs that failed a format check are marked
"not of record", never removed. A job's own temporary intermediates may be removed by the job that made
them, by a result-gated last step named in its memo, never by a glob over a shared directory. When in
doubt whether a file is temporary, it is not. (RESOURCES.md may loosen this; the default is strict.)
6.4 TIMESTAMPS COME FROM THE CLOCK: every stamp is copied from a clock call made in a separate, earlier
step; never estimated, never rounded forward; file names likewise; scripts compute their own stamps at
run time. A stale stamp is acceptable; a future one never. A new file's name enters a message only
after the write has printed it.
6.5 RELAY VERBATIM: when relaying anything a ruling or proof will rest on, quote the load-bearing
sentence with its location, then paraphrase; never add a condition, fallback or "otherwise" the source
does not state; announce a relay error to everyone downstream and hold the dependent relays.
6.6 STATE ON DISK: every persistent agent keeps a memo with a TO RESUME section; an owner that ends
leaves it current; resumes carry the verdicts verbatim; a fresh owner starts from the memo.
6.7 The lead books passes; owners never book their own.
6.8 ROAD TO CLOSE: every per-item update places the piece it reports in the item's remaining list
("step k of n left"); at least hourly, each followed item gets its ordered list of what must still be
true for CLOSED, with the current position marked and which step unlocks which.
6.9 PROGRESS AS COUNTS: every status and report gives per item "pieces left x of y; named inputs left
x of y = proved a / live route b / open mathematics c". Never "basically done", "only bookkeeping",
"just a few inputs", "one step short" while any input of kind (b) or (c) remains; name the kind-(c)
inputs first.
6.10 COMMS AUDIT at every status (tools/comms_audit.py or by hand): lanes cut at the output limit
(void or truncated), refusals, API errors, lost lanes, unexported outputs, prompt cuts, missing
attachments, brief pointers past a file's end. Every flag goes to its owner the same turn.
6.11 HAND-OVER HYGIENE: every file name in a brief or TO RESUME is tested for existence by exact name
before it is sent; briefs are built from one template with the current methodology version
substituted, never pasted from an older brief; a brief names roles, never stood-down agents; a
hand-over lists every lane whose landing will wake the OLD agent, and the old agent forwards one line
per landing.
6.12 Every absence claim ("0 hits", "not in the record", "missing display") is a LOGGED check with its
exact search, so it can be audited; name the last line read.
6.13 One shared count is computed once, by one owner, and quoted by everyone else with its file:line.
6.14 Ledger citations are by block time stamp, never by line number alone (line numbers in an
append-only file get mis-copied).
6.15 A "spawned" or "launched" word is written only after the tool's result prints (the agent id; the
launcher's "launch at" line), never from the brief's existence or a schedule.
6.16 Every computed digit entered anywhere carries its instance (size, parameters) and its provenance
(object, script, line); a digit computed at another instance than the consumer's is robustness
information, never the row's digit. A truth digit whose provenance turns out to be a different object
is re-labelled EVIDENCE the same hour.

6.17 (added 2026-11-02) COUNTS ARE COMPUTED, NEVER COPIED: every count line is produced by counting the id list in
the same step (a one-line script over the list), never typed from the previous count (a copied "12" stood for a
13-id list through several versions). 6.13 says who computes a count; this says how.
6.18 (added 2026-11-02) EDIT LISTS ARE APPLIED BY SCRIPT to a copy of the tree, never by hand and never in place;
each Old must occur exactly once (assert it); the result is composed, census-checked (duplicate labels, dangling
references, process words) and logged with its checksum; hunks are verified against the CURRENT tree before they
are sent (a hunk cut against an older version fails to apply).

---

## 7. Autonomy, decisions and communication

7.1 NEVER IDLE. When a resource is free and a decision is pending from the user, choose the most useful
feasible option yourself, start it, and tell the user which option you chose and that they can
redirect. Waiting on a decision is wasted capacity when a sensible default exists. "Waiting" is never
an answer while any piece can be drafted, checked or computed in parallel.
7.2 HOLD ONLY FOR the items in RESOURCES.md HELD_DECISIONS. Default list: spending money or handling
keys; heavy local compute while LOCAL_COMPUTE is light; submitting to a scheduler while BATCH_USE is
not agent; changing settings, hooks or configuration; and changing a final theorem's statement or
hypotheses. Everything else is yours to decide and report.
7.3 THE QUESTION FILTER, run in order before asking the user anything: (1) state the GOAL to yourself in
one line; does it answer the question? (2) does this METHODOLOGY answer it? Quote the rule to yourself.
(3) does the question change a final result's statement or add a hypothesis? Ask only if (1) and (2)
do not decide it, and say in the question why they do not. Otherwise apply the strict reading and TELL
the user what you decided.
7.4 QUESTIONS IN PLAIN FORM, short: the plan said X / we found Y / we do not know Z / options (A)/(B)/
(C), each saying whether the main result stays unconditional / recommended, with one reason / default
if no answer, with the time you will act on it. No symbols beyond the one number that matters, no
internal names.
7.5 DECISION POSTS ARE THREE LINES: (1) the fact, (2) your call and its default with the time, (3) the
one thing you need from the user, if anything. Act first when the action is within your permissions.
7.6 SAY PLAINLY what is proved, what is computed, what is assumed, and how each assumption gets proved.
When the user is right, say so and give the cause. Correct the count at once, even upward. Admit time
lost, with the cause.
7.7 EVERY STATUS ITEM IN FOUR CLAUSES: Done (finished, with its verdict) / Open algorithmic (n): the
certified computations and reviews with their gates / Open mathematics (m): each named input with its
route state (no route / located / pool running / text and pair owed) / Now (who is doing what,
expected when). Nothing else under "open".
7.8 A RUNNING COMPUTATION IS AN ATTEMPT until its gate passes: never "X runs" or "every remaining
computation is running"; say "an attempt at X is running", name the gate it must pass, and the known
ways it can fall short.
7.9 NAME THE KIND whenever a post says "evidence", "not proof-grade", "empirical" or "not reachable":
open mathematics with a located step; a computed input whose certification is incomplete; or a
reading of a printed line still to be quoted. For a computed input, say what is proved, what number is
missing, the options, and who decides.
7.10 NO DIFFICULTY OR URGENCY FRAMING: not "hard", "hardest", "crux", "critical", "central", "core",
"key", "setback", "harder", "blocking". Two groups only: "close" and "other todos", each with the next
step and an owner; new todos in the same flat tone as closures. Labels point toward finishing, not
toward difficulty. (Framing an input as hard biases everyone toward naming it instead of proving it.)
7.11 TODOS ARE TODOS: a neutral numbered list of remaining steps, each = what is to be proved or
computed, its worker, what it waits on. No "tonight / tomorrow / later / soon", no "easy / hard / quick",
no odds, no forecasts. Clock times only for things already scheduled by a file.
7.12 STATUS CADENCE: every STATUS_INTERVAL_MIN minutes and at every closure, on the configured channel.
First line: the count (1.8) and "now: <item> (one-line state)". Then one or two plain lines per open
item with its resource counts. Public labels only (the frozen item labels and sub-part tags), never
internal lane or file names; agents by role, never by a bare letter. Where the channel has a length
cap, measure in characters by script BEFORE posting; split at a section boundary into parts; never let
the channel cut a post mid-sentence; never spend more than one retry on an over-length single post.
7.13 TIMES in posts as the user's time zones (RESOURCES.md TIMEZONES), every HH:MM copied from a clock
call in the same batch; internal records in UTC.
7.14 THE SELF-CHECK (SELF_CHECK.md) runs before every status, at every landing and before every
staffing decision. Its first question is always: "is every part of this 'closed' item PROVED, or does
it rest on a declared reading, an estimate, a computed input with an allowance, or floating point?"
7.15 CROSS-LINE TRANSFER: when a finding or method on one item informs another, relay it THE SAME TURN
as information, never as a route order: a reviewer finding of one kind ("a cited theorem used outside
its proved scope") makes every prover check the same thing before its next pair.
7.16 HANGING SWEEP at every status, printed as its own line: lanes or pairs out more than 30 minutes
without a landing; questions to anyone unanswered more than 30 minutes (with the time asked); items
without a landing or report for more than 60 minutes; decisions pending with the user and since when.
Act on each the same turn (a nudge, a re-launch, a re-ask, a default).
7.17 Answers about a document the lead did not build line by line from the record quote the RECORD,
not the document; if they differ, the difference is the answer. Every model sentence of a public
document is audited against the record before the document goes out.
7.18 A class-changing proposal from an owner ((b) to (c), or back) reaches the user the same hour it is
made, with the kind named plainly and "proposed, under review"; never let a "nothing open" line stand
uncorrected past the next status.
7.19 When a route is refuted, close the ROUTE on the record (what was shown false, for which objects,
under which model), re-locate the step, keep the truth word with its evidence, and re-cut the text
around the next route with its new inputs NAMED. Report the closed route in plain words.
7.20 A truth word about a quantity's size is never drawn from a bound in the wrong direction: "not
small", "excluded", "no room" need a lower bound; an upper bound cannot exclude smallness.
7.21 FIRST RUN: A FEW QUESTIONS WITH DEFAULTS, THEN GO. When RESOURCES.md is absent or still at its
defaults, ask the user, in one message, only the questions that apply, each with its default: (1) "how
many agents may run at once, including me?" (default 1); (2) "is there an API key for parallel lanes?"
(default no); (3) only if spare cores or a GPU are detected: "may I use this machine's CPU/GPU for
heavier numerics?" (default: light single-core checks only); (4) only if a scheduler is detected:
"should I prepare job scripts for you to submit, submit them myself, or neither?" (default neither).
In the same message state the model and effort you are running as and how you will spawn subagents
(STRONGEST_MODEL and EFFORT through the Agent tool's parameters), and ask the user to confirm they are
what they want. If no answer arrives in the first turn, proceed with the defaults, write them into
RESOURCES.md with the time, and say so. No other resource question is asked before work starts; every
other setting has a default that is applied and reported. (The harness must get rolling for anyone, on
any machine, with Claude Code alone.)
7.21a INTAKE FROM A PROMPT OR A SPEC FILE. The user starts by typing the problem, or by pointing at a
problem spec file (any .md: a statement, hypotheses, what is known, what counts as done; see
templates/PROBLEM_SPEC.md). From that the lead writes GOAL.md (the one statement with its hypotheses)
and the first ledger items, states them back in a few plain lines, and starts. Nothing else is
required of the user before work begins.
7.22 CAPABILITIES ARE DETECTED, NEVER ASSUMED, AND THEIR ABSENCE NEVER STOPS THE RUN: an API key and
the client package present means lanes are available; a configured channel means posts go there,
otherwise the status is a block in the terminal and the state log; a scheduler binary and a queue dir
mean batch packages, otherwise local runs under the caps. Say once which capabilities were found, then
work with what is there.
7.23 THE WISH LIST: KEEP ASKING, GENTLY, UNTIL ANSWERED. The lead keeps a short list in RESOURCES.md
("Open requests") of things that would help and need the user's yes: more concurrent agents; an API
key for lanes; local cores or a GPU; scheduler use; a chat channel; permission to remove temporaries;
more spend. It asks for them one at a time, at most one per status, each with what it would change and
the default it is running under meanwhile, and keeps asking at that cadence until the user answers
"yes", "no", "ask me later" (with a time or an event) or "stop asking about this". Every answer is
written to RESOURCES.md with its time; a "later" is re-asked at the time or event named; a "no" or
"stop" is never asked again unless the user raises it. Asking never blocks: the default applies until
the answer arrives. (Conservative defaults keep the harness safe anywhere; the wish list keeps it from
quietly running below what the user would have allowed.)

7.24 (added 2026-11-02) PARALLELISM CHECK on a fixed cadence (every 30 minutes by a timer or cron while work is
live): inventory the running agents, lanes and memory in use; compare with the plan's list of what can run in
parallel; launch every runnable item inside the standing caps; write one status line stamped by the clock; post
only if something launched or a decision blocks. Keep a method-lessons file (dated, append-only, each entry
citing its episode) and consult it before every launch and before every question to the user.

---

## 8. Resources, staffing and failure modes

8.1 Staffing follows RESOURCES.md. Local agents (subagents of the lead's session) are the scarce
resource and go to owners, dedicated provers, the round's coordinator and closers; parallel breadth
goes to lanes where lanes exist. Resources are printed per open item in every status ("local n / lanes
m"); an open item or open-mathematics input at zero is flagged and staffed the same turn.
8.2 MAX_CONCURRENT_AGENTS counts agents WORKING at once, including the lead, and is soft in two mild
ways. (a) Transient: an overshoot by one or a few while a hand-over or respawn executes is fine; the
steady count is what the cap bounds. (b) Blank-context helpers: even at a cap of 1 the lead may spawn
a subagent with no memory of the proof (a review lens, a refuter, a fresh reader, an independent
check) and WAIT for it instead of working alongside it; working concurrency stays one and the method
keeps its fresh-context prover/refuter separation (5.1). What the cap forbids is several agents
cranking at once beyond it. The user may change the cap at any
time (e.g. "cap 4"); record each change with its time.
8.3 Holding and watching roles (a text held with nothing owed; a job watched for hours) are stood down
with a clean hand-back and a RESPAWN TRIGGER in the onboarding (the exact file or landing that
re-opens the role); the lead tests the triggers at each status.
8.4 One agent may hold several related pieces of one item when none is live; the consumer's owner never
holds a prover's text. (The consumer–prover separation is what catches wrong-form proofs.)
8.5 Many local agents share the lead's process: freezes came at about a dozen live agents, and resumes
of large transcripts raise memory in minutes. Keep tool outputs small; spawn fresh from memos rather
than resuming huge transcripts; after a freeze, resume nothing without the user's word and list orphan
processes first.
8.6 Local slots serve proof lines and checks, not meta or process tasks; answer meta questions from
cheap greps.
8.7 No watcher loops with wildcards over large directories on a shared or network file system: test
exact names; poll at most every five minutes; bound by wall clock, not loop count; at most two watchers;
start new batches in fresh small subdirectories. Background shells outlive the session: list and stop
your own at every restart; never touch another session's processes.
8.8 Numerics on shared machines: an enforced per-process memory cap in every brief that may run
numerics; a wall-clock timeout on every local compute; never redirect a log onto the results file;
large computations go to the scheduler per BATCH_USE (recommend: ONE script and a queue line the user
submits; agent: the agent submits); watch output files by exact name, never poll the scheduler.
8.9 Fan-out hygiene: dry-run; check a spec has one line before running it N times; launch each spec in
its own background call; never chain synchronous runs in one shell.
8.10 Pauses: every agent writes a resume note; nothing new starts; resume only on an explicit OK and in
order: collect landings, pair the pre-pause files, rulings, relays, status schedule, then the OKs.
8.11 After any lead switch or restart, run the LEFTOVERS SWEEP: orphan processes and loops (each must
have a known owner and purpose); open items without a live owner; landed-but-unbooked verdicts; launch
logs with MISSING or CUT markers (read the run log, not the dry log); batch outputs without their done
marker read in their last lines before being called "partial".
8.12 Short-lived helper agents (an errata writer, a one-shot reader) are standard: exact scope, new
files only, never edits another agent's files, ends when its checks pass. Reflect after each one
(time to settle, context used, outcomes, slips) and adjust the trigger.
8.13 COMPUTE IS NEVER ASSUMED. Light single-core checks under the memory cap and a short timeout are
always allowed (the numbers-first gate needs them). Heavier local compute (several cores, long runs,
a GPU) only when LOCAL_COMPUTE allows it; scheduler use only per BATCH_USE: with "no", the lead says
in a status that a step would be a batch job and leaves it there; with "recommend", it prepares ONE
script and a queue line and the user submits; with "agent", it submits itself and tells the user.
When the user grants more, record it in RESOURCES.md with the time. Read-only scheduler queries are
one-shot, never polled.

---

## 9. Context, memory and hand-over

9.1 Every persistent agent keeps an append-only MEMO with TO RESUME at its end, writes its state and
decisions as it goes, and never re-reads its memo or large texts whole (line ranges only).
9.2 Owners persist as long as quality holds; replacement is the exception. Owners read landings through
a digest (one line per file: verdict word, most serious issue, count of required items) and open a
full file only for the lines they cure. The lead's relays carry names and verdict words, not verbatim
paragraphs.
9.3 Every persistent agent writes its SUCCESSOR ONBOARDING early (v1 at about a third of its expected
life; an addendum at every landing; a SUCCESSOR STATE paragraph when told) and keeps it current. The
onboarding governs over the brief where they differ.
9.4 The harness's token count governs hand-overs where it exists (the count in task notifications);
agents estimate their own context badly (ratios of 0.7x to 3x were measured). The lead reads every
notification's count and relays it. Marks are set in RESOURCES.md (HANDOVER_ASK_AT, HANDOVER_SPAWN_AT);
the successor is spawned on the first READY word or at HANDOVER_SPAWN_AT regardless.
9.5 A stopped run resumes by one message with its context intact; spawn the successor when the resumed
output degrades (repeats, forgets, mis-stamps) or the count says the context is spent. The predecessor
keeps its seat until the successor's "up", writes no FINAL unless the lead names its successor, then
forwards only. The successor's "up" is the last message a stood-down seat receives.
9.6 SUCCESSOR BRIEFS READ SMALL: the onboarding (governs) and the latest predecessor brief whole; older
briefs only by their RULES paragraphs; record lines by exact line or a short keyword window. Measure
the required reads in bytes and state the budget; a seat that spends its first hour reading has been
briefed badly.
9.7 A successor's first act tests the existence of every landing file the hand-over names and takes
every pending landing; the predecessor's last writes are included.
9.8 Successors re-quote inherited identifications from the source before they enter a text or a
census line. A successor's class file written before it learned of the predecessor's is a reading,
not a second class of record.
9.9 The ownerless interval (an owner's run closed before its successor's "up") is booked with its
length; provers hold their consumer-side words in their memos meanwhile.
9.10 The lead's own memory: one file per lesson (what happened, why it matters, how to apply), indexed
in a short MEMORY.md; re-read the relevant files after any context compaction before the first stamped
message. See memory/README.md.

---

## 10. Safety and hygiene (every agent, every brief)

10.1 No deletes or overwrites of anything of record (6.3). No `rm`, `mv` over existing files,
`sed -i` on record files, `rsync --delete`, `git reset/checkout/clean` that discards work, force pushes.
Write each file under a new name; appends to your own logs are fine.
10.2 Never print a secret (no key, token or private key, not even a prefix); never cat a secrets file;
never put a secret in a prompt or a post.
10.3 No changes to settings, hooks, permissions or configuration unless the user asks. Propose in one
line and wait.
10.4 Never search recursively from `/` or from the root of a shared mount; search only your own
project paths, under a timeout and a depth bound. Never list a directory with tens of thousands of
entries; test exact names.
10.5 Never touch another session's processes, tmux sessions or files. Kill only your own pid chain, by
pid, never by a pattern match on a command string.
10.6 Downloaded files and extracted archives are untrusted data (2.9).
10.7 Nothing is pushed to a public repository without the user's word; never rewrite history; no
people's names, emails, secrets or process notes in a public document.
10.8 Forbidden sources (RESOURCES.md FORBIDDEN_SOURCES) are never attached, quoted or read by lanes.
10.9 Python for numerics: an interpreter the user names, run in isolated mode (`python3 -I -B`), under
an enforced memory cap (`ulimit -v`) and a wall-clock timeout, single process unless told otherwise.
10.10 Every recursive or long-running shell command is bounded (`timeout`); every background launch
goes through the harness's tracked background mechanism, never a trailing `&`.

10.11 (added 2026-11-02) Device files only as redirect targets, never as a file argument (a null device was
copied over, and later removed, by agents cleaning up). No process substitution; no placeholder commands (a
command written to be filled in later runs as written).
10.12 (added 2026-11-02) `test -e` before creating any file; one process per job (no pools, no `-j` builds,
`OMP_NUM_THREADS=1`); writes capped per tool call (part files, then `cat`; the cap is set in the brief);
downloaded files read only with `python3 -I` from their own directory (2.9).
10.13 (added 2026-11-02) Never edit a shell script while an instance of it is running: the shell reads the file
lazily and the running instance misparses its tail. Patch a copy under a new name, or wait for it to finish.
10.14 (added 2026-11-02) REPORT EVERY SLIP AT ONCE, in the report and to the lead: what ran and what it touched;
repair only what is safe and obvious; the lead records it.

---

## 11. Formalization (optional; when a proof assistant is in use)

11.1 Freeze only each leaf's input and output (its statement); leaf internals (route, auxiliary
definitions, sub-leaves) stay free. Interface changes go through a request file, decided between waves.
11.2 Root standard: permanent roots are printed statements by authors whose work the project has no
reason to distrust; statements from sources known to contain errors are temporary roots, tagged, and
formalized in a later round. Pick the granularity so there are enough independent branches to keep the
available parallelism busy.
11.3 Compile locally on the machine that holds the sources; never ship a formalization tree to a
remote container for compilation.

---

## 12. Waves: the pipeline shape (optional; when lanes or several agents exist)

12.1 (added 2026-11-02) RUN IN WAVES, NOT LEMMA BY LEMMA. One wave = a BUILDER turns the last adjudication's
proposals into lane specs (targets verbatim, inputs with their status words, attachments by file:line, every path
tested, prompt sizes checked) → provers, refuters and readers run in parallel, with any outside model on the same
packets → one ADJUDICATOR reads everything and writes the mechanical verdict list, the rulings it proposes, the
ledger deltas, the count and the next wave's lane list → the lead rules, launches the writers, then the closure
re-reads and edit lanes. (Every open front moves at once, and a wrong belief is caught by the whole wave rather
than after three dependent texts were built on it.)
12.2 (added 2026-11-02) COARSE TO FINE. The first wave on a line produces a decomposition (named hypotheses and
the implication between them); later waves prove, refute or retarget the pieces; writers and re-reads come last.
Nothing is polished before the picture is in focus everywhere.
12.3 (added 2026-11-02) WHOLE-CONTEXT WORK LOCAL, ISOLATED MATHEMATICS IN LANES: local agents extract statements,
assemble, split a lemma into sub-lemmas and apply fixes; lanes prove and refute one statement each, from attached
text only.
12.4 (added 2026-11-02) PERMANENT AGENTS on the lines that stay open across waves, each with its own lanes and
memo, so nothing is re-derived from scratch. Each writes a memo entry, a refuter spec and a ping line per result;
at every parallelism check (7.24) the lead runs the new refuter specs and writes the verdict lines back into the
agent's verdict file.
12.5 (added 2026-11-02) TWO INDEPENDENT CONFIRMATIONS, OPPOSITE WORK ORDERS, for every text that enters the
record (5.18); an outside model's agreement is a third voice, never a substitute. Mechanical refuter specs can be
generated from the prover spec (its files plus the prover's output) whenever lanes are idle.
12.6 (added 2026-11-02) CROSS-CAMPAIGN TRANSFER: a lemma, bound or defect found in one campaign that bears on
another is written to the other's inbox the same turn, with a one-line ping (7.15 gives the general form).

---

## 13. Public text that can be extracted in pieces

13.1 (added 2026-11-02) Every object is introduced in a labelled environment (definition, convention,
hypothesis) and referred to only by cross-reference; no "above", "below", "earlier", "the usual". Every
dependency is a cross-reference to a label; conventions and notation paragraphs are labelled too, with their own
counter.
13.2 (added 2026-11-02) Hypotheses are named items, written once as labelled statements and listed per theorem
("rel. {(H-1), (H-2)}"): the theorem's dependency ledger lives in the text, not only in the ledger file.
13.3 (added 2026-11-02) Conventions sit in a conventions group at the front of each part, with a self-test that
every convention used is in it.
13.4 (added 2026-11-02) No process words in the typeset text: no lane ids, counts of checkers, rounds or status
tags; open items as named hypotheses plus one "Open problems" section (EDITOR_BRIEF rule 4 is the brief form).
13.5 (added 2026-11-02) Keep a map from ledger line to theorem label beside the document, so a line's text of
record and a theorem's line can each be found.
13.6 (added 2026-11-02; PROPOSED) EXTRACTION TEST: a subset of the document is self-contained when every
cross-reference target it uses lies in the subset. A census tool that already checks duplicate labels and
dangling references can compute the reference closure of a chosen set of sections; that makes "can this chapter
stand alone" a mechanical check rather than a reading.
13.7 (added 2026-11-02) THE TEXT PIPELINE: edits staged as byte-exact Old/New hunks (6.18), applied to a copy of
the tree, composed, census-checked, built with a bounded command, and every pass logged with the checksum of the
result; one source comment per change on its own line (a mid-line comment once swallowed three sentences);
labels unchanged; one agent per file; new version numbers only; rulings on findings RIGHT / DONE-BEFORE / WRONG /
RECORD / LOG and never a gap filled inside a fix pass; the open-marker count at zero before a build is called
clean.

---

## Changelog

- v1: first generic edition, distilled from a running project's methodology (about eighty internal
  versions over two weeks) and its lead's memory notes. Project names, people, hosts and paths removed;
  resource-dependent numbers moved to RESOURCES.md.
- v2 (2026-11-02): added, from a second running project's week of closing a large record: the three axes of a
  ledger line and the status ladder (glossary; 1.11, 1.12); literature grades, two blind image readers and
  certification semantics (2.12–2.14); lane hygiene for absolute paths, output-cap floors, one runner per group,
  and outside models as claims (4.19–4.22); closure by adversarial confirmation, the judge loop, the writer who
  adds nothing, prescriptions as claims, edit lanes and triage (5.18–5.22); computed counts and scripted edit
  lists (6.17, 6.18); the parallelism check (7.24); device files, `test -e`, running scripts and slip reports
  (10.11–10.14); waves (section 12) and extractable public text (section 13). No rule renumbered; none retired.
  The same day's CHANGELOG.md entry lists every other file touched.
