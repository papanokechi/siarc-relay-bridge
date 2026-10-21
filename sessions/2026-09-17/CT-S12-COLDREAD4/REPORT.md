# CT-S12-COLDREAD4 report

Start HEAD was verified as `08aa0e2381b3dc37ee54a3200b7272755ca11d59` on branch `log-pv-01`. End-of-task HEAD was also verified as `08aa0e2381b3dc37ee54a3200b7272755ca11d59`. I read only the permitted packet file and the permitted page image under `sessions/2026-09-17/`; I did not read any other restricted cold-read files.

## 1. Jimbo page-image quotations

The page image confirms the displayed Lax equation (3.1):

```text
∂Y/∂x = ( A_0(t)/x + A_t(t)/(x-t) + diag(1,0) ) Y
```

It also shows the deformation equation `∂Y/∂t = - A_t(t)/(x-t) Y`. The finite singular locations `0` and `t` are visible from the denominators in (3.1), with the irregular point at infinity indicated by the constant diagonal term and the asymptotic formula later on the page.

The page confirms:

```text
the eigenvalues of A_ν(t) = ± (1/2) θ_ν,  (ν=0,t)
```

The page also confirms the Painleve V parameter dictionary:

```text
α = 1/8 (θ_0 - θ_t + θ_∞)^2
β = -1/8 (θ_0 - θ_t - θ_∞)^2
γ = 1 - θ_0 - θ_t
δ = -1/2
```

The same page states a standing assumption:

```text
(A1)_PV    θ_0, θ_t ∉ Z.
```

This is important because the chain later sets `θ_0 = θ_t = 0`, which is outside that stated assumption.

## 2. Recomputing C1, C2, C3

Script: `compute_pv_checks.py`  
Output: `compute_pv_checks.out`  
Output SHA-256: `270301C660C5726BF7C0DF49BA383CB34CB4AB9931C5336C365FDE8F2EDDC592`

For System C,

```text
a = 3x^2 + x + 1,   c = -x^2,
p = a'/a,           q = c/a.
```

SymPy gives

```text
R = p^2/4 + p'/2 - q
  = (12*x**4 + 4*x**3 + 4*x**2 + 11)/(4*(3*x**2 + x + 1)**2)
```

and `R - R_claim = 0`, so C1 is correct.

The roots of `a` are

```text
-1/6 - sqrt(11)*I/6,   -1/6 + sqrt(11)*I/6.
```

At both roots, SymPy gives

```text
lim (x-s)^2 R = -1/4
sqrt(1 + 4*(-1/4)) = 0.
```

Thus the local exponent difference at both finite singular points is zero. C2 is correct as a computation of exponent differences; the later identification of these differences with Jimbo's `θ_0, θ_t` is an additional matching assumption, and it lands outside Jimbo's displayed nonintegrality assumption.

At infinity,

```text
lim_{x→∞} R = 1/3,
sqrt(lim R) = sqrt(3)/3 = 1/sqrt(3).
```

Thus the leading WKB factors are `exp(± x/sqrt(3))`, whose exponent difference is `(2/sqrt(3))*x`. C3 is correct at leading order.

## 3. C4 and C5 arithmetic

Substituting `θ_0 = θ_t = 0` into Jimbo's dictionary gives

```text
α = θ_∞^2/8
β = -θ_∞^2/8
γ = 1
δ = -1/2
```

Therefore `β = -α` identically. If `β = 0`, then `θ_∞ = 0`, and consequently `α = 0`. Hence the tuple `(α, β, γ, δ) = (1/6, 0, 0, -1/2)` is arithmetically incompatible with this specialization: `β=0` forces `α=0`, and derived `γ=1` also conflicts with `γ=0`.

I did not independently verify the existence or details of the unnamed "published source" assigning `(1/6, 0, 0, -1/2)`, because the packet gives no citation for that source. The contradiction is therefore conditional on that assignment being accurately reported.

## 4. C6 rescaling derivation

Starting from the packet's PV equation,

```text
w'' = (1/(2w) + 1/(w-1)) (w')^2 - w'/z
      + (w-1)^2 (αw + β/w)/z^2 + γw/z + δw(w+1)/(w-1),
```

I derived the scaling directly in SymPy. If `W(z) = w(k z)`, then `W' = k w'` and `W'' = k^2 w''` evaluated at the old variable `kz`. Substitution and simplification gives exactly the PV equation for `W(z)` with

```text
(α, β, γ, δ) -> (α, β, kγ, k^2δ).
```

The script's symbolic difference between the transformed RHS and the RHS with `(α, β, kγ, k^2δ)` is `0`.

The inverse convention is also recorded: if the new coordinate is `Z = k z` and `V(Z) = w(Z/k)`, the transformed parameters are

```text
(α, β, γ/k, δ/k^2).
```

Thus the packet's C6 law is correct for the convention `W(z)=w(cz)`. Under either convention, keeping `δ = -1/2` fixed forces `c^2 = 1`, so `γ=1` cannot be rescaled to `γ=0`. The claimed contradiction is not removed by this rescaling convention.

## 5. C7 affine normalization

System C has finite singular points at the two roots of `a`:

```text
s_+ = -1/6 - sqrt(11)*I/6,
s_- = -1/6 + sqrt(11)*I/6,
s_+ - s_- = -sqrt(11)*I/3.
```

Jimbo's page has the normalized asymptotic factor `e^(x 0)` in the displayed matrix notation, so the leading exponent difference at infinity is the Jimbo spectral variable. Matching System C's leading exponent difference `(2/sqrt(3))*x` by an affine coordinate `z = k(x-s_0)` forces

```text
k = 2/sqrt(3)
```

up to the harmless sign/order convention from exchanging the two exponential branches.

With that normalization,

```text
t = k(s_+ - s_-) = -2i sqrt(33)/9
```

or the opposite sign if the finite singular points are ordered oppositely. Hence `|t| = 2 sqrt(33)/9`.

However, the identification of System C's two finite singular points with Jimbo's `0` and `t` is not proved by the scalar equation alone. It is a legitimate affine matching assumption for placing this two-finite-singularity, one-irregular-singularity scalar problem into Jimbo's PV coordinate normalization, but it remains an assumption unless a scalar-reduction/Lax-system identification is supplied.

## 6. Verdicts

**Claimed contradiction verdict: SOUND WITH CAVEAT.** C1-C6 check out computationally and algebraically, and the rescaling law is correct in the packet's convention. Conditional on the published tuple `(1/6, 0, 0, -1/2)` being accurately reported and on applying Jimbo's parameter dictionary to the resonant case `θ_0 = θ_t = 0`, the contradiction is real. The caveats are that the tuple's source was not supplied for independent verification, and Jimbo's page explicitly assumes `θ_0, θ_t ∉ Z`, while the chain uses `θ_0 = θ_t = 0`.

**"Single fibre, no free deformation parameter" verdict: CONDITIONAL / SOUND WITH CAVEAT.** Once Jimbo's infinity normalization and the affine identification of the two finite singularities with `0` and `t` are accepted, `k` and then `t` are fixed up to sign/order, so this fixed System C represents a single normalized fibre. That conclusion does not follow unconditionally from the scalar equation alone without the PV/Jimbo identification assumption.
