# SPRINT-W1-NORMAL-FORM — Report

**Date:** 2026-04-27
**Result classification:** **PARTIAL** (the strategic conjecture is *refuted* in its strong form, but the underlying compatibility ideal is now characterised exactly).

---

## 1. Setup

We study degree-(2,1) PCF recurrences

$$ y_{n+1} \;-\; b_n\, y_n \;+\; a_n\, y_{n-1} \;=\; 0,
\qquad
b_n = b_1 n + b_0,
\qquad
a_n = a_2 n^2 + a_1 n + a_0 .$$

(Coefficients follow the project convention `[a2, a1, a0]`, `[b1, b0]` with leading first.)

Companion matrix form for $(y_{n+1}, y_n)^\top = M(n)(y_n, y_{n-1})^\top$:

$$ M(n) = \begin{pmatrix} b_n & -a_n \\ 1 & 0 \end{pmatrix},
\qquad \det M(n) = a_n,\quad \mathrm{tr}\,M(n) = b_n .$$

The Birkhoff ansatz at infinity is

$$ y_n \;\sim\; \Gamma(n+1)\,\mu^n\,n^\alpha, $$

with $\mu$ from the leading-$n$ balance and $\alpha$ from the next-to-leading ($n^0$) balance.

---

## 2. Characteristic equation

Substituting the ansatz, expanding $(1\pm 1/n)^\alpha$ to first order in $1/n$, multiplying by $n^2$, and reading off the $[n^3]$ coefficient gives

$$ \boxed{\; \mu^2 \;-\; b_1\,\mu \;+\; a_2 \;=\; 0 \;} $$

with characteristic roots $\mu_\pm = \tfrac{1}{2}\bigl(b_1 \pm \sqrt{b_1^2 - 4 a_2}\bigr)$ and Vieta relations $\mu_+ + \mu_- = b_1$, $\mu_+\mu_- = a_2$.

Reproducibility: `indicial_symbolic.py` (sympy 1.14.0).

---

## 3. Indicial equation

The $[n^2]$ balance, after substituting $\mu^2 = b_1\mu - a_2$, is linear in $\alpha$ and has closed-form solution

$$ \boxed{\;\alpha(\mu) \;=\; -\,\frac{(b_1-b_0)\,\mu \;+\; (a_1 - a_2)}{b_1\,\mu \;-\; 2 a_2}\;} $$

(verified by sympy; substituting back into the indicial relation yields 0). Each characteristic root $\mu_\pm$ produces one indicial exponent $\alpha_\pm := \alpha(\mu_\pm)$.

The sum and product of the two indicial exponents simplify, using Vieta, to rational functions of the coefficients:

$$ S \;=\; \alpha_+ + \alpha_- \;=\; \frac{a_1 - a_2}{a_2} \;=\; \frac{a_1}{a_2} - 1, $$

$$ P \;=\; \alpha_+ \alpha_- \;=\; \frac{a_1^2 - 2 a_1 a_2 - a_1 b_0 b_1 + a_1 b_1^2 + a_2^2 + a_2 b_0^2 - a_2 b_0 b_1}{a_2\,(4 a_2 - b_1^2)}. $$

---

## 4. Forcing the indicial pair $\{1/3, 2/3\}$

The pair $\{1/3, 2/3\}$ has $S = 1$, $P = 2/9$.

**$S = 1$** $\;\Longleftrightarrow\;$ $a_1 = 2 a_2$ (denote this **C1**).

Imposing C1 and simplifying:

$$ P\bigl|_{a_1 = 2 a_2} \;=\; \frac{a_2 + b_0^2 - 3 b_0 b_1 + 2 b_1^2}{4 a_2 - b_1^2}. $$

Setting this equal to $2/9$ and clearing denominators:

$$ 9\bigl(a_2 + b_0^2 - 3 b_0 b_1 + 2 b_1^2\bigr) \;=\; 2\bigl(4 a_2 - b_1^2\bigr)$$

which factors as

$$ \boxed{\; a_2 \;=\; -(3 b_0 - 5 b_1)(3 b_0 - 4 b_1) \;=\; -9 b_0^2 + 27 b_0 b_1 - 20 b_1^2 \;} \quad\text{(\textbf{C2})}. $$

