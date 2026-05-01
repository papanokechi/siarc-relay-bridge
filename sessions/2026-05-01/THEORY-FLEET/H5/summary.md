# H5 — SIARC stratification on \(M_{1,1}=X(1)\)

## Bottom line

The canonical map from a SIARC cubic \(b\) to moduli is standard: the nonsingular curve
\[
E_b: y^2=b(x)
\]
has a period lattice \(\Lambda_b=\{\int_\gamma dx/y:\gamma\in H_1(E_b,\mathbb Z)\}\), hence a point \(\tau_b\in\mathbb H/SL_2(\mathbb Z)\).  The modular coordinate is \(j(E_b)=j(\tau_b)\).  This gives a rigorous X(1) plot and a canonical period recipe for all 50 cubic families.

However, the three SIARC trichotomy bins do **not** appear to be canonical modular-geometric substrata of \(X(1)\).  The equianharmonic subcell \(j=0\) is a genuine CM point and explains the four special cubic families, but the remaining three-way empirical partition is better viewed as arithmetic/PCF-specific structure overlaid on the j-line, not as a CM locus, a finite set of \(|j|\)-level strata, or an \(X_0(N)\) partition.

## Canonical period map

Let
\[
b(x)=a x^3+p x^2+q x+r,\qquad a\ne0,
\]
with nonzero cubic discriminant \(\Delta_3(b)\).  Then \(E_b:y^2=b(x)\) is an elliptic curve over \(\mathbb C\).  The invariant differential is \(\omega_E=dx/y\), and a symplectic homology basis \((\gamma_1,\gamma_2)\) gives periods
\[
\Omega_i=\int_{\gamma_i}\omega_E,
\qquad \tau=\Omega_2/\Omega_1,
\qquad \operatorname{Im}\tau>0.
\]
Reducing \(\tau\) by \(SL_2(\mathbb Z)\) to the standard fundamental domain
\[
\mathcal F=\{\tau\in\mathbb H: |\tau|\ge1,\\ |\Re\tau|\le1/2\}
\]
gives the canonical coordinate \(\tau_b\).  Diamond--Shurman, Chs. 1--2, describe the quotient \(SL_2(\mathbb Z)\backslash\mathbb H\) as the moduli of complex elliptic curves; Stein, Def. 1.1 and Thm. 1.2, gives the modular-group action and generators, and Stein, Thm. 2.11, identifies the elliptic points \(i\) and \(\rho=e^{2\pi i/3}\) in \(\mathcal F\).

There are two equivalent recipe-level computations.

1. **Invariant / j-inversion recipe.**  Compute \(c_4,\Delta\) for the Weierstrass model and set \(j=c_4^3/\Delta\), as in LMFDB's j-invariant knowl.  For the monic SIARC cubics \(x^3+p x^2+q x+r\),
\[
\Delta_3=p^2q^2-4q^3-4p^3r-27r^2+18pqr,
\qquad
j_b=\frac{256(p^2-3q)^3}{\Delta_3}.
\]
Then \(\tau_b\) is the unique point of \(\mathcal F\) with \(j(\tau_b)=j_b\), using
\(j=E_4^3/\Delta\) and \(\Delta=(E_4^3-E_6^2)/1728\) in the usual normalized convention.  Stein, Prop. 2.1, Prop. 2.4, and Thm. 2.17, give the Eisenstein/discriminant infrastructure.

2. **Root / AGM recipe.**  Let \(e_1,e_2,e_3\) be the roots of \(b\), choose a cross-ratio \(\lambda\), transform to Legendre form, and use complete elliptic integrals
\[
\tau=i\,K(1-\lambda)/K(\lambda)
\]
with consistent branch choices; then reduce to \(\mathcal F\).  This is the practical period algorithm used in the classical elliptic-curve literature (Husemoller, Ch. I; Cremona, Ch. 3 online edition).

## Recipe-level \(\tau_b\) table for the 50 cubic families

For every row below, \(u=p^2-3q\), \(j_b=256u^3/\Delta_3\), and \(\tau_b=j^{-1}_{\mathcal F}(j_b)\).  Rows 30--33 have \(u=0\), hence \(j=0\) and \(\tau_b=\rho=e^{2\pi i/3}\) up to the boundary convention.  No row has \(j=1728\).

