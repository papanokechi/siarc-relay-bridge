# UMB-CROSSDEG-29 -- symbolic indicial table

## Conventions

$\rho_d = a_d / b_{d/2}^2$ (leading-first coefficients).

- **BT** (rescaled): $I_{BT}(t) = t^2 - t - \rho_d$, $\Delta_{BT} = 1 + 4\rho_d$

- **Frobenius**: $I_F(r) = r^2 - r + \rho_d$, $\Delta_F = 1 - 4\rho_d$


## Per-degree symbolic table (d in {2, 4, 6})

| d | k | BT (rescaled) | Frobenius | BT-disc | F-disc |
|---|---|---------------|-----------|---------|--------|
| 2 | 1 | $t^2 - t - \rho_2$ | $r^2 - r + \rho_2$ | $1+4\rho_2$ | $1-4\rho_2$ |
| 4 | 2 | $t^2 - t - \rho_4$ | $r^2 - r + \rho_4$ | $1+4\rho_4$ | $1-4\rho_4$ |
| 6 | 3 | $t^2 - t - \rho_6$ | $r^2 - r + \rho_6$ | $1+4\rho_6$ | $1-4\rho_6$ |

*Polynomials are formally identical across d: dimension enters only through $\rho_d$.*


## Class A magic-rho catalogue (BT rational sum-1, $b \le 12$)

| b | m | $\rho = -m(b-m)/b^2$ | indicial roots |
|---|---|---------------------|----------------|
| 2 | 1 | -1/4 | {1/2, 1/2} |
| 3 | 1 | -2/9 | {1/3, 2/3} |
| 4 | 1 | -3/16 | {1/4, 3/4} |
| 5 | 1 | -4/25 | {1/5, 4/5} |
| 5 | 2 | -6/25 | {2/5, 3/5} |
| 6 | 1 | -5/36 | {1/6, 5/6} |
| 7 | 1 | -6/49 | {1/7, 6/7} |
| 7 | 2 | -10/49 | {2/7, 5/7} |
| 7 | 3 | -12/49 | {3/7, 4/7} |
| 8 | 1 | -7/64 | {1/8, 7/8} |
| 8 | 3 | -15/64 | {3/8, 5/8} |
| 9 | 1 | -8/81 | {1/9, 8/9} |
| 9 | 2 | -14/81 | {2/9, 7/9} |
| 9 | 4 | -20/81 | {4/9, 5/9} |
| 10 | 1 | -9/100 | {1/10, 9/10} |
| 10 | 3 | -21/100 | {3/10, 7/10} |
| 11 | 1 | -10/121 | {1/11, 10/11} |
| 11 | 2 | -18/121 | {2/11, 9/11} |

Simplest non-trivial entry: $b=3, m=1$, $\rho = -2/9$, roots $\{1/3, 2/3\}$.

## Class B (Frobenius double root)

$\rho = +1/4$ is the **unique** point where $\Delta_F = 0$, double root $r = 1/2$.

## HALT assessment

The two magic loci ({-2/9, +1/4, -2/25, ...}) are NOT a single family. Class A is the infinite family $\rho = -m(b-m)/b^2$ (Vieta forces rational sum-1 BT roots); Class B is the isolated point $\rho = 1/4$ (Frobenius double root). The prompt's HALT condition (single closed form unifying ALL magic ratios) is NOT met. Universality is **partial and dimension-independent**: each locus reappears at every even d, but they are governed by different indicial polynomials.
