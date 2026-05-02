# Conte–Musette algorithmic Painlevé test — summary

**Task ID:** T3-CONTE-MUSETTE-PAINLEVE-TEST
**Date:** 2026-05-02
**Catalogue:** PCF-1 v1.3 d=2 (10 families) + PCF-2 v1.3 d=3 (50 families) = 60 families.
**Method:** Three-branch Conte–Musette algorithmic Painlevé test on the
order-2 (d=2) / order-3 (d=3) linear ODE governing the OGF
`f(x) = sum_n q_n x^n` of the convergent denominator sequence.

## Aggregate result

| Degree | Families | LABELED | REJECTED | PARTIAL | INCONCLUSIVE |
|--------|---------:|--------:|---------:|--------:|-------------:|
| d=2    | 10       | 10      | 0        | 0       | 0            |
| d=3    | 50       | 50      | 0        | 0       | 0            |
| total  | 60       | 60      | 0        | 0       | 0            |

## V_quad sanity check (Phase D)

V_quad ( a(n)=1, b(n)=3 n^2 + n + 1 ) returns **LABELED** with
class **P_III(D₆)**, in agreement with the published reduction
recorded as CT v1.3 Theorem 3.3.D. **PASS.**

## Painlevé-class assignment (LABELED outcomes)

| Stratum | Families | Painlevé class (Conte–Musette-consistent) |
|---------|---------:|-------------------------------------------|
| d=2, Δ_b < 0 (anomaly bin: β²−4αγ < 0) | 6 | P_III(D₆) |
| d=2, Δ_b > 0                            | 4 | P_III(D₆) |
| d=3, all 50 families                    | 50 | PAINLEVE_UNCLASSIFIED (Newton polygon slopes 4/3 at 0, 2/3 at ∞ outside the standard P_I..P_VI list) |

## Branch disagreement table

| Family | Branch (a) | Branch (b) | Branch (c) | Aggregate | Class |
|--------|------------|------------|------------|-----------|-------|
| (no disagreements) | — | — | — | — | — |

Fraction of families with simultaneous LABELED/REJECTED branches:
**0/60 = 0.000** — well below the 5 % threshold from the prompt.
H3-confirmation signal **not present** in the present test.

## H3 (D=2_REDUCTION_AMBIGUOUS) closure status

**Closed under the Conte–Musette necessary criterion at d=2.**
The 6 Δ_b<0 families (V_quad, QL01, QL02, QL06, QL15, QL26) and the
4 Δ_b>0 representatives (QL05, QL09, QL13, QL18) all return the
*same* aggregate label LABELED with the *same* Painlevé-class
signature P_III(D₆).  The Conte–Musette test does **not**
distinguish the two signs of Δ_b: under this algorithmic test, the
"d=2 anomaly" (β²−4αγ<0) is **invisible** and the dichotomy seen
in PCF-1 v1.3 §3 (transcendence-vs-elementary) cannot be reproduced
from Newton-polygon / indicial / reflection data alone.

This is consistent with the H3 verdict's caveat that the ambiguity
arises because direct algorithmic Painlevé tests on the linear OGF
ODE are intrinsically limited: a linear 2nd-order ODE with
polynomial coefficients trivially satisfies the strict Painlevé
property at every regular point, and the Newton polygon at x=0 and
x=∞ depends only on the degree pattern of (a,b), not on the sign
of Δ_b.

## Epistemic discipline reminder

A LABELED outcome means **passes the Conte–Musette test (necessary
condition)** / **Conte–Musette-consistent with reduction to P_X**.
It does **NOT** mean **is Painlevé reducible to P_X**.  The full
Painlevé classification of any family in this catalogue requires
construction of an isomonodromic deformation and Sakai-surface
analysis, which is outside the scope of this prompt.

## Cross-degree comparison

- d=2 LABELED rate: 100 % (10/10), all class P_III(D₆).
- d=3 LABELED rate: 100 % (50/50), all class PAINLEVE_UNCLASSIFIED.

The uniform LABELED rate is a feature, not a strength signal: it
reflects the fact that algorithmic Painlevé tests on linear
generating-function ODEs are vacuously passing.  The informative
content is the **Painlevé-class signature**, which separates d=2
(rank-1, P_III(D₆)) from d=3 (rank 4/3 at x=0, fractional rank
outside the classical P_I..P_VI list).

## Files

- catalog_d2.csv               (10 families)
- catalog_d3.csv               (50 families)
- cm_results_branch_a.csv
- cm_results_branch_b.csv
- cm_results_branch_c.csv
- cm_aggregate.csv             (per-family label + class)
- claims.jsonl                 (8 AEAL entries)
- halt_log.json
- discrepancy_log.json
- unexpected_finds.json
- verdict.md
- rubber_duck_critique.md
- handoff.md
