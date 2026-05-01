# H3 — Painlevé-hierarchy reduction at d = 2

## Executive conclusion

The literature does **not** justify a top-line claim that the SIARC `d = 2` PCF anomaly has already been classified as a two-branch discrete Painlevé system. The scalar PCF error recurrence is a rank-2 **linear** difference equation. Its projectivization is a discrete Riccati map, hence linearisable. Sakai's classification, by contrast, classifies non-linear birational translations on rational surfaces, with affine Weyl-group symmetry and Okamoto spaces of initial conditions. Therefore the PCF recurrence, by itself, is not a generic discrete Painlevé equation in Sakai's sense.

The right literature-grounded statement is conditional: if the PCF recurrence is embedded into a two-variable isomonodromic deformation/Lax pair, then the usual confluence chain

`P-VI (D4^(1)) -> P-V (D5^(1)) -> P-III(D6) (D6^(1)) -> P-III(D7/D8)`

is the relevant classification axis. In that conditional embedding, the empirical discriminant split is plausibly interpreted as follows:

- `Delta_2 < 0`: oscillatory/complex-conjugate monodromy branch; predicted to land on a **P-III(D6)** confluence if the deformation has two non-apparent irregular singular directions.
- `Delta_2 > 0`: real split monodromy branch; predicted to land on **P-V (D5^(1))** if one regular singular direction survives, or on a Riccati/hypergeometric **Painlevé-trivial** divisor if the extra singularity is apparent.
- `Delta_2 = 0`: resonant boundary; should be tested separately as a possible D7/D8 or pure Riccati degeneration.

Thus the verdict is `D=2_REDUCTION_AMBIGUOUS_NEEDS_NUMERICS`, not a confirmation. The next session should construct the missing Sakai data: a birational two-dimensional map, its base-point blow-up configuration, the anti-canonical divisor type, and continuum sigma-form residuals.

## The PCF recurrence at d = 2

For a polynomial continued fraction

```text
K = b(0) + K_{n=1}^infty a(n)/b(n),        a(n), b(n) in Z[n], deg a, deg b <= 2,
```

the convergent numerator/denominator pair and the error sequence `delta_n = P_n - K Q_n` obey the same rank-2 recurrence. Writing

```text
A_n = a_2 n^2 + a_1 n + a_0,
B_n = b_2 n^2 + b_1 n + b_0,
```

the d = 2 scalar recurrence is

```text
delta_{n+1} = B_{n+1} delta_n + A_{n+1} delta_{n-1}.
```

Equivalently,

```text
[delta_{n+1}]   [B_{n+1}  A_{n+1}] [delta_n    ]
[delta_n    ] = [1        0      ] [delta_{n-1}].
```

The ratio `y_n = delta_n/delta_{n-1}` satisfies

```text
y_{n+1} = B_{n+1} + A_{n+1}/y_n.
```

This is a non-autonomous discrete Riccati equation. It is linearisable by construction. Consequently, the direct Sakai classification of this one-dimensional projective recurrence is: **Riccati/special-function leaf, not a generic discrete Painlevé translation**. Kajiwara--Noumi--Yamada's review emphasizes that discrete Painlevé equations are controlled by blow-up configurations on rational surfaces and by affine Weyl-group actions; a Riccati equation may appear as a special solution divisor, but it is not the full surface dynamics.

The SIARC discriminant `Delta_2` should therefore be read as a discriminant of the rank-2 connection/transfer data. Its sign distinguishes elliptic/oscillatory versus hyperbolic/split transfer behavior, but sign alone is not the Sakai surface type.

## Sakai framework and where d = 2 can fit

Sakai's 2001 classification starts from a compact rational surface `X` with a unique anti-canonical divisor `D` of canonical type. Root subsystems of `E_8^(1)` in the Picard lattice encode affine Weyl symmetries; translations in the affine Weyl group produce discrete Painlevé equations, and the six continuous Painlevé equations occur as degenerate cases. The accessible Springer abstract explicitly states this rational-surface, affine-Weyl, and degeneration picture for the six differential Painlevé equations.

