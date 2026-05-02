# Handoff — T25D-RETRY-13PARAM
**Date:** 2026-05-02
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~12 minutes
**Status:** COMPLETE

## What was accomplished
Refit the four saved j=0 cubic y_n series (Q_30..Q_33, dps=25000,
N=200..1200) with an 11-parameter LIN ansatz (4 base terms + 7
1/n corrections; K_FIT=7 instead of 9 — see Judgment calls), via
square-exact `mp.lu_solve` at workdps=4000. Ran PSLQ on the H6
Chowla–Selberg basis B19+ (17-member deduplicated; plus an 18-member
literal-from-prompt traceability run). Cross-checked via tail-window
fits (7-pt and 5-pt subsets) and via 1/N Richardson on the T2
4-param series. **Verdict: `PASS_A_EQ_6_ONLY`** — A=6 to PSLQ-detection
precision; no Chowla–Selberg amplitude closure detected in B19+.

## Key numerical findings

Per-family `|delta_lin_13param|` (script: `t25d_retry_runner.py`,
DPS_FIT=4000):

| family | A_lin (first 25 digits) | delta = A − 6 | |delta| | log₁₀|delta| |
|--------|------|------|------|------|
| 30 | 5.99999999999999999999999 | −3.27e-24 | 3.27e-24 | −23.49 |
| 31 | 5.99999999999999999999999 | −3.16e-24 | 3.16e-24 | −23.50 |
| 32 | 5.99999999999999999999998 | −1.19e-23 | 1.19e-23 | −22.92 |
| 33 | 5.99999999999999999999996 | −3.09e-23 | 3.09e-23 | −22.51 |

Tail-window agreement (DPS_FIT=4000):
- |A_11param − A_7param (tail N≥600)| ≈ 4–8 × 10⁻¹⁴ across all four
  families — consistent with leading missing 1/n⁴ truncation at N=600.
- |A_11param − A_5param (tail N≥800)| ≈ 1–3 × 10⁻⁸ — matches Prompt
  006's 5-param precision floor.

PSLQ Phase D (DPS_PSLQ=200, DPS_VERIFY=400, maxcoeff=10⁵⁰, tol=10⁻⁴⁰):
- 17-member deduplicated B19+: **no relation** on any of 4 families.
- 18-member literal basis (CS_sqrt3 included): trivial gamma-reflection
  identity `1·sqrt(3) − 3·CS_sqrt3 = 0` (target_coeff = 0) on every
  family — confirmed Q-linear dependence in the literal basis,
  documented in `unexpected_finds.json`.

Phase E Richardson (float64 input, slopes p ≈ 1.3–8.2):
- Directional cross-check confirms delta → 0 as N → ∞ across all 4
  families. Magnitude target (1e-10) is incompatible with the float64
  input precision; documented as `phase_E_spec_impedance`.

## Judgment calls made

1. **K_FIT = 7 instead of 9** (11 parameters total instead of 13).
   Saved CSVs contain 11 (N, y_n) rows. Prompt 014 Option B1 proposes
   adding `(N_ref=1320, y(N_ref))` as a 12th row to make a square 12×12
   system after dropping `c_9`, but `y(N_ref) = log|0|` is undefined
   (N_ref is the reference point in `y_n = log|L_N − L_ref|`). Cannot
   fabricate. Used 11×11 square-exact system instead (drop `c_8`, `c_9`).
   Truncation cost at N=1200 from dropped terms: ~1200⁻⁸ ≈ 2.3 × 10⁻²⁵,
   well below the 10⁻¹⁵ target. Documented in `discrepancy_log.json`.

2. **Deduplicated 17-member basis as the verdict-decisive PSLQ run.**
   Prompt 014's literal 18-member basis is Q-linearly dependent
   (`Gamma(1/3) Gamma(2/3) = 2π/sqrt(3)` reflection identity makes
   `CS_sqrt3 = sqrt(3)/3`). PSLQ trivially finds this with target
   coefficient = 0 — NOT a Chowla–Selberg signal. Removed `CS_sqrt3`
   for the verdict-bearing run; kept 18-member run for traceability
   in `pslq_results_18basis_literal.json`.

