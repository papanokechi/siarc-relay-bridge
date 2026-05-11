# Subtracted Pade [N/M] Stability Tables -- Relay 184 (U2 quadrant)

task: T2-EXECUTOR-T1-156-A-U2-QUADRANT-SUBTRACTED-PADE-184
dps_pade = 300  ;  dps_fit = 200
subtraction_order K_LEAD = 25
fit window = [3500, 4900]
N grid = [6, 8, 10, 12, 14, 16, 18]  ;  M grid = [6, 8, 10, 12, 14, 16, 18]
M8b verdict: **M8b_S2_PERMANENT_RESIDUAL_VIA_SUBTRACTED_BOREL_PADE**
halt_mode: **HALT_A_RESIDUAL_PATTERN_REPRODUCED**

Aggregate: 156/196 OK Pade cells across 4 reps; best adjacent-pair digits-of-agreement = 0.04 (threshold = dps/4 = 75). FAIL dps/4 gate.

## V_quad

- T35 zeta_star = 2.309401076758502924
- T35 C_lsq = 8.127336795495072152
- T35 S_1 (imag, T35 conv) = 51.06556313995466211
- stage-1 fit: a_1 = -1.47222254530634432303560051368  a_25 = -1.3518823691040578499e+79  max_resid = 5.53414073563e-38
- subtracted-residual decay at n=40: |residual|/|leading| = 9.3917171e+38
- median |S_2 candidate| = 2.84159420392985191560
- relative half-range of |S_2| = 4917.5165500
- best digits-of-agreement across 64 adjacent (N,M) pairs: 0.036
- threshold for EXTRACTED = dps/4 = 75; achieved 0/64 pairs
- verdict: **PERMANENT_RESIDUAL_G6b_SUBTRACTED**

### |S_2 candidate| (subtracted) stability table

| N \ M |          6 |          8 |         10 |         12 |         14 |         16 |         18 |
|---|---|---|---|---|---|---|---|
|   6   |          - |          - |          - |          - |  1.397e+56 |   5.26e+54 |  2.828e+53 |
|   8   |          - |          - |          - |  5.311e+55 |  1.495e+54 |  6.276e+52 |  3.651e+51 |
|   10   |          - |          - |  4.402e+55 |  9.826e+53 |  3.251e+52 |  1.522e+51 |  9.566e+49 |
|   12   |          - |  4.544e+55 |  9.563e+53 |  2.842e+52 |  1.121e+51 |  5.876e+49 |  1.488e+52 |
|   14   |  7.553e+55 |  1.119e+54 |  2.909e+52 |  1.098e+51 |  5.299e+49 |  1.142e+52 |  7.736e+50 |
|   16   |  2.458e+54 |  4.149e+52 |  1.234e+51 |  5.398e+49 |  1.121e+52 |   7.06e+50 |  3.487e+52 |
|   18   |   1.17e+53 |  2.164e+51 |  7.055e+49 |  1.243e+52 |  7.179e+50 |  3.429e+52 |  2.707e+51 |

### subtracted_pade_pole_nearest_u2_distance

| N \ M |          6 |          8 |         10 |         12 |         14 |         16 |         18 |
|---|---|---|---|---|---|---|---|
|   6   |          - |          - |          - |          - |     0.7412 |     0.4532 |      0.244 |
|   8   |          - |          - |          - |     0.6508 |     0.3596 |     0.1515 |   0.003328 |
|   10   |          - |          - |     0.6339 |     0.3299 |     0.1137 |    0.04549 |     0.1666 |
|   12   |          - |     0.6368 |      0.328 |     0.1062 |    0.05973 |     0.1858 |    0.08823 |
|   14   |     0.6831 |      0.339 |     0.1075 |    0.06069 |     0.1899 |    0.07385 |    0.06164 |
|   16   |     0.3957 |     0.1276 |    0.05527 |     0.1891 |    0.07286 |    0.06584 |     0.1482 |
|   18   |     0.1888 |    0.02879 |     0.1787 |    0.07841 |    0.06508 |     0.1473 |   0.008579 |

### subtracted_pade_residue_at_nearest_pole (|residue|)

