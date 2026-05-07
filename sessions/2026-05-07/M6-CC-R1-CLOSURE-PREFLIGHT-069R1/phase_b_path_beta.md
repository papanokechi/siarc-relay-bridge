# Phase B — Path β (Okamoto 1987 §3 τ-function reparametrisation) attempt

**Session:** 071 M6-CC-R1-CLOSURE-PREFLIGHT-069R1
**Phase:** B
**Status:** **CLOSED — B.1 cascade-block from A.1.5.F1** → verdict path NO_GO_SUBSTRATE_INSUFFICIENT
**Method:** sympy substrate transcription + Okamoto 1987 §3 eq. (3.1) τ-function-definition extraction (verbatim ≤ 30 words) + structural detection that path β depends on the same KNY chart-map substrate as path α via STEP A.1.5; (F2) cannot be formed at fire time.
**Script:** `phase_b_path_beta.py`
**Log:** `phase_b_path_beta.log`

---

## §1 — substrate pull (verbatim quote-or-citation)

### Anti-circularity rule statement (per envelope STEP B.1, QA BLOCKING #4)

The path β.2 sympy script may NOT import any $(a_{1}, a_{2})$, $\Delta$-shift values, or canonical-$\Delta$ selection from path α. Path β.2 is required to independently solve $(F1) \wedge (F2) \wedge (F3)$ using ONLY:

* V_quad scalar OGF ODE (058R substrate);
* Liouville invariant $I_{V}(z) = (3 z^{2}+5 z-3)/(9 z^{3})$ (069 substrate);
* Okamoto 1987 §3 τ-function definition (slot 07 verbatim quote, ≤ 30 words);
* 058R Phase B canonical map $M = \Phi_{\mathrm{symp}} \circ \Phi_{\mathrm{shift}} \circ \Phi_{\mathrm{resc}}$;
* STEP A.1.5 KNY chart → Okamoto four-tuple map (LANDED substrate, not α-derived; using it does NOT constitute α-circularity per envelope NOTE).

Anti-circularity scan of `phase_b_path_beta.py`:

| imported from path α deliverables       | hits  | verdict           |
|------------------------------------------|-------|-------------------|
| `phase_a_path_alpha.py` (any import)     | 0     | PASS              |
| `(a_1, a_2)` numerical / symbolic values | 0     | PASS              |
| $\Delta_{0}, \Delta_{1}, \Delta_{2}$ shift values | 0 | PASS              |
| canonical-$\Delta$ selection logic       | 0     | PASS              |

`HALT_071_PATH_BETA_CIRCULARITY` not triggered.

### V_quad scalar-OGF Liouville invariant

(069 NEW substrate; 069 `phase_d_numerical.md` §2 sympy-derived; cited at 069 `phase_d_numerical.py` SHA `89D9EEFC57D9FA47..`)

$$I_{V}(z) \;=\; \frac{3 z^{2} \;+\; 5 z \;-\; 3}{9\,z^{3}}.$$

### Okamoto 1987 §3 τ-function definition (verbatim quote, ≤ 30 words)

(slot 07 anchor PDF `07_okamoto_1987_painleve_III_FE30.pdf` SHA `65294FBCA97E3CE1..` matches recorded `65294fbc..`; text-extract `07_okamoto_1987_painleve_III_FE30.txt` L1816–L1825 transcribed verbatim modulo OCR artefacts; spec §C.1 + C.2 compliance)

> "The τ-function τ = τ(v) related to H(v) is by definition:
>  (3.1)   H = (d/dt) log τ."

Word count (whitespace-split tokens including equation symbols and label "(3.1)"): **17 words** (sympy script `phase_b_path_beta.py` STEP B.1 verification). ≤ 30-word ceiling honoured. `HALT_071_OKAMOTO_QUOTE_LENGTH` not triggered.

