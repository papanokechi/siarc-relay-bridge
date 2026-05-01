# H6 handoff

**Verdict:** `AUGMENTED_BASIS_DETECTS_ALL_6` (confidence MED).

**Roster:** `Q_L01 (-3)`, `Q_L02 (-4)`, `Q_L06 (-7)`, `V_quad (-11)`, `Q_L15 (-20)`, `Q_L26 (-28)`.

**CM orders:** `Z[(1+sqrt(-3))/2]`, `Z[i]`, `Z[(1+sqrt(-7))/2]`, `Z[(1+sqrt(-11))/2]`, `Z[sqrt(-5)]`, and conductor-2 `Z[sqrt(-7)]`.

**Basis augmentation:** add six Chowla-Selberg period constants:

- `Omega_-3 = Gamma(1/3)^3/(2*pi)`
- `Omega_-4 = Gamma(1/4)^2/(2*sqrt(2*pi))`
- `Omega_-7 = Gamma(1/7)Gamma(2/7)Gamma(4/7)/(2*pi)^(3/2)`
- `Omega_-11 = Gamma(1/11)Gamma(3/11)Gamma(4/11)Gamma(5/11)Gamma(9/11)/(2*pi)^(5/2)`
- `Omega_-20 = [Gamma(1/20)Gamma(3/20)Gamma(7/20)Gamma(9/20)/(Gamma(11/20)Gamma(13/20)Gamma(17/20)Gamma(19/20))]^(1/4)`
- `Omega_-28 = [Gamma(1/28)Gamma(9/28)Gamma(11/28)Gamma(15/28)Gamma(23/28)Gamma(25/28)/(Gamma(3/28)Gamma(5/28)Gamma(13/28)Gamma(17/28)Gamma(19/28)Gamma(27/28))]^(1/2)`

**PSLQ recipe:** target 1500 trusted digits, 1800 working digits, family-local `B18+Omega_D` before full `B24`, accept residual `<1e-1000` stable across precision escalations.

**Risk:** if partial, first suspect `Q_L15` due to class-number-two normalization; second suspect `V_quad` due to Painleve/Stokes evidence.  Stark units / real-quadratic Borcherds products are fallback, not first-line, because the six orders are imaginary CM.
