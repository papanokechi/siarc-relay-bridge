# Q2 — Post-1933 descendants: synthesis matrix (prose)

**Task:** T1-BIRKHOFF-TRJITZINSKY-LITREVIEW, Phase 1
**Date:** 2026-05-02
**Companion file:** `descendants_synthesis_matrix.tsv` (one row per
author / line, machine-readable).
**Scope:** One paragraph per cited author / line, plus a closing
"what's still open" paragraph that feeds Q3.

The eight rows below correspond to the eight items in the relay
prompt. Where the prompt's metadata disagrees with what the agent
could verify (e.g. a year/volume mismatch), the discrepancy is
flagged here and logged in `unexpected_finds.json`.

---

## (i) Birkhoff 1911 — "General theory of linear difference equations"

Trans. Amer. Math. Soc. **12** (1911), 243–284. *[Discrepancy
flag: the relay prompt cites this as "Birkhoff 1930"; volume 12
of Trans. AMS corresponds to 1911. Logged as D-01 in
`unexpected_finds.json`.]*

This is the **predecessor** that B–T 1933 inherits and
generalises. Birkhoff 1911 establishes the Newton-polygon
stratification of linear difference equations at the irregular
singularity $x = \infty$ for the **integer-rank** case (single
slope $\sigma \in \mathbb{Z}_{\ge 0}$), and gives formal-series
existence in modern notation
$\widehat y_j(x) = \exp(P_j(x)) x^{\rho_j} \widehat S_j(x^{-1})$.
Rigour tier: **theorem**. The gap that B–T 1933 addresses is the
**fractional-rank** case (slopes $p/q$, $q > 1$); Birkhoff 1911
does not handle this. Gap still open after Birkhoff 1911:
fractional-rank, sectorial-analytic existence, Borel summability,
Stokes-multiplier rigidity beyond formal level. SIARC use:
foundational; should be cited explicitly under its correct year
(1911) in any future Phase-2 attempt at B4.

## (ii) Adams (C. R.) 1928 — "On the irregular cases of the linear ordinary difference equation"

Trans. Amer. Math. Soc. **30** (1928), no. 3, pp. 507–541.

This is the **second-order parallel** to Birkhoff 1911 that B–T
1933 explicitly builds on. Adams 1928 provides a complete
formal-series treatment of the second-order irregular linear
difference equation, covering the cases where Birkhoff 1911's
generic argument breaks down (resonant / repeated-root). Rigour
tier: **theorem**. Gap addressed: explicit closed-form
formal-series for $n = 2$, including log-corrected resonant
cases. Gap still open after Adams 1928: extension to arbitrary
order $n$, fractional-rank, all analytic content. SIARC use: the
SIARC PCF stratum is the order-$n = 2$ case with polynomial
coefficients of degree $\le d$; Adams 1928 is therefore **the
most directly applicable classical reference** for any rigorous
Phase-2 attempt at B4 in the cubic and quartic cases (the only
cases at which B4 is currently empirically supported).
Adams 1928 should be cited alongside B–T 1933 in any future
SIARC paper invoking "Birkhoff–Trjitzinsky theory" at $n = 2$.

## (iii) Birkhoff & Trjitzinsky 1933 — "Analytic Theory of Singular Difference Equations"

Acta Mathematica **60** (1933), 1–89.

The **central reference** of T1. Establishes the formal-series
existence (Thm 1) and formal classification (Thm 2) for linear
difference operators of arbitrary order $n$ with rational
(or meromorphic-at-$\infty$) coefficients, including the
fractional-rank cases left open by Birkhoff 1911. Rigour tier:
**theorem (formal level only)**. Gap addressed: fractional-rank
formal-series existence; complete formal classification by
Stokes data $(P_j, \rho_j, \widehat S_j)$. Gap still open after
B–T 1933: Borel summability; sectorial-analytic existence
(formal-to-analytic upgrade); Stokes-multiplier rigidity beyond
the formal level; the polynomial-coefficient sub-case
specialisation; the SIARC arithmetic-locus / modular layer.
SIARC use: every umbrella v2.0 / PCF-2 v1.3 invocation of
"Birkhoff–Trjitzinsky" should be re-read with the **caveat**
that B–T 1933 establishes formal but not analytic content; the
analytic upgrade is post-1933. This is the **single most
important re-framing** that Phase 1 surfaces.

## (iv) Turrittin 1955 — "Convergent solutions of ordinary linear homogeneous difference equations in the neighborhood of an irregular singular point"

Acta Mathematica **93** (1955), 27–66.

