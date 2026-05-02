# Handoff — T37J-A1-CLOSED-FORM-PSLQ
**Date:** 2026-05-02
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~40 minutes
**Status:** COMPLETE

## What was accomplished
Tested whether the apparent rational a_1 values reported by 017c
admit (a) per-rep closed forms via PSLQ, and (b) a unifying
functional form f(Δ_b, A) across the 3 non-anomalous
representatives. Per-rep PSLQ at tol=1e−30 returns the rationals
−53/36 (V_quad), −89/36 (QL15), +31/4 (QL05) cleanly with HARD
HYGIENE (same relation reproduced at tol=1e−12). No unifying
f(Δ_b, A) in the tested 11-candidate functional family + 3 joint
PSLQ probes predicts all three a_1's to 1e−30. A 3-parameter
degree-1 polynomial interpolates the 3 measurements exactly (by
counting) but fails at QL09. The A=3 sub-family relation
(2A)²·a_1 = 4Δ_b − 9 holds for V_quad and QL15 but does not
extend to A=4 (predicts 23/64 vs measured 31/4 for QL05).

## Key numerical findings
* V_quad a_1 = −53/36 — PSLQ relation [−53, −36] at tol=1e−30,
  maxcoeff 1e15, residual ~1e−302; script t37j_runner.py.
* QL15 a_1 = −89/36 — PSLQ relation [89, 36] at tol=1e−30; same
  hygiene; script t37j_runner.py.
* QL05 a_1 = +31/4 — PSLQ relation [−31, 4] at tol=1e−30; same
  hygiene; script t37j_runner.py.
* No global f(Δ_b, A) found: best in tested family is
  Δ_b/(A·(A−1)) with max-residual 7.08 — fails 1e−30; script
  t37j_runner.py.
* Deg-1 polyfit a_1 = −259/12 + Δ_b/9 + 64A/9 fits the 3
  non-anomalous reps exactly (interpolation); QL09 prediction
  251/36 ≠ measured 0; script t37j_runner.py.
* A=3 sub-family relation (2A)²·a_1 = 4Δ_b − 9 holds at 8e−49
  residual for V_quad and QL15; fails for QL05 (residual 473);
  script t37j_runner.py.

## Judgment calls made
* Phase B basis: the prompt specified a 12-atom basis containing
  {1/36, 1/4, 1/9, Δ_b, Δ_b/(2A)², (Δ_b−1)/(2A)², …, 1/(2A)²}.
  An initial run with that basis returned trivial atomic identities
  (e.g., 1 + Δ_b/(4A) − 3/(2A)² = 0 at fixed (Δ_b, A)) before
  targeting a_1, because PSLQ found those rank-deficient
  dependencies first. The basis was reduced to the minimal
  [1, a_1] for the per-rep rational verification step. Structural
  Δ_b/A involvement was kept fully in Phase C. Documented in the
  certificate §2 footnote.
* Verdict label: the deg-1 polyfit technically yields a single
  closed-form expression in (Δ_b, A) matching all 3 non-anomalous
  reps to ≥30 digits, which would qualify as
  T37J_UNIFYING_CLOSED_FORM_FOUND under a strict reading of §C.5.
  However the fit is degenerate by counting (3 points, 3
  parameters → exact by construction), so it is recorded as a
  curiosity in §3.4 of the certificate and the verdict was kept
  at T37J_RATIONAL_PER_REP_ONLY. The polyfit also fails at QL09,
  ruling out T37J_UNIFYING_RELATION_FOUND_INCLUDING_QL09.

## Anomalies and open questions
* The deg-1 polyfit coefficients reconstruct as small-denominator
  rationals (c0 = −259/12, c1 = 1/9, c2 = 64/9). Is this a
  hint of a real linear-in-(Δ_b, A) structural law, or accidental
  rationality at the 3-data-point interpolation limit? Only a
  4th non-anomalous rep with (A, Δ_b) outside {(3,−11),(3,−20),(4,8)}
  can falsify or strengthen it.
* The A=3 sub-family relation (2A)²·a_1 = 4Δ_b − 9 fits two
  measurements at one A value. A 3rd A=3 rep with Δ_b ∉ {−11, −20}
  is the minimum to elevate from "2-point fit" to "sub-family
  closed form". Note the structural appeal: (2A)² = 36 at A=3 is
  the natural normalization scale of the polynomial Birkhoff
  correction at A=3. The factor 4 and the constant −9 invite a
  Birkhoff-classical-formula derivation attempt.
* QL09's a_1 = 0 boundary is NOT predicted by any tested closed
  form (best, sub-family, or polyfit). This strengthens the Q18
  interpretation that QL09 lives on a different analytic branch
  (sign(C) = −1) rather than as a vanishing locus of a global f.
* Joint PSLQ §C.2-search2 returned the trivial atomic identity
  Δ_b/(2A)²_V − Δ_b/(2A)²_QL15 − 2·Δ_b/(2A)²_QL05 = 0 (i.e.
  −11/36 + 20/36 − 16/64 = 0 with all a_1 coefficients zero).
  This is a numerical coincidence among the input (Δ_b, A) values,
  not a closed-form relation; PSLQ surfaced it before any a_1
  involving relation. Worth flagging since at maxcoeff=1e10 it
  was the dominant relation; if a future joint search at higher
  maxcoeff tries to elevate it, the coefficients-on-a_1's-are-zero
  property is the disqualifier.

## What would have been asked (if bidirectional)
* Should the polyfit deg-1 result with rational coefficients
  (c0=−259/12, c1=1/9, c2=64/9) be elevated as a candidate
  closed form despite being interpolation-degenerate? Or held
  as a curiosity until a 4th rep falsifies it?
* Is the A=3 sub-family form (2A)²·a_1 = 4Δ_b − 9 worth a
  prompt to extend the rep set with one more A=3 rep at a fresh
  Δ_b? (Cheap: an additional Conte-Musette PCF at (alpha=3,
  beta=*, …) with novel Δ_b would do it.)

## Recommended next step
Compose a follow-on prompt **T37J-EXTEND-A3-REPS** that adds
1–2 new A=3 representatives (varying β, δ, ε at α=3) to the
017c-style a_1 measurement, then re-runs the per-rep PSLQ +
sub-family fit. If (2A)²·a_1 = 4Δ_b − 9 holds at a 3rd A=3 rep,
the relation graduates from "2-point fit" to "sub-family closed
form" and feeds picture v1.11 with a real structural axiom.
Independently of T37J-EXTEND-A3-REPS, T37J's per-rep rationals
are AEAL-eligible candidates pending Claude review.

## Files committed
* t37j_runner.py
* a_1_pslq_per_rep.json
* a_1_unifying_relation_search.json
* a_1_closed_form_certificate.md
* rubber_duck_critique.md
* verdict.md
* halt_log.json (empty / no halts)
* discrepancy_log.json (empty)
* unexpected_finds.json (empty)
* claims.jsonl (18 entries)
* runner.stdout.log
* handoff.md (this file)

## AEAL claim count
18 entries written to claims.jsonl this session.
