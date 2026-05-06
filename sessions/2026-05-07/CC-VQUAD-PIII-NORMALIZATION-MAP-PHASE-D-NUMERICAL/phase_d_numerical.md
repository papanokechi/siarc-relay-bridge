# Phase D.2 — numerical cross-check (the residual)

**Session:** 069 CC-VQUAD-PIII-NORMALIZATION-MAP-PHASE-D-NUMERICAL
**Phase D.2 verdict:** **UPGRADE_V1_0_PARTIAL_NUMERICAL_PERSIST**
**Method:** sympy symbolic transcription + mpmath numerical baseline + structural obstruction map.
**Script:** `phase_d_numerical.py` — runs at mpmath dps = 50.
**Log:** `phase_d_numerical.log`.

---

## Cross-check identity (058R `phase_d_verdict.md` L62–95)

The cross-check that, if it agreed at ≥ 5 digits, would carry the
verdict ladder from `UPGRADE_V1_0_PARTIAL_NUMERICAL` (058R) to
`UPGRADE_V1_0_FULL`:

$$\bigl| M^{*}\,C_{V} \bigr| \;\overset{?}{=}\; \bigl| S_{\zeta_{*}}^{\mathrm{can}} \bigr|.$$

* $|C_V| = 8.127\,336\,795\,495\,072\,367\ldots$ at ≥ 108 digits (V_quad-native; H4 measurement; 058R Phase A `phase_a_birkhoff_match.py` SHA `7B4DD7636A3D9AD3..`).
* $|S_{\zeta_{*}}^{\mathrm{can}}|$ is the canonical-form Stokes constant given by BLMP 2024 §4 connection-matrix integral (eq. 4.28).
* $M^{*}$ is the pullback of the canonical-form Stokes map under $M = \Phi_{\mathrm{symp}} \circ \Phi_{\mathrm{shift}} \circ \Phi_{\mathrm{resc}}$. Explicit evaluation requires the symbolic gauge transformation from V_quad's scalar-OGF Lax representation to KNY 2017 §8.5.17 second-order scalar Lax form $L_1 y = 0$ (eq. 8.239).

Phases D.2.a–D.2.e below decompose the cross-check into substrate-pull + gauge construction + Jacobian + BLMP 2024 evaluation + residual.

---

## §1 — Phase D.2.a: KNY 2017 §8.5.17 differential Lax pull at V_quad parameter point

**Substrate (per envelope V1.2.D4 + 058R Phase B.3):** the actual 2×2 Lax pair anchor for $P_{III}(D_6)$ is **KNY 2017 §8.5.17 eq. 8.237–8.239** (slot anchor `g3b_2026-05-03 KNY 2017 PDF`); Okamoto 1987 §§1–4 covers Hamiltonian / affine Weyl / τ-functions / cylinder functions but does NOT contain an explicit 2×2 Lax pair (anomaly D4 surfaced at 058R).

**Hamiltonian** (KNY 2017 eq. 8.237; transcribed verbatim from 058R `phase_b_canonical_map.md` SHA `F831F9BD58D1F306..` quoted from text-extract `14_kajiwara_noumi_yamada_2017_geometric_aspects.txt` L7912–7920; ≤ 30 words):

$$H_{D_6}^{\mathrm{KNY}} \;=\; \tfrac{1}{t}\bigl\{\, p(p-1)\,q^{2} + (a_{1} + a_{2})\,q\,p + t\,p - a_{2}\,q \,\bigr\},
\qquad a_{0} + a_{1} = 1.$$

**Differential Lax operator $L_1$** (KNY 2017 eq. 8.239; verbatim, ≤ 30 words):

$$L_{1} \;=\; \rho_{0}(x; q, p, t, a_{2}) \;+\; \rho_{1}(x; q, a_{1}, a_{2}, t)\,\partial_{x} \;+\; \partial_{x}^{2},$$

where

$$\rho_{0}(x) \;=\; -\tfrac{a_{2}}{x} + \tfrac{p\,q}{x(x-q)} - \tfrac{t\,H}{x^{2}},
\qquad
\rho_{1}(x) \;=\; \tfrac{1 + a_{1} + a_{2}}{x} - \tfrac{1}{x - q} + \tfrac{t}{x^{2}} - 1.$$

(The full $L_2 = T_{\alpha} - \tfrac{1}{x-q}(p - \partial_{x})$ + $B = \partial_{t} - \tfrac{q}{t(x-q)}(x\partial_{x} - q p)$ form per KNY 2017 eq. 8.239 verbatim quote in 058R `phase_b_canonical_map.md` is cited at SHA without re-extraction here per envelope CARRY-FORWARD-SLOTS rule.)

