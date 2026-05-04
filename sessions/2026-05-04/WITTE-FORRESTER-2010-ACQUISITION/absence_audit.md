# Absence Audit — W(B_2) ↔ W((2A_1)^(1)) Homomorphism in Forrester-Witte 2005 substitute

**Substitute paper:** Forrester & Witte, "Boundary conditions associated with
the Painlevé III' and V evaluations of some random matrix averages", arXiv:math/0512142,
J. Phys. A 39 (2006) 28 S13. DOI 10.1088/0305-4470/39/28/S13.

**Substitute SHA-256:** 80E050092174159A4D7DCE3F5E8436DAA0C3A5502830178FE3ACCAB8AF83CB61
**Text extracted:** `substitute_FW_2005_PIIIp_boundary.txt`, 766 lines, 52445 B.

**Note on scope.** This audit examines a **substitute** for the spec primary
target. The spec target (J. Phys. A 43 (2010) 235202 / arXiv:0911.1762) does
not exist (see `discrepancy_log.json`). The substitute is the closest
thematic Forrester-Witte PIII' paper available.

---

## 1. Sections read

The full text was full-text-searched (regex). The paper has 6 sections:

  1. Introduction (L30–L136)
  2. Small s Expansion of Ẽ_{2,N}((0,s); a, μ; ξ) (L137–L406)
  3. Comparison with the Jimbo solution (L407–L522)
  4. The hard edge limit (L523–L677)
  5. Application (L678–L889)
  6. Acknowledgements (L890–L907)
  References (L908–end)

This is a 13 KB σ-form / Hamiltonian PIII'/PV boundary-condition paper. Topic
of every section is small-s asymptotics of σ_PV / σ_PIII' transcendents and a
Hankel-determinant application to Conrey-Rubinstein-Snaith zeta-derivative.

## 2. Symbols searched (regex, full document)

| Pattern                                  | Hits |
|------------------------------------------|------|
| `B_2` / `B_{2`                           | 0    |
| `(2A_1)` / `2A_1` / `tilde A_1` / `2A1`  | 0    |
| `D_6` / `D^{(1)}_6`                      | 0    |
| `Sakai`                                  | 0    |
| `Weyl`                                   | 0    |
| `homomorphism` / `isomorphism`           | 0    |
| `surface` (Sakai-surface sense)          | 0    |
| `root system` / `simple root`            | 0    |
| `Dynkin`                                 | 0    |
| `reflection` (Weyl-reflection sense)     | 0    |
| `Lie` (Lie-algebra sense)                | 0    |
| `Okamoto`                                | 2 (both in "Jimbo-Miwa-Okamoto σ-form", citing the Hamiltonian, not the W(B_2) Weyl-group structure) |

## 3. Findings

### 3.1 The W(B_2) ↔ W((2A_1)^(1)) homomorphism is NOT stated in this paper.

The substitute paper is exclusively in the σ-form / Hamiltonian framework
(`σ_PIII'(s)`, `σ_PV(s)`, Jimbo small-s expansion, Hankel determinant
applications). It does not invoke either the W(B_2) framing of Okamoto 1987
or the W((2A_1)^{(1)}) framing of Sakai 2001. It cites Okamoto only via the
"Jimbo-Miwa-Okamoto σ-form" name attached to the Painlevé Hamiltonians; this
is bibliographic/historical citation, not a use of Okamoto's Weyl-group
machinery.

### 3.2 This is consistent with the broader Forrester-Witte PIII' oeuvre.

The closest cousins (math-ph/0203049 OE/SE τ-functions; math-ph/0201051 PV/PIII
applications to LUE/JUE/CUE) likewise work entirely in the σ-form /
Hamiltonian / boundary-condition framework. Sakai's 2001 surface-type
classification and the W((2A_1)^{(1)}) extended affine Weyl group of PIII'
do not appear in their abstracts or titles, and the conventions translation
question is not their subject.

### 3.3 Convention-translation comment

In σ-form, the PIII' and PV equations are second-order ODEs in σ(s). The
parameter set in this framework is `(a, μ, ξ)` (matrix-ensemble parameters),
not the `(b_1, b_2, ...)` or `(θ_0, θ_∞, ...)` set of the Okamoto/Sakai Weyl
frameworks. This is why the W(B_2) ↔ W((2A_1)^{(1)}) homomorphism is invisible
in the paper: the framework simply does not need it.

## 4. Cross-walk to Phase 029 (NOUMI-YAMADA-2004-ACQUISITION) negative finding

Phase 029 confirmed:
- Noumi-Yamada 2004 AMS book TOC has no PIII chapter.
- KNY 2017 (geometric aspects) has 0 occurrences of `B_2` as Lie-group symbol.
- NY 1998 / NY 2000 OA preprints similarly do not state the homomorphism.

This audit (Phase 031 substitute) adds Forrester-Witte 2005 (the closest
thematic surrogate for the non-existent spec target) to the list of
PIII'-σ-form papers that **do not** state the W(B_2) ↔ W((2A_1)^{(1)})
homomorphism.

## 5. Implication for M6 Phase B.5

The homomorphism is **not** primary-source citable from the post-Sakai
PIII'/τ-function literature accessed so far (Sakai 2001 + Okamoto 1987 +
KNY 2017 + NY 1998 + NY 2000 + Forrester-Witte 2005). It is plausibly
folklore, but folklore is not theorem-grade.

**Recommendation:** pivot M6 Phase B.5 W cross-walk closure to the SIARC
primary-derivation route, as 029 already noted. The lit-hunt has
exhausted the most-thematically-aligned author corpus (Forrester-Witte +
Noumi-Yamada). Tier-3 lit-hunt options (Conte-Musette ch.6, Joshi-Mazzocco
2003) remain available but are speculative; given the σ-form vs.
Sakai-framework gap is structural, the SIARC primary derivation is the
expected close path.

## 6. Honest re-statement

Given that the spec target does not exist, the negative finding above is
necessarily indirect: it shows the homomorphism is not stated in the **closest
substitute**. It does not prove the homomorphism is absent from the (non-existent)
spec target. The conclusion stands by virtue of the broader oeuvre pattern,
not via direct verification of the spec target.
