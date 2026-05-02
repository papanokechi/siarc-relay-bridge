# T37J — a_1 closed-form certificate

**Task:** T37J-A1-CLOSED-FORM-PSLQ
**Date:** 2026-05-02
**Convention:** PCF coefficients [a2, a1, a0]; a_n_lead = C·Γ(n)·ζ_*^(−n)
**Precision:** mpmath dps=300; PSLQ tol ∈ {1e−30, 1e−12}; maxcoeff ≤ 1e15
**Verdict:** T37J_RATIONAL_PER_REP_ONLY

---

## 1. Per-rep a_1 measurements (from 017c)

| rep    | Δ_b  | A | a_1 (017c median, ≥40 digits)               | envelope half-range | apparent rational |
|--------|------|---|---------------------------------------------|---------------------|-------------------|
| V_quad | −11  | 3 | −1.4722222222222222222222222222222222222… | 6.27e−48            | −53/36            |
| QL15   | −20  | 3 | −2.4722222222222222222222222222222222222… | 2.39e−46            | −89/36            |
| QL05   | +8   | 4 | +7.7499999999999999999999999999999999999… | 1.41e−40            | +31/4             |
| QL09   | +1   | 4 | −1.71e−57                                   | 1.04e−42            | 0 (Q18 anomaly)   |

Phase A.2 precision ratio env/|a_1| < 1e−30 holds for V_quad, QL15, QL05.

Phase A.3 continued-fraction reconstruction (q ≤ 1000) recovers each
apparent rational with |a_1 − p/q| at the 1e−49 level (V_quad, QL15)
and 1e−43 level (QL05) — well below the 1e−30 hygiene threshold.

---

## 2. Per-rep PSLQ verification (Phase B)

PSLQ on the minimal 2-atom basis [1, a_1] at mpmath dps=300:

| rep    | tol=1e−30 relation [c0, c1] | reading           | tol=1e−12 re-check | hygiene flag |
|--------|------------------------------|-------------------|---------------------|--------------|
| V_quad | [−53, −36]                   | a_1 = −53/36       | identical relation  | clean        |
| QL15   | [+89, +36]                   | a_1 = −89/36       | identical relation  | clean        |
| QL05   | [−31, +4]                    | a_1 = +31/4        | identical relation  | clean        |

The HARD HYGIENE check (Phase B.2) shows the same relation at the
looser tolerance — no precision-artefact overclaims. The relations
above are consistent with each rep's apparent rational at ≥30
digits; PSLQ does not contradict the continued-fraction reconstruction.

Note on basis choice: an earlier 12-atom basis containing
{1, 1/2, 1/3, 1/6, …} and {Δ_b, Δ_b/A, …} was rank-degenerate
(1/2 + 1/3 + 1/6 = 1; 1 + Δ_b/(4A) − 3/(2A)² = 0 at fixed (Δ_b,A))
and PSLQ locked onto trivial atomic identities before targeting a_1.
The 2-atom [1, a_1] basis is the minimal, rank-clean choice for the
per-rep rational verification step. Structural Δ_b / A involvement
is the job of Phase C.

---

## 3. Unifying-relation search (Phase C)

### C.2 Joint PSLQ probes across V_quad, QL15, QL05

* Search 1 — atoms {1, a_1_V, a_1_QL15, a_1_QL05}:
  PSLQ returns [1, −1, 1, 0], i.e. 1 − a_1_V + a_1_QL15 = 0,
  equivalently a_1_QL15 − a_1_V = −1. This is a numerical
  identity between two A=3 reps (their a_1's differ by exactly
  −1 because (4·(−20) − 9 − (4·(−11) − 9))/36 = −36/36 = −1).
  It is a consequence of the A=3 sub-family relation §3.4 below
  combined with the integer Δ_b values of V_quad and QL15.

