# T35 Discrimination Certificate

**Top dps:** 250

## Per-representative leading Stokes multiplier S_1 = 2 pi i C

| rep_id | side | Delta_b | A_pred | N | C_tail | S_1 | C cross-method digits |
|--------|------|---------|--------|---|--------|-----|------------------------|
| V_quad | neg | -11 | 3 | 2000 | 8.1273367954950723671125787320... | (0.0 + 51.06556313995466226983... | 76.9 |
| QL15 | neg | -20 | 3 | 2000 | 21.384126494635065258284384536... | (0.0 + 134.3604293979607562971... | 74.9 |
| QL05 | pos | 8 | 4 | 2000 | 1.4032808072529649799472425015... | (0.0 + 8.817073349978938850501... | 67.8 |
| QL09 | pos | 1 | 4 | 2000 | -6.074720063790935061285275382... | (0.0 - 38.16859185004024347142... | 69.7 |

## Cross-side comparison

- |S_1[V_quad side=neg]| = 51.06556313995466211963503
- |S_1[QL15 side=neg]| = 134.360429397960757569308
- |S_1[QL05 side=pos]| = 8.81707334997893887873488
- |S_1[QL09 side=pos]| = 38.16859185004024368481623

Minimum cross-side digit-agreement on |S_1|: 0.03 digits (<10 means values differ at the 10^-10 level).

## Structural-pattern analysis

- Sign(C) on Delta<0 reps: [1, 1]
- Sign(C) on Delta>0 reps: [1, -1]
- Sign(C) varies WITHIN at least one side -> sign of C is NOT a clean A=3 vs A=4 discriminator at this scale.
- S_1 = 2 pi i C is purely imaginary for ALL 4 reps (C real) -> not a real-vs-imaginary discriminator.

## Within-side variation

- side=neg: |S_1| values agree to 0.21 digits (within-side)
- side=pos: |S_1| values agree to 0.11 digits (within-side)

## Verdict

**G6B_PARTIAL_HIGHER_ORDER_NEEDED**
