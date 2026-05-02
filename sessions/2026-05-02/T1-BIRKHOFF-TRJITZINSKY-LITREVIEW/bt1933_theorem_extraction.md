# Q1 — Birkhoff–Trjitzinsky 1933: theorem extraction in modern notation

**Task:** T1-BIRKHOFF-TRJITZINSKY-LITREVIEW, Phase 1
**Date:** 2026-05-02
**Scope:** What Birkhoff & Trjitzinsky, *Analytic Theory of Singular
Difference Equations*, Acta Mathematica 60 (1933), 1–89 (hereafter
**B–T 1933**) actually proves, in modern notation, with a clean
delineation between (i) refereed-rigorous content of B–T 1933 itself,
(ii) folklore commonly attributed to B–T but in fact established by
later authors, and (iii) extensions that are still open.

**Access caveat (important).** B–T 1933 was not opened directly in
Phase 1 (Acta Math 60 is on JSTOR / Project Euclid behind a
historical-archive paywall on at least one of the available routes;
secondary sources were used). Where a precise quotation would be
required, the deliverable marks the line as
`[paraphrase from <secondary>]`. The secondary sources used are:

* Wasow, *Asymptotic Expansions for Ordinary Differential Equations*,
  Wiley/Interscience 1965, Ch. X (canonical secondary treatment of
  the linear difference-equation analogue of Hukuhara–Turrittin).
* Jordan, *Calculus of Finite Differences*, 3rd ed., Chelsea 1965
  (independent expository review).
* Immink, *Asymptotics of Analytic Difference Equations*, Lecture
  Notes in Mathematics **1085**, Springer-Verlag 1984
  (modern Borel-summability formalisation).
* Wimp & Zeilberger, "Resurrecting the asymptotics of linear
  recurrences", J. Math. Anal. Appl. **111** (1985), 162–176
  (modern combinatorialist's reading of B–T's formal solutions).
* Sauzin, "Introduction to 1-summability and resurgence", in
  *Divergent Series, Summability and Resurgence I* (LNM 2153), 2016.

Items below are flagged **(B–T 1933 rigorous)**, **(folklore / later
attribution)**, or **(beyond B–T 1933)** as appropriate.

---

## Setup

Let
$$
   L y(x) \;=\; \sum_{k=0}^{n} p_k(x)\, y(x+k) \;=\; 0,
   \qquad p_k \in \mathbb{C}\{x^{-1}\}\big[x\big]
   \text{ (rational, polynomial, or meromorphic at }\infty\text{)},
$$
with $p_0 p_n \not\equiv 0$. Write
$\deg_x p_k = d_k$ and let $\deg = \max_k d_k$. The **Newton polygon
at $\infty$** is the lower convex hull in $\mathbb{R}^2$ of the points
$\{(k, d_k - k_0) : 0 \le k \le n,\ p_k \not\equiv 0\}$ for a
normalisation $k_0$ (conventions differ; we use B–T's convention as
restated by Wasow 1965 §X.2). The polygon's slopes
$\sigma_1 < \sigma_2 < \cdots < \sigma_r$ are the **Birkhoff ranks**
of $L$ at $\infty$.

In the SIARC PCF stratum the order is $n = 2$ (a three-term recurrence
$p_2(x) y(x+1) - p_1(x) y(x) + p_0(x) y(x-1) = 0$) and
$\max(d_0, d_1, d_2) = d$ is the ambient PCF degree. The Newton
polygon then has either one slope ($d/2$ or $d/1$ depending on
normalisation) or two slopes when $d_1 < \tfrac{1}{2}(d_0 + d_2)$
("fractional-rank" / hyper-irregular cell).

---

## Q1.a — The formal-series existence theorem ("B–T 1933, Theorem 1")

**Statement (B–T 1933 rigorous, paraphrased).** Let $L$ be a linear
difference operator of order $n$ with rational coefficients, and let
$\sigma_1 < \cdots < \sigma_r$ be the slopes of the Newton polygon
of $L$ at $x = \infty$. Then there exist a positive integer $q$ and
$n$ formal solutions of $Ly = 0$ of the canonical form
$$
   \widehat y_j(x) \;=\; \exp\!\bigl(P_j(x^{1/q})\bigr)\;
                          x^{\rho_j}\;
                          \widehat S_j\!\bigl(x^{-1/q}\bigr),
   \qquad j = 1, \dots, n,
$$
where:

* $P_j$ is a polynomial in $x^{1/q}$ of degree at most $q\sigma_r$
  (the "exponential polynomial" / characteristic polynomial of the
  highest slope);
* $\rho_j \in \mathbb{C}$ is the formal characteristic exponent
  (encoding the leading $x^\rho$ algebraic factor);
