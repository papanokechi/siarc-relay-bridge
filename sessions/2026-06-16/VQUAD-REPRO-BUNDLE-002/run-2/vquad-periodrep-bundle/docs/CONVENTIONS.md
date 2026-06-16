# CONVENTIONS

The identity $C=|\Gamma(\beta)|K$ and its three verifications depend on a small
number of convention choices. Getting any one wrong shifts intermediate
quantities (and, for the Borel-sum kernel, changes the operator factorisation in
Method A). They are collected here so a reproducer can check them at a glance.
All choices match the parent slots PERIOD-REP-VQUAD-001/002/003.

## 1. Borel-sum kernel: $e^{-\xi/z}$

The Borel / Laplace pairing uses the kernel $e^{-\xi/z}$, with the operator
duality

$$ D_\xi \;\longmapsto\; +\,\frac{1}{z}, \qquad \xi \;\longmapsto\; +\,z^2 D_z . $$

This is the convention under which Method A yields the **exact** factorisation
$M=h(z)\,L_\varphi$ with
$h(z)=27(649+30\sqrt3)/\bigl(418501\,z^2(2\sqrt3-3)\bigr)$. The corrected script
`scripts/03-verification/stage4a_methodA_v2.py` runs a **4-convention
anti-fluke test** (the sign/kernel variants $\pm\xi/z$, $\pm z/\xi$): only this
$e^{-\xi/z}$ convention reproduces the exact factorisation, so the choice is
forced, not free. An earlier draft using a different kernel sign produced a
spurious mismatch; that is why the script carries a `_v2` suffix.

> **Bundle note.** In this bundle, the *inline* Method-A self-check inside
> `scripts/03-verification/stage4_methods.py` also uses this corrected
> $+1/z$ convention (operator duality `pos_z2Dz`), so its `methodA` /
> `all_three` flags read `True`, consistent with `stage4a_methodA_v2.py` and
> with the certified result. The parent slot had retained the superseded
> $-1/z$ attempt in that one script and annotated its results file by hand; the
> bundle ships the corrected, self-consistent script instead. This flips only
> the legacy wrong-sign operator duality and changes **no** numerical result
> (Methods B and C are untouched). The exact transformation is recorded in the
> bundle-assembly tool `relativize_and_copy.py` (slot `VQUAD-REPRO-BUNDLE-001`).

## 2. Operator normalisation: $L_{1,2}=x^2+\tfrac13 x+\tfrac13$ (Marchal convention)

The degree-2 form normalising the $V_{\mathrm{quad}}$ operators is

$$ L_{1,2} \;=\; x^2 + \tfrac13 x + \tfrac13 , $$

the **Marchal convention** (after O. Marchal; cf. §2 and the paper's
Acknowledgements, June 2026). All operator coefficients in `01-algebraicity/` and
the residual checks are expressed in this normalisation; using a different
scaling rescales $h(z)$ in Method A correspondingly.

## 3. Sign of the exponent: $f=-\xi$, so $e^{-f}=e^{+\xi}$

In the Fresán–Jossen exponential-period data $(X,f,\omega)$ the period is
$\int_\gamma e^{-f}\,\omega$. Here the integrand is written $e^{+\xi}$, i.e.

$$ f \;=\; -\,\xi \qquad\Longrightarrow\qquad e^{-f}=e^{+\xi}. $$

So the rapid-decay direction (where $e^{-f}\to0$) is $\xi\to-\infty$ along the
negative real axis — exactly where the cycle $\gamma$ runs.

## 4. Base field: $\mathbb{Q}(\sqrt3)$, with $\sqrt3>0$ canonical

All exact algebra lives in the real quadratic field $\mathbb{Q}(\sqrt3)$. The
field element $\sqrt3$ is taken in its **canonical positive real form**
$\sqrt3=+1.7320508\ldots$ (the embedding $\mathbb{Q}(\sqrt3)\hookrightarrow\mathbb{R}$
with $\sqrt3>0$). In the code, elements are pairs $p+q\sqrt3$ of
`fractions.Fraction` (`Q3`), so arithmetic is exact and the embedding is fixed
by evaluating $\sqrt3$ as the positive root only at the final numeric step.

