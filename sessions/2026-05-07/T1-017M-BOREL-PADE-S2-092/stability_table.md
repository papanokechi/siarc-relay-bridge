# Padé [N/M] Stability Tables — Relay 092

dps = 300  ;  N grid = [6, 8, 10, 12, 14, 16, 18]  ;  M grid = [6, 8, 10, 12, 14, 16, 18]
M8b verdict: **M8b_S2_PERMANENT_RESIDUAL_VIA_BOREL_PADE**

All four reps yielded 49/49 OK Padé cells (no RANK_LOSS or NO_POLE_NEAR_2 failures), but **zero** adjacent-cell pairs agreed to dps/4 = 75 digits, so no convergence region exists per the relay 092 spec gate.

## V_quad

- T35 zeta_star = 2.309401076758503058
- T35 S_1 (imag, T35 conv) = 51.06556313995466
- median |S_2 candidate| = 11.0208466488280028642
- relative half-range of |S_2| = 2.1411034055
- best digits-of-agreement across 84 adjacent (N,M) pairs: 3.741
- threshold for EXTRACTED = dps/4 = 75; achieved 0/84 pairs
- verdict: **PERMANENT_RESIDUAL_G6b**

### |S_2 candidate| stability table

| N \ M |          6 |          8 |         10 |         12 |         14 |         16 |         18 |
|---|---|---|---|---|---|---|---|
|   6   |      17.92 |      15.62 |      15.58 |      15.09 |       13.2 |      13.22 |      13.09 |
|   8   |      15.59 |      29.79 |      13.02 |      13.09 |      12.69 |      11.37 |      11.21 |
|   10   |      15.42 |       13.2 |      13.07 |         13 |      10.95 |      11.42 |      8.879 |
|   12   |      13.02 |      13.02 |      10.72 |      11.04 |      7.932 |      9.264 |      9.496 |
|   14   |      13.04 |      10.55 |      10.24 |      9.069 |      9.056 |      8.344 |       7.89 |
|   16   |      11.64 |      10.88 |      9.076 |      9.032 |      10.58 |      7.969 |      6.194 |
|   18   |      11.02 |      9.084 |       9.09 |      7.155 |      7.917 |       6.87 |      6.696 |

### Distance of nearest pole to u = 2 (the S_2 location)

| N \ M |          6 |          8 |         10 |         12 |         14 |         16 |         18 |
|---|---|---|---|---|---|---|---|
|   6   |     0.6938 |       0.56 |      0.572 |     0.5555 |     0.4882 |     0.5048 |     0.5364 |
|   8   |     0.5508 |     0.1665 |     0.4726 |     0.4764 |     0.4631 |     0.4255 |     0.4197 |
|   10   |     0.5532 |     0.4812 |     0.4755 |      0.472 |     0.0522 |     0.4395 |      0.326 |
|   12   |     0.4716 |     0.4715 |     0.3904 |     0.4105 |     0.2679 |     0.3506 |     0.3638 |
|   14   |     0.4731 |     0.3775 |     0.3748 |     0.3415 |     0.3411 |     0.3207 |     0.3067 |
|   16   |     0.4294 |     0.4488 |     0.3418 |     0.3404 |     0.3802 |      0.311 |     0.2466 |
|   18   |     0.4085 |     0.3421 |     0.3424 |     0.2574 |     0.3083 |     0.2734 |     0.2673 |

### S_2 candidate Im part (T35 convention has Stokes constants pure imaginary)

| N \ M |          6 |          8 |         10 |         12 |         14 |         16 |         18 |
|---|---|---|---|---|---|---|---|
|   6   |          0 |          0 |          0 |          0 |          0 |          0 |          0 |
|   8   |          0 |          0 |          0 |          0 |          0 |          0 |          0 |
|   10   |          0 |          0 |          0 |          0 |          0 |          0 |          0 |
|   12   |          0 |          0 |          0 |          0 |          0 |          0 |          0 |
|   14   |          0 |          0 |          0 |          0 |          0 |          0 |          0 |
|   16   |          0 |          0 |          0 |          0 |          0 |          0 |          0 |
|   18   |          0 |          0 |          0 |          0 |          0 |          0 |          0 |

---

## QL15

