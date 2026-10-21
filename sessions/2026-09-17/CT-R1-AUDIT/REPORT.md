# REPORT.md — CT-R1-AUDIT

Session: `sessions/2026-09-17/CT-R1-AUDIT/`
Round **R1**, responding to the operator review of the P1–P5 deliverables.

**No pre-registration file.** P0 requires PREREG before *computation*. This
round is an audit: read-only inspection, symbolic re-derivation by hand, one
document download, and a bookkeeping script that rewrites label fields. No
hypothesis was tested against data and no threshold existed to retune. Flagging
this explicitly rather than back-filling a vacuous PREREG.

**Governance:** nothing committed, pushed, tagged, or deposited. HEAD unchanged.
All new files are inside `sessions/2026-09-17/`. Files in earlier sessions were
edited **only** to amend claim labels and to correct one overstated finding;
every such change is marked in-place with `amended_in` / `label_before` or an
explicit "AMENDED IN AUDIT ROUND R1" banner with the original text retained.

---

## 1. What was done

The operator's six items, in order of what they turned up.

### 1.1 The `.gitignore` check (operator's closing flag) — clean

`git status --porcelain --untracked-files=all` reports exactly one `.gitignore`,
at `sessions/2026-09-17/CT-S1-THEOREM/lean/.gitignore`, untracked. `git diff` on
the repo-root `.gitignore` is empty. The 6.5 GB `lean/.lake/` tree is covered
from inside the session folder. **No unintended repo change.** → `R1-01`

### 1.2 The PROVEN audit (operator's headline ask) — 3 downgrades, 1 upgrade, 1 real defect

Full detail in **`AUDIT.md`**. Summary:

* **A load-bearing unproved assertion was found in the part (i) proof.**
  `theorem.tex` Step 3 asserted, without proof, that the balanced multinomial
  coefficient is maximal. The *upper* bound does not need this, but the *lower*
  bound `d^{dn}/(dn+1)^{d−1} ≤ (dn)!/(n!)^d` is `max ≥ average` and collapses
  without it. Repaired with an exchange argument. Steps 1, 2, 4, 5 are correct
  as written, and the no-Stirling constraint is genuinely met. → `R1-02`
* **3 downgrades PROVEN → STRUCTURAL:** `S2-05` (a negative grep cannot prove
  absence), `S3A-03`, `S3A-06` (file inspection). The operator's suspicion was
  correct.
* **1 upgrade STRUCTURAL → PROVEN:** `S1-04`, because Gap G1 was closed.
* **7 upheld**, 3 of them with the basis restated — notably `S4-03`, whose proof
  is the symbolic derivation, not the 39-order residual check that the claim
  text used to lead with.
* **Taxonomy defect reported, not patched:** P0 has no label for "a verified
  fact about repository contents". I made all `file_inspection` claims
  STRUCTURAL so the corpus is at least internally consistent — previously
  `S3A-03/06` were PROVEN while `S4-01/02` were STRUCTURAL on identical
  evidence. The operator should rule on this.

### 1.3 Gap G1 — closed

Most of it is now proved in-session from `Γ(x+1) = xΓ(x)` alone, including all
the `O(1/n)` bookkeeping that part (ii) actually consumes. The residue is the
single constant `h_∞ = 1`, cited to **DLMF (5.11.12)**, §5.11(iii), `G_0 = 1` —
equation number and statement checked against `dlmf.nist.gov/5.11`, not recalled.
`theorem.pdf` is now 7 pages and compiles with no undefined references or
citations. → `R1-03`, `R1-11`

### 1.4 The companion-paper version question — the finding was wrong, but not in the way expected

The operator suspected a v1.0/v1.1 copy would explain "Conjecture 4.1 does not
exist". **It is worse than that: there is no copy at all.** CT-S4 searched
`VQUAD-PERIODREP-PAPER-001`, which is the *period-rep paper*; the companion is a
**different document** (`\bibitem{Vquad}`, Zenodo DOI `10.5281/zenodo.20455090`).
A repo-wide title-string search finds it **only** in bibliography entries,
preambles and outlines. The claim is retracted as a citation defect and restated
as missing data; `CT-S4-FORMAL-TYPE/REPORT.md` §2.1 was rewritten with the
original text retained in a `<details>` block. Finding **S4-F1 stands**, with a
different reason. → `R1-05`

### 1.5 The classification source — verified, obtained, and it pays off immediately

van der Put & Saito, *Ann. Inst. Fourier* **59** (2009), no. 7, 2611–2667, DOI
`10.5802/aif.2502`. Verified against publisher metadata and the PDF title page;
open-access copy placed at
`refs/vanderPut-Saito-AIF-2009-59-7-2611.pdf` (58 pp, sha256 `1666bd6b…`).
It is the right source — it explicitly covers *ramified* irregular
singularities, which Jimbo–Miwa–Ueno's tables exclude. **P5 step 3's halt
condition is lifted.** → `R1-06`, `R1-07`

Table 2.1 (p. 2635) extracted verbatim into **`CLASSIFICATION-TABLE.md`**. The
families are indexed by Katz-invariant multiset, and matching our systems gives
a sharp result:

| object | Katz multiset | Table 2.1 row |
|---|---|---|
| System A (`f = ΣQ_n zⁿ`) | `(1/2, −, 1/2)` | **D̃8, PIII(D8)** |
| `π*`System A under `z = w²` | `(1, −, 1)` | **D̃6, PIII(D6)** |
| D5⁽¹⁾ target | `(0, 0, 1)` | D̃5, **PV** |

