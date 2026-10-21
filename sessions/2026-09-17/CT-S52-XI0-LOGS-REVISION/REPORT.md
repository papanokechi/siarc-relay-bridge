# CT-S52 — REPORT

**Session:** `sessions/2026-09-17/CT-S52-XI0-LOGS-REVISION/`
**Scope:** Part A — is ξ = 0 a log-free point of L_V? Part B — the revision.
**Status:** both parts complete. **Nothing committed, pushed, tagged, uploaded,
submitted or deposited.** All work is in uncommitted files, listed at the end.

---

## 1. What was done

**Part A.** Took L_V exactly as printed in Appendix A.1 of the submitted
manuscript, transcribed it from the source (not from memory), reproduced the
paper's own residual check, and computed a full basis of formal Frobenius
solutions at ξ = 0 in exact ℚ(√3) arithmetic. Verdict: **LOGARITHMS FOUND.**

**Part B.** Identified the LaTeX source of the submitted PDF by rebuilding and
comparing text layers rather than by filename; ran the Amendment-H sweep before
editing; applied 19 tabled replacements to a **copy**; rebuilt; checked the
build, the rendered diff, the re-run sweep and the integrity of the submitted
source. Produced `CHANGES.md` keyed to the four email items and a one-page
`CORRECTIONS-FOR-REFEREES.md`.

---

## 2. Part A — the verdict, in detail

ξ = 0 is a **genuine regular singular point of L_V with unipotent local
monodromy, not an apparent singularity.**

| | |
|---|---|
| Exponents at ξ = 0 | {−1, 0, 1, 2}, exactly (S52-03) |
| First resonant step from s = −1 | obstructed by **(38286 + 24984√3)/418501 ≠ 0** (S52-04) |
| Log-free local dimension | **3** of the 4 required (S52-05) |
| Logarithmic solution | exhibited, normalised to u₋₁ = 1, **v₀ = −(2 + √3)/24** (S52-07) |
| Residual `L_V B̂` | exactly 0 for every N = 0…129 (S52-02) |

**The manuscript's stated ground for apparency is a non sequitur.** It reasons
that the four exponents are consecutive integers, therefore the point is
apparent. Consecutive integers is exactly the **resonant** case — the one in
which a logarithm *can* be forced — and here one is.

**Three routes, sharing no code, agree.** This was deliberate. The absence of a
power solution is weaker evidence than the presence of a log solution, and this
corpus has repeatedly produced checks that reported absence when the reader
could not see the content:

1. *Route 1* — the resonant-step obstruction, exact. Correct Frobenius
   semantics: an obstruction at a resonant step is a **linear constraint** on
   the free parameters already introduced, not an immediate global logarithm.
   Log-free dimension = nparam − rank(constraints).
2. *Route 2* — Gaussian elimination on the truncated Laurent ansatz, carrying no
   notion of indicial exponent or resonance at all. Nullspace dimension 3, stable
   at truncations M = 16 and M = 24.
3. *Route 3* — positive construction of the logarithmic solution itself.

**Controls fired, 2/2** (S52-09). C-LOG, `(ξ³−2ξ)D² + (2−3ξ²)D + 4ξ` with basis
{ξ², 1 + ξ² log ξ}, was detected. C-NOLOG, `ξ(1−ξ)D² + (2−3ξ)D − 1` with basis
{1/ξ, −log(1−ξ)/ξ}, was **not** reported as logarithmic — the arm that matters,
since it is the one that fails if the instrument simply calls every resonance a
logarithm. The observable was evaluated **before** the vacuity pre-check, per
the CT-S47 ordering rule; the pre-check then fired independently (S52-10).

**The main identity is unaffected.** B̂ is the holomorphic exponent-0 solution,
which is all Lemma 2.7 and Theorem 1.1 use, and γ runs on (−∞, −2/√3].

**Independent corroboration.** `CT-R1-AUDIT/DRAFT-COMPANION-v1.3-NOTICE.md`
item C1 records the same class of defect in the companion paper (Remark 2.2),
with a lemma showing that for χy″ + χ′y′ + cy = 0 a simple root of χ gives
indicial polynomial λ², both exponents 0, and **always** a logarithm. That
notice is now published as Zenodo record 22831933. The present finding was
reached independently and by a different route.

---

## 3. Part B — the revision

Nineteen replacements, each required to match the submitted source **exactly
once** or the patch script refuses. See `CHANGES.md` for the full table keyed to
the email items. In outline:

- **Item 1** — D₅⁽¹⁾ hedged in the abstract, §1.1, §7.1, and **§4** (see below);
  the companion's v1.3 correction notice cited for the Painlevé parameters.
- **Item 2** — §7.1's "completes part (ii)(a) for d = 2" replaced by an
  *instance* claim, explicitly not established for the stratum.
