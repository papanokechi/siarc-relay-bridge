# V_quad cross-walk — M5 / M6.CC / M9

**Relay:** 097 T2-ICA-VQUAD-PHI-PCF
**Phase:** B (V_quad parametrization cross-walk)
**Anchor (substrate):** picture v1.19 (SHA-256 prefix `8BD9043370872F07`;
383 291 B; 4 026 lines), PCF-1 v1.3 source `p12_pcf1_main.tex`
(SHA-256 `E83BB377F297DBF0837FACBA257F227DF4579E6A3518C139E3146F17174BE301`;
46 349 B; 925 lines; bridge path
`siarc-relay-bridge/sessions/2026-05-01/PCF1-V13-UPDATE/p12_pcf1_main.tex`),
058R handoff (bridge commit `2eb9b28`), 069 handoff (commit landed
2026-05-07; verdict `UPGRADE_V1_0_PARTIAL_NUMERICAL_PERSIST`),
096 TIER-A.1 `phi_assignment_statement.md` (SHA-16 `14CA0AA1A1AEB176`).

Coefficient ordering convention per repo memory: PCF coefficient
arrays stored LEADING-FIRST.

---

## 1. V_quad parametrization signature per milestone

### 1.1 M5 (PCF-1 v1.3 `p12_journal_main.tex` Theorem 5 row + bridge canonical anchor)

PCF-1 v1.3 §6 Theorem 5 (`thm:wkb`; verbatim L528-548 of bridge anchor)
sets the recurrence-coefficient template

$$
a_n = c_a\,n + \varepsilon_a,
\qquad
b_n = c_b\,n^2 + \beta\,n + \gamma,
$$

with $c_a \in \mathbb{Z}\setminus\{0\}$, $c_b \in \mathbb{Z}_{>0}$, and the
WKB exponent identity (`eq:wkb-alpha`)

$$
A \in \{3, 4\},\qquad
\alpha = A - 2\log c_b + \log|c_a|.
$$

V_quad is read off PCF-1 v1.3 §6 Theorem 5 row table (verbatim L566-577
of bridge anchor):

| Family | $\Delta$ | $A$ | $\alpha_{\mathrm{pred}}$ | $\alpha_{\mathrm{obs}}$ | match digits |
|---|---|---|---|---|---|
| $V_{\mathrm{quad}}$ | $-11$ | $4$ | $4 - 2\log 3 = 1.80277542266378$ | $1.8027754226638$ | $13$ |

V_quad's recurrence-coefficient assignment in the §6 template is

$$
a(n) = 1
\;\Longrightarrow\; (c_a, \varepsilon_a) = (0, 1),
\qquad
b(n) = 3 n^2 + n + 1
\;\Longrightarrow\; (c_b, \beta, \gamma) = (3, 1, 1).
$$

In LEADING-FIRST coefficient-array form (b-side first, then a-side):

* **b-coefficient array** $[c_b,\,\beta,\,\gamma] = [3, 1, 1]$.
* **a-coefficient array** $[c_a,\,\varepsilon_a] = [0, 1]$.
* **Combined 5-tuple** $(c_a, \varepsilon_a, c_b, \beta, \gamma) = (0, 1, 3, 1, 1)$.

The V_quad row is at the §6 table's $A = 4$ upper branch (sole sporadic
member; the five non-V_quad families QL01/QL02/QL06/QL15/QL26 sit at
$A = 3$). The §6 row description treats V_quad as a standalone sporadic
row with $\Delta = -11$.

PCF-1 v1.3 §7 also pins a separate channel-level identification
(verbatim L489-490, 18 words):

> $V_{\mathrm{quad}}$ ($\Delta = -11$) is at present the unique sporadic
> instance with an explicit Painlevé III($D_{6}$) reduction.

with `Painlevé-III($D_6$)` parameters

$$
\alpha = 1/6,\quad \beta = \gamma = 0,\quad \delta = -1/2
$$

