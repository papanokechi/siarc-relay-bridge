# Handoff -- BOREL-CHANNEL-K-SCAN
**Date:** 2026-05-01
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~25 minutes
**Status:** COMPLETE

## What was accomplished
Ran the K-extension diagnostic from BOREL-CHANNEL-5X (V_quad K-scan) on
the two MARGINAL hits flagged at K=12: QL15 (P-V, residual 9.08e-5) and
QL26 (P-III, residual 2.82e-5).  Same grid as V_quad
(K, M_pade, depth, dps) in {(12,5,200,2200), (16,7,240,3000),
(20,9,280,4000), (24,11,320,5000)}; same v3 pipeline (borel_channel.py
imported verbatim from BOREL-CHANNEL-5X).  Independently locked the
publication-ready WKB-exponent table (alpha_pred = A - 2*log(c_b) +
log|c_a| vs alpha_obs) for all 6 Delta<0 degree-2 PCFs at >= 13 matching
digits.

## Key numerical findings

### Side-by-side K-scan (canonical artefact pattern)

| K | V_quad residual | V_quad rho_* | QL15 residual | QL15 rho_* | QL26 residual | QL26 rho_* |
|---|-----------------|--------------|---------------|------------|---------------|------------|
| 12 | 7.18e-3 (PIII) | 2.175 | 9.08e-5 (PV)  | 3.391 | 2.82e-5 (PIII) | 1.800 |
| 16 | 4.95e-3 (PIII) | 2.999 | 1.17e-5 (PIII)| 1.239 | 1.97e-3 (PIII) | 3.721 |
| 20 | 1.04e-2 (PVI)  | 3.648 | 6.61e-4 (PV)  | 5.185 | 1.36e-3 (PIII) | 4.292 |
| 24 | 9.92e-2 (PVI)  | 4.587 | 5.07e-4 (PIII)| 3.815 | 4.48e-2 (PV)   | 4.753 |

- **QL15: ARTEFACT.**  Residual fails to stay <= 1e-4 (jumps to 6.6e-4
  at K=20, 5.1e-4 at K=24); best-fit equation flips P-V <-> P-III <-> P-V <->
  P-III between consecutive K; Pade nearest-pole radius non-monotone with
  spread 3.95 (3.39 -> 1.24 -> 5.19 -> 3.82).
- **QL26: ARTEFACT.**  Residual GROWS by three orders of magnitude
  across K (2.8e-5 -> 2.0e-3 -> 1.4e-3 -> 4.5e-2); Pade nearest-pole
  radius monotone diverging (1.80 -> 3.72 -> 4.29 -> 4.75, spread 2.95);
  best-fit equation flips P-III -> P-III -> P-III -> P-V.
- **No structural split**: QL15 and QL26 behave the same way as V_quad.
- **Trans-series h_k coefficients are stable to 14+ digits across K**
  for both QL15 and QL26 (h_1, h_2, h_3 unchanged at 14 digits between
  K=12 and K=24); the Borel-channel signal extraction is reliable; the
  breakdown is downstream in the Pade-Borel resummation.
- **Trans-series LSQ residual on log|delta_n|** improves geometrically
  with K for both families (QL15: 3.6e-24 -> 5.8e-41; QL26: 5.1e-23 ->
  3.1e-40), confirming the channel definition itself is well-posed.

### WKB-exponent table (publication-ready for PCF-1 v1.3)

| Family   | Delta | A | alpha_pred (= A - 2log(c_b) + log|c_a|) | alpha_obs       | match digits |
|----------|-------|---|------------------------------------------|-----------------|--------------|
| V_quad   | -11   | 4 | 4 - 2 log 3            = 1.80277542266378062  | 1.8027754226638 | 13 |
| QL01     | -3    | 3 | 3                      = 3.0                  | 3.0             | exact |
| QL02     | -4    | 3 | 3 + log 2              = 3.69314718055994531  | 3.6931471805599 | 13 |
| QL06     | -7    | 3 | 3 - 2 log 2            = 1.61370563888010938  | 1.6137056388801 | 14 |
| QL15     | -20   | 3 | 3 - 2 log 3            = 0.802775422663780617 | 0.80277542266378| 15 |
| QL26     | -28   | 3 | 3 - 2 log 4 + log 3    = 1.32602356642832845  | 1.3260235664283 | 13 |

LaTeX-ready version: `wkb_exponent_table.tex`.

## Copy-paste decision matrix (ready for Claude / next relay)

```
QL15  K-scan diagnosis: ARTEFACT
  - residual_max over K = 6.61e-4 > 1e-4 cutoff (decision rule fails)
  - rho_star_abs spread = 3.95 > 0.5 cutoff (decision rule fails)
  - best-fit equation flips P-V <-> P-III, signature of wandering Pade

QL26  K-scan diagnosis: ARTEFACT
  - residual GROWS by 3 orders of magnitude (2.82e-5 -> 4.48e-2)
  - rho_star_abs spread = 2.95, monotone divergent
  - K=12 +1.800 positive-real "outlier" pole disappears at K=16,20

V_quad (reference) diagnosis: ARTEFACT (carried over from Session E)

FINAL FLAG: BOREL CHANNEL CONFIRMED ANOMALOUS
  No Delta<0 family in {QL01, QL02, QL06, V_quad, QL15, QL26} admits a
  genuine Borel-channel Painleve reduction.  The channel must be
  re-specified (recommended: connection-coefficient channel of the
  underlying difference equation).
```

