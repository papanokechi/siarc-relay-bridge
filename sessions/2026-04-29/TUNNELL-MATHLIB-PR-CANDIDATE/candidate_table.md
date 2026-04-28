| Rank | Candidate | Statement (informal) | Lines | Generality | Completeness | Mathlib fit | PR complexity | Total /20 | Suggested Mathlib home |
|------|-----------|----------------------|-------|------------|--------------|-------------|---------------|-----------|------------------------|
| 1 | `card_even_of_involution` | Finset with fixed-point-free involution has even card | 518–569 | 5 | 5 | 5 | 5 (SMALL) | 20 | `Mathlib.Data.Finset.Card` or `Mathlib.Data.Fintype.Parity` |
| 2 | `coord_bound_of_sum_eq` | `a>0, a*v² ≤ t, t≥0 → \|v\|.natAbs ≤ \|t\|.natAbs` | 213–230 | 3 | 4 | 4 | 5 (SMALL) | 16 | `Mathlib.NumberTheory.Quadratic` |
| 3 | `solSet∞_finite` (generalized) | Positive-definite diagonal ternary form has finite integer solutions | 367–382 | 4 | 4 | 4 | 3 (MEDIUM) | 15 | `Mathlib.NumberTheory.Quadratic` |
| 4 | `neg_ne_self_of_ne_zero` | Nonzero integer triple ≠ its componentwise negation | 418–431 | 3 | 5 | 3 | 5 (SMALL) | 16 | likely already implied — skip |
| 5 | `negTriple_involution` | `(-(-x), -(-y), -(-z)) = (x,y,z)` | 451–456 | 2 | 5 | 2 | 5 (SMALL) | 14 | too narrow — skip |

**Recommendation:** Open Mathlib PR for **`card_even_of_involution`** (rank 1, 20/20).