(PCF-1 v1.3 §7 L494, prose form). This is the **M5 → M6.CC handoff
data** — M6.CC operates on the same V_quad object identified at M5,
expressed in the Painlevé-III standard parameters.

### 1.2 M6.CC (058R handoff `UPGRADE_V1_0_PARTIAL_NUMERICAL` +
069 handoff `UPGRADE_V1_0_PARTIAL_NUMERICAL_PERSIST`)

058R Phase A pins V_quad's Stokes amplitude in V_quad-native
normalization at $\ge 108$ dps:

* $|C_V| = 8.127336795495072367\ldots$ (V_quad-native; H4 measurement
  per Prompt 005 verdict `H4_EXECUTED_PASS_108_DIGITS`).
* $|2\pi C_V| = 51.06556313995466\ldots$ at mpmath dps = 50 (069
  Phase D substrate; **explicitly NOT** the canonical-form value).
* $\beta_{\text{Gevrey}} = 0$ (logarithmic Borel branch; sympy-verified
  058R Phase A; matches H4 measurement to 107 dps).

058R Phase B + 069 Phase D pin the canonical-form normalization-map
factor data:

* $\Phi_{\mathrm{resc}}$: rescaling factor $\lambda = 1/3$ (058R Phase
  B.1, sympy-derived from characteristic equation $3 C^2 - 4 = 0$);
  $|\det J(\Phi_{\mathrm{resc}})| = \lambda^2 = 1/9$ (069 Phase D.2.c).
* $\Phi_{\mathrm{shift}}$: origin $t_0 = -\zeta_*/\lambda = -4\sqrt{3}
  \approx -6.92820323$ (058R Phase B.2, modulo a global sign);
  $|\det J(\Phi_{\mathrm{shift}})| = 1$ (069 Phase D.2.c).
* $\Phi_{\mathrm{symp}}$: STRUCTURALLY CONSTRUCTIBLE via KNY 2017
  §8.5.17 eq. 8.237–8.239 (058R Phase B.3 R5 closure event);
  $|\det J(\Phi_{\mathrm{symp}})|$ at V_quad parameter point =
  `NOT_COMPUTABLE_R1_GATED` (069 Phase D.2.c, verbatim).

069 Phase D.2.b adds **NEW substrate** not in 058R deposit (069 J4):

* $I_V(z) = (3 z^2 + 5 z - 3)/(9 z^3)$ — Liouville normal-form
  invariant of V_quad's scalar OGF ODE; sympy-derived; gauge-invariant.

The V_quad parameter point in **Painlevé-III canonical form** is
quoted from CT v1.3 §3.5 (Channel-Theory v1.3; Zenodo concept DOI
`10.5281/zenodo.19972394`) as the 4-tuple

$$
(\alpha_\infty,\, \alpha_0,\, \beta_\infty,\, \beta_0)
\;=\; \bigl(\tfrac{1}{6},\, 0,\, 0,\, -\tfrac{1}{2}\bigr).
$$

058R-D2 + 069 anomaly carry-forward note that this 4-tuple sums to
$-1/3 \neq 0$ and therefore **does not satisfy** Okamoto's null-sum
constraint $\alpha_\infty + \alpha_0 + \beta_\infty + \beta_0 = 0$;
sympy-verified at 058R + 069. Reconciliation is the open M6.CC R1
carry-forward (Okamoto-convention identification of CT v1.3 §3.5
four-tuple).

In LEADING-FIRST array form:

* **Painlevé-III 4-tuple** $[\alpha_\infty,\,\alpha_0,\,\beta_\infty,\,\beta_0]
  = [1/6,\,0,\,0,\,-1/2]$.
* **Stokes amplitude scalar** $|C_V| = 8.127336795\ldots$.
* **Borel-plane partner-action distance** $|\zeta_*| = 4/\sqrt{3}$.
* **Normalization-map factor triple** $(\lambda,\,t_0,\,\Phi_{\mathrm{symp}})
  = (1/3,\,-4\sqrt{3},\,\text{R1-gated})$.

