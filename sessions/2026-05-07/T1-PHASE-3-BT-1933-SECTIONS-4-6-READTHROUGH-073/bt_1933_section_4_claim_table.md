# BT 1933 §4 — Claim Table

**Source PDF SHA-256:**
`dcd7e3c6b2a12ae1ce917d322763ff9dde5ec69ab5f23080d043699822d68fe6`
**§4 page span:** Acta p. 29 — p. 40 (PDF p. 29 — p. 40).
**§4 title:** "A lemma on summation."

Verbatim ≤ 30-word source quotes follow the policy in P8 of the relay
prompt: each quote is ≤ 30 words counted on whitespace-separated
tokens, with hyphenated forms counted as a single token. Quotes that
would exceed 30 words verbatim are paraphrased with explicit "BT 1933
§4 p. NN states (in our paraphrase): ..." framing.

The §4 single labelled result is **Lemma 8** (Acta p. 30).
Identifier T1 is reserved for this result in the §§4-6 main-theorems
index (see `bt_1933_sections_4_6_main_theorems.md`).

## Claim table

| Tag | Acta p. | Subject | Verbatim ≤ 30-word quote OR paraphrase | Word count |
| --- | --- | --- | --- | --- |
| `[CLAIM-B41]` (SETUP) | p. 29 | R-region geometry | "Let R denote a region the left boundary of which is either h or a curve, extending indefinitely upwards, with a limiting direction at infinity." | 26 |
| `[CLAIM-B42]` (SETUP) | p. 29 | right-boundary form | "This latter boundary, if with the limiting direction of the axis of reals will be assumed to be a curve of the form v = h u^t (h, e > o)." | 30 |
| `[CLAIM-B43]` (SETUP) | p. 29 | left-boundary form | "The left boundary of R, if extending upwards … will be of the form v = h(−u)^e + …(h > o; 1 > e > o)." | 24 (with elision) |
| `[CLAIM-B44]` (CLASSIFICATION) | p. 30 | hypotheses on H, Q, h | *BT 1933 §4 p. 30 states (in our paraphrase):* the function H(x) = e^{Q(x)} h(x) is analytic in R; Q(x) is "proper" (Newton-polygon dominant exponential factor) on the right boundary; h(x) is asymptotic in R to a formal s-series. | (paraphrase) |
| `[CLAIM-B45]` (Lemma 8 statement) | p. 30 | inhomogeneous difference equation, formal-to-analytic upgrade | *BT 1933 §4 p. 30 states (in our paraphrase):* the equation y(x+1) − y(x) = e^{Q(x)} h(x) admits an analytic solution y(x) on a sub-region R' interior to R, with asymptotic relation y(x) ∼ e^{Q(x)} s(x) (s(x) a formal s-series) maintained in R'. | (paraphrase) |
| `[CLAIM-B45a]` (Lemma 8 verbatim opening) | p. 30 | hypothesis (1 a) | "h(x) ∼ H̃(x) (in R) where H̃(x) is a formal s-series (Def. 1; § 1)." | 14 |
| `[CLAIM-B45b]` (Lemma 8 verbatim ansatz) | p. 30 | (1)/(2) display | "(I) H(x) = e^{Q(x)} h(x) … (2) y(x + 1) − y(x) = e^{Q(x)} h(x)." | 18 |
| `[CLAIM-B45c]` (Lemma 8 verbatim conclusion) | p. 30 | (2 a) display | "y(x) ∼ e^{Q(x)} s(x), where s(x) is a formal s-series, is maintained in the above region." | 17 |
| `[CLAIM-B46]` (PROOF MACHINERY) | p. 30 | reduction substitution | *BT 1933 §4 p. 30 states (in our paraphrase):* the proof substitutes y(x) = e^{Q(x)} t(x) + x^{k'} z(x) where t(x) is the truncated s-series with k' = m terms, reducing the problem to a recurrence for the rescaled error z(x). | (paraphrase) |
| `[CLAIM-B47]` (PROOF MACHINERY) | p. 31 | reduction to homogeneous problem | "The equation (3 a) with the second member replaced by zero is satisfied by z(x) = 1/q(x). Hence (3 b)" | 21 |
| `[CLAIM-B48]` (CONTOUR L) | p. 31 | contour-summation procedure | *BT 1933 §4 p. 31 states (in our paraphrase):* with x in R', a contour L is constructed lying interior to R with two cases: when ℜ Q ≦ o on the negative axis and the lower boundary is h, L = h + L* where L* is a path near the right boundary; otherwise L is a path near the right boundary alone. | (paraphrase) |
| `[CLAIM-B49]` (CONTOUR L) | p. 31 | exponential-decay parameter λ | "by hypothesis, Q(x) is proper along L … Hence a least integer λ can be found so that |t|^λ e^{Q(t)} → o (ℑ t = v)." | 24 (with elision) |
| `[CLAIM-B410]` (SUM-FORMULA) | p. 32 | (5) sum-formula identity | *BT 1933 §4 p. 32 states (in our paraphrase):* the contour integral (5) — taken along L_x = L (described upwards) plus the loop l_x (clockwise) — represents the formal sum (3 c) and yields a function analytic in R'. | (paraphrase) |
| `[CLAIM-B411]` (CASE I) | p. 35 | Case I dichotomy | "Case I. Along the negative axis of reals, for |x| sufficiently great, ℜ Q(x) ≦ o." | 14 |
| `[CLAIM-B412]` (CASE II) | p. 37 | Case II dichotomy | "Case II. Along the negative axis of reals ℜ Q(x) = o." | 11 |
| `[CLAIM-B413]` (CURVE Γ_H) | p. 38 | Γ_H curve construction | *BT 1933 §4 p. 38 states (in our paraphrase):* a curve Γ_H ⊂ Γ is defined by v = h(−u)^H with H = 1 − ν/p; below Γ_H the inequality (14 b) bounds the imaginary-part contribution to ℜ[Q(x−i) − Q(x)]. | (paraphrase) |
| `[CLAIM-B414]` (CLOSURE) | p. 39 | (15) Γ_H bound | "ℜ[Q(x−i) − Q(x)] ≦ 2 \|γ\| h^* s^l_i + … < q (q independent of x, i; x in R below Γ_H)." | 24 |
| `[CLAIM-B415]` (CLOSURE) | p. 40 | end-of-proof statement | "the result just mentioned, together with (10) and (12), enables us to assert that an inequality like (17) holds, for x in R', in any case." | 27 |
| `[CLAIM-B416]` (CLOSURE) | p. 40 | k → ∞ rate of κ | "κ − k = k_x − … and approaches infinity as k approaches infinity (see (3 a))." | 18 |

## Tag-class summary

| Class | Count | Tags |
| --- | --- | --- |
| SETUP | 3 | B41, B42, B43 |
| CLASSIFICATION (Newton-polygon-style ansatz) | 1 | B44 |
| Lemma 8 statement (formal + verbatim) | 4 | B45, B45a, B45b, B45c |
| Proof machinery (substitution + contour) | 4 | B46, B47, B48, B49 |
| Sum-formula | 1 | B410 |
| Case-split | 2 | B411, B412 |
| Γ_H curve | 2 | B413, B414 |
| Closure | 2 | B415, B416 |

**Total claims:** 19 across §4.

## Newton-polygon / classification cross-walk

§4 does NOT explicitly invoke a Newton-polygon construction. The
classification it carries is the "proper Q(x)" condition on the right
boundary of R, where Q(x) = µx log x + γx + ... + ν x^{1/p} is the
exponential-dominant ansatz inherited from §1. Adams 1928 §1's
Newton-polygon classification (Class 1 / Class 2) is a more explicit
statement of the same content; the [CLAIM-B44] paraphrase carries
the BT 1933 form.

## Internal cross-references in §4

- (Def. 1; § 1) at p. 30 → §1 formal s-series definition.
- (II; p. 218) at p. 30 → cited 1930 Birkhoff paper "Formal theory of
  irregular linear difference equations" (Acta Math. 54, 1930).
- (II eq. 12) at p. 33, footnote → same reference [II].
- (II eq. 13) at p. 33 → same.
- (II formula 12) at p. 39 → same.
- § 2 at p. 29 → curve F (the proper-curve definition).

These are recorded in `bt_1933_sections_4_6_internal_xref.md`.