## 5. Branch exponent $\beta=-1/(3\sqrt3)$ and the branch cut

$$ \beta \;=\; -\frac{1}{3\sqrt3} \;=\; -0.19245008972987525\ldots $$

The Borel transform $\widehat B$ has a branch point at $-\xi_0$ (with
$\xi_0=2/\sqrt3=1.1547005\ldots$). The **local exponent** of $\widehat B$ at
$-\xi_0$ is

$$ -(1+\beta) \;=\; -1+\frac{\sqrt3}{9} \;=\; -0.80754991027\ldots, $$

and the Frobenius solution there has **no logarithmic terms** (residual
$1.6\times10^{-46}$; `02-galois/stage3b_frobenius_v2.py`). The branch cut is
placed along the **negative real axis** from $-\xi_0$ to $-\infty$, i.e. the
principal cut for $(\xi+\xi_0)^{-(1+\beta)}$ taken on
$(-\infty,-\xi_0]$. The prefactor $|\Gamma(\beta)|/2\pi$ in the period
representation is the Hankel/reciprocal-Gamma normalisation associated with this
exponent.

## 6. Hankel thimble $\gamma$: orientation around $-\xi_0=-2/\sqrt3$

$\gamma$ wraps the cut on $(-\infty,-\xi_0]$ in three pieces:

| piece | description | parametrisation |
|-------|-------------|-----------------|
| $\gamma_{\text{below}}$ | ray in from $-\infty$, just below the cut | $\xi = t - i0^+$, $t:-\infty\to-\xi_0$ |
| $\gamma_{\text{loop}}$ | small circle around $-\xi_0$ | $\xi(\theta)=-\xi_0+\varepsilon\,e^{i\theta}$, $\theta:-\pi\to+\pi$ |
| $\gamma_{\text{above}}$ | ray out to $-\infty$, just above the cut | $\xi = t + i0^+$, $t:-\xi_0\to-\infty$ |

**Orientation.** The unambiguous specification is the loop parametrisation
$\xi(\theta)=-\xi_0+\varepsilon e^{i\theta}$ with $\theta$ **increasing** from
$-\pi$ to $+\pi$ — i.e. the branch point $-\xi_0$ is encircled
**counterclockwise** (the standard Hankel / reciprocal-Gamma orientation
matching the Laplace inversion $\int_0^\infty\to$ wrapped contour). Along the two
rays $e^{\xi}\to0$ super-exponentially, giving rapid decay.

> **AEAL flag — wording vs. parametrisation.** The parent slot's prose
> (`PERIOD-REP-VQUAD-003/cycle-formal-definition.md`, lines 50–54) labels this
> loop "clockwise", while giving the same parametrisation $\theta:-\pi\to+\pi$,
> which is mathematically counterclockwise. The discrepancy is a wording
> inheritance from the Laplace-inversion picture, not a computational
> difference: the scripts and the verified 46-digit value use the parametrisation
> above. **Treat the parametrisation $\theta:-\pi\to+\pi$ as authoritative**;
> the period value is orientation-checked by Methods B and C agreeing to 46
> digits. (The parent slot is read-only and is not modified.)

## Quick reference

```
kernel        e^{-ξ/z}            D_ξ ↦ +1/z,  ξ ↦ +z² D_z
operator norm L_{1,2}=x²+(1/3)x+(1/3)        (Marchal)
exponent sign f = -ξ              e^{-f}=e^{+ξ},  rapid decay as ξ→-∞
base field    ℚ(√3),  √3=+1.7320508…  (positive embedding)
β             -1/(3√3)=-0.19245008972987525…
branch        cut on (-∞,-ξ₀];  local exponent -(1+β)=-0.80754991027…
ξ₀            2/√3 = 1.1547005383792517…
loop γ        ξ=-ξ₀+εe^{iθ}, θ:-π→+π  (counterclockwise around -ξ₀)
```