### 1.3 M9 (picture v1.19 §3 P-MC + §4 M9 row + 096 TIER-A.1)

Picture v1.19 §4 M9 row (L1019-1056) places V_quad as the canonical
$d = 2$ representative of Source(Phi) with M9-gating clauses
{M4-with-formal-baseline-+-structural-roadmap, M6.CC} and the bare
M6 → M6.CC token-rewrite per 047 D1 split.

096 TIER-A.1 `phi_assignment_statement.md` §2.1 (L42-49) pins V_quad's
M9 role at the assignment level (verbatim quote, 24 words):

> For the quadratic case ($d = 2$), the canonical representative is
> `V_quad` per CT v1.3 §3.5 (Zenodo version DOI
> `10.5281/zenodo.19972394`).

096 TIER-A.1 §3.2 carries the Stokes-data axis as a **secondary
classifier** with explicit conditional flag (verbatim, 22 words):

> $P_{\mathrm{III}}(D_6)$ Stokes data live in the
> $(\alpha_\infty, \alpha_0, \beta_\infty, \beta_0)$ 4-tuple per
> CT v1.3 §3.5 + KNY 2017 §8.5.17 + V1 monodromy maps.

Numerical V_quad anchors at M9 (096 TIER-A.2 `numerical_consistency_check.md`
§2 substrate table) match 058R + 069 verbatim:

* $|C_V| = 8.127336795495072367112578732020\ldots$ at 30 dps.
* $|2\pi C_V| = 51.065563139954662269831674609923147769762888992158\ldots$ at 50 dps.
* $\beta_{\text{Gevrey}} = 0$ at $\ge 107$ dps.

In LEADING-FIRST array form, M9 carries V_quad as the **same 4-tuple
+ scalar combination** that M6.CC pins, plus the M5 recurrence
coefficients carried via CT v1.3 §3.5 citation.

---

## 2. Pair-wise drift tabulation

### 2.1 Pair (M5, M6.CC)

| Axis | M5 (PCF-1 v1.3 §6 + §7) | M6.CC (058R + 069) | Drift type |
|---|---|---|---|
| Parameter list | 5-tuple recurrence $(c_a, \varepsilon_a, c_b, \beta, \gamma) = (0, 1, 3, 1, 1)$ | 4-tuple Painlevé-III $(1/6, 0, 0, -1/2)$ + scalar $C_V$ + factor triple | Definitional translation (different coordinate systems on the same V_quad object) |
| Coefficient ordering | LEADING-FIRST b-array $[3, 1, 1]$ + a-array $[0, 1]$ | LEADING-FIRST 4-tuple $[1/6, 0, 0, -1/2]$ | Both LEADING-FIRST per repo memory |
| Normalization | V_quad-native (Wallis recurrence form) | V_quad-native + canonical-form (gated on $\Phi_{\mathrm{symp}}$) | Composition $\Phi_{\mathrm{resc}} \circ \Phi_{\mathrm{shift}} \circ \Phi_{\mathrm{symp}}$ pinned at first two factors; third factor R1-gated |
| Tuple-vs-record encoding | Tuple (positional) | Tuple (positional) | Consistent |
| 4-tuple null-sum | N/A (M5 does not assert Okamoto null-sum) | Sums to $-1/3 \neq 0$ at CT v1.3 §3.5 (058R-D2 carry-forward; 069 sympy-verified) | KNOWN CARRY-FORWARD (open M6.CC R1) |
| Channel-of-reduction | "third, distinct channel (Borel transform $\mathcal{B}[L](\zeta)$ in the Stokes-constant ODE space)" per PCF-1 v1.3 §7 L712-718 | Borel-plane Stokes-constant ODE per 058R Phase A + 069 | Consistent |
| 066 row reframing | A=4 upper branch sporadic row; LANE-2 R1 reframing as deg_a=0 row member at d=2 forward-pointed (066; PCF-1 v1.3 source UNMODIFIED per LEAVE_V1_0_CANONICAL) | N/A (M6.CC operates on V_quad object directly) | NON_BLOCKING (LANE-2 R1 forward-pointer; v1.4 amendment NOT FIRED) |

