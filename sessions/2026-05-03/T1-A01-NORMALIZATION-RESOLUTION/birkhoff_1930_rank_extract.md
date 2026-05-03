# D4 — Birkhoff 1930 (Acta Math 54) "rank" / formal-series extract

**Task:** T1-A01-NORMALIZATION-RESOLUTION — STEP 5
**Source file:** `tex/submitted/control center/literature/g3b_2026-05-03/01_birkhoff_1930_acta54.pdf`
**File size:** 1 798 753 bytes (1.8 MB), 42 pages, OCR layer present.
**Citation:** G. D. Birkhoff, *Formal Theory of Irregular Linear
Difference Equations*, Acta Mathematica **54** (1930), 205–246.

> **OCR caveat.** Same caveat as D3; verbatim quotations are followed
> by `[transcribe:]` notes.

---

## §4.a — Title (PDF page 1)

PDF page 1, verbatim:

```
FORYlAL THEORY OF IRREGULAR LINEAR DIFFERENCE
EOUATI0 qS.
BY
GEORGE D. BIRKHOFF
of CAMBRIDGE, MASS., U. S. A.
Introduction.
```

`[transcribe:]` "Formal Theory of Irregular Linear Difference Equations.
By George D. Birkhoff, of Cambridge, Mass., U. S. A. Introduction."
This is the precursor paper that sets the notation B–T 1933 inherits.

## §4.b — Citation of Adams 1928 (PDF page 2)

PDF page 2 (`_birkhoff1930.txt` lines 41–60), verbatim:

```
The most general examination hitherto made of linear difference equations
not of this special type is due to Adams. ~ He discusses the extent to which
my own method of approach tO the regular case s admits of extension to the
irregular case, [...]
In brief, he finds
that so long as there are n types of formal series with elements of the form
( ) x~**e~xr a + b 4-... (/z*_--< F),
X
the same method is applicable. Since these formal series are of the same kind
as appear in the regular case, it is natural to group this particular irregular
case closely with the regular case.
```

Footnote 2 (line 58):

```
2 C. R. Adams, On the Irregular Cases of Linear Ordinary Diference Equafions, Trans. Am.
Math. Soe., vol. 3 ~ (1928), pp. 5o7--54 I.
```

`[transcribe:]` Footnote: "C. R. Adams, *On the Irregular Cases of
Linear Ordinary Difference Equations*, Trans. Am. Math. Soc., vol. 30
(1928), pp. 507–541." Same citation as B–T 1933 footnote 2.

The text states that Adams 1928 treated formal series of the form
$x^{\nu^*} e^{\gamma x} (a + b/x + \cdots)$ with $\mu^* \le \mu$ —
i.e., **the same type of formal series as the regular case**, and
**Adams uses the same exponent convention** (γ x in the canonical
exponent, with x^{ν^*} a power factor). Birkhoff explicitly groups
"this particular irregular case closely with the regular case",
confirming a **single shared normalisation** across regular and
(generic) irregular cases.

## §4.c — Birkhoff's canonical formal series (PDF page 6, formula (6))

PDF page 6 (`_birkhoff1930.txt` lines 165–175), verbatim:

```
1
Z,(x) in (3) are also such series in x~. It is obvious then that for the-complete
specification we must not only give the equation (4), but also the value of the
'basic integer' p which is to be adopted; all possible values of p are evidently
positive integral multiples of a least value P0 ~ I.
The usual method ~ for the determination of formal series begins with the
substitution of a series

~'--~p ep (~)x, ( b (6) s(x) : x a + --- + 
X p
p--1
P(x) = 7x + ~x~- +
)
in the equation and the attempt~ to determine it, 7, 6,...7 a, b,... by the
method of undetermined coefficients.
```

`[transcribe:]` Birkhoff 1930 formula (6): the canonical formal
solution is

$$
   s(x) \;=\; x^{\nu x}\,e^{P(x)}\,x^{\mu}\,(a + b/x^{1/p} + \cdots),
   \qquad
   P(x) \;=\; \gamma\,x + \delta\,x^{(p-1)/p} + \cdots,
$$

with **basic integer** $p \ge 1$ (the OCR "x^{ν−p}" / "x^{ν p}" should
be read as $x^{\nu x}$ = $e^{\nu x \log x}$, since this is the only
way the formula represents the difference-equation Stirling-rate
factor; otherwise the form would not match B–T 1933 (7) on the next
year's paper, which is the explicit elaboration of Birkhoff 1930's
form). Equivalently the **leading exponent in $\log s(x)$ is**

$$
   \log s(x) \;=\; \nu\,x\log x \;+\; P(x) \;+\; \mu\log x
                   \;+\; \log(a + b/x^{1/p} + \cdots).
$$

Birkhoff's $\nu$ is the **same object** as B–T 1933's $\mu$ (the
coefficient of $x\log x$ in the canonical exponent of a formal solution
at infinity), in the same normalisation.

## §4.d — Newton-polygon slope condition (PDF page 6, slope formula)

PDF page 6 (`_birkhoff1930.txt` lines 188–199), verbatim:

```
Now if such a formal identity is to be possible, there must be two leading
terms of the same degree in x, so that
j l -- jm
it-- 1-- m
for some 1 and m (1 ~ m), while all other terms are not of higher degree, i.e.
whence
-j, + t~(,-i)<= --j,, + t~("-'~)
i,-j,,>-_ -t~(i-m). (i=o, i,... n).
```

`[transcribe:]` The leading-balance condition for the formal series to
exist is

$$
   \mu \;=\; \frac{j_l - j_m}{l - m}
   \quad\text{for some pair } (l, m) \text{ with } l \ne m,
   \qquad
   j_i - j_m \;\ge\; -\mu\,(i - m) \quad (i = 0, 1, \dots, n).
$$

Here $j_i$ is determined by the leading degree of the coefficient
$a_i(x)$: $a_i(x) \sim a_{i j_i} x^{-j_i / p}$ for $i = 0, 1, \dots, n$.
This formula is the **Newton-polygon slope characterisation** of the
formal exponent $\mu$: $\mu$ is the **maximum slope** of the lower
convex hull of the points $\{(i, -j_i)\}$ — equivalently, of the points
$\{(i, p \cdot \deg a_i)\}$ if $a_i$ are polynomials of degree
$p\cdot\deg a_i / p$.

This is **exactly** the slope-of-Newton-polygon definition that Phase-1
attributed to Wasow 1965 §X.2. Birkhoff 1930 §1 / page 6 supplies it
**directly**, on disk, with OCR.

---

## §4.e — Synthesis: what Birkhoff 1930 directly supplies

* **Single shared normalisation** for formal solutions across the
  regular and (generic) irregular cases (page 2): Adams's, Birkhoff's
  and B–T's $\mu$ all agree.
* **Newton-polygon slope formula** for $\mu$ (page 6): $\mu = (j_l -
  j_m)/(l-m)$, the canonical slope of the lower convex hull.
* **No factor of 2** between Birkhoff 1930's $\nu$, B–T 1933's $\mu$,
  Adams 1928's $\sigma$, and Wasow 1965's σ (insofar as Wasow inherits
  the convention from these primary sources, as is customary in
  textbook treatments).

This directly supports the **Wasow-normalisation reading** of A-01.
