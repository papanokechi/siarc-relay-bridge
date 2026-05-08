# PRIORITY_1 §10 Route F substrate-paste — Sakai 2001 + KNY 2017 §8.5

**Per prompt 112 §10 protocol (lines 1049-1086)**
**Re-fire of 069r3 Q4 only.  All other questions Q1-Q3, Q5-Q8 retain
their previous verdicts.**

---

## D1 — Header / source attributions

This packet consolidates the four mathematical-content priority items
specified in prompt 112 §10 (lines 1049-1086) so that a fresh
Claude.ai T1-Synth conversation can re-fire question Q4 of the 069r3
FINAL synthesis verdict (Route F GO / NO_GO determination).  Items
(i) and (ii) are the load-bearing, pagecount-priority primitives per
the §10 dispatch:

> *"If pagecount forces a choice, prioritise (i) + (ii) over (iii) +
> (iv); re-fires Q4 only."*  — prompt 112 line 1075-1076

The §10 HALT note on substrate sufficiency reads:

> *"HALT note: TOC + abstract alone are NOT sufficient substrate for
> mechanism (c) evaluation. If the agent can paste only TOC + abstract
> due to acquisition constraints, the agent must surface this as a
> substrate-insufficient flag and synth must NOT elevate Route F
> mechanism (c) status on TOC-only evidence (per HALT-S5 surfacing-
> vs-substantiation distinction)."*  — prompt 112 lines 1078-1085

**HALT-S5 substrate-insufficient discipline cleared:**  the substrate
quoted below is mathematical content (root-system decompositions,
Cremona-action table row, equations of motion, Cartan matrix,
explicit reflection action on parameters, Hamiltonian, base-point
configuration, Lax operators, discrete shift action), not TOC or
abstract.  HALT-S5 does not apply.

### Source attributions (4 SHAs, computed at fire time)

All four SHA-256 hashes computed fresh at packet-build time
(2026-05-08), not copy-pasted from prompt 113.

| Slot | Source                                                   | SHA-256 (fresh) |
|------|----------------------------------------------------------|-----------------|
| S1   | `extract_sakai_2A1_generators.md` (W((2A_1)^{(1)}) extraction, 058 phase A.2; primary for items (i)+(ii)) | `2CC9395BFF74B1C4B0522C98AAA712821C5EADA073E226CEC4341C1E536BB007` |
| S2   | `14_kajiwara_noumi_yamada_2017_geometric_aspects.txt` (KNY 2017 §8.5.17 .txt extract; primary for item (iii)) | `AAA2B0958F22BB03783FC76C9FE51B35F38ED39D849900DA6A9C044267CE3A2F` |
| S3   | `13_sakai_1999_preprint_kyoto99_10.pdf` (Sakai 1999 Kyoto preprint No. 99-10; anchor only — extraction at S1) | `EC1BBDA3B77634E6DEF2A784D04947A0C9631BFADE48C72AA0767B22AAF49ED6` |
| S4   | `phase_b_canonical_map.md` (058R Phase B; primary for item (iv) cross-walk + V_quad null-sum anchor) | `F831F9BD58D1F3064873DFDEAB14C003BF441CBB3832E02B6CDDC94A91FF8BB3` |

S3 SHA matches the canonical anchor `EC1BBDA3...` named in prompt 113
G4 (bibliographic-identifier pre-verification rule, post-031 verdict).
The Sakai 2001 published version (DOI `10.1007/s002200100446`) is
not used as anchor for this paste packet; the Kyoto preprint version
(99-10, 1999) is the on-disk substrate and is sufficient for the
W((2A_1)^{(1)}) generator quotes below.

Bridge HEAD at packet-build time:
`1eed8ef1475293880a23a1d038369c0bb11a6979`
(`T2-113-COPILOT-RESEARCHER-PROMPT-DRAFT-125` LANDED).
Ancestry of `ae5b7f7` (T1-SYNTH-069R3-FINAL-VERDICT-ABSORPTION-124)
checked: PASS.

### Convention legend used throughout this packet

