# CT-S24-PAPER-OUTLINE — REPORT

**Deliverable:** `OUTLINE.md`, **revision 6** (sha256 `6c992dd5…`). Outline
only; no prose was drafted and no computation bearing on any hypothesis was run.

**No PREREG.** The task is an outline. The only script is a checker over file
contents. This is stated rather than back-filled as a vacuous pre-registration
(`S24-07`), following `CT-S23-OUTSIDER-READ/REPORT.md` line 10.

---

## 0-D. Revision 6 — the last open item is closed

Claim `S24-22`. The mathematics was done in a **separate session**,
`CT-S26-UPPER-BOUND`; this section records only what came back into the outline.

### 0-D.1 What was open

Revision 5 left exactly one item: §1 ¶2 asserts a **two-sided** bound on `r_∞`,
and only the lower half (`S1-02`, `r_∞ ≥ 1`) was proved anywhere. The upper
bound was recorded in §2 as an **unfolded drafting addition carrying no claim
id** (`S24-21(a)`), with a pre-declared alternative: prove it, or weaken §1 ¶2.

It was, as §5 put it, *the one place in the outline where the text was ahead of
the corpus* — and the reason it was ahead is worth restating: the bound came
out of a derivation in conversation and was never written back to any source of
record. That is the same provenance defect as the Odlyzko citation living
outside the worktree (`S24-12`).

### 0-D.2 What was done

`CT-S26-UPPER-BOUND` proves it. **Proposition U** (`S26-01`, PROVEN,
`CT-S26-UPPER-BOUND/PROOF.md`): under (A1) together with `b(n) > 0` for every
`n ≥ 1`,

```
r_n  ≤  exp( Σ_{k=1}^{n-1} 1/(b(k)b(k+1)) )   for every n ≥ 1,
```

hence `1 ≤ r_∞ ≤ L := exp Σ_{k≥1} 1/(b(k)b(k+1)) < ∞`. Four steps, all
elementary, all from `theorem.tex`'s own eq. `rnrec` and `prop:positive`. The
**finite-`n`** form is the one proved and the one tested, because it is exact at
every `n` and needs no tail estimate.

**The pre-declared fallback — weakening §1 ¶2 — was not taken.**

### 0-D.3 What came back into the outline

The §2 box is rewritten from "not yet proved anywhere" to the proved statement,
carrying four drafting constraints:

1. **The positivity hypothesis is load-bearing** and must be stated, not
   inherited from context: three of six sign-changing `b` violate the
   inequality outright, one because `r_n` becomes non-positive (`S26-04`).
2. **The upper half must not cite `S1-02`**, which supplies the monotonicity
   step and the lower bound only. It carries `S26-01`.
3. **No Pincherle or Perron–Kreuser input is used**, so §2.0's undertaking that
   nothing rests on Birkhoff–Trjitzinsky extends to it unchanged — the same
   concern that produced the revision-5 correction.
4. **The insertion into `theorem.tex` is not done.** That file belongs to
   `CT-S1-THEOREM` and this corpus does not edit earlier sessions, so the LaTeX
   source of record still carries the one-sided statement. ~15 lines at
   drafting, after `prop:positive`, hypothesised identically.

§5's summary line gains a revision-6 paragraph; §2's claim line and artefact
list gain the `S26-*` ids and `CT-S26-UPPER-BOUND/PROOF.md`.

### 0-D.4 One finding worth carrying, from the other session

`CT-S26`'s own known-answer control **fired** (`S26-05`). Its PREREG registered
`y_n = (-1)^n I_n(2)` as an exact solution of `y_n = n y_{n-1} + y_{n-2}`; the
Bessel identity actually gives that for `y_n = (-1)^n I_{n+1}(2)`, an index
shift away. The PREREG was left unedited and the correction written as a
separate addendum.

