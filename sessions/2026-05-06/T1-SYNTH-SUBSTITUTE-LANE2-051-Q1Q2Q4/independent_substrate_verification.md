# Independent substrate verification — V1-V6

**Independence floor:** This document was authored BEFORE reading the body of
`synth_substitute_verdict.md` (only filename + bridge anchor consulted). All
findings below are derived from primary substrate (source files / first
principles) without anchoring to the synth-substitute conclusions.

**Method:** Direct file inspection (V1-V5) + first-principles derivation (V6).

---

## V1 — `cf_value()` recurrence in `session_c1_wkb.py`

**Source:** `pcf-research/pcf2/session_C1_2026-05-01/session_c1_wkb.py` L78-86.

**Verbatim code block:**

```python
def cf_value(coeffs, N: int, dps: int) -> mp.mpf:
    a3, a2, a1, a0 = coeffs
    with mp.workdps(dps):
        x = mp.mpf(a3) * N ** 3 + mp.mpf(a2) * N ** 2 + mp.mpf(a1) * N + mp.mpf(a0)
        for k in range(N - 1, -1, -1):
            bk = mp.mpf(a3) * k ** 3 + mp.mpf(a2) * k ** 2 + mp.mpf(a1) * k + mp.mpf(a0)
            x = bk + mp.mpf(1) / x
        return +x
```

**Reading:**

- The recurrence on line 84 is `x = bk + mp.mpf(1) / x`, i.e.,
  $x_k = b_k + 1 / x_{k+1}$.
- This is the canonical (1, b) CF: $K(1, b_n) = b_0 + \cfrac{1}{b_1 + \cfrac{1}{b_2 + \cdots}}$.
- The variable names `a3, a2, a1, a0` (line 80) are MISLEADING; they unpack
  the polynomial coefficients of $b_n$ (degree-3 in $k$), not an "$a_n$"
  sequence. The numerator $a_n$ is HARDCODED to $\equiv 1$ via `mp.mpf(1)`
  on line 84.

**Independent finding (V1):**

`cf_value()` in `session_c1_wkb.py` L78-86 implements the canonical (1, b)
continued fraction with $a_n \equiv 1$. **Therefore deg_a = 0 in the
implementation.** The script does NOT sweep over a non-trivial $a_n$;
it cannot, by construction.

---

## V2 — Same inspection for `session_b_pslq.py` and `quartic_tail_fit_all60.py`

### V2.a — `pcf-research/pcf2/session_B_2026-05-01/session_b_pslq.py` L162-170

```python
def cf_value(coeffs, N: int, dps: int) -> mp.mpf:
    a3, a2, a1, a0 = coeffs
    with mp.workdps(dps):
        x = mp.mpf(a3) * N ** 3 + mp.mpf(a2) * N ** 2 + mp.mpf(a1) * N + mp.mpf(a0)
        for k in range(N - 1, -1, -1):
            bk = mp.mpf(a3) * k ** 3 + mp.mpf(a2) * k ** 2 + mp.mpf(a1) * k + mp.mpf(a0)
            x = bk + mp.mpf(1) / x
        return +x
```

Identical to V1: $a_n \equiv 1$, deg_a = 0.

### V2.b — `pcf-research/pcf2/session_R1_2_2026-05-01/quartic_tail_fit_all60.py` L21-30

```python
def cf_value(coeffs, N, dps):
    a4, a3, a2, a1, a0 = coeffs
    with mp.workdps(dps):
        a4m = mp.mpf(a4); a3m = mp.mpf(a3); a2m = mp.mpf(a2)
        a1m = mp.mpf(a1); a0m = mp.mpf(a0)
        x = a4m * N**4 + a3m * N**3 + a2m * N**2 + a1m * N + a0m
        for k in range(N - 1, -1, -1):
            bk = a4m * k**4 + a3m * k**3 + a2m * k**2 + a1m * k + a0m
            x = bk + mp.mpf(1) / x
        return +x
```

Same `x = bk + mp.mpf(1) / x` recurrence on line 28. The `coeffs` tuple
holds the QUARTIC $b_n$ coefficients (not an "a"-sequence), and $a_n \equiv 1$
is hardcoded. deg_a = 0.

