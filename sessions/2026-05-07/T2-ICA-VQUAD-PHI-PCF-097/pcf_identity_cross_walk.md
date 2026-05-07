# PCF identity cross-walk — M5 / M6.CC / M9

**Relay:** 097 T2-ICA-VQUAD-PHI-PCF
**Phase:** D (PCF identity statements cross-walk)
**Anchor (substrate):** PCF-1 v1.3 source `p12_pcf1_main.tex`
(SHA-256 `E83BB377F297DBF0...4BE301`; bridge anchor at
sessions/2026-05-01/PCF1-V13-UPDATE/), 058R + 069 handoffs,
picture v1.19 (SHA-256 prefix `8BD9043370872F07`),
096 TIER-A.1, 065 cf_value() audit (verdict UNIFORM at 13 implementations),
066 LANE-2 R1 row reframing memo, 060 CMB OQ paste record.

---

## 1. PCF identity inventory at M5 (PCF-1 v1.3)

### 1.1 Main convergence identity

PCF-1 v1.3 §2 (verbatim L153-159 of bridge anchor):

$$
L \;=\; K(a_n, b_n) \;=\; b_0 + \cfrac{a_1}{b_1 + \cfrac{a_2}{b_2 + \cdots}}.
$$

Wallis convergent recurrence:

$$
p_n = b_n p_{n-1} + a_n p_{n-2}, \qquad q_n = b_n q_{n-1} + a_n q_{n-2}
$$

with seeds $(p_{-1}, p_0, q_{-1}, q_0) = (1, b_0, 0, 1)$. Convergent
error $\delta_n = p_n / q_n - L$.

### 1.2 Spec(K) invariant tuple (v5 schema)

PCF-1 v1.3 §2 (verbatim L162-164):

$$
\operatorname{Spec}(K) = (d, \Lambda, \Delta, \rho, \tau)
$$

with v5 upgrade adding components 6 and 7: $S$ (Stokes exponent) and
$\sigma$ (connection-coefficient proxy).

### 1.3 Balanced discriminant identity

PCF-1 v1.3 §2 (verbatim from §1.4 prose; see also §6 L526-527):

$$
\Delta = \beta^2 - 4\alpha\gamma
\qquad\text{where}\qquad
b_n = \alpha n^2 + \beta n + \gamma.
$$

### 1.4 Sharp dichotomy (Conjecture A v5 part (i))

PCF-1 v1.3 §3 Conjecture A (Theorem-of-Conjecture-form; verbatim L320,
formalising the empirical content L131-138):

* $\Delta \in \{+1, +8\} > 0$ ⟹ elementary closed form via
  Lindemann-Weierstrass; 24 F(2,4) Trans-stratum families.
* $\Delta \in \{-3, -4, -7, -11, -20, -28\}$ ⟹ PSLQ non-detection
  at 18-element basis / 220 dps / integer-bound $10^{10}$; 6 families.
* $\Lambda \in \mathbb{Q}(\sqrt{\Delta})$ for the second row (CM
  predicate).

### 1.5 WKB exponent identity (Theorem 5; thm:wkb)

PCF-1 v1.3 §6 (verbatim L538-553):

$$
\log|\delta_n| = -A\,n\log n + \alpha\,n - \beta_w \log n + \gamma_w
   + \sum_{k\ge 1} \frac{h_k}{n^k},
$$

with leading exponents

$$
A \in \{3, 4\},\qquad \alpha = A - 2\log c_b + \log|c_a|,
$$

where $A = 4$ for V_quad (sole sporadic upper-branch row at $\Delta = -11$)
and $A = 3$ for the five quadratic-limit families.

### 1.6 V_quad → P_III(D_6) reduction identity

PCF-1 v1.3 §7 channel-scope subsection (verbatim L673-696, paraphrased
where indicated; explicit Painlevé parameters at L494):

V_quad's Painlevé-III($D_6$) reduction at parameters

$$
\alpha_{\mathrm{P_{III}}} = \tfrac{1}{6},\quad
\beta_{\mathrm{P_{III}}} = \gamma_{\mathrm{P_{III}}} = 0,\quad
\delta_{\mathrm{P_{III}}} = -\tfrac{1}{2}
$$