**Verdict (M5, M6.CC):** `DRIFT_DETECTED_NON_BLOCKING`.

Justification: the parameter-list difference is a definitional
translation (recurrence-coefficient coordinates ↔ Painlevé-III
parameter-point coordinates) that operates on the same V_quad object
and is the explicit content of the M6.CC normalization-map task. The
4-tuple null-sum violation is a documented carry-forward (058R-D2 +
069) with a named owner (M6.CC R1; 069r1 envelope drafted). The 066
row-reframing forward-pointer is in-scope of LANE-2 W21 OQ disposition;
PCF-1 v1.3 source is unmodified. None of these block M9 V0 substrate
authoring at the assignment level (the same level that 096 already
operates at).

### 2.2 Pair (M6.CC, M9)

| Axis | M6.CC (058R + 069) | M9 (picture v1.19 + 096) | Drift type |
|---|---|---|---|
| V_quad parameter-point | CT v1.3 §3.5 4-tuple $(1/6, 0, 0, -1/2)$ | Same 4-tuple (096 TIER-A.1 §3.2 verbatim) | Bit-identical |
| Stokes amplitude $|C_V|$ | $8.127336795495072367\ldots$ at $\ge 108$ dps (058R Phase A) | Same value at 30 dps (096 TIER-A.2 §2 table) | Bit-identical (M9 truncates dps for substrate purposes) |
| $|2\pi C_V|$ V_quad-native | $51.06556313995466\ldots$ at 50 dps (069 Phase D) | Same value at 50 dps (096 TIER-A.2 §2 table) | Bit-identical |
| $\beta_{\text{Gevrey}}$ | $0$ at $\ge 107$ dps | $0$ at $\ge 107$ dps | Bit-identical |
| R1 status | NOT_COMPUTABLE_R1_GATED (069 Phase D.2.c) | INHERITS R1-gating; 096 TIER-A.2 verdict `PRE_FIRE_INPUT_R1_GATED` | Consistent (inheritance pattern) |
| Functoriality / categorical level | Component map $\Phi_{\mathrm{symp}} \circ \Phi_{\mathrm{shift}} \circ \Phi_{\mathrm{resc}}$ | Master $\Phi$ at assignment level (G7 substrate gap inherited) | Different scopes (M6.CC = component, M9 = master) |
| Canonical-vs-native distinction | Explicit anti-circularity guard (069 §HALT_OVER_CLAIM checklist item 3 forbids using V_quad-native $2\pi C_V$ as canonical-form stand-in) | 096 TIER-A.2 §3 quotes 069 verbatim and inherits the same anti-circularity discipline | Bit-identical |

**Verdict (M6.CC, M9):** `PASS_NO_DRIFT`.

Justification: every numerical value and every parameter-list element
flows from M6.CC into M9 by verbatim citation. The R1-gating is an
inheritance, not a drift. The anti-circularity discipline (do not
substitute V_quad-native for canonical-form) is preserved.

### 2.3 Pair (M5, M9)