**Independent finding (V2):** All three pcf-research/pcf2 scripts — `session_c1_wkb.py`,
`session_b_pslq.py`, `quartic_tail_fit_all60.py` — use the SAME (1, b) CF
convention with $a_n \equiv 1$ (deg_a = 0). The convention is uniform
across the cubic-CM (Session B), cubic-non-CM (Session C1), and quartic
(Session R1.2 / Q1) pipelines.

---

## V3 — PCF-2 program statement L228-235 declared scope

**Source:** `tex/submitted/pcf2_program_statement.tex` L223-238.

**Verbatim declaration (L228-234):**

```latex
We work with PCFs of the form
\begin{equation}\label{eq:pcfd3}
K(a_{n},b_{n})=b_{0}+\cfrac{a_{1}}{b_{1}+\cfrac{a_{2}}{b_{2}+\cdots}}
\end{equation}
with
\begin{align}
a_{n} &= \delta_{1}\,n + \delta_{0},\qquad \delta_{1},\delta_{0}\in\Z, \label{eq:an}\\
b_{n} &= \alpha_{3}\,n^{3} + \alpha_{2}\,n^{2} + \alpha_{1}\,n + \alpha_{0},\qquad \alpha_{i}\in\Z,\ \alpha_{3}\ne 0. \label{eq:bn}
\end{align}
```

**Recurrence:** L235-236 — `p_{n}=b_{n}p_{n-1}+a_{n}p_{n-2}` (Wallis form).

**Reading:**

- Declared $a_n$: $\delta_1 n + \delta_0$ with $\delta_1, \delta_0 \in \mathbb{Z}$.
  **NO restriction $\delta_1 \ne 0$ is imposed.** This is the d=3 PCF-2 spec.
- Declared $b_n$: cubic in $n$ with $\alpha_3 \ne 0$.
- Declared deg_a: up to 1 (i.e., $\delta_1$ may or may not be zero).

**Independent finding (V3):**

The PCF-2 v1.3 program statement at L228-234 declares $a_n = \delta_1 n + \delta_0$
without imposing $\delta_1 \ne 0$. Therefore, formally, deg_a $\in \{0, 1\}$
under the PCF-2 declared scope (with $\delta_1 = 0, \delta_0 = 1$ recovering
the $a_n \equiv 1$ corner case used by V1/V2 implementations).

**However**, the PROSE on L228 ("$a_n = \delta_1 n + \delta_0$") signals a
LINEAR functional form, and the natural reading is "deg_a = 1" with
$\delta_1$ FREE to vary. The implementations in V1/V2 do not sweep over
non-zero $\delta_1$; they fix $a_n \equiv 1$ (i.e., $\delta_1 = 0,
\delta_0 = 1$) for all numerics. **Implementation $\subset$ Declared scope
strictly: the deg_a = 0 corner is the ONLY sub-stratum tested empirically.**

---

## V4 — PCF-1 v1.3 d=2 standard stratum

**Source:** `tex/submitted/p12_journal_main.tex` L124-138.

**Verbatim declaration (L124-131):**

```latex
We work throughout with the \emph{degree-two class}
$d=2$ in the standard Spec$(K)$ convention~\cite{Papanokechi2026Spec},
namely
\begin{equation}\label{eq:d2-class}
a_{n} \;=\; \delta\,n + \varepsilon, \qquad
b_{n} \;=\; \alpha\,n^{2} + \beta\,n + \gamma,
\end{equation}
with $\alpha,\beta,\gamma,\delta,\varepsilon\in\mathbb{Z}$ and
$\alpha,\delta\neq 0$.
```

**Recurrence:** L132 — $p_n = b_n p_{n-1} + a_n p_{n-2}$ (Wallis, identical
to PCF-2 form).

**Reading:**

- Declared $a_n$: $\delta n + \varepsilon$ with $\delta \ne 0$ EXPLICITLY IMPOSED.
- Declared $b_n$: quadratic with $\alpha \ne 0$.
- Declared deg_a: STRICTLY 1 ($\delta = 0$ is excluded).

**Independent finding (V4):**

PCF-1 v1.3 d=2 stratum (p12_journal_main.tex L124-131) imposes $\alpha \ne 0$
AND $\delta \ne 0$, so deg_a = 1 strictly. PCF-1 d=2 EXCLUDES the deg_a = 0
corner that PCF-2 implementations live in.