This belongs in §2.0's drafting-discipline note, because it is the same shape as
the two citations recorded there: *derived once, remembered compressed,
reproduced from the compressed memory rather than from the source.* And it
recurred **inside the session written to remove exactly that status from the
upper bound**. A known-answer test is only as good as its known answer — a
wrong control that had happened to *agree* would have certified a broken engine.

### 0-D.5 Revision-6 state

`OUTLINE.md` sha256 `6c992dd5…`. Checker **6/6 controls, 89 claim ids cited,
0 unknown, 0 missing paths, VERDICT OK**, over 14 sessions
(`outputs/verify_outline_rev6.out.txt`, sha256 `c4b99450…`). Revision-1, -3, -4
and -5 artefacts asserted unchanged and still resolving, before and after.
`claims.jsonl`: 22 claims, `S24-01`…`S24-22`.

---

## 0-C. Revision 5 — two stale spots, one substantive

Claims `S24-20`, `S24-21`.

### 0-C.1 The method paragraph misdescribed its own proof (`S24-20`)

§1 ¶2 read *"Growth is obtained from a Pincherle/minimal-solution argument."*
`theorem.tex` does not work that way. Read directly:

| source | what it does | label |
|---|---|---|
| `prop:exists` (L109–111) | convergence of `r_n`, **unconditional** under (A1), by absolute summability of the increments and telescoping | `S1-01` PROVEN |
| `prop:positive` (L123–136) | `r_n` strictly increasing, `r_n ≥ 1`, so `r_∞ ≥ 1 > 0` and (H) is automatic | `S1-02` PROVEN |
| `rem:pincherle` (L138–156) | the minimal/dominant *interpretation* of (H); ends verbatim **"nothing below depends on this remark"**; the gap table at L416 repeats "interpretive only" | `S1-05` STRUCTURAL |

So the paragraph credited the result to an argument the paper **deliberately
does not rest on**.

**This matters twice over, and the second reason is the sharper one.** The
Odlyzko page objects to Birkhoff–Trjitzinsky as possibly non-rigorous
(`S24-13`), and §2.0 is written to pre-empt that by stating that nothing rests
on it. A method paragraph led by Pincherle invites exactly the question §2.0
exists to close.

Three edits: the sentence is replaced by the elementary-argument statement
ending **"Pincherle's theorem supplies the minimal-solution interpretation but
is not used"**; a guard is added to §2.0 item 1 against the attribution
paragraph migrating into the method statement, since the paper's own (H) comes
from `prop:positive`; and §2's claim line, which listed `S1-05` flat beside four
PROVEN propositions, now marks it STRUCTURAL and interpretive.

### 0-C.2 The two-sided bound is not an existing result (`S24-21a`)

The replacement sentence says positivity supplies `r_∞ ≠ 0` "together with a
two-sided bound". **`prop:positive` proves the lower bound only**, and a search
of the `.tex` sources for an upper bound of that shape returns nothing.

It is therefore recorded in §2 as an **unfolded drafting addition carrying no
claim id**, with its one-line proof sketched: `r_n = r_{n−1} + r_{n−2}/(b(n−1)b(n))`
and `r_{n−2} ≤ r_{n−1}` give `r_n ≤ r_{n−1}·exp(1/(b(n−1)b(n)))`, the sum
converging since `deg b ≥ 1`. **Either prove it at drafting and emit a claim, or
weaken §1 ¶2 to the one-sided statement. It must not be written citing `S1-02`.**

### 0-C.3 A stale cross-reference (`S24-21b`)

§5 N2 directed the uniqueness question to "§11", which ceased to exist at
revision 2 when §9 was cut and the sections renumbered (old §10 → §9, old
§11 → §10). Corrected to **§10**, with the renumbering noted inline so the
correction explains itself. A sweep of every remaining `§9`/`§10`/`§11`
reference found **no other stale instance** — the one surviving "§9" not about
the cut is Birkhoff–Trjitzinsky's own Fundamental Theorem §9 p. 69.

### 0-C.4 Revision-5 state