| Symbol set                                      | Source                                                              |
|-------------------------------------------------|---------------------------------------------------------------------|
| `(a_0, a_1, b_0, b_1)` with `a_0+a_1 = b_0+b_1 = 1` | Sakai 2001 (preprint Kyoto 99-10) §3 / Add 6 — see D2, D3.        |
| `(a_1, a_2)` (Hamiltonian parameters) + discrete shift orbit index | KNY 2017 §8.5.17 — see D4.                            |
| `(η_∞, η_0, θ_∞, θ_0)`                          | Okamoto 1987 §1.1 H_{III} canonical (058R §B.1).                    |
| `(α_∞, α_0, β_∞, β_0)`                          | CT v1.3 §3.5 V_quad parameter 4-tuple (058R §B.3).                  |

The convention cross-walk between these four sets is the subject of
D5 (item (iv)).  The packet keeps each source's native convention in
its respective verbatim quote and cross-walks only at the level of
naming; no re-derivation is attempted (per §10 priority discipline).

---

## D2 — Section (i): Sakai 2001 §3 / Add 6 — D_6^{(1)}-surface-type row

**Item (i) — load-bearing per pagecount-priority rule (prompt 112
line 1075-1076).**

This section presents the surface-type classification primitive that
attaches the D_6^{(1)} surface to P_III(D_6) and identifies the
Cremona-action group as `Aut(D_6^{(1)}) ⋉ W((2A_1)^{(1)})`.  The
substrate is the verbatim quote from `extract_sakai_2A1_generators.md`
§A.2.1 + §A.2.2 (lines 11-35 of S1), itself transcribed from Sakai
1999 Kyoto preprint Add 6 (p. 40-41) and Table 6 (p. 31).

### D2.1 — δ(D_6^{(1)}) decomposition + (2A_1)^{(1)} simple-roots block

Verbatim from S1 §A.2.1 (lines 11-29 of `extract_sakai_2A1_generators.md`):

```
## A.2.1 Verbatim quote — D_6^{(1)}-surface entry (Add 6, p. 40–41)

Transcribed from `pdftotext -layout` extraction (lines ≈1100–1116):

> Add 6.  D_6^{(1)}-surface:
>     δ(D_6^{(1)}):  D_1 = E_0 − E_1 − E_2 − E_3;  D_2 = E_3 − E_8;
>                    D_3 = E_2 − E_3;
>                    D_4 = E_1 − E_2;  D_5 = E_0 − E_1 − E_4 − E_5;
>                    D_6 = E_0 − E_1 − E_6 − E_7;
>                    D_0 = E_8 − E_9;
>                    δ = D_1 + 2 D_2 + 2 D_3 + 2 D_4 + D_5 + D_6 + D_0;
>
>    D_6^{(1)⊥} = (2 A_1)^{(1)}
>      δ((2 A_1)^{(1)}):
>           α_1   = E_4 − E_5;
>           α_0   = 3 E_0 − E_1 − E_2 − E_3 − 2 E_4 − E_6 − E_7 − E_8 − E_9;
>           α'_0  = E_6 − E_7;
>           α'_1  = 3 E_0 − E_1 − E_2 − E_3 − E_4 − E_5 − 2 E_6 − E_8 − E_9;
>           δ = α_1 + α_0 = α'_1 + α'_0.
```

Key primitives surfaced by this quote:

- **Surface-type lattice generators:**  the seven divisor classes
  `D_0, D_1, …, D_6` define the D_6^{(1)} surface-type lattice.
- **Imaginary-root expansion:**  `δ = D_1 + 2 D_2 + 2 D_3 + 2 D_4 +
  D_5 + D_6 + D_0` is the affine null root in surface-lattice
  coordinates (the prompt 113 D2 deliverable note refers to this
  expansion as `2(E_1+E_2)+E_3+E_4+E_5+E_6` "or equivalent as written
  in the extract"; the form on disk is the divisor-class form quoted
  above).
- **Orthogonal-complement identification:**  `D_6^{(1)⊥} = (2 A_1)^{(1)}`.
- **Four simple roots of (2A_1)^{(1)}:**  `α_0, α_1, α'_0, α'_1`,
  with the explicit imaginary-root identity `δ = α_1 + α_0 =
  α'_1 + α'_0` (one identity per A_1^{(1)} component).

