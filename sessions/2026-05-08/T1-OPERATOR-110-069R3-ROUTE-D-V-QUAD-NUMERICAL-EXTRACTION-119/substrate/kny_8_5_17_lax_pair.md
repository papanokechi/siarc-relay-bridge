# Substrate A.2 — KNY 2017 §8.5.17 d-P((2A_1)^{(1)}/D_6^{(1)}) Lax pair

**Source:** `tex/submitted/control center/literature/g3b_2026-05-03/14_kajiwara_noumi_yamada_2017_geometric_aspects.txt`, lines 7869–7922.
**PDF on disk:** `tex/submitted/control center/literature/g3b_2026-05-03/14_kajiwara_noumi_yamada_2017_geometric_aspects.pdf`.
**Substrate provenance:** ON-DISK; G3 PASS at 110 fire time.
**Loaded for:** prompt 110 Phase A.2 (relay envelope SECTION 3 A.2).

---

## §8.5.17 header (verbatim, transcribed from .txt L7869–7872)

> *"d-P((2A_1)^{(1)} / D_6^{(1)}). The corresponding continuous flow is P_III^{D_6^{(1)}} with the Hamiltonian:"*

## Hamiltonian — eq. (8.237)

```
H = (1/t) { p (p − 1) q² + (a_1 + a_2) q p + t p − a_2 q }
```
(text-extract L7876)

Affine-Weyl-root constraint:
```
a_0 + a_1 = 1     (KNY §8.5.17 .txt L7913 implied)
```

Three root parameters `(a_0, a_1, a_2) ∈ ℂ³` with one linear constraint;
two degrees of freedom (q, p) plus time `t`.

## Eight-points configuration — eq. (8.238)

```
(f_i, g_i) = ((1/3, -a_2), (1, 1/3 - a_1), (0, 0), (-t/3 + 1 - a_2 - a_1))
```
(text-extract L7881; the four base points in `(f, g)` coordinates.)

## Differential Lax form — eq. (8.239)

(text-extract L7886–7892, verbatim within ≤ 50 words per ≥quote line)

> *"L_1 = {-a_2/x + pq/(x(x-q)) - t H/x²} + {(1+a_1+a_2)/x - 1/(x-q) + t/x² - 1} ∂_x + ∂_x²,"*
>
> *"L_2 = T_α - (1/(x-q))(p - ∂_x),"*
>
> *"B = ∂_t - q/(t(x-q)) (x ∂_x - q p)."*

**Structural reading:**
- `L_1` is a SCALAR 2nd-order linear differential operator in `∂_x` (a Schrödinger-type spectral problem with `x` the spectral coordinate, `t` the isomonodromic-time deformation parameter).
- `L_1 y = 0` is the spectral problem (eigenvalue-style).
- `L_2 y = 0` (with `T_α` = affine-Weyl translation operator) gives discrete Bäcklund transform direction.
- `B y = 0` defines the isomonodromic `t`-evolution.

**Singular-point structure of L_1 (read off coefficients):**
- `x = 0`: irregular singular of Poincaré rank 1 (the `t/x²` term in `∂_x` coefficient and `-tH/x²` in `y` coefficient give double pole behavior).
- `x = q`: regular singular point (apparent singularity; `1/(x-q)` simple poles only).
- `x = ∞`: irregular singular of Poincaré rank 1 (the constant `-1` term in `∂_x` coefficient gives `e^{-x}` exponential at large `x`).

**Stokes-sector structure** (Adams 1928 / Birkhoff-Trjitzinsky 1933 framework, slot 04 `wasow_1965_dover.pdf` §X canonical):
- 2 Stokes rays at `x=0` (one ray for each formal exponential `e^{±√(t)/x}` at irregular point).
- 2 Stokes rays at `x=∞` (one ray for each formal exponential `e^{±x}`).
- Standard Stokes-multiplier matrices `S_1, S_2` per anti-Stokes ray.

## Compatibility statements — text-extract L7905–7922

> *"Compatibility of L_1 y = L_2 y = 0 gives the discrete flow for T_α (= (π_1 π_2)² s_2 s_1):*
> *a_1 = a_1 + 1, a_2 = a_2 + 1, q + q̄ = -a_2/p - a_1/(p-1), p + p̄ = 1 - t/q² - (a_1 + a_2 + 1)/q."*
> *"Compatibility of L_1 y = B y = 0 gives the P_III^{D_6^{(1)}} flow with Hamiltonian (8.237)."*

## Difference Lax form — eq. (8.241)

(text-extract L7912–7920; alternative discretization in `z`)

```
L_1 = (z + a_2 - 1)/(z - g - 1) · f (T_z^{-1} - f) + f² + f(1 - a_1 - a_2 - g - z) - t + tz/(g - z) (f T_z - 1)
L_2 = T_β · T_z + (1/(z - g)) (1 - f T_z)
B   = (z + a_2)/(z - g) (f T_z - 1) + t ∂_t T_z + z T_z
```

(Compatibility `L_1, B` gives continuous P_III^{D_6^{(1)}} with same Hamiltonian (8.237).)

## Cross-reference to 058R B.3

058R B.3 anchors on (8.239) DIFFERENTIAL form (above). The SCALAR
2nd-order structure of `L_1` is the carrier of Stokes-data extraction
in Phase B/C of this 110 EXEC session. Connection to Okamoto 1987
H_III (B.1):

```
(θ_0, θ_∞)_Okamoto  ⟷  (a_1, a_2)_KNY    (mod convention shift)
a_0 + a_1 = 1                               (KNY constraint)
```

## V_quad parameter point in KNY chart

Per 105 §3.5.1 trivial relabel: `(η_∞, η_0, θ_∞, θ_0) = (1/6, 0, 0, -1/2)`.
Therefore Hamiltonian-side `(θ_0, θ_∞) = (-1/2, 0)`.
Through Okamoto-KNY `(θ_0, θ_∞) ⟷ (a_1, a_2)`:
```
a_1 = θ_0     = -1/2     (V_quad anchor)
a_2 = θ_∞     = 0        (V_quad anchor)
a_0 = 1 - a_1 = 1 - (-1/2) = 3/2    (KNY constraint)
```

(η_∞, η_0) = (1/6, 0) enter only the `t H` term scaling — they are
NOT independent KNY parameters but rescaling/normalisation; the
project records all 4 unnormalised Okamoto parameters per CT v1.3.1
§3.5.1 commentary.

## Verbatim-quote audit

All quoted blocks above are ≤ 50 words (per envelope sect. 5.E.2 / 075-J2 + 069r1 hygiene).
Total verbatim coverage: 4 quote blocks (header + Hamiltonian + Lax pair + compatibility), max length 47 words.