- `OUTLINE.md` sha256 `769ff94d…`, 47,135 chars.
- Checker **6/6 controls**, **84** ids, **0** unknown, **0** missing,
  **VERDICT OK** → new path `outputs/verify_outline_rev5.out.txt` (`20a4f5fa…`).
- `emit_claims_rev5.py` asserted that **all three** prior artefacts
  (`fe5657ba…`, `490c7076…`, `08644185…`) resolve before the write and are
  byte-unchanged after it.
- `claims.jsonl`: **21** claims, `S24-01`…`S24-21`.

---

## 0-B. Revision 4 — N1 closed, and three rulings

`CT-S25-N1-EXHAUSTIVE` closed N1, and the operator ruled on three consequences.
All three are applied. Claims `S24-16`…`S24-19`.

### 0-B.1 N1 is closed (`S24-16`)

§5 N1 is restated from **NEW MATHEMATICS; ATTEMPT ONCE, TIME-BOXED** to
**CLOSED**. The saturated matching ideal is zero-dimensional of **degree 2**
over `ℚ(i√11)`; the lex basis is triangular with eliminant
`27θ_∞² + 108θ_∞ + 107`, and each of its two roots back-substitutes to exactly
one point, matching `CT-S16` exactly (`S25-02`, `S25-06`). The eliminant was
registered as a prediction **before** the computation ran.

The pre-declared fallback — state that the solver returned two solutions with
exhaustiveness unproven — was **not taken**, and N1 records that it was not.

**The mis-pricing finding is retained as history, not deleted.** `CT-S23` §3
filed this repair under kind (a), "a proof that exists in the corpus and was not
transcribed", and that classification was wrong: the proof did not exist. That
was true when written, so it stays, marked as history rather than as a live
cost. §5's heading and its summary paragraph get the same treatment: the line
"one piece of mathematics left to attempt" is superseded by "**the paper has no
new mathematics left to do; it is a drafting job**", with the old wording and
its reason kept beneath it.

### 0-B.2 The solver sentence, and the field (`S24-17`)

§1 ¶2 no longer reports what `sp.solve` returned. It states that the located
points are the **complete solution set**, proved by elimination over
**`ℚ(i√11)`**.

**The field is named, with a warning attached, because the wrong field is the
attractive one.** The radicals visible in the solutions are `√33`, `√11`, `√3`,
which pulls toward `ℚ(√3, √11)`; the commissioning ruling named that field and
this outline carried it until revision 4. It is wrong. The matching equations'
coefficients live in `ℚ(i√11)` via `s₊ = −1/6 + i√11/6` and `δ = −i√11/3`, and
**`√3` must not be adjoined** — it is *generated* by the eliminant, which is the
entire content of the conjugacy statement. Adjoining it would split the two
conjugate points, presenting a degree-2 ideal as two degree-1 components for the
wrong reason.

### 0-B.3 `S25-03` enters the paper (`S24-18`)

As a remark in §5, carrying two results that came free with N1.

**(a) Overdetermined by two.** `b₁ = 0` reduces to `0` modulo the Gröbner basis
of the five coefficient equations, so it lies in the radical: the quartic
matching **already forces** the no-apparent-singularity condition. Six
generators in four unknowns cutting out two points. Cleaner than "five equations
plus one condition in four unknowns", and free. The membership test carries its
own control — `θ_∞`, which vanishes nowhere on the variety, is correctly
reported **not** in the radical.

**(b) The Galois conjugacy is now exhibited exactly** by the eliminant, which is
the structural content `S22-20` lacked when it was established numerically.
Cross-referenced from §8 with the scope caveat that the exact statement is about
the **parameters**, not the Stokes data; and from §10, where it is stated
explicitly that the conjugacy **does not** close the z-dependent gauge question.

### 0-B.4 A drafting-discipline note in §2.0 (`S24-19`)

