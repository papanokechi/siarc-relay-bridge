# XI0-D3-DIRECT  Aggregate Report

K = 3 Galois bins:  +_C3_real, +_S3_real, -_S3_CM
Aggregate verdict: **G2_CLOSED_AT_D3**  (3/3 AGREE)

## Per-bin summary

| bin | family | (a3,a2,a1,a0) | alg agreement digits | num digits @N=1500 | verdict |
|---|---|---|---|---|---|
| `+_C3_real` | 19 | (1, -3, 0, 1) | 80.0 | 3.18 | **AGREES** |
| `+_S3_real` | 14 | (1, -3, -1, 1) | 80.0 | 3.18 | **AGREES** |
| `-_S3_CM` | 50 | (1, -2, 0, -1) | 80.0 | 3.35 | **AGREES** |

## Method recap

Two complementary tests per representative at dps=80:

- **Algebraic Newton-polygon**: characteristic root of L = 1 - z B(theta+1) - z^2 along the slope-1/3 edge.  |c_root| compared to xi_0_conj = 3 / alpha_3^{1/3}.
- **Numerical Borel-singularity**: Q_n recurrence at dps=80 for N in {500, 1000, 1500}.  beta_3 estimated by Q_n / (Q_{n-1} n^3) -> alpha_3, giving xi_0_measured = 3 / beta_3^{1/3}.

AGREES requires alg digits >= 60 AND numerical asymptotic match (>=1 digit at N=1500).  Numerical ladder is asymptotic so finite-N agreement is bounded by the O(1/N) subleading term a2/a3/N; full 60-digit numerical match would require N -> infty.