# Phase C — BT 1933 §5 (13 a) Structural Form (the FILL side)

**Session:** 075 T2-M6-CC-CHART-MAP-CANDIDATE-B1-CHECK
**Phase:** C
**Scope:** structural-form extraction of the candidate substrate
surfaced by 073 unexpected find U1 [CHART-MAP-CANDIDATE-B1] — the
BT 1933 §5 (13 a) periodic-functions across-strip expansion.
SUBSTRATE-INVENTORY ONLY; no chart-map construction is attempted.

---

## §C.1 — Verbatim quote of (13 a) and surrounding text

(C.1.a — equation (13 a) verbatim; 22 words on whitespace-separated
tokens of the equation line + index line, ≤ 50-word ceiling PASS.)

Source: `sessions/2026-05-07/T1-PHASE-3-BT-1933-SECTIONS-4-6-READTHROUGH-073/bt_1933_section_5_extract.md`
SHA `ec2c0d5a2dadef3b3b5342869fff31b5ae7644efe84853512485ffbc014e6b97`,
file at the [p. 47] block (ends near file line L344).

> "(13 a)   p^{r, r+1}_{i j}(x) = ∑ p^{r, r+1}_{i j; π} e^{−π_{i j}(r, r+1)}
>           (i, j = 1, ..., n; r = m, ..., η − 1)"

(C.1.b — companion line specifying the periodic-strip variable; 11
words.)

> "Now |z| = |e^{−x_r}| = e^{−q+v}; thus, it is clear that …"

(C.1.c — context line specifying $x_{r}$ in the strip $V_{r,r+1}$;
21 words.)

> "Let ℑ x_r = ℑ x, x − x_r = integer and restrict x_r to lie in the
>  strip V_{r, r+1} (when ℑ x ≧ Q > o)."

(C.1.d — power-series convergence anchor 49 words; ≤ 50 PASS.)

Source: same file, [p. 47] block (eq. (13) preamble).

> "here the power series converge within a sufficiently small circle
> with z = o for center and, unless p^{r, r+1}_{i j}(x) ≡ o, it may
> be supposed that p^{r, r+1}_{i j; o} ≠ o."

(C.1.e — 073 [CLAIM-B517] paraphrase pulled forward for context;
not re-quoted verbatim here, see 073
`bt_1933_section_5_claim_table.md` SHA `00103c17..` Phase C.4
surfacing block.)

## §C.2 — Substrate-meaning unpack (no claims beyond verbatim)

The equation (13 a) sits inside the §5 Theorem I proof. The matrix
$p^{r,r+1}(x) = (p^{r,r+1}_{i j}(x))$ is defined at p. 46
eq. (11 a) by

  Z^r(x) = Z^{r+1}(x) p^{r, r+1}(x),

i.e. as the **change-of-basis matrix** between the proper matrix
solutions $Z^r(x)$ and $Z^{r+1}(x)$ in adjacent regions $(r)$ and
$(r+1)$ separated by the B'-curve $B^r$. It is the BT-1933 incarnation
of the Stokes / connection-matrix data linking sectorial proper
matrix solutions across angular regions.

Equation (13 a) is the **Fourier / q-series expansion** of each
matrix entry $p^{r,r+1}_{i j}(x)$ in the strip variable $x_r$, with
discrete index $\pi$, integer exponents $\pi_{i j}(r, r+1)$, and
complex Fourier coefficients $p^{r, r+1}_{i j; \pi}$. The associated
periodic variable is $z = e^{-x_r}$ with $|z| = e^{-q+v}$ on the
strip $V_{r, r+1}$.