Three citations in this corpus have now needed narrowing once the page itself
was read: **Ibrahim–Salvy** ("do not know how to compute", not "is not
computable"), the **Wong–Li** title, and **Odlyzko p. 77**, where the
attribution splits (`S24-13`). In each case a compressed paraphrase had survived
into a session record. §2.0 now requires every citation to be checked against
the held page image or PDF **before drafting**, never against a prior note —
the exposition-side counterpart of the rule that an exit code is not evidence of
what a script wrote.

### 0-B.5 Revision-4 state

- `OUTLINE.md` sha256 `19695e62…`, 43,653 chars.
- Checker: **6/6 controls**, **84** claim ids cited, **0** unknown, **0** missing
  paths, **VERDICT OK**. Output written to the **new** path
  `outputs/verify_outline_rev4.out.txt` (`08644185…`).
- `emit_claims_rev4.py` asserted, *before* writing, that the revision-1
  (`fe5657ba…`) and revision-3 (`490c7076…`) artefacts still resolve for the
  claims citing them, and *after* writing, that both are byte-unchanged.
- `claims.jsonl`: **19** claims, `S24-01`…`S24-19`.
- `CT-S25-N1-EXHAUSTIVE` now appears among the sessions the outline draws on
  (13 in total).

---

## 0-A. Revision 3 — the latest rulings

Three items, plus one correction to a revision-2 finding of mine.

### 0-A.1 Odlyzko p. 77 — the correction, and the clearing

**The operator was right and my revision-2 conclusion was wrong.** I reported
zero occurrences of Odlyzko repo-wide and declined to write the citation. The
search was correct; the inference was not. The citation originated in
`CT-S22-DEPENDENCE-LIT`, whose record was deliberately stored **outside the
worktree** at
`~\.copilot\session-state\712e8e62-…\files\CT-S22-DEPENDENCE-LIT-record.md`,
and which deleted its downloaded PDFs at close. **Absence from the worktree was
the expected observation**, not evidence of an unsourced citation. The general
form: *a repo-wide search establishes absence from the repo, which is a claim
about the repo and not about the citation.*

Handling, in the order the ruling set:
1. Read the out-of-worktree record. It carries the citation with its substance.
2. **Did not cite from that record.** Re-obtained *Asymptotic Enumeration
   Methods* from the author's own site — 192 pp., 1,116,716 bytes, sha256
   `d0b58928…`, fixed in the checker **before** the document was read.
3. Verified **from a page image**. The page-offset rule (`S16-22`) applies:
   printed folio **77 is PDF index 76**, offset `−1`, resolved by locating the
   folio in the header/footer band rather than by trusting the index.
4. Written into `OUTLINE.md` §2.0 item 4 **alongside Nemes**, not in place of
   it — two independent sources for one statement.

`scripts/verify_odlyzko_p77.py` passes **5/5**, of which **three are
negative**: a fabricated near-miss fragment occurs nowhere in the document
(guarding the whitespace/ligature normaliser against matching anything), the
quoted fragments do not occur on a decoy page, and an impossible folio does not
resolve. The normalisation was declared up front with those arms, **not added
after a failure** — PDF extraction breaks lines and emits ligatures, so a raw
substring test would have failed for reasons unrelated to the claim.

**Two refinements the page image forced** (`S24-13`), both of which the
intermediate record had compressed — and both of which are reasons the ruling
to go back to the source was right:

- **The attribution splits.** "Up to a multiplicative constant" is Odlyzko
  *reporting Wimp and Zeilberger* [384]. Only the next sentence is his own.
  Citing the whole passage to Odlyzko would have misattributed the first half.
- **The same page objects to Birkhoff–Trjitzinsky** — "they may not be
  rigorous, since gaps are alleged to exist in the complicated proofs". A
  referee checking p. 77 reads this. It does not bite, because **nothing in the
  paper rests on B–T**: the growth rate is Perron–Kreuser via Gautschi, `s` is
  derived directly, and B–T is cited only for the provenance of the
  normal-solution *shape*. §2.0 now requires that to be said in the same breath
  as the B–T citation.

An incidental confirmation: Odlyzko's **Example 9.4** begins on this same page,
and it is the example `CT-S22-DEPENDENCE-LIT` used for its DLMF cross-check.
Independent corroboration that the record's page number was right.

### 0-A.2 Open questions confirmed at two; Borel material to Channel Theory v1.7

Destination **named**, replacing "v1.7 or a short note". The reason given is the
test the cut section failed for the paper, applied in the other direction: in
v1.7 the material connects **by argument, not by object**. §3.4 now records the
two things v1.7 can do that no other destination can, and that **v1.7 carries
five items**.

§3.4 also gains a **TRANSIT MANIFEST** for the two items flagged as liable to be
lost in transit. Both are **method, not result** — which is precisely why they
go missing, since no claim id carries them automatically: the **PSLQ
basis-ellipsis repair** (print the basis in full; an elided basis is what hid
the `S22-21` degeneracy) and the **`ξ₀`/`ζ*` naming prohibition**.

### 0-A.3 P0 Amendment B — artefact hashing

**Appended** to `CT-S22-STOKES/P0-AMENDMENT.md`, which now carries two
amendments; Amendment A was left unaltered. That file is in an earlier session
folder, so this is flagged explicitly: the edit is **append-only and adds no
claim**, and it is the file the amendment's own text designates as the place a
future session pastes from. If the operator would rather it live elsewhere, it
moves with no loss.

The gap closed: P0's AEAL RECORD line fixes **what** must be hashed and is
silent on **when**, and it treats the checker as standing outside the system it
checks.

**This round avoided the defect structurally rather than by memory.**
`verify_outline.py` was re-run to a **new** path, `verify_outline_rev3.out.txt`,
so the eleven revision-2 claims citing `fe5657ba…` keep resolving —
`emit_claims_rev3.py` asserts exactly that, and the assertion passed.
`verify_odlyzko_p77.py` writes its own output file rather than being piped
through `Tee-Object`, removing the surface entirely.

**An ordering constraint worth recording.** The new claims must carry the
checker's output hash, but the checker cannot pass until the claims exist —
`S24-12` was correctly flagged `UNKNOWN` on the first run. Resolved in three
phases rather than by guessing: append with `output_hash = null`; run the
checker to its final path and hash the file **on disk**; write the hash back and
**read back and assert**. Hash taken after the artefact is final, as the
amendment requires.

### 0-A.4 Revision-3 state

`OUTLINE.md` 36,417 chars, sha256 `90cac85f…`. Checker **6/6 controls, 80 claim
ids cited across 12 sessions, 0 unknown, 0 missing paths, VERDICT OK.** Four new
claims `S24-12`…`S24-15`; **15 claims** in this session.

---

## 0. Revision 2 — operator rulings applied

All five rulings are in. Two produced findings rather than edits.

| ruling | applied | note |
|---|---|---|
| Attribution paragraph in §2 | **§2.0**, five numbered items | **one citation blocked** — below |
| N1: attempt once, time-boxed | §5 N1, with the fallback pre-declared | reason for attempting recorded: sympy misbehaved twice in this run |
| §9: cut (option iii) | §3.4 + the section retained unnumbered | **implies a consequence the ruling did not state** — below |
| `r`-objects: paper only + footnote | §1 and the exposition table | deposits untouched |
| Title: the first | §1 | alternate dropped with its reason |

### 0.1 One citation is blocked — Odlyzko (`S24-09`)

The attribution list names **Odlyzko p. 77 for the connection constant**.
**Odlyzko has zero occurrences anywhere in this repository** — across `.md`,
`.py`, `.jsonl`, `.txt`, `.json` — and is absent from `CT-S8-LITCHECK/refs/`
(21 files). Per the rule against inventing literature results it was **not
written into the outline**; §2.0 item 4 records the requirement as blocked
pending an operator-supplied page.

The in-repo support for the same statement is **Nemes (2026)**,
arXiv:2508.15246v2, abstract and §1 p. 3 — connection coefficients are "often
treated as unknowns in other methods" and at best computed numerically. That is
cited instead, and the Odlyzko slot left open.

**The other four are sourced and were verified before writing** (`S24-10`):
Perron–Kreuser and Pincherle via Gautschi Thm 2.3(a) p. 35 and Thm 1.1 p. 31;
DLMF **(2.9.5)**, **(2.9.6)** and the **(2.9.14)** deferral to Wong–Li (1992a),
all four present in the hashed capture `refs/dlmf_2_9.txt` at lines 127, 143,
327, 343; Wong–Li II NOT OBTAINED per `AUDIT.md` R35, with its asymmetry.

One refinement to the ruling's wording, which the repo supports: the reason the
bounded-case clauses do not apply is that `f(n) = −b(n+2)` **grows like `n^d`**,
so the expansion that defines `f₀` does not exist — for every `d ≥ 1`, as
stated.

### 0.2 The §9 cut implies a consequence the ruling did not state (`S24-11`)

The ruling was made on §9's structure. Three things leave the paper with the
Borel material, and they should be visible rather than inferred:

1. **The open-questions section drops from three items to two.** The closed form
   for `S_{ζ*}` travels with the material. The original task specified three.
2. **`CT-S23`'s repair "expand the PSLQ basis ellipsis" no longer applies to
   this paper** — but it still applies wherever the material lands, and must not
   be dropped in transit.
3. **The `ξ₀`/`ζ*` naming prohibition travels too**, since `ζ*` no longer
   appears in the paper.

Recorded in §3.4 and §4.2 of the outline, which retains the cut material rather
than deleting it.

---

## 1. What was done

`OUTLINE.md` contains, in the order the task asked for them:

- a title (ruled) and the reason the alternate was dropped;
- a two-paragraph statement — one of the result, one of the method;
- **11 live paper sections `§0`–`§10` and 2 appendices**, each with one line of
  content and, beneath it, the claim ids and session artefacts the drafting
  stage will need; plus the cut section retained unnumbered as a record;
- **§2.0, the attribution paragraph**, five numbered items, one blocked;
- **§3, what is not in the paper**: the vacuity finding, the Channel Theory
  framing, the corpus errata history, and now the Borel material — each with its
  reason, and with the two items that *look* like errata and must stay;
- **§4, the open questions** in the form they would take in a final section:
  the `z`-dependent gauge and the three scope limits on membership, with
  `S_{ζ*}` marked as leaving the paper;
- **§5, which repairs cost new mathematics**, with N1 time-boxed and N4 resolved.

**One structural decision worth flagging:** the outline adds a section the
packet did not have — **§1, Notation and standing conventions**. Most of the
171 used-before-defined items from `CT-S23` land there rather than being
scattered. That is what turns a 171-item list into one section of writing.

## 2. Claims

| id | label | in one line |
|---|---|---|
| `S24-01` | INSPECTED | The outline exists at rev 2; 79 claim ids over 11 sessions all resolve; all cited paths exist |
| `S24-02` | INSPECTED | **Completeness of the solve is not proven anywhere, and `CT-S23` mis-filed it as exposition** |
| `S24-03` | INSPECTED | Printing `(4.4)`/`H_V` is exposition — regularity at the point is already in `S16-14` |
| `S24-04` | STRUCTURAL | §9 does not join the paper: the `V_quad → P-III(D6)` map is open (`S22-22`) — **now resolved by the cut** |
| `S24-05` | INSPECTED | The "vacuity finding" is the unsourceable v1.6 one; excluded as citation, mechanism retained |
| `S24-06` | INSPECTED | The checker caught a wrong path in the outline's own first draft |
| `S24-07` | INSPECTED | No PREREG, stated rather than back-filled |
| `S24-08` | INSPECTED | All five rulings applied; sections renumbered; 11 unique live sections |
| `S24-09` | INSPECTED | **Odlyzko is not in the repository — citation blocked, not written** |
| `S24-10` | INSPECTED | The other four attribution citations verified against held, hashed artefacts |
| `S24-11` | STRUCTURAL | **The §9 cut drops the paper's open questions from three to two** |

## 3. The instrument

`scripts/verify_outline.py` extracts every claim id and every repository path
from `OUTLINE.md` and resolves them against the 461-claim corpus and against
disk. It carries **six control arms**; five assert that it *rejects* something
it should reject.

It **found a real defect**: the first draft cited
`CT-S20B-COMPONENT/task2.py`, which lives at
`CT-S20B-COMPONENT/scripts/task2.py`. Corrected.

**A loosening, recorded as a loosening.** Citations of the form
`locate_final.py:96` were flagged as missing files, so path resolution now
strips a trailing `:NN`. Because that is exactly the move that can silently
disable a check, **two further control arms were added at the same time** — a
fake path carrying a line number, and a fake sibling of a real file carrying a
line number. Both are caught. The loosening is therefore bounded by tests
rather than by intention.

Final run: 6/6 controls, 79 claim ids cited, **0 unknown**, **0 missing paths**,
VERDICT OK.

**A defect of my own process, recorded.** Re-running the checker with
`Tee-Object` **overwrote** `outputs/verify_outline.out.txt`, while seven claims
already carried the sha256 of the *previous* content. Those hashes no longer
resolved to anything. Caught on read-back, not by the checker — which does not
police its own artefact. Repaired by re-pointing all eleven claims at the
current output and correcting `S24-01`'s now-stale section count (12 → 11 live
sections). The rev-1 output is **not recoverable**; nothing depends on it, but
the right fix going forward is to version output files rather than overwrite
them when a claim already cites one.

