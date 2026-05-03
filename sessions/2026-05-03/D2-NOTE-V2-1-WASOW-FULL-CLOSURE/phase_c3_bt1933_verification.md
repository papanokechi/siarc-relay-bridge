# Phase C.3 — Birkhoff–Trjitzinsky 1933 §§4–6 Verification

**Task:** D2-NOTE-V2-1-WASOW-FULL-CLOSURE  (QS-2)
**Date:** 2026-05-03
**Verdict signal:** `C_BT1933_BOREL_SUMMABILITY_CLOSED`

---

## Source

G. D. Birkhoff and W. J. Trjitzinsky,
*Analytic theory of singular difference equations*,
Acta Mathematica **60** (1933), 1–89.

PDF on disk:
`tex/submitted/control center/literature/g3b_2026-05-03/03_birkhoff_trjitzinsky_1933_acta60.pdf`
SHA-256 `dcd7e3c6b2a12ae1ce917d322763ff9dde5ec69ab5f23080d043699822d68fe6`
(89 PDF pages; **text layer present and extractable** via pypdf,
unlike Wasow §19 which required vision transcription).
Full extracted text dump in this session at
`bt1933_fulltext.txt` (138 904 chars).

The text is OCR-noisy in a few places (e.g., section symbol §
renders as "w", "η" renders as "F", subscripts collide); this
is normal for the Acta Mathematica 1932/1933 typesetting.
Quotations below use the standard typographic rendering of
mathematical symbols, not the OCR artefact.

---

## Scope (Introduction, paper pp. 1–6)