**Asymmetry between PCF-1 v1.3 and PCF-2 v1.3:** PCF-2 program statement
does NOT inherit the $\delta_1 \ne 0$ restriction from PCF-1, despite
self-describing as "identical to the $d=2$ convention of PCF-1 to facilitate
code reuse" (L235-236). This is a SUBSTANTIVE SCOPE BROADENING (or
oversight) in PCF-2 v1.3.

---

## V5 — V_quad declaration in `algebraic_independence_audit.py:37-40`

**Source:** `algebraic_independence_audit.py` L37-40.

**Verbatim:**

```python
# V_quad: GCF with a(n)=1, b(n)=3n²+n+1, backward mode
# CF = b(0) + 1/(b(1) + 1/(b(2) + ...)) = 1 + 1/(5 + 1/(15 + ...))
VQUAD_ALPHA = [1]          # a(n) = 1 for all n
VQUAD_BETA = [1, 1, 3]    # b(n) = 3n²+n+1
```

**Reading:**

- $a(n) = 1$ for all $n$ (deg_a = 0).
- $b(n) = 3n^2 + n + 1$ (deg_b = 2).
- "GCF" = generalised continued fraction; backward-mode evaluator.

**Independent finding (V5):**

V_quad — the central transcendental candidate of PCF-1 v1.3 — uses
$a_n \equiv 1$, i.e., **deg_a = 0**. This CONTRADICTS the PCF-1 v1.3 d=2
standard stratum (V4), which imposes $\delta \ne 0$ (deg_a = 1).

V_quad therefore lies OUTSIDE the PCF-1 v1.3 d=2 declared stratum: it is
a deg_a = 0 specimen masquerading as a d=2 stratum representative. This
is a PROTOCOL-TO-STRATUM MISMATCH WITHIN PCF-1 ITSELF (not just PCF-2).
This finding extends the synth-substitute's "SYNTH-SUB-051-UF2" mismatch
upstream: the issue exists in PCF-1 v1.3, and PCF-2 v1.3 inherits it
silently via "code reuse" and "identical convention" claims.

---

## V6 — Independent WZ Newton-polygon balance derivation

**Setup:** Wallis-class CF
$$ p_n \;=\; b_n\,p_{n-1} \;+\; a_n\,p_{n-2}, $$
with $a_n \equiv 1$ (deg_a = 0) and $b_n = c_b\,n^d + O(n^{d-1})$
(deg_b = d).

**Method:** Standard ratio analysis (Birkhoff-Trjitzinsky / Wasow §X.3).

### Step 1: Characteristic ratio.

Let $r_n := p_{n-1}/p_n$. The recurrence yields, dividing by $p_n$:
$$ 1 \;=\; b_n\,r_n \;+\; a_n\,r_n\,r_{n-1}. $$

For $r_{n-1} \approx r_n$ at leading order (a self-consistent ansatz to be
verified), $r_n$ is a root of
$$ a_n\,r^2 \;+\; b_n\,r \;-\; 1 \;=\; 0, $$
giving
$$ r_\pm \;=\; \frac{-b_n \pm \sqrt{b_n^2 + 4 a_n}}{2 a_n}. $$

For $a_n \equiv 1$, $b_n \sim c_b n^d$ with $c_b > 0$ and $n$ large:
$$ r_- \;\approx\; \frac{1}{b_n} \;\approx\; \frac{1}{c_b\,n^d} \quad\text{(small root, dominant solution)}, $$
$$ r_+ \;\approx\; -b_n \;\approx\; -c_b\,n^d \quad\text{(large root, recessive solution)}. $$

### Step 2: Dominant solution (Balance I).

The dominant $p_n$ has $r_n = p_{n-1}/p_n \to 0$, i.e., $r_n = r_- \approx 1/b_n$.
So
$$ p_n / p_{n-1} \;\approx\; b_n \;\approx\; c_b\,n^d \quad\Rightarrow\quad p_n \;\sim\; c_b^n \prod_{k=1}^n k^d \;=\; c_b^n\,(n!)^d. $$

By Stirling, $p_n \sim c_b^n\, n^{dn}\, e^{-dn}\, (2\pi n)^{d/2}$.

In Birkhoff form $\log p_n = A\,n\log n + B\,n + C\,\log n + D + \cdots$:
- **$\mu_{\rm dom} = A = d$** (the "$n\log n$" exponent of the dominant solution).
- **$\gamma_{\rm dom} = e^B = c_b\,e^{-d}$** (the geometric ratio after Stirling-cancellation).

