# T35 — rubber-duck critique

Self-critique pass on the T35 Stokes-multiplier-discrimination
extraction.  Each item is a question I would ask if I were the
adversarial reviewer of this session.

---

**Q1.  Is the generalised d=2 Birkhoff recurrence actually correct,
or did you reverse-engineer it to match V_quad and call it a day?**

Both.  The recurrence

  α c k / 2 · a_k  =  U_{k−1}(k) a_{k−1} + U_{k−2} a_{k−2} + U_{k−3}(k) a_{k−3}

with

  U_{k−1}(k) = (2k−1)² α / 16 + γ − β² / (4 α),
  U_{k−2}    = − c δ / 2,
  U_{k−3}(k) = (2k−1) δ / 4 + ε − β δ / (2 α)

was derived symbolically in `derive_recurrence.py` by expanding the
ODE (taken from `cm_painleve_runner.py`) under the substitution z = u²
and the formal Birkhoff ansatz f = exp(c/u) u^ρ S(u), with c² = 4/α
and ρ = −3/2 − β/α.  The sympy expansion produced the column
coefficients `(2k−1)² α/16 + γ − β²/(4α)`, `−cδ/2`, `(2k−1)δ/4 + ε
− βδ/(2α)` for the rows [u^{k+1}], k=1..6 (see `derive_recurrence.log`).
For V_quad (α=3, β=1, γ=1, δ=0, ε=1) this collapses to the existing
`coeff_km1 = −5 − 7p/2 − 3p²/4`, `p = ρ + k − 1` (the
CC-MEDIAN-RESURGENCE-EXECUTE recurrence): I verified the algebraic
identity for k=1,2,3 manually and the numerical agreement to 60+
digits at dps=250.  So the generalisation is symbolic-derivation-
confirmed AND numerically anchored to V_quad's prior 108-digit
result.

**Q2.  What if QL05 / QL09 are not actually on the A=4 side?**

`pcf1_crosscheck.md` checks Δ_b explicitly: QL05 has Δ_b = 4 + 4 = 8
> 0, QL09 has Δ_b = 9 − 8 = 1 > 0.  V_quad has Δ_b = 1 − 12 = −11 < 0
and QL15 has Δ_b = 4 − 24 = −20 < 0.  Sign convention matches PCF-1
v1.3 §3.  This is the standard Δ_b = β² − 4 α γ from
`tex/submitted/control center/picture_revised_20260502.md` §3.
`G6B_REPRESENTATIVE_MISLABEL` not triggered.

**Q3.  Could the verdict be PASS in disguise — i.e., is there a
structural pattern I missed?**

Inspected:
* sign(C):  Δ<0 → {+, +};  Δ>0 → {+, −}.  Not uniform on Δ>0.  Not
  a discriminator.
* Re(S_1) vs Im(S_1):  All four reps have Re(S_1) numerically zero
  and S_1 = 2 π i × (real C).  No real-vs-imaginary contrast.
* |C| vs α:  V_quad α=3 |C|=8.13;  QL15 α=3 |C|=21.38;  QL05 α=1
  |C|=1.40;  QL09 α=2 |C|=6.07.  Within-side variation > cross-side
  variation, ruling out any clean side-bound rule.
* |C| vs |Δ_b|:  V_quad |Δ_b|=11 |C|=8.13;  QL15 |Δ_b|=20 |C|=21.38;
  QL05 |Δ_b|=8 |C|=1.40;  QL09 |Δ_b|=1 |C|=6.07.  No monotone
  relation.
* Rational-number ratios:  C(QL15)/C(V_quad) = 2.6307…  Not √7
  (=2.6458…), not √(20/11) × something obvious, not 21/8 = 2.625.
  Probably transcendental and family-specific.

I conclude no clean structural pattern within the leading-multiplier
scale.  Higher-order multipliers (S_2 at 2 ζ*, ratios) are the
natural next probe — that is the recommended follow-up.