Equivalently, with $r := b_0/b_1$,

$$ \frac{a_2}{b_1^2} \;=\; -9 r^2 + 27 r - 20 . $$

This is **a one-parameter algebraic family** in $r$, *not* the single value $-2/9$.

---

## 5. Does $\{1/3, 2/3\}$ force $a_2/b_1^2 = -2/9$?

**No.** Solving $-9 r^2 + 27 r - 20 = -2/9$:

$$ 81 r^2 - 243 r + 178 = 0 \;\Longrightarrow\; r = \frac{27 \pm \sqrt{17}}{18}
\;\approx\; 1.27094 \text{ or } 1.72906. $$

Both roots are irrational. Consequently:

- Over $\mathbb{Z}$, the loci $\{a_2/b_1^2 = -2/9\}$ (the empirical Trans fingerprint) and $\{$indicial pair $= \{1/3, 2/3\}\}$ (the compatibility ideal $C$) are **disjoint**.
- The integer-grid sweep ($|b_1| \le 30$, $|b_0| \le 30$, $|a_2| \le 200$, `compatibility.py`) returns **0 simultaneous solutions** out of $\sim 7.3{\times}10^5$ triples (610 satisfy E only, 205 satisfy C only).

This **refutes the strong form** of the strategic Week-1 hypothesis "indicial pair $\{1/3, 2/3\}$ forces $a_2/b_1^2 = -2/9$".

The emergent **partial-success** picture: the indicial framework yields an *exact* compatibility ideal $C$ for the pair $\{1/3, 2/3\}$, but $C$ is two-dimensional (after fixing scale) rather than a single ratio; the Trans-empirical ratio $-2/9$ is one specific irrational slice of the much richer locus.

---

## 6. Compatibility condition $C$

$$ \boxed{\;
C \;=\; \bigl(\, a_1 - 2 a_2,\;\;
a_2 + 9 b_0^2 - 27 b_0 b_1 + 20 b_1^2 \,\bigr)
\;\subset\; \mathbb{Q}[a_0, a_1, a_2, b_0, b_1]
\;}$$

Equivalently as a parametric variety:

$$ \mathcal{V}(C) \;=\; \Bigl\{\;
(a_0, a_1, a_2, b_0, b_1) \;:\; a_1 = 2 a_2,\;
a_2 = -9 b_0^2 + 27 b_0 b_1 - 20 b_1^2,\;
a_0 \text{ free}
\Bigr\}. $$

Note that $a_0$ does *not* appear at the leading two-term Birkhoff balance: it enters only at the $[n^{-1}]$ balance, at which higher-order $\alpha$-quadratic terms also contribute.  Determining whether $a_0$ is constrained at higher order is an open question for Week 2.

---

## 7. Numerical verification (Part C)

Five integer families were simulated at `mpmath.dps = 150` with $N = 600$ convergents; the indicial exponent was extracted by least-squares fitting of

$$ \log|P_n| \;-\; \log\Gamma(n+1) \;-\; n\,\log|\mu_\mathrm{dom}| \;\approx\; \alpha\,\log n + \mathrm{const} $$

over $n \in [200, 600]$.

| Label | $a_2/b_1^2$ | Predicted $\alpha_+,\alpha_-$ | Sum | Product | Fit (dom.) | Pred. dom. | Error |
|------|------:|------:|------:|------:|------:|------:|------:|
| **T1** $(a_2,a_1,a_0,b_0,b_1)=(-2,-4,0,0,3)$ | $-2/9$ | $-0.5914,\ 1.5914$ | $1$ | $-0.9412$ | $-0.5905$ | $-0.5914$ | $9.4\!\times\!10^{-4}$ |
| **T2** $(-2,0,0,1,3)$ | $-2/9$ | $-0.6213,\ -0.3787$ | $-1$ | $\;0.2353$ | $-0.6208$ | $-0.6213$ | $4.9\!\times\!10^{-4}$ |
| **NT1** $(2,4,0,0,3)$ | $+2/9$ | $-4,\ 5$ | $1$ | $-20$ | $-4.0902$ | $-4$ | $9.0\!\times\!10^{-2}$ |
| **NT2** $(4,0,0,0,2)$ | $1$ | complex pair | $-1$ | $1/3$ | $-0.821$ | (complex) | — |
| **LOG1** $(-1,-2,0,0,6)$ | $-1/36$ | $-0.9230,\ 1.9230$ | $1$ | $-1.775$ | $-0.9227$ | $-0.9230$ | $3.0\!\times\!10^{-4}$ |

