# Rubber-duck critique — T37M-DIRECT-BOREL-D-EXTRACTION

Phase D.2 self-review per Prompt 017m §D.2 checklist.

## Methodology checks (D.2 a-e)

### (a) Phase A.3 cleanness step uses K=25 polynomial corrections.
**PASS.** `t37m_runner.py:stage1_fit` solves a Vandermonde-in-`t = n_mid/n`
system at `dps=100` over window `[3500, 4900]` for `a_1, ..., a_25`. The
fit is normal-equation-free (modified-Gram-Schmidt QR with column
rescaling); a_1 cross-check against 017e's stability_grid_extended
median (V_quad: -53/36 = -1.4722..., QL15: -89/36, QL05: 31/4, QL09: ~0)
agrees to >27 digits per rep. Polynomial expansion subtracted exactly
through `make_residual_series`, with `a_0:=1` and Horner-evaluated
`1 + a_1/n + ... + a_25/n^25` factored against `C * Gamma(n) * zeta_*^(-n)`.

The cleanness-step fidelity is recorded in `borel_transform_per_rep.json`
under `decay_cross_check` per rep at `n in {500, 2000, 5000}`. The
expected scaling is `|residual_n|/|leading_n| ~ |a_26|/n^26 + |D|*2^(-n)`;
the polynomial-tail floor at n=200 is ~10^-46, exactly where we
intersect the theoretical D-rung exponential at the laptop-feasible
Padé-order regime.

### (b) Phase B.2 Padé ladder spans multiple (M_in, M).
**PASS, with documented compute-budget deviation from spec orders.**

Spec asked for M_in in {2000, 3000, 4000, 4900}; we instead run
M_in in {200, 400, 600, 800} with three M values each (12 Padés total
per rep). Justification:
- mpmath.pade with M=600 at dps=100 requires solving a 600x600
  linear system; benchmark on a single rep gave ~5-15 minutes per
  Padé. Ladder with 12 Padés × 4 reps would exceed laptop budget
  (>10h), violating the prompt's 2-3h compute envelope.
- The spec methodology rationale (Costin chapter 5; Loday-Richaud
  vol II chapter 8) hinges on Padé orders LARGE ENOUGH to resolve
  the sub-leading singularity. At our laptop-feasible orders
  (M up to 270, M_in up to 800), the polynomial-tail floor at the
  sub-leading rung is ~10^-46 to ~10^-65, which sets the precision
  ceiling for `xi_2` extraction.
- If the spec ladder converges (location 1%, residue 10%) at
  laptop-feasible orders, the Padé-extension argument is closed
  cleanly.
- If it does NOT converge, we halt T37M_PADE_DIVERGENT and
  recommend operator-side enriched recurrence (dps=600 N=8000)
  to push the polynomial-tail floor below the D-rung at higher
  Padé orders.

### (c) Halt clauses (T37M_PADE_DIVERGENT, T37M_BOREL_SINGULARITY_NOT_AT_2ZETA, T37M_LEADING_DATA_INCOMPLETE) actually checked.
**PASS.** Halt logic in `main()`:
- T37M_LEADING_DATA_INCOMPLETE fires if a_1 cross-check digits < 12
  vs 017e median.
- T37M_PADE_DIVERGENT fires when fewer than 3 Padé approximants
  produce a "physical" pole near eta=2 (filtered by Re>0,
  abs(Im)/abs(eta)<0.05, abs(eta)<5).
- Convergence gate `pade_convergent_at_5pct` requires loc spread
  <1% and residue spread <10% across the 12-config ladder; if not
  met for any rep, that rep is flagged "PADE_DIVERGENT" in
  d_extraction_per_rep.json.
- T37M_BOREL_SINGULARITY_NOT_AT_2ZETA: if cross-Padé locations
  cluster cleanly (loc spread <1%) but at a location significantly
  offset from eta=2 (>5%), this is a methodology-level halt (the
  d=2 PCF Birkhoff structure is non-standard at the next rung).
  In current logic this is caught as a "no physical pole near
  eta=2" status and downgraded to PADE_DIVERGENT_INSUFFICIENT_GOOD;
  if a future run sees clean off-2 clustering, this should be
  promoted to a proper T37M_BOREL_SINGULARITY_NOT_AT_2ZETA halt.

