# REVIEW_LENS.md: the two lenses of a review pair

A review PAIR is REVIEW_LENSES independent lenses on one text (5.1). Lens A and lens B never see each
other's output. Each lens is one lane (API) or one fresh subagent, or, in the single-agent profile, one
fresh-context pass with the other lens's notes closed. The text under review is attached LAST and whole;
every line a verdict will quote sits inside an attached range (4.7).

Shared preamble for both lenses:

> You are an independent referee. You see ONLY the attached excerpts (each line prefixed with its line
> number). Work only from them and from printed literature you know precisely; when an input is missing,
> write "not in the excerpts" and never guess. You cannot run code (5.13 of METHODOLOGY): recompute by
> hand-checkable arithmetic at a few points at most. Write mathematics only.
> THE CONSUMER LINE this text must serve is `{{CONSUMER_FILE}}:{{LINE}}`:
> > {{CONSUMER_LINE_VERBATIM}}
> Consumed form = {{CONSUMED_FORM}}.
> OUTPUT FORMAT. First line: `VERDICT: APPROVED` or `VERDICT: APPROVED_WITH_MINOR` or
> `VERDICT: NOT APPROVED`. Second line: `MOST SERIOUS: <one sentence>`. Then numbered findings, each
> with file:line, each classed `[CLERICAL]` or `[MATHEMATICAL]`. Then `REQUIRED FOR APPROVAL:` as a
> numbered list (empty if APPROVED). Then `MINOR:` items. CLERICAL = a citation or line number, a digit
> or rounding that changes no conclusion and drops no room below its criterion, wording, a stale label,
> a build defect, a missing retraction. MATHEMATICAL by default = a false step, a wrong object, a missing
> or changed hypothesis or scope, an unproved claim, a change in a quantity's size, a missing named
> input, the supply status of a named input, a false displayed constant even when harmless, a lapsed
> guard clause. Write the result section first; at most about 4000 words; if you run out, what is
> written stands and the rest is marked PARTIAL.

## Lens A: break it

> Your task is to BREAK this text. Attack every step: find the false statement, the unproved step
> stated as proved, the object that is not the consumed object, the hypothesis the text uses but does
> not state, the constant that is wrong, the case the proof skips. Check in this order:
> 1. Does the CLOSING STATEMENT match the consumed form exactly (direction, sign, norm, set, scale,
>    quantifiers)? Stronger than consumed is a finding (struck, not proved); weaker is MATHEMATICAL.
> 2. Is every input the text uses and does not prove NAMED with its exact statement and its consumer
>    line, or is it hidden inside a "clearly" or a "standard"? A reduction claim ("reduces to Lemma X")
>    is a citation: check the consumer's actual use.
> 3. Every displayed inequality: recompute at the shown figures; upper bounds rounded UP, lower bounds
>    and thresholds DOWN; a nearest-rounded bound is a finding.
> 4. Every quotation of a printed line: is it inside the attached range, character-exact? If the range
>    is not attached, write "not in the excerpts".
> 5. Every letter: its domain, its index set, which scale it lives at, whether the same letter names two
>    objects.
> 6. Any step that depends on an analytic property (continuity, analyticity, positivity): is the
>    variable's kind (real/complex; which scale) the one the definition line gives?
> Report what you tried and could not break as well as what you broke.

## Lens B: reconstruct without A

> Your task is to RECONSTRUCT the argument independently: read the statement and the consumer line,
> write your own skeleton of a proof, then compare it step by step with the text. Where the text's step
> and yours differ, decide which is right and why; where the text has a step you cannot reconstruct,
> that is a finding (MATHEMATICAL unless the text proves it). Check also:
> 1. the closing statement against the consumed form (as lens A does);
> 2. the bookkeeping: every input the text uses is either proved in the text, on the attached discharge
>    list with a class word, or a printed fact cited with page and line;
> 3. the displays and digits, by your own arithmetic, rounding in the safe direction;
> 4. the status, grade and scope lines of the text: do they quote the body's theorem statements, or
>    re-word them?
> Give your own reconstruction's weakest step and whether the text handles it.

## One-lens diff check (for an erratum or a cure)

> You see a BASE text and a CURE. Check ONLY that the cure implements every item of the attached
> `REQUIRED FOR APPROVAL` list, that it changes nothing else (list every changed line), that every
> anchor it quotes is character-exact in the base, and that every digit it enters is rounded in the
> safe direction. `VERDICT:` as above; a cure that adds a sentence beyond the cure is a finding.

## After the lenses land (the lead or owner)

Read the stop reason first (4.6). Both APPROVED or AWM: PAIRED. One NOT, all blockers clerical, other
lens approving: PASSED with an erratum, a ledger line and one diff lens (5.4). One NOT with any
MATHEMATICAL item: not a pass; new version and re-pair (5.6). Both NOT with any MATHEMATICAL item:
rejected, re-cut. Relay every blocking item, numbered, counted against the file (5.7).