## 4. What was NOT established

- **That the outline's section order is the right one.** It follows the
  argument's dependency order, which is not always the best reading order.
- **That the claim-to-section mapping is complete.** The checker verifies that
  every cited id *exists*; it does not verify that every id that *should* be
  cited *is*. 79 of the corpus's 472 claims are cited, and the residue is
  mostly process and cold-read material that §3 excludes by design — but no
  test confirms nothing load-bearing was dropped.
- **Any mathematics.** Nothing was computed, proven or checked numerically.
  N1 was **not** attempted in this session; it is scoped, not executed.
  (It was executed and **closed** in the separate session
  `CT-S25-N1-EXHAUSTIVE` — see §0-B.1. This section describes `CT-S24` and is
  unchanged by that.)
- **The cost estimate for N1.** It is argued to be bounded; that was not tested.
  (In the event it closed inside one session.)

## 5. Open questions for the operator

**Items 1–4 below are the revision-1 list; all four are now closed. Item 5
remains open.** The closures are recorded rather than deleted so that the
sequence of decisions is legible.

1. ~~**The Odlyzko page.** §2.0 item 4 is blocked.~~ **CLOSED at revision 3:**
   re-obtained from the author's site and verified from a page image at 5/5
   controls (`S24-12`), retained **alongside** Nemes (§0-A.1).