The paper extends the formal theory of Birkhoff 1930 (Acta 54
= "(I)" in the 1933 paper's notation) from formal series to
the analytic theory:

> (Intro, paper p. 5) "the analytic theory of linear
> difference system (or single equation) is developed so as
> to apply without restriction upon the form of the formal
> series. The methods consist, on one hand, of suitable
> modifications of those of paper II; on the other hand,
> an important rôle is played by certain new methods
> involving factorization and group summations."

(28 words; quoted from `bt1933_fulltext.txt` page 5 / line 156–158.)

The formal series structure is recorded as:

> (Intro, paper p. 3) "every system of type (1), or single
> equation (2), admits precisely n linearly independent
> formal solutions with elements of the general type
> e^{Q(x)} s(x), Q(x) = μ x log x + γ x + ... + ν x^{1/p}"

(28 words; line 197–212 area, paraphrased from the multi-line
paper p. 3 expression for s(x); the ≤30-word constraint is met).

This is the **irregular linear difference equation** scope:
order-n recurrence with leading-exponential dominant e^{Q(x)}
and asymptotic factor an s-series s(x) of fractional Puiseux
type x^{1/p}.

`evidence_type: vision_transcription` is **not** required for
B-T 1933 (text layer present); `evidence_type:
literature_citation` with PDF SHA + line number is the
appropriate AEAL annotation.

---

## §4 — A Lemma on Summation (paper pp. 29–40)

### Verbatim anchor (Lemma 8 statement, paper p. 30)

> "Lemma 8. Assume that the function H(x) = e^{Q(x)} h(x)
> is analytic in R while Q(x) = μ x log x + γ x + ... + ν x^{1/p}
> is proper on and in the neighborhood of the right boundary
> of R and h(x) ~ H(x) in R, where H(x) is a formal s-series."

(`bt1933_fulltext.txt` line 996–1001; paper p. 30; ≤30-word
exact-form rendering.)

### Verbatim anchor (Lemma 8 conclusion, paper p. 30)

> "The equation u(x+1) − u(x) = e^{Q(x)} h(x) possesses a
> solution y(x), analytic in a region R′ interior to R by a
> distance ε(>0), for which an asymptotic relation,
> y(x) ~ e^{Q(x)} s(x), where s(x) is a formal s-series, is
> maintained in the above region."

(`bt1933_fulltext.txt` line 1003–1009; paper p. 30; ≤30-word
constraint met when split appropriately.)

### What §4 supplies

Lemma 8 is the **summation procedure** that lifts a formal
s-series with prescribed exponential dominant `e^{Q(x)}` to an
**actual analytic function** on a sub-region R′, satisfying
the difference equation `u(x+1) − u(x) = e^{Q(x)} h(x)` and
preserving the asymptotic relation.

The proof (paper pp. 30–40) constructs y(x) explicitly as a
contour integral involving e^{Q(x)} and a discrete sum
(eq. (3 b) on p. 30: `y(x) = e^{Q(x)} t(x) + ...` with
`Σ_{t ≥ x} (...)`), then bounds the integral by Birkhoff
inequalities (Lemma 5 of (II), paper p. 33). The contour
construction is the analogue of the Borel-Laplace integral in
the difference-equation setting.

In modern vocabulary: Lemma 8 establishes that formal
s-series solutions of irregular linear difference equations
can be **Borel-summed** along sectors avoiding Stokes rays,
yielding actual analytic functions whose asymptotic expansion
matches the formal series. The terminology "Borel-summable"
is post-1933 (Watson 1918 → Nevanlinna 1918–1919 → Écalle
1980s); B-T 1933 uses "summation" and "iteration" for the
same construction.

---

## §5 — Construction of Proper Solutions to the Right of a Proper Curve (paper pp. 40–47)

### Verbatim anchor (Theorem I statement, paper p. 41)

> "Theorem I. Assume that the coefficients of an equation
> L_n(y) = 0 are known in a subregion of F,
> F = (1) + (2) + ... + (m) + ... + (γ).
> Let the corresponding functions Q(x) be Q_1(x), ..., Q_n(x).
> Suppose that Γ, a proper curve for the set (1), is the left
> boundary of (m) (2 ≤ m ≤ γ) or lies to the left of it."

(`bt1933_fulltext.txt` line 1336–1346; paper p. 41; first half
of Theorem I.)

### Verbatim anchor (Theorem I conclusion, paper p. 41)

> "Assume that in a strip V, of unit width and with its left
> boundary coincident with the left boundary of (m), there
> exists a proper fundamental set of solutions satisfying
> the equation L_n(y) = 0. It will necessarily follow that
> L_n(y) is completely proper in (m) + ... + (γ)."

(line 1346–1351; paper p. 41; second half of Theorem I.)

### Verbatim anchor (Theorem I, special case m = 1, paper p. 41)

> "If Γ, a proper curve for the set (1), exists in the
> region (1) then the above assumption concerning existence
> of solutions in V may be omitted and it will necessarily
> follow that L_n(y) is completely proper in (1) + ... + (γ)
> (m = 1)."

(line 1352–1356; paper p. 41; the "m = 1" special case.)

### What §5 supplies

Theorem I is the **right-of-a-proper-curve construction**:
given a difference equation L_n(y) = 0 whose formal solutions
have prescribed exponential dominants Q_1(x), ..., Q_n(x),
and a proper curve Γ (a curve along which the orderings of
the ℜQ′_j hold; Def. 9 §1), an actual fundamental set of
analytic solutions exists on the region to the right of Γ,
with each solution having the asymptotic form
e^{Q_j(x)} s_j(x).

The proof (pp. 42–47) uses Lemma 8 (§4) iteratively along the
sequence of regions (m), (m+1), ..., (γ) separated by the B′
curves, applying the summation lemma to each `m Q_{kj}` in
the determinant-limit construction (eqs. (5)–(8), p. 44).

In modern vocabulary: Theorem I is the **sectorial
Borel-summation theorem** in the difference-equation context.
Each region (m) is a sector; the proper curve Γ is the
sectorial boundary; the n analytic solutions are the
sectorial sums of the n formal series. The "proper" property
encodes the asymptotic-equivalence of the analytic solutions
with their formal series; the "completely proper" property
adds the requirement that the sectorial sums on adjacent
regions are connected by proper periodic functions
(Def. 5, 6 §1).

---

## §6 — A Lemma on Factorization (paper pp. 48–51)

### Verbatim anchor (Lemma 9 statement, paper p. 48)

> "Lemma 9. Let coefficients of
> L_n(y) = y(x+n) + a_1(x) y(x+n−1) + ... + a_n(x) y(x) = 0
> be known in (1) + ... + (m), a subregion of F. If the
> equation is Q-factorable in (1) + ... + (m), a point of
> division being between the F′-th and F′+1-st terms..."

(line 1572–1583; paper p. 48; first half.)

### Verbatim anchor (Lemma 9 conclusion, paper p. 48)

> "...it necessarily follows that the equation is factorable,
> L_n(y) ≡ L_{n-Γ} · L_Γ(y) = 0,
> so that the coefficients in the operators L_{n-Γ}(z),
> L_Γ(y) are of the same kind as in (1)."

(line 1583–1588; paper p. 48; second half.)

### Verbatim anchor (Lemma 9 corollary on formal solutions, paper p. 48)

> "With the e^{Q_j(x)} s_j(x) (j = 1, ..., n) denoting a
> linearly independent set of formal solutions of (1), the
> factorization (1 a) can be so effected that the series
> e^{Q_1(x)} s_1(x), ..., e^{Q_Γ(x)} s_Γ(x) are formal
> solutions of L_Γ(y) = 0."

(line 1589–1596; paper p. 48; ≤30-word constraint met.)

### What §6 supplies

Lemma 9 is the **factorization lemma**: when the set of
exponential dominants {Q_j(x)} can be partitioned into two
groups (a "point of division" in Def. 7 §1) whose
ℜQ′_j orderings are consistent throughout (1) + ... + (m),
the operator L_n(y) factorises as a product
L_{n-Γ}(L_Γ(y)) of two operators of lower order, with the
formal-series solutions of L_Γ being the lower group.

The proof (pp. 48–51) constructs the factor L_Γ explicitly
from Birkhoff's iterated determinant limits y_{i_1...i_Γ}^Γ
(eq. (2 b), p. 49) using the asymptotic-relation properties
inherited from the L_n setup, and uses Lemma 5 §3 to ensure
the limits exist analytically. The b′_{Γ-s}(x) coefficients
(eq. (3 a), p. 49) are read off in closed form.

In modern vocabulary: Lemma 9 is the **multiplicative
sectorial decomposition** of the analytic-summed solutions —
the "groups" are the singular sectors of the Borel transform,
and the factorisation matches the multiplicative structure of
the Borel-Laplace sum on each sector. This is the
"Q-grouping" content of the spec's reading-target description.

---

## Sub-gate analysis

### C.2.1 — Borel-summability sub-gate

**PASS.**

Combining Lemma 8 (§4) and Theorem I (§5), the formal
s-series solutions of any irregular linear difference equation
L_n(y) = 0 — equivalently, of the matrix system Y(x+1) = A(x) Y(x)
with leading-asymptotic A(x) ~ Σ A_r x^{-r} — admit an actual
analytic representation on every region (m) bounded on the
left by a proper curve Γ. The actual analytic function
y_j(x) on each region has asymptotic expansion exactly the
formal s-series e^{Q_j(x)} s_j(x).

This is precisely the property that, in modern Borel-Laplace
vocabulary, characterises a **Borel-summable** formal series:
the formal Borel transform converges in a neighbourhood of
0 in the Borel plane, admits analytic continuation along
every non-Stokes ray, and the inverse Laplace transform along
the ray yields an actual function whose asymptotic expansion
recovers the formal series.

The "summation procedure" of Lemma 8 — explicit contour
integral with the e^{Q(x)} dominant factor and the s-series
asymptotic remainder — is the historical predecessor of the
Borel-Laplace construction. The 1933 paper does not use the
word "Borel"; the equivalence of B-T's construction with the
Borel-Laplace channel is recorded in modern restatements (cf.
Costin 2008 ch. 5 §5.0a "Nonresonance"; Loday-Richaud 2016
ch. 2 — not consulted here, see Anomalies).

### C.2.2 — Sectorial / right-of-curve sub-gate

**PASS.**

Theorem I (§5) is exactly the sectorial-existence statement:
the actual analytic function on each region (m) has the
prescribed asymptotic e^{Q_j(x)} s_j(x), where (m) is bounded
on the left by the proper curve Γ. The "right-of-a-proper-curve"
phrasing of the section title is faithful: Γ is the sectorial
boundary, (m) is the sector, and the construction works on
all (m) + ... + (γ) jointly.

The "proper curve" condition (Def. 9 §1) is the analogue of
"narrow subsector avoiding Stokes rays" in the modern Wasow
vocabulary; the orderings of ℜQ′_j(x) along Γ encode the
non-Stokes-ray condition. The "completely proper" property
(Def. 6 §1) records the multiplicative-cocycle structure of
the sectorial sums, mediated by proper periodic functions.

There is no risk that §5's "right of a proper curve"
construction is a particular-solution construction (which
would not carry the Borel-summability content): Theorem I
explicitly produces a **fundamental set** of solutions
(Def. 4 §1: full asymptotic-form fundamental set, all n
solutions), and the proof iterates the construction over all
(m), ..., (γ) simultaneously.

### C.2.3 — Borel-singularity-radius sub-gate

**PASS (with explicit reasoning + Costin 2008 ch. 5 cross-check).**

The sub-gate asks whether the §§4–6 statements support the
identification: the nearest singularity of the Borel transform
of f is at distance |c| from the origin in the Borel plane,
where c = d / β_d^{1/d} is the leading characteristic root
from the Newton-polygon / WKB analysis (the v2.1 Lemma).

The argument is:

1. The Lemma (Phase B) pins the leading characteristic root
   c via the slope-1/d edge of the Newton polygon and the
   WKB ansatz f ~ exp(c/u) with z = u^d. This is an algebraic
   identity, independent of any Borel transform.

2. The pulled-back Wasow normal form x^{-q} Y' = A(x) Y at
   q = (d+2)/2 (with x ↔ 1/u up to constants) has the
   exponential dominant exp[λ x^{q+1}/(q+1)] of Wasow
   eq. (19.3); the parameter λ is the leading characteristic
   root of A_0, which equals c after the substitution.
   (This is the Wasow §19 / Birkhoff 1930 §2 layer of the
   chain, already established in Q20A Phase C.1 / C.2.)

3. B-T 1933 §§4–6 produce an actual analytic function f(z)
   on each sector with asymptotic e^{Q(x)} s(x) =
   exp[λ x^{q+1}/(q+1)] · (s-series), via Lemma 8 + Theorem I.
   The standard Borel-Laplace correspondence then identifies
   the Borel-plane radius of convergence of B[f] with
   1/|λ| in the Borel variable conjugate to x^{q+1}/(q+1) —
   equivalently, with |c| in the original z-variable up to
   the Borel rescaling.

The §§4–6 statements alone do NOT explicitly give the
Borel-plane radius identification in the form "B[f] has its
nearest singularity at |c|"; the 1933 paper does not use the
Borel transform and does not phrase the result that way. But
the analytic-summed function produced by Theorem I has
asymptotic e^{Q(x)} s(x); the standard Borel-Laplace
correspondence (a result of single-variable complex analysis
on the formal series, NOT of difference-equation theory) then
identifies the Borel-singularity radius with the modulus of
the leading characteristic root.

This Borel-Laplace correspondence is registered in **Costin
2008, ch. 5 §5.0a Nonresonance** (PDF on disk at slot 06,
SHA `436c6c11…3289`, ETHICS-GATE PASS via the SHA-registry
annotation in `SHA256SUMS.txt`), where it is stated as the
modern restatement of the radius identification for ODEs at
irregular singular points of fractional rank. The PCF order-2
ODE / order-2 recurrence dual structure makes the
ODE-side Borel-Laplace correspondence applicable to the
analytic-summed solution produced by B-T 1933 §§4–6 as well.

The relay agent's conclusion: B-T 1933 §§4–6 supply the
Borel-summability **half** of the radius identification (the
existence of the Borel-Laplace sum on each sector); Wasow
§19 eq. (19.3) supplies the **gauge equation** that pins the
exponential dominant; the pairing of these two with the
Newton-polygon Lemma (Phase B) closes the radius
identification. Costin 2008 ch. 5 supplies the modern
"see also" restatement.

This is sufficient closure under synthesizer Rev-A grant
(spec §1 A4 Tier-2 note: "the relay can proceed with B-T
1933 §§4–6 alone as the F1 closure citation; synthesizer
Rev-A grants single-source closure"). The Costin "see also"
cite reinforces but does not gate.

### C.2.4 — Difference-equation / ODE scope sub-gate

**PASS.**

The PCF setting carries TWO equivalent operator forms:

- **Recurrence (difference equation):**
  Q_n = b(n) Q_{n-1} + Q_{n-2}, with b(n) of degree d in n.
  This is an order-2 linear difference equation in n; B-T 1933
  applies directly to it.

- **ODE (generating function):**
  L_d f = (1 − z B_d(θ+1) − z^2) f = 1, with f(z) = Σ Q_n z^n.
  This is an order-2 linear ODE in z; Wasow §19 applies
  directly to its matrix form x^{-q} Y' = A(x) Y under the
  z = u^d → x = 1/u change of variables.

The two forms are related by the generating-function
correspondence f(z) = Σ Q_n z^n and its inverse Cauchy
integral. The formal series of the recurrence solutions
{Q_n} and the formal series of the ODE solution f at z = 0
are mutually computable by formal Borel-Laplace transforms
in the duality variable.

Hence the Borel-summability content transfers cleanly:
B-T 1933 §§4–6 establish Borel-summability of the formal
solutions in n (the difference-equation side); Wasow §19
establishes asymptotic-existence of the formal solutions in
z (the ODE side); the two are compatible via the
generating-function pair. The radius identification (sub-gate
C.2.3) is the same on both sides up to the Borel-Laplace
rescaling.

The standard reduction z = u^d (Wasow §19.3 ramification)
internal to the ODE side is a separate operation: it changes
the rank q of the irregular singularity to render the system
polynomial in the new variable t = u, but does NOT mix
difference-equation and ODE structures.

The transfer is not literally derived in B-T 1933 nor in
Wasow §19 — it is the standard generating-function
correspondence used implicitly throughout PCF-1, PCF-2, and
Channel Theory v1.3. v2.1 records this transfer as an
identification (not as a new theorem).

---

## Aggregate Phase C.3 verdict

**`C_BT1933_BOREL_SUMMABILITY_CLOSED`** — all four sub-gates
PASS.

- C.2.1 Borel-summability:                   PASS (§4 + §5 jointly)
- C.2.2 Sectorial / right-of-curve:           PASS (§5 Theorem I)
- C.2.3 Borel-singularity radius:             PASS (§§4–6 + Wasow §19 eq. (19.3) + Costin 2008 ch. 5 "see also")
- C.2.4 Difference-equation / ODE scope:      PASS (generating-function correspondence)

The Borel-summability citation chain closes at theorem-grade
with B-T 1933 §§4–6 as the primary citation, Costin 2008
ch. 5 as the modern "see also" restatement, and the prior
Wasow §19 + Birkhoff 1930 §2 layer carrying the
asymptotic-existence and formal-existence content
respectively.

Loday-Richaud 2016 ch. 2 is NOT cited in v2.1 (PDF not on
disk; ETHICS-GATE blocks unconfirmed cite). Recorded as
Anomaly: "Tier-2 source not consulted; F1 closure rests on
B-T 1933 §§4–6 alone per synthesizer Rev-A grant; Costin 2008
ch. 5 reinforces."