The first two are exact matches and mutually consistent (a quadratic cover is
the classical PIII(D8)↔PIII(D6) relation). **Neither is PV.** → `R1-08`

System B does **not** match any row at face value (one Katz-1 irregular point
plus *three* regular singular points; the table allows `#S = 4` only when all
`r(p) = 0`). If exactly one of `{ρ±, ∞}` is **apparent** it becomes `(0, 0, 1)`
= PV. That is the open hinge and I did not close it. → `R1-09`, labelled
**CONJECTURED**

### 1.6 P5b — run, and independently re-derived

Delegated session `CT-S5B-COVER` applied `z = w²` to System A and `z ↦ 1/z` to
System B. I re-derived its two central computations by hand rather than
accepting them; **every value matches exactly** (`AUDIT.md` §5). Its verdict:
the ramified/unramified mismatch is a **coordinate artefact locally at the
branch point**, but global configurations are not reconciled, so CT-S4's verdict
(c) is *sharpened, not settled*. → `R1-10`

---

## 2. Claims

11 claims in `claims.jsonl`: **3 PROVEN, 1 VERIFIED, 6 STRUCTURAL, 1
CONJECTURED.**

Corpus after R1: **58 claims — 19 PROVEN, 11 VERIFIED, 27 STRUCTURAL, 1
CONJECTURED**, across seven session folders. Every row parses and carries
exactly one valid label.

---

## 3. What was NOT established

* **Nothing is machine-checked.** `lean/XiZero/Basic.lean` still has 7 `sorry`s
  and states only part (i). PROVEN throughout this corpus means "complete
  human-written proof", per P0.
* **The part (i) review was mine, not independent.** The operator offered
  "either / or"; I read it directly. If a genuinely cold read is still wanted,
  the repaired Step 3 sub-lemma is the passage to hand over.
* **System B's row in Table 2.1 is unresolved**, pending the apparency
  computation for `ρ±` and `∞`. VQ-N1's apparent indices `[0,0]` were not
  recomputed — by CT-S5B-COVER or by me.
* **Global isomorphism** of `π*`System A with System B remains unestablished;
  the computed global configurations disagree.
* **The 2317.8 digits of `r_∞` remain VERIFIED, not rigorous.** Unchanged, and
  still adequate for the dps-2000 PSLQ null.
* **The 10 VERIFIED labels were not re-audited** — not asked for, and each
  traces to a script and a hashed output.
* **Gap G1's residual citation** is a citation, not a proof. Named explicitly in
  the abstract, at the point of use, and in §`sec:gaps`.

---

## 4. Open questions for the operator

1. **Rule on the taxonomy gap.** P0's four labels have no slot for verified
   facts about repository contents. I used STRUCTURAL. Confirm or replace.
2. **Supply the V_quad companion paper.** It is absent from this repo in every
   version. Until it arrives, "Conjecture 4.1" cannot be checked, and P5 step 1
   stays halted.
3. **Authorise the apparency computation** for System B's `ρ±` and `∞`. It is
   the one remaining step between the current state and a decidable answer on
   whether System B is the D̃5 / PV row.
4. **Note the consequence of `R1-08` for "two objects, two surfaces".** Because
   the Katz multiset is an invariant of the family, and System A lands on
   PIII(D8) while the D5⁽¹⁾ target is PV, the two-objects reading is **not**
   merely a coordinate artefact at the level of Table 2.1 rows. This is
   STRUCTURAL and deliberately not written into any conjecture file.
5. **`op:cc-median-resurgence-execute` should be restated** to name which formal
   series its ζ\* Stokes constant concerns, per your own reading that `K` is
   ξ₀-level connection data for `f = ΣQ_n zⁿ` and therefore **not** `S_{ζ*}`.
   No repo file was edited to this effect.
6. **Deposit decision is yours** — Channel Theory v1.7 or standalone note. Both
   theorems are now PROVEN (part (ii) modulo one named classical citation).

---

## 5. Uncommitted files

Created this round, in `sessions/2026-09-17/CT-R1-AUDIT/`:

* `AUDIT.md` — the audit of the 13 PROVEN labels
* `CLASSIFICATION-TABLE.md` — verified citation, Table 2.1 verbatim, and the matches
* `REPORT.md` — this file
* `claims.jsonl` — 11 claims
* `apply_audit.py`, `apply_audit.log` — the label amendment script and its output
* `make_claims.py`
* `refs/vanderPut-Saito-AIF-2009-59-7-2611.pdf`

Created this round, in `sessions/2026-09-17/CT-S5B-COVER/` (delegated P5b):

* `PREREG.md`, `formal_type.py`, `formal_type_p5b.json`, `run.log`,
  `claims.jsonl`, `REPORT.md`

Modified this round, in earlier session folders:

* `CT-S1-THEOREM/theorem.tex` — Step 3 sub-lemma added; Gap G1 closed;
  bibliography added; abstract labels updated
* `CT-S1-THEOREM/theorem.pdf` — recompiled, 6 → 7 pages
* `CT-S1-THEOREM/claims.jsonl`, `CT-S2-RHO-D4/claims.jsonl`,
  `CT-S3A-ZETA-AUDIT/claims.jsonl`, `CT-S3B-RINF/claims.jsonl`,
  `CT-S4-FORMAL-TYPE/claims.jsonl` — label amendments
* `CT-S4-FORMAL-TYPE/REPORT.md` — §2.1 rewritten, original retained inline

Nothing outside `sessions/2026-09-17/` was touched.

---

# R2 — response to operator review #2

All four rulings executed or honoured. **No commit, push, tag, PR, or deposit.**
HEAD unchanged. Everything below is uncommitted files under
`sessions/2026-09-17/`.