3. **PASS_A_EQ_6_ONLY in the soft branch (10⁻³⁰ < |delta| < 10⁻¹⁵).**
   The prompt's stretch goal (10⁻³⁰) is below the 11-param truncation
   floor (~10⁻²⁵). The achieved 10⁻²³ is the realistic precision
   floor of the K_FIT=7 model; PSLQ at the input precision exhausted
   the H6 B19+ basis. No relation found ⇒ no Chowla–Selberg closure
   in this basis at this precision. Verdict logic flags the precision
   shortfall vs the stretch goal in the summary.

4. **Phase E precision impedance not a verdict downgrade.** The 1e-10
   agreement target between Richardson and `delta_lin_13param` is
   incompatible with the float64-stored T2 input. Documented; verdict
   not downgraded.

## Anomalies and open questions

- **Open question for operator/Claude:** is `PASS_A_EQ_6_ONLY` at
  |delta| ~ 10⁻²³ formally sufficient to close G5 / G16, or does the
  strategic picture v1.6 require the stretch-goal 10⁻³⁰ precision (which
  would need K_FIT=9 → 13 params, requiring fresh y_n at N up to 2400
  with dps ≥ 44300)? The current result clears the 10⁻¹⁵ minimum target
  with 8+ orders of margin and exhausts the H6 B19+ basis at the
  PSLQ precision used.

- **Trivial relation in literal basis.** Anyone re-running PSLQ on the
  literal 18-member basis specified in Prompt 014 will see the trivial
  reflection identity. Recommend Prompt 014 (and any successor) replace
  the basis spec to omit `Gamma(1/3) Gamma(2/3) / (2 pi)` (since it is
  Q-equivalent to `sqrt(3)`, not a CS amplitude — the genuine D=−3 CS
  amplitude is `Omega_-3 = Gamma(1/3)^3 / (2 pi)`, encoded by the
  separate `Gamma(1/3)^3` and `pi` basis members).

- **No discrepancies vs Prompt 006.** Phase 006's empirical signal
  (A_lin → 6 with monotone |delta_lin| decrease, AEAL-logged) is fully
  consistent with this session's 11-param refit reaching 10⁻²³.

## What would have been asked (if bidirectional)

- "The saved CSVs don't have a y(N_ref=1320) row — should I (a) re-run
  cf_value to get one (~30s; risks bit-level mpmath drift), (b) drop
  to K_FIT=7 for a square 11×11 system, or (c) add Tikhonov?" → went
  with (b); cleanest, no fabrication, well-documented.
- "The literal B18 from Prompt 014 contains both `sqrt(3)` and the
  trivially-equivalent `Gamma(1/3) Gamma(2/3) / (2 pi)`. Drop one for
  the decisive run, yes?" → went ahead; documented both.
- "Does PASS_A_EQ_6_ONLY at 10⁻²³ close G5 / G16, or does the operator
  want the stretch 10⁻³⁰?"

## Recommended next step

If the operator accepts `PASS_A_EQ_6_ONLY` at 10⁻²³ for G5 / G16
closure, deposit `pcf2_v1.4_amendment.md` as PCF-2 §6 v1.4. If a
stretch-goal closure is required, run a Prompt 014b: regenerate y_n
at N up to 2400 (dps ≥ 44300) and refit at K_FIT=9 (full 13-param);
expected |delta| ~ 2400⁻¹⁰ ≈ 1.7 × 10⁻³⁴, comfortably below 10⁻³⁰.

## Files committed

```
sessions/2026-05-02/T25D-RETRY-13PARAM/
├── claims.jsonl                       (12 AEAL entries)
├── discrepancy_log.json               (K_FIT discrepancy)
├── fit_13param_results.json           (Phase B output)
├── halt_log.json                      (verdict + summary)
├── handoff.md                         (this file)
├── load_log.txt                       (Phase A hash-verify log)
├── output_hashes.json                 (sha256 of all artefacts)
├── pcf2_v1.4_amendment.md             (Phase F draft)
├── pslq_results.json                  (Phase D, 17-member basis)
├── pslq_results_18basis_literal.json  (Phase D, 18-member basis,
│                                       trivial relation traceability)
├── richardson_xcheck.json             (Phase E)
├── rubber_duck_critique.md            (self-review)
├── runner.stdout.log                  (full runner stdout)
├── t25d_retry_runner.py               (the runner)
├── tail_window_xcheck.json            (Phase C JSON)
├── tail_window_xcheck.tsv             (Phase C TSV)
├── unexpected_finds.json              (PSLQ trivial relation +
│                                       Phase E spec impedance)
└── verdict.md                         (one-liner + headline)
```

## AEAL claim count

12 entries written to `claims.jsonl` this session.