* $\widehat S_j(t)$ is a formal power series in $t = x^{-1/q}$, in
  general **divergent** (Gevrey of order $1/\sigma_k$ at slope
  $\sigma_k$ in the modern reading of Immink 1984 / Braaksma 1992;
  this Gevrey statement is **beyond B–T 1933** and is not in B–T's
  text).

[paraphrase from Wasow 1965 §X.2; Immink 1984 §1.3]

**Hypotheses precisely required by B–T 1933.**

1. Rational coefficients (B–T also covers meromorphic-at-$\infty$
   coefficients with suitable growth bounds; the rational case is
   the principal one).
2. Non-vanishing leading and trailing coefficients
   $p_0(x), p_n(x) \not\equiv 0$.
3. **Genericity / non-resonance condition** on the characteristic
   polynomial of the highest slope (no two roots differ by an
   integer in $x^{1/q}$; this is the analogue of the Hukuhara
   non-resonance condition for ODE).

**Class of operators covered.** All slopes from $0$ (regular case;
trivially Fuchsian) up to integer slopes; B–T 1933 also addresses
**fractional slopes** (slope $p/q$ with $q > 1$), which is the
content distinguishing B–T 1933 from Birkhoff 1911.

**Folklore note (clearly NOT a result of B–T 1933).** The
**convergence** of the formal $\widehat S_j$ in some sector
(rather than mere formal existence) is **NOT** in B–T 1933.
Convergence in the regular-singular case is Turrittin 1955;
multisummability of the divergent case is Braaksma 1991+.

---

## Q1.b — The Stokes-classification theorem ("B–T 1933, Theorem 2")

**Statement (B–T 1933 rigorous, paraphrased).** Two formal solutions
of the canonical form above belong to the same Stokes datum (i.e.
agree term-by-term in their formal expansion) if and only if they
agree in their characteristic polynomial $P_j$, their exponent
$\rho_j$, and the formal series $\widehat S_j$ as elements of
$\mathbb{C}[\![x^{-1/q}]\!]$. The collection
$(P_j, \rho_j, \widehat S_j)_{j=1}^n$ is a complete formal invariant
of $L$ at $\infty$.

[paraphrase from Wasow 1965 §X.3; Wimp–Zeilberger 1985 §2]