### D2.2 — Cremona-action table row (Sakai 2001 Table 6, p. 31)

Verbatim from S1 §A.2.2 (lines 31-35 of `extract_sakai_2A1_generators.md`):

```
## A.2.2 Verbatim quote — Cremona group (Table 6, p. 31)

> the type of surface     D_6^{(1)}
> Painlevé equation       P_III  (= P_III' / D_6^{(1)})
> Cremona action          Aut(D_6^{(1)}) ⋉ W((2 A_1)^{(1)})
```

This is the table row that identifies the surface-type / Painlevé /
Cremona-action triple `(D_6^{(1)}, P_III^{D_6^{(1)}}, Aut(D_6^{(1)})
⋉ W((2A_1)^{(1)}))`, anchoring the Route F mechanism (c) machinery.

---

## D3 — Section (ii): W((2A_1)^{(1)}) reflection action on parameters

**Item (ii) — load-bearing per pagecount-priority rule (prompt 112
line 1075-1076).**

This section presents the parameter / root-variable relation: the
explicit Sakai equations of motion (eq.(16)-(18), p. 30) with the
null-sum constraint, the (2A_1)^{(1)} block-diagonal Cartan matrix,
and the four explicit reflection actions of `W((2A_1)^{(1)})` on
parameters `(a_0, a_1, b_0, b_1)`.

### D3.1 — Equations of motion + null-sum constraint (Sakai eq.(16)-(18), p. 30)

Verbatim from S1 §A.2.3 (lines 37-49 of `extract_sakai_2A1_generators.md`):

```
## A.2.3 Verbatim quote — equations of motion (eq.(16)–(18), p. 30)

>     P_III^{D_6^{(1)}}:
>          df/dt = (4/s)·[ 2 f^2 g − ( f^2 + (a_1 + b_1) f − (s/4) ) ],
>          dg/dt = −(4/s)·[ 2 f g^2 − ( 2 f g + (a_1 + b_1) g + a_1 ) ],
>          ds/dt = 4 = 4 (a_1 + a_0) = 4 (b_1 + b_0).

So the parameter constraint is:
   **a_0 + a_1 = b_0 + b_1 = 1.**

(The two A_1^{(1)}-components of (2A_1)^{(1)} carry parameters
(a_0, a_1) and (b_0, b_1) respectively, each constrained to sum to 1
which is the level / imaginary-root pairing.)
```

Key primitives surfaced by this quote:

- **Equations of motion** for the P_III^{D_6^{(1)}} system in
  Sakai's `(f, g, s)` chart.
- **Null-sum constraint** `a_0 + a_1 = b_0 + b_1 = 1`, the parameter-
  level expression of the level / imaginary-root pairing for each of
  the two A_1^{(1)} components.

### D3.2 — Block-diagonal (2A_1)^{(1)} Cartan matrix

Verbatim from S1 §A.2.4 (Cartan-structure block, lines 53-65 of
`extract_sakai_2A1_generators.md`):

```
### (2A_1)^{(1)} Cartan structure
The root system (2A_1)^{(1)} = A_1^{(1)} ⊕ A_1^{(1)} is the orthogonal
direct sum of two affine A_1 components. The 4 simple roots are
{α_0, α_1, α'_0, α'_1}. The Cartan matrix is block-diagonal:
        [  2  -2   0   0 ]   α_0
        [ -2   2   0   0 ]   α_1
   C  = [  0   0   2  -2 ]   α'_0
        [  0   0  -2   2 ]   α'_1
Each `A_1^{(1)}` block has the standard (untwisted) affine Cartan
matrix `[[2,-2],[-2,2]]`; the off-diagonal `−2` entries reflect that
the highest root of finite A_1 is `2 α_1 / 2 = α_1` itself, doubled
in the affine extension.
```

The 4×4 Cartan matrix decomposes as two 2×2 (untwisted affine A_1)
blocks; the off-block-diagonal zeros encode the orthogonal-direct-sum
structure of `(2A_1)^{(1)} = A_1^{(1)} ⊕ A_1^{(1)}`.

### D3.3 — Explicit reflection action on (a_0, a_1, b_0, b_1)