The **first rigorous convergent-solution theorem** in the
irregular-difference-equation case. Establishes that the formal
series of B–T 1933 in the **regular-singular** stratum (single
integer slope, non-resonant) is the asymptotic expansion of a
genuine analytic solution on a sector, and that the
formal-to-analytic correspondence is rigid up to Stokes
multipliers. Rigour tier: **theorem**. Gap addressed: the
formal-to-analytic upgrade left open by B–T 1933 in the
regular-singular case. Gap still open after Turrittin 1955:
extension to slopes that produce divergent formal series
(this is the irregular-divergent case, Borel-summability
content of Immink 1984+); fractional-rank multisummability
(Braaksma 1991+). SIARC use: directly underwrites the
**upper bound** $\psi_{\mathrm{upper}}(d)$ in Q3's gap
proposition; should be cited in PCF-2 v1.3 §B4 as the rigorous
version of "convergent" for the regular-singular Newton-polygon
case (which the SIARC PCF stratum at generic $d$ inhabits).

## (v) Wasow 1965 — "Asymptotic Expansions for Ordinary Differential Equations"

Wiley/Interscience, 1965. Chapter X covers the difference-equation
analogue.

The **canonical secondary treatment** of B–T 1933 in the modern
ODE-asymptotics language. Wasow 1965 §X.2 reformulates B–T 1933,
Theorem 1 in WKB / Birkhoff-matrix notation; §X.3 gives the
**polynomial-coefficient refinement** (the case where the $p_k$
of the difference operator are polynomials, not merely rational).
Rigour tier: **theorem (textbook synthesis of Birkhoff 1911,
Adams 1928, B–T 1933, Turrittin 1955)**. Gap addressed:
modern-notation reformulation of B–T 1933; explicit
polynomial-coefficient bounds. Gap still open after Wasow 1965:
multisummability framework (post-1990); resurgence; SIARC
arithmetic content. SIARC use: Wasow 1965 §X.3 is **the
literature anchor for the upper-bound expression
$\psi_{\mathrm{upper}}(d)$** in Q3; should be cited as the
canonical secondary reference whenever PCF-2 v1.3 names
"Birkhoff–Trjitzinsky theory" without quoting B–T 1933 directly.

## (vi) Immink 1984/1991+ — "Asymptotics of Analytic Difference Equations"

Lecture Notes in Mathematics **1085**, Springer-Verlag, 1984
(monograph). Subsequent papers in Compositio Mathematica and
elsewhere on Borel summability of difference-equation formal
series. *[Discrepancy flag: the relay prompt cites this as
"Immink 1991+ … LNM 1085"; LNM 1085 is the 1984 monograph, not
1991. The 1991+ Compositio papers refine the LNM monograph.
Logged as D-02 in `unexpected_finds.json`.]*

Establishes **Borel summability** of formal-series solutions of
linear meromorphic difference equations in the **rank-1
irregular** case. This is the **first rigorous formal-to-analytic
upgrade** in the irregular-divergent regime, and the result that
upgrades B–T 1933's formal series to a genuine sectorial
asymptotic. Rigour tier: **theorem**. Gap addressed: Borel
summability of B–T's formal series in rank 1; sectorial-analytic
existence in the irregular-divergent case. Gap still open after
Immink: rank > 1 / fractional-rank multisummability (Braaksma);
resurgence-theoretic alien-derivative content (Costin / Écalle).
SIARC use: directly underwrites the formal-to-analytic upgrade
required by SIARC B4 at $d \ge 3$ in the regular-singular
Newton-polygon case; should be cited in any Phase-2 proof
attempt as the **analytic upgrade** of B–T 1933 needed for the
SIARC normalisation to match a rigorous theorem.

## (vii) Braaksma 1991/1992 — "Multisummability of formal power series solutions of nonlinear meromorphic differential equations"

