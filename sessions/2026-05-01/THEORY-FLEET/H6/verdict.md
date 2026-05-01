# AUGMENTED_BASIS_DETECTS_ALL_6

H6 predicts that the Chowla-Selberg augmentation detects all six PCF-1 negative-discriminant CM non-detections.

The proposed basis is

`B24 = B18 ∪ {Omega_-3, Omega_-4, Omega_-7, Omega_-11, Omega_-20, Omega_-28}`,

where each `Omega_D` is the CM period/Gamma-product generator attached to the corresponding order of discriminant `D`.

Confidence is **MED**, not HIGH.  Chowla-Selberg rigorously supplies the missing Gamma-products for CM elliptic periods, and the six PCF-1 discriminants are exactly imaginary-quadratic CM orders.  However, PCF-1 has not yet proved that the six PCF limits are pure elliptic CM periods.  If one family fails, the most plausible exceptions are `Q_L15` (`D=-20`, class number two normalization) and `V_quad` (`D=-11`, Painleve/Stokes channel evidence).

Fallback verdict if testing fails: `AUGMENTED_BASIS_DETECTS_PARTIAL`, then test class-field algebraic multipliers, Barnes-G/Painleve connection constants, and only later Stark-unit or real-quadratic Borcherds-product constants.
