# H2 — Eisenstein E4 / CM-period structure behind the R1.1 cubic j-split

**Status:** `LITERATURE_INACCESSIBLE_PARTIAL`. This is theory-only: no code or numerical recomputation was run. The modular-form answer below is usable as a provisional H2 handoff, but the original Chowla--Selberg 1967 De Gruyter page reported “requires authentication,” EuDML returned 403, the OUP/IMRN Yu item was not accessible, and one Darmon--Vonk Project Euclid page was blocked by Incapsula. I therefore do **not** claim theorem-number-level verification for the paywalled/blocked sources.

## 1. Period map for each nonsingular cubic family

For every SIARC cubic family with nonsingular curve
\[
E_b: y^2=b(x),\qquad b(x)=a_3x^3+a_2x^2+a_1x+a_0,
\]
let \(\Delta_b\ne0\). The required period coordinate is the isomorphism class of \(E_b(\mathbb C)\). Concretely:

1. Transform \(E_b\) by an affine change of variables and differential-preserving scaling to
   \[
   Y^2=4X^3-g_2X-g_3.
   \]
   Equivalently use the usual invariants \(c_4,c_6,\Delta_E\); the scale of \(b\) changes the period lattice scale but not \(\tau\).
2. Choose a symplectic basis \((\gamma_1,\gamma_2)\) of \(H_1(E_b,\mathbb Z)\) and periods
   \[
   \omega_i=\int_{\gamma_i}\frac{dX}{Y},\qquad \operatorname{Im}(\omega_2/\omega_1)>0.
   \]
3. Put \(\tau_b=\omega_2/\omega_1\), then reduce it by \(SL_2(\mathbb Z)\) to the standard fundamental domain
   \[
   \mathcal F=\{\tau\in\mathbb H: |\operatorname{Re}\tau|\le 1/2,
   |\tau|\ge1\},
   \]
   with a fixed boundary convention. This gives the canonical representative in \(\mathbb H/SL_2(\mathbb Z)\).

In the real-root Legendre normalization, one may equivalently compute a cross-ratio \(\lambda\) of the three roots and use \(\tau=iK(1-\lambda)/K(\lambda)\), followed by the same fundamental-domain reduction. The invariant check is
\[
j(E_b)=j(\tau_b)=1728\frac{g_2^3}{g_2^3-27g_3^2}=\frac{c_4^3}{\Delta_E}.
\]
This is the explicit recipe for all 50 nonsingular cubic families; the family list only supplies the coefficients \(a_i\).

## 2. Modular-form rewriting of the R1.1 observation

The classical full-level modular-form structure is rigid. Diamond--Shurman, Chapter 1 and Chapter 4 (§§4.2, 4.4--4.5), and Zagier's *Elliptic Modular Forms and Their Applications* state the standard identities
\[
M_*(SL_2(\mathbb Z))=\mathbb C[E_4,E_6],\qquad
\Delta(\tau)=\frac{E_4(\tau)^3-E_6(\tau)^2}{1728}=\eta(\tau)^{24},
\]
\[
j(\tau)=\frac{E_4(\tau)^3}{\Delta(\tau)}
=1728\frac{E_4(\tau)^3}{E_4(\tau)^3-E_6(\tau)^2}.
\]
Here \(\Delta\) has no zero on \(\mathbb H\). Therefore:

- \(j=0\) if and only if \(E_4=0\), i.e. \(\tau\) is the equianharmonic elliptic point \(\rho=e^{2\pi i/3}\) up to modular equivalence.
- \(j=1728\) if and only if \(E_6=0\), i.e. \(\tau=i\) up to modular equivalence.
- In Petersson-invariant logarithmic form,
  \[
  \log|j(\tau)|=3\log\|E_4(\tau)\|-\log\|\Delta(\tau)\|+O(1),
  \]
  because the powers of \(\operatorname{Im}\tau\) cancel in the ratio.

Thus R1.1's empirical discriminator is not a raw weight-4 modular form. The natural modular object is the **weight-zero Eisenstein/cusp ratio**
\[
J_4(\tau)=\frac{E_4(\tau)^3}{\Delta(\tau)}=\frac{E_4(\tau)^3}{\eta(\tau)^{24}}=j(\tau).
\]
Locally near the equianharmonic point, however, the reason the split is visible is the simple zero of \(E_4\). The observed independence from the algebraic cubic discriminant \(\log|\Delta_3|\) is consistent with this: \(\Delta(\tau)=\eta^{24}\) is a modular cusp form/metric factor on \(X(1)\), not the polynomial discriminant of the displayed cubic model.

A literal asymptotic law \(A-2d=C\log|j|\) cannot be correct at exact \(j=0\), since \(\log|j|=-\infty\). The better reading is that finite-window or subleading WKB leakage ranks the families by the modular height \(J_4\), while the true leading exponential coefficient remains the universal \(2d\) at the equianharmonic CM point.

## 3. CM periods: what the accessible literature supports