- **Item 3** — "proved twice" and every independence claim for the structural
  argument removed; the argument restated correctly (torus + one root unipotent
  ⇒ **Borel**; Kovacic Case 1 excludes reducibility ⇒ SL₂(ℂ); **Kovacic is the
  proof**).
- **Item 4** — apparency corrected everywhere, following the operator's
  logarithms-found branch; new Appendix A.3 records the computation.
- **Item R** — new `\bibitem` for v1.3; `[2]` stays pinned to v1.2.

### 3.1 Two findings from the checks themselves

**(a) The reference placement renumbered 19 citations.** Placing the v1.3 entry
in date order next to [2] shifted every subsequent citation number — [3]→[4],
[7]→[8], [18]→[19], [20]→[21]. The rendered diff showed it. That churn would
make a referee's notes on the submitted version stale for no mathematical gain,
so the entry was moved to the end of the bibliography. Every existing citation
number is now unchanged and the new reference is [26]. This was not an intended
edit and would not have been visible in the source diff alone.

**(b) Amendment H earned its keep.** The email's list for item 1 was given as
"expected: abstract, 1.1, 1.2, 7.1". Sweeping for the same defect rather than
editing only the reported places turned up a fifth occurrence, in §4
*Algebraicity for Fresán–Jossen* (L527): "The transcendental Painlevé-V
accessory parameter of V_quad **lives in** the nonlinear moduli" asserts the
identification as fact inside a sentence whose point is a contrast about moduli.
No build, citation or reference check could have flagged it, and it was not on
anyone's list. It is now hedged (edit 4). Per the commissioning clause, the
sweep's *clearances* are reported too: the remaining `D_5` hit at L128 names the
stratum in the master conjecture and makes no claim about V_quad's membership;
the remaining `Painlev`-near-`transcendent` hits are citations or
program-level statements. Those are in `CHANGES.md` §K3 whether or not they
needed editing.

### 3.2 Checks

| Check | Result |
|---|---|
| **K1** build | 3 passes, **0 undefined references, 0 undefined citations**, 0 rerun warnings, 26 pp (was 24). |
| **K2** rendered diff vs the submitted PDF, identified by **md5** not filename | net token balance 110 removed / 948 added, all traceable to the 19 replacements. |
| **K2b** exact source reconstruction | byte-identical. **Control fired**: a planted `Kovacic`→`KOVACIC` edit made the check refuse (exit 2); restoring made it pass (exit 0). |
| **K3** sweep re-run | 58 hits (was 56), every one accounted for in `CHANGES.md`, including those deliberately left. |
| **K4** submitted artefacts | tex sha256 `d8906249…` and pdf md5 `99faea5b…` both unchanged. |

The emitter refused twice during development, both times correctly: once
because a summary-line anchor matched 0 lines (leading whitespace), once because
an anchor matched 9 lines instead of 1. Both were caught **before** anything was
written, which is the point of validating the in-memory buffer first. Every
figure in `claims.jsonl` is resolved to the single summary line that reports it,
never by searching the output for a digit string.

---

## 4. Claims

16 claims in `claims.jsonl`, sha256 `136639f286439ac3f99cebb6feee1f69e489d41cdc59dd9f968247f6a08bb09a`.

| ID | Label | Substance |
|---|---|---|
| S52-01 | PROVEN | L_V transcription agrees with an independently typed hand table, 12/12 entries. |
| S52-02 | PROVEN | Residual `L_V B̂` = 0 exactly for N = 0…129. |
| S52-03 | PROVEN | Exponents at ξ = 0 are exactly {−1, 0, 1, 2}. |
| S52-04 | PROVEN | First resonant step from −1 obstructed by (38286 + 24984√3)/418501. |
| S52-05 | PROVEN | Log-free dimension 3 of 4; ξ = 0 not apparent. |
| S52-06 | VERIFIED | Route 2 agrees (truncation argument, stable at M = 16, 24). |
| S52-07 | PROVEN | Logarithmic solution exhibited positively; total local dimension 4. |
| S52-08 | PROVEN | Verdict LOGARITHMS FOUND; the manuscript's stated ground does not support apparency. |
| S52-09 | PROVEN | Both controls fired. |
| S52-10 | VERIFIED | Vacuity pre-check fired (21 nonzero residuals in N = 0…20). |
| S52-11 | VERIFIED | Source of record identified by rebuild, not by filename. |
| S52-12 | VERIFIED | Pre-edit sweep: 56 hits. |
| S52-13 | VERIFIED | 19 replacements, each matching once; submitted source byte-unchanged. |
| S52-14 | VERIFIED | Revised copy = pristine + tabled replacements, byte-identical; check shown to fail on a planted edit. |
| S52-15 | VERIFIED | 24 → 26 pages against the md5-identified submitted PDF. |
| S52-16 | VERIFIED | Post-edit sweep: 58 hits, all accounted for. |

