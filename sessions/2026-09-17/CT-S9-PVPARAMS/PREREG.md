# PREREG — CT-S9-PVPARAMS

Session folder: `sessions\2026-09-17\CT-S9-PVPARAMS\`.

## Sources and conventions fixed before computation

INSPECTED — Painleve V equation convention. Source: DLMF, Eq. 32.2.5, fetched as `refs\DLMF_32.2.E5.tex` from https://dlmf.nist.gov/32.2.E5.tex, sha256 `613250E4AC93F60736348BBE063D535D3E3E790D7F7689E885483E043ED4943F`. Verbatim quote:

```tex
\[\frac{{\mathrm{d}}^{2}w}{{\mathrm{d}z}^{2}}=\left(\frac{1}{2w}+\frac{1}{w-1}%
\right)\left(\frac{\mathrm{d}w}{\mathrm{d}z}\right)^{2}-\frac{1}{z}\frac{%
\mathrm{d}w}{\mathrm{d}z}+\frac{(w-1)^{2}}{z^{2}}\left(\alpha w+\frac{\beta}{w%}
\right)+\frac{\gamma w}{z}+\frac{\delta w(w+1)}{w-1},\]
```

INSPECTED — PV isomonodromy/Lax convention and parameter dictionary. Source: Michio Jimbo, "Monodromy Problem and the Boundary Condition for Some Painleve Equations," Publ. RIMS 18 (1982), p. 1152, fetched from https://ems.press/doi/pdf/10.2977/prims/1195183300 as `refs\jimbo_1982_prims.pdf`, sha256 `255D4F079767FB050CB462DC91204AFAF09507BBA74789ADE1DA10DCE4F18815`; page image retained as `outputs\jimbo_page16-16.png`. Verbatim quote from p. 1152:

```text
(3.1)  ∂Y/∂x = ( A_0(t)/x + A_t(t)/(x-t) + (1 0; 0 0) )Y,
       ∂Y/∂t = - A_t(t)/(x-t) Y.

We set

the eigenvalues of A_v(t) = ± 1/2 θ_v,  (v=0,t)

diagonal of A_0(t)+A_t(t) = -1/2 ( θ_∞ ; -θ_∞ ).

Then y(t)=... satisfies (PV) with the parameters

α = 1/8 (θ_0 - θ_t + θ_∞)^2,   β = -1/8 (θ_0 - θ_t - θ_∞)^2,

γ = 1 - θ_0 - θ_t,             δ = -1/2.
```

INSPECTED — PV row/Katz-family convention. Source: van der Put and Saito, "Moduli spaces for linear differential equations and the Painleve equations," Ann. Inst. Fourier 59 (2009), Table 2.1 on journal p. 2635/PDF p. 26, repo source `sessions\2026-09-17\CT-R1-AUDIT\refs\vanderPut-Saito-AIF-2009-59-7-2611.pdf`; extracted text retained as `outputs\vdp_pages24-28.txt`. Verbatim quote from the extracted table line:

```text
D̃5          PV                    0    0     1   -     3
```

## Hypothesis under test

STRUCTURAL — If System C can be matched to the Jimbo PV Lax convention above, then the two finite regular singularities should provide the two finite exponent differences θ_0 and θ_t (up to labeling/sign conventions), while the unramified rank-1 irregular singularity at infinity should provide the formal-monodromy exponent datum entering θ_∞ and the exponential normalization entering δ.

## Observables fixed before computation

PROVEN-if-symbolic — For System C, compute exactly and symbolically: `b-a'`; the finite singular points; the indicial polynomials and exponent differences at both finite points; the Frobenius resonance/log coefficient; the normal-form potential and residues; the transformed normal-form potential at infinity; pole order, ramification and Katz invariant; formal exponential factors and formal monodromy exponent(s) in the scalar normal form.

## Falsification criteria for the companion parameter values

Using only the Jimbo dictionary quoted above:

- If either finite exponent difference is not zero, then the companion's use of `θ_1=θ_2=0` is falsified.
- If the finite exponent differences are zero but the singularities have non-trivial unipotent monodromy, then `β=0` and/or `γ=0` may not be justified by apparentness; they survive only if the quoted dictionary depends solely on exponent differences and the scalar-to-Jimbo identification is accepted.
- If the scalar formal monodromy datum at infinity cannot be mapped unambiguously to Jimbo's `θ_∞`, then `α=1/6` is undetermined by local data in this convention.
- `δ=-1/2` is treated as Jimbo's normalization, not as a value computed from System C unless a scale-normalized Lax embedding is exhibited.

Criteria will not be changed after symbolic results are seen.