**What this is NOT.** B–T 1933, Theorem 2 is a **formal
classification**. It does *not* establish that distinct Stokes data
correspond to distinct **analytic** solutions on a sector — that is
the Stokes-multiplier theorem of Birkhoff 1913 / Turrittin 1955
(formal-to-analytic lifting), which is **not** the content of B–T
1933, Theorem 2. Confusion on this point is common in the secondary
literature; a direct quotation of B–T 1933 §III would resolve any
remaining ambiguity (flagged in `handoff.md`, "What would have been
asked").

---

## Q1.c — Formal vs. analytic separation

**B–T 1933 establishes:** formal-series solutions of the canonical
form (Q1.a), and a complete formal classification (Q1.b). This is a
**formal** theory. The question of when the divergent series
$\widehat S_j$ is the **asymptotic expansion** of a genuine analytic
solution on a sector — i.e. **Borel summability** or
**multisummability** — is **outside the scope of B–T 1933**.

**B–T 1933 does NOT establish:**

* Borel summability of the formal series in any sector. (This is
  Immink 1984 / 1991+ for the rank-1 case; Braaksma 1991 / 1992 for
  the multisummable / fractional-rank case.)
* Sectorial existence of analytic solutions matching a given formal
  solution as asymptotic expansion. (This is the difference-equation
  analogue of the Hukuhara–Turrittin–Sibuya theorem; established
  rigorously by Turrittin 1955 in the convergent / regular case,
  by Immink in the rank-1 irregular case, by Braaksma in the
  multisummable case.)
* Stokes-multiplier rigidity beyond the formal level.

This delineation is the **single most important** contextual fact
for SIARC's KEYSTONE move: every "B–T proves $A = 2d$"-type claim in
the SIARC corpus must be re-read as "B–T's *formal* slope analysis
predicts $A = 2d$ as a *formal-Newton-polygon* invariant," with the
analytic upgrade to a rigorous statement about actual approximant
errors requiring a post-1933 result (Turrittin / Immink / Braaksma)
on Borel-summability or sectorial asymptotic-existence.

---

## Q1.d — Rank stratification and what B–T 1933 covers

The Birkhoff rank stratification at $\infty$ for a linear difference
operator $L$ of order $n$:

| Stratum | Newton-polygon shape | Coverage |
|---|---|---|
| **Regular / Fuchsian** | single slope $\sigma = 0$ | Birkhoff 1911 (predecessor, **not** B–T 1933); Adams 1928 for the second-order case |
| **Regular-singular** | single slope $\sigma \in \mathbb{Z}_{> 0}$, non-resonant | B–T 1933 Thm 1+2 (formal); Turrittin 1955 (analytic, convergent) |
| **Fractional-rank** | single slope $\sigma = p/q$, $q > 1$ | **B–T 1933 Thm 1+2 (formal)**, the principal new content vs. Birkhoff 1911; Braaksma 1991+ (analytic, multisummable) |
| **Multi-slope / hyper-irregular** | $r > 1$ distinct slopes | B–T 1933 partial (formal); Immink 1984 / Braaksma 1991+ (analytic) |
| **Resonant / non-generic** | repeated characteristic roots, log corrections | B–T 1933 partial (formal, with explicit log-correction terms), but the case-by-case enumeration is largely **folklore reattributed to later authors** (Wasow 1965 §X.4 gives the textbook treatment) |

**SIARC PCF stratum (canonical case).** Order $n = 2$, polynomial
coefficients of degree $\le d$, generic discriminant $\not\equiv 0$.
Newton polygon is single-sloped with slope $d$ (or $d/1$ depending
on normalisation); two formal characteristic exponents at
$\infty$. **This is the regular-singular stratum** in the table
above when $d \ge 2$ and the discriminant of the leading symbol
does not vanish identically; B–T 1933 Thm 1+2 covers the formal
content. The arithmetic loci where the Newton polygon degenerates
(Newton-polygon vertex coincidence) lie in the **resonant** row and
are partially treated by B–T 1933 with case-by-case logarithmic
corrections.

---

## Q1.e — "What B–T proved vs. what is folklore"

The secondary literature commonly attributes to B–T 1933 results
which are in fact due to later authors. The **most frequent
misattributions**:

* **"B–T proves Borel summability."** *FALSE.* Borel summability of
  rank-1 difference equations is **Immink 1984/1991**, not B–T 1933.
  B–T's formal series are not, in general, Borel summable; some are,
  some are multisummable, and the regularity classification is
  post-1933.
* **"B–T proves convergence of the formal series in a sector."*
  *FALSE.* This is **Turrittin 1955** in the regular-singular case;
  **Immink** / **Braaksma** in the irregular case.
* **"B–T proves the Stokes-multiplier rigidity theorem."** *FALSE.*
  The rigidity (formal data $\Rightarrow$ analytic data on sectors)
  is **Birkhoff 1913** for ODE, with the difference-equation
  analogue made rigorous by **Turrittin 1955** and **Immink 1984**.
* **"B–T proves $A = 2d$ for the SIARC PCF stratum at all $d$."**
  *FALSE — this is a SIARC-internal statement.* B–T 1933 establishes
  the **formal Newton-polygon slope** (which **predicts** $A = 2d$
  as a formal-asymptotic statement under a specific normalisation
  of the SIARC asymptotic ansatz, see Q3); the analytic upgrade
  from formal slope to actual $A_{\mathrm{PCF}}(b)$ requires a
  post-1933 sectorial-asymptotic result (Turrittin / Wasow / Immink)
  and a separate argument that the SIARC normalisation matches the
  formal exponent without an $O(1)$ shift. **This is the gap that
  Phase 2 of T1 must address.**

The polynomial-coefficient case (the SIARC PCF stratum) **is a
post-1933 formalisation**; B–T 1933's theorems are stated for
rational/meromorphic coefficients without specialising to the
polynomial sub-case, and certainly without specialising to
SIARC's particular three-term-recurrence normalisation. The
specialisation to polynomial coefficients is implicit in
Wasow 1965 §X.3 and explicit in Wimp–Zeilberger 1985.

---

## Phase-1 conclusion (Q1)

B–T 1933 establishes the **formal** existence-and-classification
theorems for linear difference operators with rational coefficients
at the irregular singularity $x = \infty$, including the
fractional-rank case left open by Birkhoff 1911. It does **not**
establish Borel summability, sectorial analytic existence, or
Stokes-multiplier rigidity — those are post-1933 results
(Turrittin 1955, Wasow 1965, Immink 1984+, Braaksma 1991+).

In particular, the SIARC umbrella v2.0 statement "extends $A = 2d$
to all $d$ via the Birkhoff–Trjitzinsky asymptotic theory of
irregular linear difference equations
\cite{Birkhoff1930,BirkhoffTrjitzinsky1933}" (umbrella main.tex,
line 295) is **predicted by, consistent with, and structurally
compatible with** B–T 1933's formal theory; but B–T 1933 *alone*
does **not** rigorously imply the SIARC sharp B4 statement at
$d \ge 3$. The rigorous derivation requires a Turrittin-style
formal-to-analytic upgrade applied specifically to the SIARC
normalisation, plus a non-resonance argument on the
SIARC-arithmetic loci (the modular-discriminant axis of PCF-2
v1.3).
