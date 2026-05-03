# Phase D — Verdict Aggregation (Dispatch 4)

**Dispatch 4 timestamp:** 2026-05-03 (re-fire 4)

## Inputs (signals)

| Phase | Signal | Source |
|-------|--------|--------|
| A*    | `A_DIRECT_IDENTITY_d10` | cached; SHA-256 re-validated this dispatch |
| C.0   | `C0_GATE_PASS` (re-issued with new Wasow hash `f59d6835…a5fd`) | `phase_c0_gate_pass.md` |
| C.1   | `C_WASOW_UNIFORM` | `phase_c1_wasow_verification.md` |
| C.2   | `C_BIRKHOFF_UNIFORM` (formal half) + Borel half re-targeted to Wasow §19 (uniform) | `phase_c2_birkhoff_verification.md` (dispatch 3, retained) |
| C.3   | `C_LITERATURE_UNIFORM` | `phase_c_summary.md` |

## Verdict ladder traversal (Prompt 018 §2 step 7 / §3)

The verdict ladder in Prompt 018 §3 lists, in order of preference:

1. **`UPGRADE_FULL`** — A* identity holds AND literature uniform in d (no cap).
2. `UPGRADE_PARTIAL_d_LE_d*` — A* identity holds AND literature bounded at some d* < ∞.
3. `UPGRADE_REJECTED` — A* identity fails OR literature contradicts the construction.
4. `HALT_*` — gate failure or unresolved discrepancy.

Phase A* identity holds (cached `A_DIRECT_IDENTITY_d10`, 18/18 pass over
d ∈ {2..10}, SHA-validated this dispatch).
Phase C.3 produces `C_LITERATURE_UNIFORM` (no d-cap).
Hence **rung 1** matches: **`UPGRADE_FULL`**.

## Verdict

```
UPGRADE_FULL
```

## What this closes

| Item | Pre-dispatch-4 status | Post-dispatch-4 status |
|------|------------------------|-------------------------|
| **G1** | open (gap proposition `A ∈ [ψ_lower(d), ψ_upper(d)]` unproven) | **closed** — direct identity holds at all d ∈ {2..10}; literature confirms framework extends uniformly to all d ≥ 2; gap collapses to identity |
| **G2** | partial (Phase A symbolic match at d=2,3,4) | **strengthened** — extended to d=10 with no breakage; uniform in d |
| **M2** (literature module) | partial (formal-half theorem from Birkhoff §2; Borel-half open) | **done** — Wasow §19 Thm 19.1 + eq. (19.3) supply the general-case canonical form and Borel content uniformly in q ≥ 0 |
| **M9** gating set | `{M2, M4, M6}` | `{M4, M6}` — M2 is now done; M9 unblocks once M4 (numerical residual at higher d) and M6 (cross-paper consistency) close |

## D2-NOTE v2 disposition

Per Prompt 018 §2 Phase E logic, `UPGRADE_FULL` triggers a D2-NOTE v2
draft. The draft is produced by Phase E (next).

Note: the d=10 Phase A* sweep, Wasow §19 keystone Theorem 19.1, and the
re-targeting of Prompt 018's Borel-content spec from Birkhoff §§2-3 to
Wasow §19 eq. (19.3) — these are the three new substantive contributions
of dispatch 4 over the dispatch-3 partial result.

## Anomalies for synthesizer-side review

1. **Vocabulary equivalence**: Wasow uses "shearing transformations" +
   "characteristic exponents"; Prompt 018 spec uses "Newton polygon edges"
   + "characteristic roots". Treated as substantively equivalent;
   recommend confirming in synthesizer review.
2. **PCF d ↔ Wasow q mapping**: `q = (d+2)/2`. For odd d this is half-integer;
   Wasow §19.3 handles fractional q via independent-variable ramification
   `x = const · t^p`. Mathematically tight, but synthesizer should confirm
   the half-integer case is not a special edge condition the SIARC stratum
   needs to flag separately.
3. **Spec error on Birkhoff §§2-3 Borel content**: dispatched 4 records
   the negative finding (not in §§2-3) and the positive finding (in
   Wasow §19 eq. 19.3). Synthesizer should update Prompt 018 spec for
   future re-fires (or downstream prompts) to cite Wasow §19 directly.
4. **Vision-based PNG transcription as evidence type**: dispatch 4 uses
   `vision_transcription` (with PDF SHA + page number + verbatim ≤30-word
   quote) rather than `tesseract_ocr` or `embedded_text_layer`. AEAL-honest;
   reproducible by re-loading the same PNGs. Synthesizer-side note: this
   sets precedent for future image-only-PDF anchors and should be added to
   the AEAL evidence-type vocabulary if not already.
5. **No halt this dispatch.** All gates pass. Compare with dispatches 1-3
   which all halted on Phase C.0 path mismatch (1, 2) or Wasow-PDF
   image-only / wrong-section (3).

## Verdict signal (final)

`UPGRADE_FULL`
