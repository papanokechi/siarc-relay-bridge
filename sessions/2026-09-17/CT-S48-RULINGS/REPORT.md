# REPORT — CT-S48-RULINGS

**Date:** 2026-09-21 · **Status:** complete · **Nothing committed.**

A record session. It executes four operator rulings and checks that each record
action says something true about the files it names. No mathematics is done
here, nothing is re-derived, and no earlier session is edited.

---

## 1. What was done

| ruling | action taken |
|---|---|
| 1 — close the formula pass | recorded as `S48-05`, with the closure's scope stated exactly |
| 2 — annotate `S25-01`'s scope | new claim `S48-01` carrying `supersedes: S25-01`; the original stands unedited |
| 3 — sibling markers are a standing rule, narrowly | `P0-AMENDMENT-G-SIBLING-MARKER.md`, adopted; instance verified against live digests |
| 4 — confirm `PROVEN` on `S47-12`, and record the line about labels | `S48-03` (the fact) and `S48-04` (the rule) |

`scripts/check_rulings.py` — **18 checks, 0 FAILED; 6 controls, 6 FIRED**,
exit 0. Every figure resolves to the summary line that reports it, per `S44-17`.

## 2. The four actions

### 2.1 Closing the pass (`S48-05`)

Recorded with the scope written out, so that "closed" can never later be read as
"every display was re-derived":

- **56 of 56** displays routed;
- **38** symbolic identities at residual 0;
- **12** short route-S displays accepted on a resolving corpus claim, **without**
  independent re-derivation.

The two highest-risk displays — `eq:QC`'s `22/22/54/5` and §5's exact `q` and
`p` — were both re-derived, and in both cases the prediction was made **before**
the instrument existed. That is what makes the agreement mean anything.

### 2.2 Annotating `S25-01` (`S48-01`)

`S25-01`'s controls are about the solutions **recorded** in
`CT-S16-MEMBERSHIP-C/outputs/pq_solution.txt`. Its claim text names that file and
names `locate_final.py`, and names **no printed-side artefact at all** — not
`section5.tex`, not *printed*, not *typeset*. So it establishes nothing about the
forms typeset in the paper. What covers those is CT-S47, which parses the
numerals out of `section5.tex` itself.

The gap reads as covered until someone checks, which is the whole reason for
annotating it. Control `R1c` fires — the detector sees `section5.tex` when the
token is present — so *"names no printed-side artefact"* means absence, not
unreadability.

### 2.3 Amendment G (`S48-02`)

Adopted, narrowly. The bar is **demonstrated harm**, set by the operator at two
occurrences, and `jimbo_p1152.png` cleared it: CT-S15's misattributed
transcriptions, then CT-S46 route P, where trusting the filename would have
reported correct prose as unverifiable. Verified against **live-computed**
digests, not recorded ones.

### 2.4 The label line (`S48-03`, `S48-04`)

`S16-R18-02` carries `PROVEN` and its own claim text contains a formula wrong as
written. The label stays, and the reasoning is the substance:

> **A label is a verdict on a result; it has never been a guarantee about the
> bytes of its statement.**

So the instrument is supersession, not relabelling. Downgrading would assert the
mathematics was in doubt; it was not. And no label, at any strength, would have
caught this — which is the argument for the formula pass having existed.

---

## 3. Findings

### 3.1 A literal needle cannot see a line-wrapped sentence (`S48-06`)

Check `R3-f` — *"the marker states the rule"* — **failed on its first run against
a marker that states the rule perfectly well.** The needle was a literal
single-space string; the sentence *"Resolve these images by hash, never by
filename."* wraps between `hash,` and `never`.

This is `S43-12` recurring, and it is the same shape as every other
absence-the-reader-cannot-see defect in this run: the failure is **verbally
identical** to the failure it exists to detect. Diagnosed against the raw file
before anything was edited, so a correct marker was not "repaired".

Fixed in the **reader**: each needle compiles to a regex joining its
whitespace-separated tokens with `\s+`. Given a control requiring that the same
wrap-tolerant needle does **not** match the rule stated **backwards** — without
which a needle loose enough to cross a line break might be loose enough to match
anything.

### 3.2 The advance prediction was a partial hit, and is recorded as one (`S48-07`)

PREREG §5 named **R3** as the most likely failure, for a stated mechanism: the
marker records digests as 16-hex prefixes, and a reader comparing full 64-hex
digests would report absence. R3 is indeed where the run failed — but at `R3-f`
on line wrapping, not at `R3-c/d/e` on digest width. The prefix comparison had
been built as the PREREG said and passed.

Right block, wrong mechanism. Calling that a hit would overstate what foresight
bought.

---

## 4. Claims

| id | label | subject |
|---|---|---|
| S48-01 | INSPECTED | **supersedes S25-01** — recorded vs printed scope |
| S48-02 | INSPECTED | amendment G adopted; instance verified on live digests |
| S48-03 | INSPECTED | a `PROVEN` claim contains a formula wrong as written |
| S48-04 | STRUCTURAL | what a label grades, and why supersession is the instrument |
| S48-05 | STRUCTURAL | the formula pass is closed, with its scope stated |
| S48-06 | VERIFIED | the wrap-blind needle, found and repaired |
| S48-07 | STRUCTURAL | the PREREG prediction was a partial hit |

`claims.jsonl`, sha256 `f329d530fe9d2ae9…`.

---

## 5. What was NOT established

- **Nothing mathematical.** This session re-derives nothing and checks no
  formula. Its claims are about what other records say.
- **`S48-04` is a ruling, not a result.** The general statement about labels is
  the operator's; what is checked here is only the instance that occasioned it.
- **Amendment G is not retroactive.** No sweep for other misleading filenames
  was run, by design — the bar is demonstrated harm, and a sweep would invert
  that into tidiness.
- **The twelve un-re-derived displays remain un-re-derived.** Closure is a
  ruling about acceptable residual risk, not evidence that they are right.

---

## 6. Uncommitted files

```
sessions/2026-09-17/CT-S48-RULINGS/
  PREREG.md
  REPORT.md
  claims.jsonl
  P0-AMENDMENT-G-SIBLING-MARKER.md
  scripts/check_rulings.py
  scripts/emit_claims_s48.py
  outputs/check_rulings.out.txt
```

All new. No existing file is modified by this session.
