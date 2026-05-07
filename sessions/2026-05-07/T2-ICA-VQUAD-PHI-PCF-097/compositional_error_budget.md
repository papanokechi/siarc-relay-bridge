# Compositional error-budget — M5 → M6.CC → M9

**Relay:** 097 T2-ICA-VQUAD-PHI-PCF
**Phase:** E (Compositional error-budget per Reviewer A BS-3)
**Anchor (substrate):** PCF-1 v1.3 source `p12_pcf1_main.tex`
(SHA-256 `E83BB377F297DBF0...4BE301`), 058R + 069 handoffs,
099 Q22 deposit-readiness memo (sessions/2026-05-07/T1-Q22-
DEPOSIT-READINESS-MEMO-099/), 096 TIER-A.2 numerical-consistency
check (SHA-16 `4EEE6B50973D4BB7`).

Per Reviewer A BS-3: without an end-to-end error budget across
M5 → M6.CC → M9 compositions, the M9 V0 announcement cannot
quantify its uncertainty bounds. The audit below is the
**substrate-level** budget (no NEW computation; aggregates
existing residual measurements at substrate-anchored dps).

---

## 1. Per-link residual inventory

### 1.1 M5 — Theorem 5 / WKB-exponent extraction (PCF-1 v1.3 §6)

PCF-1 v1.3 Table `tab:wkb-exponents` (verbatim L566-577) records
$\alpha_{\mathrm{pred}}$ vs $\alpha_{\mathrm{obs}}$ residual at the
6 $\Delta < 0$ degree-2 PCF families:

| Family | match digits | residual (order of magnitude) |
|---|---|---|
| $V_{\mathrm{quad}}$ | 13 | $\sim 10^{-13}$ |
| QL01 | exact | $0$ |
| QL02 | 13 | $\sim 10^{-13}$ |
| QL06 | 14 | $\sim 10^{-14}$ |
| QL15 | 15 | $\sim 10^{-15}$ |
| QL26 | 13 | $\sim 10^{-13}$ |

**Worst case** (V_quad, QL02, QL26): $\sim 10^{-13}$ at the WKB-exponent
identity level.

**Per-link bound assumption:** least-squares extraction of
$(A, \alpha, \beta_w, \gamma_w)$ on $n \in [15, 120]$ at $K = 12$,
$\mathrm{dps} = 2200$ (PCF-1 v1.3 §6 L555 verbatim) — the residual
is the truncation error at $K = 12$.

### 1.2 M5 → M6.H4 — H4 Stokes-amplitude measurement

058R Phase A re-cite of H4 measurement (Prompt 005 verdict
`H4_EXECUTED_PASS_108_DIGITS`):

* Cross-method amplitude agreement: **108 digits** (forecast 30-50;
  central 40).
* Three independent extractors (ratio test, three-point, Δ²-log)
  cross-validated.
* $|C_V| = 8.127336795495072367\ldots$ at $\ge 108$ dps.
* $\beta_{\text{Gevrey}} = 0$ at $\ge 107$ dps.

**Worst case:** $\sim 10^{-107}$ residual at the H4 measurement
level (V_quad-native normalization).

**Per-link bound assumption:** mpmath dps 250, $N = 5000$ recurrence
depth (per picture v1.19 §6 row 005). The 108-digit cross-method
agreement is at the lowest-dps cross-validator (Δ²-log).

### 1.3 M6.H4 → M6.CC (Birkhoff-formal-series Phase A)

058R Phase A: $\beta_{\text{Gevrey}} = 0$ sympy-verified at the
Birkhoff level, matching H4 measurement to 107 dps.

* Characteristic equation $3 C^2 - 4 = 0$ → $|\zeta_*| = 4/\sqrt{3}$
  is exact (sympy-derived; no precision residual).
* $\lambda = 1/3$ is exact (sympy-derived from $3 C^2 - 4 = 0$
  reduction to canonical $C^2 = 1$).
* $t_0 = -\zeta_* / \lambda = -4\sqrt{3}$ is exact (sympy).
* $|\det J(\Phi_{\mathrm{resc}})| = \lambda^2 = 1/9$ is exact.
* $|\det J(\Phi_{\mathrm{shift}})| = 1$ is exact.

**Worst case at this link:** $\sim 10^{-107}$ from the H4
$\beta_{\text{Gevrey}} = 0$ inheritance (the rest of the Phase A
substrate is sympy-exact).

**Per-link bound assumption:** sympy symbolic exactness at the
Birkhoff-formal-series level; numerical residual carried over from
H4 measurement only at $\beta_{\text{Gevrey}}$ flag.

