MEDIAN_RESURGENCE_GIVES_30+_DIGITS

# Verdict

Median resurgence should break the observed ~7 digit Padé-Borel-Laplace wall for `V_quad` at
\[
\zeta_* = 4/\sqrt{3}.
\]
The wall is consistent with slow global approximation to a branch cut, not with lack of information in the coefficients. Écalle/Sauzin alien calculus gives the correct local object: the alien derivative at `ζ*`, whose coefficient is the desired Stokes constant. Median summation supplies the half-Stokes prescription needed for an unambiguous real resummation.

With 5000 coefficients at 250 dps and `ζ*` fixed to 200 digits, the expected extraction precision is **30--50 digits**, with **~40 digits** the central forecast. The method should fit the branch exponent, then extract the alien amplitude from the large-order tail and cross-check it by local Borel singular-germ fitting.

I do **not** recommend the stronger closed-form verdict yet. Gamma products at thirds/sixths are plausible candidates, but literature alone does not prove the Stokes constant has such a form.

Resolving `op:cc-branch-resurgence` would close the `V_quad ↔ P-III(D6)` correspondence **conditionally**: the extracted Stokes coefficient must match the PIII(D6) isomonodromic Stokes/monodromy datum under a documented normalization map.