## R2 — what was done

| ruling | action | status |
|---|---|---|
| 1 — adopt `INSPECTED` | applied across all 7 `claims.jsonl`; both sub-rules enforced, rule 1(a) asserted programmatically | **done** |
| 2 — get the companion from Zenodo | 3 versions downloaded to `refs/`, sha256 recorded; **Conjecture 4.1 question settled** | **done** |
| 3 — authorise apparency computation | `CT-S6-APPARENCY` launched with the operator's scope verbatim, plus System C and Remark 2.2 added mid-run | **running** |
| 4 — leave the open problem as a flag | no restatement written | **honoured** |
| caveats on §3 | recorded in `CLASSIFICATION-TABLE.md` §5 | **done** |

## R2 — the headline result

**The operator's version hypothesis was right, and it was the whole explanation.**
Object 4.1 is a *Theorem* in companion v1.0 and v1.1, and becomes a *Conjecture*
only at v1.2. The repo cites version DOI `…20455090` = **v1.0**. There is no
citation defect — only a version mismatch.

**And Conjecture 4.1 is about a system neither CT-S4 nor CT-S5B analysed.** It
concerns **System C**, `(3x²+x+1)y'' + (6x+1)y' − x²y = 0` (companion §2.2,
eq. (6)–(7)). Its finite singular points `(−1 ± i√11)/6` are exactly those of the
*inverted* System B, which strongly suggests System B and System C are related by
`z ↦ 1/z` up to gauge — **not proved**.

This matters for the classification finding: the conjecture's own text concedes
that its `D5^(1)` determination rests on the **Jimbo–Miwa–Ueno** tables, which
**exclude ramified cases**. Ramification is precisely what CT-S4/S5B found. So
the conjecture's evidential base cannot, by construction, see the alternative
that the van der Put–Saito table raises.

## R2 — claims

Five new claims `R1-12 … R1-16` appended to `CT-R1-AUDIT/claims.jsonl`; five
existing claims rewritten (`S2-05`, `S3A-06` rephrased per rule 1(b);
`S4-01`, `S4-08`, `R1-05` marked SUPERSEDED). Corpus is now 63 claims:
PROVEN 19, INSPECTED 20, STRUCTURAL 13, VERIFIED 10, CONJECTURED 1.

## R2 — what was NOT established

* **System C has not been analysed.** Its formal type, and whether its finite
  singularities really are apparent as companion Remark 2.2 asserts, are in
  `CT-S6-APPARENCY`'s scope and not yet returned.
* **System B ≅ inverted System C** is suggested by coincident singular points,
  not proved. A gauge transformation would have to be exhibited.
* **The `−` slot in System A's `(1/2, −, 1/2)`** remains an unjustified premise.
* **No membership claim.** Per the operator's caveat, a matching Katz multiset is
  necessary, not sufficient; no deformation parameter has been exhibited for any
  system, so nothing here identifies a Painlevé family.
* **Nothing is machine-checked.** Seven `sorry`s remain in `XiZero.lean`.
* `r_∞`'s 2317.8 digits remain **VERIFIED**, not rigorous.

## R2 — open questions for the operator

1. **Schema (claim R1-16).** Confirm or replace the new
   `evidence_type: "proof"`. Twelve genuine mathematical results were tagged
   `file_inspection` only because their proofs live in `.tex`/`.md` files;
   literal rule 1(a) would have demoted them. See `AUDIT.md` §R2.2.1.
2. **Bibliography.** The repo's `\bibitem{Vquad}` points at v1.0 and carries a
   title that differs from the actual Zenodo title across all three versions.
   Correcting it is an authoring decision; **no file was edited.**
3. **The historical record.** Does the PIII(D8)/PIII(D6) finding warrant
   revisiting the v1.4 "correction" from PIII(D6) to `D5^(1)`? Not touched.
4. **Deposit route** — v1.7 versus standalone note. Operator's decision.

---

## R2 addendum — `CT-S6-APPARENCY` complete

The apparency session authorised by ruling 3 has returned and been
independently spot-checked (`VERIFY-S6.md`, `verify_s6.py`). Three outcomes
change the picture:

1. **Companion Remark 2.2 is false, in general.** Not merely unsupported: for
   `χy'' + χ'y' + cy = 0` at any simple root of `χ` with `c(s) ≠ 0` the indicial
   polynomial is `λ²`, so the exponents are always `0,0` and the point is never
   apparent. PROVEN. **Conjecture 4.1 uses apparency as a premise**, so its
   argument for `β = γ = 0` fails.
2. **Its conclusion nevertheless survives.** System C's effective Katz multiset
   is `(0,0,1)`, which **is** the D̃5 / PV row of van der Put–Saito Table 2.1,
   p. 2635. Right row, wrong reason.
3. **System C = inverted System B, exactly** — identical normal forms. And CT-S6's
   own `(1,0,0,0)` for System B is superseded: the point `z = ∞` becomes
   *ordinary* under the rank-1 twist implicit in the normal form, so System B's
   effective multiset is `(0,0,1)` too, as the equivalence requires.

System A is unaffected: its multiset is ramified, and half-integer Katz
invariants survive twisting, so it cannot move into the `(0,0,1)` row. The
`−` slot question is closed — it marks an **absent** point (S6-C9, PROVEN).

**Still not established:** family membership for any system, for the reason in
the operator's caveat 5.1 — no deformation parameter has been exhibited. That
remains the open well-posedness problem.