### 1.4 M6.CC Phase B → Phase D (symplectic factor + Jacobian)

069 Phase D.2.b OBSTRUCTED_R1_GATED:

* $|\det J(\Phi_{\mathrm{symp}})|$ at V_quad parameter point:
  **NOT_COMPUTABLE_R1_GATED** (depends on Phase D.2.b gauge $G(x)$).
* Liouville normal-form invariant $I_V(z) = (3 z^2 + 5 z - 3)/(9 z^3)$
  is sympy-exact (NEW substrate at 069); no precision residual.

**Worst case at this link:** **INCOMPUTABLE** — the symplectic
Jacobian factor blocks the canonical-form Stokes-value
$|S_{\zeta_*}^{\mathrm{can}}|$ assembly. The R1 substrate gap
(Okamoto 1987 §§2-3 Lax-pair primary-source acquisition + KNY
$(a_1, a_2) \to$ BLMP $(e_1, e_2)$ conversion) is the named
upstream owner.

**Per-link bound assumption:** the R1-gating is structural — until
the gauge $G(x)$ is constructible in closed form, this link's
residual cannot be quantified by mpmath (069 Phase D.2.e verdict
honesty rule: PERSIST not PRECISION_DEGRADED, because input
unavailability ≠ floor degradation).

### 1.5 M7 → M9 (j=0 Chowla–Selberg residual; Q22 path-(a))

099 deposit-readiness memo path-(a) substrate (014 prompt verdict
`PASS_A_EQ_6_ONLY`):

* $|\delta_a| = 3.08904186542 \times 10^{-23}$ (max across 4 j=0
  cubic families at K_FIT=7 / dps=25000 / N up to 1200).
* PSLQ on H6 B19+ at maxcoeff=1e50/tol=1e-40 returns no
  Gamma(1/3) closure relation in any family.
* Stretch goal $|\delta| < 10^{-30}$ NOT achieved at K_FIT=7;
  truncation floor at K_FIT=9 / N=2400 / dps≥44300 is
  $\sim 10^{-34}$ per substrate (path-(b) post-deposit stretch).

**Worst case at M7 → M9:** $\sim 10^{-23}$ at the j=0 endpoint
A=6-only branch (path-(a) realization at K_FIT=7, the deposit-eligible
realization).

**Per-link bound assumption:** the residual is the saturation floor
of the 11-param LIN refit at K_FIT=7 / dps=25000 / N up to 1200
(099 §C precedent table verbatim). Path-(b) reduction to $10^{-34}$
is post-deposit stretch (POST-deposit; not deposit gate).

### 1.6 M9 V0 numerical Stokes consistency (096 TIER-A.2)

096 TIER-A.2 verdict `PRE_FIRE_INPUT_R1_GATED`:

* LHS $|2\pi C_V|_{V_{\mathrm{quad}}\text{-native}} = 51.06556\ldots$
  at 50 dps.
* RHS $|S_{\zeta_*}^{\mathrm{can}}|$: **NOT NUMERICALLY AVAILABLE**
  (R1-gated via $|\det J(\Phi_{\mathrm{symp}})|$ chain).
* $\Delta_{\mathrm{RH}} = | |M^* C_V| - |S_{\zeta_*}^{\mathrm{can}}| |$:
  **INCOMPUTABLE** at this fire's time.

**Worst case at this link:** **INCOMPUTABLE** — same R1-gating as
M6.CC Phase D.2.c.

**Per-link bound assumption:** the V0 substrate target is 10 dps
per Reviewer D Q4 recommendation; this is achievable once R1 closes
(target sub-block of `phase_d_numerical.py` from 069 has the script
template ready at mpmath dps = 30+).

---

## 2. End-to-end error-budget table

| Link | Per-link bound | Status |
|---|---|---|
| M5 WKB-exponent (PCF-1 v1.3 Theorem 5) | $\sim 10^{-13}$ at worst across 6 families (V_quad: 13 digits) | BOUNDED |
| M5 → M6.H4 (H4 Stokes-amplitude measurement) | $\sim 10^{-107}$ via 108-digit cross-method agreement | BOUNDED (108-digit margin against 30-50 forecast) |
| M6.H4 → M6.CC Phase A (Birkhoff formal-series) | $\sim 10^{-107}$ inherited from H4 $\beta_{\text{Gevrey}}$; rest sympy-exact | BOUNDED |
| M6.CC Phase A → Phase B (factor pinning $\Phi_{\mathrm{resc}} + \Phi_{\mathrm{shift}}$) | sympy-exact ($\lambda = 1/3$, $t_0 = -4\sqrt{3}$, $|\det J|$ rational) | BOUNDED (exact) |
| M6.CC Phase B → Phase D (symplectic factor + Jacobian) | INCOMPUTABLE (R1-gated; named owner 069r1) | UNBOUNDED-AT-CURRENT-FIRE |
| M7 → M9 ($j = 0$ Chowla–Selberg path-(a) residual) | $\sim 10^{-23}$ at K_FIT=7 (path-(a) deposit-eligible) | BOUNDED |
| M9 V0 numerical Stokes consistency (096 TIER-A.2) | INCOMPUTABLE (R1-gated; 10-dps target post R1-closure) | UNBOUNDED-AT-CURRENT-FIRE |