2. ~~**N1 is scoped but not run.**~~ **CLOSED at revision 4:** attempted once,
   inside its box, and **proved** by `CT-S25-N1-EXHAUSTIVE` (`S25-02`,
   `S25-06`). The fallback was not taken (§0-B.1).
3. ~~**Where does the Borel material go?**~~ **CLOSED at revision 3:** Channel
   Theory **v1.7**, with a transit manifest for the two method items that carry
   no claim id (§0-A.2).
4. ~~**Two open questions, not three.**~~ **CONFIRMED at revision 3:** the
   z-dependent gauge and the scope limits on membership; `S_{ζ*}` travels with
   the Borel material.
5. **`CT-S23` open question 5 is still open** — PREREG arm (i) needs replacing
   with a graded observable, not deleting. Unchanged by this session.

**New, from revision 4 — one item.** The paper now has **no new mathematics left
to do**. The remaining decision is not mathematical: whether drafting begins
with the paper or with **Packet 2 (Channel Theory v1.7)**, which is ready and
independent of it.

**New, from revision 5 — one item, small but real.** ~~§1 ¶2 now asserts a
**two-sided** bound on `r_∞`, and only the lower half is proved anywhere
(`S1-02`). The upper bound `r_∞ ≤ exp Σ 1/(b(k)b(k+1))` is a one-line addition
to `prop:positive` that **has not been written**, and it carries no claim id.
It is the one place in the outline where the text is ahead of the corpus.
Decide at drafting: prove it and emit a claim, or weaken the sentence. It must
not be written citing `S1-02`.~~
**CLOSED at revision 6.** Proved as Proposition U in `CT-S26-UPPER-BOUND`
(`S26-01`, PROVEN); the fallback was not taken; §1 ¶2 stands. The text is no
longer ahead of the corpus anywhere. Two residues, neither a decision: the
~15-line insertion into `theorem.tex` at drafting (not done here — earlier
session), and the requirement to state the positivity hypothesis explicitly
because it is load-bearing (`S26-04`).

