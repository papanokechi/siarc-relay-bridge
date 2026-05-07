# Phase A — Path α (chart-shift) attempt

**Session:** 071 M6-CC-R1-CLOSURE-PREFLIGHT-069R1
**Phase:** A
**Status:** **CLOSED — A.1.5.F1 (substrate gap)** → verdict path NO_GO_SUBSTRATE_INSUFFICIENT
**Method:** sympy substrate transcription + structural search of 058R + 069 deposits for the explicit KNY → Okamoto four-tuple map; degradation per envelope STEP A.1.5 Failure Mode A.1.5.F1.
**Script:** `phase_a_path_alpha.py`
**Log:** `phase_a_path_alpha.log`

---

## §1 — substrate pull (verbatim quote-or-citation)

### CT v1.3 §3.5 four-tuple at V_quad parameter point

(058R substrate via 069 `phase_d_numerical.md` §1; SHA `E98D74EBD30EB43C..`)

$$(\alpha_{\infty},\, \alpha_{0},\, \beta_{\infty},\, \beta_{0}) \;=\; \bigl(\tfrac{1}{6},\ 0,\ 0,\ -\tfrac{1}{2}\bigr).$$

### 069 sympy-verified Okamoto null-sum

(069 anomaly D2 carry-forward verbatim from 069 `handoff.md` L23 + L39; cited at 069 `phase_d_numerical.md` §1 SHA `E98D74EBD30EB43C..`)

$$\alpha_{\infty} + \alpha_{0} + \beta_{\infty} + \beta_{0} \;=\; \tfrac{1}{6} + 0 + 0 - \tfrac{1}{2} \;=\; -\tfrac{1}{3} \;\neq\; 0.$$

### KNY linear relation

