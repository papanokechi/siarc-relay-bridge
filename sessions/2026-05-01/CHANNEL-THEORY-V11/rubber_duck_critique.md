# Rubber-duck critique — channel_theory_outline v1.1 (CHANNEL-THEORY-V11)

Date: 2026-05-01
Scope: pre-Zenodo self-review of v1.1 rewrite, focused on the four
critical questions enumerated in the H1 prompt.

---

## (i) Is the universality identity ξ₀ = 2/√β₂ stated precisely enough for B1 to reference?

**Verdict: yes, with one caveat.**

Proposition 3.3.A (`prop:xi0`) states the identity in terms of:
- the operator \eqref{eq:Lf-cc}, an explicit order-2 ODE annihilating
  f(z) = Σ Q_n zⁿ;
- a Newton polygon with a single slope-1/2 edge (0,0)—(1,2) of
  multiplicity 2;
- the characteristic polynomial 1 − (β₂/4) c² and its positive root;
- the indicial exponent ρ = −3/2 − β₁/β₂ pinned by the level-1/u
  trans-series ansatz in u = √z.

The proof is sketched (5 lines) and points to the CC-PIPELINE-G
script `newton_birkhoff.py` and AEAL claims 1–4. The worked example
on V_quad with explicit lattice points {(0,0), (1,0), (1,1), (1,2),
(2,0)} makes the abstract statement concrete.

**Caveat.** "ξ₀ = leading Borel-plane singularity radius" is the
*formal-solution* notion, i.e. the magnitude of the slope-1/2
characteristic root. The Stokes constant proper (residue at the
Borel singularity, requiring a contour-integral Laplace step) is
NOT computed here. Bridge B1 references `ξ₀` as the radius, which
is sound; if a future B1 statement instead references the Stokes
constant, the present prop is necessary-not-sufficient. This is
flagged in the prompt's request for the Borel-Laplace residual
(`op:cc-formal-borel`) and is honestly disclosed in
`thm:vquad-cc`'s caveat.

The QL01/QL02 split via a₂ adds a second invariant tier without
ambiguity. B2 uses (ξ₀, ρ) up to that split; B3 uses (ξ₀, ρ, a₂, …).

## (ii) Is the V_quad recovery framing ("exact modulo Borel-Laplace") honest about the residual numerical step?

**Verdict: yes.**

Theorem 3.3.D splits explicitly:
- (i) ξ₀ = 2/√3 — exact algebraic, 200 digits, from `prop:xi0`.
- (ii) ρ = −11/6 — exact rational, 200 digits.
- (iii) connection-coefficient ratio match — *modulo Borel-Laplace
  summation*.

The prose immediately following the theorem statement spells out
that the Domb–Sykes secondary metric showed slow convergence on
K ≤ 200 in CC-PIPELINE-G (sample radii drift in the leading digits
visible in `results_vquad.json` -> `borel_sample_radii`). The proof
sketch acknowledges no closed-form Stokes-multiplier expression yet
exists.

The "exact modulo Borel-Laplace" framing is therefore not over-
claimed. The headline "V_quad recovered" is structurally accurate
(the formal singular data is the literature value, exactly); the
residual numerical step is the contour-integral Laplace summation
of the formal pair, which is what `op:cc-formal-borel` exists to
discharge.

## (iii) Is the new B1/B2/B3 tier structure better than v1.0's discriminant-driven version?

**Verdict: yes — strictly better.**

v1.0 wrote bridge identities Φ_Δ as functions of the discriminant
Δ. Two structural objections to that framing:

- The discriminant of the degree-2 polynomial b is Δ = β₁² − 4 β₂ β₀.
  This is a single algebraic invariant of the *roots* of b, but the
  CC channel sees the *operator coefficients*, of which only β₂
  determines ξ₀ (Proposition 3.3.A). The discriminant collapses
  data the channel does not collapse.