J. Differential Equations **92** (1991), 45–75 ("Multisummability
and Stokes multipliers of linear meromorphic differential
equations"). Annales de l'Institut Fourier **42** (1992), 517–540
("Multisummability of formal power series solutions of nonlinear
meromorphic differential equations"). *[Discrepancy flag: the
relay prompt cites Compositio Math 100; the closest Braaksma
paper to that description is the 1992 Ann. Inst. Fourier; the
agent could not confirm a Compositio Math 100 paper by Braaksma
on this topic. Logged as D-03 in `unexpected_finds.json`.]*

Establishes the **multisummability framework**: when the
Newton polygon has multiple slopes (multi-rank / fractional-rank
case), the formal series is multisummable in the sense of
Écalle, with a precise Borel-Laplace iterate associated to each
slope. Rigour tier: **theorem**. Gap addressed: the
fractional-rank / multi-slope analytic gap left open by B–T
1933 and Immink 1984. Gap still open after Braaksma:
resurgence-theoretic alien-derivative content (handed to Costin /
Écalle / Sauzin). SIARC use: relevant only at SIARC arithmetic
loci where the Newton polygon degenerates; for the bulk of
the SIARC PCF stratum at generic $b$ the rank-1 / regular-singular
case suffices and Immink + Wasow are the operative references.

## (viii) Costin 1998+ — "Asymptotics and Borel Summability" + Duke / IMRN papers

O. Costin, "On Borel summation and Stokes phenomena for rank-1
nonlinear systems of ordinary differential equations", Duke
Mathematical Journal **93** (1998), 289–344. O. Costin,
*Asymptotics and Borel Summability*, CRC Press, 2008.

Establishes the **resurgence framework with median half-Stokes
prescription**: the Stokes coefficient at a Borel-plane
singularity is computed as the alien derivative amplitude, and
the half-Stokes ambiguity is fixed by median summation. Rigour
tier: **theorem (Duke 1998 + book 2008)**. Gap addressed: the
resurgence-theoretic content beyond multisummability (alien
derivatives, generic-Stokes-data classification). Gap still
open: non-rank-1 generalisations need Loday-Richaud / Sauzin
extension. SIARC use: cited by channel theory v1.3 §3.5 as the
foundation of `op:cc-median-resurgence-execute`; **orthogonal to
the bulk of T1's B4 question**, but relevant to
`op:cc-formal-borel` reframe and to Theory-Fleet H4's
`MEDIAN_RESURGENCE_GIVES_30+_DIGITS` prediction. Costin's
median prescription is the rigorous backbone of H4.

## Loday-Richaud 2016 — "Divergent Series, Summability and Resurgence II"

Lecture Notes in Mathematics **2154**, Springer, 2016
(textbook synthesis).

Provides the **modern unified textbook treatment** of
multisummability + resurgence for ODE and difference equations.
Rigour tier: **textbook synthesis (theorem-grade)**. Gap
addressed: scattered Braaksma / Costin / Écalle results unified
in a single volume with explicit difference-equation chapter.
SIARC use: canonical modern reference; should replace ad-hoc
citations to multiple primary papers in any future SIARC
program-paper bibliography.

---

## What's still open after this cohort (feeds into Q3)

After the eight-author cohort above, the **rigorous** content
relevant to SIARC's PCF stratum at $d \ge 3$ stands as follows:

1. **Formal-Newton-polygon slope** of the SIARC three-term
   recurrence with polynomial coefficients of degree $\le d$ is
   well-understood (B–T 1933, Wasow 1965 §X.3); the formal
   characteristic exponents and the Newton-polygon slope
   structure are computable in closed form.
2. **Sectorial-analytic existence** of solutions matching the
   formal series in the regular-singular Newton-polygon case is
   covered by Turrittin 1955 / Immink 1984; the formal-to-analytic
   upgrade in the bulk of the SIARC stratum is therefore rigorous.
3. **The translation from formal-Newton-polygon slope to
   $A_{\mathrm{PCF}}(b)$** in the SIARC normalisation is
   **NOT explicitly established by any of the eight authors**.
   This is the SIARC-specific specialisation gap. The
   translation requires:
   * (a) writing the SIARC PCF approximant error
     $\delta_n(b) = \mathrm{Pcf}(1, b)_n - \lim$ as a ratio of
     two sectorial-analytic solutions of the underlying B–T
     three-term recurrence;
   * (b) showing the ratio's asymptotic exponent in
     $-A n \log n + \alpha n - \beta \log n + \gamma$ form
     equals the difference of the two formal Newton-polygon
     characteristic exponents in the SIARC normalisation;
   * (c) verifying non-resonance / non-degeneracy at all
     $b$ in the irreducible-non-singular SIARC stratum.

Steps (a)–(b) are **plausibly** handled by a combined
Wasow §X.3 + Immink 1984 argument; step (c) requires an
arithmetic argument on the discriminant axis $\Delta_d(b)$ that
is **not** in the post-1933 literature consulted in Phase 1.

This is **the gap proposition** of Q3.

## Caveats on this synthesis

* The agent did not directly read B–T 1933 or any of the eight
  primary papers; the synthesis is from the secondary sources
  listed in `bt1933_theorem_extraction.md`. Where a precise
  theorem statement matters, the corresponding row of the .tsv
  should be re-verified by the operator against the primary
  source via institutional library access.
* The 1991+ Compositio Math citation in the relay prompt for
  Braaksma did not match any paper the agent could verify;
  the closest match (Ann. Inst. Fourier 42 (1992)) is used
  instead, with the discrepancy logged.
* H1's `B4_PROVED_AT_d≥3_RESIDUE_AT_d=2` verdict label
  conflicts with the Phase-1 reading: B–T 1933 plus its
  descendants **predict / are consistent with** $A = 2d$ at
  $d \ge 3$, but do **not** rigorously establish it without the
  SIARC-specialisation argument (a)–(c) above. Logged as
  inconsistency D-04 in `unexpected_finds.json`.
