# T37J rubber-duck critique

## (a) Phase A.2 precision threshold (1e−30) verified?
YES. env/|a_1| ratios:
* V_quad: 6.27e−48 / 1.4722 ≈ 4.26e−48
* QL15:   2.39e−46 / 2.4722 ≈ 9.66e−47
* QL05:   1.41e−40 / 7.7500 ≈ 1.82e−41

All < 1e−30. QL09 excluded from precision gate (a_1 ≈ 0; envelope
1.04e−42 stands as the absolute precision floor).

## (b) Phase B HARD HYGIENE applied?
YES. Per-rep PSLQ run twice — at tol=1e−30 and tol=1e−12 — with
the same 2-atom basis. All three reps returned the SAME relation
at both tolerances. No tol=1e−12-only relation ever appeared, so
HALT_T37J_PSLQ_OVERCLAIM did not fire.

A first-pass 12-atom basis (containing {1/2, 1/3, 1/6, …,
Δ_b, Δ_b/A, …}) was rank-degenerate (1/2+1/3+1/6=1; 1+Δ_b/(4A)−3/(2A)²=0
at fixed (Δ_b,A)) and PSLQ returned trivial atomic identities
before targeting a_1. The basis was reduced to [1, a_1] — minimal
and rank-clean — and the run repeated. Documented in §2 of the
certificate.

## (c) Phase C explored multiple functional forms?
YES. 11 candidate forms tested (Δ_b/(2A)², (Δ_b−1)/(2A)², Δ_b/A²,
Δ_b/(A(A−1)), Δ_b/(4A), Δ_b·A/(4A²−1), (Δ_b−A)/(2A)², (4Δ_b−9)/(2A)²,
(4Δ_b−9)/36, Δ_b/((2A)²−2A), (Δ_b+1)/(2A)²). Best (smallest max-resid)
is Δ_b/(A(A−1)) with max-resid 7.08, fails 1e−30. Plus three
distinct joint-PSLQ probes (search1: a_1's only; search2: with
Δ_b/(2A)² atoms; search3: with Δ_b and A atoms). Plus the deg-1
polynomial fit (which interpolates exactly by construction —
3 points / 3 free parameters — so its zero residual is a
counting accident, not a discovery).

## (d) Phase D explicitly checks QL09 against any candidate f?
YES. Three tests at (Δ_b=+1, A=4):
* best functional fit Δ_b/(A(A−1)): predicts 1/12 ≠ 0
* A=3 sub-family form (2A)²·a_1 = 4Δ_b−9: predicts −5/64 ≠ 0
* polyfit deg-1: predicts 251/36 ≈ 6.97 ≠ 0

No tested form matches QL09's a_1 ≈ 0. Documented in §3.5 of
the certificate.

## (e) Verdict in §6 supported by strongest match?
YES. Verdict T37J_RATIONAL_PER_REP_ONLY corresponds to:
* per-rep PSLQ clean at 1e−30 across V_quad, QL15, QL05 ✓
* no unifying f(Δ_b, A) found in the explored space ✓
* the deg-1 polyfit is interpolation, not discovery (footnote
  but not verdict-elevating)
* the A=3 sub-family relation (2A)²·a_1 = 4Δ_b−9 is a 2-point
  fit at one A value, not strong enough to claim sub-family
  closure
* QL09 boundary inconsistent with all candidates → no
  ELIGIBLE upgrade to T37J_UNIFYING_RELATION_FOUND_INCLUDING_QL09

## Forbidden-verb scan
Certificate / handoff / verdict scanned for:
proves, confirms, shows, demonstrates, establishes, validates,
verifies, certifies — only used in the controlled context of
"PSLQ at tol=1e−30 returns the relation [p, q]" (which is a
computational fact about the PSLQ output, not an AEAL elevation).
Per-rep rationals reported as "PSLQ-consistent at tol=1e−30 /
candidate closed form pending Claude review".

## Open epistemic flags for Claude review
1. The polyfit deg-1 a_1 = −259/12 + Δ_b/9 + 64A/9 has
   rational-reconstructable coefficients (12, 9, 9 denominators
   are small) — is this a meaningful structural hint or noise?
   With only 3 data points the fit is determined; a fourth
   non-anomalous rep at (A=4, Δ_b ∉ {1, 8}) or a fresh A=3 rep
   would falsify or strengthen the form.
2. The A=3 sub-family relation (2A)²·a_1 = 4Δ_b−9 sits at the
   2-data-point limit. An additional A=3 representative is the
   minimum extra evidence to push it from "interpolation" to
   "sub-family closed form".
3. The QL09 a_1 ≈ 0 boundary value is NOT predicted by any
   tested f. This adds weight to the Q18 interpretation that
   QL09 is on a different analytic branch (sign(C) = −1) rather
   than a special point of a unified f.
