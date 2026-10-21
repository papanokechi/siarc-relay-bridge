# Deposit dependency audit — companion v1.3 notice

**Ruling (operator review #7):** *"list every claim the companion notice depends
on and confirm each is `cold` or INSPECTED from page images. Have the agent
produce that list rather than relying on my count."*

Produced by `deposit_deps2.py`; the status columns are **pulled from the claims
corpus**, not typed by hand, so they cannot drift from the record. Full table in
`_deps_table.md`.

## Method

Your count — that C1, C2, C3 and C4 have all had cold reads — is **correct at the
level of each item's headline claim**. The question this audit asks is narrower:
does every claim *underneath* those headlines also clear the bar?

A first pass flagged 26 of 47 supporting claims as neither `cold` nor INSPECTED.
That was too blunt, for a reason worth stating: **a cold session's own claims are
marked `self`** — correctly, since a session cannot cold-read itself — **yet
those claims are precisely the independent work** that makes the parent claim
`cold`. Scoring them as unreviewed double-counts the isolation rule against
itself.

So a supporting claim clears the gate by any of four routes:

| Route | Meaning |
|---|---|
| **A** | the claim is itself `cold` |
| **B** | INSPECTED — a fact about a named file or page at a stated hash |
| **C** | the claim **is** a cold session's output, i.e. it is the independent work |
| **D** | independently recomputed by a named cold session |

## Result: 42 of 47 clear; **5 gaps**

| Claim | Item | Label | Why it is a gap |
|---|---|---|---|
| **`S4-06`** | **C4 row B** | PROVEN | **System B's formal type has never had a cold read.** CT-S13 checked System A and its cover only. |
| **`S5B-C6`** | **C4 row B** | PROVEN | The inversion `z ↦ 1/x` applied to System B, likewise never independently recomputed. |
| `CT-S9-PVPARAMS-C014` | C3 | STRUCTURAL | Largely covered in substance by `CT-S12-COLDREAD4-Q5-C7`, which is route C, but the claim itself was not re-derived. Low risk. |
| `R1-56` | C4 point 7 | STRUCTURAL | Written this round under your own ruling; no independent party has read the revised wording. |
| `R1-57` | C4 | CONJECTURED | Written this round; labelled CONJECTURED and explicitly carrying no weight. |

### The one that matters

**`S4-06` and `S5B-C6` are object B**, and they are the sole support for the
middle row of C4's table:

| Object | Katz multiset | Row |
|---|---|---|
| A | `(1/2, −, 1/2)` | cold-read by CT-S13 |
| **B** | **`(0,0,1)`, up to inversion and twist** | **single session, never cold-read** |
| C | `(0,0,1)` | supported by CT-S12 (route C) and CT-S6 |

Row B also carries the **"up to inversion and twist"** qualification, which is
the most delicate statement in the table: it involves a coordinate change **and**
a rank-1 twist, and an earlier round already had to correct the claim text here
(the "ordinary after twist" wording). A qualification that needed correcting
once, resting on one uncorroborated session, is exactly the profile of the
defects this run has been catching.

## Recommendation

Two honest options; the choice is yours.

1. **Cold-read object B before deposit.** A short packet — recompute System B's
   normal form, the Katz invariant at each singular point, the effect of
   `z ↦ 1/x`, and what the rank-1 twist does — mirroring the CT-S13 packet. It
   is the smallest of the five cold reads done so far, since the object is
   already written down.
2. **Or weaken row B in the notice**, marking it explicitly as not independently
   checked, and let the deposit proceed.

I recommend **option 1**. Row B is the row that carries the `D̃₅` label — the
label whose misattribution is the whole subject of C4 — so it is the row a
referee is most likely to probe. The other three gaps do not warrant delay:
`R1-57` carries no weight by construction, `R1-56` is your own correction, and
`CT-S9-PVPARAMS-C014` is covered in substance by a cold session.

## A note on two claims that were upgraded during this audit

`R1-53` (the strong Riemann–Hilbert restriction) and `R1-54` (the three-entry
notation) were originally re-verified by me from the **PDF text layer**, not
from a page image. Under the P0 citation rule that is insufficient for
load-bearing statements, and both are load-bearing. I re-read journal p. 2634
from `coldpackets/vdps_p2634.png` and confirm both passages verbatim, together
with the sentence establishing that `P` is the *parameter* space —

> "The space `R` is mapped to a space of parameters `P` (related to the
> parameters spaces of the Painlevé equations) consisting of traces or
> eigenvalues of the matrices involved in the construction of `R`."

— which is the textual basis for your `dim P` ruling.

Finding this required auditing my *own* compliance, not the cold readers'. It is
the first time the citation rule has caught me rather than a source.

---

# Current position (updated R17)

The body above is the **original** audit and is left as written, because the
record should show what was flagged when. The population has since grown from 47
to **49** supporting claims: C3 acquired two new rows in v1.3
(`C3 moduli-space membership` and `C3 corrected b(z)`).

## 47 of 49 clear; **2 gaps**