(All structural labels above are paraphrases of 073's verbatim §5
extract and 073's [CLAIM-B517] tag; no new claims introduced.)

## §C.3 — Decomposition into structural primitives

The structural primitives below are extracted from the §C.1 verbatim
quotes (and the §C.2 unpack of 073-tagged context). Each primitive
is labelled `[FILL-PRIMITIVE-Cn]` per envelope §6.

### [FILL-PRIMITIVE-C1] Domain space of (13 a)

- **Object:** the entry $p^{r, r+1}_{i j}(x)$ is indexed by
  matrix-entry pair $(i, j) \in \{1, \ldots, n\}^{2}$ and adjacent-
  region label $r \in \{m, \ldots, \eta - 1\}$, **and** is a
  function of the continuous strip variable $x_{r}$ (with
  $\Im x \geq Q > 0$).
- **Dimensionality:** discrete part $n^{2} \times (\eta - m)$;
  continuous part is one complex variable $x$ in the strip
  $V_{r, r+1}$.
- **Nature:** a function-space object — entries of an $n \times n$
  matrix-valued function of $x$, **not** parameter-space coordinates
  of an equation.

### [FILL-PRIMITIVE-C2] Codomain space of (13 a)

- **Object:** complex-valued holomorphic function of $x$ (or
  $x_{r}$) on the strip $V_{r, r+1}$ where $\Im x \geq Q > 0$.
- **Dimensionality:** one complex value per $(i, j, r)$ matrix-entry
  per $x$ in the strip.
- **Constraint(s):** holomorphy on the strip; convergent power
  series in $z$ within a small circle; periodicity in $\Im x$
  (period 1, since $z = e^{-x_{r}}$ is periodic under $x \mapsto
  x + 1$).
- **Nature:** function-space object (complex-valued function on a
  strip), **not** a real parameter scalar.

### [FILL-PRIMITIVE-C3] Functional form of (13 a)

- **Form:** $p^{r, r+1}_{i j}(x) = \sum_{\pi} p^{r, r+1}_{i j; \pi}
  e^{-\pi_{i j}(r, r+1)}$ with $|z| = e^{-q + v}$, i.e. a
  **Fourier / q-series expansion** in the periodic variable
  $z = e^{-x_{r}}$.
- **Index nature:** $\pi$ is a discrete index; $\pi_{i j}(r, r+1)$
  are **integer exponents** per the (13) preamble verbatim.
- **Coefficient nature:** $p^{r, r+1}_{i j; \pi}$ are complex
  numbers (not functions), determined by analyticity on the strip
  and the 073 [CLAIM-B517] structural data.
- **Nature:** ANALYTIC series expansion, **not** an algebraic
  closed-form polynomial / rational expression.

### [FILL-PRIMITIVE-C4] Map cardinality / arity

- **Cardinality:** $n^{2}$ scalar entry-functions per region pair
  $(r, r+1)$; total $n^{2} \times (\eta - m)$ scalar
  entry-functions.
- **Arity per entry:** each $p^{r, r+1}_{i j}(x)$ is a function of
  one continuous complex variable $x$ on the strip.
- **Net structure:** $\{(i, j, r)\}$-indexed family of functions
  $\mathbb{C}_{\text{strip}} \to \mathbb{C}$.

### [FILL-PRIMITIVE-C5] Sectorial / regional structure

- **Specification by §5 Theorem I + (11 a):** (13 a) is **sectorial
  by construction** — it is defined per pair of adjacent regions
  $(r, r+1)$ separated by the B'-curve $B^{r}$, and each entry
  $p^{r, r+1}_{i j}(x)$ encodes how the proper matrix solution
  $Z^{r}(x)$ in region $(r)$ recombines into $Z^{r+1}(x)$ in
  region $(r + 1)$ across the angular-sector boundary.
- **Anchor:** 073 `bt_1933_section_5_extract.md` SHA `ec2c0d5a..`
  [p. 46] block eq. (11 a); same file [p. 47] block eq. (13 a).

### [FILL-PRIMITIVE-C6] Constraint / linear relation structure

- **Domain side:** matrix-index combinatorics
  $i, j \in \{1, \ldots, n\}$ + region adjacency
  $r \in \{m, \ldots, \eta - 1\}$ — **no algebraic linear constraint
  on parameters** (the BT 1933 setup parametrises the equation by
  $L_{n}(y) = 0$ coefficients $a_{j}(x)$, not by a finite-tuple
  parameter chart).
- **Codomain side:** convergent-power-series condition on $z$
  within a small circle around $z = 0$; non-vanishing leading
  coefficient $p^{r, r+1}_{i j; 0} \neq 0$ (unless the entry is
  identically zero) — these are **analytic** constraints on the
  series, not algebraic constraints on parameter scalars.
- **Note:** there is **no analogue** of the Okamoto null-sum
  $\alpha_{\infty} + \alpha_{0} + \beta_{\infty} + \beta_{0} = 0$
  in (13 a)'s structure as quoted; in particular, the 073 §5
  extract does not surface any null-sum or linear constraint on
  the scalar Fourier coefficients $p^{r, r+1}_{i j; \pi}$.

### [FILL-PRIMITIVE-C7] Mathematical type

- **Type:** ANALYTIC connection-matrix data — Stokes / connection
  multipliers in BT-1933 form, expanded as Fourier series in the
  periodic strip variable.
- **Distinction:** (13 a) is **NOT** a parameter-chart translation
  identity; it is **NOT** an algebraic identity on equation-
  coefficient parameters; it is a function-space description of
  how proper matrix solutions in adjacent angular regions are
  related.

## §C.4 — Structural-form spec table (fill side)

Table format mirrors Phase B.3.

| Primitive             | Fill-side specification                                                                                                                  |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| [FILL-PRIMITIVE-C1]   | Domain = $(i, j, r) \in \{1,\ldots,n\}^{2} \times \{m,\ldots,\eta-1\}$ + continuous $x$ in strip; function-space object.                  |
| [FILL-PRIMITIVE-C2]   | Codomain = $\mathbb{C}$-valued holomorphic function of $x$ on strip $V_{r, r+1}$; periodic in $\Im x$.                                    |
| [FILL-PRIMITIVE-C3]   | Form = Fourier / q-series $\sum_{\pi} c_{\pi} e^{-\pi_{i j}(r,r+1)}$ in $z = e^{-x_{r}}$; **analytic** series, not closed-form algebraic. |
| [FILL-PRIMITIVE-C4]   | Cardinality = $n^{2} \times (\eta - m)$ scalar entry-functions; arity each: 1 complex variable $x$ in strip → $\mathbb{C}$.               |
| [FILL-PRIMITIVE-C5]   | Sector-dependent **by construction** — defined per adjacent-region pair $(r, r+1)$ separated by B'-curve $B^{r}$.                          |
| [FILL-PRIMITIVE-C6]   | Analytic constraints (convergent power series in $z$; non-vanishing leading coefficient); no algebraic linear constraint on parameters.   |
| [FILL-PRIMITIVE-C7]   | Type = analytic connection-matrix / Stokes-data (function-space object), **not** algebraic chart-translation.                              |

## §C.5 — Discipline reassertion

Phase C extracts the structural form of BT 1933 §5 (13 a) at the
substrate-inventory level. It does **not** assert that (13 a)
constitutes the chart-map needed by 069r1 §A.1.5; it does **not**
assert that R1 is closed; it does **not** assert M6.CC is upgraded.
Per envelope §6 the present file consumes only verbatim quotes from
073 `bt_1933_section_5_extract.md` SHA `ec2c0d5a..` and 073
`bt_1933_section_5_claim_table.md` SHA `00103c17..`. The 073
[CHART-MAP-CANDIDATE-B1] tag is a substrate-inventory observation;
its structural-form match status against 069r1 §A.1.5 is the subject
of Phase D matrix.

End of `bt_5_13a_structural_form.md`.