is established **in the connection-coefficient channel of the
underlying second-order linear difference equation** (Borel
transform $\mathcal{B}[L](\zeta)$ in Stokes-constant ODE space).
PCF-1 v1.3 explicitly distinguishes this Borel-transform channel
from two operationally available channels (recurrence-parameter
channel; Borel-resummation channel) which **do not** recover the
P_III(D_6) reduction at the precision tested.

### 1.7 LANE-2 R1 row reframing (066 forward-pointer; PCF-1 v1.3 source UNMODIFIED)

LANE-2 Item 3 verdict `LEAVE_V1_0_CANONICAL`: PCF-1 v1.3 source held
canonical at v1.3; v1.4 amendment forward-pointed (NOT FIRED). 066
re-attributes V_quad's $A = 4$ row entry from a borderline-mechanism
(i') framing to **deg_a = 0 row member at d = 2** under the extended
four-row Phase A enumeration of 064 supplement §2.3. Source is
unchanged at PCF-1 v1.3; 066 is a forward-pointer note.

### 1.8 CMB OQ paste (060 record)

CMB.txt OPEN QUESTIONS FOR T1 SYNTH section absorbed 3 OQ entries
at 060 paste (sessions/2026-05-06/CMB-OQ-PASTE-W20-051-Q1Q2Q4-
EXECUTION/): Q1-MECHANISM-IDENTIFICATION + Q2-BORDERLINE-Q-ANSATZ +
Q4-SECTORIAL-UPGRADE. These are PCF-1-related synthesizer questions
(M4 / borderline mechanism / Wasow §X.3 Theorem 11.1 sectorial
upgrade) — not changes to the M5 PCF identity itself.

---

## 2. PCF identity inventory at M6.CC (058R + 069)

M6.CC operates on the **same** PCF identity as M5 (no M5 identity is
modified). 058R + 069 add the following identity-relevant components:

### 2.1 Borel-transform channel content

058R Phase A (sympy-derived, verbatim from Phase A md):

* $\beta_{\text{Gevrey}} = 0$ at the Birkhoff level (logarithmic Borel
  branch of V_quad's scalar OGF ODE).
* Characteristic equation $3 C^2 - 4 = 0$ ⟹ $|\zeta_*| = 4/\sqrt{3}$
  (Borel-plane partner-action distance).
* $C_V = 8.127336795495072367\ldots$ at $\ge 108$ dps (V_quad-native
  Stokes amplitude; H4 measurement).
* $|2\pi C_V| = 51.06556313995466\ldots$ at 50 dps (V_quad-native;
  **NOT** the canonical-form value).

### 2.2 V_quad → P_III(D_6) normalization map

058R Phase B + 069 Phase D:

$$
M = \Phi_{\mathrm{symp}} \circ \Phi_{\mathrm{shift}} \circ \Phi_{\mathrm{resc}}
$$

with $\lambda = 1/3$, $t_0 = -4\sqrt{3}$, $|\det J(\Phi_{\mathrm{resc}})|
= 1/9$, $|\det J(\Phi_{\mathrm{shift}})| = 1$,
$|\det J(\Phi_{\mathrm{symp}})|$ NOT_COMPUTABLE_R1_GATED.

### 2.3 Liouville normal-form invariant (069 NEW substrate)

069 Phase D.2.b sympy-derives, gauge-invariant:

$$
I_V(z) = \frac{3 z^2 + 5 z - 3}{9 z^3}.
$$

This is NEW substrate at 069 not in 058R deposit; gauge-invariant
under the symbolic gauge transformation $G(x)$ that the R1-gated
Phase D.2.b symbolic step would construct. Forward-pointed for
069r1 R1-closure preflight.

### 2.4 KNY 2017 §8.5.17 Hamiltonian + Lax-pair anchor

Verbatim from 058R Phase D.2.a substrate (KNY 2017 §8.5.17):

$$
H_{D_6}^{\mathrm{KNY}} = \tfrac{1}{t}\bigl[p(p-1) q^2 + (a_1 + a_2) q p
   + t p - a_2 q\bigr]
$$

with constraint $a_0 + a_1 = 1$. Lax operator
$L_1 = \rho_0 + \rho_1 \partial_x + \partial_x^2$.

### 2.5 CT v1.3 §3.5 4-tuple (with null-sum violation)

CT v1.3 §3.5 (Channel-Theory v1.3; Zenodo concept DOI
`10.5281/zenodo.19972394`):

$$
(\alpha_\infty,\, \alpha_0,\, \beta_\infty,\, \beta_0)
\;=\; \bigl(\tfrac{1}{6},\, 0,\, 0,\, -\tfrac{1}{2}\bigr).
$$

058R-D2 + 069 (sympy-verified): null-sum
$\alpha_\infty + \alpha_0 + \beta_\infty + \beta_0 = -1/3 \neq 0$.

This is an open M6.CC R1 carry-forward. Reconciliation may proceed
via additional shift in the $(a_0, a_1, a_2)$ chart, or via Okamoto
§3 τ-function reparametrisation (069r1 envelope drafted with both
paths α and β explicit).

### 2.6 W-framework cross-walk (058R Phase B.5 INDEX-2 EMBEDDING FINAL)

Per 033 + 036 absorption (picture v1.19 v18→v19 deposit):

$$
\varphi : W^{\mathrm{aff}}(B_2) \hookrightarrow \mathrm{Aut}(D_6^{(1)})
   \ltimes W\bigl((2 A_1)^{(1)}\bigr)
$$

with cokernel $\mathbb{Z}/2 = P^\vee(B_2) / Q^\vee(B_2) =$
centre$(\mathrm{Spin}(5)) = \mathrm{Sp}(2)$. Strict-iso pivot ruled
out; INDEX-2 EMBEDDING FINAL is the canonical Phase B.5 closure
form.

058R-D3: spec's "$W(D_6)$" framing has no literature anchor; literature
uses $W_a(B_2) = W_a(C_2)$ + $(2 A_1)^{(1)}$ symmetry-type +
$D_6^{(1)}$ surface-type. Cross-walk is **inclusion** not quotient.

---

## 3. PCF identity inventory at M9 (picture v1.19 + 096)

### 3.1 V0 announcement assignment rule (096 §4.1)

$$
\Phi(\mathcal{F}) \;\longmapsto\;
   \bigl(\Delta_d(\mathcal{F}),\;
         \|\Delta(\mathcal{F})\|_{\mathrm{Pet}},\;
         \xi_0(\mathcal{F})\bigr).
$$

Component anchors:

* $\xi_0(\mathcal{F})$ — D2-NOTE v2.1 Theorem 4.1 THEOREM-GRADE for
  all $d \ge 2$ uniformly (Zenodo version DOI
  `10.5281/zenodo.20015923`).
* $\Delta_d(\mathcal{F})$ — picture v1.19 §3 P-PET row L850-856,
  $j = 0$ A=6-only branch CLOSED via Q22 path-(a) at $|\delta_a|
  = 3.08904186542 \times 10^{-23}$ (014 prompt + 099 deposit-readiness
  memo).
* $\|\Delta\|_{\mathrm{Pet}}$ — derived from $\Delta_d$ via
  Petersson inner product at the working weight (cubic case:
  weight 12, $SL_2(\mathbb{Z})$).

### 3.2 PCF-2 cf_value() uniformity (065 audit)

065 audit verdict UNIFORM at 13 implementations: every cf_value()
implementation across PCF-2 source uses the same continued-fraction
identity convention $L = b_0 + a_1/(b_1 + a_2/(b_2 + \ldots))$ with
the head-class HC0 / HC1 signatures (HC0 = `a_n`-parameterised; HC1
= inline `mp.mpf(1) / x` Wallis style). This is the **PCF identity
implementation-level uniformity audit** at PCF-2 source.

### 3.3 V0 numerical Stokes consistency (096 TIER-A.2)

Verdict `PRE_FIRE_INPUT_R1_GATED`. The intended residual is

$$
\Delta_{\mathrm{RH}} = \bigl|\,|M^* C_V| - |S_{\zeta_*}^{\mathrm{can}}|\,\bigr|
$$

where $M^* = \Phi_{\mathrm{resc}} \circ \Phi_{\mathrm{shift}} \circ
\Phi_{\mathrm{symp}}$ (composite Jacobian). LHS = 51.06556... RHS =
not yet pinned; both quantities R1-gated via 069 / 058R chain.

### 3.4 Source-side equivalence relation (informal)

Picture v1.19 §3 P-MC L440 lists obvious equivalences ("rescaling
$b$, integer translates of $a_0$, etc."). 096 §2.2 carries this
informally; M13 follow-up is the categorical-level closure target.

---

## 4. Pair-wise drift tabulation per identity

### 4.1 Main convergence identity $L = K(a_n, b_n) = b_0 + a_1/(b_1 + \ldots)$

| Milestone | Form | Sign / branch | Status |
|---|---|---|---|
| M5 | $L = b_0 + a_1/(b_1 + a_2/(b_2 + \ldots))$ | Real-positive convergence per §2; conditional on Wallis convergence per §6 Theorem 5 | Canonical |
| M6.CC | Operates on V_quad's $L$ (same identity); transforms via $\Phi_{\mathrm{resc/shift/symp}}$ to canonical form | $\lambda > 0$, $t_0 < 0$ both numerically pinned; symplectic factor R1-gated | Component map; same convergence target |
| M9 | Identity carried via CT v1.3 + 065 audit UNIFORM at PCF-2 implementations | Same | Implementation-level uniformity verified |

**Verdict (main identity):** `PASS_NO_DRIFT`.

Justification: identity $L = K(a_n, b_n)$ is bit-identical across
M5 (PCF-1 v1.3 §2) + M6.CC (058R operates on V_quad's $L$) + M9
(096 + 065 implementation-level audit verdict UNIFORM). Branch and
sign conventions consistent (real-positive convergence of $L$,
$\lambda > 0$ rescaling factor pinned at $1/3$, $t_0 = -4\sqrt{3}$
shift origin pinned).

### 4.2 Spec(K) invariant tuple identity

| Milestone | Form | Status |
|---|---|---|
| M5 | $\operatorname{Spec}(K) = (d, \Lambda, \Delta, \rho, \tau, S, \sigma)$ at v5 | Canonical |
| M6.CC | Carries V_quad's $\operatorname{Spec}(K)$ values into the canonical-form normalization map (e.g. $\Delta = -11$ feeds $\sqrt{-11}$ into V_quad's CM root; $S, \sigma$ as Stokes-axis substrate) | Consistent |
| M9 | $\xi_0$ promoted to THEOREM-GRADE (D2-NOTE v2.1) which sits **next to** $\operatorname{Spec}(K)$ as the M9 V0 invariant target — not the same tuple | Different scopes (M9 V0 carries a derived invariant triple, not the raw Spec(K) tuple) |

**Verdict (Spec(K) tuple):** `PASS_NO_DRIFT`.

Justification: M9 V0's invariant triple $(\Delta_d, \|\Delta\|_{\mathrm{Pet}},
\xi_0)$ is a **derived** target distinct from M5's raw Spec(K) tuple
$(d, \Lambda, \Delta, \rho, \tau, S, \sigma)$; this is by design at
the master-functor target and does not constitute drift.

### 4.3 Balanced discriminant $\Delta = \beta^2 - 4\alpha\gamma$

| Milestone | Form | Status |
|---|---|---|
| M5 | $\Delta = \beta^2 - 4\alpha\gamma$ from $b_n = \alpha n^2 + \beta n + \gamma$; V_quad has $\Delta = -11$ | Canonical |
| M6.CC | $\Delta = -11$ for V_quad implicit in $\sqrt{-11}$ root structure of recurrence; $\zeta_* = 4/\sqrt{3}$ derived from $3 C^2 - 4 = 0$ uses $c_b = 3$ from same recurrence | Consistent (same recurrence input) |
| M9 | $\Delta_d$ at picture v1.19 §3 P-PET row is the **modular discriminant** of the associated curve at degree $d$, not the balanced PCF discriminant | Different objects: M9 $\Delta_d$ ≠ M5 $\Delta$; M5 $\Delta$ feeds M9 $\Delta_d$ via the PCF → curve correspondence |

**Verdict ($\Delta$ identities):** `DRIFT_DETECTED_NON_BLOCKING`.

Justification: M5 uses **balanced PCF discriminant**
$\Delta = \beta^2 - 4\alpha\gamma$; M9 V0 uses **modular discriminant**
$\Delta_d$ of the associated elliptic / hyperelliptic curve; both are
named with the symbol $\Delta$. Picture v1.19 §3 P-PET row is explicit
about $\Delta_d$ being modular-discriminant-valued. 096 TIER-A.1 §3.1
inherits picture v1.19 wording. The notational overlap is documented
across the substrate (no contradiction); rebrand to $\Delta_{\mathrm{PCF}}$
vs $\Delta_d^{\mathrm{mod}}$ is a forward-pointer drafting suggestion
for V0 announcement clarity (NOT-firing-here).

### 4.4 Sharp dichotomy (Conjecture A v5)

| Milestone | Form | Status |
|---|---|---|
| M5 | $\Delta > 0$ (sign of balanced PCF discriminant) ⟹ elementary; $\Delta < 0$ ⟹ PSLQ non-detection at 220 dps / integer-bound $10^{10}$ | Canonical |
| M6.CC | Implicit; M6.CC operates on V_quad which is in the $\Delta < 0$ row | Consistent |
| M9 | Carried via picture v1.19 §3 P-CC + §3 P-MC rows; classification is what M9 announces formally | Consistent |

**Verdict (sharp dichotomy):** `PASS_NO_DRIFT`.

### 4.5 WKB exponent identity (Theorem 5; A ∈ {3, 4})

| Milestone | Form | Status |
|---|---|---|
| M5 | $A \in \{3, 4\}$; $A = 4$ for V_quad; $A = 3$ for QL01/QL02/QL06/QL15/QL26 | Canonical |
| M6.CC | $A = 4$ feeds V_quad's $\xi_0$ Newton-polygon slope as Borel-summability anchor (D2-NOTE v2.1 Theorem 4.1 + B-T 1933 §§7-9) | Consistent |
| M9 | $\xi_0$ THEOREM-GRADE via D2-NOTE v2.1 carries $A \in \{3, 4\}$ implicitly via the Newton-polygon-slope formula | Consistent |
| 066 LANE-2 R1 | V_quad row reframed as deg_a = 0 row member at d = 2 (NOT borderline (i')); PCF-1 v1.3 source UNMODIFIED | NON_BLOCKING (LANE-2 v1.4 amendment forward-pointed; not fired) |

**Verdict (WKB exponent identity):** `DRIFT_DETECTED_NON_BLOCKING`.

Justification: 066 forward-pointer carries a row-attribution change
that is in-scope of LANE-2 W21 OQ disposition. PCF-1 v1.3 source is
unmodified at v1.3. This is the LANE-2 LEAVE_V1_0_CANONICAL discipline.

### 4.6 V_quad → P_III(D_6) reduction identity

| Milestone | Form | Status |
|---|---|---|
| M5 | $(\alpha, \beta, \gamma, \delta) = (1/6, 0, 0, -1/2)$ in P_III(D_6) standard form (PCF-1 v1.3 §7 L494 prose form) | Canonical |
| M6.CC | 4-tuple $(\alpha_\infty, \alpha_0, \beta_\infty, \beta_0) = (1/6, 0, 0, -1/2)$ at CT v1.3 §3.5 reading; null-sum = $-1/3 \neq 0$ violation | KNOWN CARRY-FORWARD (058R-D2; sympy-verified at 069) |
| M9 | Same 4-tuple via 096 §3.2 verbatim citation; secondary Stokes-data classifier conditional on M6.CC R1 closure | Consistent (inheritance pattern) |

**Verdict (V_quad → P_III(D_6) reduction):** `DRIFT_DETECTED_NON_BLOCKING`.

Justification: the 4-tuple null-sum violation is the open M6.CC R1
carry-forward (058R-D2; 069). Reconciliation paths α + β are explicit
at 069r1 envelope. M5's own §7 $(\alpha, \beta, \gamma, \delta)$
prose form is consistent with the 4-tuple reading once Okamoto's
parameter renaming convention is applied. Forward-pointer is named
+ documented; non-blocking.

### 4.7 cf_value() implementation-level uniformity (065 audit)

| Milestone | Form | Status |
|---|---|---|
| M5 | $L = b_0 + a_1/(b_1 + a_2/(b_2 + \ldots))$ canonical Wallis form at PCF-1 v1.3 §2 | Canonical |
| M6.CC | sympy-derived characteristic equation; uses V_quad recurrence directly | Consistent (065 audit row 5 + 6 covers M6.CC adjacent sources at session_B + session_C1) |
| M9 | 13 PCF-2 implementations all UNIFORM per 065 audit | Consistent at implementation level |

**Verdict (cf_value uniformity):** `PASS_NO_DRIFT`.

---

## 5. Aggregate cross-walk-pcf-identity-verdict

| Identity | Verdict |
|---|---|
| Main convergence identity $L = K(a_n, b_n)$ | `PASS_NO_DRIFT` |
| Spec(K) invariant tuple | `PASS_NO_DRIFT` |
| Balanced discriminant $\Delta = \beta^2 - 4\alpha\gamma$ | `DRIFT_DETECTED_NON_BLOCKING` (M9 $\Delta_d$ = modular discriminant; notational overlap documented) |
| Sharp dichotomy (Conjecture A v5) | `PASS_NO_DRIFT` |
| WKB exponent identity (Theorem 5; $A \in \{3, 4\}$) | `DRIFT_DETECTED_NON_BLOCKING` (066 LANE-2 R1 row reframing forward-pointer; PCF-1 v1.3 source UNMODIFIED) |
| V_quad → P_III(D_6) reduction identity | `DRIFT_DETECTED_NON_BLOCKING` (058R-D2 null-sum violation; 069r1 R1-closure preflight envelope drafted) |
| cf_value implementation uniformity | `PASS_NO_DRIFT` (065 audit verdict UNIFORM at 13 implementations) |

**Aggregate (max severity across 7 identities):** `DRIFT_DETECTED_NON_BLOCKING`.

**HALT_097_PCF_IDENTITY_BLOCKING_DRIFT:** **NOT TRIGGERED** (no identity returns
`DRIFT_DETECTED_BLOCKING`).

The three non-blocking items (M5 $\Delta$ vs M9 $\Delta_d$ notational
overlap, 066 LANE-2 R1 row reframing forward-pointer, 058R-D2 null-sum
violation) all have named owners and explicit reconciliation paths
(rebrand suggestion at V0 announcement drafting; LANE-2 v1.4 amendment;
069r1 R1-closure preflight). None block M9 V0 substrate authoring.

---

## 6. AEAL anchor (097-D-1)

* This file SHA-256: computed at fire end; recorded at
  `claims.jsonl` 097-D-1 with `output_hash`.
* Substrate anchors:
  * PCF-1 v1.3 source SHA-256 `E83BB377F297DBF0...4BE301`.
  * picture v1.19 SHA-256 prefix `8BD9043370872F07`.
  * 058R bridge commit `2eb9b28`.
  * 069 handoff at sessions/2026-05-07/CC-VQUAD-PIII-NORMALIZATION-MAP-PHASE-D-NUMERICAL/.
  * 096 TIER-A.1 SHA-16 `14CA0AA1A1AEB176`.
  * 065 cf_value() audit at sessions/2026-05-06/PCF2-CF_VALUE-AUDIT-9IMPLS-065/.
  * 066 LANE-2 R1 row reframing memo at sessions/2026-05-07/PCF1-V13-V_QUAD-ROW-REFRAMING-066/.
  * 060 CMB OQ paste record at sessions/2026-05-06/CMB-OQ-PASTE-W20-051-Q1Q2Q4-EXECUTION/.
  * 099 Q22 deposit-readiness memo at sessions/2026-05-07/T1-Q22-DEPOSIT-READINESS-MEMO-099/
    (path-(a) $|\delta_a| = 3.08904186542 \times 10^{-23}$).

End pcf_identity_cross_walk.md.