- T35 zeta_star = 2.309401076758503058
- T35 S_1 (imag, T35 conv) = 134.36042939796076
- median |S_2 candidate| = 70.6265177290000712702
- relative half-range of |S_2| = 3.9503603932
- best digits-of-agreement across 84 adjacent (N,M) pairs: 3.342
- threshold for EXTRACTED = dps/4 = 75; achieved 0/84 pairs
- verdict: **PERMANENT_RESIDUAL_G6b**

### |S_2 candidate| stability table

| N \ M |          6 |          8 |         10 |         12 |         14 |         16 |         18 |
|---|---|---|---|---|---|---|---|
|   6   |      215.8 |        237 |      216.3 |      211.4 |      228.4 |      18.87 |      18.88 |
|   8   |      23.18 |      213.5 |        213 |      215.3 |      226.7 |      70.63 |      137.1 |
|   10   |      228.4 |        199 |      213.2 |      222.6 |      183.8 |      297.9 |      64.84 |
|   12   |      183.3 |      119.2 |      61.98 |      77.23 |      59.69 |      53.08 |       56.1 |
|   14   |      219.3 |      63.25 |      286.9 |      58.71 |      60.69 |      51.26 |      32.15 |
|   16   |      71.84 |      69.96 |      58.47 |      61.77 |      52.39 |      31.65 |      34.53 |
|   18   |      97.75 |      57.45 |      42.94 |      81.25 |      28.87 |      34.85 |      23.62 |

### Distance of nearest pole to u = 2 (the S_2 location)

| N \ M |          6 |          8 |         10 |         12 |         14 |         16 |         18 |
|---|---|---|---|---|---|---|---|
|   6   |     0.3892 |     0.4173 |     0.3546 |     0.3446 |     0.3678 |     0.7395 |     0.7512 |
|   8   |     0.8189 |     0.3483 |     0.3478 |     0.3518 |     0.3859 |    0.07477 |     0.1986 |
|   10   |     0.3772 |     0.3252 |     0.3479 |     0.3735 |     0.2657 |     0.5902 |    0.04495 |
|   12   |     0.3047 |     0.1938 |     0.0487 |    0.09009 |    0.03431 |    0.01114 |    0.01997 |
|   14   |     0.3633 |    0.05253 |     0.6506 |    0.03092 |    0.04286 |    0.00537 |    0.06756 |
|   16   |    0.07616 |    0.06985 |    0.03015 |    0.06168 |   0.008267 |    0.07027 |    0.05986 |
|   18   |     0.1328 |    0.02675 |    0.01795 |     0.1574 |    0.08203 |    0.05862 |     0.1103 |

### S_2 candidate Im part (T35 convention has Stokes constants pure imaginary)

| N \ M |          6 |          8 |         10 |         12 |         14 |         16 |         18 |
|---|---|---|---|---|---|---|---|
|   6   |          0 |          0 |          0 |          0 |          0 |          0 |          0 |
|   8   |          0 |          0 |          0 |          0 |          0 |          0 |          0 |
|   10   |          0 |          0 |          0 |          0 |          0 |          0 |          0 |
|   12   |          0 |          0 |          0 |          0 |          0 |          0 |          0 |
|   14   |          0 |          0 |          0 |          0 |          0 |          0 |          0 |
|   16   |          0 |          0 |          0 |          0 |          0 |          0 |          0 |
|   18   |          0 |          0 |          0 |          0 |          0 |          0 |          0 |

---

## QL05

- T35 zeta_star = 4.0
- T35 S_1 (imag, T35 conv) = 8.817073349978939
- median |S_2 candidate| = 9.61812272050165298817
- relative half-range of |S_2| = 76.850378863
- best digits-of-agreement across 84 adjacent (N,M) pairs: 2.267
- threshold for EXTRACTED = dps/4 = 75; achieved 0/84 pairs
- verdict: **PERMANENT_RESIDUAL_G6b**

### |S_2 candidate| stability table