## Judgment calls made
1. **h cross-check at K=24 captured by re-running the full pipeline
   one extra time per family**, since `borel_probe` already iterates
   `h in {0.1, 0.05, 0.025}` internally and stores the per-h
   residual_validate in `fit_results`.  The extra re-run is redundant
   in compute but doubled the K=24 fit_results record so
   h-independence can be inspected from `*_k_scan.json`.  All three
   h-values give residuals within a factor of ~2 of each other at
   K=24 (well below the artefact threshold), so design-block step
   size is not driving the artefact.

2. **Decision rule cutoffs** taken verbatim from the prompt: residual
   <= 1e-4 across K AND rho_spread < 0.5 -> CONFIRMED.  QL15 satisfies
   the residual cutoff at K=12 and K=16 only, and the rho_spread cutoff
   at no K subset of size >= 3.  No tier-juggling.

3. **WKB closed-form for V_quad uses A=4** (the V_quad recurrence has
   degree-2 b and degree-0 a, i.e. (deg b - deg a) = 2 instead of 1
   for the QL family; the leading log q_n ~ 2 log(n!) gives A=4).
   For QL01..QL26, A=3 is the (1+2)*log(n!)/n leading term (degree-1
   a, degree-2 b).  This matches the closed-form predictions in
   BOREL-CHANNEL-5X/summary.json to >= 13 digits.

## Anomalies and open questions
1. **QL15 K=16 residual dip to 1.17e-5** (better than K=12) before
   jumping to 6.6e-4 at K=20.  This is the only datum across the
   3-family K-scan that even briefly looks like signal.  However,
   the best-fit equation flips P-V -> P-III at the K=12 -> K=16 step,
   the Pade nearest-pole radius drops from 3.39 to 1.24, and the
   K=20 jump back to 6.6e-4 with rho=5.19 wipes out any monotone
   trend.  Documented in unexpected_finds.json -- Pade artefact, not
   real signal.

2. **QL26's K=12 positive-real pole at rho=+1.800** (the unique
   anti-Stokes outlier flagged by Session E) does NOT survive K-scan:
   it disappears at K=16, K=20 and reappears at a different location
   (rho=+5.189) at K=24.  This adds another data point that the K=12
   Borel-plane geometry of QL26 is a [5/5] Pade truncation artefact.

3. **The trans-series channel itself remains the publication-ready
   positive result.**  All 6 Delta<0 families' (A, alpha) leading
   exponents match the WKB closed form A - 2 log(c_b) + log|c_a| to
   >= 13 digits.  The negative result (no Borel-channel Painleve
   reduction) is downstream of this universal positive.

4. **Open: is there a different formal-series channel that DOES yield
   a Painleve reduction?**  The recommended next direction is the
   connection-coefficient channel of the underlying 2nd-order linear
   difference equation, where Stokes constants are intrinsic invariants
   of the pair (a_n, b_n) and not artefacts of any particular Pade
   truncation in the Borel plane.

## What would have been asked (if bidirectional)
1. Should QL15's K=16 residual dip (1.17e-5) be re-checked at finer
   K resolution {13, 14, 15} to rule out a missed isolated convergence
   (would take ~15 additional minutes)?  Default: no, the K=20 jump
   already rules out monotone signal.
2. For PCF-1 v1.3, should the WKB-exponent table include the rho_*
   axis classification (negative-real Stokes / off-axis / positive-real)
   as a fourth column?  Default: no, the axis class is K-dependent and
   not stable across the K-scan.

## Recommended next step
**PCF-1-V1.3-WKB-LOCK**: a small downstream session that drops
`wkb_exponent_table.tex` into `tex/submitted/pcf1_main.tex` (or the
v1.3 working copy), updates the corresponding text paragraph to cite
"Conjecture A part (iv) on Borel-channel Painleve reduction" as
**FALSE in this channel** with explicit reference to BOREL-CHANNEL-5X
and BOREL-CHANNEL-K-SCAN, and re-builds.  No new computation required.

After v1.3 is locked, the natural follow-up is **CONNECTION-CHANNEL-POC**:
build a small prototype of the connection-coefficient channel for V_quad
(known P-III(D6) reduction) as a gate, and apply to the 5 quadratic-limit
families.

## Files committed
- ql15_k_scan.py             (QL15 K-extension scan)
- ql26_k_scan.py             (QL26 K-extension scan)
- ql15_k_scan.json           (QL15 grid + h cross-check at K=24)
- ql26_k_scan.json           (QL26 grid + h cross-check at K=24)
- ql15_k_scan.log, ql26_k_scan.log
- aggregate.py               (side-by-side + decision rule + final flag)
- aggregate.log
- k_scan_summary.json        (4-row table per family + V_quad reference + verdicts)
- build_wkb_table.py         (WKB closed-form vs alpha_obs)
- wkb_exponent_table.tex     (LaTeX table for PCF-1 v1.3)
- wkb_exponent_table.json    (machine-readable WKB table)
- claims.jsonl               (10 AEAL entries)
- halt_log.json              (no halt triggered)
- discrepancy_log.json       (empty)
- unexpected_finds.json      (3 informational items)
- handoff.md                 (this file)

## AEAL claim count
10 entries written to claims.jsonl this session.
