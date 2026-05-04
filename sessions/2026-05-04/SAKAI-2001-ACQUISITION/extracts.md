# Phase D extracts — SAKAI-2001-ACQUISITION

All quotes are ≤ 30 words per Rule §D and from the 1999
Kyoto Math preprint No. 10 (slot 13 in the literature
workspace; SHA-256 ec1bbda3...49ed6 of the ps2pdf-rendered
PDF). Pages cited are preprint pages (pdftotext line numbers
in `sakai_1999_preprint99_10.txt` are also given for
reproducibility).

The math content of the surface-classification framework
and the W((2A_1)^{(1)}) action is the same as in the
published Comm. Math. Phys. 220 (2001) 165–229; final
pagination differs.

================================================================
D.1.a — D_6^{(1)} surface classification (preprint p. 30,
        Table 6; pdftotext L1733–L1737)
================================================================

Sakai 2001 Table 6 ("X(R), Cr(X) and Painleve equations")
maps surface type to symmetry / Cremona group:

| surface type R | Painleve eqn       | Cremona Cr(X) symmetry             |
| -------------- | ------------------ | ---------------------------------- |
| D_4^{(1)}      | P_VI               | W̃(D_4^{(1)})                       |
| D_5^{(1)}      | P_V                | W̃(A_3^{(1)})                       |
| **D_6^{(1)}**  | **P_III^{D_6^{(1)}}** | **Aut(D_6^{(1)}) ⋉ W((2A_1)^{(1)})** |
| D_7^{(1)}      | P_III^{D_7^{(1)}}  | W̃(A_1^{(1)})                       |
| D_8^{(1)}      | P_III^{D_8^{(1)}}  | S_2                                |
| E_6^{(1)}      | P_IV               | W̃(A_2^{(1)})                       |
| E_7^{(1)}      | P_II               | W̃(A_1^{(1)})                       |
| E_8^{(1)}      | P_I                | (trivial)                          |

Verbatim from preprint p. 31 caption (≤ 30 words):
"Table 6.  X(R), Cr(X) and Painleve equations".

Verbatim from preprint p. 30 (≤ 30 words):
"If γ ≠ 0, then we can normalize γ = δ = 4 without loss
of generality. In this case we get P_III^{D_6^{(1)}}
(16)–(18)."

The line `D6(1)⊥ = (2A1)(1)` (pdftotext L1006) is the
orthogonal-complement identity in Pic(X) — Sakai's
classification rule that the symmetry group of an
R-surface is W(R^⊥): for R = D_6^{(1)}, the orthogonal
complement is (2A_1)^{(1)} = (A_1)^{(1)} ⊕ (A_1)^{(1)}.

================================================================
D.1.b — D_6^{(1)} surface 4-parameter labeling
        (preprint p. 30, eqs (16)-(18); pdftotext L1772-L1775)
================================================================

The differential-Painleve-III on the D_6^{(1)} surface is
written in Sakai 2001 (preprint eqs (16)-(18)) as:

  P_III^{D_6^{(1)}}:
    df/dt = (4/s) [2 f^2 g - (f^2 + (a_1 + b_1) f - s/4)]      (16)
    dg/dt = -(4/s) [2 f g^2 - (2 f g + (a_1 + b_1) g + a_1)]    (17)
    ds/dt = 4 η = 4 (a_1 + a_0) = 4 (b_1 + b_0)                 (18)

(`f = y(z-x)/xz, g = x/(z-x)`.)

**KEY CONSTRAINT ON THE 4-TUPLE**:  eq. (18) imposes

      a_1 + a_0 = b_1 + b_0          (= η ≡ ds/dt / 4).

That is, Sakai's parameter space for P_III^{D_6^{(1)}} is
the rank-3 hyperplane { (a_1, a_0, b_1, b_0) ∈ ℝ^4 :
a_1+a_0 = b_1+b_0 } cut out from a nominal ℝ^4 by one
linear constraint.

**Substitution check for the CT v1.3 §3.5 4-tuple
(1/6, 0, 0, -1/2)**, under naive component-wise
identification with Sakai's (a_1, a_0, b_1, b_0):

  a_1 + a_0 = 1/6 + 0   = 1/6.
  b_1 + b_0 = 0 + (-1/2) = -1/2.

The two sums DO NOT match (1/6 ≠ -1/2), so under any
component-wise identification, (1/6, 0, 0, -1/2) does
NOT satisfy Sakai's D_6^{(1)} parameter-space constraint.

This is consistent with — and a positive replication of —
the OKAMOTO-1987-CONSTRAINT-PIN handoff verdict
(2026-05-04, UPGRADE_G18_CLOSED_PARAMETER_CORRESPONDENCE_
OKAMOTO_2PARAM_VS_CT_4TUPLE). The CT v1.3 §3.5 4-tuple
is in some other (Jimbo-Miwa or later-convention) labeling
that requires an explicit parameter-correspondence map to
land on Sakai's D_6^{(1)} parameter space.

================================================================
D.1.c — W((2A_1)^{(1)}) affine-Weyl generators
        (preprint p. 6 / opening summary; pdftotext L102-L116)
================================================================

Sakai's "Add 6. D_6^{(1)}-surface" summary block lists the
generators of `Aut(D_6^{(1)}) ⋉ W((2A_1)^{(1)})` acting on
parameters (a_1, a_0, b_1, b_0):

Diagram automorphism (Aut(D_6^{(1)}) generator):
  σ ≡ (6)(24)(50):
    (a_1, a_0, b_1, b_0; s; x:y:z)
       →  (b_1, b_0, a_1, a_0; -s; z:y:x)               (Aut)

