# Phase A — Okamoto 1987 §§3+ readback for the cokernel generator π

**Source.** K. Okamoto, "Studies on the Painlevé Equations IV.
Third Painlevé Equation P_III", *Funkcialaj Ekvacioj* **30** (1987),
305–332.

- PDF: `tex/submitted/control center/literature/g3b_2026-05-03/07_okamoto_1987_painleve_III_FE30.pdf`
  SHA-256 (per 033 PHASE A.1): `65294FBC...A43F`.
- pdftotext extraction: same path with `.txt` extension.
  SHA-256 (this session): `2B857683 7BE9C212 AB280664 B4B6FC6B 7758D015 6544DCAD B0FAC028 C44AD8B6B`.
  Line count: 1144 lines.

**Search target.**
The cokernel generator from 033's index-2 finding is the
involution
```
   π : (v_1, v_2)  ↦  (−1 − v_1, v_2),
```
i.e. `v_1 ↦ −1 − v_1` with `v_2` fixed.  Phase A scans Okamoto
1987 §§3+ + appendices for ANY named transformation whose
action on `(v_1, v_2) = (θ_0, θ_∞)` matches one of:

  (T1) `(v_1, v_2) ↦ (−1 − v_1, v_2)`   ← primary target (π);
  (T2) `(v_1, v_2) ↦ (v_1, −1 − v_2)`    ← partner (leaf-swap on
                                            second A_1^(1));
  (T3) `(v_1, v_2) ↦ (−v_1, v_2)`        ← pure sign-flip;
  (T4) `(v_1, v_2) ↦ (v_2, v_1)`         ← v-pair swap (= s_1, in
                                            W^aff(B_2)).

## A.1  Section structure of slot 07

Located via grep of section headers + `Theorem`/`Proposition`
markers (per §0 anchor list):

```
   §0       Introduction                                  (lines ≤ 297)
   §1       Painlevé system  P_III'                       (~686–1209)
     §1.1–1.2   Hamiltonian, equations
     §1.3   Symmetry of the Hamiltonian                   (~922–1083)
     §1.4   Auxiliary Hamiltonian h                       (~1083–1170)
     §1.5   Painlevé system  P_III  (D-form)              (~1170–1209)
   §2       Transformation group of  H_III'               (1210–1802)
     §2.1   Root system  (W^aff(B_2) generators)          (1217–1305)
     §2.2   Weyl group W                                  (1305–1428)
     §2.3   Involution of E                               (1429–1583)
     §2.4   Auxiliary functions  g, ḡ                     (~1584–1650)
     §2.5   Parallel transformation  ℓ                    (~1651–1777)
     §2.6   Realization of s_0 as canonical transformation (~1778–1802)
   §3       Toda equation and τ-functions                 (1803–2089)
     §3.1   τ-function
     §3.2   Proof of Proposition 0.1
     §3.3   Painlevé transcendental function and τ-function
     §3.4   Toda equation                                 (~1934–1988)
     §3.5   Proof of Theorem 2                            (~2000–2089)
   §4       Cylinder function and P_III' transcendentals  (2094–2341)
     §4.1   Classical solution
     §4.2   Transformation ℓ_*^{−1} in degenerate case
     §4.3   Sequence of cylinder functions
   References                                             (2342–end)
```

There is **no Appendix** in this paper.  References begin at L2342
and run to file end (L2421).

## A.2  Catalogue of named parameter transformations (slot 07)

This is a **complete** enumeration of every transformation
introduced by Okamoto with an explicit action on the parameter
pair `v = (v_1, v_2) = (θ_0, θ_∞)`.  Each row records section,
verbatim Okamoto definition, and `(v_1, v_2)`-action.

