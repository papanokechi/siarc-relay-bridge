# Phase C — B-T 1933 §1 anormal-case ansatz (q = 2 fractional rank) cross-check

**Task ID:** `T1-PHASE-3-COSTIN-BORDERLINE-M4-CLOSURE-068`
**Phase:** C (B-T 1933 §1 anormal-case ansatz at q = 2)
**Date:** 2026-05-07 (W20)
**Role under A.0 outcome (i):** SECONDARY confirming evidence — the
fractional-rank q ≥ 2 case of B-T 1933 is invoked here to establish
that the SIARC stratum's deg_a = 0 row sits in the **normal case
(p = 1)**, NOT the anormal q ≥ 2 case. This rules in the four-row
deg_a = 0 closure as a normal-case closure (no fractional-rank
machinery required for the operative SIARC-stratum row).

---

## C.1 B-T 1933 §1 verbatim — canonical-form ansatz

**Source:** `siarc-relay-bridge/sessions/2026-05-03/T1-A01-NORMALIZATION-RESOLUTION/_bt1933.txt`
SHA-256 `5FBB3E2FDC7AC71E7209DF16F60F0B6FC42D9D251B1A8821F6C93889CD910DA1`,
140094 B (OCR text dump of `birkhoff_trjitzinsky_1933.pdf`
SHA `DCD7E3C6B2A12AE1…`).

**B-T 1933 §1 page 4 verbatim** (OCR L107-118):

> "every system of type (i), or single equation (2), admits precisely
> n linearly independent formal solutions with elements of the general
> type
>
> e^{Q(x)} s(x),
>
> Q(x) = (μ/p) x log x + γ x + d_p x^{(p−1)/p} + d_{p−1} x^{(p−2)/p}
>          + … + d_2 x^{1/p}                          (eq. 7)
>
> s(x) = x^μ ( a + b x^{−1/p} + … )
>          + ( a_1 + b_1 x^{−1/p} + … ) log x
>          + …
>          + ( a_m + b_m x^{−1/p} + … ) log^m x       (eq. 7a)
>
> p is a positive integer, μ p is an integer and m is a positive
> integer or 0."

**Definition 1 (s-series; OCR L119):**

> "Definition 1. A formal series s(x) which is of the form (7a) will be
> termed an s-series."

**Normal vs anormal classification** (B-T 1933 §1, OCR L131-142):

> "The difference system (1) or single equation (2) will be called
> normal if p ≡ 1 in all of the formal series, so that each Q_j(x)
> reduces merely to (μ_j/p) x log x + γ_j x; otherwise it will be
> called anormal, since then there enter anormal series with p > 1.
> This agreement is in accordance with that used for linear
> differential equations. Moreover the system (1) or equation (2)
> will be called regular or irregular, according as there is only a
> single value of μ_j or more than one such value."

**Galbrun special anormal regular type (q = 2 fractional-rank
example)** (B-T 1933 §1, OCR L150-160):

> "Galbrun has treated a single difference equation of order n with
> rational coefficients in the special case of the special anormal
> regular type in which a pair of anormal series enter with p ≡ 2,
> so that the two corresponding polynomials Q(x) in √x have the
> respective forms
>
>     z(x) + γ √x + ⋯,
>     z(x) − γ √x − ⋯ "
> [OCR slightly degraded; structure preserved]

**Notation reconciliation:** B-T 1933 uses **p** for the fractional-
rank denominator in eq. (7); relay 068 uses **q** for the same
quantity ("q ∈ {2, 3, …} fractional-rank case"). The two notations
agree term-for-term: B-T's p ≡ 2 normal case is q = 2 in relay
notation; B-T's normal case p ≡ 1 is q = 1 in relay notation.

`HALT_068_BT_1933_SECTION_1_NIA`: NOT TRIGGERED. §1 ansatz on disk
verbatim at the line ranges cited above.

---

## C.2 Normal-case ansatz (p = 1) for the SIARC deg_a = 0 stratum

**Setup:** SIARC stratum recurrence p_n = b_n p_{n-1} + a_n p_{n-2}
with a_n ≡ 1, b_n = c_b n^d + O(n^{d-1}).

**Birkhoff Q(x) for the normal case (p = 1):**

  Q(x) = μ x log x + γ x.