**New, from revision 6 — one item, for the operator, not for drafting.**
`CT-S26-UPPER-BOUND/REPORT.md` §6 asks where Proposition U should land. The
recommendation is `theorem.tex` after `prop:positive`, combined with it into one
two-sided statement — but that is an edit to an earlier session's file, and this
session did neither a copy-forward nor sought a waiver.

Also still pending: `CT-S22-STOKES/P0-AMENDMENT.md` remains **PROPOSED**, now
carrying **two** amendments (A, basis degeneracy; B, artefact hashing).

## 6. Uncommitted files

```
sessions/2026-09-17/CT-S24-PAPER-OUTLINE/
  OUTLINE.md                              revision 6, sha256 6c992dd5…
  REPORT.md
  claims.jsonl                            22 claims, S24-01…S24-22
  scripts/verify_outline.py
  scripts/verify_odlyzko_p77.py
  scripts/emit_claims_rev3.py
  scripts/emit_claims_rev4.py
  scripts/emit_claims_rev5.py
  scripts/emit_claims_rev6.py
  refs/odlyzko_asymptotic_enum.pdf        d0b58928…
  refs/odlyzko_p77.png                    f9843a43…
  outputs/verify_outline.out.txt          fe5657ba…  (revision 1 — do not touch)
  outputs/verify_outline_rev3.out.txt     490c7076…  (revision 3 — do not touch)
  outputs/verify_outline_rev4.out.txt     08644185…  (revision 4 — do not touch)
  outputs/verify_outline_rev5.out.txt     20a4f5fa…  (revision 5 — do not touch)
  outputs/verify_outline_rev6.out.txt     c4b99450…
  outputs/verify_odlyzko_p77.out.txt      78cbabfe…

sessions/2026-09-17/CT-S22-STOKES/
  P0-AMENDMENT.md                         append-only edit; Amendment A unaltered

sessions/2026-09-17/CT-S26-UPPER-BOUND/   (separate session; see its own REPORT.md §7)
  PREREG.md  PROOF.md  ADDENDUM-1.md  REPORT.md
  claims.jsonl                            7 claims, S26-01…S26-07
  scripts/upper_bound.py  scripts/emit_claims.py
  outputs/upper_bound.out.txt             a220c136…  (the FAIL run — do not touch)
  outputs/upper_bound_rev2.out.txt        f1f32dd8…
```

The earlier `outputs/` files are listed as **do not touch** because claims cite
their hashes; re-running a checker over them would invalidate those citations
(P0 Amendment B).

Nothing was committed, pushed, deposited or sent.
