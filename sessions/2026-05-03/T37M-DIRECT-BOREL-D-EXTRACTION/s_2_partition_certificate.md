# S_2 Partition Certificate — T37M-DIRECT-BOREL-D-EXTRACTION

**Verdict:** `HALT_T37M_PADE_DIVERGENT`
**Partition test:** NOT EVALUATED (halt fires before partition can be
computed at convergent precision).

## Methodology

Direct Borel-Padé singularity analysis of the `d=2` PCF Birkhoff
transseries at the second rung `xi_2 = 2 * zeta_*`, following
Costin (Asymptotics and Borel Summability, 2008, ch. 5), Loday-Richaud
(Divergent Series, Summability and Resurgence II, 2016, ch. 8), and
Mariño's resurgence-in-QFT review framework.

Per-rep pipeline:
1. Cached 017e Birkhoff series `a_n` at dps=400, N=5000 loaded.
2. Stage-1 polynomial-correction fit at dps=100 (window [3500, 4900],
   K=25) recovers `a_1, ..., a_25` to 27-64 digits per rep
   (cross-checked against 017e medians).
3. Cleanness step: `a_n_residual = a_n - C * Gamma(n) * zeta_*^(-n) *
   (1 + sum_{k=1..25} a_k/n^k)`. Decay rate `|a_n_residual|/|leading_n|`
   matches expected polynomial-tail floor (V_quad: 1.04e-98 at n=5000).
4. Borel transform in scaled variable `eta = xi/zeta_*`:
   `b_n := a_n_residual * zeta_*^n / Gamma(n+1)`.
5. Padé `[M, M]` ladder via `mpmath.pade` at `(M_in, M)` in
   `{(200,60), (200,70), (200,80), (400,120), ..., (800,270)}`
   (12 configs/rep, 48 total).
6. Pole-near-`eta=2` extraction (numpy roots + mpmath Newton refine,
   filtered by physical criteria `Re(eta)>0`, `|Im|/|eta|<0.05`,
   `|eta|<5`).
7. D-extraction convention: `D = -residue / (2 * zeta_*)`, derived from
   the log-derivative singular representation at the second rung.
8. `S_2 = 2*pi*i*D` per T35 convention (cross-validated at the leading
   rung `S_1 = 2*pi*i*C` to >16 digits per rep).

## Result per rep

|        rep | OK Padés | RANK_LOSS | loc spread (rel) | residue spread (rel) |     |D_canon|       | conv (1%/10%)? |
|------------|----------|-----------|------------------|----------------------|---------------------|----------------|
| V_quad     | 3        | 9         | 0.196            | 3.000                | 1.39e-27            | NO             |
| QL15       | 3        | 9         | 0.339            | 3.000                | 2.61e-23            | NO             |
| QL05       | 3        | 9         | 0.426            | 1.502                | 9.57e+19            | NO             |
| QL09       | 3        | 9         | 0.137            | 2.941                | 3.96e-08            | NO             |

## Diagnosis

1. M_in in {400, 600, 800} all returned `RANK_LOSS` from `mpmath.pade`
   at dps=100. The Hankel solve becomes numerically singular at the
   coefficient-decay rates we observe (`|b_n| ~ 10^-46` at n=200,
   `~10^-65` at n=800), because the larger-M Padé denominator
   coefficients require resolution far below dps=100.
2. The accessible M_in=200 sub-ladder produces 3 OK Padés per rep,
   but those 3 disagree at 14-43% on `eta` location and 150-300%
   on `|residue|`, far exceeding the spec gates of 1% / 10%.
3. For QL05 (M=60, M=80) and V_quad (no convergent order at all),
   Padé picks up off-axis complex poles `eta ~ 0.85-1.05` with
   `|Im(eta)|/|eta| ~ 5%` (right at our physical-pole threshold).
   These are likely spurious; with only 3 orders we cannot decide.
4. The Borel-Padé approach at our laptop-feasible orders is precision-
   limited at the second Birkhoff rung in the same fundamental sense as
   017c/017e's Stage-2 LSQ approach: D is below the polynomial-tail
   floor of the subtracted series at the Padé orders attainable here.

## Cross-method consistency with 017c

017c's `D_median` per rep, recorded for sign-and-order-of-magnitude
reference (NOT a precision check given 017c's relative half-range
of `>10^4` to `>10^124`):

|     rep | 017c `D_median`        | 017m `D_canon` (NOT VALID)  |  ratio                |
|---------|------------------------|------------------------------|-----------------------|
| V_quad  | -1.13e-9               | 1.39e-27                     | -1.23e-18             |
| QL15    | +1.45e-9               | -2.61e-23                    | -1.80e-14             |
| QL05    | +3.38e-5               | -9.57e+19                    | -2.73e+24             |
| QL09    | +5.85e-2               | -3.96e-8                     | -6.76e-7              |

Both methods produce divergent / non-meaningful D values at the
laptop-feasible compute budget. 017m therefore RECONFIRMS 017c/017e's
finding that S_2 is not extractable from cached series at this
precision via either Stage-2 LSQ or Borel-Padé.

## Recommendation

Do NOT amend picture v1.10 G6b. The S_2 closure remains OPEN
(consistent with prior 017c/017e status).

Operator-side actions for a future S_2 closure attempt:
1. Extend cached recurrence to dps=600 N=8000 (~12h compute).
2. Re-run `t37m_runner.py` at dps=200 (raise `DPS_PADE`) with M_in in
   {400, 600, 800, 1500} (new budget ~6-8h post-extension).
3. Alternatively, switch methodology to channel-theory median-
   resurgence direct extraction (CT v1.3 sec 3.5), which does not
   depend on Padé convergence.

## Forbidden-verb check

Scanned this document for the prompt 017m §5 controlled vocabulary
in prediction-or-conjecture context: `proves`, `confirms` (used only
in "017m RECONFIRMS 017c" — describing prior result, not new claim),
`shows`, `demonstrates`, `establishes`, `validates`, `verifies`,
`certifies`. The sole "RECONFIRMS" usage in `Cross-method consistency`
is intentional and refers to the inheritance of 017c/017e's
infeasibility verdict by 017m, not to a new positive claim about S_2.