Silverman's *Advanced Topics*, especially the complex multiplication chapter, gives the CM framework: CM \(j\)-values are algebraic singular moduli and CM periods are exceptional transcendental quantities. Chowla--Selberg expresses products of CM eta-values/periods in terms of Gamma-products. The original 1967 paper is bibliographically clear (J. reine angew. Math. 227, 86--110, DOI 10.1515/crll.1967.227.86) but was not accessible here; the open 1949 PNAS announcement, the Wikipedia formula page, and Gross/Kaneko-style expositions support the form
\[
\sum_{[\mathfrak a]}\log\left(\sqrt{\operatorname{Im}\tau_{\mathfrak a}}|\eta(\tau_{\mathfrak a})|^2\right)
=\text{explicit Gamma-product determined by the imaginary quadratic discriminant}.
\]
For \(D=-3\) (equianharmonic, \(j=0\)) this specializes, up to algebraic and \(\pi\)-power factors fixed by normalization, to Gamma-values at thirds such as \(\Gamma(1/3)\). For \(D=-4\) (lemniscatic, \(j=1728\)) it specializes to Gamma-values at quarters such as \(\Gamma(1/4)\).

Nesterenko's 1996 MathNet page verifies the broad transcendence setting: fields generated by modular values and derivatives have large transcendence degree away from the CM exceptions. Stark's conjectures, in Tate's formulation, place special derivatives of Artin \(L\)-functions in logarithmic-unit/regulator form; these are conceptually adjacent to Chowla--Selberg/CM-period formulas but do not themselves determine the SIARC coefficient \(A\). Recent Darmon--Vonk and Darmon--Pozzi--Vonk papers concern real-multiplication analogues of singular moduli and cocycles. They are useful warning signs that RM analogues are subtler, but H2's cubic observation is classical CM/modular-curve material.

The requested Yu CM-period theorem could not be pinned down from accessible official text in this run: web results conflicted between a Yu IMRN elliptic-logarithm item and a Jing Yu CM-period item, while the OUP page was 403. I therefore do not use Yu as a proof input.

## 4. Prediction for R1.1

**Candidate finer discriminator.** The best candidate is
\[
\boxed{\;j(\tau_b)=E_4(\tau_b)^3/\Delta(\tau_b)=E_4(\tau_b)^3/\eta(\tau_b)^{24}\;}
\]
with the local interpretation “the \(E_4\)-zero at the equianharmonic elliptic point drives the split.” Raw \(E_4\) is not modular-invariant by itself; use either \(j\) or Petersson-normalized ratios.

**Exact closed form at \(j=0\).** The predicted leading coefficient is
\[
\boxed{A_{\mathrm{true}}-2d=0\quad\text{at }\tau=\rho,\quad
\text{so for cubics }A_{\mathrm{true}}-6=0.}
\]
The Chowla--Selberg Gamma-product is expected in the period normalization and hence in amplitude/intercept terms such as \(\gamma\), not in the leading exponential slope \(A\). In short: **zero modulo a CM period**, not “a nonzero Gamma-product slope.” This matches the four R1.1 equianharmonic families hitting \(A=6\) to \(10^{-3}\) and the R1.3 deep-WKB replication.

**Prediction at \(j=1728\).** H2 alone does not force \(A-2d=0\) at \(\tau=i\). If an elliptic-point correction exists there, it should be controlled by the simple zero of \(E_6\) and a lemniscatic \(\Gamma(1/4)\) period in subleading constants.

**Next residual after subtracting \(\log|j|\).** First test the Petersson eta/discriminant height
\[
\log\|\Delta(\tau_b)\|=\log\big((\operatorname{Im}\tau_b)^6|\eta(\tau_b)|^{24}\big),
\]
or equivalently \(\log(\sqrt{\operatorname{Im}\tau_b}|\eta(\tau_b)|^2)\). If that does not absorb the residue, the next modular singularity is the order-2 elliptic point:
\[
\log|j(\tau_b)-1728|=2\log\|E_6(\tau_b)\|-\log\|\Delta(\tau_b)\|+O(1).
\]
This gives a concrete discriminator queue: `log|j|` first, eta/Petersson discriminant second, `E6` or `j-1728` third.

## 5. Fit to empirical anchors

- R1.1/R1.3 Spearman correlation with \(\log|j|\): explained as the weight-zero ratio \(E_4^3/\eta^{24}\), not as algebraic discriminant size.
- Equianharmonic \(j=0\) cell: explained; \(E_4(\rho)=0\) predicts the exact baseline \(A=2d=6\) in the true leading term.
- Independence from \(\log|\Delta_3|\): explained; the modular denominator is \(\eta^{24}\), not the displayed polynomial discriminant.
- d=4 sharp cross-degree failure: not fatal. H2 predicts a cubic Weierstrass moduli effect and likely a subleading/finite-fit leakage; it does not by itself promote the same sharp cell law to quartics.

Final working answer: **modular structure strongly explains the direction and the j=0 exactness, but paywalled/blocked CM-period sources prevent a full theorem-certified verdict in this run.**
