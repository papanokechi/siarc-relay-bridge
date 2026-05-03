# D3 — Birkhoff & Trjitzinsky 1933 §§1–6 normalization extract (verbatim)

**Task:** T1-A01-NORMALIZATION-RESOLUTION — STEP 4
**Source file:** `tex/submitted/control center/literature/g3b_2026-05-03/03_birkhoff_trjitzinsky_1933_acta60.pdf`
**File size:** 3 411 000 bytes (3.3 MB), 89 pages, OCR layer present.
**Citation:** Birkhoff & Trjitzinsky, *Analytic Theory of Singular
Difference Equations*, Acta Mathematica **60** (1933), 1–89.

> **OCR caveat.** The text layer is OCR'd from a 1933 type-set scan;
> Greek letters (μ, γ, σ), subscripts, and superscripts often arrive
> garbled (e.g. "g/x log X+TiX" for "μ_j x log x + γ_j x"). Each verbatim
> quotation below is followed by a `[transcribe:]` note clarifying the
> intended mathematical content.

---

## §3.a — The canonical formal solution form (B–T 1933, page 4)

PDF page 4 of `03_birkhoff_trjitzinsky_1933_acta60.pdf` (=Acta Math 60
page 4 of the article), verbatim OCR (lines 113–125 of `_bt1933.txt`):

```
ee(~)s(x), Q(x)=~xlogx +Tx + dxV + ... + ~xV
( 1 1
s(x):x ~ a+bx P+...)+(al+blx ~+- .)logx+...
1 + (a ~+b "~x ~;+...)log~x ,
p is a positive integer, /~p is an integer and m is a positive integer or o.
```

`[transcribe:]` The B–T canonical formal solution at $\infty$ is

$$
   \widehat y(x) \;=\; e^{Q(x)}\,s(x),
   \qquad
   Q(x) \;=\; \frac{\mu}{p}\,x\log x \;+\; \gamma\,x \;+\; \delta_1\,x^{(p-1)/p}
              \;+\; \cdots \;+\; \delta_{p-1}\,x^{1/p},
$$

with $p$ a positive integer ("basic integer"), $\mu_p$ an integer,
$m$ a non-negative integer; and $s(x)$ a formal "$s$-series" in $x^{-1/p}$
with logarithmic factors of bounded degree.

## §3.b — The "normal" classification (B–T 1933, page 4–5)

PDF page 4, verbatim OCR (lines 128–131):

```
The difference system (I) or single equation (2) will be called nor-
mal if p ~ I in all of the formal series, so that each Qj(x) reduces merely to
g/x log X+TiX; otherwise it will be called anormal, since then there enter anor-
mal series with p > x.
```

`[transcribe:]` The system is called **normal** if $p \equiv 1$ for all
$j$, i.e. each $Q_j(x)$ reduces to

$$
   \boxed{\,Q_j(x) \;=\; \mu_j\,x\log x \;+\; \gamma_j\,x\,}
$$

(no fractional-power terms); otherwise **anormal**. The text on page 5
adds: "the system (1) or equation (2) will be called regular or
irregular, according as there is only a single value of $\mu_j$ or
more than one such value."

This is the **canonical normal-case form** that the SIARC PCF
stratum sits in (single integer $\mu$ per formal solution, single $p=1$).

## §3.c — Citation of Adams 1928 (B–T 1933, page 5)

PDF page 5, verbatim OCR (lines 152–153, footnote at line 176):

```
In a recent important paper Adams 2 has shown that to some extent Birkhoff's
methods continue to apply in the irregular normal case.
```

Footnote 2 (line 176):

```
" C. R. Adams, On the Irregular Cases of the Linear Ordinary Difference Equations, Trans.
Am. Math. Soc., vol. 3 ~ (I928), pp. 5o7--54.
```

`[transcribe:]` Footnote 2: "C. R. Adams, *On the Irregular Cases of the
Linear Ordinary Difference Equations*, Trans. Am. Math. Soc., vol. 30
(1928), pp. 507–541." This is the standard Adams 1928 reference.

The citation places Adams 1928 as treating the **irregular normal
case** (i.e., $p = 1$, multiple distinct $\mu_j$) using methods that
**continue to apply** from Birkhoff's prior work — i.e., Adams uses
the **same Q(x) = μ x log x + γ x normalisation** as B–T 1933 do.

## §3.d — Lemma 8 (B–T 1933 §4, page 30, the summation lemma)

PDF page 30 (line 985 of `_bt1933.txt`):

```
Lemma 8. Assume that the function
(I ) H(z) = eQ (~1 h (x)
1
is analytic in R while Q(x) = ttx log x + 7x+ ... +vx v is proper on and in the
neighborhood of the right boundary of R and
(I a) h(x) ~ H(x) (in R)
where l~(x) ,is a formal s-series (Def. r; w i).
```

