# Handoff — T36-S2-EXTRACTION

**Date:** 2026-05-02
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~25 minutes
**Status:** HALTED  (verdict: `HALT_T36_S2_RICHARDSON_DIVERGED`,
                     secondary key `T36_S2_CROSSMETHOD_MISMATCH`)

## What was accomplished

The Phase A load + sanity check passed for all four T35 cached CSVs
(V_quad, QL15, QL05, QL09; dps=250, N=2000).  The Phase B leading-
term subtraction was performed using T35's reported `C` and
`zeta_*` per rep (T35-consistent convention; see rubber-duck critique
for the deviation from prompt-016's literal `(C/2pi)` factor).
The Phase B convention check `a_n / (C * Gamma(n) * zeta_*^(-n)) -> 1`
**failed** the prompt's 60-digit target across all four reps,
agreeing with 1 only to ~3 digits at n=1500..1900 (QL09 ~5.4 digits).
The Phase C residual Richardson + LSQ on `R_n := r_n * (2 zeta_*)^n /
Gamma(n)` **diverged** for all four reps (cross-method digit
agreement ~10^-15, R_inf magnitudes ~10^654 — manifest noise
amplification, NOT an S_2 measurement).  The runner halted with key
`T36_S2_CROSSMETHOD_MISMATCH` per its halt logic.

A post-halt diagnostic (`extract_a1.py`) measured the **first
polynomial-in-1/n correction `a_1`** per rep to 3-4 digits via an
endpoint estimator on `s_n := n * (a_n / a_n_lead - 1)`.

## Key numerical findings

- **Convention-check ratios** (T36_S2_RICHARDSON_DIVERGED root cause),
  agree-with-1 digits at n=1900, in `t36_runner.py`, dps=300:
  V_quad: 3.111;  QL15: 2.886;  QL05: 2.389;  QL09: 5.557.
  These would need to be ~60 for the prompt's S_2 extraction
  recipe to apply.

- **First polynomial correction a_1** (3-4 digits, in `extract_a1.py`,
  dps=280):
  - V_quad (neg, A=3, Δ_b=-11):  a_1 ≈ **-1.47165**
  - QL15   (neg, A=3, Δ_b=-20):  a_1 ≈ **-2.47108**
  - QL05   (pos, A=4, Δ_b=+8):   a_1 ≈ **+7.76157**
  - QL09   (pos, A=4, Δ_b=+1):   a_1 ≈ **-0.00527** (anomalously near zero)

- **No S_2 measurement** is carried in this session.  The Phase C
  R_inf values are noise; they are explicitly flagged as such in
  `halt_log.json` and excluded from `claims.jsonl`.

- AEAL claim count: 11 entries in `claims.jsonl` (4 convention-check
  failures, 1 phase-C divergence diagnostic, 4 a_1 endpoint
  measurements, 1 structural finding, 1 verdict).

## Judgment calls made

1. **Convention deviation from prompt 016 §2 Phase B literal text.**
   The prompt writes `a_n_lead = (C / 2pi) * Gamma(n) * zeta_*^(-n)`,
   under which the convention check would yield ratio → 2π (not 1).
   We adopted the T35-consistent convention `a_n_lead = C * Gamma(n)
   * zeta_*^(-n)` so the test could be informative; documented in
   `rubber_duck_critique.md`.  This is the only judgement call that
   touches the runner's logic.

2. **Soft handling of the convention-check failure.**  The prompt's
   `T36_CONVENTION_MISMATCH` halt clause is worded for sign/phase
   convention errors ("global factor of -1 or i"), not for 1/n decay
   to 1.  We logged each rep's failure under `unexpected_finds.json`
   and let the runner proceed to Phase C; Phase C's Richardson then
   diverged honestly and triggered `T36_S2_CROSSMETHOD_MISMATCH`.
   On reflection, the halt should be relabelled
   `T36_S2_RICHARDSON_DIVERGED` with the underlying cause
   "polynomial-in-1/n corrections to leading"; we made that
   relabelling explicit in `halt_log.json`.

3. **Replaced the runner's Phase-C noise outputs in `claims.jsonl`
   with honest a_1 measurements + a structural-finding claim.**  The
   Phase-C R_inf values (~10^654) are not meaningful AEAL entries
   under any honest reading; emitting them would be an interpretive
   overclaim.  We retained the cross-method digit-agreement diagnostic
   (which legitimately documents the divergence) and added the
   `extract_a1.py` measurements + the structural-finding claim about
   polynomial corrections being non-zero.

4. **Skipped the optional Phase F (Q18 basis-convention probe).**  The
   probe would re-run QL09 with `c = -2/sqrt(alpha)` to test whether
   QL09's negative-C anomaly is a basis artefact.  Given that Phase C
   diverged for a structural reason orthogonal to Q18, the probe
   would not have helped and was deferred.

## Anomalies and open questions

**1.  Polynomial corrections to leading Birkhoff are non-zero in
d=2 PCFs.**  T36 finds `a_1 ≈ -1.47, -2.47, +7.76, -0.005` for the
four reps.  T35's measured `beta_R = 0` (G19 row, "no Gamma-shift
universal at d=2") was correctly bounding the LEADING Gamma argument
only.  G19 should be reworded to make this explicit: it does not
imply that the polynomial coefficients `(a_1, a_2, ...)` of the
leading amplitude vanish.  Whether the picture-revised v1.8 §5 G19
text needs editing is a synthesizer call.

**2.  QL09's a_1 is anomalously near zero (~ -0.005).**  The other
three reps have a_1 of magnitude 1 to 8.  This is a NEW anomaly,
distinct from but possibly correlated with QL09's existing T35
anomaly (negative leading C).  We do not interpret it; we record it.

**3.  a_1 does NOT cleanly partition by side at this 3-digit
precision.**  Negative-side reps both have negative a_1 of order
-1 to -2.5; positive-side reps have +7.76 (QL05) and ~ -0.005 (QL09).
Whether a_1 partitions cleanly at higher precision (or whether the
ratio `a_1 / C` does, or whether some other invariant does) is open.

**4.  Q18 (sign-of-C basis convention).**  Untouched in this session.
The polynomial-correction discovery layered on top adds a second
basis-convention concern: are the `a_k` themselves basis-independent?
Probably yes (they are coefficients of the formal Birkhoff series in
a fixed expansion variable u), but worth noting.

**5.  Q19 status.**  T36 does NOT contradict Q19 at the leading
Gamma-argument level.  It does sharpen Q19: "beta_R = 0" is a
property of the leading exponent, not of the polynomial coefficients
that follow.

## What would have been asked (if bidirectional)

- "The prompt's `a_n_lead = (C/2pi) * Gamma(n) * zeta_*^(-n)` formula
  contradicts T35's `S_1 = 2 pi i C` calibration.  Should I follow the
  literal prompt formula (and halt every rep on convention mismatch)
  or the T35-consistent one?"
- "After observing the 1/n decay of the convention check, should I
  pivot to a polynomial-correction-aware S_2 extraction within the
  budget, or halt cleanly?  Halting is the AEAL-disciplined choice;
  pivoting would deliver an S_2 estimate but extends the prompt
  scope."  (Halted, per discipline.)

## Recommended next step

**Prompt 018 should be `T37-S2-EXTRACTION-POLYNOMIAL-AWARE`**, with
the following structure:

1. Use the SAME cached T35 dps=250 / N=2000 CSVs (read-only).
2. For each rep, joint-fit `(C, a_1, a_2, ..., a_K)` with K ~ 40 via
   constrained-LSQ on `T_n = a_n * zeta_*^n / Gamma(n)` over a window
   where the next-ladder-rung signal is below the dps-250 floor,
   e.g. n in [200, 600].
3. Subtract the FULL polynomial-leading expansion `C * (1 + a_1/n +
   ... + a_K/n^K) * Gamma(n) * zeta_*^(-n)` from a_n.
4. Apply Richardson on the resulting r_n at the 2 zeta_* scale; this
   should now converge if the polynomial subtraction is precise enough.
5. Verdict ladder per prompt-016 §2 Phase E.

If joint-fit precision is insufficient, the alternative is to extend
the cached series itself: re-run T35's recurrence at dps=400, N=5000.

## Files committed

(under `siarc-relay-bridge/sessions/2026-05-02/T36-S2-EXTRACTION/`)

- `representatives.json`              (copied from T35; identical)
- `T35_stokes_multipliers_per_rep.csv` (copied from T35; reference C, zeta_*)
- `t36_runner.py`                     (main runner; halted at Phase C)
- `t36_run.log`                       (full runner log)
- `extract_a1.py`                     (post-halt a_1 diagnostic)
- `extract_a1.stdout.log`             (a_1 diagnostic log)
- `a1_polynomial_corrections.csv`     (per-rep a_1 measurements)
- `discrimination_certificate.md`     (HALT-state certificate)
- `rubber_duck_critique.md`           (convention deviation + Phase C divergence)
- `claims.jsonl`                      (11 AEAL entries)
- `halt_log.json`                     (halt key + diagnostic detail)
- `discrepancy_log.json`              ({})
- `unexpected_finds.json`             (4 convention-check anomalies, by rep)
- `handoff.md`                        (this file)

## AEAL claim count

11 entries written to `claims.jsonl` this session.