| id | \(b(n)\) | \(\Delta_3\) | SIARC bin | \(u\) | \(\tau_b\) recipe |
|---:|---|---:|---|---:|---|
| 1 | \(n^3-3n^2-3n-3\) | -864 | -_S3_CM | 18 | \(j^{-1}_{\mathcal F}(256u^3/\Delta)\) |
| 2 | \(n^3-3n^2-3n-2\) | -459 | -_S3_CM | 18 | same recipe |
| 3 | \(n^3-3n^2-3n-1\) | -108 | -_S3_CM | 18 | same recipe |
| 4 | \(n^3-3n^2-3n+2\) | 621 | +_S3_real | 18 | same recipe |
| 5 | \(n^3-3n^2-3n+3\) | 756 | +_S3_real | 18 | same recipe |
| 6 | \(n^3-3n^2-2n-3\) | -823 | -_S3_CM | 15 | same recipe |
| 7 | \(n^3-3n^2-2n-2\) | -472 | -_S3_CM | 15 | same recipe |
| 8 | \(n^3-3n^2-2n-1\) | -175 | -_S3_CM | 15 | same recipe |
| 9 | \(n^3-3n^2-2n+1\) | 257 | +_S3_real | 15 | same recipe |
| 10 | \(n^3-3n^2-2n+3\) | 473 | +_S3_real | 15 | same recipe |
| 11 | \(n^3-3n^2-n-3\) | -716 | -_S3_CM | 12 | same recipe |
| 12 | \(n^3-3n^2-n-2\) | -419 | -_S3_CM | 12 | same recipe |
| 13 | \(n^3-3n^2-n-1\) | -176 | -_S3_CM | 12 | same recipe |
| 14 | \(n^3-3n^2-n+1\) | 148 | +_S3_real | 12 | same recipe |
| 15 | \(n^3-3n^2-n+2\) | 229 | +_S3_real | 12 | same recipe |
| 16 | \(n^3-3n^2-3\) | -567 | -_S3_CM | 9 | same recipe |
| 17 | \(n^3-3n^2-2\) | -324 | -_S3_CM | 9 | same recipe |
| 18 | \(n^3-3n^2-1\) | -135 | -_S3_CM | 9 | same recipe |
| 19 | \(n^3-3n^2+1\) | 81 | +_C3_real | 9 | same recipe |
| 20 | \(n^3-3n^2+3\) | 81 | +_C3_real | 9 | same recipe |
| 21 | \(n^3-3n^2+n-2\) | -211 | -_S3_CM | 6 | same recipe |
| 22 | \(n^3-3n^2+n-1\) | -76 | -_S3_CM | 6 | same recipe |
| 23 | \(n^3-3n^2+n+3\) | -76 | -_S3_CM | 6 | same recipe |
| 24 | \(n^3-3n^2+2n-3\) | -239 | -_S3_CM | 3 | same recipe |
| 25 | \(n^3-3n^2+2n-2\) | -104 | -_S3_CM | 3 | same recipe |
| 26 | \(n^3-3n^2+2n-1\) | -23 | -_S3_CM | 3 | same recipe |
| 27 | \(n^3-3n^2+2n+1\) | -23 | -_S3_CM | 3 | same recipe |
| 28 | \(n^3-3n^2+2n+2\) | -104 | -_S3_CM | 3 | same recipe |
| 29 | \(n^3-3n^2+2n+3\) | -239 | -_S3_CM | 3 | same recipe |
| 30 | \(n^3-3n^2+3n-3\) | -108 | -_S3_CM | 0 | \(\rho\), equianharmonic CM |
| 31 | \(n^3-3n^2+3n+1\) | -108 | -_S3_CM | 0 | \(\rho\), equianharmonic CM |
| 32 | \(n^3-3n^2+3n+2\) | -243 | -_S3_CM | 0 | \(\rho\), equianharmonic CM |
| 33 | \(n^3-3n^2+3n+3\) | -432 | -_S3_CM | 0 | \(\rho\), equianharmonic CM |
| 34 | \(n^3-2n^2-3n-3\) | -519 | -_S3_CM | 13 | same recipe |
| 35 | \(n^3-2n^2-3n-2\) | -244 | -_S3_CM | 13 | same recipe |
| 36 | \(n^3-2n^2-3n-1\) | -23 | -_S3_CM | 13 | same recipe |
| 37 | \(n^3-2n^2-3n+1\) | 257 | +_S3_real | 13 | same recipe |
| 38 | \(n^3-2n^2-3n+2\) | 316 | +_S3_real | 13 | same recipe |
| 39 | \(n^3-2n^2-3n+3\) | 321 | +_S3_real | 13 | same recipe |
| 40 | \(n^3-2n^2-2n-2\) | -268 | -_S3_CM | 10 | same recipe |
| 41 | \(n^3-2n^2-2n-1\) | -83 | -_S3_CM | 10 | same recipe |
| 42 | \(n^3-2n^2-2n+2\) | 148 | +_S3_real | 10 | same recipe |
| 43 | \(n^3-2n^2-n-3\) | -439 | -_S3_CM | 7 | same recipe |
| 44 | \(n^3-2n^2-n-2\) | -236 | -_S3_CM | 7 | same recipe |
| 45 | \(n^3-2n^2-n-1\) | -87 | -_S3_CM | 7 | same recipe |
| 46 | \(n^3-2n^2-n+1\) | 49 | +_C3_real | 7 | same recipe |
| 47 | \(n^3-2n^2-n+3\) | -31 | -_S3_CM | 7 | same recipe |
| 48 | \(n^3-2n^2-3\) | -339 | -_S3_CM | 4 | same recipe |
| 49 | \(n^3-2n^2-2\) | -172 | -_S3_CM | 4 | same recipe |
| 50 | \(n^3-2n^2-1\) | -59 | -_S3_CM | 4 | same recipe |

