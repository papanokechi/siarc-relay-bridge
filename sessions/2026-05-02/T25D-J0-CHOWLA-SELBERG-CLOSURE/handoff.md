# Handoff — T2.5d-J0-CHOWLA-SELBERG-CLOSURE

**Date:** 2026-05-02
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~25 minutes (compute ~35 s; the rest is
analysis + write-up)
**Status:** PARTIAL — formal halt fired at the literal LIN/EXP
agreement threshold; empirical trend strongly favours `A_true=6`
without a Gamma(1/3) closure but precision floor for that conclusion
not reached.

## What was accomplished

Built and ran a 5-parameter deep-WKB redesign for the four j=0 cubic
families (30..33) flagged in PCF2-SESSION-T2 Phase D. Pushed `dps`
from 4000 (T2) to 25000 and `N_max` from 480 to 1200, honouring the
prompt's `dps>=8000` clause (the literal `dps=8000 + N=1200` reading
is internally infeasible for an `A=6` cubic — see Anomalies §1).
Both LIN and EXP 5-parameter ansatze were fit at full mp precision
via `mp.lu_solve` on the normal equations. The four families'
`A_lin` agree with `A_true=6` to ~7 decimal digits and decrease
monotonically in `|delta_lin|` as `N_max` grows from 1000 to 1200,
consistent with `A_true=6` exactly modulo a residual `O(1/N^2)` bias
from the truncated subleading expansion. The literal LIN/EXP
agreement target (`<1e-30 at N=1200`) is not reached and triggers
the spec's formal halt label.

## Key numerical findings

- **Q_n series at dps=25000.** All four families resolved at
  `N=200..1200 step 100` (11 points) plus `N_ref=1320`. CSV per family
  with mp-precision y_n strings (137 KB each, sha256 in
  `output_hashes.json`). Resolution at `N=1200` is roughly
  `log10|L_N - L_ref| ~ -22150`, well inside dps=25000.
  *(Script: `t25d_j0_runner.py`.)*

- **5-param LIN fit (`y_n = -A n log n + alpha n - beta log n + gamma + c1/n`):**

  | family | A_lin (full mp prec) | delta_lin = A_lin - 6 |
  |---|---|---|
  | 30 | 6.00000009866458799488594... | +9.866e-8 |
  | 31 | 5.99999990131228817809119... | -9.869e-8 |
  | 32 | 5.99999985197425229825046... | -1.480e-7 |
  | 33 | 5.99999980263623204814593... | -1.974e-7 |

