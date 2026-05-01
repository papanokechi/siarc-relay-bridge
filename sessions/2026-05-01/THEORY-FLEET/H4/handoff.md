# H4 Handoff — Écalle median resurgence for `V_quad`

**Verdict:** `MEDIAN_RESURGENCE_GIVES_30+_DIGITS`

## Core conclusion

The `ζ* = 4/sqrt(3)` feature should be handled as a resurgent branch-point singularity, not as a Padé pole. Écalle/Sauzin alien calculus identifies the Stokes coefficient as the alien derivative amplitude at `ζ*`; median summation fixes the half-Stokes ambiguity. The existing 5000 coefficients at 250 dps should be enough for **30--50 digits** of the leading Stokes coefficient, with ~40 digits the central forecast.

## Recipe summary

1. Fix coefficient/Borel normalization and factorial shift.
2. Treat `A = 4/sqrt(3)` as exact.
3. Fit the branch exponent from high-order ratios.
4. Extract the amplitude from `a_n A^(n+β)/Γ(n+β)` via inverse-power asymptotics and sequence acceleration.
5. Cross-check by local Borel singular-germ fitting near `ζ*`.
6. Use the Stokes automorphism/median half-jump to fix sign and phase.

## Closed-form outlook

Closed form is plausible but not established. First PSLQ candidates should use powers of `2`, `3`, `π`, and gamma values at thirds/sixths. Catalan or `Γ(1/4)` is secondary.

## P-III(D6) implication

Resolving `op:cc-branch-resurgence` closes the `V_quad ↔ P-III(D6)` correspondence **only after** matching the extracted action, branch exponent, Stokes coefficient, and median sign to the isomonodromic Stokes data under an explicit normalization map.

## Aggregator cue

Fire T4. Do not require more coefficients initially. If extraction stalls near the old 7-digit wall, suspect normalization or branch-model error before declaring coefficient insufficiency.
