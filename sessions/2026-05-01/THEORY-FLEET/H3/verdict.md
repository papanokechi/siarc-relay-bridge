# D=2_REDUCTION_AMBIGUOUS_NEEDS_NUMERICS

## Verdict

The d = 2 PCF anomaly is **not yet confirmed** as a two-branch Painlevé reduction by the accessible literature alone.

## Rationale

1. The explicit d = 2 PCF error recurrence is linear:

```text
delta_{n+1} = b(n+1) delta_n + a(n+1) delta_{n-1},
```

with quadratic `a,b`. Its projective ratio is a discrete Riccati map:

```text
y_{n+1} = b(n+1) + a(n+1)/y_n.
```

A Riccati map is linearisable and is not, by itself, a generic discrete Painlevé equation in Sakai's rational-surface sense.

2. Sakai's framework classifies affine-Weyl translations on rational surfaces. To classify the SIARC d = 2 object one must construct the missing two-dimensional birational map or Lax/isomonodromic deformation and compute its blow-up/root type.

3. The expected conditional branch assignment is plausible but unproved:

- `Delta_2 < 0` -> P-III(D6), if two non-apparent irregular singular directions appear.
- `Delta_2 > 0` -> P-V, if one regular singular direction survives; otherwise Riccati/Painlevé-trivial if apparent.
- `Delta_2 = 0` -> resonance boundary, possibly D7/D8 or Riccati collapse.

4. The claim `d >= 3 -> generic P-VI stratum` is compatible with the confluence hierarchy, but it requires a D4^(1) surface/four-regular-singularity calculation not available in this pass.

## What would change the verdict

Upgrade to `D=2_REDUCES_TO_PAINLEVE_TWO_BRANCHES_CONFIRMED` only if the next session computes distinct Sakai surface types or sigma-form residual hierarchies for the two signs of `Delta_2`.