**V_quad parameter point — CT v1.3 §3.5 four-tuple form**:

$$(\alpha_{\infty}, \alpha_{0}, \beta_{\infty}, \beta_{0}) \;=\; \bigl( \tfrac{1}{6},\ 0,\ 0,\ -\tfrac{1}{2} \bigr).$$

**Okamoto null-sum check** (sympy-evaluated):

$$\alpha_{\infty} + \alpha_{0} + \beta_{\infty} + \beta_{0} \;=\; \tfrac{1}{6} + 0 + 0 - \tfrac{1}{2} \;=\; -\tfrac{1}{3} \;\neq\; 0.$$

This is **anomaly D2** carried forward unchanged from 058R. Okamoto 1987's null-sum constraint $\alpha_{\infty}+\alpha_{0}+\beta_{\infty}+\beta_{0}=0$ is violated by V_quad's CT v1.3 §3.5 four-tuple. Reconciliation requires either:

* (path α) an additional shift in the $(a_{0}, a_{1}, a_{2})$ chart that restores the null-sum after Okamoto $\to$ KNY conversion, **or**
* (path β) a τ-function reparametrisation per Okamoto 1987 §3 that absorbs the $-1/3$ offset into a different normalisation.

Neither path α nor path β is closed-form within the agent budget. The conversion from CT v1.3 four-tuple to KNY $(a_{0}, a_{1}, a_{2})$ at V_quad parameter point is **R1-gated**.

**Φ_resc + Φ_shift PINNED** (058R Phase B `phase_b_canonical_map.md` SHA `F831F9BD58D1F306..`):

* $\Phi_{\mathrm{resc}}$: $z = \lambda\, t$ with $\lambda = c_{0}^{2}/4 = 1/3$.
* $\Phi_{\mathrm{shift}}$: $t \to t + t_{0}$ with $t_{0} = -\zeta_{*}/\lambda = -3 \cdot 4/\sqrt{3} = -4\sqrt{3}$.

**[Status]** $(a_{1}, a_{2})$ at V_quad parameter point: **NOT PINNED**. R1 carry-forward open per 058R + envelope PRE-CONDITION 2 default (B). The KNY pull at the V_quad parameter point therefore captures the **structural form** of $L_1$ in the chart $(x; q, p, t, a_{1}, a_{2})$ but does **not** specialise the $(a_{1}, a_{2})$ pair.

---

## §2 — Phase D.2.b: symbolic gauge transformation $G(x)$ construction

**Goal.** Construct $G(x)$ such that

$$L_{1}^{V_{\mathrm{quad}}}(x) \circ G \;=\; G \circ L_{1}^{\mathrm{KNY}}(x)$$

at the V_quad parameter point.

**V_quad scalar OGF ODE** (058R Phase A re-derivation; SHA-anchored at `7B4DD7636A3D9AD3..`):

$$3\,z^{3}\,f''(z) \;+\; 10\,z^{2}\,f'(z) \;+\; \bigl(z^{2} + 5\,z - 1\bigr)\,f(z) \;=\; 0.$$

(Derivative order: 2. The envelope wording "third-order scalar-OGF Lax representation" describes the singularity structure at $z=0$ — Newton-polygon edge slope 1/2 yielding rank-1 essential singularity in the ramified $u = \sqrt{z}$ coordinate — not the differential order.)

**Liouville normal-form invariant of V_quad's ODE.** Writing the ODE as $f'' + p_{V}(z)\,f' + q_{V}(z)\,f = 0$ with $p_{V}(z) = 10/(3z)$ and $q_{V}(z) = (z^{2}+5z-1)/(3 z^{3})$, the gauge-invariant (under $f \mapsto h(z)\,f$ for any non-vanishing $h$) is

$$I_{V}(z) \;=\; q_{V}(z) \;-\; \tfrac{1}{4}\,p_{V}(z)^{2} \;-\; \tfrac{1}{2}\,p_{V}'(z) \;=\; \boxed{\;\frac{3 z^{2} \;+\; 5 z \;-\; 3}{9\,z^{3}}.\;}$$

(sympy verified; output `I_V(z) = (3*z**2 + 5*z - 3)/(9*z**3)` from `phase_d_numerical.log`.) This is a **NEW** structural quantity (not in 058R deposit). It pins the V_quad-side normal form at the gauge level and is independent of any KNY-side parameter convention.