| N \ M |          6 |          8 |         10 |         12 |         14 |         16 |         18 |
|---|---|---|---|---|---|---|---|
|   6   |      22.18 |      8.149 |      5.729 |      4.692 |       4.04 |      3.629 |        3.5 |
|   8   |       4.97 |      161.7 |       10.1 |      8.736 |      8.081 |      11.63 |      9.221 |
|   10   |      7.443 |      8.745 |      8.587 |       8.32 |      8.805 |       9.04 |       9.14 |
|   12   |      8.976 |      7.288 |      9.415 |      9.688 |        9.8 |      9.978 |      742.7 |
|   14   |      8.738 |      9.141 |      373.9 |      9.514 |      96.12 |      286.1 |      587.1 |
|   16   |      9.618 |      9.969 |      10.08 |      366.9 |      638.4 |        179 |      225.3 |
|   18   |      9.987 |      9.179 |        248 |      323.6 |      241.2 |      230.9 |      232.1 |

### Distance of nearest pole to u = 2 (the S_2 location)

| N \ M |          6 |          8 |         10 |         12 |         14 |         16 |         18 |
|---|---|---|---|---|---|---|---|
|   6   |     0.7534 |     0.8559 |     0.8856 |     0.9004 |     0.9103 |     0.9169 |     0.9187 |
|   8   |      0.895 |     0.1748 |     0.7365 |     0.7729 |     0.7859 |     0.5213 |     0.7087 |
|   10   |     0.8326 |     0.7736 |     0.7763 |     0.7816 |     0.7647 |     0.7345 |     0.7227 |
|   12   |     0.7683 |     0.5154 |     0.7426 |     0.7041 |     0.6984 |     0.6855 |     0.3773 |
|   14   |     0.7733 |     0.7633 |     0.2997 |     0.7059 |     0.0652 |     0.1941 |     0.3286 |
|   16   |     0.7187 |     0.6926 |     0.6862 |     0.2335 |     0.3245 |    0.07451 |     0.1315 |
|   18   |      0.692 |     0.7143 |     0.1597 |     0.2095 |     0.1451 |      0.136 |     0.1369 |

### S_2 candidate Im part (T35 convention has Stokes constants pure imaginary)

| N \ M |          6 |          8 |         10 |         12 |         14 |         16 |         18 |
|---|---|---|---|---|---|---|---|
|   6   |          0 |          0 |          0 |          0 |          0 |          0 |          0 |
|   8   |          0 |          0 |          0 |          0 |          0 |          0 |          0 |
|   10   |          0 |          0 |          0 |          0 |          0 |          0 |          0 |
|   12   |          0 |          0 |          0 |          0 |          0 |          0 |          0 |
|   14   |          0 |          0 |          0 |          0 |          0 |          0 |          0 |
|   16   |          0 |          0 |          0 |          0 |          0 |          0 |          0 |
|   18   |          0 |          0 |          0 |          0 |          0 |          0 |          0 |

---

## QL09

- T35 zeta_star = 2.828427124746190097
- T35 S_1 (imag, T35 conv) = -38.168591850040244
- median |S_2 candidate| = 48.8721457658737582870
- relative half-range of |S_2| = 10.079581422
- best digits-of-agreement across 84 adjacent (N,M) pairs: 2.429
- threshold for EXTRACTED = dps/4 = 75; achieved 0/84 pairs
- verdict: **PERMANENT_RESIDUAL_G6b**

### |S_2 candidate| stability table

| N \ M |          6 |          8 |         10 |         12 |         14 |         16 |         18 |
|---|---|---|---|---|---|---|---|
|   6   |      8.188 |       8.06 |      8.635 |      7.939 |      7.988 |      7.795 |       7.52 |
|   8   |      8.827 |      8.582 |      20.72 |      173.7 |      120.6 |       70.8 |      57.74 |
|   10   |      8.036 |      8.092 |       7.87 |      29.88 |      49.09 |      6.811 |      38.71 |
|   12   |      499.4 |        245 |      65.82 |      66.06 |      56.56 |       51.3 |      48.87 |
|   14   |      7.229 |      55.06 |      6.816 |       50.5 |      49.12 |      45.97 |      40.71 |
|   16   |      63.77 |      67.48 |      52.92 |       51.2 |      47.91 |      53.25 |      54.78 |
|   18   |      261.5 |      50.65 |      43.07 |      43.29 |       56.2 |      54.35 |       39.4 |

### Distance of nearest pole to u = 2 (the S_2 location)