| Axis | M5 (PCF-1 v1.3) | M9 (picture v1.19 + 096) | Drift type |
|---|---|---|---|
| V_quad recurrence | $a(n) = 1$, $b(n) = 3 n^2 + n + 1$ (PCF-1 v1.3 §6 L566 verbatim) | Carried via CT v1.3 §3.5 citation (096 TIER-A.1 §2.1 verbatim) | Cited not redefined |
| Painlevé-III parameter-point | Pin $\alpha = 1/6, \beta = \gamma = 0, \delta = -1/2$ (§7 L494 prose) | 4-tuple $(1/6, 0, 0, -1/2)$ (096 TIER-A.1 §3.2 verbatim) | Same numerical content; M5 prose form vs M9 4-tuple form |
| Channel of reduction | "third, distinct channel (Borel transform $\mathcal{B}[L](\zeta)$ in the Stokes-constant ODE space)" (§7 L712-718) | Same channel anchored via M6.CC pipeline (096 TIER-A.1 §3.2 + 058R) | Consistent |
| WKB exponent $A$ | $A = 4$ for V_quad (PCF-1 v1.3 §6 L545 verbatim) | NOT carried at the assignment-level statement; 096 TIER-A.1 references 064 supplement four-row Phase A enumeration in DEPENDS_ON section | LANE-2 R1 forward-pointer; PCF-1 v1.3 source UNMODIFIED |
| 066 LANE-2 row reframing | Source unmodified at v1.3 (LANE-2 Item 3 `LEAVE_V1_0_CANONICAL`); v1.4 amendment forward-pointed (NOT FIRED) | 096 TIER-A.1 cites V_quad as canonical $d = 2$ representative without restating the A=4 row attribution | Consistent within the LANE-2 LEAVE_V1_0_CANONICAL discipline |

**Verdict (M5, M9):** `DRIFT_DETECTED_NON_BLOCKING`.

Justification: every M5-side numerical / parametric element is either
verbatim-cited at M9 (via CT v1.3) or held in a forward-pointer state
under the LANE-2 LEAVE_V1_0_CANONICAL discipline. No contradiction;
no semantic loosening; non-blocking.

---

## 3. Aggregate cross-walk-vquad-verdict

| Pair | Verdict |
|---|---|
| (M5, M6.CC) | `DRIFT_DETECTED_NON_BLOCKING` |
| (M6.CC, M9) | `PASS_NO_DRIFT` |
| (M5, M9) | `DRIFT_DETECTED_NON_BLOCKING` |

**Aggregate (max severity across 3 pairs):** `DRIFT_DETECTED_NON_BLOCKING`.

**HALT_097_VQUAD_BLOCKING_DRIFT:** **NOT TRIGGERED** (no pair returns
`DRIFT_DETECTED_BLOCKING`).

The single substantive non-blocking item is the CT v1.3 §3.5 4-tuple
Okamoto null-sum violation (sums to $-1/3$), which is the open M6.CC
R1 carry-forward (named owner: 069r1 envelope). M9 V0 substrate
inheritance via 096 TIER-A.1 + TIER-A.2 already absorbs this as a
`PRE_FIRE_INPUT_R1_GATED` flag at the secondary-classifier axis.

---

## 4. AEAL anchor (097-B-1)

* This file SHA-256: computed at fire end; recorded at
  `claims.jsonl` 097-B-1 with `output_hash`.
* Substrate anchors:
  * picture v1.19 SHA-256 prefix `8BD9043370872F07`.
  * PCF-1 v1.3 source SHA-256 `E83BB377F297DBF0...4BE301` (bridge-deposit).
  * 058R bridge commit `2eb9b28` (handoff verdict
    `UPGRADE_V1_0_PARTIAL_NUMERICAL`).
  * 069 handoff verdict `UPGRADE_V1_0_PARTIAL_NUMERICAL_PERSIST`
    (sessions/2026-05-07/CC-VQUAD-PIII-NORMALIZATION-MAP-PHASE-D-NUMERICAL/).
  * 096 TIER-A.1 SHA-16 `14CA0AA1A1AEB176`.
  * 096 TIER-A.2 SHA-16 `4EEE6B50973D4BB7`.
  * 066 PCF1-V13 reframing memo (sessions/2026-05-07/PCF1-V13-V_QUAD-ROW-REFRAMING-066/).

End vquad_cross_walk.md.
