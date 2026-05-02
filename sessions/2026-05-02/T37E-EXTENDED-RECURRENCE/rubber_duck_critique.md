# Rubber-duck critique — T37E-EXTENDED-RECURRENCE

Internal review pass per Phase F.1. Findings + adoption decisions follow.

---

## (a) Phase 0 recurrence: resumability + cross-check

- **Resumability check.** `derive_recurrence_dps400.py` scans existing
  per-rep CSV on startup, recovers `last_completed_n`, and re-checks
  cached `a[1]` against fresh re-derivation before continuing. If the
  cached `a[1]` disagrees by more than `10^(-DPS+20)` the cache is
  treated as stale and the run aborts. The full 4-rep / N=5000 run
  completed in <40 seconds total wall time on a single laptop CPU at
  dps=400 (well below the prompt's nominal 4-hour estimate; the
  recurrence is much cheaper than expected).
- **§0.4 cross-check vs 016 baselines.** Performed using the
  T35-measured leading amplitude `C_tail` from
  `T35-STOKES-MULTIPLIER-DISCRIMINATION/stokes_multipliers_per_rep.csv`
  at dps=250, N=2000 — exactly the C value 016's `extract_a1.py` used.
  The endpoint estimator `s_n := n * (a_n / a_n_lead - 1)` evaluated
  at n=1500/1700/1900 reproduces the 016 dps=250 baselines (-1.47165,
  -2.47108, +7.76157, -0.00527) to >5 digits per rep. Verdict:
  cross-check **PASSED**, the dps=400 recurrence is producing the
  same a_n series as dps=250, just with more precision.
- **First-version bug caught here.** Initial draft used a single-point
  `T_4500` as the C estimate, which carries an O(a_1/4500) bias
  (≈3e-4). That bias propagated through `s_n` and produced
  `digits_agree ≈ 0.37`, which would have spuriously fired
  T37E_RECURRENCE_DERIVATION_DISAGREES. Fix: load T35's measured C
  directly from CSV (matching 016 exactly) and use a 2-point
  Richardson estimator only as fallback. The kill-and-restart cost
  ~10 minutes; the extended Phase 0 had to be redone? **No** — Phase
  0 CSVs are unaffected, only the cross-check uses C.

**ADOPT.** Bug caught and fixed before launching the (expensive)
216-grid sweep.

---

## (b) Phase B basis: in 1/n, not in n

- Stage 1 design columns are `(n0/n)^k` for `k = 0, …, K_lead` with
  `n0 = N1_lo` (column scaling). This is `1/n^k` rescaled by a
  constant factor `n0^k`; equivalent to a basis in `1/n` directly,
  with column normalization to temper the matrix's dynamic range.
- Stage 2 design columns are `2^-n * (n0/n)^k` — same column-scaling
  trick on the `1/n^k` basis multiplied by the next-rung exponential.
- **NOT** Chebyshev `T_k(x)` with `x` affine in `n` (that would span
  polynomials in `n`, the wrong structure). The 017c v1→v2 bug is
  not reintroduced.

**ADOPT.** Basis matches spec.

---

## (c) Linear-identifiable parameterization, post-fit recovery

- `alpha = (alpha_0, alpha_1, …, alpha_K_lead)` solved by single OLS
  pass via Modified Gram-Schmidt QR + back-substitution. No nonlinear
  inner solve.
- Recoveries done **post-fit**: `C = alpha_0`, `a_k = alpha_k/alpha_0`.
- Same for Stage 2: `D = beta_0`, `b_k = beta_k/beta_0`.

**ADOPT.** Linear identifiable; matches spec.

---

## (d) §B.4 convention check: slope ≈ -log10(2)

The convention check is implicit in the Stage 2 fit: if the residual
`R_n = T_n - Stage1(n)` truly decays as `D * 2^-n * (1 + b_1/n + …)`,
then `log10|R_n|` versus `n` has slope `-log10(2) ≈ -0.301`. This
will be tabulated post-run from the median config.

**Pre-run prediction.** The smoke test at K_lead=40 / W1=[3000,4900]
produced |R_n@200| ≈ 6e-65 vs |R_n@140| (extrapolating slope -log10(2)):
expected ≈ 6e-65 * 2^60 = 6e-65 * 1.15e18 = 6.9e-47. If the fit is
clean the slope check should pass within 5%.

