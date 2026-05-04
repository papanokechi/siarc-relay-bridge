# Absence audit — W(B_2) ↔ W((2A_1)^(1)) homomorphism in Noumi-Yamada-family OA literature

Task: NOUMI-YAMADA-2004-ACQUISITION
Date: 2026-05-04
Spec: §2 Phase D (D.1 - D.6); D.6 absence path

## Search target

The explicit isomorphism / quotient / covering / homomorphism
linking the W(B_2) action on PIII' (Okamoto 1987 §2.1, slot 07,
2-parameter (v_1, v_2) framing) to the W((2A_1)^(1)) action on the
D_6^(1) surface (Sakai 2001 Table 6, slot 13, 4-tuple (a_0, a_1,
b_0, b_1) framing).

## Sources consulted (this session)

| Slot | Source | Year | Pages | Disposition | B_2 hits | "(2A_1)" hits |
|------|--------|------|-------|-------------|----------|---------------|
| 07   | Okamoto 1987 PIII (FE30)            | 1987 | 38   | already on disk | yes (W(B_2)) | n/a (predates Sakai) |
| 08   | BLMP 2024 (PIII D_6)                | 2024 | 60+  | already on disk | n/a       | yes (transitive)     |
| 13   | Sakai 1999 preprint Kyoto-99-10     | 2001 | ~50  | already on disk | n/a       | yes (Table 6)        |
| 14   | KNY 2017 'Geometric Aspects'        | 2017 | 168  | NEW slot 14     | **0** (a) | yes (sec 8.6)        |
| 15   | NY 1998 'Affine Weyl groups, ...'   | 1998 | 16   | NEW slot 15     | **0**     | **0**                |
| 16   | NY 2000 'Birational Weyl group ...' | 2000 | 31   | NEW slot 16     | **0**     | **0**                |
| --   | NY 2004 MMONO/223 (book)            | 2004 | 156  | PAYWALL_TOC_ONLY | unknown  | unknown              |

(a) The single grep hit for "B_2" in slot 14 is a citation to
Brézin-Kazakov, Phys. Lett. **B** 236 (the journal name), not the
Lie group W(B_2).

## Verbatim grep evidence (slot 14, KNY 2017 = arXiv:1509.08186)

Surface-classification side (Sakai-style D_6^(1) / W((2A_1)^(1))):

```
Line 4963:  2A(1) (1)
Line 4964:    1  /D6     Sec. 8.1.20  Sec. 8.2.19  Sec. 8.4.17  Sec. 8.5.17  Sec. 8.6.16
Line 5307:  6 ) and P((2A1 ) /D6 ) (PIII )
Line 5318:  (ii) Painlevé differential equation: PIII6 (y = qs , s2 = t)
Line 5328:  1 /D7 ) and P( A1 /D7 ) (PIII )
Line 5340:  (ii) Painlevé differential equation: PIII7 (y = qs , s2 = t)
Line 5349:  0 /D8 ) (PIII )
Line 5356:  (ii) Painlevé differential equation: PIII8 (y = qs , s2 = t)
Line 7873:  The corresponding continuous flow is PIII6 with the Hamiltonian:
```

Okamoto-bridge side (W(B_2) framing):

```
[no hits for "B_2" / "B(2)" / "B_{2}" as Lie-group symbol]

Okamoto citation pattern:
Line  96: initiated by Okamoto [95] and subsequently extended by Sakai [112] ...
Line 116: has been initiated by Okamoto's pioneering work [95]. For each Painlevé
Line 164: sense of Okamoto and Sakai.
Line 1451: It has been observed by Okamoto for all the Painlevé differential equations
            that there is a remark[able W-symmetry...]
Line 9795: [95] K. Okamoto, Sur les feuilletages associés aux équations du second ordre
Line 9801: [97] K. Okamoto, Studies on the Painlevé equations. III. Second and fourth
            Painlevé equation, P_II and P_IV  [NOT the slot 07 PIII paper]
```

KNY 2017 cites Okamoto's PIII / PV paper [99] (Japan. J. Math. 13 (1987))
but does NOT translate Okamoto's W(B_2) generators into the modern
W((2A_1)^(1)) framework. The PIII6 / PIII7 / PIII8 sections (lines
5307-5356, 7873-8018) work entirely in the Sakai surface-classification
convention.

## Verbatim grep evidence (slot 15, NY 1998 = arXiv:math/9804132)

```
Line 25:  Painlevé equations P_II , P_III , P_IV , P_V and P_VI admit the affine
          Weyl groups of type [A_1^(1), B_2^(1) [implicit?], A_2^(1), A_3^(1), D_4^(1)]
Line 193: W -homomorphism Q → L such that ...   [generic abstract framework]
Line 487: The group W_f is now isomorphic to P ⋊ W_0, where P is the weight lattice
Line 725: elementarily. The Painlevé equation P_V is covered as the case n = 1
```

