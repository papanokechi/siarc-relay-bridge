# Handoff — T37L-A1ZERO-CATALOGUE-SCAN
**Date:** 2026-05-03
**Agent:** GitHub Copilot (VS Code, Claude Opus 4.7)
**Session duration:** ~25 minutes
**Status:** COMPLETE

## What was accomplished

017L was asked to populate sub-stratum (iii) of G20 (the d=2 PCFs
with a₁ = 0). The bracket form B(α, β, γ) := α/16 + γ − β²/(4α)
recorded in 017f Find #1 was independently re-derived via sympy from
the recurrence's k=1 step, the algebraic locus B = 0 was solved
(2-dimensional quadric surface; γ = (4β² − α²)/(16α)), and 6
algebraically-distinct integer-lattice candidates were generated and
run through the T37F Birkhoff recurrence at dps=300, N=2000. All 6
candidates exhibit a₁ = 0 exactly at the recurrence level and to
fit-level |a₁| ≤ 10⁻⁴⁹ with envelope half-range ≤ 10⁻⁴⁰. Verdict:
**T37L_THIRD_STRATUM_HIGHER_DIM**.

## Key numerical findings

* B(QL09) = 0 exactly; B at the 3 other T35 reps (V_quad, QL15,
  QL05) lies in the range 1.10 to 1.94 in absolute value — clean
  separation. (script: t37L_runner.py, dps=300)
* Algebraic locus B = 0 ⇔ α² + 16αγ − 4β² = 0 — a 2-dimensional
  quadric in (α, β, γ)-space. (script: t37L_runner.py, sympy)
* Integer lattice in (α ≤ 10, |β| ≤ 20): 21 points; QL09 (2, 3, 1)
  is one of them. (script: t37L_runner.py)
* 6 candidates Q1–Q6 with (α, β) ∈ {(2,3), (2,1), (2,5), (4,2),
  (4,6), (8,4)} — all yield recurrence a₁ = 0 exactly and fit-level
  |a₁| in 10⁻⁴⁹ to 10⁻⁵⁶ across a 9-config K_lead × W₁ envelope grid.
  (script: t37L_runner.py, dps=300, N=2000, K_lead=25, W₁=(400,1900))

## Judgment calls made

1. **(δ, ε) assigned canonically (1, 0) for new candidates** instead
   of running a Conte–Musette family-extension to derive natural
   (A_pred, Δ_b) per candidate. Justification: at k=1 the recurrence
   has no a₍ₖ₋₂₎ or a₍ₖ₋₃₎ contribution, so (δ, ε) are inert at the
   a₁ rung; the structural finding holds regardless of (δ, ε)
   choice. The auxiliary invariants are recommended as an
   operator-side follow-up.

2. **K_cand = 6 instead of 5.** Added a QL09-baseline reproduction
   row (Q1) on top of 5 distinct algebraic candidates. The baseline
   reproduces 017f's a₁ ≈ 10⁻⁴⁹ at this prompt's precision, sanity-
   checking the recurrence implementation.

3. **Verdict mapping HIGHER_DIM (not 1PARAMETER).** The locus B = 0
   is genuinely 2-dimensional; calling sub-stratum (iii) "1-parameter"
   would understate. With (δ, ε) cylinder factor, the full
   parameter-space sub-stratum is 4-dim, but reported HIGHER_DIM at
   the level of (α, β, γ) per §6's verdict ladder.

## Anomalies and open questions

**This is the most important section. Reviewer please read carefully.**

1. **(δ, ε) are inert at a₁ for d=2 PCFs (Unexpected Find #1).**
   Independently of any (α, β, γ) choice on B = 0, varying δ, ε
   does not perturb a₁. This is a structural feature of the d=2
   recurrence (k=1 step has only the U_{k−1} contribution) and lifts
   the a₁ = 0 sub-stratum from a 2-d surface to a 4-d cylinder. This
   may be obvious but is worth recording — it changes the dimension
   count Picture v1.11 should report.

2. **The 21 integer lattice points have not been Painlevé-classified.**
   Each has its own (A_pred, Δ_b, side, c0, ρ) signature once (δ, ε)
   are fixed. T37L did not compute these. Without that data, we
   cannot say which lattice points correspond to "natural"
   Painlevé-Lax PCFs vs. degenerate / artificial ones. The
   lattice-vs-natural distinction is an operator-side question.

3. **a₂ at the new candidates was not extracted.** Per 017f, QL09
   has a₂ = −10 and a₃ = −70/3 (clean rationals). The new candidates
   may exhibit similarly-clean a₂ rationals OR not — testing this
   would refine sub-stratum (iii) further (e.g., is there a
   *secondary* algebraic identity governing a₂?). Out of T37L scope
   per "ONE quantity per candidate".

4. **Connection to T37J A=3 sub-family relation.** T37J found
   (2A)² · a₁ = 4Δ_b − 9 fits {V_quad, QL15} but FAILS {QL05, QL09}.
   For QL09 the relation gives a₁ = (4·1 − 9)/16 = −5/16, but actual
   a₁ = 0 — confirming T37J's failure. The bracket B = 0 is the
   *correct* structural identity that QL09 satisfies and a₁=0
   reflects. T37J's relation was a coincidental fit on (V_quad,
   QL15) that does not generalize. Reviewer may want to record this.