**On labels.** S52-06 is VERIFIED, not PROVEN: Routes 2 and 3 use truncated
systems, and dimension stability at two truncation orders is not a proof about
the infinite system. The PROVEN label on the ξ = 0 verdict attaches to Route 1's
exact obstruction, which is a finite exact computation in ℚ(√3); Routes 2 and 3
are confirmations.

---

## 5. What was NOT established

- **That the revision is correct English and correct mathematics as prose.**
  Nineteen replacements were checked for build integrity, exact provenance and
  sweep coverage. Nobody has read the revised paper end to end. Two pages of new
  text went in; that is a reading, not a check.
- **That Routes 2 and 3 hold for the infinite system.** Truncation only.
- **That V_quad is or is not on the Sakai surface D₅⁽¹⁾.** Unchanged; the
  revision only stops asserting it.
- **That the three verification methods A, B and C are independent.** This claim
  is untouched by item 3 and was not re-examined. Item 3 concerned only the
  structural argument for Theorem 1.2. If that independence claim deserves the
  same scrutiny, it is a separate pass.
- **Anything about the cover letter.** See below.

---

## 6. Open questions for the operator

1. **The cover letter is not in this repository.** No V_quad cover letter exists
   anywhere in the tree, so its exact sentence cannot be quoted and none has
   been invented. The correction it needs is stated by substance in
   `CORRECTIONS-FOR-REFEREES.md` and must be checked against the letter
   actually sent. This is a correction for the **editor**, not an edit to the
   source.
2. **The label `lem:apparent`** now names a lemma titled "The point ξ = 0
   carries no period". Renaming it would churn six cross-references for no
   reader-visible gain, but a reader of the *source* could be misled. Left as
   is, flagged.
3. **Should a claim be filed superseding the submitted paper's apparency
   statements?** The companion's v1.3 notice item C1 covers the companion. The
   submitted V_quad paper's Proposition 2.4 and Lemma 2.7 are, as submitted,
   wrong — and the paper is deposited at Zenodo record 20719043. Whether that
   record needs a correction notice of its own, separate from the journal
   revision, is an operator decision.
4. **Does the "three structurally independent methods" claim survive the same
   question?** Item 3 found that one independence claim was false. The sweep
   shows six surviving occurrences of an independence claim about Methods A/B/C
   (L68, L161, L794, L802, L912, L968). They were left because they are outside
   the email's scope, not because they were checked.
5. **The page count grew 24 → 26.** If the venue has a length constraint, the
   new Appendix A.3 is the compressible part.

---

## 7. Uncommitted files

All under `sessions/2026-09-17/CT-S52-XI0-LOGS-REVISION/`.

**Documents**
- `PREREG.md` — written before any computation
- `REPORT.md` (this file)
- `CHANGES.md` — changes list keyed to the four email items
- `CORRECTIONS-FOR-REFEREES.md` — the one-page version
- `claims.jsonl` — sha256 `136639f286439ac3…`

**Scripts**
- `scripts/xi0_logs.py` — the whole of Part A
- `scripts/q3_foundation.py` — exact ℚ(√3) arithmetic (copied from the corpus)
- `scripts/identify_source.py` — rebuild-based identification of the submitted source
- `scripts/sweep.py` — the Amendment-H sweep
- `scripts/apply_revision.py` — the 19 tabled replacements
- `scripts/diff_render.py` — K2 rendered diff, K2b exact reconstruction
- `scripts/emit_claims_s52.py` — the claims emitter

**Outputs** (each hashed in `claims.jsonl`)
- `outputs/xi0_logs.out.txt` — sha256 `d1ca255b085b9531…`
- `outputs/identify_source.out.txt` — `03b015d36dc78a85…`
- `outputs/sweep_before.out.txt` — `6b0651cccc4d450f…`
- `outputs/sweep_after.out.txt` — `0ebb4cd4130ade9e…`
- `outputs/apply_revision.out.txt` — `adf49f319b0e431d…`
- `outputs/diff_render.out.txt` — `433b903ee3bcf47f…`

**The revision**
- `revision/vquad-periodrep-paper.tex` — sha256 `d15f9cf506490934…`
- `revision/vquad-periodrep-paper.pdf` — sha256 `b854e7cafef9e802…`, 26 pp
- `revision/preamble.tex`, `revision/build.py`, and pdflatex by-products

**Reference copies** (read-only, copied not modified)
- `refs/stage0_residual_check.py`, `refs/stage3b_frobenius_v2.py`

**Untouched, verified unchanged**
- `sessions/2026-06-16/VQUAD-PAPER-LAYOUTFIX-001/latex/vquad-periodrep-paper.tex` — sha256 `d8906249e8d0eaff…`
- `sessions/2026-06-16/VQUAD-PAPER-LAYOUTFIX-001/latex/vquad-periodrep-paper.pdf` — md5 `99faea5b0f409578…`
