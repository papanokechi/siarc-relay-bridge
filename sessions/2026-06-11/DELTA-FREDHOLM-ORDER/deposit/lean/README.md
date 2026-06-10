# pcf-fredholm — Lean 4 core of the pcf-delta Fredholm determinant identity

Machine-checked **finitary core** of the determinant identity underlying the
Fredholm representation of the pcf-delta growth constant. The numerics were
validated independently in session **DELTA-FREDHOLM-P0** (VERIFIED to 65 digits by
two channels); this project proves the finite algebraic identities in Lean 4 /
Mathlib with a clean axiom cone.

## Verdict

**PROVEN.** Both headline theorems hold with axiom cone ⊆
`{propext, Classical.choice, Quot.sound}` and **no `sorryAx`** (zero `sorry` in
source):

* **`T_DET`** : `det (Amat w lam M) = cseq w lam M` for all `M`, over any
  `CommRing R`. The verbatim tridiagonal determinant equals the load-bearing
  continuant.
* **`T_COMB`** : `cseq w lam M = Rpoly w lam M` for all `M` — the continuant equals
  the weighted independence (sparse-subset) polynomial of the path on `{2,…,M}`.
  Proved in **full general `M`** by deletion–contraction (not the finite fallback
  the brief permitted).

Together they give the headline finite identity
`det (Amat w lam M) = Rpoly w lam M` in the `-1`/super-diagonal convention.

### G0 falsification finding (reported, not papered over)

The brief's G0 base case `c 1 = 1 + lam·w 1` is **wrong** for the verbatim matrix:
`Amat w lam 1 = [1]`, so `det = 1`. The corrected, self-consistent base case is
`c 1 = 1`; then `cseq w lam M` is exactly the path-`{2,…,M}` independence
polynomial (the P0 object). Lean witnesses: `g0_det_one`, `g0_brief_base_is_wrong`.
See `SCOPE.md §2`.

## Build instructions

Toolchain is **pinned** (do not float): `leanprover/lean4:v4.30.0`, Mathlib
`v4.30.0` (`lake-manifest.json` rev `c5ea00351c28e24afc9f0f84379aa41082b1188f`).

```sh
cd lean/pcf-fredholm
lake exe cache get      # fetch prebuilt Mathlib oleans (~once)
lake build              # builds PcfFredholm.Core; prints the axiom cones
```

The `#print axioms` audit (Phase V) runs at the end of `PcfFredholm/Core.lean` and
emits, verbatim:

```
'PcfFredholm.T_DET'        depends on axioms: [propext, Classical.choice, Quot.sound]
'PcfFredholm.T_COMB'       depends on axioms: [propext, Classical.choice, Quot.sound]
'PcfFredholm.Amat_det_rec' depends on axioms: [propext, Classical.choice, Quot.sound]
'PcfFredholm.Amat_inner_det' depends on axioms: [propext, Classical.choice, Quot.sound]
'PcfFredholm.Rpoly_rec'    depends on axioms: [propext, Classical.choice, Quot.sound]
```

## Locked convention (G0)

Over a commutative ring `R`, weights `w : ℕ → R`, activity `lam : R`:

```
cseq:  c 0 = 1,  c 1 = 1,  c (n+2) = c (n+1) + lam * w (n+2) * c n
Amat:  A i i = 1,  A i (i+1) = lam * w (i+2),  A (i+1) i = -1,  else 0
Rpoly: R_M = Σ_{S ⊆ {2..M}, sparse} Π_{i∈S} lam * w i
```

## Four-class grading

| Class | Declarations |
|---|---|
| **PROVEN** (cone clean, no sorryAx) | `T_DET`, `T_COMB`, `Amat_det_rec`, `Amat_inner_det`, `Rpoly_rec`, all G0 lemmas, all helpers — **every declaration in the file** |
| **STATEMENT-ONLY** (named sorry) | none |
| **VERIFIED-finite** (decide/norm_num at finite M) | none — `T_COMB` was upgraded to full general-`M` PROVEN |
| **OUT-OF-SCOPE / DEFERRED** | operator/Fredholm limit and trace formula (carried as analytic hypotheses); `T_SYM` symmetric squared form (deferred, needs real `sqrt`) |

## Honest limitations

* The headline is the **finite, algebraic** identity. The analytic passage to the
  Fredholm determinant — `T_M → T` (Hilbert–Schmidt), trace-class `T²`,
  `det(I+lam·T_M²) → det(I+lam·T²)` — is **OUT OF SCOPE** and carried as the
  analytic hypothesis in the companion preprint (cf. EBR's cited-conditional
  Borel-summability). It is **not** asserted as a Lean theorem here.
* The trace formula `delta = (1/2) Σ (-1)^{m+1} Tr T^{2m}/m` and the
  central-binomial leading law are P0 numerics, **not** formalized here.
* **`T_SYM`** (`c M² = det(I + lam • Tsym_M²)`) is **deferred**: it needs the real
  `sqrt`-weighted symmetric matrix, heavier than the general-`R` core and not
  required for the headline. See `SCOPE.md §7` for the pick-up plan (depends only
  on the already-proven `T_DET`).

## Files

| Path | Contents |
|---|---|
| `PcfFredholm/Core.lean` | definitions (`cseq`, `Amat`, `Sp`, `Rpoly`), G0 gate, `T_DET`, `T_COMB`, axiom-cone audit |
| `PcfFredholm.lean` | root import |
| `SCOPE.md` | locked convention, falsification finding, axiom output, grading, scope/deferred |
| `claims.jsonl` | one entry per target declaration (`evidence_type: "build"`, axiom cone, sorry count) |
| `lakefile.toml`, `lean-toolchain`, `lake-manifest.json` | pinned toolchain (committed) |