**End-to-end maximum across links:** dominated by the two
INCOMPUTABLE links (M6.CC Phase D + M9 V0 numerical Stokes
consistency); both R1-gated via the same upstream gap.

**End-to-end minimum across BOUNDED links:** $\sim 10^{-13}$ at the
M5 Theorem 5 WKB-exponent identity (worst case across 6 families;
V_quad sits at 13 digits).

---

## 3. Verdict per Phase E.P3

The relay's verdict choices are:

* `BUDGET_BOUNDED` — all links have finite per-link bounds and a
  finite end-to-end bound is derivable.
* `BUDGET_UNBOUNDED` — no finite end-to-end bound is derivable.
* `INSUFFICIENT_DATA` — at least one link's bound is not yet
  computable but the bound itself is finite-by-construction once
  the upstream gap closes.

**097 Phase E verdict:** `INSUFFICIENT_DATA`.

Justification: 5 of 7 links are BOUNDED at substrate-anchored
precision (dps spans $10^{-13}$ to $10^{-107}$). The 2 R1-gated
links (M6.CC Phase D + M9 V0 numerical Stokes consistency) carry
finite-by-construction residuals — the residual
$\Delta_{\mathrm{RH}} = | |M^* C_V| - |S_{\zeta_*}^{\mathrm{can}}| |$
is well-defined as a finite real number per its mathematical
definition; what's missing is the numerical pin of
$|\det J(\Phi_{\mathrm{symp}})|$ which becomes computable once R1
closes. This is INSUFFICIENT_DATA, not UNBOUNDED.

**HALT_097_BUDGET_UNBOUNDED:** **NOT TRIGGERED** (the end-to-end
bound is derivable in principle and finite-by-construction; current
incomputability is structural-data-availability, not divergence).

---

## 4. Forward-pointed precision targets

Once R1 closes (069r1 R1-closure preflight envelope drafted; paths
α + β explicit), the two currently-INCOMPUTABLE links resolve as
follows:

* **M6.CC Phase D.2.c** $|\det J(\Phi_{\mathrm{symp}})|$ becomes
  pinnable at mpmath dps $\ge 30$ via the gauge $G(x)$ closed form.
* **M9 V0 numerical Stokes consistency** becomes pinnable at the
  Reviewer-D-Q4-target 10 dps; the 069 `phase_d_numerical.py`
  script template runs at mpmath dps = 50 once `det_symp` and
  `S_can` placeholders are resolved.

End-to-end bound at M9 V0 announcement substrate (post R1 closure):
worst case among the 7 links remains $\sim 10^{-13}$ at the
PCF-1 v1.3 Theorem 5 WKB-exponent identity — the M9 V0 announcement
cannot exceed the precision of its weakest contributing component.
The 096 TIER-A.2 10-dps target is consistent with this overall
budget envelope.

---

## 5. AEAL anchor (097-E-1)

* This file SHA-256: computed at fire end; recorded at
  `claims.jsonl` 097-E-1 with `output_hash`.
* Substrate anchors:
  * PCF-1 v1.3 Theorem 5 + Table at sessions/2026-05-01/PCF1-V13-UPDATE/p12_pcf1_main.tex L538-577.
  * 058R Phase A H4 re-cite at sessions/2026-05-06/CC-VQUAD-PIII-NORMALIZATION-MAP-RERE-FIRE/phase_a_birkhoff_match.md.
  * 069 Phase D verdict at sessions/2026-05-07/CC-VQUAD-PIII-NORMALIZATION-MAP-PHASE-D-NUMERICAL/phase_d_numerical.md.
  * 099 Q22 deposit-readiness memo at sessions/2026-05-07/T1-Q22-DEPOSIT-READINESS-MEMO-099/.
  * 096 TIER-A.2 numerical_consistency_check.md SHA-16 `4EEE6B50973D4BB7`.

End compositional_error_budget.md.