## Are the bins modular-geometric?

- **CM locus?**  Only rows 30--33 are forced onto a CM point, \(j=0\).  The catalogue label `-_S3_CM` is the imaginary quadratic resolvent of the cubic discriminant, not the elliptic curve's endomorphism ring.  Most rows in that bin are not CM points on \(X(1)\).
- **\(|j|\)-level sets?**  The R1.1 statistic shows a strong monotone correlation with \(\log|j|\), but \(|j|=c\) is a real-analytic contour, not an algebraic modular subvariety of \(X(1)\), and it does not canonically produce exactly three bins.
- **\(X_0(N)\) substratum?**  \(X_0(N)\) classifies elliptic curves plus a cyclic subgroup of order \(N\).  Forgetting the subgroup maps onto \(X(1)\); therefore a single \(X_0(N)\) does not partition the j-line unless extra arithmetic data are imposed.  The SIARC bins contain Galois/resolvent information not visible in the complex moduli point alone.

Thus H5's classification is: **not modular-geometric**, with a genuine CM subcell at \(j=0\).

## Lemniscatic prediction

The lemniscatic point is \(\tau=i\), \(j=1728\).  For a monic cubic it is equivalent to the depressed-cubic parameter \(Q=0\), i.e.
\[
2p^3-9pq+27r=0.
\]
No irreducible row in the 50-family catalogue satisfies it.  For quartics, using the stated SIARC formula \(j=6912 I^3/(4I^3-J^2)\), \(j=1728\) corresponds to \(J=0\).  I therefore predict zero lemniscatic occupants in the current d=4/Q1 catalogue window, matching the cubic catalogue; in a much wider enumeration it is a sparse Diophantine condition rather than an impossibility.  If a d=4 lemniscatic family is eventually found, it should not by itself imply the d=3 equianharmonic universality.

## Recommended X(1) visualization

Plot the standard fundamental domain with boundary arcs, mark \(\rho\) and \(i\), place every \(\tau_b\) using either AGM periods or inverse-j evaluation, color by SIARC trichotomy bin, and overlay thin contours of \(\log(|j|+1)\).  Use distinct glyphs for rows 30--33.  The diagnostic question is whether colors form geometric regions in \(\mathcal F\); H5 predicts they will not, except for the isolated \(j=0\) cluster.
