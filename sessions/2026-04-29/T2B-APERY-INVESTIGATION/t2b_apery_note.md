# T2B — Theoretical Note on the $a_2/b_1^2 = -2/9$ Identity in $F(2,4)$ Trans Families

**Date:** 2026-04-29
**Status:** empirical observation, not a theorem. No HALT criteria met.

## (a) What $-2/9$ means analytically

For a degree-(2,1) PCF with $a(n) = a_2 n^2 + a_1 n + a_0$ and
$b(n) = b_1 n + b_0$, the asymptotic ratio
$$\frac{a(n)}{b(n)^2} \longrightarrow \frac{a_2}{b_1^2}$$
is the **leading-term ratio**. Under the standard equivalence transformation
$K(a_n / b_n) \mapsto K(c_n / 1)$ with $c_n = a_n/(b_{n-1}b_n)$, one has
$c_n \to a_2/b_1^2$. Hence $a_2/b_1^2$ is the **asymptotic Worpitzky
parameter** of the equivalent canonical form. The value $-2/9 \approx
-0.2222$ encodes the asymptotic balance between the quadratic numerator
and the squared linear denominator.

## (b) Relationship to the Worpitzky bound $-1/4$

Worpitzky's theorem (and the Pringsheim / Scott–Wall parabola theorem)
guarantees convergence of $K(c_n/1)$ when $|c_n| \le 1/4$ (parabolic
region). The boundary $c = -1/4$ is well known as a marginal-convergence
locus.

$|-2/9| = 0.2222\ldots < 1/4$: the $F(2,4)$ Trans families lie
**strictly inside** the Worpitzky region, **not on the boundary**.

A direct enumeration of the achievable ratios under the empirical
constraint $a_2 \in \{-2, 1\}$, $b_1 \in \{\pm 2, \pm 3\}$ (the
empirically observed Trans-family leading coefficients at $D = 4$,
per Prop. `prop:deg21` of `main_R1.tex`) gives only four values:

| $a_2$ | $b_1^2$ | $a_2/b_1^2$ | region |
|------:|--------:|------------:|:-------|
| $-2$ | 4 | $-1/2$ | outside parabolic region (divergent / oscillatory) |
| $-2$ | 9 | $-2/9$ | **interior, negative** |
| $1$ | 4 | $1/4$ | parabolic boundary |
| $1$ | 9 | $1/9$ | interior, positive |

So $-2/9$ is the **unique negative Worpitzky-interior ratio achievable
at $D = 4$** from this constrained leading-coefficient pool. The
$+1/9$ families empirically populate $\Rat$ and $\Des$ rather than
$\Trans$ (per the F(2,4) census); the $-1/2$ families fail to
converge; the $+1/4$ families sit on the marginal locus and yield
algebraic / boundary behavior. By arithmetic exhaustion, every
convergent $\Trans$ family at $D=4$ is forced into the cell
$\{a_2 = -2, b_1^2 = 9\}$, hence ratio $-2/9$.

This is a **pigeonhole consequence of the small coefficient bound**,
not a deep convergence-theoretic critical value.

## (c) Appearance in known $\pi$ / $\pi^2$ continued fractions

Numerical/literature survey:

- Brouncker variant $4/\pi = 1 + 1^2/(3 + 2^2/(5 + 3^2/(7 + \ldots)))$:
  $a(n) = n^2$, $b(n) = 2n+1$, ratio $a_2/b_1^2 = 1/4$ (verified to
  50 dps in `_t2b_check.py`). This is degree-(2,1) and **Möbius-of-$\pi$**,
  but with ratio $+1/4$, not $-2/9$.
- Brouncker classical $4/\pi = 1 + 1^2/(2 + 3^2/(2 + 5^2/(2 + \ldots)))$:
  $b(n) = 2$ constant, $b_1 = 0$ — ratio undefined.
- Lange's CF $\pi = 3 + 1^2/(6 + 3^2/(6 + 5^2/(6 + \ldots)))$:
  $b$ constant, ratio undefined.
- Apéry's CF for $\zeta(2) = \pi^2/6$: degree-(4,2), ratio
  $a_4/b_2^2 = -1/121$. Wrong profile.
- No classical $\pi$ or $\pi^2$ CF in standard references
  (Lorentzen–Waadeland, Cuyt–Petersen) is found with ratio $-2/9$.

## (d) Möbius-of-$\pi$ does NOT force the ratio

Two Möbius-of-$\pi$ cases give different leading ratios:

| family | limit | $a_2/b_1^2$ |
|---|---|---|
| Brouncker $4/\pi$ | $\pi/4 \cdot 4 = 4/\pi$ | $+1/4$ |
| F(2,4) Trans | $(\alpha\pi+\beta)/(\gamma\pi+\delta)$ | $-2/9$ |

Therefore "$L$ is Möbius-of-$\pi$" does **not** imply any specific
value of $a_2/b_1^2$. The leading ratio carries no Möbius-π forcing.
This is corroborated by T2A: at degree-(4,2) the analogous ratio
$a_d/b_{d/2}^2$ is uniformly distributed over $\{1/4, 1/2, 1, 2\}$
across 1000 deep-validated Trans families with no predictive power
(bridge: T2A-CMAX2-RATIO).

## (e) Honest assessment: theorem, conjecture, or observation?

**Empirical observation.** Specifically:

1. The paper `main_R1.tex` proves the identity for **3 representative
   families** (Prop. `prop:ratio`); the L2-EXACTNESS-SCANNER (2026-04-23)
   extended the observation to all 24 families. Neither is a theorem
   in the sense of analytic forcing.
2. The mechanism is **arithmetic exhaustion** of the achievable Worpitzky-
   interior ratios at $D = 4$ given the empirical leading-coefficient
   set $\{a_2, b_1\}$. Remove the $D = 4$ bound (T2A: $D = 3$ at
   degree-(4,2)) and the structure dissolves.
3. **No connection to Apéry's CF** for $\zeta(2)$ is established;
   profiles differ (degree-(2,1) vs (4,2)) and ratios differ ($-2/9$
   vs $-1/121$).
4. **No connection to Worpitzky critical values** is established; $-2/9$
   is interior, not boundary.
5. **No Möbius-of-$\pi$ forcing** is established; counterexample:
   Brouncker $4/\pi$ has ratio $+1/4$.

**Conclusion:** The $-2/9$ identity is correctly stated in `main_R1.tex`
as an open problem (`prob:deg21open`), not a theorem. It is an arithmetic
consequence of the small coefficient bound, not a deep structural law.
Future work at larger $D$ in $F(2, D)$ should test whether the family
of Worpitzky-interior negative ratios broadens (predicted) or whether
$-2/9$ continues to dominate (would suggest a genuine deeper structure).

## Recommended next investigations

- **F(2,5) / F(2,6) survey:** does the Trans stratum at $D > 4$ admit
  ratios other than $-2/9$? If yes, the pigeonhole explanation is
  confirmed; if no, escalate to genuine arithmetic-constraint hypothesis.
- **Hypergeometric witness search beyond ${}_2F_1$:** the paper's
  Problem `prob:hyp` proposes ${}_3F_2$ / Heun. A positive identification
  would supersede the $-2/9$ ratio as the structural invariant.
- **Equivalent canonical form:** explicitly compute the
  equivalence-transformed $c_n$ for all 24 families and check whether
  $c_n \to -2/9$ at the predicted rate ($O(1/n)$ correction). This
  would tighten the asymptotic analysis but not change the conclusion.
