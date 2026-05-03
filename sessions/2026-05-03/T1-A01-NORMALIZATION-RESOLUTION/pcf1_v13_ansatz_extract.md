# D1 — PCF-1 v1.3 §2 / §6 ansatz extract (verbatim)

**Task:** T1-A01-NORMALIZATION-RESOLUTION — STEP 1
**Source file:** `siarc-relay-bridge/sessions/2026-05-01/PCF1-V13-UPDATE/p12_pcf1_main.tex`
**Source SHA-256:** computed at session B1 (see `claims.jsonl`).

---

## §2.a — Three-term recurrence (the Wallis convergent)

PCF-1 v1.3, `\section{The Spec(K) Framework --- v5 Upgrade}` (TeX line 190),
verbatim:

```tex
We work with PCFs of the form
\[
K(a_{n},b_{n})=b_{0}+\cfrac{a_{1}}{b_{1}+\cfrac{a_{2}}{b_{2}+\cdots}},
\]
together with the Wallis convergent recurrence
$p_{n}=b_{n}p_{n-1}+a_{n}p_{n-2}$ and seeds
$(p_{-1},p_{0},q_{-1},q_{0})=(1,b_{0},0,1)$.
```

So PCF-1's three-term recurrence is

$$
   p_n \;=\; b_n\,p_{n-1} \;+\; a_n\,p_{n-2},
   \qquad q_n \;=\; b_n\,q_{n-1} \;+\; a_n\,q_{n-2},
$$

with seeds $(p_{-1},p_0,q_{-1},q_0)=(1,b_0,0,1)$, and Wallis convergent error

$$
   \delta_n \;=\; \frac{p_n}{q_n} \;-\; L,
   \qquad L \;=\; \lim_{n\to\infty}\frac{p_n}{q_n}.
$$

## §2.b — The amplitude exponent A (PCF-1 v1.3 §6, "WKB Exponent Identity")

PCF-1 v1.3, `\section{The WKB Exponent Identity}` (TeX line 516),
Theorem 5 statement, verbatim (TeX lines 525–545):

```tex
Let $a_{n}=c_{a}n+\varepsilon_{a}$ and
$b_{n}=c_{b}n^{2}+\beta n+\gamma$ be the recurrence coefficients of
a degree-two PCF in the scope of this paper, with leading
coefficients $c_{a}\in\mathbb{Z}\setminus\{0\}$ and
$c_{b}\in\mathbb{Z}_{>0}$. Then the Wallis convergent error
$\delta_{n}=p_{n}/q_{n}-L$ admits the formal asymptotic expansion
\begin{equation}\label{eq:wkb}
\log|\delta_{n}| \;=\; -A\,n\log n \;+\; \alpha\,n
  \;-\; \beta_{w}\log n \;+\; \gamma_{w}
  \;+\; \sum_{k\ge 1}\frac{h_{k}}{n^{k}},
\end{equation}
with leading exponents
\begin{equation}\label{eq:wkb-alpha}
A\in\{3,4\},\qquad
\alpha \;=\; A \;-\; 2\log c_{b} \;+\; \log|c_{a}|,
\end{equation}
where $A=4$ for $V_{\mathrm{quad}}$ and $A=3$ for the five
quadratic-limit families QL01, QL02, QL06, QL15, QL26.
```

So PCF-1 v1.3 defines $A$ as the coefficient of $-n\log n$ in the
asymptotic expansion of $\log|\delta_n|$ as $n\to\infty$. The
$n\log n$ leading channel is the Stirling-rate channel.

## §2.c — Polynomial degrees of $a_n, b_n$ in $n$ (the "d" convention)

PCF-1 v1.3 §5 (TeX line ~225), verbatim:

```tex
v5 explicitly distinguishes these via the
\emph{class label} ``$d=k$ balanced'' meaning the leading-degree pair
$(\deg a,\deg b)$ is $(k+1,k)$ in the $\delta$-direction and $(k-1,k)$ in
the $\alpha$-direction.
```

So the **dominant growth degree** is $d = \max(\deg a_n, \deg b_n)$ in
$n$, with $a_n$ and $b_n$ playing asymmetric roles. For the d=2 class
(the body of PCF-1 v1.3), $\deg b_n = 2$ and $\deg a_n = 1$, so
$d = 2$. The empirical record then exhibits $A \in \{3, 4\}$ for the six
$\Delta<0$ families plus the V_quad (Δ<0) family (Table
`tab:wkb-exponents`, TeX line ~565), all with $d = 2$.

## §2.d — Identification of $A$ with a Newton-polygon slope?

PCF-1 v1.3 §6 (Remark `rem:wkb-formal`, TeX line ~547) verbatim:

```tex
A rigorous proof of~\eqref{eq:wkb}--\eqref{eq:wkb-alpha} would proceed
via a WKB analysis of the Wallis recurrence
$p_{n}=b_{n}p_{n-1}+a_{n}p_{n-2}$; we leave it as an open problem
of independent interest.
```

So PCF-1 v1.3 does **not** explicitly identify $A$ with the
Newton-polygon slope of the recurrence operator at $\infty$, nor with
Wasow's $\sigma$ or Adams's $2\sigma$. The identification is
implicit in the "WKB" name and in the structural form $-A\,n\log n
+ \alpha\,n - \beta_w\log n + \gamma_w$, which matches the canonical
Birkhoff–Trjitzinsky 1933 form $\exp(Q(x))\,x^{\rho}\,s(x)$ with
$Q(x) = \mu\,x\log x + \gamma\,x$ in B–T's "normal case" (see D3).

---

## Empirical bracket reference (no re-derivation; cited from Phase-1)

Phase-1 (`gap_proposition_for_d_ge_3.md`, §3) derived

$$
   A \in [d,\ 2d]
   \quad \text{for } d \ge 3, \text{ literature-derivable},
$$

with B4 = 2d at the upper end **under the Wasow-normalisation reading**.
Under the alternative Adams-normalisation reading the bracket would
shift to $[d/2, d]$ and B4 = 2d would be **outside** the literature
bracket — a major-halt branch. Resolving this is the present task.

For $d = 2$ the empirical PCF-1 v1.3 record gives $A \in \{3, 4\}$,
which sits in the Wasow bracket $[d, 2d] = [2, 4]$ and **outside** the
Adams bracket $[d/2, d] = [1, 2]$. The d=2 empirical record is therefore
itself a strong cross-check in favour of the Wasow reading; this is
**consistent with**, but not by itself a verbatim resolution of, the
A-01 ambiguity.
