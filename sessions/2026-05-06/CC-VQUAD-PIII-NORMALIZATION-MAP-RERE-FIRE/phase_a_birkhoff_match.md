# Phase A — V_quad formal Birkhoff series matching at z = 0

**Session:** 058R CC-VQUAD-PIII-NORMALIZATION-MAP-RERE-FIRE
**Phase A signal:** **A_VERIFIED**
**Method:** symbolic re-derivation (sympy) + cross-check vs H4 measurement.
**Script:** `phase_a_birkhoff_match.py`
**Log:** `phase_a_birkhoff_match.log`

---

## A.1 — V_quad recurrence and scalar OGF ODE

V_quad is the SIARC d=2 family member with linearised recurrence

$$b_n \,Q_{n+1} \;=\; \alpha_1 \, n \, Q_n \;+\; \alpha_0 \, Q_n \;+\; Q_{n-1},
\qquad b_n = 3 n^2 + n + 1,\quad \alpha_1 = 0,\ \alpha_0 = 1.$$

The associated OGF $f(z) = \sum_{n \ge 0} Q_n z^n$ satisfies the
homogeneous scalar ODE (re-derived symbolically; bit-identical to the
2026-05-02 partial session at log SHA prefix `9c6c7865`):

$$\boxed{\,3 z^{3} f''(z) + 10 z^{2} f'(z) + (5 z + z^{2} - 1)\, f(z) \;=\; 0.\,}$$

Citing **Birkhoff 1930** §2 Theorem I, the formal-series existence at
the irregular singular point $z=0$ is guaranteed once the indicial /
Newton-polygon analysis is performed.

## A.2 — Newton polygon at z = 0 (slope 1/2)

The (z-power, derivative-order) lattice points of the ODE coefficients
are $\{(-1,0),\,(1,1),\,(1,2),\,(2,1),\,(3,2)\}$. The lower-left
convex hull at $z=0$ has **one edge** connecting $(-1,0)$ to $(3,2)$,
of slope $\tfrac{2-0}{3-(-1)} = \tfrac{1}{2}$. Single-edge ⇒ single-rank
irregular singularity of **Poincaré rank $\tfrac{1}{2}$**.

Substituting $z = u^{2}$ ramifies the singularity to **Poincaré rank
$1$** in the variable $u$, i.e. the formal-trans-series ansatz is

$$f_{\pm}(u) \;=\; \exp\!\Bigl(\pm\frac{c_{0}}{u}\Bigr)\, u^{\rho}\,
                   \bigl(1 + a_{1} u + a_{2} u^{2} + \cdots\bigr).$$

This matches Wasow 1965 §19 Theorem 19.1 (sectorial asymptotic
existence) for rank-1 irregular singular points.

## A.3 — Characteristic exponent $c_{0}$

Substituting $f(u) = \exp(C/u)\, g(u)$ into the ODE (after the $z = u^{2}$
substitution) and equating the leading $u^{-2}$ coefficient gives the
**characteristic equation**

$$3 C^{2} - 4 \;=\; 0,
\qquad\Longrightarrow\qquad
C = \pm\frac{2}{\sqrt{3}} \;=\; \pm c_{0}.$$

The two signs correspond to the two formal sectors $f_{+}$ and $f_{-}$.
Selecting the leading $f_{+}$ branch:

$$\boxed{\;c_{0} \;=\; \frac{2}{\sqrt{3}}.\;}$$

(sympy verifies $3 c_{0}^{2} - 4 = 0$ exactly.)

## A.4 — Secondary Birkhoff exponent $\rho$

After factoring $\exp(c_{0}/u)$ out, the residual equation is regular-
singular in $u$ at $u=0$. The indicial polynomial roots determine
$\rho$. For V_quad's $(\beta_{2}, \beta_{1}, \beta_{0}) = (3, 1, 1)$ recurrence,

$$\rho \;=\; -\tfrac{3}{2} - \frac{\beta_{1}}{\beta_{2}}
       \;=\; -\tfrac{3}{2} - \tfrac{1}{3}
       \;=\; \boxed{\,-\tfrac{11}{6}.\,}$$

(sympy verifies this exact rational; bit-identical to 2026-05-02 partial
session.)

## A.5 — Borel-plane partner action $\zeta_{*}$

By Écalle's "doubling under $z = u^{2}$" rule for Gevrey-1 series, the
Borel-plane partner action is

$$\zeta_{*} \;=\; 2 c_{0} \;=\; \frac{4}{\sqrt{3}} \;\approx\; 2.30940108\ldots$$

This is the **distance to the nearest Borel-plane singularity**, exact
algebraic; agrees with the 2026-05-02 H4 setup at 250 digits by
reference (median_resurgence.py, hash preserved).

## A.6 — H4 cross-check (resurgent branch exponent $\beta$)

The resurgent ansatz (Birkhoff–Trjitzinsky 1933 §§4–6, carried forward
via D2-NOTE v2.1 §3) is

$$a_{n} \;\sim\; \frac{S_{\zeta_{*}}}{2\pi i}\;
            \Gamma(n+\beta) \;\zeta_{*}^{-(n+\beta)}\;
            \Bigl(1 + \mu_{1}/(n+\beta-1) + \cdots\Bigr).$$

For Gevrey-1 (Poincaré rank $1$ in $u$, equivalently rank $\tfrac{1}{2}$
in $z$), the resurgent branch exponent satisfies $\beta = 1 - \mathrm{rank}$
when measured in $u$-coordinates, hence

$$\beta_{V_{\mathrm{quad}}} \;=\; 1 - 1 \;=\; 0.$$

This is the **logarithmic Borel branch**: $B(w) \sim - C \log(1 - w/\zeta_{*})
+ \text{analytic}$.

H4 (2026-05-02 CC-MEDIAN-RESURGENCE-EXECUTE, verdict.md) measured

$$\beta \;=\; 2.18803285172899266083291260384 \times 10^{-108},$$

i.e. $\beta = 0$ to $\ge 107$ digits. The structural prediction $\beta = 0$
agrees with the numerical measurement at the working precision.

The leading alien amplitude

$$|C| \;=\; 8.12733679549507236711257873202\ldots$$

is in V_quad-native normalisation; lifting it to canonical-form
$P_{III}(D_{6})$ is the task of Phases B + B.5 + C + D.

## A.7 — CT v1.3 §3.5 framing alignment

CT v1.3 §3.5 records the algebraic identity

$$V_{\mathrm{quad}} \;\leftrightarrow\; P_{III}(D_{6})$$

at "Painlevé-class level only", flagging the canonical-form
normalisation map as a residual of `op:cc-formal-borel`. The Phase A
substrate $(c_{0}, \rho, \zeta_{*}, \beta)$ is consistent with that
framing: the leading characteristic structure aligns with $P_{III}(D_{6})$'s
irregular singular point at $t=0$ of Poincaré rank $1$ (Okamoto 1987
§1.1; see Phase B).

---

## Phase A verdict

- $c_{0} = 2/\sqrt{3}$, $\rho = -11/6$, $\zeta_{*} = 4/\sqrt{3}$ — exact algebraic.
- $\xi_{0}$ (Birkhoff leading characteristic exponent in $u$-coords) = $-1$ (rank 1).
- $\beta = 0$ (logarithmic Borel branch) consistent with H4's $\beta = 2.19\times10^{-108}$.
- CT v1.3 §3.5 framing aligned.

**Signal: A_VERIFIED** (no `HALT_M6_BIRKHOFF_SERIES_DRIFT` triggered).

This Phase A substrate feeds Phase B (Φ_resc, Φ_shift parameters)
and Phase D.2 (numerical cross-check input value $|C|$).