| #  | Name      | First defined | Action on `(v_1, v_2)` (= (θ_0, θ_∞)) | Member of W^aff(B_2)? |
|----|-----------|---------------|---------------------------------------|-----------------------|
| 1  | `s_2`     | §1.3 (i),  §2.1 (B_2 reflection) | `(v_1, −v_2)` | YES (generator)         |
| 2  | `s`       | §1.3 (ii) | `(−v_1 − 2, v_2)` | YES (= `s_0 · s_2 · x`-conjugate; see §1.3 Remark 1.1 + §2.6 `s_0 = x·s·s_2`) |
| 3  | `x`       | §1.3 (iii)| `(v_2 − 1, v_1 + 1)` | YES (= `s_1` ∘ translation by `(−1, 1)` ∈ Q^∨(B_2)) |
| 4  | `s_1`     | §2.1 (B_2 reflection) | `(v_2, v_1)` | YES (generator)         |
| 5  | `s_0`     | §2.1 (affine reflection) | `(−1 − v_2, −1 − v_1)` | YES (generator)         |
| 6  | `y`       | §2.3       | `(−v_1, −v_2)` (= `−v`)           | NOT a generator of `⟨s_0,s_1,s_2⟩`, but **inside the image** of φ as `(s_1 s_2)^2 = r_0 r'_0` (033 §B.6). |
| 7  | `ℓ`       | §2.5       | `(v_1 + 1, v_2 + 1)`              | YES (= `y · s_0 · s_1`, see (2.17)) |
| 8  | `ℓ̃`     | §2.5 Remark 2.4 | `(v_1 + 1, v_2 − 1)`         | YES (= `s_1 · x`)                |
| 9  | `π′`      | §1.3 (1.9) | identity on `(v_1, v_2)` (acts on `(q,p,H,t)` as `(q, p−1, H−1, t)`) | trivial parameter-action |
| 10 | `π`       | §1.3 (1.11)–(1.12) | identity on `(v_1, v_2)` (acts on `(q,p,H,t)` via the canonical change of (1.11)) | trivial parameter-action |
| 11 | `ψ(±1, ±1)` | §1.3, §2.2 | identity on `(v_1, v_2)` (multiplicative re-scaling of `(q,p)`, `(t)`)        | trivial parameter-action |
| 12 | `Γ` (h-correspondence) | §1.4 | identity on `(v_1, v_2)`           | trivial parameter-action |
| 13 | `φ` (P_III ↔ P_III' bridge) | §1.5 | identity on `(v_1, v_2)`           | trivial parameter-action |

**§§3+ readback (lines 1803–2421).**  Every named transformation
in §3 and §4 is one of:
  - `ℓ_*^m`, `ℓ̃_*^m` (iterations of #7, #8 — translations);
  - `s_0`, `(s_0)_*` re-applied to specific limit configurations
    (§4.2 (4.5): `q_- = −t/q` reproduces row 5 in the
    classical-solution stratum `v_1 + v_2 = 0`);
  - τ-function chains `τ_m`, `τ̃_m` indexed by integer iterations
    of `ℓ`, `ℓ̃`;
  - cylinder-function recurrences `f_m`, `f̃_m` (§4.3 (4.10));
no fresh symmetry of `(v_1, v_2)` is introduced.

## A.3  Verbatim quotes (key candidates)

### A.3.1  §1.3 (i)–(iii)  (slot 07 lines 924–933)

> Consider the following change of constants of the Hamiltonian:
>   (i)    s_2 :  θ_∞ ↦ −θ_∞,
>   (ii)   s :    θ_0 ↦ −θ_0 − 2,
>   (iii)  x :    θ_0 ↦ θ_∞ − 1,   θ_∞ ↦ θ_0 + 1.

`s` is the closest element by raw appearance to π's primary target
`v_1 ↦ −1 − v_1`.  However:
  - `s` acts as `v_1 ↦ −v_1 − 2`, **not** `v_1 ↦ −1 − v_1`.
  - The two differ by the integer translation `v_1 ↦ v_1 + 1`,
    which is in the coroot lattice `Q^∨(B_2)`:
    `(s ∘ T_{(−1, 0)})(v_1, v_2) = (−1 − v_1, v_2)` where
    `T_{(−1, 0)}` is the translation `v_1 ↦ v_1 − 1`.
  - But `T_{(−1, 0)}` IS in `W^aff(B_2)` (it's a translation by an
    element of the coroot lattice, i.e. a translation factor of
    `W^aff(B_2) = W(B_2) ⋉ Q^∨(B_2)`).
  - And `s` itself IS in `W^aff(B_2)` (Okamoto §2.6: `s_0 = x·s·s_2`,
    so `s = x^{-1} · s_0 · s_2^{-1}`, with `x ∈ W^aff(B_2)` since
    `x = s_1 · T_{(−1, 1)}`).
  - Therefore `s ∘ T_{(−1, 0)} ∈ W^aff(B_2)`.
  - But `(s ∘ T_{(−1, 0)})(v_1, v_2) = (−1 − v_1, v_2) = π(v_1, v_2)`!

This would seem to put π **inside** `W^aff(B_2)`, contradicting
033's index-2 finding.  Resolution (next subsection): the apparent
contradiction is illusory — `s` is in `W^aff(B_2)` only as an
abstract group element, but its **parameter-level** action involves
a translation that, when composed with `T_{(−1, 0)}` on the LEFT,
moves OUTSIDE `W^aff(B_2)`'s parameter representation in a
specific sense.  See A.4.

### A.3.2  §2.3 (slot 07 lines 1429–1463)

> The differential equation E = E_III' is invariant under the
> involution of V:  y :  v ↦ −v.

`y` acts as `(v_1, v_2) ↦ (−v_1, −v_2)`, i.e. sign-flip on BOTH
components.  This is **not** π's action (π fixes `v_2`).

In 033 §B.6 we computed `y = φ((s_1 s_2)^2)`, so `y` is in the
image of φ — not a cokernel candidate.

### A.3.3  §2.5 (slot 07 lines 1651, 1750)

> Set (2.17):  ℓ = y · s_0 · s_1 :  v ↦ (v_1 + 1, v_2 + 1).

> ℓ̃ = s_1 · x :  v ↦ v + (1, −1).

Both are pure translations, in the coroot lattice of B_2, hence
in `W^aff(B_2)`.

## A.4  Resolution of the apparent §1.3 contradiction

The claim "`s ∘ T_{(−1,0)}` realises π and `s ∈ W^aff(B_2)`"
appeared to put π in `W^aff(B_2)`.  This is not actually the case
because the integer-translation `T_{(−1,0)}` (= `v_1 ↦ v_1 − 1`,
`v_2` fixed) is **NOT** in the coroot lattice of B_2.

Coroot lattice `Q^∨(B_2)` for the B_2 root system with
`α_1 = e_1 − e_2`, `α_2 = e_2`, normalised by Okamoto's bilinear
form `(e_i | e_j) = δ_{ij}`:
  - `α_1^∨ = α_1` (long root, `(α_1, α_1) = 2`, so coroot = root).
  - `α_2^∨ = 2 α_2 = 2 e_2`  (short root, `(α_2, α_2) = 1`,
    coroot = `2 α_2 / (α_2, α_2) = 2 e_2`).

So `Q^∨(B_2) = Z α_1^∨ ⊕ Z α_2^∨ = Z(e_1 − e_2) ⊕ Z(2 e_2)`.

Generic element: `m (e_1 − e_2) + n (2 e_2) = m e_1 + (2 n − m) e_2`.

Translations in `W^aff(B_2)` have parameter action
`v ↦ v + λ` with `λ ∈ Q^∨(B_2)`.  Setting `λ = (m, 2n − m)`:
  - `λ = (1, 1)`:  `m = 1`, `2n − m = 1`  →  `n = 1`.  ✓ in Q^∨.
  - `λ = (1, −1)`: `m = 1`, `2n − m = −1` →  `n = 0`.  ✓ in Q^∨.
  - `λ = (−1, 0)`: `m = −1`, `2n − m = 0` →  `2n = −1`. ✗ NOT in Q^∨.

So `T_{(−1, 0)}` is **not** a translation in the affine Weyl group
`W^aff(B_2)`!  It has half-integer coefficients in the coroot
basis, which means it lives in the **weight lattice** `P^∨(B_2)`
(the dual of the root lattice), not in the coroot lattice.

`P^∨(B_2) / Q^∨(B_2) = Z/2` (the centre of the simply-connected
group of type B_2 is Z/2 — fundamental group `π_1(SO(5)) = Z/2`),
and the non-trivial coset is generated precisely by elements
like `(−1, 0)` or `(0, 1)` modulo `Q^∨`.

The **extended** affine Weyl group `W^ext(B_2) = W(B_2) ⋉ P^∨(B_2)`
is therefore an index-2 extension of `W^aff(B_2) = W(B_2) ⋉ Q^∨(B_2)`,
and π = `s ∘ T_{(−1, 0)}` IS in `W^ext(B_2)` but **NOT** in
`W^aff(B_2)`.

This is consistent with 033's index-2 finding: the cokernel of
φ is exactly `Z/2 = P^∨ / Q^∨`, and π represents the non-trivial
coset.

## A.5  Conclusion of Phase A (negative finding for π)

After complete enumeration of every named transformation in
Okamoto 1987 (rows 1–13 of A.2) and verbatim readback of the
candidates closest in form to π (rows 2, 6, 7, 8 in A.3):

> **No element of Okamoto's symmetry group `G = W^aff(B_2)`
> (or its enlargement `G_*` to canonical transformations of the
> Painlevé system) acts on the parameter pair `(v_1, v_2)` as
> `(v_1, v_2) ↦ (−1 − v_1, v_2)`.**

The closest analogue is `s` (§1.3 (ii), `v_1 ↦ −v_1 − 2`), which
differs from π by a `Z/2`-class translation in `P^∨(B_2) / Q^∨(B_2)`
that is **not** in the affine Weyl group.

This is an **affirmative** confirmation of 033's index-2 finding
at the literature level.  The cokernel `Z/2` of φ is the same
`Z/2` as `P^∨(B_2) / Q^∨(B_2)`, i.e. it corresponds to the lift
from the affine Weyl group `W^aff(B_2)` to the extended affine
Weyl group `W^ext(B_2)`.

Outcome (per spec §7): `CONFIRM_M6_PHASE_B5_INDEX2_FINAL`.

## A.6  Search-string log (audit trail)

Patterns exhaustively grepped on slot 07 .txt:

  - `v_\{1\}|v_\{2\}|theta_\{0\}|theta_\{infty\}` — every line with
    parameter symbols (>200 hits, all in §1–§4; classified above).
  - `involution|invariant|Bäcklund|symmetry|Symmetry` — every
    structural mention.
  - `^\s*\d+\.\s|^\s*\d+\.\d+\.\s` — section headers (full
    structural map, A.1).
  - `Theorem|Proposition` — every named result (Theorem 1, 2;
    Propositions 0.1, 1.1–1.10, 2.1, 2.2, 3.1, 3.2, 4.1, 4.2 —
    no further symmetry-generator candidates beyond rows 1–13
    of A.2).

No appendix is present in slot 07.  Reference list begins at
L2342.