* Search 2 — atoms {1, a_1's, Δ_b/(2A)² per rep}: PSLQ returns
  [0, 0, 0, 0, 1, −1, −2], i.e. an atomic identity among the
  three Δ_b/(2A)² values (−11/36 − (−20/36) − 2·(8/64) = 0)
  with all a_1 coefficients zero. NOT a closed-form relation.

* Search 3 — atoms {1, a_1's, Δ_b's, A's}: PSLQ returns
  [1, 0, 0, 0, 0, 0, 0, 0, 1, −1], i.e. 1 + A_QL15 − A_QL05 = 0
  with all a_1 coefficients zero. Trivially true since
  A_QL15 = 3, A_QL05 = 4. NOT a closed-form relation.

No joint linear PSLQ probe at maxcoeff ≤ 1e10 returns a
relation linking the a_1 values to a single Δ_b / A combination
across all 3 non-anomalous reps.

### C.3 Functional-form fit

Tested 11 candidate forms f(Δ_b, A); per-rep residual reported
as |a_1_rep − f(Δ_b_rep, A_rep)|. Best candidate:

* form: Δ_b / (A·(A−1))
* max_resid across {V_quad, QL15, QL05}: 7.0833…
* passes 1e−30: **NO**

No simple algebraic f(Δ_b, A) in the tested family predicts
all three non-anomalous a_1 values to 1e−30 precision.

### C.4 Polynomial fit a_1 = c0 + c1·Δ_b + c2·A (3 points, 3 unknowns)

Solving the linear system across V_quad, QL15, QL05 yields
exactly (rational reconstruction at q ≤ 2000):

  **c0 = −259/12,  c1 = 1/9,  c2 = 64/9**

i.e.  a_1 = −259/12 + Δ_b / 9 + 64·A / 9.

Per-rep residuals are 0 by construction (3 points / 3 free
parameters → interpolation, not discovery). The rational
coefficients are reconstructed exactly via continued fraction;
this is a notable curiosity but **not** a structural relation —
any 3 measurements of a function of (Δ_b, A) admit such a fit.

### C.5 QL09 boundary check (Phase D)

Tested candidate forms at QL09 (Δ_b = +1, A = 4); QL09's
measured a_1 is 0 to ~57 digits.

| candidate                            | predicted a_1 at QL09 | diff vs measured |
|--------------------------------------|-----------------------|------------------|
| best functional fit Δ_b/(A(A−1))     | 1/12 ≈ 0.0833         | 0.0833           |
| A=3 sub-family form (2A)²a_1=4Δ_b−9  | −5/64 ≈ −0.078125     | 0.078125         |
| polyfit deg-1 (§3.4)                 | 251/36 ≈ 6.972        | 6.972            |

**No** tested closed-form candidate is consistent with QL09's
a_1 ≈ 0 at 1e−30 precision. This is consistent with QL09 being
the Q18 anomaly stratum (sign(C) = −1) and not on the same
analytic branch as V_quad / QL15 / QL05.

### 3.4 A=3 sub-family relation (NOT global)

The relation **(2A)²·a_1 = 4·Δ_b − 9** holds exactly across
the two A=3 representatives:

* V_quad: 36·(−53/36) = −53; 4·(−11) − 9 = −53. residual ~8e−49.
* QL15:   36·(−89/36) = −89; 4·(−20) − 9 = −89. residual ~8e−49.

Extension to QL05 (A=4): predicts a_1 = (4·8 − 9)/64 = 23/64 ≈
0.359, vs measured 31/4 = 7.75. Residual 473 (full-magnitude).
The relation is consistent with two A=3 measurements but does
not extend to A=4. With only one A=3 free parameter (effectively
Δ_b at fixed A=3), two measurements determine a line; the
relation is not over-constrained on the A=3 branch.

Joint PSLQ on {1, a_1_V, a_1_QL15, Δ_b_V, Δ_b_QL15} (Phase C
sub-search) returns [1, −1, 1, 0, 0], confirming
a_1_QL15 = a_1_V − 1, which is a numerical consequence of the
sub-family relation evaluated at Δ_b = −11 and Δ_b = −20.

---

## 4. Picture v1.11 amendment recommendation

* **Per-rep rationals** {V_quad: −53/36, QL15: −89/36, QL05: +31/4}
  are PSLQ-clean at tol=1e−30. Suitable for AEAL-evidence elevation
  pending Claude review.

* **No global f(Δ_b, A)** in the simple algebraic family tested
  (11 forms in C.3 plus the full PSLQ joint sweep in C.2) predicts
  all three a_1's to 1e−30. The 3-point degree-1 polyfit
  a_1 = −259/12 + Δ_b/9 + 64A/9 fits by interpolation but fails
  at QL09 and is not a genuine closed form.

* **A=3 sub-family relation** (2A)²·a_1 = 4Δ_b − 9 is consistent
  with both A=3 measurements but is a 2-point fit; needs at
  least one more A=3 representative with Δ_b ∉ {−11, −20} to
  test as a genuine sub-family closed form.

* **G20** stays "closed via partition + per-rep rationals (a
  discrete catalogue)" rather than "closed via a single closed
  form across the family". Picture v1.11 records the catalogue.

* **Open question for Claude**: is there a deeper PCF-analytic
  reason that the A=3 reps satisfy (2A)²·a_1 = 4Δ_b − 9 while
  the A=4 reps do not? The factor (2A)² = 4A² appears naturally
  in the leading Birkhoff polynomial-correction structure;
  testing the relation against a third A=3 representative
  (or against a recomputed A=4 rep with non-anomalous Δ_b) would
  discriminate "interpolation coincidence" from "real sub-family
  closed form".

* The QL09 a_1 = 0 anomaly remains (separately) the subject of
  017f.

---

## 5. AEAL claims summary

18 claims written to claims.jsonl this session, covering Phase A
precision check + CF reconstructions; Phase B per-rep PSLQ at
both tolerances; Phase C joint PSLQ + functional-fit + sub-family
form test + polyfit; Phase D QL09 boundary; verdict label.

---

*Forbidden-verb hygiene: this certificate uses "consistent with",
"is consistent with", "PSLQ-clean", "matches" exclusively in
prediction-or-conjecture context. The per-rep rationals are
**PSLQ-consistent at tol=1e−30**; AEAL elevation is contingent
on Claude review and cross-validation against the analytic
Birkhoff structure.*