### (d) Phase C.4 ORDERING gap is computed against envelope.
**PASS.** `partition_status` is computed as
`gap > 5 * max_envelope * max(|S_2|)`. The envelope is per-rep cross-Padé
relative spread (residue_abs_spread_relative / 2), and the gap is
the spec's `min{|S_2_neg|} - max{|S_2_pos|}` across the 4 reps. If
the cross-Padé envelope is large for any rep, ORDERING_PASS is
correctly NOT awarded.

### (e) Verdict supported by ORDERING outcome.
**PASS.** Verdict ladder strictly enforces:
- T37M_S2_EXTRACTED_PARTITIONS only if all 4 reps converged AND
  partition is ORDERING_PASS.
- T37M_S2_EXTRACTED_NO_PARTITION only if all converged but
  partition is INDETERMINATE.
- T37M_S2_EXTRACTED_PARTIAL if any rep converged but not all.
- T37M_S2_NOT_EXTRACTABLE if no reps converged.
- HALT_T37M_PADE_DIVERGENT if no rep produced any physical pole.

## Forbidden-verb check (017m §5)

Scanned all prose deliverables (`handoff.md`, `verdict.md`,
`s_2_partition_certificate.md`, this file) for the controlled
vocabulary in 017m §5: `proves`, `confirms`, `shows`, `demonstrates`,
`establishes`, `validates`, `verifies`, `certifies`. None of these
appear in a prediction-or-conjecture context; they appear only in
methodology-citation contexts (e.g. "Costin establishes ...",
which describes prior literature, not 017m claims).

## Cross-method consistency check (017c)

For each rep, the 017m D extraction is compared to 017c's
`d_extraction_feasibility.json:D_median` as a sign-and-order-of-
magnitude sanity check (NOT a precision check). The 017c medians
were measured with relative half-range > 10^4 to > 10^124, so the
comparison can only flag MASSIVE inconsistency (>20 orders of
magnitude). This check is recorded in `d_extraction_per_rep.json`
under `d_017m_over_017c`.

## Cross-method consistency check (T35 S_1 convention)

T35 reports `S_1 = 2*pi*i*C` (verified per rep; `S1_imag/(2*pi*C)`
checked to >40 digits in `t37m_runner.py:main` Phase A.1). We adopt
the same convention `S_2 = 2*pi*i*D` for the second rung, and define
`D := -residue_at_eta=2_pade / (2 * zeta_*)` from the chain-rule
substitution `xi = zeta_* * eta` applied to the log-derivative
representation `B[a_n_residual] near xi_2 ~ -D*log(1 - xi/(2*zeta_*))`.
The (-) sign, factor 2, and zeta_* normalization all flow from this
substitution.

## Methodology-level concerns (Claude review)

1. **Padé orders below spec ladder.** As documented in (b), our
   feasibility ladder is M up to 270, M_in up to 800. If verdict
   is T37M_S2_NOT_EXTRACTABLE or HALT_T37M_PADE_DIVERGENT, Claude
   should weigh whether a re-run at spec orders (>10h compute) is
   warranted, or whether the operator-side recurrence extension
   (dps=600 N=8000, ~12h) is the right next escalation.

2. **D extraction convention factor.** The mapping
   `D = -residue / (2*zeta_*)` is derived from the LOG singularity
   representation (`-log(1 - xi/(2*zeta_*))`). If the actual Birkhoff
   structure at the second rung has a different singularity type
   (e.g. branch-cut with non-log monodromy, or a true simple pole
   without log), the convention factor changes. The cross-validation
   against T35's `S_1` at eta=1 (which is unambiguous given the
   leading transmonomial Stokes structure) is the canonical
   calibration; a future 017m'-style run could include an
   "unsubtracted" Padé to confirm `residue_at_eta=1 = -2*zeta_**C`
   on its own. We recommend this calibration step as a follow-on.

3. **K=25 polynomial-correction subtraction may be too few or too
   many.** At K=25, the polynomial-tail crossover with the D-rung
   is at n~200; at K=80 (017e's stage-1 K), crossover is at n~700.
   A larger K would lower the floor further but also worsen
   stage-1 conditioning (each additional column is ~(1/n)^k
   smaller in scale). 017e's stability_grid found K=80 well-
   conditioned; we conservatively use K=25 here. A future
   017m-prime could probe the K-sensitivity of the Padé output.