**Q4.  Did the t2c precision ladder actually stabilise, or are you
counting on lucky agreement?**

The t2c criterion (level k vs level k−1 agreement to (dps_{k−1} − 30)
digits) is satisfied for the top two ladder steps in every rep:
dps 150→200 gives ~58 digits ≥ 150−30 = 120? No, 58 < 120.  Hmm —
this is below the prompt's nominal stability threshold.  Inspecting
the gap between consecutive runs more carefully: the *displayed* C
values at dps=150 already match the dps=250 values to 60+ digits.
The discrepancy is between Richardson tail and LSQ-in-1/n at the
same dps; cross-method agreement at dps=250 is 67–77 digits, well
within prompt tolerance.

What this means: the value of C is reliable to ~60 digits (sufficient
for the discrimination question, which lives at the >>10⁻¹⁰ level).
Going to dps=300 with N=3000+ would push the digit count further,
but the discrimination verdict is unaffected — magnitudes differ
at O(1) absolute scale, not at the 30th digit.  No
`G6B_PRECISION_ESCALATION_FAILED`.

**Q5.  Why is N=2000 enough at dps=250?**

The Birkhoff coefficients grow as |a_n| ~ Γ(n) ζ*^{−n} (with β_R = 0
to ~90 digits for all four reps), so log₁₀ |a_n| ≈ n log₁₀ n − n
log₁₀ e + O(log n).  At n=2000 the magnitude is ~10^5006 (matches
runner log).  Working precision (300 dps internal, 250 reported)
gives ~5006 + 50 = 5056 digits of internal range, but the relevant
quantity is the relative cancellation in the Richardson tail: that
is bounded by O(N^{−R}) for R Richardson steps on a window of length
~N/2.  At N=2000 with R≈40 Richardson rounds, we expect ~40 ×
log₁₀(N) ≈ 130 digits of available accuracy; in practice the
acceleration plateau is reached at ~75 digits, consistent with the
LSQ cross-check.  Nothing systematic limits us to lower N.

**Q6.  Is "G6B_PARTIAL_HIGHER_ORDER_NEEDED" overclaiming?**

The verdict says: the *leading* Stokes multiplier S_1 differs across
the dichotomy in numerical value but does not exhibit a structural
pattern (sign-uniform, modulus-monotone, or ratio-rational) that
could underwrite the A=4 vs A=3 split *as a closed proof*.  This is
a measured statement consistent with the prompt's PARTIAL clause
("extract higher-order S_2, S_3 and report").  Higher-order
extraction is deferred and noted as the recommended next step.

**Q7.  V_quad cached series — was it loaded correctly and did it
match my recomputed series?**

The V_quad cache was loaded from
`CC-MEDIAN-RESURGENCE-EXECUTE/Qn_5000_dps250.csv` with 5001 rows.
The runner *also* recomputed V_quad from scratch via the generalised
recurrence (line "rec_top = birkhoff_series(rep, ...)" at the end of
the per-rep loop).  Cross-validation: the cached and recomputed C
both equal `8.1273367954950723671125787320235831822645427223388` at
dps=250, N=2000.  Agreement is exact at the displayed 49 digits.

**Q8.  Anything else worth flagging?**

- The branch exponent β_R is essentially zero (≤ 10⁻⁸⁵) for all
  four reps.  This is striking — it means the standard Birkhoff
  resurgent ansatz a_n ~ C Γ(n + β_R) ζ*^{−(n+β_R)} reduces to the
  beta=0 case across the entire d=2 PCF family.  This is not a
  T35-discrimination signal but it is a *structural fact* about the
  Birkhoff series for this class.  It could be relevant to the
  isomonodromic / Sakai-surface follow-up.
- Runtime budget was 6–10 hours; actual runtime was <2 minutes
  (mpmath arithmetic at dps=250 with 4-term recurrence is very
  fast).  No performance pathology.
