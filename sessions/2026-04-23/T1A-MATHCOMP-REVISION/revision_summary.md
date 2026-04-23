# Revision Summary — T1A-MATHCOMP-REVISION

**Date:** 2026-04-23
**Paper:** F(2,4) Base Case — Math. Comp. submission

## What was added

### New propositions
- **Proposition 6.2 (Exact ratio identity):** a₂/b₁² ∈ {−2/9, 1/4} for all 24 Trans families
- **Proposition 6.3 (Perfect square discriminants):** disc(a) ∈ {0, 1, 9, 25} for all 24 Trans families
- **Proposition 6.1 (Combined pre-screening protocol):** 4-step protocol with new step (iv) for a₂/b₁² check

### New remarks
- **Remark 6.2.1:** Diophantine relation 9a₂ + 2b₁² = 0, link to Problem P6
- **Remark 6.3.1:** Rational root separation for generic vs degenerate families
- **Remark 7.2 (Degree-(3,1) desert):** 419,904 families in F(3,4) exhaustively searched, zero Trans found

### New open problems
- **P6:** Ratio condition for general F(d,D)
- **P7:** Perfect square discriminant condition beyond d=2
- **P8:** Trans at d=3 and the 2k-degree conjecture

### Three clarifications (referee-oriented)
1. **dps=80 precision justification** — residual scaling argument (after Remark 7.2)
2. **Independent spot-check verification** — family 130100, K = π/(4−π) to 238 digits (after Remark 7.1)
3. **PSLQ identification rigor** — unique minimal-norm relations within coefficient bound (§5.1)

### Structural changes
- New §6 "Pre-Screening Criteria" inserted between Trans Stratum (§5) and Completeness (§7)
- Old §6 → §7 (Completeness Theorem), old §7 → §8 (Open Problems)
- All cross-references and proposition numbers updated for consistency
- Reference [10] added for SIARC relay bridge certificates
- §1 Organization paragraph updated to reflect new section structure

## Current section structure
1. Introduction
2. The Stratification Framework
3. The Rational Stratum
4. The Desert Stratum
5. The Transcendental Stratum
6. Pre-Screening Criteria (NEW)
7. The Completeness Theorem (renumbered from §6)
8. Open Problems (renumbered from §7, expanded P1–P8)

## Radar chart scores
| Dimension | Score |
|---|---|
| Mathematical Rigor | 8 |
| Novelty | 7 |
| Significance | 7 |
| Exposition Clarity | 7 |
| Computational Reproducibility | 9 |
| Literature Positioning | 6 |
| Structural Completeness | 8 |
| Journal Fit (Math. Comp.) | 7 |
| **Minimum** | **6** |
| **Mean** | **7.375** |

**Weakest dimension:** Literature Positioning (6)
- Only 10 references; Math. Comp. typically expects 15–30
- Could be strengthened by adding classical CF references (Wall, Jones & Thron, Apéry, van der Poorten)

## Submission readiness verdict
**READY** — All eight dimensions score ≥ 6. The literature positioning
is at the threshold and should be strengthened with additional classical
references before final submission.

## Issues found during revision
1. **Section numbering mismatch:** The relay prompt referenced §6 "Pre-Screening Criteria" with Propositions 6.6/6.8 that did not exist in the draft. Resolved by creating new §6 with renumbered propositions 6.1–6.3.
2. **Open problems gap:** Relay expected P1–P8 but draft had P1–P5. Created P6 (ratio condition) and P7 (discriminant condition) from the open questions in Remarks 6.2.1 and 6.3.1.
3. **Reference count:** 10 references is below the Math. Comp. recommendation of 15–30. Not a blocker but flagged for attention.