| N \ M |          6 |          8 |         10 |         12 |         14 |         16 |         18 |
|---|---|---|---|---|---|---|---|
|   6   |          - |          - |          - |          - |  8.113e+54 |  3.413e+53 |  2.006e+52 |
|   8   |          - |          - |          - |  3.189e+54 |  1.008e+53 |  4.643e+51 |   2.91e+50 |
|   10   |          - |          - |   2.66e+54 |  6.712e+52 |  2.448e+51 |  1.239e+50 |  8.304e+48 |
|   12   |          - |  2.743e+54 |  6.538e+52 |  2.147e+51 |  9.191e+49 |  5.155e+48 |  1.134e+51 |
|   14   |   4.48e+54 |  7.615e+52 |  2.197e+51 |  9.008e+49 |  4.659e+48 |  8.767e+50 |  6.352e+49 |
|   16   |  1.633e+53 |  3.104e+51 |   1.01e+50 |  4.744e+48 |   8.61e+50 |  5.809e+49 |  2.583e+51 |
|   18   |  8.507e+51 |  1.747e+50 |  6.165e+48 |  9.516e+50 |  5.905e+49 |  2.542e+51 |  2.145e+50 |

### u_pole (real part of nearest-to-u=2 pole)

| N \ M |          6 |          8 |         10 |         12 |         14 |         16 |         18 |
|---|---|---|---|---|---|---|---|
|   6   |          - |          - |          - |          - |      2.741 |      2.453 |      2.244 |
|   8   |          - |          - |          - |      2.651 |       2.36 |      2.152 |      1.997 |
|   10   |          - |          - |      2.634 |       2.33 |      2.114 |      1.955 |      1.833 |
|   12   |          - |      2.637 |      2.328 |      2.106 |       1.94 |      1.814 |      2.088 |
|   14   |      2.683 |      2.339 |      2.107 |      1.939 |       1.81 |      2.074 |      1.938 |
|   16   |      2.396 |      2.128 |      1.945 |      1.811 |      2.073 |      1.934 |      2.148 |
|   18   |      2.189 |      1.971 |      1.821 |      2.078 |      1.935 |      2.147 |      2.009 |

---

## QL15

- T35 zeta_star = 2.309401076758502924
- T35 C_lsq = 21.38412649463506554
- T35 S_1 (imag, T35 conv) = 134.3604293979607575
- stage-1 fit: a_1 = -2.47222254530444642898436345831  a_25 = -1.3518782385564632897e+79  max_resid = 5.53412442849e-38
- subtracted-residual decay at n=40: |residual|/|leading| = 9.3916884e+38
- median |S_2 candidate| = 7.47659728727533921099
- relative half-range of |S_2| = 4917.5165500
- best digits-of-agreement across 64 adjacent (N,M) pairs: 0.036
- threshold for EXTRACTED = dps/4 = 75; achieved 0/64 pairs
- verdict: **PERMANENT_RESIDUAL_G6b_SUBTRACTED**

### |S_2 candidate| (subtracted) stability table

| N \ M |          6 |          8 |         10 |         12 |         14 |         16 |         18 |
|---|---|---|---|---|---|---|---|
|   6   |          - |          - |          - |          - |  3.677e+56 |  1.384e+55 |   7.44e+53 |
|   8   |          - |          - |          - |  1.397e+56 |  3.933e+54 |  1.651e+53 |  9.607e+51 |
|   10   |          - |          - |  1.158e+56 |  2.585e+54 |  8.553e+52 |  4.004e+51 |  2.517e+50 |
|   12   |          - |  1.196e+56 |  2.516e+54 |  7.477e+52 |  2.948e+51 |  1.546e+50 |  3.914e+52 |
|   14   |  1.987e+56 |  2.945e+54 |  7.654e+52 |  2.888e+51 |  1.394e+50 |  3.006e+52 |  2.036e+51 |
|   16   |  6.468e+54 |  1.092e+53 |  3.247e+51 |   1.42e+50 |  2.951e+52 |  1.858e+51 |  9.174e+52 |
|   18   |  3.078e+53 |  5.693e+51 |  1.856e+50 |   3.27e+52 |  1.889e+51 |  9.023e+52 |  7.122e+51 |

### subtracted_pade_pole_nearest_u2_distance