### Step 3: Recessive solution (Balance III).

The recessive $p_n^{\rm rec}$ has $r_n = r_+ \approx -b_n$, i.e.,
$$ p_n^{\rm rec} / p_{n-1}^{\rm rec} \;\approx\; \frac{1}{r_+} \;\approx\; -\frac{1}{b_n} \;\approx\; -\frac{1}{c_b\,n^d}. $$

Then
$$ p_n^{\rm rec} \;\sim\; (-1)^n\,c_b^{-n}\,(n!)^{-d}, $$
so $\log|p_n^{\rm rec}| = -d\,n\log n + (d - \log c_b)\,n - (d/2)\log n + \cdots$.

- **$\mu_{\rm sub} = -d$** (the "$n\log n$" exponent of the recessive solution).
- **$\gamma_{\rm sub} = -1/c_b \cdot e^d$** (with the SIGN coming from $r_+ < 0$ for $a_n, b_n > 0$).

For the more general Wallis case $a_n \sim c_a\,n^{d_a}$ (deg_a = $d_a > 0$),
the analogous derivation gives $r_+ \approx -b_n/a_n$ to leading order, hence
$p_n^{\rm rec}/p_{n-1}^{\rm rec} \approx -a_n/b_n$, and
$\gamma_{\rm sub} = -c_a/c_b \cdot (\text{Stirling cancellation factor})$.
In the deg_a = 0 corner ($c_a = 1$, $d_a = 0$), this reduces to
$\gamma_{\rm sub} = -1/c_b \cdot e^{d}$.

The SIGN $-c_a/c_b$ at the leading "geometric ratio" level is the
robust observation; the Stirling-factor magnitude depends on convention.

### Step 4: A_naive.

The CF precision rate in the "Wallis-error" convention is governed by
the ratio of dominant to recessive convergent denominators:
$$ \log_{10}\bigl|q_n^{\rm dom} / q_n^{\rm rec}\bigr| \;\sim\; (\mu_{\rm dom} - \mu_{\rm sub})\,n\log n \;+\; \cdots $$

**Independent computation:**
$$ A_{\rm naive} \;=\; \mu_{\rm dom} - \mu_{\rm sub} \;=\; d - (-d) \;=\; \boxed{2d} \quad\text{(when deg\_a = 0).} $$

For comparison (deg_a = 1, deg_b = $d$): the analogous computation gives
$\mu_{\rm sub} = -(d - 1)$ (because the recessive ratio is $-a_n/b_n
\sim -c_a/c_b \cdot n^{d_a - d}$, contributing $d - d_a = d - 1$ to the
recessive Stirling exponent), hence $A_{\rm naive} = 2d - 1$ at deg_a = 1.

**General formula:** $A_{\rm naive} = 2d - d_a$.

### Numerical anchors:

| stratum | $d$ | $d_a$ | $A_{\rm naive}$ |
|---------|-----|-------|-----------------|
| PCF-1 d=2, deg_a=1 (declared) | 2 | 1 | 3 |
| PCF-1 V_quad (actual; $a_n\equiv 1$) | 2 | 0 | 4 |
| PCF-2 d=3, deg_a=1 (declared, hypothetical) | 3 | 1 | 5 |
| PCF-2 d=3, deg_a=0 (actual implementation) | 3 | 0 | 6 |
| PCF-2 d=4 (Q1 quartic), deg_a=0 (actual) | 4 | 0 | 8 |

**Independent finding (V6):**

Standard WZ Newton-polygon balance for the Wallis CF $p_n = b_n p_{n-1} + a_n p_{n-2}$
with deg_a = 0, deg_b = $d$ yields:
- $\mu_{\rm dom} = d$, $\gamma_{\rm dom} = c_b\,e^{-d}$ (Balance I, dominant).
- $\mu_{\rm sub} = -d$, $\gamma_{\rm sub}$ has SIGN $-c_a/c_b$ at leading
  order (Balance III, recessive).
- $A_{\rm naive} = \mu_{\rm dom} - \mu_{\rm sub} = 2d$ for deg_a = 0,
  uniform across all bins (NO Galois dependence).