**Additional open question for the operator (5).** Conjecture 4.1's *reason* is
now refuted while its *conclusion* stands. Whether that warrants any action is
an authoring decision; **no conjecture file was edited.**

### Final file list (all uncommitted, all under `sessions/2026-09-17/`)

`CT-R1-AUDIT/`: `AUDIT.md`, `CLASSIFICATION-TABLE.md`, `REPORT.md`,
`VERIFY-S6.md`, `claims.jsonl` (21), `apply_audit.py`, `apply_audit_r2.py`,
`verify_s6.py`, `append_verify_claims.py`, `make_claims.py`,
`list_inspection.py`, logs, and `refs/` (van der Put–Saito PDF + companion
v1.0/v1.1/v1.2 PDFs, sha256 recorded).
`CT-S5B-COVER/`, `CT-S6-APPARENCY/`: as reported by those sessions.
Amended in place: `CT-S1-THEOREM/{theorem.tex,theorem.pdf,REPORT.md}`,
`CT-S4-FORMAL-TYPE/REPORT.md`, and the `claims.jsonl` of all sessions.

HEAD `08aa0e2381b3dc37ee54a3200b7272755ca11d59`, unchanged. Nothing committed,
pushed, tagged, deposited, or submitted.

---

# R3–R5 — response to operator review #3

## R3.1 The two confirmations, applied

* **Correction A (Remark 2.2 lemma is more general).** Accepted and applied.
  The `c(s) ≠ 0` hypothesis is dropped: at any simple root `s` of `χ`, `p = χ'/χ`
  has residue exactly 1 and `q = c/χ` has at most a simple pole, so the indicial
  polynomial is `λ²` **whatever `c(s)` is**. Equal exponents at a regular
  singular point force a log term, so the point is never apparent. Claim
  **R1-18** rewritten; `VERIFY-S6.md` §2 amended.
* **Correction B ("up to twist").** Accepted and applied. System B's `(0,0,1)`
  is valid in Table 2.1's setting (trace-free rank-2 connections) because that
  setting is equivalence up to rank-1 twist — not equivalence of the operators.
  Claim **R1-20** rewritten to say "up to twist"; `VERIFY-S6.md` §3 amended.

## R3.2 Ruling 1 — `evidence_type: "proof"` with a `review` field

Adopted. Values `self | cold | lean`; deposit requires `cold` or `lean`.
Backfilled across the whole corpus; the invariant "no `file_inspection` claim is
PROVEN" is re-checked by `apply_audit_r5.py` on every run and currently holds.

Current state: **21 proof claims — `self` 19, `cold` 2, `lean` 0.**
The two `cold` claims are `S1-03` and `S1-04`, i.e. exactly the two the operator
named. `lean` remains empty and will stay so while the 7 `sorry`s exist.

One label-creep incident was caught and reversed while applying this ruling:
`CT-S10-COLDREAD2` marked **its own** supporting lemmas `review: cold`. It was a
cold reader *of `theorem.tex`*, but nobody has cold-read **it**, and a session
cannot cold-read itself. Those two claims were downgraded to `self`. Its verdict
on `theorem.tex` is unaffected, and remains what moved `S1-03`/`S1-04` to `cold`.

## R3.3 Ruling 2 — the stale `\bibitem{Vquad}`: located, and no fix needed

The operator's first hypothesis was right. The bibitem is **not** in Channel
Theory at all — it is in the **period-rep paper**, and the repo source is older
than the deposit. Specifically:

* the **2026-06-16 cascade** already carries the real Zenodo title and the
  **concept DOI** — this is the deposit-ready `run-2` path, and it is **correct**;
* only the **superseded 2026-06-15 draft** and **REPRO-BUNDLE-001** still hold
  the stale version pin.

So there is nothing to fix on the path that matters. Recorded, not fixed, per
the ruling. One residual remains for the operator: the version read is named
only in prose, not inside the bibitem itself.

## R4 — gate 1, first pass

`CT-S7-COLDREAD` found a genuine defect in `theorem.tex`: DLMF **(5.11.12)** was
misquoted as the full `G_k` expansion. Rather than take the agent's word, the
live DLMF page was downloaded and parsed directly (stored, sha256
`929045c7…`): (5.11.12) is the plain ratio, **(5.11.13)** is the `G_k`
expansion, **(5.11.15)** gives `G_0 = 1`. The proof only ever needed (5.11.12),
so the **mathematics was unaffected**; the citation was wrong at five sites and
is now repaired.

## R5 — ruling 4, and gate 1 closed

### Ruling 4 — PV parameters re-derived

`CT-S9-PVPARAMS` did not halt; it found a quotable convention. Its dictionary
was verified against the **primary source by reading the page image** (Jimbo,
PRIMS, p. 1152) and its computation re-derived from scratch. CT-S9 is correct,
and `VERIFY-S9.md` adds three things it missed:

1. **The contradiction is genuine, not conventional.** Under `z ↦ cz`, PV maps
   `(α,β,γ,δ) → (α,β,cγ,c²δ)`; holding `δ = −1/2` forces `c = ±1`, so `γ = 1`
   **cannot** be rescaled to `γ = 0`.
2. **Jimbo's (A1)_PV (`θ₀, θ_t ∉ ℤ`) is violated** by `θ₀ = θ_t = 0`. The
   dictionary precedes (A1) and survives; the rest of Jimbo's machinery does not
   cover this case. This coheres: integer `θ` is the resonant case, and
   resonance is when logs appear — which CT-S6 independently found.
3. **The PV time is fixed, not free:** `t = ∓2i√33/9`. This answers the
   operator's standing question. System C is a single *fibre*, so a membership
   claim must exhibit an isomonodromic **family** with that fibre. Not found.