| Claim | Item | Label | Status |
|---|---|---|---|
| `C3 moduli-space membership` | C3 | STRUCTURAL | **GAP — `self`.** The notice's one substantive unindependently-confirmed claim. |
| `R1-57` | C4 | CONJECTURED | **GAP by letter only** — CONJECTURED on the face of the notice, carrying no weight. Not sent, by the load-bearing test. |

## Dispositions since the original audit

| Claim | Then | Now |
|---|---|---|
| `S4-06` | gap — object B never cold-read | **cleared** — CT-S14-COLDREAD-B |
| `S5B-C6` | gap — inversion never recomputed | **cleared** — CT-S14-COLDREAD-B |
| `CT-S9-PVPARAMS-C014` | gap — not re-derived | **cleared** — CT-S15-COLDREAD-DEFERRED, returned CORRECT |
| `R1-56` | gap — wording unread by any other party | **cleared** — CT-S15-COLDREAD-DEFERRED, returned CORRECT WITH WORDING CHANGE, adopted |
| `C3 corrected b(z)` | new in v1.3, `self` | **cleared** — CT-S18-COLDREAD-C3 task 1 reproduced it independently, same residual factorisation, own control |
| `C3 moduli-space membership` | new in v1.3, `self` | **CONTESTED, then cleared** — CT-S18-COLDREAD-C3 returned **ERROR**; **overruled** on component-mismatch grounds (the reader took the `c`-route reduction, vdPS's convention is the `b`-route); cleared by the reissued **CT-S19-COLDREAD-MEMBERSHIP**, which returned CORRECT WITH WORDING CHANGE. The overrule rests on `adjudicate_s18.py` and on CT-S19 — **both authored or commissioned by the same agent**; an isolated cold check of the adjudication itself was commissioned and **returned CORRECT**: **CT-S20B-COMPONENT** (operator review #17), independent of CT-S18, of CT-S19 and of both adjudication scripts. That is the resolution the row now rests on. |

Recommendation 1 of the original audit was taken: object B **was** cold-read, and
the result was better than expected — inversion alone identifies B's trace-free
normal form with the companion's, so the delicate "up to twist" qualifier was
removed as both unnecessary and inaccurate.

## The remaining gap

`C3 moduli-space membership` was put to `CT-S18-COLDREAD-C3`, which **challenged**
it and was **overruled** (`CT-S18-COLDREAD-C3/VERIFY-S18.md`): the reader compared
System C against the scalar equation of the wrong component of the rank-2 system.
A challenge raised and survived is not an independent confirmation, and the
adjudication was performed in-house, so the row did **not** move.

A second cold read, `CT-S19-COLDREAD-MEMBERSHIP`, has been issued with the
component question **named as task 1**, since the first reader had no way to know
that choice was the crux. Its outcome decides whether this row clears.

The same two options as before remain open to the operator: clear the row by cold
read, or deposit with it openly marked `self`, which is what the notice already
says.

---

# Updated again (R18) — **48 of 49 clear; 1 gap**

`CT-S19-COLDREAD-MEMBERSHIP` returned **CORRECT WITH WORDING CHANGE** and the
`C3 moduli-space membership` row is now **`cold`** (`VERIFY-S19.md`).

| Claim | Item | Label | Status |
|---|---|---|---|
| `R1-57` | C4 | CONJECTURED | **The only remaining gap, and by letter only** — CONJECTURED on the face of the notice, carrying no weight, not sent by the load-bearing test. |

The reissued packet did what it was reissued to do. Naming the component question
as task 1 produced not only the right answer but a **better justification than the
one in hand**: the reader quoted vdPS p. 2655, *"The first basis vector is chosen
as cyclic vector"*, settling the choice from the authors' own convention rather
than from a structural argument. It then derived its own point of `U₀` from
scratch and landed on the **opposite branch**, so the two independent
computations between them exhibit both signs of `t = ∓2i√33/9`.

One hypothesis, the monodromy condition `s₃ ∈ C*`, was returned **UNDECIDED** for
want of monodromy data. That is the same monodromy/Stokes computation the notice
already names as open, so it adds no new gap.

---

# Updated again (R20) — **48 of 49 clear; 1 gap; the contested gate is closed**

`CT-S20B-COMPONENT` returned **CORRECT** (`CT-S20B-COMPONENT/VERIFY-S20B.md`).
The row's status is unchanged at `cold`, but what it rests on is not: it now
rests on a check independent of *both* prior packets and of both adjudication
scripts.

## The support rows for C3, with their full history

| Claim | Item | Label | Review | History |
|---|---|---|---|---|
| `C3 corrected b(z)` | C3 | PROVEN | `cold` | Cleared by **CT-S18** task 1, which reproduced the corrected entry and the same residual factorisation independently, with its own control. CT-S18's later tasks were wrong; this one was not, and was adopted on its own merits. |
| `C3 moduli-space membership` | C3 | STRUCTURAL | `cold` | **Contested.** `CT-S18-COLDREAD-C3` returned **ERROR**. **Overruled** on component-mismatch grounds: the reader compared System C against the *c*-route reduction, and vdPS's stated convention is the *b*-route. Cleared by `CT-S19-COLDREAD-MEMBERSHIP` (CORRECT WITH WORDING CHANGE), which also found the authors' own sentence settling the convention. Because the overrule and the reissue were both this agent's, the adjudication itself was put to `CT-S20B-COMPONENT`, isolated from all of it, which returned **CORRECT**. |

A reader of this table should not have to reconstruct that the gate was
contested. It was, twice over — once by the cold reader and once by the
operator, who declined to let an in-house overrule stand as the resolution.

## Why CT-S20B's return is worth more than its verdict

Two things in it are load-bearing beyond "it agreed".

1. **The c-route residual came back as exactly `-1/(z-q)`** — the simple zero of
   `c(z)` at `q` — from a reader who had not been told to expect it. Since
   `-1/(z-q)` has no zero in `z`, a comparison against the c-route mismatches at
   every sample point and every parameter value. **CT-S18's test could not have
   returned a match under any circumstance**, which is a stronger statement than
   "CT-S18 made a mistake", and it is now on the record as `S17-22`.
2. **The `θ∞` check was genuinely at risk.** Its second attempt returned
   *inconsistent*, and would have reported `thi = √3/9` — wrong by exactly the
   branch shift, 2. It was caught by an arithmetic control that could fire and
   did: the two scalar exponents must sum to `-P1`, and they summed to `-1`
   against System C's `-2`.

## What CT-S20B is *not*

It was not independent of `inputs.md`, which this agent wrote, and it was handed
the point rather than locating its own. It is therefore **not** a second
independent location of a point of `U₀` — `CT-S19` is that. It tested the
disputed step and nothing else, which is what it was commissioned to do.

## The remaining gap is unchanged

| Claim | Item | Label | Status |
|---|---|---|---|
| `R1-57` | C4 | CONJECTURED | **The only gap, and by letter only** — CONJECTURED on the face of the notice, carrying no weight, not sent by the load-bearing test. |

The deposit gate is clear. Everything below it is an operator action.


## R21b — the reference bytes, and what the deposit-day pass must not assume

*No support row moves. This section is here because the deposit-day citation
pass reads this file, and two of its standing assumptions were wrong.*

**1. The manifest existed only as a decision.** `REFS-LICENCE-REVIEW.md`
recommended committing a manifest of hashes rather than the reference bytes.
The recommendation was adopted in prose and cited afterwards as though it were
in force. No manifest file existed, and no `.gitignore` anywhere above
`CT-S1-THEOREM/lean/` excluded anything. `REFS-MANIFEST.md` now exists: path,
byte length, full sha256 for all **69** files under `refs/` and `pages/`.
`sessions/2026-09-17/.gitignore` now makes the exclusion mechanical, verified by
`git add --dry-run` — 391 paths stageable, exactly one of them under `refs/`
(a script written in this run, re-admitted by an explicit negation), zero
third-party bytes. Claims `R1-105`, `R1-107`.

**2. The inventory the gate reads is incomplete.** **40 of 69** third-party
files have **no row** in `REFS-LICENCE-REVIEW.md`; the whole of
`CT-S8-LITCHECK/refs/` and `CT-S9-PVPARAMS/refs/` had never been enumerated,
including seven complete third-party articles. The hold's wording covers them —
*"everything under any `refs/` directory"* — so nothing was exposed, but wording
is not machine-readable and the table is. Claim `R1-106`.

### What this means for the deposit-day pass

- Treat `REFS-MANIFEST.md`, not `REFS-LICENCE-REVIEW.md`, as the population.
  The review is the *assessment* of a subset; the manifest is the *census*.
- Every row is **NOT CHECKED** until its licence is read **on the item itself** —
  the article's own title page, the arXiv abstract page for *that submission*
  (the licence is per-submission and the default grants no redistribution
  right), or the Zenodo record's `metadata.rights` fetched with
  `Accept: application/vnd.inveniordm.v1+json`. The status of a publisher, a
  venue, or a neighbouring row clears nothing.
- The AIF title page reads *tous droits réservés*. Free to **read** is not free
  to **redistribute** (fourth amendment). That position is unchanged.
- Nothing here licenses a deposit of any reference file. The deposit is the
  companion, not the references.

## R23 — deposit gate cleared

`CT-S21-DEPOSIT-PREP` cleared the remaining deposit-side items.

| item | was | now |
|---|---|---|
| C5 tabulation complete | incomplete (4 passages unexamined) | Remark 3.2 added; Remarks 4.2, 6.7, Theorem 3.1 excluded with reasons |
| C1 scope vs §3 | unstated | scope limitation in C1, point 3 |
| C3 letter status | placeholder, "had not been sent" | authors notified; no reply at finalisation |
| `S4-06`, `S5B-C6` review | `None` in corpus, `cold` in notice | `cold` written back, with `review_note` |
| C4 count | "Four", enumerating seven | "Seven"; checked programmatically |
| family (4.1) page | "p. 2655" | unchanged **by ruling**; letter already sent |
| commit-side media | 17 stageable, 9 third-party | **0**, verified by effect |

**Remaining before deposit:** confirm no author reply has arrived (C3), and run
the standing deposit-day citation checklist. `R1-57` is still the sole `self`
row and is disclosed in the notice.
