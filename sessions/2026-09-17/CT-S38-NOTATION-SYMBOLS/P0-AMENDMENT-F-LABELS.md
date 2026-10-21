# P0 amendment F — the label list is five, not four — **ADOPTED**

**Status: ADOPTED, 2026-09-20, by operator ruling.**

> **`INSPECTED` beyond P0's four labels.** P0 is stale, not the corpus.
> INSPECTED was adopted as a ruling and carries 74+ claims. Update P0's label
> list to five.

Raised by CT-S37 Group B's draft check, which reported prose carrying a label
that P0's `EPISTEMIC LABELS` block does not enumerate. The check was right to
report it and right not to repair it: a checker that silently accepts a label
its own specification omits cannot distinguish an adopted fifth label from a
typo.

---

## The amendment

P0's `EPISTEMIC LABELS` block currently reads:

```text
EPISTEMIC LABELS (every claim you report carries exactly one):
- PROVEN: complete proof, or machine-checked.
- VERIFIED: numerically checked at stated dps with a stated residual.
- STRUCTURAL: follows from a structural or symbolic argument that is not fully
  formalised.
- CONJECTURED: everything else.
Never upgrade a label in prose. A numerical agreement is VERIFIED, not PROVEN.
```

It is replaced by:

```text
EPISTEMIC LABELS (every claim you report carries exactly one):
- PROVEN: complete proof, or machine-checked.
- VERIFIED: numerically checked at stated dps with a stated residual.
- INSPECTED: established by reading a stored artefact -- a file, a published
  page, a printed table -- and reporting what it says. The reading is the
  evidence; it certifies the quotation, not the reasoning around it.
- STRUCTURAL: follows from a structural or symbolic argument that is not fully
  formalised.
- CONJECTURED: everything else.
Never upgrade a label in prose. A numerical agreement is VERIFIED, not PROVEN.
A reading is INSPECTED, not PROVEN.
```

The ordering is deliberate: the five run from strongest to weakest evidence, and
`INSPECTED` sits where it does because a reading of an artefact is stronger than
a symbolic argument about one and weaker than a residual at stated precision.

## Why the closing line is part of the amendment

`A reading is INSPECTED, not PROVEN` is not decoration. It is the rule the R1
audit was opened to enforce, already carried in `CT-R1-AUDIT/P0-CITATION-RULE.md`
rule 1(a):

> No `file_inspection` claim carries the label **PROVEN**. Reading a proof in a
> file is not proving it. This is the defect the R1 audit was opened to fix:
> twelve claims had been tagged PROVEN on the strength of a file that contained
> a proof, one of which had a load-bearing gap.

Rule 1(a) states what such a claim may **not** be labelled. Until `INSPECTED`
existed there was no label it **could** carry, so the twelve claims were
relabelled into `STRUCTURAL` and `VERIFIED` on judgement rather than into a
class that names what was actually done. Amendment F closes that gap: 1(a) and F
are the negative and positive halves of one rule, and F is the reason 1(a) is
now enforceable without a judgement call.

## Evidence

`scripts/label_census.py`, output `outputs/label_census.out.txt`. The census
walks every `claims.jsonl` under `sessions/2026-09-17/` and reports the `label`
field of every claim line.

### Scope — what "corpus" means here

**Revised 2026-09-20 by operator ruling, on the finding recorded as `S40-04`.**

The word **corpus** in this amendment means the **Channel Theory corpus**: the
sessions under this programme, `sessions/2026-09-17/`. That is the root
`label_census.py` walks and the root it prints. It is **not** all of
`sessions/`.

The distinction is load-bearing, because two checks in the same run used the
word for two different sets. `draft_check.py`'s corpus index walks the whole of
`sessions/` — **451** `claims.jsonl` files, **4 195** claim lines, 1 411 unique
claim ids — and across that wider tree the five labels do **not** partition:

| | |
|---|---:|
| claim lines with no `label` field at all | **3 458** |
| `PROCEED` | 14 |
| `REFINED` | 1 |

The 15 out-of-five values sit in `2026-05-13` and `2026-05-14`, in records of a
**different workstream with a different schema** — `"label": "PROCEED"` appears
beside `lock`, `band` and `confidence` fields, which the AEAL claim schema does
not have. They are not a sixth epistemic label; they are a different vocabulary
in a different system, and the four further verdict-style values found on
unparseable lines are the same.

So F's substance holds **where it was measured**, and the closure it asserts is
a closure of the Channel Theory label list. Any future check that treats
Amendment F as a statement about all of `sessions/` is reading it wrongly.
Verified by two differently-implemented readers (`pathlib.rglob` + `json.loads`,
and `os.walk` + a raw-bytes regex) agreeing on every figure above and resolving
to named `file:line` locations.

| label | claims |
|---|---:|
| PROVEN | 140 |
| VERIFIED | 170 |
| INSPECTED | **215** |
| STRUCTURAL | 118 |
| CONJECTURED | 6 |
| **total** | **649** |

Across 35 `claims.jsonl` files — every Channel Theory session's record except
this session's own, which is excluded by construction so that the census does
not change when it is cited. The ruling's figure was `74+`; the actual count is
**215**, and `INSPECTED` is not a marginal fifth category but **the most common
label in the Channel Theory corpus**, carrying 33.1% of all claims — more than
`PROVEN` and `CONJECTURED` combined.

Six checks, all passing:

- **C1** every claim line carries a `label` field;
- **C2** no line carries two;
- **C3** every label is one of the five;
- **C4** the five **partition** the Channel Theory corpus — 140+170+215+118+6 =
  649, so there is no sixth label under `sessions/2026-09-17/`, and the
  amendment closes that list rather than extending an open one;
- **C5** `INSPECTED` is present;
- **C6** this session's own `claims.jsonl` exists **and** is excluded — without
  the existence half, the exclusion would be satisfied vacuously.

**Control.** A synthetic claim line carrying `label: "ASSUMED"` is injected into
the census and must be reported as outside the five. It was: `CAUGHT`. Without
this arm, C3 and C4 would pass on a corpus scanned by a reader that could not
see labels at all — the census would report five categories and zero anomalies
whether or not it was reading anything. The control is what distinguishes *"no
sixth label exists"* from *"I could not detect a sixth label"*.

## Label

**VERIFIED** — a census of stored files at exact counts, reproducible from the
script, with a firing control. The *ruling* that the fifth label is legitimate
is the operator's; this file establishes only that the corpus carries it, at
what scale, and that nothing else is carried.

## What this amendment does not do

It does not relabel anything. The operator's third ruling in the same message is
explicit that the corpus wins over a prose rule:

> **"Exclusions are VERIFIED" versus the corpus.** The corpus won, correctly. My
> drafting rule was written from the v1.7 notice's tier table and doesn't hold
> for S6-C7. Don't relabel anything to fit a prose rule.

Amendment F is the same principle applied to P0 itself: when a specification and
the corpus disagree, establish which is stale before changing either, and change
the stale one. Here the census settles it — a list omitting 215 claims is the
stale artefact.
