# P0 amendment H — unswept scope, a check scoped by the report — **ADOPTED**

**Status: ADOPTED, 2026-09-21, by operator ruling.**

The operator named the class, ruled it distinct from anything already in P0,
and added the commissioning clause:

> **Amendment H: adopt.** The distinctness argument holds — A through G each
> guard whether a check *can* fire; S44-05 fired correctly and told the truth
> about §3. The defect was that the item list came from whoever reported the
> problem, so "where else does R occur?" was never in scope and could never
> fail. That's upstream of every existing amendment. The `section1.tex:225`
> evidence is the second instance in the same shape: six items because six
> were noticed.
>
> One clause worth having in it: when a repair pass is commissioned from a
> reported list, its first act is to sweep for the same defect elsewhere, and
> the sweep's result is part of the output whether or not it finds anything.

---

## The amendment

Added to P0 after the `PRE-REGISTRATION` block:

```text
SCOPE OF A SWEEP
- A pass that repairs occurrences of a thing must state where it LOOKED, not
  only what it FIXED, and must derive its item list from the artefact rather
  than from the report that raised the problem.
- Before claiming a symbol, a phrase, or a convention has been unified,
  enumerate every occurrence in the corpus and account for each. A pass whose
  items are the ones someone noticed has swept the reporter's attention, not
  the corpus.
- A claim of unification must name its scope explicitly. "X was unified in
  section 3" and "X is unified" are different claims; only the second needs a
  census, and only a census can support it.
- When a repair pass is COMMISSIONED FROM A REPORTED LIST, its first act is to
  sweep for the same defect elsewhere. The sweep's result is part of the pass's
  output whether or not it finds anything: a sweep that finds nothing must say
  so, and say where it looked. A pass that reports only its repairs has not
  reported its scope.
```

## The clause added on adoption

The rule as proposed said that a sweep must state where it looked. The
operator's clause fixes *when* it looks and makes its result non-optional.
Both halves matter and they fail differently:

- **Ordering.** The sweep runs *first*, before the reported items are repaired.
  A sweep run afterwards is written by someone who has just spent a session
  inside the reported list, and it inherits that list's shape — which is the
  defect the amendment exists to prevent, reintroduced at the point meant to
  catch it.
- **Non-optional reporting.** An empty sweep and an absent sweep are
  indistinguishable in a report that only records repairs. Requiring the null
  result to be printed is the same construction as this run's non-vacuity rule:
  a count of zero is a result, but only if something asserts that zero things
  were tested is different from zero things found.

`S44-05` would have failed the clause: the `R` pass repaired the reported §3
and its output named no scope at all, so nothing in the record distinguished
"§6 and §9 were checked and are fine" from "§6 and §9 were never looked at".
They were never looked at.

## The instance

`S44-05` (CT-S44-NOTATION-2) recorded that the colliding symbol `R` had been
unified into section 1's general form and section 3 brought into line with it.
**That claim is literally accurate.** Section 3 was repaired; section 1 does
carry the general form.

What the claim did not say is where the pass *looked*. Its item list came from
the end-to-end read's findings — the places a reader had happened to notice a
collision — and not from an enumeration of where `R` occurs. Sections 6 and 9
also write `R`, in a third and fourth typography, and no item covered them; the
pass reported success on a partial application, and every instrument agreed,
because each was checking the items the pass declared.

The same shape produced section 1's **six-entry reuse list**: six *noticed*
collisions, recorded as though they were six *reused letters*. The sweep that
this session finally ran (`scripts/symbol_index.py`) finds **31** letters in
more than one role, **26** of them unnamed — including `b`, the paper's central
polynomial.

## Why it is not already covered

P0's existing amendments guard the **firing** of a check:

- **C** and its revision — a check must be able to fail, and a reader that
  invents a defect fails like one that misses it.
- **E** — a mutant must be drawn from outside the check's own constant list.
- **F** — labels, and the corpus they partition.
- **G** — sibling markers for a name that has misled.

Every one of those asks *can this check fire?* Here the check fires perfectly.
`S44-05`'s verification was sound, its controls fired, and its statement was
true. The defect is upstream of the check entirely: the **item list** was
inherited from the report, so the question "where else does `R` occur?" was
never asked, and therefore never failed.

That is why it needs its own rule. A guard on firing cannot catch a check
aimed at the wrong set.

## Relation to the census rule

Amendment H requires an enumeration; it does not require the enumeration to be
a **gate**. `symbol_index.py` is deliberately a census: two syntactic roles need
not be two meanings, section 1 declares `P`/`Q` and `s`/`s_±` in prose no
item-head reader can see, and failing on the 26-letter residue would be a
threshold tuned to an answer. The rule is that the sweep must *look* everywhere
and *report* what it found — not that everything it finds is a defect.

## Label

**STRUCTURAL** — the failure class is established by reading `S44-05` against
the four typographies of `R` in the final text and against the census, but the
generalisation to a standing rule was a proposal, and its adoption was the
operator's.

Recorded as claim `S50-06`, written while the amendment was PROPOSED. Claim
`S50-12` supersedes it: it records the adoption and the commissioning clause,
with `S50-06` standing unedited.