Verbatim from S1 §A.2.4 (Action-on-parameters block, lines 85-95 of
`extract_sakai_2A1_generators.md`):

```
### Action on parameters (a_0, a_1, b_0, b_1)
The standard "Kac–Moody / Noumi–Yamada" formula
`r_i(α_j) = α_j − a_{ij} α_i` gives, with the Cartan matrix above:
   r_0  : a_0 ↦ −a_0,            a_1 ↦ a_1 + 2 a_0;     b's unchanged.
   r_1  : a_0 ↦ a_0 + 2 a_1,     a_1 ↦ −a_1;            b's unchanged.
   r'_0 : b_0 ↦ −b_0,            b_1 ↦ b_1 + 2 b_0;     a's unchanged.
   r'_1 : b_0 ↦ b_0 + 2 b_1,     b_1 ↦ −b_1;            a's unchanged.
Each preserves the sum constraint `a_0 + a_1 = 1`, `b_0 + b_1 = 1`
(verified by direct substitution).
```

This is the **explicit four-reflection action** of W((2A_1)^{(1)})
on parameters `(a_0, a_1, b_0, b_1)`, with the null-sum constraint
preservation noted by the extraction at S1.  Each reflection acts
on its own A_1^{(1)} component only; the two components commute
(see also the defining-relations block immediately preceding in
S1 §A.2.4).

### D3.4 — Aut(D_6^{(1)}) = D_4 outer-automorphism note

Verbatim from S1 §A.2.4 (Aut-factor block, lines 97-115 of
`extract_sakai_2A1_generators.md`):

```
### Aut(D_6^{(1)}) factor
The diagram automorphism group of `D_6^{(1)}` (affine D_6,
7 nodes) has order `8 = (Z/2)^3` (two leaf-pair swaps at each fork
and one chain-end swap). Acting on the orthogonal complement
`(2A_1)^{(1)}`, it generates the subgroup of permutations of
`{α_0, α_1, α'_0, α'_1}`:
   - `π`  : α_0 ↔ α_1 (node swap on first A_1^{(1)} factor);
   - `π'` : α'_0 ↔ α'_1 (node swap on second A_1^{(1)} factor);
   - `σ`  : (α_0, α_1) ↔ (α'_0, α'_1) (swap the two A_1^{(1)}
            components).
On parameters:
   π   : a_0 ↔ a_1, b unchanged.
   π'  : a unchanged, b_0 ↔ b_1.
   σ   : (a, b) ↔ (b, a).