5. **The bracket is c-independent.** Unlike at higher k where U_{k−2}
   carries a factor of c, U_{k−1}(1) = B contains no c. So a₁ = 0
   ⇔ B = 0 is genuinely basis-independent (017f's "third stratum
   confirmed" finding). T37L re-confirms by independent derivation.

## What would have been asked (if bidirectional)

1. "Should I run a Conte–Musette pass to compute (A_pred, Δ_b) for
   each of the 21 integer lattice points, or defer that to a
   dedicated follow-on prompt?" — defaulted to defer.

2. "Is the 4-dim cylinder lift (B = 0 in (α,β,γ) lifted to full
   (α,β,γ,δ,ε) space) the right way to record sub-stratum (iii) in
   Picture v1.11, or should the picture restrict to the 2-d quadric
   in (α,β,γ) projection?" — defaulted to record both.

3. "Should T37L attempt to extract a₂ at one or two of the new
   lattice points to check whether a *second* algebraic identity
   structures the sub-stratum further?" — defaulted to skip per
   "ONE quantity per candidate".

## Recommended next step

**T37M-A2-EXTRACTION-ON-LOCUS** (if the sub-stratum-(iii) finding
holds up to Claude review): for 2 or 3 of the new lattice points
(e.g. Q4 = (4, 2, 0, 1, 0) and Q5 = (4, 6, 2, 1, 0)), extract a₂ via
the same K_lead = 25 stage-1 fit and PSLQ-test it against small
rationals + simple polynomials in (α, β, γ, δ, ε). If a₂ is *also*
governed by a simple algebraic identity on the locus, sub-stratum
(iii) is structurally rich; if a₂ is generic across the locus, then
B = 0 is the only structural identity at d=2 and a₁ = 0 is its sole
manifestation.

Alternative: **T37N-CONTE-MUSETTE-ON-LATTICE** — run the upstream
Conte–Musette classifier on each of the 21 integer lattice points to
record (A_pred, Δ_b, side, c0, ρ) per point, populating the
sub-stratum (iii) catalogue with full Painlevé invariants.

## Files committed

* t37L_runner.py
* bracket_algebraic_solution.json
* catalogue_candidates.json
* candidates_a_1_numerical_confirmation.json
* third_stratum_certificate.md
* verdict.md
* handoff.md (this file)
* halt_log.json (empty: `{"halts": []}`)
* discrepancy_log.json (empty: `{"discrepancies": []}`)
* unexpected_finds.json (1 find: (δ, ε) inert at a₁)
* claims.jsonl (17 entries)
* rubber_duck_critique.md
* t37L_run.log
* t37L_stdout.log

## AEAL claim count

17 entries written to claims.jsonl this session (≥ 16 required by §3).

Breakdown:
* 1 entry: bracket form recovered + sympy-rederived
* 4 entries: B numerical evaluation per T35 rep (V_quad, QL15, QL05, QL09)
* 1 entry: algebraic locus classification (2-d quadric)
* 1 entry: integer lattice enumeration (21 points)
* 1 entry: candidate set (6 candidates)
* 6 entries: per-candidate a₁ confirmation
* 1 entry: sub-stratum classification + count summary
* 1 entry: Picture v1.11 amendment recommendation
* 1 entry: verdict label

## Picture v1.11 amendment recommendation (for Claude)

G20 sub-stratum (iii) at d=2 is consistent with being a
**2-dimensional algebraic sub-variety** of (α, β, γ)-space, defined
by α/16 + γ − β²/(4α) = 0 (equivalently α² + 16αγ − 4β² = 0).
Including (δ, ε) as inert directions lifts to a 4-dim cylinder.
QL09 is one integer-lattice point among infinitely many; T35's
4-rep catalogue intersects sub-stratum (iii) only at QL09 by
representative-choice, not by sub-stratum scarcity. Operator-side
family extension can populate the sub-stratum arbitrarily densely.

The bracket form is c-independent, hence basis-independent, hence
the "third stratum" interpretation of QL09 (017f) lifts to the
entire B = 0 locus.
