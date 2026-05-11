# caveats.md — Caveat / residual / boundary language templates

These are operator paste-ready into v1.5 manuscript OR Umbrella v2.3 Appendix C OR any subsequent caveat-bearing artefact. Verbatim phrasings preserved.

## M7 HARD-BRANCH-PENDING

### Long form (paragraph; for §-body or Appendix use):

> The j=0 amplitude / Chowla–Selberg closure is recorded at soft-branch tolerance: max |δ_lin| = 3.09 × 10⁻²³ at dps = 25,000 (PCF-2 v1.4 amendment, bridge `e857172`). The corresponding hard-branch tolerance |δ| < 10⁻³⁰ is **forward-pointed under Q22 path-(b)** and is **not closed** at the M7 V0 ratification cascade `7f93b9e`. Future work may refine the closure at hard-branch tolerance via extended-precision PSLQ on the 17-member deduplicated H6 Chowla–Selberg basis B19+; this is documented as residual `M7 HARD-BRANCH-PENDING` in the SIARC pipeline.

### Short form (footnote):

> M7 V0 ratification adopts the j=0 amplitude / Chowla–Selberg resolution at soft-branch tolerance only; hard-branch (|δ| < 10⁻³⁰) remains forward-pointed under Q22 path-(b). Annotation: *(SOFT-BRANCH; HARD-BRANCH-PENDING)*. Anchor: SIARC bridge SHA `7f93b9e`.

### One-liner (inline annotation):

> *(SOFT-BRANCH; HARD-BRANCH-PENDING; bridge `7f93b9e`)*

---

## M8b d≥3 caveat (for Umbrella v2.3 Appendix C iii — out-of-scope for PCF-2 v1.4 paper)

Forward-deferred to Umbrella v2.3 Appendix C iii drafting (separate work-stream slot 155-UMBRELLA-V23 fire). The slot 155 §Q5a draft remains:

### Long form (paragraph; D-156-1 V0+ vs V1 variants):

**Variant A — V0+ commitment (operator selects V0+ in D-156-1):**

> The |S_2| extraction at degree d=2 achieves laptop-feasible numerical foreclosure under the M8b V0 cascade `74c5630` (cascade 130R, cross-provider dual-witness). At d=2 the extraction is within reach of the laptop-class compute budget documented in the reproduction checklist; the foreclosure verdict is `(NUMERICAL-FORECLOSURE; d≥3-CAVEAT-CARRIED-FORWARD)`. **The d≥3 caveat remains structurally open to upward recovery**: future extended-precision or distributed-compute pipelines may extract |S_2| at d=3 and beyond, refining the M8b numerical foreclosure to a wider dimensional regime. This is documented as future-work scope, NOT as a retraction of the d=2 V0 result. Anchor: SIARC bridge SHA `74c5630`.

**Variant B — V1 commitment (operator selects V1 in D-156-1):**

> The |S_2| extraction at degree d=2 achieves laptop-feasible numerical foreclosure under the M8b V0 cascade `74c5630` (cascade 130R, cross-provider dual-witness). At d=2 the extraction is within reach of the laptop-class compute budget documented in the reproduction checklist; the foreclosure verdict is `(NUMERICAL-FORECLOSURE; d≥3-CAVEAT-CARRIED-FORWARD)`. **The d≥3 regime is documented as future-work scope**: present work does not extend to d≥3 |S_2| extraction. Anchor: SIARC bridge SHA `74c5630`.

### Short form (footnote, D-156-1-agnostic):

> M8b V0 ratification scopes the |S_2| numerical foreclosure to d=2 laptop-feasible regime; d≥3 is carried forward as future-work scope. Annotation: *(NUMERICAL-FORECLOSURE; d≥3-CAVEAT-CARRIED-FORWARD)*. Anchor: SIARC bridge SHA `74c5630`.

### One-liner (inline annotation):

> *(NUMERICAL-FORECLOSURE; d≥3-CAVEAT-CARRIED-FORWARD; bridge `74c5630`)*

---

## M10 sorry-discharge work-stream — SAFE phrasing (D-153-3 compliant)

### Recommended template:

> The M10 axis covers Lean formalization of the SIARC cascade discipline; sorry-discharge work continues as a separate engineering work-stream tracked under the SIARC pipeline. M10 is **not** a mathematical-content closure axis. A status report on the Lean formalization work-stream is scheduled for 2026-08-02.

### Forward-reference template (2026-08-02 status report):

> The current M10 Lean formalization sorry-discharge state is documented in the SIARC pipeline status logs. A consolidated status report is scheduled for 2026-08-02 covering: (a) sorries-discharged-since-last-status, (b) Mathlib dependency upgrades (cf. slot 148.B / UF-168-1 toolchain alignment work-stream), (c) any axiom modifications, (d) any sorries reopened due to API breakage. The 2026-08-02 status report does not constitute a math-content closure claim; it is a formalization-state attestation.