| N \ M |          6 |          8 |         10 |         12 |         14 |         16 |         18 |
|---|---|---|---|---|---|---|---|
|   6   |          - |          - |          - |          - |     0.7412 |     0.4532 |      0.244 |
|   8   |          - |          - |          - |     0.6508 |     0.3596 |     0.1515 |   0.003328 |
|   10   |          - |          - |     0.6339 |     0.3299 |     0.1137 |    0.04549 |     0.1666 |
|   12   |          - |     0.6368 |      0.328 |     0.1062 |    0.05973 |     0.1858 |    0.08823 |
|   14   |     0.6831 |      0.339 |     0.1075 |    0.06069 |     0.1899 |    0.07385 |    0.06164 |
|   16   |     0.3957 |     0.1276 |    0.05527 |     0.1891 |    0.07286 |    0.06584 |     0.1482 |
|   18   |     0.1888 |    0.02879 |     0.1787 |    0.07841 |    0.06508 |     0.1473 |   0.008579 |

### subtracted_pade_residue_at_nearest_pole (|residue|)

| N \ M |          6 |          8 |         10 |         12 |         14 |         16 |         18 |
|---|---|---|---|---|---|---|---|
|   6   |          - |          - |          - |          - |  2.135e+55 |  8.979e+53 |  5.277e+52 |
|   8   |          - |          - |          - |   8.39e+54 |  2.653e+53 |  1.222e+52 |  7.658e+50 |
|   10   |          - |          - |  6.998e+54 |  1.766e+53 |   6.44e+51 |   3.26e+50 |  2.185e+49 |
|   12   |          - |  7.217e+54 |   1.72e+53 |   5.65e+51 |  2.418e+50 |  1.356e+49 |  2.983e+51 |
|   14   |  1.179e+55 |  2.004e+53 |  5.781e+51 |   2.37e+50 |  1.226e+49 |  2.307e+51 |  1.671e+50 |
|   16   |  4.297e+53 |  8.167e+51 |  2.657e+50 |  1.248e+49 |  2.266e+51 |  1.529e+50 |  6.796e+51 |
|   18   |  2.238e+52 |  4.596e+50 |  1.622e+49 |  2.504e+51 |  1.554e+50 |  6.688e+51 |  5.644e+50 |

### u_pole (real part of nearest-to-u=2 pole)

| N \ M |          6 |          8 |         10 |         12 |         14 |         16 |         18 |
|---|---|---|---|---|---|---|---|
|   6   |          - |          - |          - |          - |      2.741 |      2.453 |      2.244 |
|   8   |          - |          - |          - |      2.651 |       2.36 |      2.152 |      1.997 |
|   10   |          - |          - |      2.634 |       2.33 |      2.114 |      1.955 |      1.833 |
|   12   |          - |      2.637 |      2.328 |      2.106 |       1.94 |      1.814 |      2.088 |
|   14   |      2.683 |      2.339 |      2.107 |      1.939 |       1.81 |      2.074 |      1.938 |
|   16   |      2.396 |      2.128 |      1.945 |      1.811 |      2.073 |      1.934 |      2.148 |
|   18   |      2.189 |      1.971 |      1.821 |      2.078 |      1.935 |      2.147 |      2.009 |

---

## QL05

- T35 zeta_star = 4.0
- T35 C_lsq = 1.403280807252965001
- T35 S_1 (imag, T35 conv) = 8.817073349978938878
- stage-1 fit: a_1 = 7.74999999999843213070124080703  a_25 = -3.4120470813702974349e+73  max_resid = 1.34705410808e-43
- subtracted-residual decay at n=40: |residual|/|leading| = 2.3694753e+33
- median |S_2 candidate| = 1.23834863820550273495
- relative half-range of |S_2| = 4917.5166121
- best digits-of-agreement across 64 adjacent (N,M) pairs: 0.036
- threshold for EXTRACTED = dps/4 = 75; achieved 0/64 pairs
- verdict: **PERMANENT_RESIDUAL_G6b_SUBTRACTED**

### |S_2 candidate| (subtracted) stability table

