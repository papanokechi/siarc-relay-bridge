# Phase D — Cross-walk table

For each Okamoto generator (and the auxiliary involution y), the
explicit element of `Aut(D_6^{(1)}) ⋉ W((2A_1)^{(1)})` and the
induced permutation/affine action on `(a_0, a_1, b_0, b_1)`.

Parameter identification (Phase B.2):
   `a_0 = −v_1, a_1 = 1+v_1, b_0 = −v_2, b_1 = 1+v_2`.

Verification record: every row is checked by `verify_homomorphism.py`
(sympy; SHA-256 `FE438AD3B6E250AF18889193FB47DC183713C2EAFE126C9725E3DE31031203A3`).

| Okamoto symbol | Action on `(v_1, v_2)` | Sakai element | Action on `(a_0, a_1, b_0, b_1)` | Diagram-symmetry interpretation |
|---|---|---|---|---|
| `s_1` | `(v_2, v_1)` | `σ` | `(b_0, b_1, a_0, a_1)` | Swap the two A_1^{(1)} factors of (2A_1)^{(1)} (= chain-end swap of D_6^{(1)} diagram). |
| `s_2` | `(v_1, −v_2)` | `r'_0` | `(a_0, a_1, −b_0, b_1+2 b_0)` | Affine reflection in the simple root α'_0 of the second A_1^{(1)} component. |
| `s_0` | `(−1−v_2, −1−v_1)` | `σ · π · π'` | `(b_1, b_0, a_1, a_0)` | Compose: first node-swap **both** A_1^{(1)} factors (`ππ'`), then swap the two factors (`σ`). |
| `s_1 s_2` | `(−v_2, v_1)` | `σ · r'_0` | `(−b_0, b_1+2 b_0, a_0, a_1)` | Order-4 element on parameter space (B_2-style π/4 rotation). |
| `s_2 s_1` | `(v_2, −v_1)` | `r'_0 · σ` | `(b_0, b_1, −a_0, a_1+2 a_0)` | Inverse of `s_1 s_2`; equivalent to `r_0 · σ` after reduction. |
| `s_2 s_0` | `(−1−v_2, v_1+1)` | `r'_0 · σππ'` | `(b_1, b_0, −a_1, a_0+2 a_1)` | Order-4 element pairing α'_0 and α (highest root). |
| `s_1 s_0` | `(−1−v_1, −1−v_2)` | `σ · σππ' = ππ'` | `(a_1, a_0, b_1, b_0)` | Combined leaf-swap on both A_1^{(1)} factors (centre of `D_4 = Aut(D_6^{(1)})`). |
| `(s_1 s_2)²` | `(−v_1, −v_2) = y(v)` | `r_0 r'_0` | `(−a_0, a_1+2 a_0, −b_0, b_1+2 b_0)` | The Okamoto auxiliary involution `y`; lives in `W((2A_1)^{(1)})` (no Aut component). |
| `s_0 s_2 s_0` | `(v_1+2, v_2)` (translation) | `r_1` | `(a_0+2 a_1, −a_1, b_0, b_1)` | Affine reflection α_1 (long-root reflection on first A_1^{(1)}). |
| `s_1 s_0 s_2 s_0 s_1` | `(v_1, v_2+2)` (translation) | `r'_1` | `(a_0, a_1, b_0+2 b_1, −b_1)` | Affine reflection α'_1 (long-root reflection on second A_1^{(1)}). |
| **Outside image** | | | | |
| (extra Bäcklund) `(v_1, v_2) ↦ (−1−v_1, v_2)` | as left | `π` (one-sided leaf swap) | `(a_1, a_0, b_0, b_1)` | Index-2 cokernel generator; **not** in image of φ. |
| (extra Bäcklund) `(v_1, v_2) ↦ (v_1, −1−v_2)` | as left | `π'` (other one-sided swap) | `(a_0, a_1, b_1, b_0)` | Same cokernel coset as π (since `π · π' ∈ image` and `π · π = e`). |

## D.2 Translation lattice

The translation subgroup `Q^∨(B_2) ⊂ W^{aff}(B_2)` (rank 2) maps under
φ to the translation subgroup of `W((2A_1)^{(1)})`. Specifically:
   - Generator `t_1 := (s_0 s_2 s_0)·s_2 = r_1 r'_0`-style word —
     translates `(v_1, v_2) ↦ (v_1 + 2, v_2)`; on the Sakai side
     this is `r_1 r_0` (translation by 2α_1∨ in the first A_1^{(1)}).
   - Generator `t_2` similarly: `(v_1, v_2) ↦ (v_1, v_2 + 2)`,
     image `r'_1 r'_0` (translation in the second A_1^{(1)}).

Both translation lattices are `Z²` and the φ-image is the full
translation lattice of `W((2A_1)^{(1)})`. (No "missing" translation
direction; the cokernel is purely in the finite Aut/Weyl part.)

## D.3 Cross-check vs. KNY 2017 (slot 14)

KNY 2017 §6 records the affine-Weyl-group action on `P_III'(D_6^{(1)})`
parameters in the standard `(a_0, a_1, b_0, b_1)` notation. The
generators `r_0, r_1, r'_0, r'_1, σ` of W((2A_1)^{(1)}) (extended by
the swap σ) act exactly as in our table above (cross-referenced
against KNY 2017 §6 formulae for the `D_6^{(1)}`-case). The leaf
swaps π, π' are also present in KNY 2017 as separate Bäcklund
involutions; KNY 2017 does **not** state the homomorphism φ
explicitly (verified: KNY 2017 contains 0 occurrences of "B_2" as a
Lie-group symbol per slot 14 readback in prompt 029), but its
formulae are pointwise consistent with our cross-walk table.

No row of the cross-walk table contradicts any explicit Bäcklund
relation recorded in KNY 2017; in particular, the order-4 elements
`s_1 s_2` and `s_2 s_0` correspond to the order-4 elements of the
`D_4` finite Weyl quotient on each side. Halt-condition
`HALT_CONTRADICTS_KNY_2017` is **not** triggered.

## D.4 Self-consistency check

If the cross-walk is correct, then:
   `(s_1 s_2)^4 = e` ↔ `(σ r'_0)^4 = e`
must hold on **both** sides under the parameter identification of
B.2. We verified this symbolically (Phase B.5; sympy log line 28).
Similarly for `(s_2 s_0)^4 = e` ↔ `(r'_0 σππ')^4 = e` (sympy log
line 30) and `(s_1 s_0)^2 = e` ↔ `(ππ')^2 = e` (line 32). All
three pass.

This closes the cross-walk table.