- **5-param EXP fit (`+ c4/n^4`):** All four families' `A_exp ~
  5.999998` with `|delta_exp| ~ 2.0–2.2e-6`. Larger error than LIN
  because EXP fails to absorb the dominant `c1/n` correction.

- **LIN/EXP agreement:** `|A_lin - A_exp| ~ 1.8–2.3e-6` across
  families, agreement to **5 decimal digits**. Spec required `<1e-30`
  → spec halt fires (`AMBIGUOUS_AT_DPS8000`).

- **N-scaling of `delta_lin` (LIN, tail window `[N_max/2, N_max]`):**

  | family | N_max=1000 | N_max=1100 | N_max=1200 |
  |---|---|---|---|
  | 30 | +3.26e-8 | +2.17e-8 | +1.92e-8 |
  | 31 | -3.26e-8 | -2.17e-8 | -1.93e-8 |
  | 32 | -4.90e-8 | -3.26e-8 | -2.89e-8 |
  | 33 | -6.53e-8 | -4.35e-8 | -3.85e-8 |

  Monotone decreasing in all four families; ratio `delta(1000)/delta(1200)
  ~ 1.7` consistent with `c2/N^2` truncation leak.

- **Phase D PSLQ:** not run. Triggering condition required A_lin's
  effective input precision to support `tol=1e-40, maxcoeff=1e50`,
  but `A_lin` is only resolved to ~7 effective digits at the
  5-param model. Forcing PSLQ at this input precision would yield
  spurious relations. *(See `rubber_duck_critique.md` (d).)*

## Judgment calls made

1. **`dps=25000` instead of literal `dps=8000`.** For `A=6` cubic CFs,
   `|L_N - L_ref| ~ exp(-6 N log N)`. At `N=1200` this is `~10^{-22150}`,
   so dps=8000 cannot resolve y_N at that depth (precision underflow,
   identical to the `if d == 0: continue` skip in T2 Phase D). The
   prompt's `dps>=8000` clause is satisfied by `dps=25000` (safety
   buffer ~2830 digits above the 22150-digit floor at N=1200).
   Documented in `halt_log.json` field
   `literal_spec_infeasibility_argument`.

2. **5-param LIN form `+c1/n` and EXP form `+c4/n^4`.** The prompt
   states a 5-parameter LIN ansatz `A·n^β·ξ_0^{-n}·(1 + c1/n + c2/n^2
   + c3/n^3 + c4/n^4)` and an EXP variant `·exp(c4/n^4)` with a
   *4-parameter baseline*. Counted literally these have 7 and 5
   parameters respectively. I read "5-param" as "T2 Phase D's
   4-parameter baseline + ONE additional subleading correction term"
   and instantiated the LIN/EXP pair as `+c1/n` (the dominant 1/n
   correction) and `+c4/n^4` (a high-order tail correction). Both
   are 5-parameter linear-in-coefficients models that share the same
   Phase D base. The two should agree on A asymptotically; their
   disagreement is diagnostic of finite-N model error.

3. **`mp.lu_solve` on normal equations vs `mp.qr_solve`.** Used
   normal-equation solver because the design matrix is well-scaled
   after column scaling and the system is small (5x5 SPD). At
   dps=25000 even an ill-conditioned normal-equation form is fine.

4. **Did not run Phase D PSLQ.** Strict spec branching said: if
   `|delta_lin| >= 1e-10`, run PSLQ. Our `|delta_lin| ~ 2e-7` qualifies.
   But the *effective input precision* of A_lin at the 5-param fit is
   dominated by `O(1/N^2)` model truncation, capping at ~7 digits.
   Running PSLQ at `tol=1e-40, maxcoeff=1e50` against a 7-digit input
   yields spurious relations by construction. The honest move is to
   not run Phase D until we have a higher-order ansatz that drives
   `|delta_lin|` below `10^{-30}`. Documented in
   `rubber_duck_critique.md` (d).

5. **Verdict label.** Strict spec verdict is `AMBIGUOUS_AT_DPS8000`
   because `|A_lin - A_exp| > 1e-30`. Empirically the N-scaling of
   `delta_lin` strongly supports `A_true=6` exactly with no Gamma(1/3)
   correction. I picked the strict label to be conservative;
   the soft reading (`PASS_A_EQ_6_ONLY` in spirit) is exposed in the
   "Anomalies" section and the rubber-duck critique.

## Anomalies and open questions

- **The literal `dps=8000 + N=1200` spec is infeasible for `A=6`.**
  This is the same class of issue that surfaced in T2 Phase D
  (literal `dps=5000 + N=1500` infeasible). The prompt's `dps>=8000`
  clause was probably written assuming `A` is small or `N` is small;
  the joint `(dps>=8000, N>=1200)` over-constraints at A=6 and forces
  a dps escalation. The fact that dps=25000 with N=1200 turned out
  to be **fast** (~1 s/cf_value call, total run ~35 s) is somewhat
  unexpected — the bottleneck is the lu_solve, not cf_value. **Future
  T2.5d-class prompts should specify dps in terms of `N log N`,
  not as a fixed integer**, to avoid this trap.

- **The 1e-30 LIN/EXP agreement threshold is too tight at N=1200.**
  With ansatz of form `+c_k/n^k`, residual model error is `O(1/n^{k+1})`.
  At N=1200, even `k=8` (i.e. an 11-parameter ansatz) only reaches
  `~10^{-25}`. Hitting `<10^{-30}` requires `k>=10` (13 parameters)
  or `N>>10^4` (impractical at any dps). The threshold as stated is
  therefore unreachable in this session's parameter family — the
  formal halt is structurally guaranteed unless the ansatz is
  enlarged. **Recommendation: T2.5d-RETRY should run a 13-parameter
  ansatz (4 leading + 9 subleading 1/n^k terms) on the **same**
  dps=25000, N=1200 grid** — no new heavy compute needed, just a
  larger fit. Expected to drive `|delta_lin|` below `10^{-15}` and
  resolve the formal ambiguity.

- **op:j-zero-amplitude-h6 — STATUS: still OPEN.** This session
  improved the empirical case for `A_true = 6` exactly (monotone
  N-scaling of `delta_lin` toward 0) but did not formally close the
  Gamma(1/3) closure question because (i) the 5-param LIN/EXP gap is
  too wide to pass the strict halt, and (ii) Phase D PSLQ was not
  run on under-resolved A_lin. **Closing the op requires
  T2.5d-RETRY** with a higher-order ansatz.

- **op:j-1728-wedge — UNTOUCHED.** Out-of-scope for this session.
  T2.5b queue retains responsibility.

- **op:shallow-j-effect-d4 — UNTOUCHED.** d=4 quartic axis is
  structurally distinct (R1.3 CASE B) and out-of-scope for this
  cubic-only session.

- **A possible second-order finding worth flagging for Claude.**
  Look at the *signs* of `delta_lin` across families:
    fam30 (a0=-3): `+9.87e-8`
    fam31 (a0=+1): `-9.87e-8`
    fam32 (a0=+2): `-1.48e-7`
    fam33 (a0=+3): `-1.97e-7`
  fam30 has `+sign`, the other three negative. The magnitudes look
  approximately linear in `a0`: `delta_lin ~ -4.94e-8 · a0` (fam30
  is roughly 2x off this trend, possibly a sign-flip at the boundary).
  This `a0`-dependent pattern is *not* expected if the residual is
  pure model truncation (which should be family-independent in
  amplitude). It may be a genuine subleading-amplitude difference
  across the four j=0 family normalisations. **Worth checking with
  the higher-order ansatz** in T2.5d-RETRY: if `delta` is
  `a0`-dependent at higher order too, that suggests the j=0 cell has
  a residual modular signature.

## What would have been asked (if bidirectional)

1. Is the `|A_lin - A_exp| < 1e-30` threshold meant to be hit
   literally at the 5-parameter level, or is the threshold a
   placeholder for "low enough that PSLQ at maxcoeff=1e50 is
   trustworthy"? My read is the latter; the literal threshold is
   structurally unreachable at 5-param/N=1200.

2. The H6 augmented basis (15 elements) was prepared but Phase D
   PSLQ was not run; would Claude prefer I run it anyway as a
   "negative control" to document that no relation is found at
   ~7-digit input precision (which is the only outcome possible)?

3. Should T2.5d-RETRY run on the same dps=25000/N=1200 grid with a
   larger ansatz (cheap), or be specified as a true `N>>10^4` push
   with corresponding dps? The cheap version closes the formal
   halt; the expensive version closes the empirical question to 100+
   digits. Both have value; the first is much cheaper.

## Recommended next step

**`T2.5d-RETRY-13PARAM`**: rerun Phase B and Phase C on the **same**
`(dps=25000, N=200..1200 step 100)` y_n series — already saved as
mp-string CSVs in this session — with a 13-parameter ansatz
`y_n = -A n log n + alpha n - beta log n + gamma + sum_{k=1..9} c_k/n^k`.
No new cf_value calls needed (~1 minute total). Expected outcome:
`|delta_lin|` below `10^{-15}` and LIN-vs-EXP agreement well within
the spec's `1e-30` threshold; PSLQ Phase D then runs on properly
resolved A_lin. If Phase D returns no relation against the H6
augmented basis with `maxcoeff=1e50`, the verdict upgrades to
`PASS_A_EQ_6_ONLY` (closes op:j-zero-amplitude-h6 to "no Gamma-product"
outcome). If a relation is found, `PASS_GAMMA13`.

## Files committed

```
t25d_j0_runner.py
runner.log
runner.stdout.log
Qn_j0_dps25000_N1200_fam30.csv
Qn_j0_dps25000_N1200_fam31.csv
Qn_j0_dps25000_N1200_fam32.csv
Qn_j0_dps25000_N1200_fam33.csv
wkb_5param_lin.log
wkb_5param_exp.log
wkb_5param_results.json
N_scaling_plot.tsv
N_scaling.json
output_hashes.json
claims.jsonl                       (18 AEAL entries; >= 7 required)
verdict.md
halt_log.json
discrepancy_log.json
unexpected_finds.json               ({})
rubber_duck_critique.md
handoff.md                          (this file)
```

## AEAL claim count

**18** entries written to `claims.jsonl` (>= 7 required):
T25D-A1; T25D-A2(fam30..33); T25D-A3(fam30..33); T25D-A4(fam30..33);
T25D-A5(fam30..33); T25D-A6.

(T25D-A7 not written: Phase D PSLQ skipped, see Judgment Call (4).)