Net: **right row, wrong reason — and now also wrong parameters.**

### Gate 1 — CLOSED

`CT-S10-COLDREAD2` re-read the repaired passage cold and found the mathematics
sound, including the corrected equation numbers. Its only finding was a second
citation defect: **Release 1.2.4** vs the actual **Version 1.2.8, release date
2026-09-15**. Confirmed against the stored page, corrected, recompiled clean at
7 pages. `S1-04` is now `review: cold`.

**Three independent reads produced three defects, all in citation metadata, none
in the argument.** See `DEPOSIT-PLAN.md` for the recommendation that follows.

## R3–R5 — what was NOT established

* **Gate 3 (prior art) — still open**, and still the largest risk. The growth law
  is close to classical material (Perron, Birkhoff–Trjitzinsky, Wong–Li), and
  until `CT-S8-LITCHECK` returns, **the note's contribution claim is unsupported**.
* **Gate 2 — open by design.** 7 `sorry`s remain in `XiZero.lean`; nothing is
  machine-checked, and the note must not say otherwise.
* **Family membership — open for all three objects.** Every row match in
  Table 2.1 is a necessary condition only.
* **The source of the v1.0–v1.3 PIII(D₆) label** is still not established.
  Nothing in this run shows which object it was derived for. My earlier reading
  that the old label "may have been closer to right" is **withdrawn**.
* **`α = 1/6`** is neither confirmed nor refuted — it is undetermined by local
  scalar data, since `α = θ∞²/8` and `θ∞` is not fixed by that data.

## R3–R5 — open questions for the operator

1. **The bibitem residual:** the version read is named in prose, not in the
   bibitem. Fix in that paper's next version, or leave?
2. **The citation-hygiene pattern:** should every external reference in the note
   be re-fetched and hashed at deposit time? (Recommended; cheap.)
3. **The historical record:** does the PIII(D₈)/PIII(D₆) finding warrant any
   action on the v1.4 "correction", beyond the note scoped in
   `CORRECTION-NOTE-SCOPE.md`?
4. **Conjecture 4.1** now has its conclusion intact while both its *reason* and
   its *parameter values* are refuted. Errata-style handling in the next
   companion version is an authoring decision and is left to the operator.

---

# R6 — gate 3 returned

See `AUDIT.md` R6, `VERIFY-S8.md`, and `DEPOSIT-PLAN.md` §§4–6.

**The prior-art gate the operator insisted on has paid for itself.** Result 1 —
the piece described as "the deposit-worthy core" — is a corollary of the
Perron–Kreuser theorem plus Pincherle's theorem, both classical. This was
verified independently, not merely accepted from the agent, and one OCR artefact
that would have flipped the conclusion was caught by re-rendering the source page.

Consequences:

* The contribution claim is rewritten (`DEPOSIT-PLAN.md` §5): Result 1 is
  presented **with attribution** as a corollary; the contribution is the explicit
  amplitude `K`, the Borel framing, and the vacuity explanation.
* `S1-03` keeps PROVEN and `review: cold`. Correctness and priority are separate
  axes; priority is recorded in a new `audit_r6` field rather than by inventing a
  label.
* **Deposit is not recommended** while gate 3 is open.

## R6 — what was NOT established

* **Whether `s = β_{d−1}/β_d + (d−1)/2` is already in print.** DLMF §2.9
  explicitly defers our case to **Wong & Li, *Stud. Appl. Math.* 87(4) (1992),
  289–324**, which is paywalled and was not obtained. NOT FOUND ≠ new.
* **How much weight the `K` novelty claim can carry** while the above is open.
* Sources not obtained, each listed with what would have been checked:
  Perron 1911 *Acta Math.* 34; Pincherle 1892; Birkhoff 1930 (Project Euclid
  bot-blocked); Perron's *Kettenbrüche* 1913 (scan downloaded but **no OCR
  layer — not searched, and no claim is attributed to it**); Elaydi, Kooman,
  Van der Cruyssen, Wimp App. B.

## R6 — open questions for the operator

1. **Wong & Li (1992a) access** — institutional, interlibrary, or a request to
   the authors. This is the one blocking item, and it is not resolvable from open
   sources. Everything else about the deposit waits on it.
2. Given Result 1 is classical, is a standalone note still the right route, or
   does the reduced contribution sit better as a section of Channel Theory v1.7?
   This is an authoring decision and is entirely the operator's.
3. Should `refs/` sources that were obtained be retained in-session, or moved to
   a shared `refs/` area for reuse? (Nothing has been moved.)

---

# R7 — operator review #4

Full detail in `AUDIT.md` R7. Drafts: `DRAFT-CT-v1.7-NOTICE.md`,
`DRAFT-COMPANION-v1.3-NOTICE.md`. Standing rule: `P0-CITATION-RULE.md`.

## R7 — what was done

1. **Wong–Li access** — attempted and **failed legitimately**. Paywalled at
   Wiley; no mirror or shadow library used. The citation itself was verified and
   a numbering trap found: DLMF's "1992a" is the paper titled **"II"**
   (*Stud. Appl. Math.* 87(4), 289–324). Quote the full citation when requesting.
2. **Channel Theory v1.7 notice drafted** — items N1–N4, with `[WONG-LI]`
   passages carrying two alternative phrasings so the draft is complete either
   way.
3. **Companion v1.3 correction notice drafted** — items C1–C4, with C3 written
   in the well-posedness form the operator specified: *"has the local formal
   type of the PV/D̃₅ family; whether it embeds in an isomonodromic PV
   deformation is open."*
