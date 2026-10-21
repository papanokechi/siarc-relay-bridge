# PREREG — CT-S18-COLDREAD-C3

Written before any computation.

## Hypothesis

Family (4.1) as printed in the provided van der Put--Saito page has a `b(z)` entry whose `z=1` value must satisfy the paper's own Section 3.2 constraint `det A(1) = -theta_1^2/4`. I will test the printed entry directly. If it fails, I will solve only for the single scalar correction required by that determinant constraint and then test the corrected expression.

## Observable

For the matrix `A(z)` in family (4.1), compute the symbolic residual

`Res = det(A(1)) + theta_1^2/4`.

The observable is the simplified/factored residual for the printed and corrected entries, plus high-precision numerical checks of the symbolic identities. Equality is accepted only by simplifying the difference/residual to zero and by independent high-precision numerical substitution at rational/complex points.

## Falsifier and threshold

The corrected formula is falsified if any of the following occur:

1. `simplify/cancel/together(Res_corrected)` is not exactly zero;
2. at 80 decimal digits, any test point gives `abs(Res_corrected) > 1e-70`;
3. the deliberately wrong control variant is not rejected by at least one exact or numerical assertion.

For locating System C in chart `U_0`, the substitution is falsified if either the transformed second-order coefficients `P` or `Q` differ from System C by an exact nonzero residual or by a numerical residual greater than `1e-70` at 80 dps. A deliberately wrong variant must be rejected.

## Vacuity pre-check

Before interpreting zero residuals, each script will assert that a deliberately wrong variant fails the same test. Batch operations will report counts in and out.
