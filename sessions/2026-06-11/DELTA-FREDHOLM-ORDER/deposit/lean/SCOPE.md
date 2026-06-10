# SCOPE — DELTA-FREDHOLM-LEAN-CORE

Machine-checked finitary core of the determinant identity underlying the Fredholm
representation of the pcf-delta growth constant (companion numerics: session
DELTA-FREDHOLM-P0, VERIFIED to 65 digits by two independent channels).

Toolchain (pinned, committed): `leanprover/lean4:v4.30.0`, Mathlib `v4.30.0`
(`lake-manifest.json` rev `c5ea00351c28e24afc9f0f84379aa41082b1188f`).

---

## 1. Locked G0 convention (verbatim)

Over a general commutative ring `R`, with weights `w : ℕ → R` and activity `lam : R`:

**Continuant (load-bearing object, NOT the matrix):**
```
c 0       = 1
c 1       = 1
c (n+2)   = c (n+1) + lam * w (n+2) * c n          -- (REC)
```

**Tridiagonal matrix** `Amat w lam M : Matrix (Fin M) (Fin M) R`:
```
A i j = 1                if (i:ℕ) = (j:ℕ)            -- diagonal
      = lam * w (i+2)    if (j:ℕ) = (i:ℕ) + 1        -- super-diagonal (slot weight)
      = -1               if (i:ℕ) = (j:ℕ) + 1        -- sub-diagonal
      = 0                otherwise
```
Comparisons are taken on the `ℕ`-values of the `Fin` indices.

---

## 2. G0 FALSIFICATION FINDING (falsification-first; reported, not papered over)

The brief's G0 text pinned the base case `c 1 = 1 + lam * w 1`. This is **WRONG**
for the verbatim matrix: `Amat w lam 1` is the `1×1` matrix `[1]`, so
`det (Amat w lam 1) = 1`, not `1 + lam * w 1`.

* Lean witness `g0_det_one    : (Amat w lam 1).det = 1`.
* Lean counterexample `g0_brief_base_is_wrong`: with `w ≡ 1`, `lam = 1` over `ℤ`,
  `det (Amat 1) = 1 ≠ 2 = 1 + lam * w 1`.

**Corrected, self-consistent convention** (the one formalized here): `c 1 = 1`.
Under it `cseq w lam M` is the weighted **independence (sparse-subset) polynomial**
of the path on the index set `{2,…,M}`, vertex `i` carrying weight `lam * w i` —
exactly the P0 object "path on indices {2..N}". The G0 ladder confirms

```
det (Amat w lam 1) = 1
det (Amat w lam 2) = 1 + lam * w 2
det (Amat w lam 3) = 1 + lam * w 2 + lam * w 3
```

all equal to `cseq w lam M` (lemmas `g0_matches_cseq_one/two/three`), and the P0
brute-force enumeration matches the `Rpoly` independence-polynomial definition
proved equal to `cseq` in `T_COMB`.

> Note on the original super-diagonal index `w (i+2)`: it is **retained verbatim**;
> the single correction is the base value `c 1 = 1` (equivalently, there is no
> isolated `lam * w 1` term — vertex `1` is not in the path `{2,…,M}`).

---

## 3. Grading of every declaration (four-class)

PROVEN = builds with axiom cone ⊆ `{propext, Classical.choice, Quot.sound}`, no `sorryAx`.

| Declaration | Class | Role |
|---|---|---|
| `cseq`, `Amat`, `Sp`, `Rpoly` | DEFINITION | the locked objects |
| `cseq_zero/one`, `cseq_add_two` | PROVEN | recurrence simp lemmas |
| `g0_det_one/two/three` | PROVEN | G0 determinant ladder |
| `g0_matches_cseq_one/two/three` | PROVEN | G0 ↔ `cseq` agreement |
| `g0_brief_base_is_wrong` | PROVEN | falsification counterexample |
| `Amat_val_eq`, `Amat_submatrix_castSucc`, `Amat_inner_submatrix` | PROVEN | entry/block helpers |
| `Amat_inner_det` | PROVEN | sub-diagonal cofactor block det |
| `Amat_det_rec` | PROVEN | **determinant recurrence (P1 crux)** |
| **`T_DET`** | **PROVEN** | **det (Amat w lam M) = cseq w lam M, ∀M** |
| `mem_Sp`, `Sp_zero/one`, `Rpoly_zero/one` | PROVEN | sparse-subset basics |
| `Sp_succ_not`, `Sp_succ_mem`, `insert_injOn_Sp` | PROVEN | deletion–contraction split |
| `Rpoly_rec` | PROVEN | independence-poly recurrence (P2 crux) |
| **`T_COMB`** | **PROVEN** | **cseq w lam M = Rpoly w lam M, ∀M** |

No declaration carries `sorryAx`. There are **zero** `sorry` in the source.
`T_COMB` is the **full general-`M`** identity (deletion–contraction proof), not the
finite `T_COMB'` fallback the brief permitted.

---

## 4. `#print axioms` output (verbatim, Phase V)

```
'PcfFredholm.T_DET' depends on axioms: [propext, Classical.choice, Quot.sound]
'PcfFredholm.T_COMB' depends on axioms: [propext, Classical.choice, Quot.sound]
'PcfFredholm.Amat_det_rec' depends on axioms: [propext, Classical.choice, Quot.sound]
'PcfFredholm.Amat_inner_det' depends on axioms: [propext, Classical.choice, Quot.sound]
'PcfFredholm.Rpoly_rec' depends on axioms: [propext, Classical.choice, Quot.sound]
```

All cones ⊆ `{propext, Classical.choice, Quot.sound}`. No `sorryAx`. **PROVEN.**

---

## 5. STATEMENT-ONLY

None. Every target declaration is PROVEN.

---

## 6. OUT OF SCOPE (carried as analytic hypotheses in the companion preprint)

These are **not** formalized here and are **not** asserted as Lean theorems:

* The operator limit `T_M → T` (Hilbert–Schmidt), trace-class `T²`, and the
  Fredholm-determinant convergence `det(I + lam·T_M²) → det(I + lam·T²)`. Carried
  as the analytic hypothesis, exactly as EBR carries Borel-summability
  cited-conditional. The finite identities (`T_DET`, `T_COMB`) are the PROVEN
  deliverable; the limit is STRUCTURAL in the companion preprint.
* The trace formula `delta = (1/2) Σ (-1)^{m+1} Tr T^{2m} / m` and the
  central-binomial leading law. Numerics live in P0; not formalized here.

## 7. DEFERRED (dependency-ordered)

* **T_SYM** (STRUCTURAL, optional): `c M ^ 2 = det (I + lam • (Tsym_M)²)` with the
  symmetric `sqrt(w)`-weighted zero-diagonal tridiagonal matrix. **Deferred.**
  It requires real `sqrt` machinery (`Real.sqrt`, `R := ℝ`), which is heavier than
  the general-`R` core and is not needed for the headline identity: `(T_DET)` +
  `(T_COMB)` already give the finite identity in the `-1`/super-diagonal
  convention. To pick up later: instantiate `R := ℝ`, define `Tsym_M i j = sqrt (w·)`
  on the off-diagonals, and relate `det (I + lam • Tsym²)` to `(cseq)²` via a
  diagonal similarity `D Tsym D⁻¹` matching the asymmetric `Amat` (`D = diag √(w)`
  telescoping), then apply `T_DET`. Dependency: only the already-proven `T_DET`.