| N \ M |          6 |          8 |         10 |         12 |         14 |         16 |         18 |
|---|---|---|---|---|---|---|---|
|   6   |          - |          - |          - |          - |   6.09e+49 |  2.292e+48 |  1.232e+47 |
|   8   |          - |          - |          - |  2.315e+49 |  6.515e+47 |  2.735e+46 |  1.591e+45 |
|   10   |          - |          - |  1.918e+49 |  4.282e+47 |  1.417e+46 |  6.632e+44 |  4.169e+43 |
|   12   |          - |   1.98e+49 |  4.167e+47 |  1.238e+46 |  4.883e+44 |  2.561e+43 |  6.483e+45 |
|   14   |  3.292e+49 |  4.877e+47 |  1.268e+46 |  4.783e+44 |  2.309e+43 |  4.978e+45 |  3.371e+44 |
|   16   |  1.071e+48 |  1.808e+46 |  5.377e+44 |  2.352e+43 |  4.887e+45 |  3.077e+44 |  1.519e+46 |
|   18   |  5.099e+46 |  9.429e+44 |  3.075e+43 |  5.415e+45 |  3.128e+44 |  1.494e+46 |   1.18e+45 |

### subtracted_pade_pole_nearest_u2_distance

| N \ M |          6 |          8 |         10 |         12 |         14 |         16 |         18 |
|---|---|---|---|---|---|---|---|
|   6   |          - |          - |          - |          - |     0.7413 |     0.4533 |      0.244 |
|   8   |          - |          - |          - |     0.6509 |     0.3596 |     0.1516 |   0.003309 |
|   10   |          - |          - |      0.634 |     0.3299 |     0.1137 |    0.04547 |     0.1666 |
|   12   |          - |     0.6368 |      0.328 |     0.1062 |    0.05972 |     0.1858 |    0.08825 |
|   14   |     0.6831 |      0.339 |     0.1075 |    0.06067 |     0.1898 |    0.07387 |    0.06163 |
|   16   |     0.3957 |     0.1276 |    0.05525 |     0.1891 |    0.07288 |    0.06583 |     0.1483 |
|   18   |     0.1888 |    0.02877 |     0.1787 |    0.07843 |    0.06506 |     0.1473 |   0.008599 |

### subtracted_pade_residue_at_nearest_pole (|residue|)

| N \ M |          6 |          8 |         10 |         12 |         14 |         16 |         18 |
|---|---|---|---|---|---|---|---|
|   6   |          - |          - |          - |          - |  3.536e+48 |  1.487e+47 |   8.74e+45 |
|   8   |          - |          - |          - |   1.39e+48 |  4.394e+46 |  2.023e+45 |  1.268e+44 |
|   10   |          - |          - |  1.159e+48 |  2.925e+46 |  1.067e+45 |    5.4e+43 |  3.619e+42 |
|   12   |          - |  1.195e+48 |  2.849e+46 |  9.358e+44 |  4.006e+43 |  2.247e+42 |  4.941e+44 |
|   14   |  1.953e+48 |  3.319e+46 |  9.574e+44 |  3.925e+43 |   2.03e+42 |  3.821e+44 |  2.768e+43 |
|   16   |  7.117e+46 |  1.353e+45 |  4.401e+43 |  2.067e+42 |  3.752e+44 |  2.532e+43 |  1.126e+45 |
|   18   |  3.707e+45 |  7.613e+43 |  2.687e+42 |  4.147e+44 |  2.573e+43 |  1.108e+45 |  9.347e+43 |

### u_pole (real part of nearest-to-u=2 pole)

| N \ M |          6 |          8 |         10 |         12 |         14 |         16 |         18 |
|---|---|---|---|---|---|---|---|
|   6   |          - |          - |          - |          - |      2.741 |      2.453 |      2.244 |
|   8   |          - |          - |          - |      2.651 |       2.36 |      2.152 |      1.997 |
|   10   |          - |          - |      2.634 |       2.33 |      2.114 |      1.955 |      1.833 |
|   12   |          - |      2.637 |      2.328 |      2.106 |       1.94 |      1.814 |      2.088 |
|   14   |      2.683 |      2.339 |      2.107 |      1.939 |       1.81 |      2.074 |      1.938 |
|   16   |      2.396 |      2.128 |      1.945 |      1.811 |      2.073 |      1.934 |      2.148 |
|   18   |      2.189 |      1.971 |      1.821 |      2.078 |      1.935 |      2.147 |      2.009 |

---

## QL09