### UNSAFE phrasings — DO NOT USE:

- ❌ "M10 closed." — re-characterizes tooling state as math-content closure.
- ❌ "M10 V0 ratification." — implies math-content cascade where none exists.
- ❌ "M10 sorries discharged." — when not all sorries are actually discharged, this is false; when they are, the phrasing should be "Lean formalization of axes M_k for k in {…} complete pending peer review" without invoking the M10 label.
- ❌ "M10 axis closed alongside M4/M7/M8a/M8b." — conflates formalization tier with math content tier; D-153-3 violation.

---

## M2 Q22 final-disposition note

### Collapse-to-no-op template (low-stakes residual; recommended):

> Q22 (the j=0 amplitude hard-branch stretch goal) is **path-(b) forward-pointed** under the M7 V0 ratification cascade `7f93b9e`. The Q22 final-disposition track is held open pending future hard-branch refinement; no math-content disposition is required at v1.4 or v1.5 release time. If hard-branch refinement is achieved, Q22 status updates to "closed in hard branch" via a future cascade; absent that, Q22 remains forward-pointed as a documented residual.

### One-liner:

> *(Q22 path-(b) forward-pointed; bridge `7f93b9e`)*

---

## Reproduction Appendix template (per S153 Q4(4c) mitigation)

```
Reproducibility scope statement (M7 V0 cascade 7f93b9e):

  Numerical scripts location:
    - pcf-research/T25D-RETRY-13PARAM/ (Prompt 014 PASS_A_EQ_6_ONLY closure)
    - Bridge SHA e857172 (2026-05-02): T25D-RETRY-13PARAM substrate
    - Bridge SHA 7f93b9e (2026-05-09): M7 V0 ratification cascade record

  Parameter ranges:
    - dps (mpmath digits): 25,000
    - N (truncation index): N ≤ 1200
    - LIN parameter count: 11 (j=0 amplitude refit)
    - K_FIT (Padé order): 7
    - PSLQ basis: 17-member deduplicated H6 Chowla–Selberg basis B19+
      (NOT literal 18-basis; Γ-reflection identity deduplicates
      {√3, Γ(1/3)Γ(2/3)/(2π)} pair per Q23 hygiene)
    - PSLQ maxcoeff: 10⁵⁰
    - PSLQ tolerance: 10⁻⁴⁰

  V0 anchor values (DO NOT MODIFY; cite verbatim):
    - max |δ_lin|: 3.09 × 10⁻²³  (across Q_30..Q_33)
    - PSLQ verdict: no Γ(1/3) relation in any of the 4 j=0 families
    - Hard-branch stretch goal: |δ| < 10⁻³⁰ (NOT CLOSED; forward-pointed)

  M4 V0 anchor values (cross-reference; cited verbatim from cascade 106 bridge 5f9db69):
    [Refer to cascade 106 bridge record at 5f9db69 for M4 V0 numerical anchors;
    cited as cross-reference, not modified in PCF-2 scope.]

  Software / library versions:
    - Python: 3.11+ (per ANTI-CONFLATION rule)
    - mpmath: 1.3.0+
    - SymPy: 1.12+
    - Hardware: laptop-class (M8b d=2 numerical foreclosure scope per cascade 130R)

  Reproducibility scope statement:
    Results in this paper are reproducible at the laptop-feasible
    dimensional regime (d=2 for M8b-style numerical foreclosures;
    d=3 for the cubic-discriminant program; d=4 deep-WKB null
    documented as rule-out). Beyond-laptop-class compute (e.g.,
    d≥3 |S_2| extraction) is documented as future-work scope
    and is NOT a retraction of any V0 result.
```

---

## Annotation glossary (for future caveat reuse)

| Annotation | Meaning | Anchor |
|---|---|---|
| (SOFT-BRANCH; HARD-BRANCH-PENDING) | Soft-branch closure at the documented dps; hard-branch goal is forward-pointed; not closed | M7 V0 cascade `7f93b9e` |
| (NUMERICAL-FORECLOSURE; d≥3-CAVEAT-CARRIED-FORWARD) | Numerical foreclosure at d=2 (laptop-feasible); d≥3 is future-work | M8b V0 cascade `74c5630` |
| (ALG-TEST-SCALE; STOKES-DICHOTOMY-DELEGATED-TO-M8B) | M8a catalogue labelling complete; Stokes dichotomy delegated to M8b | M8a V0 cascade `cb429e1` |
| (Q22 path-(b) forward-pointed) | Hard-branch stretch goal active; no disposition required | M7 V0 cascade `7f93b9e` |