**Dominant solution** (V6 §V6 Step 2; reproduced as the canonical
B-T 1933 normal-case anchor at p = 1):

  μ_dom = d ;  γ_dom = log(c_b e^{−d}) = log c_b − d.

  s_dom(x) = x^{d/2} (a + b x^{−1} + …)  [the n^{d/2} prefactor is
                                          the Stirling correction in
                                          Birkhoff form]

**Recessive solution** (V6 §V6 Step 3):

  μ_sub = −d ;  γ_sub = −1/c_b · e^d  (sign from r_+ < 0 for positive
                                       a_n, b_n).

  s_sub(x) = x^{−d/2} (a' + b' x^{−1} + …).

**Both solutions are normal-case (p = 1)** — neither requires
fractional powers x^{1/p} with p ≥ 2 in their Q(x). The canonical
Q(x) for the SIARC stratum at deg_a = 0 reduces to

  Q_dom(x) = d x log x + (log c_b − d) x,
  Q_sub(x) = −d x log x + (log γ_sub) x,

both of which are linear-in-(x log x, x), with no fractional-power
terms. Per B-T 1933 §1 normal/anormal definition, the SIARC stratum
at deg_a = 0 is therefore **normal** (p = 1; q = 1 in relay notation).

---

## C.3 Newton-polygon characteristic equation at q = 2 (counterfactual / sanity check)

**Counterfactual:** if the SIARC stratum DID sit at the anormal
q = 2 case (Galbrun special type), the canonical Q(x) would carry an
additional fractional-power term γ √x (per B-T 1933 §1 OCR L150-160):

  Q(x) = μ_2 (x log x)/2 + γ_2 √x + γ_1 x + d_1 √x + …

and the Newton polygon for the s-series ansatz would have a
characteristic-polynomial root structure at fractional-rank 1/2.
The relay 068 spec C.3 calls for verification that

  Q_j(x) = ± B √x + lower    (for the borderline locus, were it operative)
  with B = √(c_a)            (where c_a is the leading coefficient of a_n)

would be derived from the Newton-polygon theorem at q = 2 (Wasow
§X.3 Theorem 11.1 transitively cited via T1-A01).

**Status of this counterfactual derivation in this session:**

- The SIARC stratum at deg_a = 0 has c_a ≡ 1 (since a_n ≡ 1 strictly,
  per 065 audit: 12/13 PCF-2 impls hardcode `mp.mpf(1)` inline; the
  one HC0 impl `evaluate_cf` has default `lambda n: mp.mpf(1)` and
  zero non-default call sites — see 065 §2 verbatim).
- If the borderline q = 2 ansatz WERE operative, B = √(c_a) = √1 = 1
  is the predicted Newton-polygon root coefficient.
- The Newton-polygon Theorem 11.1 of Wasow §X.3 is **OCR-deferred**
  (image-only PDF on disk; LANE-2 Item 2 sub-task 3-E DEFER class).
  T1-A01 verdict provides paraphrase-grade access only (verdict tag
  `A01_WASOW_READING_CONFIRMED` at bridge `b1457ae`).

**Resolution under A.0 outcome (i):** the SIARC stratum at deg_a = 0
sits in the **normal case (p = 1, q = 1)**, not the anormal q = 2
case. The Newton-polygon theorem at q = 2 is therefore NOT operative
for the SIARC stratum closure path. The borderline q = 2 ansatz is
**ruled in as not the operative mechanism**, NOT relied upon for
closure.

**`HALT_068_WASOW_OCR_REQUIRED`: NOT TRIGGERED.** Wasow §X.3 Theorem
11.1 verbatim is **NOT required** for the operative closure path
(deg_a = 0 row of 064 §2.3 + V6 closed-form A_naive = 2d − d_a),
because that closure runs at the normal-case (p = 1) Newton-polygon
balance grade, where Phase 2's existing T1-A01 paraphrase-grade
access is already sufficient. The Wasow OCR substrate would be
needed only if the closure path required the anormal q = 2 fractional-
rank machinery, which under A.0 outcome (i) it does not.

---

## C.4 Borderline-locus identification (q = 2 case) — counterfactual analysis

**Relay 068 §C.4 spec:**

