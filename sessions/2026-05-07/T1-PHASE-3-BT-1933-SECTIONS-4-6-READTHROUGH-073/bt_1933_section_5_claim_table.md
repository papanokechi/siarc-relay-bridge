# BT 1933 §5 — Claim Table

**Source PDF SHA-256:**
`dcd7e3c6b2a12ae1ce917d322763ff9dde5ec69ab5f23080d043699822d68fe6`
**§5 page span:** Acta p. 40 — p. 48 (PDF p. 40 — p. 48).
**§5 title:** "Construction of proper solutions to the right of a proper curve."

Verbatim ≤ 30-word source quotes follow the policy in P8 of the relay
prompt: each quote is ≤ 30 words counted on whitespace-separated
tokens, with hyphenated forms counted as a single token. Quotes that
would exceed 30 words verbatim are paraphrased with explicit "BT 1933
§5 p. NN states (in our paraphrase): ..." framing.

The §5 single labelled result is **Theorem I** (Acta p. 41).
Identifier T2 is reserved for this result in the §§4-6 main-theorems
index (see `bt_1933_sections_4_6_main_theorems.md`).

## Claim table

| Tag | Acta p. | Subject | Verbatim ≤ 30-word quote OR paraphrase | Word count |
| --- | --- | --- | --- | --- |
| `[CLAIM-B51]` (FORMAL ANSATZ) | p. 41 | known coefficients setup | "Assume that the coefficients of an equation L_n(y) = o (2; § 1) are known (cf § 1) in a subregion of F (§ 1), F = (1) + ... + (η)." | 30 |
| `[CLAIM-B52]` (FORMAL ANSATZ) | p. 41 | exponential dominants | "Let the corresponding functions Q(x) be (1) Q_1(x), ... Q_n(x)." | 9 |
| `[CLAIM-B53]` (PROPER CURVE) | p. 41 | proper-curve hypothesis | "Suppose that Γ, a proper curve (Def. 9; § 1) for the set (1), is the left boundary of (m) (2 ≦ m ≦ η) or lies to the left of it." | 30 |
| `[CLAIM-B54]` (FORMAL→ANALYTIC) | p. 41 | strip-V hypothesis | *BT 1933 §5 p. 41 states (in our paraphrase):* in a unit-width strip V coincident with the left boundary of (m), there exists a proper fundamental set of solutions (Def. 4; § 1) for L_n(y) = o. | (paraphrase) |
| `[CLAIM-B55]` (Theorem I conclusion) | p. 41 | completely-proper conclusion | "It will necessarily follow that L_n(y) is completely proper (Def. 6; § 1) in (m) + ... + (η)." | 17 |
| `[CLAIM-B56]` (Theorem I corollary) | p. 41 | m=1 case | *BT 1933 §5 p. 41 states (in our paraphrase):* if Γ exists in region (1) the strip-V hypothesis is omittable; L_n is then completely proper in (m) + ... + (η) with m = 1. | (paraphrase) |
| `[CLAIM-B57]` (B'-CURVE PARTITION) | p. 41 | regions (s) | "the regions (1), (2), ... (η) are separated by B'-curves, (2) B^1, B^2, ..., B^{η−1}." | 14 |
| `[CLAIM-B58]` (DOMINANT ORDERING) | p. 41 | (3) ordering | "ℜ Q'_1(x) > ℜ Q'_2(x) > ... > ℜ Q'_n(x). (x in (s))." | 14 |
| `[CLAIM-B59]` (DETERMINANT-LIMIT INDUCTION) | p. 42 | determinant limits via §3 Lemmas 4–7 | *BT 1933 §5 p. 42 states (in our paraphrase):* by iteration of (3), determinant limits of orders 1, 2, ..., n corresponding to _sQ(x) are constructed in (m) using §3 Lemmas 4–5 (m = 1) or 6–7 (m > 1). | (paraphrase) |
| `[CLAIM-B510]` (FORMAL SERIES coefficients) | p. 42 | (4 a) formal-series form | *BT 1933 §5 p. 42 states (in our paraphrase):* the determinant-limit functions _m y_{i_1...i_k; 1...k}(x) are analytic in (m) and asymptotic to e^{_m Q_1 + ... + _m Q_k}(x) times a formal s-series _m S_{i_1...i_k; 1...k}(x). | (paraphrase) |
| `[CLAIM-B511]` (FORMAL SERIES coefficients) | p. 43 | (4 e) column-by-column form | "_m z_{i j}(x) ∼ e^{_m Q_j(x)} _m s_{i j}(x) (i = 1, ..., n; j = 1, ..., k − 1)." | 21 |
| `[CLAIM-B512]` (LEMMA-8 INVOCATION) | p. 44 | §4 Lemma 8 invocation | "Lemma 8 (§ 4) is applicable for evaluation of any of the expressions (6 c) ∑_{t≡x} _m v_{k j}(t)   (j = 1, ..., k − 1) occurring in (5)." | 23 |
| `[CLAIM-B513]` (LEMMA-8 INVOCATION) | p. 44 | (6 d) summation result | "we evaluate (6 c) as a function analytic in a region (m)', slightly interior to (m), and satisfying in (m)' an asymptotic relation" | 22 |
| `[CLAIM-B514]` (FORMAL SERIES output) | p. 45 | (7) k-th column ansatz | "_m z_{1 k}(x) ∼ e^{_m Q_k(x)} _m a_{1 k}(x)         (x in (m)), where _m a_{1 k}(x) is a formal s-series." | 22 |
| `[CLAIM-B515]` (BACK-RECONSTRUCTION) | p. 45 | (8) full-column from row 1 | *BT 1933 §5 p. 45 states (in our paraphrase):* the remaining elements _m z_{i k}(x) (i = 2, ..., n) are determined from _m z_{1 k}(x + 1), ..., _m z_{1 k}(x + n) via (8), inverting the iteration relation. | (paraphrase) |
| `[CLAIM-B516]` (PROPER MATRIX SOLUTION) | p. 45 | matrix proper in (m) | "Thus a solution _m z_{i k}(x) (i = 1, ..., n), possessing all the desired properties, has been constructed. This proves existence of a matrix solution proper in (m)." | 28 |
| `[CLAIM-B517]` (CHART-MAP candidate) | p. 47 | proper-periodic-functions structure | *BT 1933 §5 p. 47 states (in our paraphrase):* the periodic-functions matrix p^{r, r+1}(x) connecting solutions across B'-curves expands as (13 a) ∑ p^{r, r+1}_{i j; π} e^{−π_{i j}(r, r+1) x_r} with x_r = ℑ x ≧ Q > o, supplying the across-strip transition data. | (paraphrase; **[CHART-MAP-CANDIDATE-B1]** — see Phase C.4 surfacing below) |
| `[CLAIM-B518]` (Theorem I closure) | p. 47 | "L_n completely proper" conclusion | "L_n(y) is seen to be completely proper in (m) + ... + (η)." | 13 |

## Tag-class summary

| Class | Count | Tags |
| --- | --- | --- |
| Theorem I formal ansatz + hypotheses | 4 | B51, B52, B53, B54 |
| Theorem I conclusion | 2 | B55, B56 |
| Region/B'-curve setup | 2 | B57, B58 |
| Determinant-limit induction (uses §3 Lemmas 4–7) | 1 | B59 |
| Formal-series coefficients (per column) | 3 | B510, B511, B514 |
| Lemma-8 invocation (uses §4 result) | 2 | B512, B513 |
| Back-reconstruction + matrix proper | 2 | B515, B516 |
| Periodic-functions / Stokes-data structure | 1 | B517 (CHART-MAP-CANDIDATE-B1) |
| Theorem I closure | 1 | B518 |

**Total claims:** 18 across §5.

## Phase C.4 surfacing — [CHART-MAP-CANDIDATE-B1]

`[CLAIM-B517]` is tagged **[CHART-MAP-CANDIDATE-B1]** because it
exposes — in the §5 proof of Theorem I — an explicit expansion of
the *connection matrix* between proper solutions in adjacent regions
(r) and (r+1), namely the q-series

  p^{r, r+1}_{i j}(x) = ∑_π p^{r, r+1}_{i j; π} z^{π_{i j}(r, r+1)}
                         (z = e^{− 2π√−1 x_r}; |z| = e^{−q+v})

with integer exponents π. This is the BT 1933 incarnation of the
Stokes / connection / chart-map data linking sectorial proper solutions
across B'-curves.

**EXPLICIT CAVEAT per relay 073 Phase C.4:** Identification of
[CHART-MAP-CANDIDATE-B1] in BT§5 is a **SUBSTRATE-INVENTORY
observation, NOT an assertion that R1 is closed by BT alone. R1
closure remains a W21 LANE-1 derivation task per 069r1 NO_GO.**

Whether the §5 (13 a) periodic-functions expansion supplies the
specific (a_0, a_1, a_2) → (α, β) chart map needed by 069r1's R1
closure — i.e., whether the n = 2 PCF specialisation of (13 a)
recovers the SIARC-stratum (a_0, a_1, a_2) ↔ (α, β)
parameter-space identification — is **OUT OF SCOPE for this
T3-mechanical relay**. The fact-of-existence of an across-strip
periodic-functions chart-map structure in BT§5 (13 a) is the
substrate observation. The synthesizer-level derivation that
specialises (13 a) at n = 2 to the PCF (a_0, a_1, a_2) coefficient-
space is an open W21 LANE-1 Phase 3 task.

## Internal cross-references in §5

- (2; § 1), (cf § 1), F (§ 1) at p. 41 → §1 difference-equation setup.
- (Def. 9; § 1) at p. 41 → §1 proper-curve definition.
- (Def. 4; § 1) at p. 41 → §1 proper-fundamental-set-of-solutions def.
- (Def. 6; § 1) at p. 41 → §1 completely-proper-operator definition.
- (6; § 1), (6 a; § 1) at p. 41 → §1 system Y(x+1) = D(x) Y(x) form.
- (1 a; § 1) at p. 42 → §1 system Y(x+1) = Z(x) Y(x) generality.
- Lemmas 4 and 5; § 3 at p. 42 → §3 iteration-from-infinite-left lemmas.
- Lemmas 6 and 7; § 3 at p. 42 → §3 iteration-from-strip-V lemmas.
- (II) at p. 43 → 1930 Birkhoff paper "Formal theory of irregular
  linear difference equations" (Acta Math. 54, 1930).
- (II; p. 259) at p. 45 → same 1930 paper.
- (Def. 5; § 1) at p. 46 → §1 proper-periodic-functions definition.
- (Def. 3; § 1) at p. 47 → §1 (a different proper-functions definition).
- §4 (the Lemma 8 invocation) at p. 44 → INTERNAL §§4-6 reference;
  §5 explicitly depends on §4 for the contour-summation evaluation.

These are recorded in `bt_1933_sections_4_6_internal_xref.md`.
