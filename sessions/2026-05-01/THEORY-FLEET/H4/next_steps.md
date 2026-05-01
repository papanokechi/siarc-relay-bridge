# H4 Next Steps — T4 median-resurgence extraction

## Recommended T-move

Fire **T4: Écalle median resurgence on `V_quad`**.

## Recipe to execute later (no code executed in this theory pass)

1. **Freeze conventions**
   - Record the exact Birkhoff coefficient normalization.
   - Record the exact Borel transform convention and factorial shift.
   - Normalize the adjacent alien sector so its leading coefficient is known, preferably 1.

2. **Use exact action**
   - Set `A = ζ* = 4/sqrt(3)` from Session G/G2.
   - Do not refit `A`; use it as exact input.

3. **Fit branch exponent**
   - Use high-order ratio estimators `A*a[n+1]/a[n]-n`.
   - Test half-integer, rational, and algebraic-logarithmic drift models.
   - If `log(n)/n` drift appears, include a logarithmic companion in the singular ansatz.

4. **Extract the Stokes coefficient**
   - Form `R_n = a_n*A^(n+beta)/Gamma(n+beta)`.
   - Fit inverse-power tails over multiple late-order windows.
   - Richardson/Weniger accelerate to `n = infinity`.
   - Convert the limit to `S_A` using the documented `2πi` and adjacent-sector normalization.

5. **Cross-check locally in the Borel plane**
   - Use Padé/conformal continuation only near `ζ*`.
   - Fit the singular germ and compare the amplitude to the large-order estimate.
   - Verify the lateral discontinuity and median half-jump sign.

6. **Closed-form test only after stability**
   - Require at least 30 stable digits before PSLQ.
   - Candidate basis priority: `π`, powers of `2,3`, `Γ(1/3)`, `Γ(2/3)`, `Γ(1/6)`, `Γ(5/6)`.
   - Try PIII(D6) monodromy gamma/trigonometric bases next.
   - Treat Catalan/`Γ(1/4)` as low-priority unless new geometry indicates `τ=i`.

7. **P-III(D6) closure test**
   - Write an explicit normalization map between `V_quad` and PIII(D6) variables.
   - Compare branch exponent, action, Stokes coefficient, and median sign convention.
   - Declare correspondence closed only if all four agree.

## Success thresholds

- **Green:** ≥30 stable digits across windows and local Borel cross-check; proceed to PIII(D6) matching.
- **Gold:** ≥40 stable digits plus successful PSLQ in a gamma-at-thirds/sixths basis.
- **Red:** ≤10 stable digits after large-order extraction; inspect normalization, logarithmic terms, and secondary singularities before requesting more coefficients.