Line 25 implicitly acknowledges that PIII has SOME affine Weyl group
(by the listing pattern), but the body of the paper develops only the
A-type (A_l^(1)) construction and applies it to PII / PIV / PV. There
is NO explicit W(B_2) ↔ W((2A_1)^(1)) homomorphism statement.

## Verbatim grep evidence (slot 16, NY 2000 = arXiv:math/0012028)

```
Line 81:   for any f, g, h ∈ A. A homomorphism T : A → B between two Poisson algebras
Line 100:  define a homomorphism r_i ...
Line 177:  natural homomorphism Q → L is a W (A)-homomorphism.
Line 426:  transformations, isomorphic to the Weyl group W (G_2) [G_2 example only]
Line 524:  by ρ : W → W the homomorphism defined by ρ(s_i) = r_i (i ∈ I)
```

This paper develops the **abstract** Weyl-group → birational-action
framework (any Kac-Moody type Weyl group, realized on a nilpotent
Poisson algebra). The worked example is W(G_2) (line 426). There is NO
specialization to PIII or to W(B_2) → W((2A_1)^(1)).

## Conclusion: ABSENCE OF EXPLICIT HOMOMORPHISM

Across the three NEW slots (14, 15, 16) — which together comprise
the OA-accessible Noumi-Yamada-family literature most likely to
contain the bridge — the explicit W(B_2) ↔ W((2A_1)^(1)) homomorphism
**is not stated**.

The pattern of evidence is:
- Pre-Sakai NY (slots 15-16): work in abstract or A-type frameworks;
  do not reach the PIII/B_2 case.
- Post-Sakai NY (slot 14, KNY 2017): work entirely in the Sakai
  surface-classification convention W((2A_1)^(1)) on D_6^(1); cite
  Okamoto for foundational W-symmetry observation but do not
  retrace the historical W(B_2) → W((2A_1)^(1)) translation.

Combined with the AMS TOC (Phase A): NY 2004 has no dedicated PIII
chapter and is structured around τ-functions / Jacobi-Trudi / A-type
worked examples. The probability that the explicit bridge appears in
NY 2004 is LOW (transitive inference: it would be unusual to derive a
W(B_2) ↔ W((2A_1)^(1)) homomorphism in a book without a PIII chapter,
especially when the same author group's later 2017 review does not
contain it).

**Recommended disposition for M6 spec Phase B.5:**

- The bridge is NOT folklore-stated in OA Noumi-Yamada literature.
- The bridge is implicit in Sakai's classification-equivalence claim
  (W((2A_1)^(1)) is the affine extension of W(B_2) for rank-2
  non-simply-laced root systems, via the standard isomorphism
  B_2 ≅ C_2 and the (2A_1)^(1) interpretation as the affine extension
  of the rank-2 BC system; this is folklore-level Lie theory but is
  not written out as a theorem in PIII context).
- M6 Phase B.5 anchor cannot be theorem-grade-upgraded from these
  sources. It remains anchor-PARTIAL.

Two pathways to close M6 Phase B.5 properly:
1. **ILL of NY 2004** (operator action; verifies definitively whether
   the book contains the bridge — predicted absent but worth direct
   confirmation).
2. **Witte-Forrester 2010** (J. Phys. A: Math. Theor. 43, 235202) —
   spec §6 Phase D.6 follow-on candidate; this paper explicitly
   anchors the τ-function approach for PIII random-matrix
   applications and may contain the W cross-walk.
3. **Direct primary derivation** (separate Researcher prompt):
   write out the B_2 → (2A_1)^(1) homomorphism from the Cartan
   matrices and verify it is a group homomorphism on the Tits
   relations; this is folklore-level Lie theory but produces a
   citable statement under SIARC authorship.

## Substitution checks (Phase D.3 / D.4)

Spec asked: do NY 2004 W(B_2) generators coincide with Okamoto 1987
§2.1, and do NY 2004 W((2A_1)^(1)) generators coincide with Sakai 2001
Table 6?

Since NY 2004 was not acquired (paywall) and the Tier-2 surrogates
(slots 14/15/16) do not state these generators in the PIII context
(only in A-type or G_2 contexts), Phase D.3 / D.4 substitution checks
are **vacuous (no NY 2004 generators to compare)**.

No `discrepancy_log.json` entry is warranted from this session.

## Halt-condition check (Phase E)

§4 halt conditions tested:
- HALT_NY04_HOMOMORPHISM_DISAGREES_WITH_SAKAI_TABLE_6: not triggered
  (no NY 2004 homomorphism statement to compare).
- HALT_NY04_HOMOMORPHISM_DISAGREES_WITH_OKAMOTO_BB2: not triggered
  (same reason).
- HALT_NY04_BB2_TO_2A1_IS_NOT_GROUP_HOMOMORPHISM: not triggered (no
  homomorphism statement was tested for group-relation compatibility).

Halt log: empty (`{}`).