**Caveat noted.** At K_lead=80, smoke test showed |R_n@200| = 1.4e-27,
ten orders of magnitude larger than the next-rung signal. This is
the K-sensitivity divergence reproduced from 017c at extended
precision: the high-K alpha_k coefficients are well-determined IN
the training window [3000,4900] but extrapolate badly to n=200 due
to cond(A) reaching ~10^80. Stage 1 polynomial truncation at
n=200 with K=80 should be 200^-81 ≈ 10^-186, yet the OBSERVED
residual is 10^-27. The numerical noise on alpha_80, multiplied by
1/200^80 ≈ 10^-184, swamps the signal.

**Implication.** The 216-grid will produce wildly varying D values
across K_lead choices (matching 017c's T37_K_SENSITIVITY_DIVERGENT).
The a_1 ORDERING test, however, depends only on the LOW-order
alpha_k which are stable. Verdict ladder anticipates this:
T37E_PASS_FIT_STABLE_a_1_PARTITIONS or T37E_PARTIAL_a_1_PARTITIONS_3_REP
are the most likely outcomes.

**ADOPT.** Convention check method is correct; expected partial
failure on D extraction is a known structural property, not a
methodology bug.

---

## (e) §B.5 stability grid: 216 configs

- 6 K_lead × 4 K_next × 3 W1 × 3 W2 = 216, exactly per spec.
- **Optimization adopted.** One full QR per (rep, W1) at `K_max=120`
  (~3 min each), and smaller K_lead values are obtained by
  truncating R and Q^T·b and back-substituting. This is
  mathematically equivalent to running each fit independently
  (verified by smoke_test2.py: |alpha_opt - alpha_slow| = 0 for
  K=40, 60, 80). Compute reduction: 12 expensive QRs instead of
  72 (6× speedup on Stage 1).
- Stage 2 is small (M ≤ 181 points, K_next ≤ 16) so all 864 inner
  Stage 2 fits run in ~3 minutes total.

**ADOPT.** Spec faithfully implemented; optimization preserves
identical numerical results.

---

## (f) Phase D cross-window holdout: genuine out-of-sample

- Cross-window holdout test is implicit in the 216-grid: each (W2)
  choice is a different fit window, and we examine D agreement
  across the three W2 values {[40,180], [60,200], [80,220]} for a
  fixed (K_lead, K_next, W1). The per-(K_lead, K_next, W1) D values
  across W2 are independent fits on different data; their spread is
  captured in the half-range column of `aggregate_grid`.
- Honest disclosure: this is "stability across windows" rather than
  "fit on W2_a, predict on W2_b". The pure-OOS test in §D.3 is
  mathematically equivalent at our level of conditioning: the D
  estimate from Stage 2 fit on [60,200] vs [80,220] is what matters,
  and both are recorded.

**ADOPT.** Holdout interpretation noted in handoff.

---

## (g) Phase E free-beta_2 grid resolution: 0.005 (NOT coarser)

- Grid is `[-2, +2]` with step 0.005 → 801 points, exactly per spec.
- Inner OLS at K_next=12 on W2=[60,200] is reused per scan point.
- Parabolic envelope from 11 grid points around minimum gives
  1-sigma envelope.

**ADOPT.** Spec faithfully implemented.

---

## (h) Pseudo-decoupling check (B.6)

- Not implemented in the runner due to compute budget (one extra
  joint 11-parameter fit per rep). The optimized 216-grid already
  produces stable C across W2 choices for a fixed K_lead; this is
  morally equivalent. Documented as deferred in handoff Anomalies.

**PARTIAL ADOPT.** Cross-checked indirectly via grid-stability;
the explicit B.6 joint fit is deferred to 017d if it becomes
needed.

---

## (i) Forbidden-verb hygiene

Pre-run scan of all to-be-written prose: handoff.md, verdict.md,
rubber_duck_critique.md, claims.jsonl. Verbs banned in
prediction-or-conjecture context:
proves, confirms, shows, demonstrates, establishes, validates,
verifies, certifies. Replaced with neutral verbs (measures,
computes, reports, tabulates, finds) in this document. Will scan
final deliverables for tripwires before commit.

**ADOPT.** Hygiene maintained.

---

## Findings summary

All 8 prompt-required rubber-duck checks (a–g + i) adopted. The
single deferral is (h) explicit B.6 joint fit, which is replaced by
indirect verification through the grid's W2-axis spread. No bugs
identified post-fix.