This is Okamoto 1987 §3 eq. (3.1) — the canonical τ-function-from-Hamiltonian definition for $P_{III'}$ in Okamoto's 1987 normalisation $H_{III'} = \tfrac{1}{t}\bigl[q^{2} p^{2} - \{\eta_{\infty} q^{2} + \theta_{0} q - \eta_{0} t\} p + \tfrac{1}{2} \eta_{\infty}(\theta_{0}+\theta_{\infty}) q\bigr]$ (Okamoto 1987 eq. (0.1) — not re-extracted here; cited via 058R `phase_b_canonical_map.md` §B.2 verbatim).

### 058R Phase B canonical map

(058R `phase_b_canonical_map.md` SHA `F831F9BD58D1F306..`)

$$M \;=\; \Phi_{\mathrm{symp}} \circ \Phi_{\mathrm{shift}} \circ \Phi_{\mathrm{resc}}.$$

* $\Phi_{\mathrm{resc}}$: $z = \lambda\, t$ with $\lambda = c_{0}^{2}/4 = 1/3$.
* $\Phi_{\mathrm{shift}}$: $t \to t + t_{0}$ with $t_{0} = -\zeta_{*}/\lambda = -4\sqrt{3}$ (where $\zeta_{*} = 4/\sqrt{3}$).
* $\Phi_{\mathrm{symp}}$: structural form pinned (058R §B.3); Jacobian numerical value R1-gated.

### V_quad scalar OGF ODE form

(058R Phase A; cited via 058R `phase_a_birkhoff_match.py` SHA `7B4DD7636A3D9AD3..`)

$$3\,z^{3}\,f''(z) \;+\; 10\,z^{2}\,f'(z) \;+\; \bigl(z^{2} + 5\,z - 1\bigr)\,f(z) \;=\; 0.$$

---

## §2 — Phase B.2 τ-function reparametrisation sympy derivation (DEGRADED to substrate-gap statement)

### What §2 would have computed (counterfactual)

Had the explicit four-tuple map been substrate-supported, sympy would construct the system

$$\text{(F1)}\qquad
   \sigma(t) \;=\; t \cdot \frac{d}{dt} \log \tau(t),$$

(Okamoto Hamiltonian σ as the t-multiplied logarithmic derivative of τ; the "auxiliary Hamiltonian σ" formulation in Okamoto 1987 §3 derived from eq. (3.1) by the standard $\sigma = t\,H$ rescaling for $P_{III'}$);

$$\text{(F2)}\qquad
   (\alpha'_{\infty},\, \alpha'_{0},\, \beta'_{\infty},\, \beta'_{0})
   \;=\; (\alpha_{\infty} + \delta_{\infty},\, \alpha_{0} + \delta_{0},\, \beta_{\infty} + \delta_{\infty}',\, \beta_{0} + \delta_{0}'),$$

with $\sum (\alpha'_{\ast} + \beta'_{\ast}) = 0$ Okamoto null-sum on the reparametrised four-tuple;

$$\text{(F3)}\qquad
   I_{V}(z(x)) \;\equiv\; I_{\mathrm{KNY}}^{(\beta\text{-reparam})}(x;\, a_{0}, a_{1}, a_{2}),$$

with $z = \lambda(t + t_{0}) = (t - 4\sqrt{3})/3$ pull-back of the Liouville invariant.

### What §2 cannot compute given path α A.1.5.F1 cascade

(F2) and (F3) **both require** the explicit map between KNY $(a_{0}, a_{1}, a_{2})$ and Okamoto $(\alpha_{\infty}, \alpha_{0}, \beta_{\infty}, \beta_{0})$. STEP B.1 anti-circularity rule explicitly **permits** the use of the LANDED chart-map substrate (the map is shared, not α-derived). STEP A.1.5 substrate search detected the map is **ABSENT** from 058R + 069 deposit.

(F2) cannot be formed without a parametric description of how the four-tuple components depend on $(a_{0}, a_{1}, a_{2})$: a τ-function reparametrisation that "absorbs" the null-sum violation acts on the four-tuple side via $(\delta_{\infty}, \delta_{0}, \delta_{\infty}', \delta_{0}')$ but to verify the resulting $(\alpha'_{\ast}, \beta'_{\ast})$ "pushes forward to the KNY $(a_{0}, a_{1}, a_{2})$ chart consistently with 058R Phase B" requires the explicit chart-map.

(F3) cannot be evaluated without the closed-form chart-map: $I_{\mathrm{KNY}}^{(\beta\text{-reparam})}$ depends on $(a_{0}, a_{1}, a_{2})$ via the KNY 2017 §8.5.17 ρ_0 + ρ_1 expressions for $L_{1}$ (069 `phase_d_numerical.md` §2; cited at SHA `E98D74EBD30EB43C..`), and the τ-function reparametrisation enters via the gauge-equivalence class. With no chart-map, no closed-form τ-induced shift δ can be numerically extracted.

### Path β substrate-gap detection

The path β substrate gap is a **cascade** of the path α A.1.5.F1 substrate gap, not an independent obstruction. Specifically:

* Path β does NOT require path α's $(a_{1}', a_{2}')$ output (anti-circularity rule honoured).
* Path β DOES require the same LANDED-substrate chart-map that path α STEP A.1.5 found absent.
* The cascade routes through (F2) and (F3) simultaneously — an Okamoto 1987 §3 τ-function reparametrisation can be defined ABSTRACTLY as $\sigma(t) = t \cdot d/dt \log \tau(t)$ (the verbatim quote above) without any chart-map; but to exhibit a CLOSED-FORM δ that satisfies (F2) AND consistency-pushes-forward to KNY chart per (F3), the chart-map needs to be substrate-supplied.

### Failure mode determination

| candidate failure mode                                            | trigger?  | basis                                                                                    |
|-------------------------------------------------------------------|-----------|------------------------------------------------------------------------------------------|
| B.1 anti-circularity violation (HALT_071_PATH_BETA_CIRCULARITY)   | NO        | scan of `phase_b_path_beta.py` returns 0 imports / values from path α (see §1 table)       |
| B.2.F1 (τ-function reparam inconsistent with (F3); HALT_071_PATH_BETA_INCONSISTENT) | NO | (F2)/(F3) cannot be FORMED without chart-map substrate; INCONSISTENT verdict not reached |
| B.2.F2 (τ-function reparam requires Okamoto §4)                   | NO        | upstream substrate gap (chart-map) precedes higher-order Okamoto Hamiltonian question   |
| **CASCADE-BLOCK from path α A.1.5.F1**                            | **YES**   | path β depends on the same chart-map that path α found absent                            |

Path β is closed via **CASCADE-BLOCK from A.1.5.F1**, not via either of B's own phase-level halts. This is the cleaner failure mode: the substrate gap is shared, not independent.

### Per envelope: degrade (F1) ∧ (F2) ∧ (F3) attempt to substrate-gap statement

Envelope STEP B.2 instructs solving (F1) ∧ (F2) ∧ (F3) for closed-form $\delta + \tau$. With cascade-block at fire time, the system is **NOT FORMED**.

### sympy script outputs (see `phase_b_path_beta.py` + `.log`)

The sympy script `phase_b_path_beta.py` produces verifiable artefacts:

* sympy-pulls in the Okamoto 1987 §3 eq. (3.1) verbatim quote as a string constant `OKAMOTO_3_1_QUOTE` (≤ 30 words).
* sympy-verifies the V_quad-side Liouville invariant matches 069 substrate at V_quad parameter point (re-derivation; same as Phase A STEP 3, repeated independently per anti-circularity rule).
* sympy declares (F1) abstractly via `sigma(t) = t * sympy.diff(log(tau(t)), t)` — the Okamoto definition itself — and verifies it is well-formed sympy.
* sympy declares (F2) and (F3) require chart-map substrate that is ABSENT; documents `NotImplemented_substrate_gap` for both.
* No fabricated Okamoto-side $\delta$ values; no path-α imports.

---

## §3 — Phase B.3 (a_1'', a_2'') extraction (NOT REACHED)

Phase B.3 (a_1'', a_2'') extraction requires Phase B.2 to have produced a closed-form $\delta + \tau$. Given cascade-block, B.2 did not form (F2) ∧ (F3); B.3 is **NOT REACHED**.

Path β verdict: **NO_GO_PATH_BETA via cascade-block from A.1.5.F1** — closed without producing a closed-form $(a_{1}'', a_{2}'')$ at V_quad parameter point.

---

## Path β conclusion

* Substrate search exhaustive within anti-circularity-permitted scope.
* Okamoto 1987 §3 eq. (3.1) τ-function definition cleanly extracted (≤ 30 words verbatim).
* (F1) abstract form is well-defined (the canonical Okamoto definition itself).
* (F2) ∧ (F3) cannot be formed because the KNY chart → Okamoto four-tuple map is the same LANDED-substrate gap that triggered path α A.1.5.F1.
* Path β closed via cascade-block; verdict path NO_GO_PATH_BETA enabled.

### Combined Phase A + Phase B conclusion

Both paths closed without producing closed-form $(a_{1}, a_{2})$. Cascade pattern:

* **Path α STEP A.1.5.F1** detects substrate gap directly (chart-map absent).
* **Path β STEP B.1** anti-circularity-clean; **Path β STEP B.2** cascade-blocked by the same chart-map gap.

Envelope verdict ladder selection: **NO_GO_SUBSTRATE_INSUFFICIENT** (both paths closed with halts/cascades).

End of `phase_b_path_beta.md`.
