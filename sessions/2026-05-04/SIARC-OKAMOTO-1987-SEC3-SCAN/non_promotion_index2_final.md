# Phase B — Non-promotion writeup: π is Sakai-side / extended-affine, NOT in Okamoto's `W^aff(B_2)`

**Outcome (per spec §7):** `CONFIRM_M6_PHASE_B5_INDEX2_FINAL`.

The spec asks whether the cokernel generator
```
    π : (v_1, v_2) ↦ (−1 − v_1, v_2)
```
appears in Okamoto 1987 §§3+ + appendices as a named element of
the Painlevé symmetry group `G_* ⊃ G ≅ W^aff(B_2)`.

After complete enumeration (Phase A.2, table of 13 named
transformations) and verbatim readback of the four closest
candidates (Phase A.3, including `s` and `y`), the answer is:

> **No.**  π is not in any element listed by Okamoto in §§1–§4,
> nor in any composition of those elements.  No appendix exists
> in this paper; the reference list begins at line 2342.

This file documents:
  - Which §§/Theorems/Propositions were read (B.1).
  - Why π was not located (B.2).
  - Which methodological framing makes index-2 the **natural**
    final result, not a defect of 033's construction (B.3).
  - Recommendation for picture v1.18 / M6 spec (B.4).

## B.1  Sections read in full + audit trail

Per Phase A.1:
  - §1.1–§1.5  (lines 686–1209): Hamiltonian + auxiliary
    function setup.  All parameter transformations enumerated
    in Phase A.2 rows 1–4, 9–13.
  - §2.1–§2.6  (lines 1210–1802): the W^aff(B_2) generator
    construction.  Rows 1, 4, 5, 6, 7, 8 of A.2.  Theorem 1
    (line 1305) is the apex: `(s_i)_*`, `(s_0)_*` realise the
    Cremona representation of `G ≅ W^aff(B_2)`.  No further
    generator in §2.
  - §3.1–§3.5  (lines 1803–2089): Toda equation + τ-function
    theory.  Theorem 2 (line 1989) is about Toda from iterated
    `ℓ_*`, `ℓ̃_*`.  No new symmetry generator.
  - §4.1–§4.3  (lines 2094–2341): cylinder-function classical
    solutions, `ℓ_*^{−1}` in degenerate stratum `v_1 + v_2 = 0`.
    Proposition 4.1, 4.2.  No new symmetry generator.
  - References (lines 2342–end).
  - **No appendix** in this paper (operator-confirmed via
    structural grep on slot 07 .txt; no header matching
    `Appendix` exists).

The Phase A search exhausted every line of §3 + §4.

## B.2  Why π was not located

Because the natural Okamoto-side analogue, the involution `s`
of §1.3 (ii) (`v_1 ↦ −v_1 − 2`), differs from π
(`v_1 ↦ −1 − v_1 = −v_1 − 1`) by exactly one half-period of
the short coroot.  More precisely:

  - `s = π ∘ T_{(−1, 0)}` (verified symbolically in
    `verify_pi_outside_W_aff.py`, log line 1).
  - `T_{(−1, 0)}` = the translation `v_1 ↦ v_1 − 1`, `v_2` fixed.
  - The coroot lattice of B_2 (with Okamoto's normalisation
    `(e_i | e_j) = δ_ij`) is
        `Q^∨(B_2) = Z(e_1 − e_2) + Z(2 e_2)`
                 `= {(a, b) ∈ Z² : a + b even}`.
  - `(−1, 0)` has `a + b = −1` (odd) ⇒ **not in `Q^∨`**.
  - But `(−1, 0) ∈ P^∨(B_2) = Z²` (the full coweight lattice).
  - So `T_{(−1, 0)} ∈ W^ext(B_2) \ W^aff(B_2)`, and hence
    `π = s ∘ T_{(−1, 0)} ∈ W^ext(B_2) \ W^aff(B_2)`.

This is the lattice-theoretic explanation for 033's index-2
result: the cokernel of `φ : W^aff(B_2) ↪ Aut(D_6^(1)) ⋉ W((2A_1)^(1))`
**is** `P^∨(B_2) / Q^∨(B_2) ≅ Z/2`, and π represents the unique
non-trivial coset.  There is no element of `W^aff(B_2)` whose
parameter action is π, because that would require a translation
in `Q^∨(B_2)` with integer-odd coordinates — impossible.

## B.3  Why index-2 is the **natural** final result

Three independent pieces of evidence converge:

**(B.3.a) Lattice theory.**  For a simple Lie algebra of type
`X_r`, the index `|P^∨ / Q^∨|` equals the order of the centre
of the simply-connected group of type `X_r`, which equals the
fundamental group of the adjoint group.  For B_2 = C_2,
`P^∨(B_2) / Q^∨(B_2) = Z/2` (the centre of `Spin(5) = Sp(2)` is
`Z/2`).  This Z/2 is precisely the index-2 obstruction in 033.

**(B.3.b) Sakai surface theory (slot 13, 033 Phase A.2).**
The full Cremona group of the `D_6^{(1)}`-surface is
`Aut(D_6^{(1)}) ⋉ W((2A_1)^{(1)})`, and its Weyl-group description
(Sakai 2001, Proposition 4 + Add 6) involves both root-lattice
and weight-lattice factors of the `(2A_1)^{(1)}` system.  The
index-2 difference is exactly the "extended" vs "non-extended"
affine Weyl group ambiguity that is standard in the
isomonodromy / Painlevé literature.

**(B.3.c) Okamoto 1987 itself, §1.3 (ii).**  Okamoto presents
`s : θ_0 ↦ −θ_0 − 2` (NOT `θ_0 ↦ −1 − θ_0`).  The shift `−2`
is forced on Okamoto's normalisation by the requirement that
`s` lie in `W^aff(B_2)` (i.e., `Q^∨` translation + reflection).
A `−1` shift would lie outside `W^aff(B_2)`.  Okamoto's choice
of `−2` is therefore the **maximal** sign-flip shift consistent
with a pure-affine-Weyl-group symmetry.  The complementary
involution with shift `−1` is the one Sakai needs for the full
Cremona group, but Okamoto did not name it (because he was
working within the `W^aff(B_2)` framework, not the extended
framework `W^ext(B_2)`).

This is consistent with **the universal pattern** that Okamoto's
1987 P_III' paper, like his earlier P_IV / P_VI papers, works
within the **non-extended** affine Weyl group, leaving the
diagram-automorphism factor (which generates the `P^∨ / Q^∨`
extension) implicit.  The Sakai 2001 surface-theoretic
description, in contrast, automatically gives the **extended**
affine Weyl group via the `Aut(D_6^{(1)})` factor.  033's
construction φ bridges the two by realising `W^aff(B_2)` as an
index-2 subgroup of the Sakai full Cremona group.

## B.4  Recommendation for picture v1.18 / M6 spec

**No amendment to picture v1.18 M6 row needed.**  The current
v1.18 phrasing (per 035 deliverables, picture v1.18 §M6 row)
already classifies M6 Phase B.5 as
`STILL_PARTIAL_PENDING_PIVOT_DECISION` with the explicit
SIARC-primary derivation (033) at INDEX-2 grade as the
operator-side pivot candidate.  Phase A of 036 confirms that
**no further upgrade to STRICT_ISOMORPHISM is achievable from
Okamoto 1987 alone**, so the index-2 finding is **final at the
literature level** for the post-Sakai era's most-cited
Okamoto-side reference.

**Suggested operator-paced line edit for v1.18 M6 row text**
(optional; not required for v1.18 deposit decision):

  Add to the M6 row's "Anchors" or "Notes" column:
  > Okamoto §§3+ scan (036 SIARC-OKAMOTO-1987-SEC3-SCAN, bridge
  > 2026-05-04): exhaustive enumeration of all 13 named parameter
  > transformations in Okamoto 1987 confirms π is **not** in any
  > Okamoto-listed generator of `G ≅ W^aff(B_2)` nor any
  > composition thereof; lattice-theoretic explanation:
  > `P^∨(B_2) / Q^∨(B_2) ≅ Z/2` is the cokernel of φ.  The
  > index-2 result is final at the Okamoto-paper level; for
  > strict isomorphism, see operator-side decision branch on
  > whether to absorb the index-2 into the v1.4 §3.5
  > formulation (extended affine Weyl group) or keep it as
  > a 033-anchored side-note.

(This is a recommendation only.  Operator + Claude reconcile
on whether to apply it in a v1.19 cycle or leave it implicit.)

## B.5  AEAL-honest scope statement

Phase A's negative finding is bounded by the slot 07 readback
(pdftotext extraction; SHA-256 of .txt
`2B857683...44AD8B6B`).  The pdftotext extraction is line-
faithful for §1.3 (ii) (`s` row), §2.1 (B_2 generators),
§2.3 (y involution), §2.5 (ℓ, ℓ̃), §3.4 (Toda iteration),
§4.2 (degenerate `ℓ_*^{−1}`), §4.3 (cylinder f_m).  Equation
fragments are partially garbled (TeX-diacritic noise), but
the **named-element headers and parameter-action statements**
are clean and machine-readable.  The complete enumeration of
Phase A.2 is therefore reliable; no hidden Bäcklund table is
plausible at this level of audit.
