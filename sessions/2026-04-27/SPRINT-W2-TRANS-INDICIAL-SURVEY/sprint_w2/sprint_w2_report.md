# SPRINT-W2-TRANS-INDICIAL-SURVEY — Report

**Date:** 2026-04-27
**Result classification:** **NEGATIVE** (no new indicial invariant found) **with one positive corollary** (an iff theorem connecting `a₂/b₁² = −2/9` to a characteristic-root-ratio identity, confirmed by PSLQ).

---

## 1. Week-1 recap

W1 derived the closed-form indicial exponent
$$\alpha(\mu) = -\frac{(b_1 - b_0)\,\mu + (a_1 - a_2)}{b_1\,\mu - 2 a_2},
\qquad \mu^2 = b_1\mu - a_2,$$
and proved that the indicial pair $\{1/3, 2/3\}$ does **not** force $a_2/b_1^2 = -2/9$: the latter corresponds to irrational $b_0/b_1 = (27 \pm \sqrt{17})/18$ which no integer family realises.

W1 left open the question: *what is the actual indicial structure of integer Trans families, and what universal invariant identifies them?*

---

## 2. Indicial survey (50 Trans families)

Generated 50 integer Trans families with $a_2/b_1^2 = -2/9$ (i.e. $b_1 \in \{3,6,9,12,15\}$ and $a_2 = -2b_1^2/9 \in \{-2,-8,-18,-32,-50\}$), varying $b_0$, $a_1$, $a_0$ over small integers. For each family computed (script `indicial_survey.py`):

- characteristic roots $\mu_\pm$, modulus ratio $|\mu_+/\mu_-|$;
- indicial exponents $\alpha(\mu_\pm)$ via the W1 closed form;
- indicial sum $S$, product $P$, discriminant $D = (\alpha_+ - \alpha_-)^2$;
- numerical $\alpha_{\mathrm{fit}}$ from least-squares on 500 convergents at `mpmath.dps = 150`.

**Key finding** (Part A3):

| quantity | range across 50 Trans families | constant? |
|---|---|---|
| $\lvert\mu_+/\mu_-\rvert$ | exactly $6.34232921921324541236605739198\ldots$ | **YES** |
| sum $S$ | $\{-3,\ -1,\ +1\}$ | NO (3 values) |
| product $P$ | 9 distinct values in $[-2.235,\ +2.235]$ | NO |
| discriminant $D$ | 8 distinct values in $[0.059,\ 9.94]$ | NO |
| numeric $\alpha_{\mathrm{fit}}$ | varies | matches symbolic dominant root |

The numeric fits agree with the symbolic prediction to ~$10^{-3}$ on every family.

---

## 3. Separation test (Trans vs Log vs Alg)

Ran the same survey on 10 Log-style families (e.g. $a_2/b_1^2 \in \{-1/4,-1/9,+1/9,-1/16,-2/25\}$) and 10 Alg-style families (degenerate or complex characteristic). Script `separation_test.py`:

| class | $\lvert\mu_+/\mu_-\rvert$ | sum range | product range |
|---|---|---|---|
| **Trans** | $\{6.342\}$ (one value) | $\{-3,-1,1\}$ | 9 values |
| Log | $\{5.83, 6.85, 10.91, 14.43, 17.94\}$ | $\{-3,-2,-1,2\}$ | 6 values |
| Alg | $\{1\}$ (degenerate / complex) | $\{-1, -0.556, -0.5\}$ | 4 values |

`|μ+/μ-|` separates the three classes by definition (it is a function of $a_2/b_1^2$ alone, by Vieta). The other indicial features overlap freely between classes.

---

## 4. The "true invariant" found is tautological

The only quantity constant across the 50 Trans families — `|μ+/μ-| = (13 + 3√17)/4` — is **algebraically equivalent** to the Trans definition itself:

$$\boxed{\quad \lvert\mu_+/\mu_-\rvert \;=\; \tfrac{13 + 3\sqrt{17}}{4}
\;\Longleftrightarrow\;
a_2/b_1^2 \;=\; -\tfrac{2}{9}\;\;\text{(with } a_2<0\text{)}.\quad}$$

**Verification by PSLQ at dps=150** (script `forcing_condition.py`):

- Basis $\{1,\ \sqrt{17},\ \rho\}$ where $\rho := |\mu_+/\mu_-|$: PSLQ returns $[13, 3, -4]$, i.e. $13 + 3\sqrt{17} - 4\rho = 0$, with $L$-coefficient $= -4 \neq 0$ (Phantom Hit Rule passes). Reconstruction error $= 0$ (zero at >100 digits).
- Wider basis $\{1, \sqrt{2}, \sqrt{3}, \sqrt{5}, \sqrt{17}, \pi, \log 2, \rho\}$: PSLQ returns $[-13, 0, 0, 0, -3, 0, 0, 4]$ — same identity, $L$-coeff $= 4 \neq 0$.