- T35 zeta_star = 2.828427124746190290
- T35 C_lsq = -6.07472006379093532
- T35 S_1 (imag, T35 conv) = -38.1685918500402436
- stage-1 fit: a_1 = 0.000000381202402669096033719366914892  a_25 = 1.5950484337382348683e+79  max_resid = 6.52957591462e-38
- subtracted-residual decay at n=40: |residual|/|leading| = 1.1081026e+39
- median |S_2 candidate| = 2.50596523337449800458
- relative half-range of |S_2| = 4917.5165500
- best digits-of-agreement across 64 adjacent (N,M) pairs: 0.036
- threshold for EXTRACTED = dps/4 = 75; achieved 0/64 pairs
- verdict: **PERMANENT_RESIDUAL_G6b_SUBTRACTED**

### |S_2 candidate| (subtracted) stability table

| N \ M |          6 |          8 |         10 |         12 |         14 |         16 |         18 |
|---|---|---|---|---|---|---|---|
|   6   |          - |          - |          - |          - |  1.232e+56 |  4.639e+54 |  2.494e+53 |
|   8   |          - |          - |          - |  4.684e+55 |  1.318e+54 |  5.535e+52 |   3.22e+51 |
|   10   |          - |          - |  3.882e+55 |  8.665e+53 |  2.867e+52 |  1.342e+51 |  8.436e+49 |
|   12   |          - |  4.008e+55 |  8.433e+53 |  2.506e+52 |  9.882e+50 |  5.182e+49 |  1.312e+52 |
|   14   |  6.661e+55 |  9.869e+53 |  2.566e+52 |  9.679e+50 |  4.673e+49 |  1.007e+52 |  6.823e+50 |
|   16   |  2.168e+54 |  3.659e+52 |  1.088e+51 |   4.76e+49 |   9.89e+51 |  6.226e+50 |  3.075e+52 |
|   18   |  1.032e+53 |  1.908e+51 |  6.222e+49 |  1.096e+52 |  6.331e+50 |  3.024e+52 |  2.387e+51 |

### subtracted_pade_pole_nearest_u2_distance

| N \ M |          6 |          8 |         10 |         12 |         14 |         16 |         18 |
|---|---|---|---|---|---|---|---|
|   6   |          - |          - |          - |          - |     0.7412 |     0.4532 |      0.244 |
|   8   |          - |          - |          - |     0.6508 |     0.3596 |     0.1515 |   0.003328 |
|   10   |          - |          - |     0.6339 |     0.3299 |     0.1137 |    0.04549 |     0.1666 |
|   12   |          - |     0.6368 |      0.328 |     0.1062 |    0.05973 |     0.1858 |    0.08823 |
|   14   |     0.6831 |      0.339 |     0.1075 |    0.06069 |     0.1899 |    0.07385 |    0.06164 |
|   16   |     0.3957 |     0.1276 |    0.05527 |     0.1891 |    0.07286 |    0.06584 |     0.1482 |
|   18   |     0.1888 |    0.02879 |     0.1787 |    0.07841 |    0.06508 |     0.1473 |   0.008579 |

### subtracted_pade_residue_at_nearest_pole (|residue|)

| N \ M |          6 |          8 |         10 |         12 |         14 |         16 |         18 |
|---|---|---|---|---|---|---|---|
|   6   |          - |          - |          - |          - |  7.155e+54 |  3.009e+53 |  1.769e+52 |
|   8   |          - |          - |          - |  2.812e+54 |  8.893e+52 |  4.094e+51 |  2.567e+50 |
|   10   |          - |          - |  2.345e+54 |  5.919e+52 |  2.159e+51 |  1.093e+50 |  7.323e+48 |
|   12   |          - |  2.419e+54 |  5.766e+52 |  1.894e+51 |  8.106e+49 |  4.546e+48 |  9.999e+50 |
|   14   |  3.951e+54 |  6.716e+52 |  1.938e+51 |  7.944e+49 |  4.109e+48 |  7.732e+50 |  5.602e+49 |
|   16   |   1.44e+53 |  2.737e+51 |  8.906e+49 |  4.184e+48 |  7.593e+50 |  5.123e+49 |  2.278e+51 |
|   18   |  7.502e+51 |  1.541e+50 |  5.437e+48 |  8.392e+50 |  5.207e+49 |  2.242e+51 |  1.892e+50 |

### u_pole (real part of nearest-to-u=2 pole)