4. **Both cold reads run and returned.** A: SOUND, and it **improved the proof**.
   B: SOUND WITH CAVEAT, having independently re-derived the rescaling law in
   both conventions and independently rediscovered the (A1)_PV violation.
5. **P0 citation rule adopted**, with the measured evidence base recorded.

## R7 — claims

`R1-43` … `R1-49` appended; `R1-18`, `R1-31`, `R1-32`, `R1-33` promoted to
`review: cold`. Corpus: **178 claims** — PROVEN 63, INSPECTED 64, STRUCTURAL 31,
VERIFIED 19, CONJECTURED 1. The invariant "no `file_inspection` claim is PROVEN"
holds.

## R7 — what was NOT established

* **Whether the exponent formula `s` is already in print.** Unchanged, and
  unresolvable without Wong & Li (1992a).
* **Family membership for any of objects A, B, C.** All row matches remain
  necessary conditions only.
* **The affine identification** of System C's finite singular points with
  Jimbo's `0` and `t` remains an assumption — independently confirmed as such by
  the cold reader, not merely asserted by the originating session.
* **Nothing is machine-checked.** Seven `sorry`s remain.

## R7 — open questions for the operator

1. **Wong–Li (1992a) access.** The one blocker. Both `[WONG-LI]` alternatives
   are pre-written, so the v1.7 draft can be finalised the day the paper is read.
2. **Scope of the `review` field** — see `AUDIT.md` R7.5. It has been applied to
   three non-proof claims; restrict it if you prefer.
3. **Order of the two notices.** The companion v1.3 correction is the stronger
   material and does not depend on Wong–Li; it could go out first, with Channel
   Theory v1.7 following once the paper is obtained.

---

## R8 — Operator review #5 (Wong-Li request, review taxonomy, companion-first deposit)

### What was done

1. **Author request drafted and corrected.** The operator's draft arrived
   separately from review #5. The requested title check **fired**: the draft
   omitted the word *linear* from both the subject line and the citation. Both
   the publisher record (Crossref, DOI `10.1002/sapm1992874289`) and the stored
   DLMF bibliography carry it. Corrected in both places, and the DOI added, so
   the identification no longer rests on the title — which matters because DLMF
   **1992b** carries the same title minus "II" and is the wrong paper.
   The signature block was verified against the 2026-06-16 deposit metadata,
   ORCID digit by digit. → `AUTHOR-REQUEST-WONGLI.md`
2. **`review` taxonomy refined** with a type-dependent definition of `cold` and
   a mandatory `review_note`. Retro-applied: 8 cold, 28 self, none missing a
   note. `R1-40` promoted; no downgrades needed. → `apply_audit_r8.py`
3. **Gate 1 PASS.** All 11 quoted tuples, equation numbers and remark numbers
   verified against companion v1.2 from 3× page images. → `GATE1-VERIFY.md`
4. **Gate 3 PASS after one fix.** C3 did not match the drafted wording.
5. **Gate 2 dispatched** as an isolated cold read of C4.

### Claims

| ID | Label | Review | Substance |
|---|---|---|---|
| R1-61 | INSPECTED | self | Wong-Li title defect: "linear" missing; corrected |
| R1-62 | INSPECTED | self | Identity block matches the repository exactly |
| R1-63 | INSPECTED | self | Gate 1: all 11 quoted items match v1.2 |
| R1-64 | INSPECTED | self | v1.2 itself states and uses `(α,β,cγ,c²δ)` |
| R1-65 | PROVEN | self | `γ = 1` on the companion's own `θ` values; independent of C1 |
| R1-66 | INSPECTED | self | Five downstream passages depend on apparency (C5) |
| R1-50 | INSPECTED | self | Gate 3: C3 wording defect found and fixed |
| R1-51 | INSPECTED | self | Review taxonomy refined and retro-applied |

Corpus: **187 claims** — INSPECTED 71, PROVEN 64, STRUCTURAL 31, VERIFIED 20,
CONJECTURED 1. Rule 1(a) invariant (no `file_inspection` claim is PROVEN)
**holds**.

### What was NOT established

* **Wong–Li (1992a) is still NOT OBTAINED.** It remains the sole blocker on the
  Channel Theory v1.7 notice. Purchase and sending are operator-gated.
* **No current contact address was looked up**, per instruction. A City
  University of Hong Kong association appeared in an earlier open web search and
  is recorded as **unverified**; it is a starting point, not a finding.
* **Gate 2 is open** pending CT-S13's return.
* Nothing is machine-checked; the 7 `sorry`s in `XiZero.lean` remain.
* Family membership remains open for all three objects; every row match is a
  necessary condition only.

### Open questions for the operator

1. **Does C5 change the scope of the v1.3 notice?** §7.1 item 1 is presented in
   v1.2 as one of four components of a "complete explanation". Withdrawing it
   weakens a summary section that is not otherwise in error. Whether the notice
   should re-argue it or simply withdraw it is an authoring decision.
2. **Should C2 lead with F2 rather than C1?** F2 does not depend on any lemma
   proved in this run, so it is the more robust ground. C1 remains necessary for
   Remark 2.2 itself and for the monodromy statement.