(per QA REC #6 — single-policy resolution: cite via 069 `phase_d_numerical.md` §1 SHA `E98D74EBD30EB43C..` ONLY; do NOT re-extract verbatim from KNY 2017 PDF in this session)

$$a_{0} + a_{1} \;=\; 1.$$

### V_quad parameter point — PINNED form

(058R Phase A, citable via 058R `phase_a_birkhoff_match.md` SHA `413A3845F67E7166..`; H4 measurement at ≥ 108 dps per 058R `phase_a_birkhoff_match.py` SHA `7B4DD7636A3D9AD3..`)

$|C_{V}| = 8.127\,336\,795\,495\,072\,367\ldots$

V_quad scalar OGF ODE form (058R Phase A; cited):

$$3\,z^{3}\,f''(z) \;+\; 10\,z^{2}\,f'(z) \;+\; \bigl(z^{2} + 5\,z - 1\bigr)\,f(z) \;=\; 0.$$

### 058R Phase B pin

(058R `phase_b_canonical_map.md` SHA `F831F9BD58D1F306..`)

* $\Phi_{\mathrm{resc}}$: $z = \lambda\, t$ with $\lambda = c_{0}^{2}/4 = 1/3$.
* $\Phi_{\mathrm{shift}}$: $t \to t + t_{0}$ with $t_{0} = -\zeta_{*}/\lambda = -4\sqrt{3}$.

### V_quad scalar-OGF Liouville invariant (069 NEW substrate)

(069 `phase_d_numerical.md` §2; sympy-derived; cited at 069 `phase_d_numerical.py` SHA `89D9EEFC57D9FA47..`)

$$I_{V}(z) \;=\; \frac{3 z^{2} \;+\; 5 z \;-\; 3}{9\,z^{3}}.$$

This is gauge-invariant under $f \mapsto h(z)\,f$ for any non-vanishing $h$, and pins the V_quad-side normal form independently of any KNY-side parameter convention.

---

## §1.5 — KNY chart → Okamoto four-tuple map (per envelope STEP A.1.5)

### Required artefact

The envelope requires that the explicit map between the KNY 2017 §8.5.17 $(a_{0}, a_{1}, a_{2})$ chart and the Okamoto 1987 §3 four-tuple $(\alpha_{\infty}, \alpha_{0}, \beta_{\infty}, \beta_{0})$ convention be cited verbatim from 058R + 069 substrate as four equations:

$$\alpha_{\infty} \;=\; f_{\alpha_{\infty}}(a_{0}, a_{1}, a_{2}),\qquad
   \alpha_{0} \;=\; f_{\alpha_{0}}(a_{0}, a_{1}, a_{2}),$$

$$\beta_{\infty} \;=\; f_{\beta_{\infty}}(a_{0}, a_{1}, a_{2}),\qquad
   \beta_{0} \;=\; f_{\beta_{0}}(a_{0}, a_{1}, a_{2}),$$

with each $f_{\ast}$ a closed-form polynomial (or rational) expression in $(a_{0}, a_{1}, a_{2})$.

### Substrate search

Two-stage substring scan of 058R + 069 deposits performed at fire time:

**Stage 1 — bridge-wide grep on 058R deliverables** (`sessions/2026-05-06/CC-VQUAD-PIII-NORMALIZATION-MAP-RERE-FIRE/`) for any of the patterns
`alpha_inf`, `alpha_0`, `beta_inf`, `beta_0`, `α_∞`, `α_0`, `β_∞`, `β_0`, `four-tuple`, `null.sum`,
`local exponent`, `monodromy parameter`:

| file                                  | hits   | content nature                                                          |
|---------------------------------------|--------|-------------------------------------------------------------------------|
| `discrepancy_log.json`                | 5+     | D1 + D2 entries describing the OPEN map status (R1 anomaly itself)     |
| `claims.jsonl` C1                     | 1      | Anomaly D1 + D2 declaration; no closed-form $f_{\ast}$ provided        |
| `phase_b5_affine_weyl_crosswalk.md`   | 4      | Lines 88–89 quote KNY 2017 §8.5.16 P_III equation form $\alpha y^{2}+\beta+\gamma y^{3}+\delta/y$ with $\alpha = 4(1+2 a_{0} - 2 a_{1})$, $\beta = -4(1+a_{0}-a_{1})$, $\gamma = 4$, $\delta = -4$ — these are **P_III equation coefficients** $(\alpha, \beta, \gamma, \delta)$ in the standard Painlevé III convention, **NOT** Okamoto's four-tuple $(\alpha_{\infty}, \alpha_{0}, \beta_{\infty}, \beta_{0})$. Different conventions sharing the symbols $\alpha, \beta$. |
| `phase_b_canonical_map.md` L136–140   | 1      | Verbatim:<br>"(i) explicit conversion of the V_quad's CT v1.3 §3.5 4-tuple $(\alpha_{\infty}, \alpha_{0}, \beta_{\infty}, \beta_{0}) = (1/6, 0, 0, -1/2)$ to KNY $(a_{0}, a_{1}, a_{2})$ — **this is residual R1 partially closed**; the 4-tuple does NOT satisfy Okamoto's $\alpha_{\infty}+\alpha_{0}+\beta_{\infty}+\beta_{0}=0$ constraint (sums to $-1/3$)..." |

**Stage 2 — 069 deliverables grep** (`sessions/2026-05-07/CC-VQUAD-PIII-NORMALIZATION-MAP-PHASE-D-NUMERICAL/`) for `f_alpha`, `chart-map`, `chart map`, `conversion.*chart`, `a_0.*alpha`, `alpha.*a_0`, `exponent.*a_`, `a_.*exponent`:

Returns **zero hits**. 069 carries forward the four-tuple $(\alpha_{\infty}, \alpha_{0}, \beta_{\infty}, \beta_{0}) = (1/6, 0, 0, -1/2)$ as 058R-substrate input, but does NOT introduce or pin a closed-form $f_{\ast}$ map.

### Conclusion — STEP A.1.5 Failure Mode A.1.5.F1 trigger

The explicit map $f_{\alpha_{\infty}} / f_{\alpha_{0}} / f_{\beta_{\infty}} / f_{\beta_{0}}$ is **NOT present** in 058R + 069 substrate as a closed-form polynomial (or rational) expression in $(a_{0}, a_{1}, a_{2})$. What 058R substrate explicitly states is: *the conversion is residual R1, partially closed* (058R `phase_b_canonical_map.md` L136–140; SHA `F831F9BD58D1F306..`); and the four-tuple's null-sum violation is anomaly D2 carried forward unchanged.

This matches the envelope's described failure mode at STEP A.1.5:

> "Failure mode A.1.5.F1: the explicit map is NOT present in 058R + 069 substrate (agent searches and finds no closed-form expression for $f_{\alpha_{\infty}}$ / $f_{\alpha_{0}}$ / $f_{\beta_{\infty}}$ / $f_{\beta_{0}}$). This is a substrate gap → escalate to W21 LANE-1 T1-Synth analytic-guidance request. Verdict path: NO_GO_SUBSTRATE_INSUFFICIENT."

A.1.5.F1 is **TRIGGERED**.

### Surfacing as discrepancy entry

Substrate gap surfaced in `discrepancy_log.json` as entry **D-A.1.5** (NEW; non-blocking at envelope level — A.1.5.F1 is not a phase-level halt but a substrate-gap detection that produces verdict NO_GO_SUBSTRATE_INSUFFICIENT directly).

### Component-order discipline note

The KNY chart $(a_{0}, a_{1}, a_{2})$ is component-ordered per KNY 2017 §8.5.17 convention. The project-wide PCF tuple-ordering convention `[a2, a1, a0]` (LEADING-FIRST) does **NOT** apply here. This note is reproduced in `phase_a_path_alpha.py` script header.

---

## §2 — Phase A.2 chart-shift sympy derivation (DEGRADED to substrate-gap statement)

### What §2 would have computed (counterfactual; documents the pattern for W21 LANE-1)

Had the explicit four-tuple map been substrate-supported, sympy would construct the system

$$\text{(E1)}\qquad f_{\alpha_{\infty}}(a_{0}+\Delta_{0}, a_{1}+\Delta_{1}, a_{2}+\Delta_{2})
   + f_{\alpha_{0}}(\cdot)
   + f_{\beta_{\infty}}(\cdot)
   + f_{\beta_{0}}(\cdot)
   \;=\; 0$$

$$\text{(E2)}\qquad \Delta_{0} + \Delta_{1} \;=\; 0
   \quad (\text{KNY linear-relation invariance after pre-shift } a_{0}+a_{1}=1)$$

$$\text{(E3.a)}\qquad \lambda'(a_{0}+\Delta_{0}, a_{1}+\Delta_{1}, a_{2}+\Delta_{2}) \;=\; 1/3$$

$$\text{(E3.b)}\qquad t_{0}'(a_{0}+\Delta_{0}, a_{1}+\Delta_{1}, a_{2}+\Delta_{2}) \;=\; -4\sqrt{3}$$

$$\text{(E3.c)}\qquad I_{V}'(z;\, a_{0}+\Delta_{0}, a_{1}+\Delta_{1}, a_{2}+\Delta_{2})
   \;=\; \frac{3 z^{2} + 5 z - 3}{9 z^{3}}$$

and solve $\text{(E1)} \wedge \text{(E2)} \wedge \text{(E3)}$ for $\Delta = (\Delta_{0}, \Delta_{1}, \Delta_{2})$ in closed form, then extract $(a_{1}', a_{2}') = (a_{1} + \Delta_{1}, a_{2} + \Delta_{2})$ at V_quad parameter point.

### What §2 cannot compute given A.1.5.F1

(E1) is the null-sum restoration constraint. Its evaluation requires the explicit form of $f_{\alpha_{\infty}}, f_{\alpha_{0}}, f_{\beta_{\infty}}, f_{\beta_{0}}$. With A.1.5.F1 triggered, (E1) is **NOT EVALUABLE** at fire time.

(E3.a) and (E3.b) are also NOT EVALUABLE — they require explicit expressions for $\lambda'(a_{0}, a_{1}, a_{2})$ and $t_{0}'(a_{0}, a_{1}, a_{2})$, which 058R substrate pins **only at V_quad parameter point** (numerically: $\lambda = 1/3$, $t_{0} = -4\sqrt{3}$), not as functions of $(a_{0}, a_{1}, a_{2})$. (058R `phase_b_canonical_map.md` §B.2; substrate gap of secondary nature relative to A.1.5.F1.)

(E3.c) requires explicit $I_{V}'(z; a_{0}, a_{1}, a_{2})$ as a function of the chart; substrate pins it only at V_quad parameter point (069 §2).

### Per envelope: degrade (E3) to substrate-supported subset

Envelope text:
> "If 058R + 069 substrate does NOT supply explicit expressions for λ' / t_0' / I_V' as functions of (a_0, a_1, a_2), document the substrate gap in phase_a_path_alpha.md §2 and degrade (E3) to its minimal subset that IS substrate-supported. ... Do NOT fabricate the missing expressions."

Substrate-supported subset of (E3) at V_quad parameter point:

| equation | substrate-supported form |
|----------|--------------------------|
| (E3.a)   | $\lambda = 1/3$ at V_quad point (PINNED, scalar; no functional form available) |
| (E3.b)   | $t_{0} = -4\sqrt{3}$ at V_quad point (PINNED, scalar; no functional form available) |
| (E3.c)   | $I_{V}(z) = (3 z^{2} + 5 z - 3)/(9 z^{3})$ at V_quad point (PINNED, gauge-invariant; no chart-dependent form available) |

The substrate-supported subset is **scalar pinning at one point**, not invariance equations parametrised by $(a_{0}, a_{1}, a_{2})$. The system (E1) ∧ (E2) ∧ (E3) cannot be solved for $\Delta$ in closed form at fire time without the explicit chart-map.

### sympy script outputs (see `phase_a_path_alpha.py` + `.log`)

The sympy script `phase_a_path_alpha.py` produces verifiable artefacts:

* sympy-verifies the Okamoto null-sum violation: $1/6 + 0 + 0 - 1/2 = -1/3$.
* sympy-verifies KNY linear relation: from $a_{0} + a_{1} = 1$ and $(a_{0}', a_{1}') = (a_{0} + \Delta_{0}, a_{1} + \Delta_{1})$ with $a_{0}' + a_{1}' = 1$, deduce $\Delta_{0} + \Delta_{1} = 0$ (i.e. (E2) closed-form).
* sympy declares (E1) abstract (without explicit $f_{\ast}$ map): `NotImplemented` placeholder; documents the substrate-gap detection in script body.
* sympy-verifies V_quad-side Liouville invariant matches 069 substrate at V_quad parameter point: $I_{V}(z) = (3 z^{2} + 5 z - 3)/(9 z^{3})$ (re-derived from the V_quad scalar-OGF ODE coefficients $p_{V}(z) = 10/(3 z)$, $q_{V}(z) = (z^{2}+5z-1)/(3 z^{3})$ via $I_{V} = q_{V} - \frac{1}{4} p_{V}^{2} - \frac{1}{2} p_{V}'$).
* No fabricated $f_{\alpha_{\infty}}, f_{\alpha_{0}}, f_{\beta_{\infty}}, f_{\beta_{0}}$ expressions.

### Failure mode determination

| candidate failure mode                                    | trigger?  | basis                                        |
|-----------------------------------------------------------|-----------|----------------------------------------------|
| A.1.5.F1 (substrate gap; explicit map absent)             | **YES**   | substrate search exhaustive; map is residual R1 itself per 058R `phase_b_canonical_map.md` L136–140 |
| A.2.F1 (system over-determined)                           | n/a       | system not formed (A.1.5.F1 is upstream)     |
| A.2.F2 (system under-determined)                          | n/a       | system not formed (A.1.5.F1 is upstream)     |
| HALT_071_PATH_ALPHA_OVERDETERMINED (phase-level halt)     | NO        | A.1.5.F1 routes around the phase-level halt; the system is not formed at all, not over-determined |

`HALT_071_PATH_ALPHA_OVERDETERMINED` is **NOT TRIGGERED** — the obstruction is upstream of the system formation. A.1.5.F1 routes directly to verdict path NO_GO_SUBSTRATE_INSUFFICIENT (envelope STEP A.1.5).

---

## §3 — Phase A.3 (a_1, a_2) extraction (NOT REACHED)

Phase A.3 (a_1', a_2') extraction requires Phase A.2 to have produced a closed-form (or canonical-selected) $\Delta$. Given A.1.5.F1, A.2 did not form the system; A.3 is **NOT REACHED**.

Path α verdict: **NO_GO_PATH_ALPHA via A.1.5.F1 (substrate gap)** — closed without producing a closed-form $(a_{1}', a_{2}')$ at V_quad parameter point.

---

## Path α conclusion

* Substrate search exhaustive across 058R + 069 deliverables.
* Explicit four-tuple map $f_{\alpha_{\infty}} / f_{\alpha_{0}} / f_{\beta_{\infty}} / f_{\beta_{0}}$ as functions of $(a_{0}, a_{1}, a_{2})$ is **absent** from substrate; this absence IS residual R1 (not a side condition of R1 closure).
* A.1.5.F1 triggered; verdict path NO_GO_SUBSTRATE_INSUFFICIENT enabled.
* Path β STEP B.1 anti-circularity rule shares the same map dependency; substrate gap propagates to path β (documented in `phase_b_path_beta.md`).
* Phase D verdict-token recommendation cleanly aligns with NO_GO_SUBSTRATE_INSUFFICIENT.

End of `phase_a_path_alpha.md`.
