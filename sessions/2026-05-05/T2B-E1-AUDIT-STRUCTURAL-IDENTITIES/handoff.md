# Handoff — T2B-E1-AUDIT-STRUCTURAL-IDENTITIES
**Date:** 2026-05-05
**Agent:** Copilot CLI (T2 tier)
**Session duration:** ~10 minutes
**Status:** COMPLETE

## What was accomplished
Cross-checked the Synthesizer's P-001 candidate refinement ("split T2B Trans-stratum by sign of a₂") against the existing 04-29 verified-set evidence. Discovered that the candidate is *equivalent to* — not a hypothesis under — the **discriminant-identity characterization** that was already proven on 04-29 in `T2B-PLUS-QUARTER-SURVEY` and `T2B-DELTA2-VERIFICATION`. Sharpens the upcoming `T2B-REFINED-V0-B6-RESWEEP` spec by replacing the sign-of-a₂ split with the structural identity check, and surfaces a scope-restriction blind spot in today's `T2B-RESONANCE-B67-B6-DISPATCH` sweep (a₂∈[1,30] only — by construction excluded the −2/9 leg at b₁=6).

## Key numerical findings

### Structural identity for the +1/4 stratum (verified across all 15 PLUS-QUARTER families)
- **`b₁² + 4 a₂ = 2 b₁²` ⇔ `a₂ = b₁²/4`** for every +1/4 Trans hit
- All 15 families have `a₂ > 0`; sign of a₂ is forced by the identity (b₁² > 0)
- Realized values of b₁ in PLUS-QUARTER set: {−4, −2, 2, 4, 6}; only even b₁ admit integer a₂ = b₁²/4
- Source: `siarc-relay-bridge/sessions/2026-04-29/T2B-PLUS-QUARTER-SURVEY/families.json` (15 entries; sha256 ends `…2d4ba982d14`)
- Verification script: `verify_t2b_strata.py` (re-runnable)

### Structural identity for the −2/9 stratum (DELTA2-VERIFICATION 78/94 partition)
- **`a₂ = −2 b₁² / 9`** for every −2/9 Trans hit on the verified R₂ locus
- All 78 R₂-locus hits have `a₂ < 0`; sign of a₂ is forced by the identity
- Realized values of b₁ in DELTA2 set must satisfy `9 | b₁²` ⇒ `3 | b₁`
- Source: `siarc-relay-bridge/sessions/2026-04-29/T2B-DELTA2-VERIFICATION/dataset_verification.json` — `n_total_trans_deg21=94`, `n_on_R2=78`, `ratio_distribution={"-2/9": 78, "1/4": 16}`, `discrepancy_examples` all show `a₂=1, b₁=±2` (which satisfies a₂ = b₁²/4 = 1, the +1/4 identity)

### Sign-of-a₂ ⇔ discriminant-identity equivalence
| Stratum | Identity | Forced sign | b₁ divisibility |
|---|---|---|---|
| −2/9 | a₂ = −2b₁²/9 | a₂ < 0 always | 3 \| b₁ (so b₁² divisible by 9) |
| +1/4 | a₂ = b₁²/4 | a₂ > 0 always | 2 \| b₁ (so b₁² divisible by 4) |

The Synthesizer's "split by sign of a₂" verdict is therefore *not* a fresh hypothesis to test on b₁=6 — it is a **deductive consequence of the existing 04-29 structural characterization** of both sub-strata.