| N \ M |          6 |          8 |         10 |         12 |         14 |         16 |         18 |
|---|---|---|---|---|---|---|---|
|   6   |     0.9236 |     0.9247 |     0.8984 |     0.8483 |     0.8404 |     0.8467 |     0.8548 |
|   8   |     0.8952 |      0.885 |     0.2135 |     0.3961 |     0.2467 |    0.02839 |    0.04663 |
|   10   |     0.8434 |     0.8356 |     0.8441 |     0.3856 |    0.09742 |     0.7812 |     0.1945 |
|   12   |     0.5383 |     0.3091 |    0.03667 |    0.03696 |    0.07744 |     0.1039 |     0.1151 |
|   14   |     0.8594 |    0.07864 |      0.776 |     0.1069 |     0.1131 |     0.1252 |     0.1435 |
|   16   |     0.0472 |    0.03554 |    0.09509 |     0.1031 |     0.1189 |    0.09202 |    0.02201 |
|   18   |     0.1639 |     0.1054 |     0.1351 |     0.1343 |   0.003217 |    0.09068 |     0.1676 |

### S_2 candidate Im part (T35 convention has Stokes constants pure imaginary)

| N \ M |          6 |          8 |         10 |         12 |         14 |         16 |         18 |
|---|---|---|---|---|---|---|---|
|   6   |          0 |          0 |          0 |          0 |          0 |          0 |          0 |
|   8   |          0 |          0 |          0 |          0 |          0 |          0 |          0 |
|   10   |          0 |          0 |          0 |          0 |          0 |          0 |          0 |
|   12   |          0 |          0 |          0 |          0 |          0 |          0 |          0 |
|   14   |          0 |          0 |          0 |          0 |          0 |          0 |          0 |
|   16   |          0 |          0 |          0 |          0 |          0 |          0 |          0 |
|   18   |          0 |          0 |          0 |          0 |          0 |          0 |          0 |

---

## Divergence-pattern diagnostic (per Phase D2)

### V_quad
- |S_2| span (max/min): 4.809× (so spans ~0 orders of magnitude)
- |S_2| at fixed M=18, N varying: non-monotonic
- |S_2| at fixed N=18, M varying: non-monotonic
- sign of Im(S_2 candidate) across cells: coherent_pos
- nearest pole distances to u=2: min=0.0522, max=0.6938

### QL15
- |S_2| span (max/min): 15.78× (so spans ~1 orders of magnitude)
- |S_2| at fixed M=18, N varying: non-monotonic
- |S_2| at fixed N=18, M varying: non-monotonic
- sign of Im(S_2 candidate) across cells: coherent_pos
- nearest pole distances to u=2: min=0.00537, max=0.8189

### QL05
- |S_2| span (max/min): 212.2× (so spans ~2 orders of magnitude)
- |S_2| at fixed M=18, N varying: non-monotonic
- |S_2| at fixed N=18, M varying: non-monotonic
- sign of Im(S_2 candidate) across cells: coherent_pos
- nearest pole distances to u=2: min=0.0652, max=0.9187

### QL09
- |S_2| span (max/min): 73.32× (so spans ~1 orders of magnitude)
- |S_2| at fixed M=18, N varying: non-monotonic
- |S_2| at fixed N=18, M varying: non-monotonic
- sign of Im(S_2 candidate) across cells: coherent_pos
- nearest pole distances to u=2: min=0.003217, max=0.9247

## Aggregate interpretation

Per peer-AI rubric A's signal-floor concern (absorbed in 092 spec): Padé-stability across [N/M] orders is itself the inline signal-floor diagnostic. Across all four reps the small-(N,M) sweep produces well-formed Padé approximants (no RANK_LOSS at this conservative order, consistent with 092's design relative to T37M's M_in∈{200..800}), but the residue at the pole nearest u=2 fails to stabilise — the pole drifts in distance from 2 and its residue varies by 1-2 orders across the (N,M) grid. This **absence of convergence is the negative-result substrate**: at the laptop-feasible recurrence depth (017m / T37E cache, dps=400, N=5000, post-leading-sector polynomial structure), the sub-leading transmonomial governing S_2 is below the resolution floor of the small-order Padé construction.

Combined with T37M's high-order (M=200..800) RANK_LOSS verdict, the M8b-axis sub-leading Stokes constant is bracketed: **too small for low-order Padé to resolve, too noisy for high-order Padé to capture without numerical singularity**. This is the canonical PERMANENT_RESIDUAL_G6b signature.
