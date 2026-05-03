# arXiv classification recommendation — D2-NOTE v2.1

**Status:** advisory; final classification deferred to operator (Q31 in
relay spec).

## Recommendation

**Primary:** `math.CA` (Classical Analysis and ODEs)

**Cross-list:** `math.NT` (Number Theory)

## Rationale

The note's mathematical content is, in increasing order of weight:

1. **Borel summability of formal series at irregular singular points
   of linear ODEs / difference equations** (the load-bearing layer of
   §3 / §4): this is a `math.CA` topic. The literature anchors —
   Birkhoff 1930, Birkhoff–Trjitzinsky 1933, Wasow 1965, Costin 2008 —
   all sit in `math.CA` (asymptotic analysis, resurgence theory,
   classical ODE / difference-equation theory).

2. **Newton-polygon construction at irregular singular points** (§3.1
   Lemma 3.1, §2.1, §3 d=4): also `math.CA`. The Newton-polygon
   slope-1/d edge analysis is a classical-analysis tool; the
   correspondence with Wasow shearing exponent g_0 = 1/d is a vocabulary
   harmonisation across two `math.CA` notations.

3. **Polynomial continued fractions as objects** (§1 setup): the PCF
   formalism originates in number-theoretic and approximation-theoretic
   work (Lorentzen–Waadeland, Wimp), but the v2.1 manuscript treats
   them purely as carriers of an order-2 ODE / difference equation. The
   number-theoretic motivation (irrationality measures, Apéry-style
   constructions) is implicit in the PCF formalism but does not
   appear as a load-bearing argument in v2.1.

A submission classified primary `math.CA` cross-list `math.NT` reflects
this weighting accurately. v2's primary classification (operator's
choice) is preserved unless v2.1 changes weight; v2.1 strengthens
the `math.CA` content by adding the explicit Birkhoff–Trjitzinsky 1933
§§4–6 anchor, the Newton-polygon Lemma, and the q = (d+2)/2 derivation
— all `math.CA`.

## Alternative classifications considered

- `math-ph` (Mathematical Physics): the trans-series / Borel-summability
  framework sometimes lives in `math-ph` when the application is to
  resurgence in physics (e.g. Costin–Tanveer 2020 work on instantons).
  Not the case here: v2.1 has no physical-application discussion.
  **Rejected.**

- `math.AG` (Algebraic Geometry): irregular-singularity theory has
  cross-currents into algebraic geometry (Stokes structures, irregular
  Riemann–Hilbert). Not engaged with in v2.1.
  **Rejected.**

- `math.DS` (Dynamical Systems): difference-equation iteration is
  dynamical-systems-adjacent. v2.1 does not engage with the dynamical
  side. **Rejected.**

## Operator action (Q31)

The operator should set the arXiv primary/secondary classification
when (and if) the v2.1 PDF is submitted to arXiv. The Zenodo deposit
does not require an arXiv classification.

If v2 was submitted to arXiv with primary `math.NT` cross-list `math.CA`,
the operator may either keep that ordering for continuity or switch to
the recommendation above; both are defensible. The recommendation here
is offered as a write-up of the agent's reading of the manuscript.

## SHA-256 anchors

This recommendation references:
- `d2_note_v2_1.tex` SHA `840120e73534da8ef6a44fb977405fd2a8630219c4cf75a9acd7d8c75b388165`