**Symbolic verification (Part D2):** From Vieta $\mu_+\mu_- = a_2$, $\mu_+ + \mu_- = b_1$, hence $a_2/b_1^2 = q/(1+q)^2$ with $q := \mu_+/\mu_-$. Setting $q = -(13+3\sqrt{17})/4$ and `sympy.simplify` gives exactly $-2/9$.

The other branch $q = +(13+3\sqrt{17})/4$ (same modulus, opposite sign) gives $a_2/b_1^2 = +2/17$, so the converse needs the sign condition $a_2 < 0$.

---

## 5. Revised theorem statement (Form 4)

> **Theorem (W2).** Let $b_1 \neq 0$ in $\mathbb{Q}$. For a degree-(2,1) PCF
> $y_{n+1} = (b_1 n + b_0)\,y_n - (a_2 n^2 + a_1 n + a_0)\,y_{n-1}$,
> with $a_2 < 0$, the following are equivalent:
>
> 1. $a_2 / b_1^2 \;=\; -\dfrac{2}{9}$.
>
> 2. $\bigl\lvert \mu_+/\mu_- \bigr\rvert \;=\; \dfrac{13 + 3\sqrt{17}}{4}$, where $\mu_\pm$ are the roots of $\mu^2 - b_1\mu + a_2 = 0$.

This is **not** an indicial-exponent theorem. The indicial exponents themselves (sum, product, discriminant, individual values) all vary as $a_1$, $b_0$, $a_0$ vary on the Trans locus.

The theorem says only that the *characteristic-root modulus ratio* is a specific quadratic irrational on the Trans locus — equivalent to the original definition by Vieta.

---

## 6. Conclusions and Week-3 recommendation

**Headline.** The leading-order Birkhoff/indicial framework provides **no new structural invariant** that explains why $a_2/b_1^2 = -2/9$ produces transcendental CF limits. The "invariant" found ($|\mu_+/\mu_-|$) is just a recasting of the Trans definition.

**Why this is informative.** The Trans property cannot be characterised by anything visible at the leading two-term Birkhoff balance. Whatever distinguishes Trans CFs from Log/Alg CFs lives in:

- (a) **Higher-order Birkhoff coefficients.** $a_0$ enters only at $[n^{-1}]$ and could supply the missing constraint. The $\alpha(\alpha-1)$ contribution at that order is non-linear and might select a discrete sub-locus of $a_2/b_1^2 = -2/9$.
- (b) **Padé / convergence-rate exponent.** The rate $|y_n/x_n - L| = O(\rho^{-n})$ with $\rho = |\mu_+/\mu_-|$ is *the same* on the entire Trans locus, but the *coefficient* and *correction* may carry the arithmetic content.
- (c) **Galois resolvent of the companion matrix.** $M(n) = \begin{pmatrix} b_n & -a_n \\ 1 & 0\end{pmatrix}$ has discriminant $b_n^2 - 4 a_n$ which is $O(n^2)$ on the Trans locus; its rationality / integrality structure (Galois group of the splitting field per $n$) might separate Trans from Log.
- (d) **Stokes data / connection coefficients.** The continuous-$q$ analogue would give a one-parameter monodromy invariant; the irrational corner $b_0/b_1 = (27\pm\sqrt{17})/18$ found in W1 strongly suggests this is the right framework.

**Recommended Week-3 prompt:** Compute the $[n^{-1}]$ Birkhoff balance at $a_2 = -2b_1^2/9$ symbolically (now non-linear in $\alpha$, but tractable since $\alpha$ is already known in closed form from W1). Test whether the resulting equation has rational solutions for $\alpha$ (giving the "true" indicial pair) only at specific values of $a_0$ and $a_1/b_1$. If yes, that is the missing constraint. If not, pivot to Padé-rate analysis.

---

## 7. Files

| file | role |
|---|---|
| `indicial_survey.py` | Part A — enumerate 50 Trans + 20 non-Trans, compute all indicial features |
| `separation_test.py` | Part B — class-distribution comparison |
| `forcing_condition.py` | Parts C, D — symbolic $S, P, D$ on the Trans locus, PSLQ confirmation |
| `_indicial_survey.log` | log of Part A output |
| `_separation_test.log` | log of Part B output |
| `_forcing_condition.log` | log of Parts C, D output |
| `indicial_survey.json` | machine-readable per-family data |
| `claims.jsonl` | 6 AEAL entries |
| `halt_log.json`, `discrepancy_log.json`, `unexpected_finds.json` | all `{}` |
| `sprint_w2_report.md` | this document |
