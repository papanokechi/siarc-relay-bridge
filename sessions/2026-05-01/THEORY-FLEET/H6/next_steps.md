# H6 next steps

## T5-CS PSLQ test

1. Reproduce the PCF-1 null result with the original 18-element basis at the original precision gate.
2. Compute each PCF limit and the relevant `Omega_D` at 1800 working digits, retaining at least 1500 trusted digits.
3. Run family-local PSLQ first:
   - `Q_L01`: `B18 + Omega_-3`
   - `Q_L02`: `B18 + Omega_-4`
   - `Q_L06`: `B18 + Omega_-7`
   - `V_quad`: `B18 + Omega_-11`
   - `Q_L15`: `B18 + Omega_-20`
   - `Q_L26`: `B18 + Omega_-28`
4. Accept a relation only if it is stable at 1200, 1500, and 1800 digits, has residual `< 1e-1000`, and coefficients remain below `1e80` in the first pass.
5. If family-local tests succeed, run the full `B24` basis to detect cross-family shared factors.

## Normalization diagnostics

If a family fails with the displayed `Omega_D`, test in order:

1. the raw character quotient `Q_D`;
2. `Q_D^(w/(4h))` from the eta-product Chowla-Selberg formula;
3. the reflection-reduced product listed in `summary.md`;
4. class-field algebraic multipliers (`sqrt(5)` is the first suspect for `D=-20`).

Only after these normalization variants fail should the case be labelled beyond Chowla-Selberg.

## Falsification criterion

Declare a family not detected by Chowla-Selberg if no relation appears at 1500 trusted digits with coefficient bound `1e120` and residual better than `1e-700` for all normalizations above.

## Beyond-CS escalation

Escalate in this order:

1. `D=-20`: include Hilbert/ring-class algebraic multipliers and roots of the CS class product.
2. `V_quad`: test Barnes-G or Painleve-III connection constants if a Stokes multiplier is numerically isolated.
3. Only then test Stark-unit or real-quadratic Borcherds-product constants inspired by Darmon-Vonk RM theory.
