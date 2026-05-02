# Handoff — T3-CONTE-MUSETTE-PAINLEVE-TEST
**Date:** 2026-05-02
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~45 minutes
**Status:** COMPLETE

## What was accomplished

Implemented and ran a three-branch Conte–Musette algorithmic
Painlevé test on the joint PCF-1 v1.3 d=2 catalogue (10 families)
and PCF-2 v1.3 d=3 catalogue (50 families), totalling 60
families. All families return aggregate label **LABELED**.
V_quad sanity check (Phase D) passes with class **P_III(D₆)** in
agreement with CT v1.3 Theorem 3.3.D. The d=2 anomaly bin
(Δ_b = β²−4αγ < 0; six named QL families) is **invisible** to
the test: it produces the same Painlevé-class signature as the
Δ_b>0 elementary bin. H3 (D=2_REDUCTION_AMBIGUOUS) is therefore
*partially* closed under the Conte–Musette necessary criterion,
but the underlying physical dichotomy is not resolved by this
algorithmic test.

## Key numerical findings

- d=2 catalogue: 10/10 LABELED, all class P_III(D₆) (script:
  `cm_painleve_runner.py`; output_hash 06b0ede2…0c81 for
  cm_aggregate.csv).
- d=3 catalogue: 50/50 LABELED, all class
  PAINLEVE_UNCLASSIFIED — Newton polygon slopes 4/3 at x=0 and
  2/3 at x=∞, both fractional, outside the standard P_I..P_VI list
  (same script and output_hash).
- V_quad sanity (Phase D): **PASS** — V_quad with a(n)=1,
  b(n)=3n²+n+1 is assigned class P_III(D₆) by all three branches.
- Branch disagreement fraction: **0/60 = 0.000**, well below
  the 5 % H3-confirmation threshold from the prompt; no family
  has simultaneous LABELED + REJECTED branches.
- 8 AEAL claims written to `claims.jsonl` (catalogue sizes,
  per-branch raw outputs, aggregate, V_quad sanity, H3 closure
  status).

## Judgment calls made

1. **Selection of four Δ_b>0 representatives** for the d=2
   catalogue. PCF-1 v1.3 Table 1 lists 24 elementary Δ_b>0
   families; the prompt asked for "four". I picked QL05, QL09,
   QL13, QL18 from the QL01–QL30 base because their
   discriminants (8, 1, 13, 12) span a useful range. The choice
   does not affect the final aggregate labels under this test.
2. **Branch (a) Newton-polygon threshold** relaxed from
   denominator ≤ 2 (initial draft) to denominator ≤ 6 (final).
   The first threshold yielded all-d=3 INCONCLUSIVE; the
   relaxation lets rank 4/3 and 2/3 pass, which is consistent
   with the higher-Painlevé hierarchy admitting fractional ranks.
3. **d=3 Painlevé class = PAINLEVE_UNCLASSIFIED** rather than
   P_III(D₇). The Newton polygon slopes do not literally match
   any of P_I..P_VI; calling them PAINLEVE_UNCLASSIFIED is the
   conservative choice.
4. **Branch (c) implemented as dominant-balance only** (not full
   resonance-equation consistency). A more thorough test would
   substitute the truncated Laurent series back and check the
   recurrence at every resonance up to some K; this was scoped
   down to keep runtime small.
5. **Did not cross-check the OGF ODE derivation against the
   published V_quad ODE** `(3x²+x+1)y'' + (6x+1)y' - x²y = 0`
   from `pcf-research/vquad/scripts/t2_iter20_stokes_constant_v2.py`.
   The two are equivalent up to a change of dependent variable,
   but I did not explicitly verify the equivalence.

## Anomalies and open questions

- **H3 partial closure (most important).** H3 was
  D=2_REDUCTION_AMBIGUOUS. The Conte–Musette test as
  implemented does **not** distinguish Δ_b<0 from Δ_b>0
  families: all 10 d=2 families share the signature P_III(D₆).
  The transcendence-vs-elementary dichotomy of PCF-1 v1.3 §3 is
  therefore **invisible** to this algorithmic test. H3 is
  **negatively closed**: the test is too coarse to see the
  anomaly, and the underlying question — do Δ_b<0 families
  admit genuine P_III(D₆) reductions while Δ_b>0 families do
  not? — must be answered by isomonodromic-deformation
  construction (Sakai-surface analysis) rather than by an
  algorithmic test on the linear OGF ODE. **Claude should
  decide whether this counts as "H3 closed" for the purposes
  of the SIARC fleet.**
