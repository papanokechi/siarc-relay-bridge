# H3 next steps — algorithmic verification recipe

## Goal

Decide whether the SIARC d = 2 PCF anomaly is a true two-branch Painlevé reduction or a Riccati/linear recurrence with Painlevé-like asymptotics.

## Required test set

Select representative PCF-1 d = 2 families:

1. at least 3 with `Delta_2 < 0`,
2. at least 3 with `Delta_2 > 0`,
3. any available `Delta_2 = 0` or near-zero boundary cases.

## Step-by-step recipe

1. **Write the recurrence.** For each family form

   ```text
   U_n = [[b(n+1), a(n+1)], [1, 0]],
   delta_{n+1} = b(n+1) delta_n + a(n+1) delta_{n-1}.
   ```

2. **Normalize the continuum scaling.** Put `n=t/epsilon`, gauge out the dominant WKB exponential, and derive the scalar ODE or first-order matrix connection that approximates the recurrence.

3. **Classify singularities.** Compute regular/irregular singular points, Poincaré ranks, local monodromy exponents, and whether finite singularities are apparent. This decides the candidate class:

   - four regular singularities -> PVI / D4^(1),
   - one confluence -> PV / D5^(1),
   - two irregular directions -> PIII(D6) / D6^(1),
   - apparent or resonant collapse -> Riccati/P-trivial or PIII(D7/D8).

4. **Construct Sakai data.** Build a two-dimensional birational map using `(ratio, accessory parameter)` or equivalent Lax variables. Locate base points, blow them up, and compute the anti-canonical divisor/root type. This is the decisive classification step.

5. **Sigma-form residual tests.** Fit the normalized continuum variable to Jimbo--Miwa--Okamoto sigma forms for PV and PIII(D6). Repeat for decreasing `epsilon`; require stable monodromy parameters and residual decay at the predicted WKB order.

6. **Entropy/Riccati test.** Compute degree growth of the induced map. Linear growth/zero entropy with no nontrivial two-dimensional lift means Riccati/Painlevé-trivial rather than generic discrete Painlevé.

## Expected outcomes

- `Delta_2 < 0`: PIII(D6) residual should dominate after confluence normalization; transfer multipliers should be complex-conjugate/oscillatory.
- `Delta_2 > 0`: PV residual should dominate unless apparentness collapses the branch to Riccati; transfer multipliers should be real split.
- `d >= 3`: if the generic PVI story is correct, the analogous lift should show four regular singularities and D4^(1) surface type.

## Falsification criteria

Reject the two-branch hypothesis if both discriminant signs have the same Sakai surface type and the same best sigma-form residual after normalization, or if all tested cases remain linearisable Riccati leaves with no nontrivial two-dimensional isomonodromic deformation.