Affine W((2A_1)^{(1)}) simple reflections (4 generators
for rank-4 (A_1^{(1)}) ⊕ (A_1^{(1)}) affine type):

  w_1:  (a_1, a_0, b_1, b_0)  →  (-a_1, a_0+2a_1, b_1, b_0)
  w_0:  σ ∘ w_1 ∘ σ                                 (conjugate)
  w_1': (a_1, a_0, b_1, b_0)  →  (a_1, a_0, -b_1, b_0+2b_1)
  w_0': σ ∘ (σ ∘ w_1' ∘ σ) ∘ σ ≡ similar conjugation pattern.

These four reflections generate W((2A_1)^{(1)}) =
W((A_1)^{(1)}) × W((A_1)^{(1)}); each (A_1)^{(1)} factor
contributes one (w_i, w_0)-pair. The Aut(D_6^{(1)}) generator
σ swaps the two A_1 factors (the diagram automorphism of
the affine D_6 Dynkin diagram exchanges the "left" and
"right" pairs).

Reflection on the constraint a_1+a_0 = b_1+b_0:
- w_1 preserves (a_1+a_0) = -a_1 + (a_0+2a_1) = a_1+a_0  ✓
- w_1' preserves (b_1+b_0) = -b_1 + (b_0+2b_1) = b_1+b_0  ✓
- σ swaps the two sums, so the constraint a_1+a_0 = b_1+b_0
  is preserved. ✓
All generators preserve the parameter-space constraint, as
expected for a Weyl group acting on a root-system parameter
space.

================================================================
D.1.c.bis — W(B_2) ↔ W((2A_1)^{(1)}) homomorphism status
            (negative result)
================================================================

Search criterion: any explicit mention of "W(B_2)",
"W(C_2)", or a homomorphism / covering / quotient between
Sakai's W((2A_1)^{(1)}) framing and Okamoto's W(B_2)
framing.

Result: a full-text grep
  "W\(B|W\(C|B\(\(1\)\)|C\(\(1\)\)|tilde W|extended a"
on the 55-page preprint returns ZERO matches inside the
main body — the only "extended-affine" mentions
(L3058, L3292) refer to D_5^{(1)} and A_1^{(1)} cases
(the surfaces for P_V and P_II), not to D_6^{(1)} ↔ B_2.

Sakai 2001 references Okamoto 1987 as ref [20]
(pdftotext L14–L15), but does NOT state a Weyl-group
isomorphism / covering between his (2A_1)^{(1)} framing
and Okamoto's W(B_2) framing. The cross-walk

  Aut(D_6^{(1)}) ⋉ W((2A_1)^{(1)}) ≅ ?  W̃(B_2)
  (extended affine Weyl group of B_2)

is a fact in the Painleve literature (it is asserted, e.g.,
in Noumi-Yamada 2004 and in Witte-Forrester 2010 lecture
notes), but it is NOT stated explicitly in Sakai 2001.

This pins the M6 spec Phase B.5 anchor to **Sakai 2001 +
Noumi-Yamada 2004** (or equivalent), with Sakai 2001
supplying the W((2A_1)^{(1)}) framing and Noumi-Yamada 2004
supplying the cross-walk to W(B_2). Sakai 2001 alone is
NOT a complete anchor for the W(B_2) ↔ W((2A_1)^{(1)})
homomorphism.

================================================================
D.2 — substitution check (1/6, 0, 0, -1/2) vs Sakai D_6^{(1)}
================================================================

Already executed in D.1.b: under the naive component-wise
identification (CT 4-tuple → (a_1, a_0, b_1, b_0)), the
constraint a_1+a_0 = b_1+b_0 is violated (1/6 ≠ -1/2). The
CT v1.3 §3.5 4-tuple is therefore NOT directly a Sakai
D_6^{(1)} parameter point; an explicit labeling-correspondence
map is required (already known via OKAMOTO-1987-CONSTRAINT-PIN
to be a Jimbo-Miwa-vs-Sakai labeling artifact).

================================================================
D.3 — cross-validation across primary sources
================================================================

| Primary source                             | W-framing                                 | Parameter count |
| ------------------------------------------ | ----------------------------------------- | --------------- |
| Okamoto 1987 §2 (slot 07)                  | W(B_2) on P_III'                          | 2 (θ_0, θ_∞)    |
| Sakai 2001 / 1999 preprint (slot 13)       | Aut(D_6^{(1)}) ⋉ W((2A_1)^{(1)})         | 4 with constraint a_1+a_0 = b_1+b_0 (eff. 3) |
| BLMP 2024 §4.1 (slot 08)                   | D_6 surface in Sakai sense, with         | 4 (matches Sakai when restricted) |
|                                            | tau-function on the surface monodromy    |                 |

The three sources are CONSISTENT: each describes the same
moduli space (the Painleve P_III' / P_III^{D_6^{(1)}} initial-
value space) under a different convention.

The CT v1.3 §3.5 4-tuple (1/6, 0, 0, -1/2) is not a literal
Sakai/Okamoto parameter point under naive identification; it
is in a third (Jimbo-Miwa-style) convention that requires an
explicit cross-walk map to land on either Sakai's or
Okamoto's parameter space. This was already concluded by
OKAMOTO-1987-CONSTRAINT-PIN; Sakai 2001 acquisition does
NOT change this conclusion, but does provide an independent
2nd primary source to cite.