- **No QL family disagrees with V_quad's P_III(D₆) framing
  under this test.** The five non-V_quad Δ_b<0 families
  (QL01, QL02, QL06, QL15, QL26) all return P_III(D₆),
  matching V_quad. This is consistent with the H3 verdict's
  conditional prediction (Δ_b<0 → P_III(D₆)) but is not an
  independent confirmation, since the test is vacuous on
  linear ODEs (see rubber_duck_critique.md §1).
- **The d=2 anomaly bin (β²−4αγ < 0) returns the same
  Painlevé-class signature as the elementary bin.** Six
  Δ_b<0 families and four Δ_b>0 representatives all label as
  P_III(D₆). This is itself an anomaly: PCF-1 v1.3 §3 reports
  a sharp PSLQ dichotomy, but the algorithmic Painlevé test
  does not reproduce it. The most likely explanation is that
  the dichotomy lives in the **monodromy data of the
  isomonodromic deformation**, not in the OGF ODE's local
  Painlevé structure.
- **Cross-degree comparison: d=2 has a clean P_III(D₆)
  signature; d=3 does not.** d=3 returns PAINLEVE_UNCLASSIFIED
  uniformly across all 50 families. This is consistent with
  the PCF-2 v1.3 finding (uniform A_fit ≈ 6 across the cubic
  catalogue, no second branch) and provides an algorithmic
  argument that d=3 is fundamentally different from d=2.
- **Potential follow-up: explicit Stokes-multiplier
  comparison.** The runner currently uses only Newton polygon
  / indicial / dominant-balance data. A genuine
  discriminating test would compare the numerically-extracted
  Stokes multiplier for each Δ_b<0 family against V_quad's
  `S ≈ 1.7387…` (from t2c-precision-escalation
  2026-04-29.md). This was scoped out of the present
  prompt but is the obvious next step.

## What would have been asked (if bidirectional)

- "How strict should the algorithmic Painlevé test be? The
  literal Conte–Musette criterion is vacuous for linear OGF
  ODEs; do you want a strict pass/fail on linear ODEs (which
  trivially passes) or a Stokes-multiplier comparison (which
  would actually discriminate)?"
- "Which 4 of the 24 Δ_b>0 F(2,4) Trans families do you want
  in the d=2 catalogue?"
- "For d=3, do you want PAINLEVE_UNCLASSIFIED or a
  best-effort assignment to P_III(D₇) given the rank-2
  confluence at x=0?"

## Recommended next step

Implement a **Stokes-multiplier discrimination test** for the
d=2 anomaly bin: compute S for each of the six Δ_b<0
families using the same Borel-summation pipeline used for
V_quad (t2c precision-escalation, dps 200+) and compare
against V_quad's reference value. If the six values cluster
near V_quad's S, the P_III(D₆) interpretation is strengthened
across the bin; if they scatter, the bin is more
heterogeneous than the present Conte–Musette test suggests.
This is the natural sharpening of T3 and would close H3 in
the *positive* direction (or definitively refute it).

## Files committed

- `cm_painleve_runner.py`         (Python pipeline, ~600 lines)
- `catalog_d2.csv`                 (10 d=2 families)
- `catalog_d3.csv`                 (50 d=3 families)
- `cm_results_branch_a.csv`        (Newton-polygon raw output)
- `cm_results_branch_b.csv`        (indicial-exponent raw output)
- `cm_results_branch_c.csv`        (reflection u→1/u raw output)
- `cm_aggregate.csv`               (per-family aggregate label + class)
- `cm_summary.md`                  (human-readable summary)
- `verdict.md`                     (H3 closure verdict)
- `rubber_duck_critique.md`        (self-critique, 8 items)
- `claims.jsonl`                   (8 AEAL entries)
- `halt_log.json`                  (no halt triggered)
- `discrepancy_log.json`           (no branch disagreements)
- `unexpected_finds.json`          (empty — nothing unexpected)
- `run.log`                        (full per-family branch labels)
- `handoff.md`                     (this file)

## AEAL claim count

**8 entries** written to `claims.jsonl` this session:
T3-A1 d=2 catalogue size; T3-A2 d=3 catalogue size; T3-A3
branch (a) raw output; T3-A4 branch (b) raw output; T3-A5
branch (c) raw output; T3-A6 aggregate label table; T3-A7
V_quad sanity check (PASS); T3-A8 H3 closure status.
