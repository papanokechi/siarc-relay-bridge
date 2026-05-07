# Phase C — Path α vs Path β cross-check

**Session:** 071 M6-CC-R1-CLOSURE-PREFLIGHT-069R1
**Phase:** C
**Status:** **N/A — neither path closed** → verdict path NO_GO_SUBSTRATE_INSUFFICIENT
**Method:** documentation of envelope C.1 cross-check semantics, branch selection (no-cross-check branch), and verdict-band ladder mapping.

---

## §1 — cross-check semantics NOTE (per envelope STEP C.1, QA BLOCKING #4)

The envelope STEP C.1 cross-check semantics NOTE states:

> "the Phase C residual ρ measures consistency of the SHARED pushforward map M = Φ_symp ∘ Φ_shift ∘ Φ_resc as applied to two different starting points (α: chart-shifted KNY pre-image; β: τ-reparametrised V_quad pre-image). It does NOT constitute independent verification of R1 closure in the strong cohomological sense. A small ρ supports but does not prove that path α and path β have arrived at the same R1 closure; a large ρ rules out that they have. The verdict tokens are framed accordingly (GO_* = consistency-supports; NO_GO_PATH_COLLISION = consistency-refutes; neither token claims independence beyond shared-pushforward agreement)."

This NOTE is reproduced verbatim because it determines how Phase C output is read: ρ is NOT a strong-independence verifier; it is a shared-pushforward consistency check. With neither path having produced a closed-form $(a_{1}, a_{2})$ at fire time, ρ is undefined.

---

## §2 — branch selection (envelope STEP C.1)

Envelope STEP C.1 enumerates three branches:

| branch                                       | applicability                                                          |
|----------------------------------------------|------------------------------------------------------------------------|
| both A.3 and B.3 succeeded                   | compute ρ; verdict from 5-band ladder (CONSISTENT / DEGRADED / COLLISION) |
| only one of A.3 or B.3 succeeded             | document the closed path; verdict GO_PATH_ALPHA or GO_PATH_BETA        |
| **neither A.3 nor B.3 succeeded**            | **document failure modes from both paths; verdict NO_GO_SUBSTRATE_INSUFFICIENT** |

### Branch determination at fire time

| path  | A.3 / B.3 closed? | failure mode                               |
|-------|-------------------|--------------------------------------------|
| α     | NO                | A.1.5.F1 (substrate gap; chart-map absent) |
| β     | NO                | CASCADE-BLOCK from A.1.5.F1 (same chart-map gap; B.1 anti-circularity-clean; (F2)/(F3) cannot be formed) |

**Branch:** "neither A.3 nor B.3 succeeded".

---

## §3 — residual ρ status

ρ is undefined. No values of $(a_{1}', a_{2}')$ from path α or $(a_{1}'', a_{2}'')$ from path β exist at fire time.

| 5-band ladder rung                                          | threshold                | met?                |
|-------------------------------------------------------------|--------------------------|---------------------|
| GO_BOTH_PATHS_CONSISTENT                                    | ρ = 0 OR ρ < 10^{-25}    | ρ undefined; n/a    |
| GO_BOTH_PATHS_DEGRADED                                      | 10^{-25} ≤ ρ < 10^{-5}   | ρ undefined; n/a    |
| NO_GO_PATH_COLLISION                                        | ρ ≥ 10^{-5}              | ρ undefined; n/a    |
| GO_PATH_ALPHA / GO_PATH_BETA (single-path GO)               | only one closed          | n/a (neither closed) |
| **NO_GO_SUBSTRATE_INSUFFICIENT**                            | **neither closed**       | **SELECTED**        |

`HALT_071_PATH_COLLISION` not triggered (no ρ to compare against threshold).

---

## §4 — Failure-mode summary from both paths

### Path α A.1.5.F1

* Substrate search exhaustive across 058R + 069 deliverables.
* Required artefact: closed-form $f_{\alpha_{\infty}}, f_{\alpha_{0}}, f_{\beta_{\infty}}, f_{\beta_{0}}$ as functions of $(a_{0}, a_{1}, a_{2})$.
* Result: ABSENT. 058R `phase_b_canonical_map.md` L136–140 declares the conversion "is residual R1 partially closed" — i.e., the chart-map IS the open R1 itself, not a side condition of R1 closure.
* The 058R `phase_b5_affine_weyl_crosswalk.md` L88–89 expressions $\alpha = 4(1+2 a_{0}-2 a_{1}), \beta = -4(1+a_{0}-a_{1}), \gamma = 4, \delta = -4$ are P_III equation-coefficients $(\alpha, \beta, \gamma, \delta)$ in the standard Painlevé III convention; they are NOT Okamoto's four-tuple $(\alpha_{\infty}, \alpha_{0}, \beta_{\infty}, \beta_{0})$ despite sharing the symbols $\alpha, \beta$. (Surface as discrepancy entry D-A.1.5.B in `discrepancy_log.json`.)

### Path β CASCADE-BLOCK from A.1.5.F1

* B.1 anti-circularity self-check PASS (zero imports/values from path α).
* (F1) Okamoto 1987 §3 eq. (3.1) verbatim quote (≤ 30 words; 17 words measured) extracted cleanly; sympy declares the abstract definition $\sigma(t) = t \cdot d/dt \log \tau(t)$ well-formed.
* (F2) null-sum restoration on reparametrised four-tuple requires consistency-pushforward to KNY chart — same chart-map substrate gap as path α A.1.5.F1.
* (F3) Liouville-invariant pushforward consistency requires explicit $I_{\mathrm{KNY}}^{(\beta\text{-reparam})}(x; a_{0}, a_{1}, a_{2})$ — same chart-map substrate gap.
* B.3 NOT REACHED.
* Failure mode tagged CASCADE-BLOCK rather than `HALT_071_PATH_BETA_INCONSISTENT` for forensic clarity (the τ-function reparametrisation is NOT structurally inconsistent with V_quad's Liouville invariant; the substrate gap is upstream of consistency-checking).

---

## §5 — verdict-token recommendation for Phase D

Phase C selects **NO_GO_SUBSTRATE_INSUFFICIENT** for Phase D verdict-token consumption.

Per envelope STEP D.2 token-only discipline, Phase D's recommendation block is a single-sentence path-viability flag (no enumeration of 069r2 phases, halts, AEAL, verdicts, or deliverables).

End of `phase_c_cross_check.md`.