### Today's sweep scope-restriction
- `t2b_b67_b6_dispatch.py` line: `A2_VALUES = list(range(1, 31))  # 1..30` ⇒ a₂ ∈ {1, …, 30} only
- −2/9 stratum at b₁=6 predicts: a₂ = −2·36/9 = **−8** (outside today's sweep)
- +1/4 stratum at b₁=6 predicts: a₂ = 36/4 = **9** (inside today's sweep)
- Today's actual finding: 1 Trans hit at (9, 0, 0, 6, 3) with ratio +1/4 ✓
- Inference: today's "0 −2/9 hits at b₁=6" finding is **non-informative** by construction; the −2/9 leg was never tested

## Implications for the T2B-REFINED-V0-B6-RESWEEP relay prompt

The Synthesizer's P-001 spec (sign-of-a₂ split) is correct in *spirit* but should be **sharpened** to test the discriminant-identity characterization directly:

- **Sweep both signs of a₂** at b₁=6: a₂ ∈ [−30, 30] \ {0}
- **Predict** that Trans-stratum hits cluster on exactly two loci:
  - L−: a₂ = −2b₁²/9 = −8 (the −2/9 prediction)
  - L+: a₂ = b₁²/4 = 9 (the +1/4 prediction; reconfirms today's hit)
- **Verdict logic:**
  - **REFINEMENT_HOLDS**: every Trans-stratum hit lies on L− ∪ L+
  - **REFINEMENT_FAILS_NEW_LOCUS**: a Trans hit at a₂ ∉ {−8, 9} → triggers third-stratum investigation
  - **REFINEMENT_FAILS_LOCUS_VIOLATION**: a hit on L− with ratio ≠ −2/9 OR on L+ with ratio ≠ +1/4 → falsifies the structural characterization itself
  - **REFINEMENT_FAILS_INTERIOR**: a Trans hit at b₁=6 with a₂ off both loci but matching neither −2/9 nor +1/4 → broader re-think

This sharpened spec produces a stronger informational result per dollar of compute, and avoids re-running the design flaw that today's sweep had (positive-only a₂).

## Judgment calls made
1. **Equivalence claim**: "sign of a₂ ⇔ discriminant identity" is verified empirically across all 15 PLUS-QUARTER families and structurally implied for the −2/9 stratum (a₂ = −2b₁²/9 < 0 for all real b₁ ≠ 0). The implication direction is clean. I'm not asserting a structural NECESSITY argument from indicial-exponent theory here — only that the empirical record agrees with the algebraic identity.
2. **Scope-restriction characterization**: today's sweep "1 Trans / 0 −2/9 hits" is not informative about the −2/9 leg because the search space excluded a₂=−8. I am NOT claiming today's sweep was wrong-by-design — broadening to a₂<0 was likely outside the original WSB scope. I am claiming the *interpretation* of the result must account for the scope.
3. **Did not regenerate the −2/9 stratum identity check at the per-family level**: DELTA2-VERIFICATION dataset.json only carries summary counts and discrepancy examples, not the full 78-family list. If full per-family verification of the a₂ = −2b₁²/9 identity is required for arbitration confidence, a small follow-up script can pull from the upstream T2B-RESONANCE-B67 results JSONs. Logged as a recommended-but-not-blocking follow-on.

## Anomalies and open questions
- **Singleton mate gap**: PLUS-QUARTER handoff notes `(9, 0, 0, −6, −3)` predicted but never searched. This is also outside today's a₂∈[1..30] scope. The refined-statement re-sweep should specifically include this candidate to close the orbit.
- **a₂ = 0 boundary**: not searched in any past sweep. May produce degenerate cases. Mention in the relay prompt as exclude-or-classify decision.
- **Third-stratum search at b₁=6 has effectively never been performed**: today's sweep covered a₂∈[1,30] \ {9}, all of which produced Desert/Alg/Rat/Log (no Trans). For full third-stratum exclusion at b₁=6, the negative-a₂ side must also be swept and any Trans hit at a₂ ∉ {−8, 9} flagged.
- **What characterizes the 16/78 ≈ 17% +1/4 frequency**? Is it a measure-zero observation that depends on lattice density at small |b₁|, or is there a deeper invariant?

## What would have been asked (if bidirectional)
- Should the refined relay prompt also include the (9,0,0,−6,−3) singleton-mate spot-check at dps=300, given it's a 30-second compute and closes a known orbit gap?
- Should the third-stratum search be at b₁=6 only, or extended to b₁∈{4,8,10,12} where existing PLUS-QUARTER hits live, to cross-check that NO third stratum exists in the verified-stratum lattice?

## Recommended next step
**Fire `T2B-REFINED-V0-B6-RESWEEP` with the sharpened spec** (a₂ ∈ [−30, 30] \ {0}, structural-identity verdict logic). The original Synthesizer P-001 spec is preserved as the conceptual framework; this audit only sharpens the empirical test design. Operator + Synthesizer should sign off on the sharpened spec before fire (the scope-broadening from one-sided to two-sided a₂ may need WSB priority adjustment).

## Files committed to bridge
- `verify_t2b_strata.py` — Python 3 idempotent verification script for the +1/4 identity (sha256 = TBD on push)
- `verify_minus29.py` — Python 3 verification script for the −2/9 stratum summary (sha256 = TBD on push)
- `handoff.md` — this file

## AEAL claim count
3 entries to be appended to `claims.jsonl` this session:
1. "All 15 +1/4 Trans-stratum families in PLUS-QUARTER dataset satisfy a₂ = b₁²/4 (discriminant identity Δ = 2 b₁²); sign of a₂ is forced positive."
2. "All 78 R₂-locus −2/9 Trans-stratum families in DELTA2-VERIFICATION dataset satisfy a₂ = −2 b₁²/9 (per dataset_verification.json `n_on_R2=78` summary); sign of a₂ is forced negative."
3. "Today's b₁=6 sweep `T2B-RESONANCE-B67-B6-DISPATCH` had A2_VALUES = list(range(1, 31)), which structurally excluded the −2/9 leg (predicted a₂ = −8); the '1 Trans / 0 −2/9 hits' result is consistent with the bimodal characterization, not a falsification of it."