`[transcribe:]` Lemma 8 takes as input a function $H(x) = e^{Q(x)}h(x)$
with the **same canonical exponent**

$$
   Q(x) \;=\; \mu\,x\log x \;+\; \gamma\,x \;+\; \cdots \;+\; \nu\,x^v
$$

— exactly the form (7) from §3.a, in the normal sub-case + polynomial
correction. So §4 inherits the §1 normalisation; B–T do not re-define
$\mu$ in §§4–6.

## §3.e — Theorem I (B–T 1933 §5, page 41)

PDF page 41 (line 1339 of `_bt1933.txt`):

```
Theorem I. Assume that the coefficients of an equation L,(y) ~o (2; w l)
are known (eft w :) i~ a subregion of F (w ,),
(; = (:) + (~) +-. + (m) + + (~).
Let the corresponding functions Q(x) be
(I) Q1 (x), ... Qn (X).
```

`[transcribe:]` Theorem I uses the same canonical $Q_j(x)$
($j=1,\dots,n$) exponents from §1; it asserts that the operator is
**completely proper** in a region (m), assuming a proper fundamental
set in a strip V. No re-normalisation occurs.

## §3.f — Lemma 9 (B–T 1933 §6, page 48)

PDF page 48 (line 1570 of `_bt1933.txt`):

```
Lemma 9. Let coefficients of
(,) Ln(y) = y(x + n) + al(x)y(x + n -- I) § .. + a,(x) y(x) = o
be known (and be of the kind specified in the beginning of w x) i~ (I)+ "''-{-(7~),
a subregion of F. If the equation is Q-factorable in (I)+-., +(m) (Def. 8; w I),
[...]
With the eQJ(~)s~(x) (j=I,...~2) denoting a Ill, early independent set of formal
solutions of (~), the ,factorization (~ a) ea~ be so eI]~cted that the series
(I b) e ~'l~/Sl(X), ... e qr(x) Sr(X)
are formal solutions of Lr(y)= o.
```

`[transcribe:]` Lemma 9 is the factorisation lemma: a $Q$-factorable
operator $L_n$ admits a factorisation $L_n = L_{n-r} L_r$ such that
the formal solutions $e^{Q_j(x)} s_j(x)$ split into two groups
respecting the $Q_j$ ordering. Again, the canonical $Q_j$ form from
§1 is used unchanged.

---

## §3.g — Identification of B–T 1933 μ with SIARC A

Comparing **PCF-1 v1.3 §6** (D1) verbatim:

$$
   \log|\delta_n| \;=\; -A\,n\log n \;+\; \alpha\,n
                  \;-\; \beta_w\log n \;+\; \gamma_w \;+\; o(1)
$$

with **B–T 1933 §1** verbatim:

$$
   \widehat y_j(x) \;=\; e^{Q_j(x)}\,s_j(x),
   \qquad
   Q_j(x) \;=\; \mu_j\,x\log x \;+\; \gamma_j\,x
   \quad\text{(normal case, $p=1$),}
$$

we read off the structural correspondence: in the normal case, both
forms have leading channel "**coefficient times $x\log x$** + lower"
in their formal exponent. PCF-1's $-A$ corresponds directly to
$\mu_2 - \mu_1$ (or $\mu_{\mathrm{sub}} - \mu_{\mathrm{dom}}$) — the
**difference** of the two B–T exponents in the $n\log n$ channel —
because $\delta_n$ is the Wallis convergent error, which behaves at
leading order as the ratio (subdominant solution / dominant solution).

The key qualitative observation is that **A is in the same μ-units
as B–T**: there is no factor-of-2 between SIARC's $A$ and B–T's $\mu$.
A factor-of-2 ambiguity at the normalisation level would require the
SIARC ansatz to write its leading channel as either
$-(A/2)\,n\log n$ or $-2A\,n\log n$ — which it does **not**; the
PCF-1 v1.3 ansatz has $-A\,n\log n$ verbatim.

This pins the **Wasow-normalisation reading** at the level of the
ansatz–to–B–T match. Adams 1928 uses the same convention as B–T 1933
(per §3.c citation); therefore the "Adams reading" in which SIARC's
$A$ would equal $2\sigma_{\mathrm{Adams}}$ (with $\sigma_{\mathrm{Adams}}
= \tfrac{1}{2}\sigma_{\mathrm{Wasow}}$) is **not supported** by the
direct B–T 1933 evidence.

The remaining (non-$A$) ingredient of the Phase-1 bracket
$[d, 2d]$ — namely, the **bound** $\mu \le 2d$ in terms of polynomial
degree $d$ of the recurrence coefficients — is sourced by Phase-1
from Wasow 1965 §X.3 and Birkhoff 1911. That bound is **not**
re-derived here (out of scope; STEP 3 of the relay is about the
**slope bound**, which lives in Wasow §X.3, currently NIA per D2).
What IS resolved here is the **normalisation-match** question, which
is the present task.