**KNY $L_1$ Liouville invariant.** Writing KNY's $L_1 y = 0$ in the same normalised form gives

$$I_{\mathrm{KNY}}(x; q, p, t, a_{1}, a_{2}) \;=\; \rho_{0}(x) \;-\; \tfrac{1}{4}\,\rho_{1}(x)^{2} \;-\; \tfrac{1}{2}\,\rho_{1}'(x).$$

Closed-form expansion of $I_{\mathrm{KNY}}$ at the V_quad parameter point requires:

1. **R1 closure**: $(a_{1}, a_{2})$ at V_quad point — **OPEN**.
2. **Hamiltonian flow integration**: $(q(t), p(t))$ at $t_{0} = -4\sqrt{3}$ from KNY's Hamilton equations $\dot q = \partial H/\partial p$, $\dot p = -\partial H/\partial q$ — **conditional on R1 closure** for the parameter-side $(a_{1}, a_{2})$.
3. **Schwarzian invariant matching** $I_{V}(z(x)) \equiv I_{\mathrm{KNY}}(x; \ldots)$ under $z = \lambda(t + t_{0}) = (t-4\sqrt{3})/3$ — **conditional on steps 1 + 2**.

Steps 1 + 2 are R1-gated; step 3 is conditional on steps 1 + 2 outputs.

**[Obstruction]** Closed-form symbolic gauge $G(x)$ at V_quad parameter point is **OBSTRUCTED_R1_GATED**.

**Verdict ladder mapping:** per envelope §HALTS the candidate halt at this step is `HALT_069_GAUGE_TRANSFORM_FAILURE`, with verdict path `UPGRADE_V1_0_PARTIAL_NUMERICAL_PERSIST`. The structural cause is the unresolved R1 (CT v1.3 §3.5 four-tuple to KNY $(a_{0}, a_{1}, a_{2})$ identification with Okamoto null-sum reconciliation), surfaced as 058R anomalies D1 + D2. Without R1 closure the gauge transformation cannot be specialised at the V_quad parameter point.

The Liouville invariant $I_V(z) = (3z^{2} + 5z - 3)/(9 z^{3})$ on the V_quad side is the **clean substrate** that any future R1-closure relay (069r1) can pull forward to compute the gauge transformation once $(a_{1}, a_{2})$ is pinned.

---

## §3 — Phase D.2.c: $|\det J(\Phi_{\mathrm{symp}})|$ numerical evaluation

**Block Jacobian factorisation** (058R Phase B `phase_b_canonical_map.md` §B.4; SHA `F831F9BD58D1F306..`):

$$\det J(M) \;=\; \det J(\Phi_{\mathrm{symp}}) \cdot \det J(\Phi_{\mathrm{shift}}) \cdot \det J(\Phi_{\mathrm{resc}}).$$

Pinned blocks (058R Phase B):

| block          | $\det J$    | basis                                                        |
|----------------|-------------|--------------------------------------------------------------|
| $\Phi_{\mathrm{resc}}$  | $\lambda^{2} = 1/9$ | scalar rescaling $z = (1/3)\,t$ on $(q, p)$                |
| $\Phi_{\mathrm{shift}}$ | $1$          | affine shift $t \to t + t_{0}$                              |
| $\Phi_{\mathrm{symp}}$  | open        | gauge transform from V_quad scalar-OGF to KNY 2nd-order Lax |

**Numerical $|\det J(\Phi_{\mathrm{symp}})|$ at V_quad parameter point.** The structural form is the canonical $(q, p) \leftrightarrow (q, p)$ gauge transformation that aligns Okamoto 1987 $H_{III}$ with KNY 2017 $H_{D_6}^{\mathrm{KNY}}$. The mapping is bijective on the relevant chart with non-degenerate Jacobian (058R `phase_b_canonical_map.md` §B.3 verbatim).

The **numerical value** at the V_quad parameter point requires the explicit gauge $G(x)$ from §2. Because the gauge is OBSTRUCTED_R1_GATED, the numerical Jacobian factor is **NOT_COMPUTABLE_R1_GATED** in this session.

**[Status]** $|\det J(\Phi_{\mathrm{symp}})|$ numerical: **NOT COMPUTABLE** in 069. Structural form unchanged from 058R (bijective + non-degenerate on relevant chart).

`HALT_069_PHI_SYMP_NUMERICAL_INCONSISTENCY` is **NOT TRIGGERED** — no NaN, inf, divergent series, or value inconsistent with 058R structural form was produced; the obstruction is upstream (gauge transformation R1-gated), not numerical-instability.

