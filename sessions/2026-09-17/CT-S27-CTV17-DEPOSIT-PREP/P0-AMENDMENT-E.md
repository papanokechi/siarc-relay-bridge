# P0 amendment E — mutant provenance — **ADOPTED**

**Status: ADOPTED, 2026-09-19, by operator ruling.**

> **Amendment E: approve.** Mutant provenance — a mutant drawn from the check's
> own pattern list proves only that the list is consulted. It's distinct from A
> through D, it has two live instances (X2's string list, and P1 without P2),
> and you applied it before it was ruled on, which is the right order.
>
> That clears the backlog to zero.

The ruling names a **second** live instance beyond `X2`, which this file had
recorded only as prospective application: **`P1` without `P2`**. That is the
sharper case. `P1` alone is not merely under-controlled — it is *satisfied by
destroying what it protects*, since deleting the citations along with the paths
leaves zero residue and a perfect pass. The operator placed it in a class
already known to the corpus:

> P1 alone is satisfied by deleting the citations, which is exactly the shape of
> a check that passes by destroying what it was protecting — the same class as a
> search space with no target in it.

That is Amendment A's defect (a PSLQ basis whose relation has coefficient zero
on the target) reappearing as a *verification* defect rather than a *search*
defect. E and A are therefore siblings: A asks whether the search space contains
the target; E asks whether the test set can reach the property.

**Backlog after this ruling: zero.**

---

## The proposal, as ruled on

Originally flagged by the operator in the ruling that adopted A–D:

> On defect 2, the general form is worth keeping in view: **a mutant drawn from
> the check's own pattern list can only prove the list is consulted, never that
> it is adequate.** That's a different failure from the ones already in C and A
> — it's about where test cases come from, not about what the check reads. If a
> fifth amendment is ever warranted, that's the candidate.

This file states the text and the evidence for it. The backlog rule from the
A–D ruling — *don't let a fifth accumulate unruled* — is the reason it was
written down immediately rather than carried in conversation, and the reason it
was presented for a single ruling rather than held until a sixth appeared. It
was ruled on in the round it was proposed.

---

## Why this is not already covered by A, C or B

| amendment | the question it forces | what it constrains |
|---|---|---|
| A | is the search space degenerate before I search it? | **the hypothesis** |
| B | is this hash taken after the artefact is final? | **the artefact** |
| C | did the check actually read the file? | **the check's input path** |
| **E** | where did this test case come from? | **the check's test set** |

C is the closest, and it is genuinely different. C says a broken *reader* makes
a check unable to see its subject, and that mutant testing cannot detect this
because a broken reader misreads the mutant too. E says the *reader is fine, the
logic is fine, and the mutant passes* — and the check is still inadequate,
because the mutant was manufactured from the same enumeration the check matches
on. A check and its mutant drawn from one list are a closed loop: the loop is
consistent, and says nothing about the world outside it.

The shared generalisation is that **a control must be independent of the thing
it controls**. C breaks independence at the input path; E breaks it at the test
set. That is the fifth instance of the pattern, after the four recorded under C.

---

## The evidence

**`X2`, this session (`S27-07`).** The check "no draft-stage language is
published" matched four literal, case-sensitive strings:

```text
'DRAFT ONLY', 'Not deposited', 'no deposit is authorised', 'draft only'
```

The description ended:

> End of draft v1.7 notice. Draft only — no deposit, no metadata edit.

`Draft only` — capital D, lower-case o — matches none of the four. The check
**passed** on text that would have published draft-stage language into a
permanent record.

Its sole mutant inserted `DRAFT ONLY. Not deposited.` — a string taken
**verbatim from `X2`'s own list**. The mutant was rejected, the check reported
`1 mutant(s) rejected`, and the report read as though the property were tested.
What was actually demonstrated is that `X2` consults its list. Nothing about
whether the list covers the property it is named for.

Caught only by reading the description's tail by eye, for an unrelated reason.

**The repair, and why it is the right shape.** `X2` was rewritten as a
case-insensitive word-boundary pattern with a quotation allowance, and given
**three** mutants none of which appear in the pattern — the first being verbatim
the sentence that got through. All three are rejected.

**Applied prospectively this round (`S27-15`).** The two new checks written for
the provenance strip, `P1` and `P2`, take their mutants from outside their own
lists by construction: each `P1` mutant is a verbatim string that stood in the
pre-strip notice, drawn from the source text rather than composed from the
patterns `P1` matches on. The amendment was followed before it was ruled on,
which the operator identified as the right order.

`P2`'s existence is the second live instance the ruling names: without it, `P1`
is a check that can pass by destroying what it protects.

---

## Adopted text

Append to P0 under PRE-REGISTRATION, after the READER INTEGRITY clause:

```text
- MUTANT PROVENANCE. A control must be independent of the check it controls,
  in its test cases as well as its input path:
    * A mutant drawn from the check's own pattern list, string table, or
      enumeration proves only that the list is CONSULTED. It cannot show the
      list is ADEQUATE, because check and mutant then form a closed loop that
      says nothing about the property the check is named for.
    * Every check that matches against an enumeration MUST carry at least one
      mutant constructed WITHOUT reference to that enumeration: taken verbatim
      from real source text, from a neighbouring artefact, or from the
      phrasing a human would naturally write. State the provenance of each
      mutant in the check, so that a later reader can see it is independent.
    * Where a check has already failed in the field, the text that got through
      MUST be adopted verbatim as one of its mutants.
    * A report of 'N mutants rejected' is evidence about the property only to
      the extent that the mutants were drawn independently; otherwise it is
      evidence about the list.
```

---

## What this would have cost, and what it costs now

`X2`'s defect stood through eleven passing runs of a 13-check verifier. The
amendment's cost is one sentence of provenance per mutant and, where an
enumeration is involved, one extra mutant. That is small against the failure
mode, which is a check that reports `PASS` and `1 mutant(s) rejected` while the
defect it exists to catch sits in the artefact.

The honest limitation: E cannot be mechanically enforced. Nothing in a test
harness can tell where a string came from. It is a discipline on the author,
which is why the adopted text requires the provenance to be **stated in the
check** — the statement is what a reviewer can check, and its absence is what a
reviewer can flag.

---

## Status

**ADOPTED 2026-09-19.** Ruled in the round it was proposed, on two live
instances: `X2`'s string list, and `P1` without `P2`.

**P0 amendment backlog: zero.** A, B, C (as amended, and extended the same day
with the symmetry bullet), D and E are all ruled. Nothing is PROPOSED and
unruled.