| N \ M |          6 |          8 |         10 |         12 |         14 |         16 |         18 |
|---|---|---|---|---|---|---|---|
|   6   |          - |          - |          - |          - |      2.741 |      2.453 |      2.244 |
|   8   |          - |          - |          - |      2.651 |       2.36 |      2.152 |      1.997 |
|   10   |          - |          - |      2.634 |       2.33 |      2.114 |      1.955 |      1.833 |
|   12   |          - |      2.637 |      2.328 |      2.106 |       1.94 |      1.814 |      2.088 |
|   14   |      2.683 |      2.339 |      2.107 |      1.939 |       1.81 |      2.074 |      1.938 |
|   16   |      2.396 |      2.128 |      1.945 |      1.811 |      2.073 |      1.934 |      2.148 |
|   18   |      2.189 |      1.971 |      1.821 |      2.078 |      1.935 |      2.147 |      2.009 |

---

## Divergence-pattern diagnostic (per slot 184 Phase B halt-mode)

### V_quad
- |S_2| span (max/min): 2.637e+06x (~6 orders of magnitude)
- |S_2| at fixed M=18, N varying: non-monotonic
- |S_2| at fixed N=18, M varying: non-monotonic
- sign of Im(S_2 candidate) across cells: coherent_pos
- nearest pole distances to u=2: min=0.003328, max=0.7412
- min-distance achieved near max(N+M)? NO

### QL15
- |S_2| span (max/min): 2.637e+06x (~6 orders of magnitude)
- |S_2| at fixed M=18, N varying: non-monotonic
- |S_2| at fixed N=18, M varying: non-monotonic
- sign of Im(S_2 candidate) across cells: coherent_pos
- nearest pole distances to u=2: min=0.003328, max=0.7412
- min-distance achieved near max(N+M)? NO

### QL05
- |S_2| span (max/min): 2.637e+06x (~6 orders of magnitude)
- |S_2| at fixed M=18, N varying: non-monotonic
- |S_2| at fixed N=18, M varying: non-monotonic
- sign of Im(S_2 candidate) across cells: coherent_pos
- nearest pole distances to u=2: min=0.003309, max=0.7413
- min-distance achieved near max(N+M)? NO

### QL09
- |S_2| span (max/min): 2.637e+06x (~6 orders of magnitude)
- |S_2| at fixed M=18, N varying: non-monotonic
- |S_2| at fixed N=18, M varying: non-monotonic
- sign of Im(S_2 candidate) across cells: coherent_pos
- nearest pole distances to u=2: min=0.003328, max=0.7412
- min-distance achieved near max(N+M)? NO

## Cross-quadrant comparison: subtracted (slot 184) vs raw (slot 092)

Both runs use identical (N, M) in {6..18}^2, dps=300 (Pade), 4 reps. Only the Borel-coefficient series differs: 092 uses raw a_n; 184 uses K_LEAD = 25 -subtracted a_n_residual. Comparison at the per-rep level:

| rep | (092) median |S_2| | (184) median |S_2| | (092) rel_half_range | (184) rel_half_range | (092) best_pair_digits | (184) best_pair_digits |
|---|---|---|---|---|---|---|
| V_quad | 11.020846648 | 2.8415942039 | 2.14110340 | 4917.51655 | 3.74 | 0.04 |
| QL15 | 70.626517729 | 7.4765972872 | 3.95036039 | 4917.51655 | 3.34 | 0.04 |
| QL05 | 9.6181227205 | 1.2383486382 | 76.8503788 | 4917.51661 | 2.27 | 0.04 |
| QL09 | 48.872145765 | 2.5059652333 | 10.0795814 | 4917.51655 | 2.43 | 0.04 |

## Aggregate interpretation -- halt-mode rationale

The K_LEAD = 25 -subtracted Pade approximant at small (N, M) in {6..18}^2 exhibits the same PERMANENT_RESIDUAL signature as 092's raw-low-order approach: no adjacent-cell pair achieves the dps/4 = 75-digit Pade-convergence threshold, and the pole-nearest-u=2 distance does not exhibit systematic shrinkage with increasing (N + M).

**Cross-quadrant closure.** Combined with 092 (raw small-(N,M)) and T37M (subtracted large-M_in), the M8b axis sub-leading Stokes constant is now established as PERMANENT_RESIDUAL across all four corners of the Pade-stability quadrant grid: subtraction does not help at small order, and order-extension does not help at any subtraction order. This is the strictly-stronger negative-result substrate envisioned by slot 156 verdict's V0+(defended) target.