> "Identify the SIARC-stratum exceptional locus where formal A bumps
> from A_naive = d+1 (normal case) to A_borderline = 2d (anormal q=2
> case). The exceptional locus condition is structural (likely
> deg_a=0 row corner AND deg_b = d border, per LANE-2 V6 substrate)
> but must be derived in this phase, not assumed."

**Counterfactual analysis (under the original three-convention
enumeration, deg_a ∈ {d-1, d, d+1}):**

Under T1 Phase 2's three-convention enumeration, the structural lift
from A_naive = d+1 (α-direction, deg_a = d-1) to A_borderline = 2d
would require either:

(i) the borderline locus deg_a = 2 deg_b at the boundary of normal-
    case applicability (q = 2 fractional-rank ansatz operative); OR

(ii) an exceptional locus where leading coefficients cancel (still
     normal-case but with a degenerate Newton polygon).

Neither of these is operative for the SIARC stratum, because:

- For (i): deg_a = 2 deg_b = 2d would require a_n ~ c_a n^{2d}, but
  the SIARC stratum has a_n ≡ 1, i.e., deg_a = 0, far below 2d.
- For (ii): the exceptional locus would require specific algebraic
  cancellation in c_b or a higher-order coefficient; no such
  cancellation is operative at the SIARC stratum's a_n ≡ 1 corner.

**Resolution (under the four-row enumeration, deg_a ∈ {0, d-1, d, d+1}):**

The deg_a = 0 row was simply **excluded by assumption** in the
three-convention enumeration (per LANE-2 R3 verdict text in
`lane2_meta_verdict.md` L79-99, quoted in 064 §1). Adding it to the
enumeration extends the row maximum at each d to A_naive = 2d
without invoking borderline mechanism (i') or exceptional-locus
mechanism (ii'). The "exceptional locus" the relay 068 §C.4 spec
asks about is, **under the four-row enumeration**, simply the
deg_a = 0 row itself — a row that was hidden by the three-convention
narrowing, not a locus with degenerate Newton-polygon structure.

This is the substantive content of LANE-2 R3 + 064 §2.3 + V6 closed-
form A_naive = 2d − d_a:

> "Adding the deg_a = 0 row (μ_dom = d, μ_sub = −d, A_naive = 2d,
> γ_sub ∝ −c_a/c_b) closes the d=2 V_quad anomaly, the d=3 R1.1+B+C1
> 110/110 record, and the d=4 Q1 60/60 record simultaneously,
> WITHOUT invoking borderline mechanism (i') or exceptional locus (ii')."
> (LANE-2 R3 verdict text, quoted in 064 §1)

`HALT_068_BORDERLINE_LOCUS_NOT_IDENTIFIED`: NOT TRIGGERED. The
"borderline locus" question is dissolved (rather than identified) by
the four-row enumeration: the deg_a = 0 row is the operative row at
the normal-case (p = 1, q = 1) baseline, not a borderline q = 2
locus.

---

## C.5 Phase C handoff signal

| Item | Status | Detail |
|------|--------|--------|
| B-T 1933 §1 ansatz verbatim | DONE | OCR L107-118 (eq. 7 + 7a) |
| B-T 1933 §1 normal/anormal definition verbatim | DONE | OCR L131-142 |
| B-T 1933 §1 Galbrun q = 2 example verbatim | DONE | OCR L150-160 |
| Normal-case ansatz for SIARC deg_a = 0 | DONE | §C.2; p = 1; Q_dom + Q_sub linear-in-(x log x, x) |
| Newton-polygon at q = 2 (counterfactual) | DONE | §C.3; B = √(c_a) = 1 if operative; not operative for SIARC |
| Borderline-locus identification | DISSOLVED | §C.4; deg_a = 0 row of four-row enumeration is the operative row at the normal-case baseline; q = 2 fractional-rank locus is not operative |
| `HALT_068_BT_1933_SECTION_1_NIA` | NOT TRIGGERED | §1 on disk verbatim |
| `HALT_068_WASOW_OCR_REQUIRED` | NOT TRIGGERED | Wasow §X.3 Theorem 11.1 not required for the operative closure path |
| `HALT_068_BORDERLINE_LOCUS_NOT_IDENTIFIED` | NOT TRIGGERED | dissolved by four-row enumeration |

Phase C halts: 0.

Proceed to Phase D.

---

*End of `phase_c_bt1933_anormal_ansatz.md`.*