**Key takeaways.**

1. The symbolic Birkhoff prediction for $\alpha$ is verified numerically to roughly $10^{-3}$ on every family with real $\mu$ (NT1's larger residual is consistent with finite-$n$ corrections at $\alpha = -4$, where the next-order term carries more weight; the slope is *signed* correctly).
2. **The Trans-style families T1 and T2, both having $a_2/b_1^2 = -2/9$, do *not* exhibit indicial exponents $\{1/3, 2/3\}$.** T1's predicted/measured pair is $\{-0.591, 1.591\}$; T2's is $\{-0.621, -0.379\}$.
3. The phantom-hit rule (PSLQ relations with vanishing L-coefficient rejected) does not directly apply here — Part C uses direct numerical least-squares fitting, not PSLQ — but is recorded in `claims.jsonl` as observed.

---

## 8. Conclusion

**Headline finding:** The strategic Week-1 conjecture *"indicial pair $\{1/3, 2/3\}$ forces $a_2/b_1^2 = -2/9$"* is **false in its strong form**. The indicial pair forces a *quadratic locus* $\mathcal{V}(C)$ in $(b_0/b_1, a_2/b_1^2)$ space; the empirical Trans value $-2/9$ corresponds only to two irrational $b_0/b_1$ ratios, $r = (27 \pm \sqrt{17})/18$, neither of which is realisable over $\mathbb{Z}$.

**Reinterpretation of the empirical data.** Either
- (a) the 585k empirical "Trans" PCFs with $a_2/b_1^2 = -2/9$ do *not* in fact have indicial pair $\{1/3, 2/3\}$ — their convergence mechanism is something else; or
- (b) the indicial structure of these PCFs is observed only *approximately* (e.g., via near-integer slopes in numerical fits), and the exact algebraic constraint comes from a higher-order or different invariant.

The Week-1 deliverables (this report, `compatibility.py`, `numerical_verify.py`) make these two alternatives experimentally distinguishable: re-running the indicial-fitter on a sample of the empirical 585k families will resolve which is the case.

**Recommended Week-2 work.**
1. Apply `numerical_verify.py` to a sample of $\sim 100$ actual T2B Trans PCFs (when the dataset is connected) and record their fitted indicial exponents.
2. If exponents *are* $\{1/3, 2/3\}$ within numerical precision, derive the next-order ($[n^{-1}]$) balance and check whether it adds the missing constraint that selects $r = (27 \pm \sqrt{17})/18$ with corrections.
3. If exponents are *not* $\{1/3, 2/3\}$, search for the actual rational invariant (sum $\bullet$ product $\bullet$ resultant) that is preserved across the Trans family.
4. Investigate whether the $-2/9$ ratio arises instead from a Galois-theoretic / monodromy condition on the companion $M(n)$ rather than from Birkhoff exponents.

---

## 9. Files

| File | Description |
|-|-|
| `indicial_symbolic.py` | Parts A, B (sympy derivation) |
| `numerical_verify.py` | Part C (mpmath dps=150 fitting on 5 families) |
| `compatibility.py` | Part D (write $C$, integer-grid sweep) |
| `_indicial_symbolic.log` | Output of Part A/B |
| `_numerical_verify.log` | Output of Part C |
| `_compatibility.log` | Output of Part D |
| `compatibility_summary.json` | Machine-readable Part D result |
| `claims.jsonl` | AEAL claims (10 entries) |
| `halt_log.json`, `discrepancy_log.json`, `unexpected_finds.json` | All `{}` (no halt) |
| `sprint_w1_report.md` | This document |
| `handoff.md` | One-page summary for Claude review |