The general formula $A_{\rm naive} = 2d - d_a$ agrees with PCF-1 v1.3
prediction ($A=3$ at d=2, $d_a=1$) for the DECLARED stratum, but the
PCF-1 V_quad EMPIRICAL probe (deg_a = 0) lives in the $A = 4$ row, not
the $A = 3$ row. The synth-substitute's $A_{\rm naive} = 2d$ claim at
deg_a = 0 is independently confirmed.

The sign of $\gamma_{\rm sub}$ at leading order is **negative**
($\propto -c_a/c_b$), consistent with the recessive root $r_+ < 0$ for
positive $a_n, b_n$. This matches the rubber-duck-corrected sign
$\gamma = -c_a/c_b$ (vs. an erroneous $+1/c_b$ that would have been
derived without tracking the sign of the recessive root).

---

## V1-V6 summary table

| V# | Finding (verbatim short form) | Matches synth-substitute claim? |
|----|--------------------------------|----------------------------------|
| V1 | `cf_value()` in session_c1_wkb.py L78-86 uses `x = bk + 1/x` recurrence; deg_a = 0 hardcoded. | **YES** (independent confirmation pending verdict-body read) |
| V2 | session_b_pslq.py L162-170 + quartic_tail_fit_all60.py L21-30 use the IDENTICAL `x = bk + 1/x` recurrence; deg_a = 0 across all three pcf2 cubic + quartic pipelines. | **YES** (independent extension of V1 to PSLQ + quartic) |
| V3 | pcf2_program_statement.tex L228-234 declares $a_n = \delta_1 n + \delta_0$ with NO $\delta_1 \ne 0$ restriction; "deg_a $\le$ 1" formally, with deg_a = 0 only as a corner. | **YES**, but with refinement: declared scope is deg_a $\in \{0, 1\}$, NOT deg_a = 1 strictly. |
| V4 | p12_journal_main.tex L124-131 imposes $\alpha, \delta \ne 0$ for PCF-1 d=2; deg_a = 1 STRICTLY, $\delta = 0$ excluded. | **YES** (matches synth-substitute; PCF-1 is stricter than PCF-2). |
| V5 | algebraic_independence_audit.py L37-40 declares VQUAD_ALPHA = [1] (a(n)=1) → V_quad has deg_a = 0, OUTSIDE PCF-1 d=2 declared stratum. | **YES** — extends synth-substitute SYNTH-SUB-051-UF2 finding upstream into PCF-1 v1.3 itself. |
| V6 | Independent WZ derivation: $\mu_{\rm dom} = d$, $\mu_{\rm sub} = -d$, $\gamma_{\rm sub} \propto -c_a/c_b$, $A_{\rm naive} = 2d$ for deg_a = 0. General: $A_{\rm naive} = 2d - d_a$. | **YES** (independently confirms $A_{\rm naive} = 2d$ at deg_a = 0; sign $-c_a/c_b$ confirmed). |

**Summary:** All six independent verifications V1-V6 confirm the load-bearing
substrate claims of the synth-substitute. No contradiction surfaced. Therefore
**HALT_061_V1_CONTRADICTS / V3_CONTRADICTS / V6_CONTRADICTS_SYNTH_SUBSTITUTE
do NOT trigger.**

One INDEPENDENT REFINEMENT (V3): the PCF-2 program statement does not
impose $\delta_1 \ne 0$, so its declared scope formally INCLUDES deg_a = 0
as a corner. The synth-substitute's framing ("deg_a = 1 declared, deg_a = 0
implemented") is therefore correct in spirit but slightly imprecise — the
issue is that the implementation tests ONLY the $\delta_1 = 0$ corner,
NOT the rest of the $\delta_1 \ne 0$ slice that would be expected
under a "deg_a = 1" reading. This refinement is logged as
[D-V3-refinement-of-synth-substitute-framing] for STEP 5.

One INDEPENDENT FRESH FINDING (V5): the protocol-to-stratum mismatch
exists IN PCF-1 v1.3 ITSELF (V_quad uses deg_a = 0 while §6/Theorem 5
nominally targets deg_a = 1 stratum). This is upstream of PCF-2 and
implies the mismatch is SYSTEMIC across the SIARC PCF program, not
specific to PCF-2 R1.1/R1.3/Q1. This is logged as
[U-V5-systemic-pcf1-pcf2-deg_a-zero-corner-test-only] in unexpected_finds.

The synth-substitute body may now be read.
