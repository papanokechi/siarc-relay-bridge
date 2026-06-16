# 04 — Cycle: the Hankel rapid-decay thimble γ

This stage makes the integration cycle $\gamma$ in the exponential-period
representation explicit and verifies it is a genuine **rapid-decay cycle** in
the sense required by the Fresán–Jossen framework.

## The cycle

The Borel transform $\widehat B$ has its dominant singularity at $-\xi_0$ with
$\xi_0 = 2/\sqrt3$, and a branch point there with exponent $-(1+\beta)$. The
cycle $\gamma$ is a **Hankel thimble** wrapping the branch cut along the
negative real axis from $-\xi_0$ out to $-\infty$:

- a ray coming in from $-\infty$ just **below** the cut ($\gamma_{\text{below}}$),
- a small loop **around** the branch point $-\xi_0$ ($\gamma_{\text{loop}}$),
- a ray going back out to $-\infty$ just **above** the cut ($\gamma_{\text{above}}$),

with the loop parametrised by $\xi(\theta)=-\xi_0+\varepsilon\,e^{i\theta}$,
$\theta:-\pi\to+\pi$ — i.e. encircling $-\xi_0$ **counterclockwise** (the
standard Hankel orientation, matching the Laplace/Borel inversion
$\int_0^\infty\to$ wrapped contour). The precise parametrisation is the
authoritative specification of orientation; see
[`../../docs/CONVENTIONS.md`](../../docs/CONVENTIONS.md). Along the rays the
integrand carries $e^{\xi}$ with $\xi\to-\infty$, so the integrand decays
**super-exponentially** — that is the rapid-decay condition, and it is what
makes $\int_\gamma e^{\xi}\widehat B(\xi)\,d\xi$ converge and define an
exponential period.

## Script

| Script | Produces | What it shows (paper ref) |
|--------|----------|---------------------------|
| `stage1_hankel_period.py` | `stage1_hankel_results.json` | Defines $\gamma$ explicitly; verifies rapid decay $e^{\xi}\to0$ along the rays; computes the Hankel period $\int_\gamma e^{\xi}\widehat B(\xi)\,d\xi \Rightarrow S\,e^{-\xi_0}$, the value Method B uses (§3, §5.2). |

Standalone (`mpmath`/`json` only). Run **from this directory**:

```bash
cd scripts/04-cycle
python stage1_hankel_period.py
```

The output `stage1_hankel_results.json` is written next to the script; compare
against [`../../data/`](../../data/). The contour value is consistent with the
Method B Borel–Laplace check in [`../03-verification/`](../03-verification/).