---

## §4 — Phase D.2.d: BLMP 2024 §4.28 connection-matrix evaluation

**Substrate.** BLMP 2024 §4 connection-matrix formula (eq. 4.28; slot 08 SHA `96c49cdd..`) evaluates $|S_{\zeta_{*}}^{\mathrm{can}}|$ as a function of monodromy parameters $(e_{1}, e_{2}) \in (\mathbb{C}^{*})^{2}$ on the cubic-surface monodromy manifold $\mathcal{M}$ (BLMP 2024 Definition 1.3, eq. 1.16). Conversion from KNY $(a_{1}, a_{2})$ to BLMP $(e_{1}, e_{2})$ is given in BLMP 2024 §4 explicit formula.

**[Status]** $(a_{1}, a_{2})$ at V_quad parameter point: **NOT PINNED** (R1-gated per §1). Therefore BLMP 2024 §4.28 integrand at V_quad point: **NOT EVALUABLE**. Thus $|S_{\zeta_{*}}^{\mathrm{can}}|$ at V_quad point: **NOT COMPUTABLE** in 069.

**[Runtime fallback]** Runtime-fallback `HALT_069_R1_SCOPE_AMBIGUOUS` surfaced (NOT halt-listed in envelope; envelope-author note: appears as runtime-safety fallback only because operator's PRE-CONDITION 2 choice settles it before fire). Operator-decidable PRE-CONDITION 2 default = (B) routes to clean halt for 069r1 R1-closure preflight relay.

`HALT_069_BL2024_PRECISION_FLOOR_INSUFFICIENT` is **NOT TRIGGERED** — the precision floor question is moot because the integrand is not evaluable (a_1, a_2 unpinned), not because of numerical-precision degradation.

**H4 baseline (V_quad-native; informational only — NOT the canonical-form value).**

At mpmath dps = 50:

$$|C_{V}| \;=\; 8.127\,336\,795\,495\,072\,367\,112\,578\,732\,02\ldots$$

$$\bigl| 2\pi\,C_{V} \bigr| \;=\; 51.065\,563\,139\,954\,662\,269\,831\,674\,609\,923\,147\,769\,762\,888\,992\,158\ldots$$

The relation $|S_{\zeta_{*}}^{V}| = 2\pi C_{V}$ holds in V_quad-native normalisation (Birkhoff–Trjitzinsky 1933 convention; carry-forward via D2-NOTE v2.1 per spec C.4/C.5 directive). This is **NOT** the canonical-form value $|S_{\zeta_{*}}^{\mathrm{can}}|$ (which would be evaluated independently from BLMP 2024 §4.28). The cross-check identity in §5 requires an independent canonical-form evaluation; using the V_quad-native value as a stand-in for the canonical value would be circular and is forbidden by `HALT_069_OVER_CLAIM` checklist item (3) ("residual Δ < 10^{-5} computed from independent left-hand and right-hand sides").

---

## §5 — Phase D.2.e: cross-check + verdict selection

**Residual definition.**

$$\Delta \;=\; \frac{\bigl|\,|M^{*} C_{V}| - |S_{\zeta_{*}}^{\mathrm{can}}|\,\bigr|}{\max\bigl(|M^{*} C_{V}|,\ |S_{\zeta_{*}}^{\mathrm{can}}|\bigr)}.$$

**Left-hand side $|M^{*} C_{V}|$ at V_quad parameter point:**

| factor                              | value                                | status                       |
|-------------------------------------|--------------------------------------|------------------------------|
| $|C_V|$                             | $8.127\,336\,795\,495\,072\,367\ldots$ (≥108 dps) | PINNED (058R Phase A; H4) |
| $|\det J(\Phi_{\mathrm{resc}})|$    | $1/9$                               | PINNED (058R Phase B)        |
| $|\det J(\Phi_{\mathrm{shift}})|$   | $1$                                 | PINNED (058R Phase B)        |
| $|\det J(\Phi_{\mathrm{symp}})|$    | —                                   | NOT_COMPUTABLE_R1_GATED      |

LHS evaluates at fire time as **NOT COMPUTABLE** without §2 + §3 outputs.

**Right-hand side $|S_{\zeta_{*}}^{\mathrm{can}}|$ at V_quad parameter point:**

| factor                                      | status                       |
|---------------------------------------------|------------------------------|
| BLMP 2024 §4.28 integrand at $(a_1, a_2)$ | NOT_COMPUTABLE_R1_GATED      |

RHS evaluates as **NOT COMPUTABLE** without R1 closure for $(a_{1}, a_{2})$.

**Residual Δ.** Δ = INCOMPUTABLE (both LHS and RHS R1-gated).

**Precision-floor log:**

* mpmath dps = 50 (set at script entry).
* $|C_V|$ provenance: H4 measurement at ≥ 108 digits (058R `phase_a_birkhoff_match.py` SHA `7B4DD7636A3D9AD3..`).
* $|2\pi C_V| = 51.0655\ldots$ at 50 dps (V_quad-native; not the canonical-form quantity).
* tail-error estimate: not applicable (no integrand evaluated; no truncation introduced).

**Verdict-ladder selection** (envelope §VERDICT LADDER; per RECOMMENDED #4 + #5 from QA, no probability anchoring):

| rung                                                      | threshold        | met?       |
|-----------------------------------------------------------|------------------|------------|
| `UPGRADE_V1_0_FULL`                                       | Δ < 10^{-5}      | NOT MET    |
| `UPGRADE_V1_0_PARTIAL_NUMERICAL_PRECISION_DEGRADED`       | 10^{-5} ≤ Δ < 10^{-2} | NOT MET    |
| `HALT_069_STOKES_NUMERICAL_MISMATCH`                      | Δ ≥ 10^{-2}      | NOT MET    |
| `UPGRADE_V1_0_PARTIAL_NUMERICAL_PERSIST`                  | Δ INCOMPUTABLE   | **SELECTED** |

**Selected verdict: `UPGRADE_V1_0_PARTIAL_NUMERICAL_PERSIST`.**

058R verdict `UPGRADE_V1_0_PARTIAL_NUMERICAL` is re-confirmed at 069. No progress on the residual: the gauge transformation $G(x)$ is OBSTRUCTED_R1_GATED, the Jacobian factor $|\det J(\Phi_{\mathrm{symp}})|$ is NOT_COMPUTABLE_R1_GATED, and the BLMP 2024 §4.28 evaluation is NOT_COMPUTABLE_R1_GATED.

---

## Outcomes (envelope §VERDICT LADDER, PERSIST rung)

* **M6.CC closure status:** STRUCTURAL (058R level unchanged); numerical residual unchanged.
* **G15** (Φ_symp residual on KNY 2017 §8.5.17 Lax-pair anchor): MOSTLY CLOSED (no change from 058R).
* **G22** (V_quad → P_III(D_6) canonical-form normalisation map at 108-digit canonical-form precision): partial (no change from 058R).
* **op:cc-formal-borel residual:** partial (no change from 058R).
* **M9 gating:** {M6.CC numerical residual} (no change from 058R).
* **Picture v1.20 deposit:** NOT TRIGGERED (operator-gated; conditional on FULL or PRECISION_DEGRADED).

## Refire path

* (a) **069r1 preflight** at synthesizer cadence: R1 closure (CT v1.3 §3.5 four-tuple ↔ KNY $(a_0, a_1, a_2)$ identification with null-sum reconciliation). Estimated 1–2 h agent runtime. Lands a clean $(a_{1}, a_{2})$ parameter point at V_quad. Permits 069 re-fire on Phase D.2 sub-steps a–e with R1 closed.
* (b) **069 re-fire with extended budget** (PRE-CONDITION 2 path A inline): operator dispatches 069 at 6–10 h budget with R1 closure inline; agent attempts paths α + β at Phase D.2.b inline.
* (c) **W21 LANE-1 T1-Synth analytic guidance request relay**: operator escalates the gauge-transform symbolic difficulty to LANE-1 for analytic review. Estimated 1–2 h synthesizer activity.

The envelope §RECOMMENDED NEXT STEPS lists option (c) for the PERSIST rung verdict.

---

## §6 — Forbidden-verb scan + scope-discipline scan (self-check)

This Phase D.2 deliverable's prose (excluding verbatim ≤ 30-word literature quotes in §1) was scanned by the agent at write time for the envelope §EPISTEMIC DISCIPLINE forbidden-verb list (12 entries; case-sensitive) plus the deprecated-citation pattern. Scan output recorded in `forbidden_verb_scan.md`.

This Phase D.2 deliverable does NOT re-derive any 058R LANDED phase; cites Phases 0/A/B/B.5/C/E by SHA anchor. No `HALT_069_SCOPE_CREEP_INTO_LANDED_PHASE` violation.

End Phase D.2 numerical write-up.
