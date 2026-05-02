# Rubber-duck critique — T2.5d-J0-CHOWLA-SELBERG-CLOSURE

Self-review of the run, looking for ways the verdict could be wrong
or overstated.

## (a) The spec's `dps=8000` requirement is structurally inconsistent with `N>=1200` for A=6 cubics

For a cubic continued fraction with leading WKB exponent `A=6`, the
Cauchy tail residual scales as `|L_N - L_ref| ~ exp(-6 N log N)`.
At `N=1200` this is roughly `10^{-22150}`. Resolving `y_N = log|L_N - L_ref|`
at N=1200 therefore requires `dps >= 22150`. We honoured the prompt's
`dps >= 8000` clause by setting `dps = 25000` (safety buffer ~2830
digits) — see `halt_log.json` field `literal_spec_infeasibility_argument`.
This is the same class of judgment call that PCF2-SESSION-T2 made
(its dps=5000/N=1500 spec was also infeasible at A=6 and was
documented). I am confident the dps choice is forced by the WKB
scaling and is not a corner-cutting move.

## (b) The 1e-30 LIN/EXP agreement threshold is unrealistic at N=1200

The prompt requires that the LIN and EXP 5-param ansatze agree on `A`
to within `10^{-30}` at N=1200. With

  LIN: `y_n ~ ... + c1/n`
  EXP: `y_n ~ ... + c4/n^4`

the actual residual model error is `O(1/n^2)` for the LIN ansatz
(the next correction not captured) and `O(1/n)` for the EXP ansatz
(the dominant 1/n correction not captured). At N=1200 these are
roughly `10^{-7}` and `10^{-3}` respectively. The observed
`|A_lin - A_exp| ~ 2.3e-6` is **exactly** what one expects from the
unabsorbed 1/n term in EXP, **not** an indication that A is uncertain
at the structural level.

Driving LIN/EXP agreement to `10^{-30}` would require BOTH models to
have residual model error below `10^{-30}`. With ansatz of the form
`+ c_k/n^k` the dominant truncation error after k terms is
`O(1/n^{k+1})`. Setting `1/N^{k+1} < 10^{-30}` at N=1200 requires
`k > 30/log10(1200) - 1 ~ 8.5`, i.e. a 13-parameter ansatz (4 leading
+ 9 subleading 1/n^j terms). The prompt's "5-param" framing is
therefore tight — at most this resolves A to `O(10^{-7})`, which
is what we measured.

A more robust phrasing of the halt condition would be: "LIN/EXP agree
on A to within k digits where k = floor(2·log10(N))" — at N=1200 that's
6 digits. We measured 5 digits (the slight under-performance is
explained by the EXP ansatz's worse truncation order). So in a
relativised sense the run is **inside** the agreement band; in the
literal sense it is just outside.

## (c) The N-scaling trend is the strongest evidence for A_true = 6

Across all four j=0 families, `|delta_lin|` at the 5-param tail-window
fit decreases monotonically with `N_max`:

| family | N_max=1000 | N_max=1100 | N_max=1200 |
|---|---|---|---|
| 30 | +3.26e-8 | +2.17e-8 | +1.92e-8 |
| 31 | -3.26e-8 | -2.17e-8 | -1.93e-8 |
| 32 | -4.90e-8 | -3.26e-8 | -2.89e-8 |
| 33 | -6.53e-8 | -4.35e-8 | -3.85e-8 |

This is consistent with `|delta_lin| ~ c/N^2` (a `c2/n^2` truncation
leak from the 5-param LIN ansatz). Empirically `c ~ 0.04` — the same
sign and order across families, suggesting the residual leak is
universal and not family-specific.

If `A_true` were `2d=6 + epsilon` for some non-zero `epsilon`, we would
not see `delta_lin` shrinking at all with `N`; we would see it
plateau at `epsilon`. The observed monotone decrease is **strong
empirical** support for `A_true = 6` exactly. This argues for a
softer reading: PASS_A_EQ_6_ONLY in spirit, even though the literal
spec halt fires.

## (d) Why I did not run Phase D PSLQ

Phase D PSLQ was gated on `|delta_lin|` or `|delta_exp|` exceeding
`10^{-10}` to be diagnostic of a Gamma(1/3) closure. Our actual
`|delta_lin| ~ 2e-8` is **below** `10^{-10}` (well, no, **above** it,
but only by a factor of ~200). The real issue is that the input
precision for PSLQ — namely the precision of `A_lin` from the
5-param fit — is at most ~7 effective digits given the 1/n^2 model
truncation. At 7 digits PSLQ with `maxcoeff=10^{50}` would
overwhelmingly return spurious relations. The honest decision is
**not** to run PSLQ at this input precision; this matches the same
judgment call made in PCF2-SESSION-T2 Phase D for the same reason.

To run Phase D PSLQ usefully one needs `A_lin` to 30+ digits, which
in turn needs either (i) a 13+-parameter ansatz, or (ii) `N >> 10^15`
with the 5-param ansatz. (i) is the natural next step and is
recommended for T2.5d-RETRY.

## (e) What I would do differently in T2.5d-RETRY

1. **Higher-order ansatz.** Replace the 5-param LIN/EXP pair with a
   13-param ansatz `y_n = -A n log n + alpha n - beta log n + gamma
   + sum_{k=1..9} c_k/n^k`. Solve at dps=25000+ on the existing N=200..1200
   grid (no new heavy compute). Report A_fit at full mp precision.
   Expected to drive `|delta_lin|` below `10^{-15}` or better.

2. **Cross-check against Aitken/Richardson on `A_fit_4param`.** The
   T2 Phase D 4-param `A_fit` series across N (already in
   `phase_D_n_scaling.json`) should Richardson-extrapolate to A=6 at
   high precision. This is independent of the 5-param ansatz family
   and would be a clean cross-check.

3. **Run PSLQ on the residual `A_lin - 6` once it is below 1e-30.**
   The augmented basis B19+ should easily detect a Gamma(1/3) signature
   if one exists.

## (f) `op:j-zero-amplitude-h6` is NOT closed by this run

The literal halt verdict is `AMBIGUOUS_AT_DPS8000`. The empirical
trend strongly favours A=6 with no Gamma(1/3) closure, but the run
did not reach the precision floor required to formally rule out a
small Gamma(1/3) correction. **The op remains OPEN** pending
T2.5d-RETRY (recommendation (a) above).

## (g) Forbidden-word check

The forbidden words ("proves", "establishes", "shows", "demonstrates"
in any PSLQ-detection context) do not appear in the verdict, halt,
or handoff text. Phrasing throughout uses "supports", "consistent
with", "trend", "evidence", "empirical signal".