- The QL01/QL02 pair has identical (ξ₀, ρ) but distinct discriminants
  (−3 vs −4). Conversely V_quad and QL15 have different discriminants
  (−11 vs −20) but identical ξ₀ = 2/√3. So discriminant is neither
  finer nor coarser than the channel data; it is *orthogonal*.

The tier B1/B2/B3 structure parametrises bridge identities by the
number of leading invariants required, which matches what the
channel actually measures. Table `tab:bridge-tier` makes the per-
family candidacy concrete: V_quad is the B1 anchor in the trivial
sense (β₂-driven ξ₀); QL15 is a B1-reject (β₂ shared, label
mismatched); QL01/QL02 is a B2 candidate; the rest default to B3.

The remaining weakness: tier B1's "Painlevé label determined by β₂
alone" is a strong empirical claim verified on a single family, and
already partially refuted by the QL15 reject. We document this and
list `op:bridge-witness-tier` as the open problem.

## (iv) Does op:xi0-degree-d connect cleanly to PCF-2 v1.1's Conjecture B4 (A = 2d)?

**Verdict: yes, via a candidate constant.**

PCF-2 v1.1 (10.5281/zenodo.19939463) Conjecture B4 states A = 2d for
every degree-d PCF in scope, with A the leading WKB exponent of
log|δ_n| = −A n log n + …. Our `prop:wkb` gives the d = 2 case as
A = {3, 4} (split by whether a_n is constant or linear in n) —
exactly the case PCF-2 flags as `op:d2-anomaly`.

`op:xi0-degree-d` extends our Newton-polygon characteristic-root
identity to higher degree:
- d = 2: ξ₀ = 2/√β₂ (proved here).
- d = 3 conjecture: ξ₀ = 2 √2 / β₃^(1/3) (i.e. c(d) = 2 √((d−1)!)
  with d = 3 giving c(3) = 2 √2).
- d generic: ξ₀ = c(d) / β_d^(1/d) for some explicit c(d).

The candidate c(d) = 2 √((d−1)!) is sourced from CC-PIPELINE-G
handoff item UF-G2 / op:cc-degree-d (the d-dependent generalisation
flagged but not proved there). It connects to PCF-2's A = 2d
because both quantities (A and ξ₀) are leading invariants of the
formal solution at the irregular singular point of the
generating-function ODE, related by the Frobenius / WKB
correspondence. A clean degree-3 verification would simultaneously
discharge `op:xi0-degree-d` at d = 3 and produce a structural
witness for PCF-2's Conjecture B4 at d = 3.

The cross-reference is documented in:
- the abstract (closing sentence);
- `prop:wkb` post-discussion paragraph (cross-reference to PCF-2
  v1.1, op:d2-anomaly);
- `op:xi0-degree-d` problem statement (explicit B4 reference and
  candidate c(d) form).

## Other quick checks

- **Page count.** Compiled output is 12 pp, in [12, 20]. Conservative
  margin; if Zenodo upload requires a single-column reformat the
  page count will rise into the comfortable middle of the range.
- **Bibliography.** Three new entries (`siarc_pcf2_v11`,
  `siarc_cc_pipeline_f`, `siarc_cc_pipeline_g`); one existing entry
  (`siarc_pcf1_v13`) updated with the now-known DOI
  10.5281/zenodo.19937196.
- **Cross-references.** All `\Cref{...}` resolve (no "??"); `bibtex`
  reports one cosmetic warning ("empty publisher in
  sauzin2014resurgent" — pre-existing in v1.0, not regressed).
- **AI disclosure.** Updated to cite CC-PIPELINE-F (UF-1) and
  CC-PIPELINE-G (Newton polygon + Birkhoff, three universality
  findings).
- **Title.** Promoted from v1.0's "Channel structure of asymptotic
  deformations in PCF dynamics: an outline" to v1.1's "Channel theory
  for polynomial continued fractions: asymptotic channels, the
  ξ₀ = 2/√β₂ identity, and a bridge conjecture". The promotion
  highlights the new keystone identity in the title itself, which
  is appropriate for a Zenodo top-level posting.

## Blocking concerns: none.