3. **Optional sharpenings to the email** (§2.9 → §2.9(ii); "your paper" → "the
   *Studies* paper") were identified but **not applied**, so the draft comes
   back with exactly the defect fixed and no editorial drift.

### R8 addendum — Gate 2 CLOSED

`CT-S13-COLDREAD5` returned after the section above was written. It independently
reproduced the Katz data and both Table 2.1 lookups, returned **ERROR** on the
family-membership inference (A6), and found a restriction this run did not have:
van der Put–Saito p. 2634 exempts **`(1/2, −, 1/2)`** — object A's own type —
from the strong Riemann–Hilbert guarantee, and restricts the row accordingly. I
re-read that page from the PDF and confirm the quotation.

C4 was weakened and re-grounded (new points 1, 5, 6, 7); its review status moves
`self` → **cold**. One caveat the reader raised was **declined on evidence**: the
three-entry notation is the authors' own, per the running text on the same page.

Claims `R1-52`–`R1-55` appended. → `VERIFY-S13.md`

**All three gates on the companion v1.3 notice are now closed.**

| Gate | Status |
|---|---|
| 1 — PV tuple and quoted numbers vs v1.2, from page images | **PASS**, no defect; two findings that strengthen C2 |
| 2 — cold read of C4 | **PASS**, one defect found and fixed |
| 3 — "necessary condition" wording; C3 verbatim | **PASS** after one fix |

Final corpus: **198 claims** — INSPECTED 73, PROVEN 68, STRUCTURAL 34,
VERIFIED 22, CONJECTURED 1. Review: 44 `self`, 11 `cold`, **none lacking a
`review_note`**. Rule 1(a) invariant holds. HEAD `08aa0e2`, unchanged.

**The deposit is now yours to make.** Nothing has been committed or submitted.

---

## R9 — Operator review #6 applied

| Ruling | Applied |
|---|---|
| `dim P = 0` must not be linked to C3's single-fibre concern | C4 point 7 rewritten: states only that PIII(D₈) has no free parameters; notes `P` is the parameter space and that the isomonodromic time still gives a one-dimensional deformation; "whether object A lies in a deformation" kept as a separate open question |
| Quadratic-cover route to the strong Riemann–Hilbert condition | added as a possible approach only, labelled **CONJECTURED**, carrying no weight |
| C2 should lead with the C1-independent ground | done — C2 now opens with `γ = 1 − θ₀ − θ_t = 1` from published sources alone; C1 follows as labelled independent corroboration |
| §7.1 should be recorded, not re-argued | C5 rewritten: item 1 refuted, "complete explanation" withdrawn, items 2–4 stated not to depend on apparency **with their correctness not re-examined**; the endorsement words *survive*/*stand*/*unaffected* removed |
| Deposit-day citation re-fetch | checklist added to the notice, four citations, **deliberately not executed now** |

Claims `R1-56`–`R1-60`, all `self`.

Corpus: **203 claims** — INSPECTED 74, PROVEN 68, STRUCTURAL 37, VERIFIED 22,
CONJECTURED 2. Review: 49 `self`, 11 `cold`, none lacking a `review_note`.
Rule 1(a) invariant holds. HEAD `08aa0e2`, unchanged.

### The third open question, as requested

Reproduced verbatim from the R8 section above:

> 3. **Optional sharpenings to the email** (§2.9 → §2.9(ii); "your paper" → "the
>    *Studies* paper") were identified but **not applied**, so the draft comes
>    back with exactly the defect fixed and no editorial drift.

In full: both are in `AUTHOR-REQUEST-WONGLI.md` §3 under "Two optional remarks,
not applied". Neither is a defect.

1. Your draft says "The DLMF (§2.9)". The subsection that actually cites
   Wong–Li, and that states the bounded-coefficient restriction motivating the
   request, is **§2.9(ii)**.
2. Your draft says the exponent may "already appear in your paper". Since Wong
   and Li wrote two papers with nearly the same title, **"the *Studies* paper"**
   removes the last trace of ambiguity — though quoting the DOI, which I did
   add, already handles it.

I did not apply either, on the principle that a draft sent back for a title
check should return with the title fixed and nothing else changed.

---

# R11 — operator review #8

All four rulings applied, plus the three housekeeping items. The object-B cold
read you authorised returned, and its findings were adopted claim by claim.

## The headline

**Objects B and C turned out to be the same object.** Under `z ↦ 1/x` their
trace-free normal forms are identically equal — not similar, equal — and the
inversion carries B's singular points `(−1±i√11)/2` exactly onto the companion's
`(−1±i√11)/6`. That `/2` vs `/6` difference had been sitting in the record as an
unexplained discrepancy; it was the inversion all along.

## Your question, answered

You asked whether the twist that makes B match System C takes B into the class
van der Put–Saito classify. **It does not — and B does not need it.**

The twist alters the trace by `−dlog A ≠ 0`, and p. 2634 requires `trace 0`, so
it genuinely leaves the classified class. But the pullback's `2/x` term
contributes nothing to the normal potential, so **inversion alone** reaches B's
trace-free normal form, and that is where the row is read. The twist only
converts that form into the companion's *printed* scalar operator — a feature of
presentation, not of classification.

So row B stands, and the phrase "up to inversion and twist" was both unnecessary
and inaccurate. It has been removed, and the exact normal-form identity now
appears under the C4 table in its place.

## What I corrected while adopting

Two of CT-S14's six task answers needed work, which is why the claim-by-claim
rule exists:

- It called the integer-difference points **"apparent"**. The substance — *not
  ordinary* — is right and adopted. The word is wrong, and contradicts our own
  C1: `residue(P) = 1` with `Q` at most a simple pole forces a log term, so those
  points are non-apparent. CT-S14 was isolated from C1 by design, so this is a
  defect in adoption, not in the reviewer.
- Its task 4 is correct but phrased as though the row were at risk; its own task
  5 says otherwise. Adopted with the qualification above.

Also worth flagging: my own verification script reported `False` on a root
comparison whose two sides are visibly identical — a SymPy artefact on
unevaluated radicals. Taken at face value it would have read as a refutation of
the central result. An elementwise check confirms the match.

## A defect in my own tooling, reported openly

My R11 append script deduplicated by `claim_id` and **silently dropped** three of
eleven claims whose IDs had been reused from R10 — and those three carried the
central result. It exited zero. I caught it only because it printed a count.

This shows the R9 duplicate-ID fix was incomplete: the invariant catches
duplicates after the fact, but the append path could still lose data quietly. The
replacement aborts on collision. Recorded as `R1-85` rather than quietly fixed,
since the record should show it.

## Where the notice stands

The three gates were already closed; the two object-B gaps are now cleared by an
independent cold read. The dependency audit stands at **44 of 47 cleared**, with
the remaining three (`CT-S9-PVPARAMS-C014`, `R1-56`, `R1-57`) shown in the
notice's support list as `self`, deferred by your decision — `R1-57` is
CONJECTURED and carries no weight.

**The companion v1.3 notice now needs only the deposit-day citation pass.**
Nothing has been deposited, committed, or submitted; HEAD is unchanged at
`08aa0e2`.

Channel Theory v1.7 still waits on Wong–Li. The reprint request is written and
ready; finding the address and sending it remain yours.

## Open questions for you

1. **Do you want row C merged into row B in the C4 table?** They are now known to
   be the same object in different presentations. I have kept them as separate
   rows, because the notice's purpose is to say that distinct *names* were being
   conflated, and collapsing them would undercut that. But the table could
   instead carry one row with both presentations noted.
2. **Does the B–C identity change anything on the Painlevé side?** C3 says System
   C is a single fibre with no deformation written down. If B and C are the same
   object, then whatever deformation would settle C settles B too — which may
   make the open question easier to pose than it looked.
3. **`R1-56` and `CT-S9-PVPARAMS-C014` remain `self`.** Deferred by your ruling
   and marked as such. Say the word if you would rather they were cold-read
   before deposit rather than after.

---

# R12-R13 - operator review #9

All five rulings applied. Both cold reads have now returned and been adopted
claim by claim. **The notice needs only the deposit-day citation pass.**

## Your wording ruling was right, and it caught a real slip

"B and C are the same object" was too strong for a notice about loose identity
claims. What was shown is identical trace-free normal forms under `z -> 1/x`,
which is **projective equivalence** - change of variable plus a rank-1 gauge. The
printed operators differ by the trace-altering twist, so they are not the same
operator. Corrected in the notice and in the claim text.

Your reframing is in: the three names form **two classes**, A and `{B, C}`, and
the conflation C4 corrects is between A and the `{B,C}` class - which sharpens
C4 rather than diluting it. The deformation-transport observation and the
`t = -+2i sqrt(33)/9` consistency check are recorded as a **future problem**,
CONJECTURED, not as results.

## Load-bearing test

- **`R1-56`: load-bearing.** C4 point 7 exists only to state it. Sent.
- **`CT-S9-PVPARAMS-C014`: corroborating only.** The notice asserts *openness*,
  so a later positive result would not falsify it, and C3's fixed-time sentence
  rests on the separately cold affine computation.
- **`R1-57`: corroborating only**, CONJECTURED on the face of the notice.

Both candidates travelled in one packet as you directed. Verdicts: **CORRECT WITH
WORDING CHANGE** and **CORRECT**. The reader also found a sentence on p. 2635 -
*"We will also describe the corresponding one-dimensional families of
differential modules `M(t)`"* - which supports point 7 **directly** instead of by
inference. That is a better footing than the claim had before.

Dependency audit: **46 of 47 cleared**. The single gap is `R1-57`, CONJECTURED.

## The OCR finding - worth your attention

CT-S15 was given page images and **ran OCR on them**. Two transcriptions were
wrong, and one was on a load-bearing hypothesis:

- Jimbo `(3.1)`'s constant matrix is `diag(1,0)`; it reported `(1/2)sigma_3`.
- `(A1)_PV` reads `theta_0, theta_t not in Z`; it added `theta_inf`.

Neither reached the notice - C2's `(A1)` line and dictionary were verified
earlier by direct reading and are correct - but this is the Gautschi (2.8)
near-miss recurring **one review after** that lesson went into P0. Supplying page
images does not enforce the rule if the reader converts them back into text.

P0 now says: a load-bearing statement is read by **looking at the rendered
page**; OCR is a text layer and does not satisfy the rule; an agent that cannot
view an image must **halt and report that**. Packets must state the halt
condition, since listing image files plainly does not convey it.

I also caught myself naming CT-S15 claim_ids I had not verified existed, while
wiring the cleared claims into the dependency script. Route A already covered
them, so the link check would never have tested those ids. Removed rather than
patched.

## Where things stand

The companion v1.3 notice is complete: every supporting claim is `cold` or
INSPECTED except the one CONJECTURED item that carries no weight. **Only the
deposit-day citation pass remains, and the release is yours to make.** The
backup has been refreshed as you asked, with its hash in a sidecar file.

Channel Theory v1.7 still waits on Wong-Li; the reprint request is ready to send.

## Open questions

1. **Should the notice name the two rejected transcriptions, as it now does?** I
   put them in the methodology note on the grounds that a correction notice
   should show its own corrections. If you would rather that stayed in the audit
   trail and out of the deposited text, it is a clean deletion.
2. **`R1-57` remains the single dependency gap.** It is CONJECTURED and carries
   no weight, so I did not send it. Say the word if you want it dropped from the
   notice entirely instead.