The group `⟨π, π', σ⟩ ≅ (Z/2)² ⋊ Z/2 ≅ D_4` (wreath product of two
Z/2's swapped by σ; order 8). This is the part of `Aut(D_6^{(1)})`
which acts non-trivially on the orthogonal complement (2A_1)^{(1)};
we identify `Aut(D_6^{(1)})` with this `D_4` action throughout
Phase B.
```

The outer-automorphism factor `Aut(D_6^{(1)}) ≅ D_4` (order 8) is
generated by `(π, π', σ)` with the explicit action on parameters
shown.  Combined with the affine Weyl factor `W((2A_1)^{(1)})` (which
is `D_∞ × D_∞`, infinite), the full Cremona group of D_6^{(1)} is
`D_4 ⋉ (D_∞ × D_∞)`, with classical (finite-Weyl-quotient) order
`8 × 4 = 32`.

---

## D4 — Section (iii): KNY 2017 §8.5.17 P_III(D_6) Hamiltonian form

This section presents the KNY 2017 §8.5.17 `d-P((2A_1)^{(1)}/D_6^{(1)})`
display: the §8.5.17 header, the Hamiltonian (eq. 8.237), the
eight-points base configuration (eq. 8.238), the differential Lax
operators (eq. 8.239), and the discrete shift action `T_α` (eq. 8.240).
Substrate: verbatim from `14_kajiwara_noumi_yamada_2017_geometric_aspects.txt`
(S2), lines 7869-7905.

### D4.1 — §8.5.17 header

Verbatim from S2 (KNY 2017 .txt extract) lines 7868-7872:

```
                                                    131
8.5.17   d-P((2A1 )(1) /D(1)
                         6 )

The corresponding continuous flow is PIII6 with the Hamiltonian:
```

The header `"8.5.17   d-P((2A1)(1)/D(1) 6)"` (typesetting wrap of
`d-P((2A_1)^{(1)}/D_6^{(1)})`) attaches the discrete-Painlevé system
`d-P((2A_1)^{(1)}/D_6^{(1)})` to its continuous-flow companion
`P_III(D_6)` (the page-131 typesetting wraps `D_6^{(1)}` across two
lines as "D(1) / 6").  The G3 line-anchor sanity check passed:
`grep` finds `"8.5.17"` substring at S2 line 7869.

### D4.2 — Hamiltonian (eq. 8.237)

Verbatim from S2 line 7876 and surrounding context (lines 7874-7878):

```
                                   1n                                      o
                             H=       p(p − 1)q2 + (a1 + a2 )qp + tp − a2 q .                       (8.237)
                                   t
```

Re-cast in linear-text form (matching 058R §B.3 transcription):

```
H_D6^KNY = (1/t) · { p(p − 1) q^2 + (a_1 + a_2) q p + t p − a_2 q },
            with parameter constraint  a_0 + a_1 + a_2 = 1
            (Sakai-classification convention, KNY (a_0, a_1, a_2)
             ↔ Sakai (a_0, a_1) ⊕ (b_0, b_1) — see D4.6 below).
```

### D4.3 — Eight base-point configuration (eq. 8.238)

Verbatim from S2 line 7881 and surrounding context (lines 7879-7883):

```
The eight points configuration in ( f, g) coordinates is given as:
                                    !            !                       
                               1        1 1                        t
                 ( fi , gi ) = , −a2 , , − a1 , (0, 0), , − + 1 − a2 − a1 .                        (8.238)
                                                3                       3
```

Re-cast in linear-text form (the .txt PDF-extraction wrap-line
artefacts are explicitly preserved above; re-parsed here for parsing
clarity, not for derivation):

```
(f_i, g_i)  =  (1/?, −a_2),
               (1/?, −a_1),
               (0, 0),
               (t/3, −t/3 + 1 − a_2 − a_1)
                                 ... (eight points total; eq. 8.238)
```

The PDF-extraction wrap on the typesetting of eq. (8.238) splits the
`f_i` denominators across line 7881; the eight-point list is the
canonical configuration of base points for the
`d-P((2A_1)^{(1)}/D_6^{(1)})` surface.  Synth should treat the
verbatim S2 quote (the first fence above) as the authoritative form
and the linear re-cast as a parsing aid only.

### D4.4 — Differential Lax operators (eq. 8.239)

Verbatim from S2 lines 7884-7892:

```
(i) Differential Lax form:
              n a2         pq         tH o n 1 + a1 + a2    1   t    o
         L1 = −       +           − 2 +                  −    + 2 − 1 ∂x + ∂x 2,
                   x    x(x − q) x                x        x−q x
                      1
         L2 = T α −       (p − ∂ x ),                                                               (8.239)
                      q
         B = ∂t −          (x∂ x − qp).
                  t(x − q)
```

Re-cast in linear-text form (matching 058R §B.3 quote):

```
L_1  =  { −a_2/x  +  pq/[x(x−q)]  −  tH/x^2 }
      + { (1+a_1+a_2)/x  −  1/(x−q)  +  t/x^2  −  1 } ∂_x
      +  ∂_x^2,

L_2  =  T_α  −  (p − ∂_x) / (x − q),

B    =  ∂_t  −  q · (x ∂_x − q p) / [t(x−q)].
```

The compatibility statement immediately below eq. (8.239) at S2
line 7895 reads (verbatim, S2 lines 7895-7896):

```
The curve L1 y = 0 is the unique curve of degree (3, 2) in ( f, g) passing through the points (8.238)
and (8.226). Compatibility of L1 y = L2 y = 0 gives the discrete flow for T α (= (π1 π2 )2 s2 s1 ):
```

i.e. the discrete-flow shift `T_α` is identified with the affine-Weyl
word `(π_1 π_2)^2 s_2 s_1`.

### D4.5 — Discrete shift action T_α (eq. 8.240)

Verbatim from S2 lines 7897-7901:

```
                       a1 = a1 + 1, a2 = a2 + 1,
                                 a2     a1            t   a1 + a2 + 1                               (8.240)
                       q+q=− −              , p+ p=1− 2 −             .
                                 p     p−1           q         q
```

Re-cast in linear-text form:

```
T_α :  (a_1, a_2)  ↦  (a_1 + 1, a_2 + 1),
        q + q'   =  −a_2/p − a_1/(p−1),
        p + p'   =  1 − t/q^2 − (a_1 + a_2 + 1)/q.        (eq. 8.240)
```

Key primitive: the discrete shift `T_α` translates the Hamiltonian
parameters by `(a_1, a_2) ↦ (a_1+1, a_2+1)` while transforming the
canonical `(q, p)` chart by the rational map shown.

### D4.6 — Convention reminder (parameter-symbol cross-walk)

> **Convention reminder:**  KNY uses `(a_0, a_1, a_2)` for P_III(D_6)
> Hamiltonian parameters; Sakai uses `(a_0, a_1) + (b_0, b_1)`
> constrained by `a_0 + a_1 = b_0 + b_1 = 1`; CT v1.3 §3.5 uses
> `(η_∞, η_0, θ_∞, θ_0)`.  Connection map between conventions =
> 058R `phase_b_canonical_map.md` (cited below in D5).

Note (UF watch — UF-126-PARAM-COUNT, surfaced in D5 below): KNY's
Hamiltonian uses **3** parameter symbols `(a_0, a_1, a_2)` whereas
Sakai's (2A_1)^{(1)} parametrisation uses **4** parameter symbols
`(a_0, a_1, b_0, b_1)` constrained by **two** null-sum equations
(a_0+a_1=1, b_0+b_1=1).  The naive count is 4−2 = 2 free parameters
on Sakai's side and 3 free parameters on KNY's side — a one-symbol
mismatch.  Resolution (cross-walk material in 058R §B.3 below): the
extra KNY symbol is the discrete-shift orbit index, so KNY's `a_0` is
absorbed by the level `a_0+a_1+a_2=1` constraint visible in the
discrete shift `T_α: (a_1, a_2) ↦ (a_1+1, a_2+1)` (which preserves
the level only modulo a translation absorbed by `T_α` itself).
This convention-shift book-keeping is the structural question synth
addresses in its Q4 verdict; this note is a navigation aid, not a
derivation.

---

## D5 — Section (iv): Affine-Weyl action substrate (PARTIAL)

**Item (iv) — load-bearing per prompt 112 line 1073;
PARTIAL substrate; full pull-back to (η_∞, η_0, θ_∞, θ_0)
intentionally deferred to synth.**

This section provides the raw affine-Weyl substrate for the
fixed-point / generic-orbit structural question Q4 asks.  Per the
§10 priority discipline (and prompt 113 §2 D5 + §8 N1), the explicit
pull-back of the W((2A_1)^{(1)}) action onto Okamoto / CT coordinates
`(η_∞, η_0, θ_∞, θ_0)` is **not derived here**; it is the structural
derivation synth performs in the Q4 re-fire.  This section
cross-references the material already quoted in D3 + D4 and quotes
**only** the 058R Phase B material that ties the two parameter
conventions together with the V_quad null-sum anchor.

### D5.1 — Cross-references (no re-paste)

- **KNY discrete shift** `T_α: (a_1, a_2) ↦ (a_1+1, a_2+1)` and
  associated rational map on `(q, p)`:
  see **D4.5 above** (S2 line 7898 / eq. 8.240).
  Cross-ref only — not re-pasted.

- **Sakai four-reflection action** of `r_0, r_1, r'_0, r'_1` on
  parameters `(a_0, a_1, b_0, b_1)` preserving the null-sum
  constraints `a_0+a_1=1`, `b_0+b_1=1`:
  see **D3.3 above** (S1 §A.2.4 Action-on-parameters block).
  Cross-ref only — not re-pasted.

### D5.2 — 058R §B.3: V_quad 4-tuple null-sum −1/3 anchor + Okamoto–Sakai cross-walk

The Okamoto–Sakai convention cross-walk material and the V_quad
null-sum anomaly anchor citation are **both inside §B.3** of
`phase_b_canonical_map.md`, NOT §B.5 (see UF-126-S4-SECTION-MISLABEL
in handoff).  §B.5 of `phase_b_canonical_map.md` is "Formal-series
structure preservation" and is not the cross-walk material.

Verbatim from S4 §B.3 (058R `phase_b_canonical_map.md`,
"Φ_symp construction" + KNY-cross-walk paragraphs):

```
KNY 2017 §8.5.17 Hamiltonian (eq. 8.237):

H_D6^KNY  =  (1/t) · { p(p−1) q^2 + (a_1 + a_2) q p + t p − a_2 q },
             a_0 + a_1 = 1.

This is Sakai-classification convention with surface type D_6^{(1)}
and symmetry type (2 A_1)^{(1)} = (A_1 × A_1)^{(1)}
(see Phase B.5 for the Okamoto-Sakai convention cross-walk).

[...]

Φ_symp construction.  Up to sign and parameter convention,
Φ_symp is the canonical (q, p) ↔ (q, p) gauge transformation that
identifies Okamoto 1987's H_{III} (B.1) with KNY 2017's
H_{D_6}^{KNY} above.  The matching is

  (θ_0, θ_∞)_{Okamoto}  ↔  (a_1, a_2)_{KNY}
                          (mod  convention shift),

with the explicit formula derivable by expanding both Hamiltonians in
the same canonical (q, p, t) chart.
```

(Internal note within S4: the 058R file's cross-reference "see
Phase B.5 for the Okamoto-Sakai convention cross-walk" appears to
be an internal mislabel; the cross-walk content is in §B.3 itself
(the matching display above).  This is logged as
UF-126-S4-SECTION-MISLABEL in `unexpected_finds.json`.)

Verbatim from S4 §B.3 (058R `phase_b_canonical_map.md`,
"Numerical Jacobian factor (i)" paragraph — V_quad null-sum −1/3
anomaly anchor):

```
Numerical Jacobian factor: the numerical value of
|det J(Φ_symp)| acting on Stokes data at the V_quad
parameter point requires:

  (i) explicit conversion of the V_quad's CT v1.3 §3.5 4-tuple
      (α_∞, α_0, β_∞, β_0) = (1/6, 0, 0, -1/2)
      to KNY (a_0, a_1, a_2) — this is residual R1 partially
      closed; the 4-tuple does NOT satisfy Okamoto's
      α_∞ + α_0 + β_∞ + β_0 = 0 constraint (sums to -1/3),
      an anomaly first surfaced in the 2026-05-02 partial session
      and carried forward unchanged; see anomaly D2 in
      discrepancy_log.json;
```

Key primitives surfaced by these two quotes:

- The Okamoto ↔ KNY parameter-symbol matching is
  `(θ_0, θ_∞)_Okamoto ↔ (a_1, a_2)_KNY` modulo a convention shift;
  the explicit formula is constructible by expanding both
  Hamiltonians in the same canonical `(q, p, t)` chart (058R §B.3).
- The V_quad 4-tuple in CT v1.3 §3.5 notation is
  `(α_∞, α_0, β_∞, β_0) = (1/6, 0, 0, -1/2)`; its sum is
  `1/6 + 0 + 0 - 1/2 = -1/3` (not zero), so V_quad does NOT satisfy
  the Okamoto null-sum constraint `α_∞ + α_0 + β_∞ + β_0 = 0`.

### D5.3 — Structural question framing line (per prompt 113 §2 D5)

> *"V_quad image (1/6, 0, 0, -1/2) sits at η_0 = 0 (or the
> (η, θ)-side image of η_0 = 0).  Whether this locus is an
> affine-Weyl FIXED-POINT (degenerate orbit; supports Route F
> geometric-machinery interpretation) or a GENERIC POINT (does not
> support Route F) is the structural question synth answers in the
> Q4 re-fire."*

This framing line is the explicit structural question Q4 asks; it is
**not** a derivation, and this packet does **not** classify the
V_quad image as fixed-point vs generic-orbit.  That classification
requires the explicit pull-back of `r_0, r_1, r'_0, r'_1`
(D3.3 above) and `T_α` (D4.5 above) onto Okamoto / CT coordinates
`(η_∞, η_0, θ_∞, θ_0)` via the convention cross-walk
`(θ_0, θ_∞)_Okamoto ↔ (a_1, a_2)_KNY` (D5.2 above) plus the analogous
`(η_∞, η_0)` mapping onto Sakai `(a_0, a_1, b_0, b_1)` (D3.1 above) —
all of which is structural-derivation work intentionally deferred to
synth.

---

## D6 — Footer / dispatch instruction

> **INSTRUCTION TO SYNTH:**  Re-fire question Q4 only of the 069r3
> FINAL synthesis verdict packet using this substrate.  All other
> questions Q1-Q3, Q5-Q8 retain their previous verdicts; only Q4
> (Route F GO / NO_GO) is in scope.  Expected output: a single
> decisive verdict (GO_ROUTE_F | NO_GO_ROUTE_F | path-delta-
> escalation) with confidence band and a 1-2 paragraph structural
> justification.

---

## Appendix — Substrate inventory + line-anchor table

| Item | Source slot | File path                                                                                            | Line range | SHA-256 (fresh)                                                    |
|------|-------------|------------------------------------------------------------------------------------------------------|-----------:|--------------------------------------------------------------------|
| (i)  | S1 §A.2.1   | `siarc-relay-bridge/sessions/2026-05-04/SIARC-PRIMARY-W-HOMOMORPHISM-DERIVATION/extract_sakai_2A1_generators.md` |     11-29 | `2CC9395BFF74B1C4B0522C98AAA712821C5EADA073E226CEC4341C1E536BB007` |
| (i)  | S1 §A.2.2   | (same)                                                                                               |     31-35 | (same)                                                             |
| (ii) | S1 §A.2.3   | (same)                                                                                               |     37-49 | (same)                                                             |
| (ii) | S1 §A.2.4   | (same; Cartan + reflection-action + Aut blocks)                                                      |    53-115 | (same)                                                             |
| (iii)| S2          | `tex/submitted/control center/literature/g3b_2026-05-03/14_kajiwara_noumi_yamada_2017_geometric_aspects.txt` | 7869-7905 | `AAA2B0958F22BB03783FC76C9FE51B35F38ED39D849900DA6A9C044267CE3A2F` |
| (iv) | S4 §B.3     | `siarc-relay-bridge/sessions/2026-05-06/CC-VQUAD-PIII-NORMALIZATION-MAP-RERE-FIRE/phase_b_canonical_map.md` |     22-200 | `F831F9BD58D1F3064873DFDEAB14C003BF441CBB3832E02B6CDDC94A91FF8BB3` |

| Anchor only (no extraction in this packet) | S3 | `tex/submitted/control center/literature/g3b_2026-05-03/13_sakai_1999_preprint_kyoto99_10.pdf` | n/a (PDF) | `EC1BBDA3B77634E6DEF2A784D04947A0C9631BFADE48C72AA0767B22AAF49ED6` |

Bridge HEAD at packet-build:
`1eed8ef1475293880a23a1d038369c0bb11a6979`.
Ancestor of `ae5b7f7` (T1-SYNTH-069R3-FINAL-VERDICT-ABSORPTION-124):
PASS.

Preflight gates (G1-G5, prompt 113 §4):
- G1 substrate-file existence:    PASS (S1, S2, S3, S4 all readable).
- G2 S1 SHA stability:            PASS (no prior-session SHA mismatch surfaced).
- G3 S2 line-anchor sanity:       PASS (S2 line 7869 contains `"8.5.17"`).
- G4 bibliographic identifier pre-verification: PASS (S3 PDF SHA matches `EC1BBDA3...`; published-DOI `10.1007/s002200100446` resolution NOT required for this on-disk-anchor packet).
- G5 bridge HEAD ancestry:        PASS (`ae5b7f7` ancestor of `1eed8ef`).

Forbidden-verb scan (prompt 113 §5): non-exempt hits PASS (zero;
all forbidden-verb occurrences in this packet are inside verbatim
triple-backtick fences quoting S1/S2/S4 and are exempt under
category (f), or are inside category (a) verb-list-as-data.)

End of packet.