The standard continuous degeneration chain can be used as an identification guide:

| Isomonodromic singularity pattern | Continuous class | Sakai/Okamoto surface type |
|---|---:|---:|
| four regular singularities | P-VI | D4^(1) |
| three effective singular directions / one confluence | P-V | D5^(1) |
| two irregular singular directions with nonzero monodromy parameters | P-III(D6) | D6^(1) |
| further resonance/apparent collapse | P-III(D7/D8) or Riccati | D7^(1)/D8^(1) or divisor |

This table is a classification guide, not a proof for SIARC. To prove the d = 2 split, one must exhibit the PCF family as an isomonodromic deformation problem and compute the surface type. Without the two-dimensional birational map and base points, the most one can infer is a plausible confluence class.

## Formal continuum limit

The direct WKB continuum limit of the scalar recurrence is not a universal Painlevé ODE. With `n = t/epsilon` and a local WKB ansatz `delta_n ~ exp(S(t)/epsilon) u(t)`, the leading eikonal equation has the form

```text
lambda(t)^2 - B_0(t) lambda(t) - A_0(t) = 0,
S'(t) = log lambda(t),
```

where `A_0, B_0` are the leading scaled coefficient functions. The next transport equation is Riccati/linear after projectivization. Equivalently, after gauge normalization it can be written as a family-dependent second-order linear ODE

```text
psi'' + P(t) psi' + Q(t) psi = 0,
```

or a Schrödinger/WKB form

```text
epsilon^2 phi'' = V(t; epsilon) phi.
```

A Painlevé equation appears only after adding an isomonodromic deformation parameter and imposing monodromy preservation. In that conditional setting, the branch candidates are the standard normal forms

```text
P-III(D6):
q'' = (q')^2/q - q'/t + (alpha q^2 + beta)/t + gamma q^3 + delta/q,
        gamma delta != 0,
```

and

```text
P-V:
q'' = (1/(2q)+1/(q-1))(q')^2 - q'/t
      + ((q-1)^2/t^2)(alpha q + beta/q) + gamma q/t
      + delta q(q+1)/(q-1).
```

The d = 2 data are consistent with a PV-to-PIII confluence scenario, but the literature does not let us assign the branch solely from the sign of `Delta_2`.

## Branch predictions

### Delta_2 < 0

The negative-discriminant branch should have complex-conjugate transfer multipliers and oscillatory WKB phases. If the associated deformation has two non-apparent irregular singularities, the natural confluence class is **P-III(D6)**. This matches the empirical conjecture and the known role of PIII(D6) in two-irregular-singularity isomonodromy. Confidence: **medium**, because the monodromy/surface data remain to be computed.

### Delta_2 > 0

The positive-discriminant branch should have real split multipliers. If the confluence retains one regular singular direction before the irregular point, the class should be **P-V**. If the extra singularity is apparent or the accessory parameter lies on a Riccati divisor, the correct label is **Painlevé-trivial/Riccati** rather than generic PV. Confidence: **medium-low** until apparentness tests are run.

### d >= 3

The conjectural statement that `d >= 3` is a generic P-VI stratum is plausible only if the higher-degree PCF family produces four effective regular singular directions in its isomonodromic lift. The absence of the d = 2 anomaly is compatible with this picture, but Sakai classification still requires explicit blow-up data. Confidence: **low-to-medium**.

## Literature accessibility note

The key accessible sources were: Springer pages and Crossref metadata for Conte--Musette and Sakai; arXiv and journal metadata for Kajiwara--Noumi--Yamada; AMS metadata for Fokas--Its--Kapaev--Novokshenov; Crossref/web metadata for Joshi--Kruskal and Kruskal--Joshi--Halburd; Crossref metadata for Its--Kapaev and Dubrovin--Kapaev. Web searches did not locate a clear joint "Kapaev--Hubert" Painlevé/isomonodromy paper; I therefore used Kapaev's isomonodromy references and flagged this instead of inventing a citation.
