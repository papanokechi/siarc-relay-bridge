# Phase A — T1 Phase 2 substrate readback + G24 A_fit gate + 064/066/067 supersession check

**Task ID:** `T1-PHASE-3-COSTIN-BORDERLINE-M4-CLOSURE-068`
**Phase:** A (substrate readback + supersession gate)
**Date:** 2026-05-07 (W20 dispatch)

---

## A.0 Supersession gate — `Q.SUP` answer (P10)

**Question (verbatim from relay 068 §PHASE A.0):**

> "Is the SIARC stratum's operative row IN the deg_a=0 row reading per
> 064 + LANE-2 R3? AND does that row carry A_naive = 2d at d ∈ {2, 3, 4}
> via three-convention enumeration?"

**Substrate consulted:**

1. 064 supplement
   `phase_a_supplementary_deg_a_zero.md` (SHA `80E28568FF142B1A…`,
   16792 B), §2.2 "New deg_a = 0 row (substrate citation: P3 + V6)"
   verbatim:

   > "Applying balance (III) at deg_a = 0 — the SIARC PCF corner used by
   > every harvest implementation per LANE-2 P1 — yields a fourth row at
   > each value of d. P2 substrate
   > (`independent_depth_probe.md` L121-126) records the three new rows
   > verbatim:
   >
   > | d | Convention            | deg a | deg b | μ_dom | μ_sub | A_naive |
   > |---|-----------------------|-------|-------|-------|-------|---------|
   > | 2 | (1, b) PCF-2 corner   | 0     | 2     | 2     | −2    | **4**   |
   > | 3 | (1, b) PCF-2 corner   | 0     | 3     | 3     | −3    | **6**   |
   > | 4 | (1, b) PCF-2 corner   | 0     | 4     | 4     | −4    | **8**   |"
   > (064 §2.2)

2. LANE-2 V6 substrate
   `independent_substrate_verification.md` (SHA `56063BF7BA8AD6A0…`,
   15695 B), §V6 Step 4, L274-282 verbatim:

   > "**A_naive = μ_dom − μ_sub = d − (−d) = 2d** (when deg_a = 0).
   > … General formula: **A_naive = 2d − d_a**." (V6, L274-282)

3. 065 cf_value audit
   `cf_value_audit_pcf2_9impls.md` (SHA `16512BCC71C9A19E…`,
   11700 B), §2 verbatim tally:

   > "HC1 (strict inline `mp.mpf(1)`): **12 of 13**;
   > HC0 (parameterised, default `lambda n: mp.mpf(1)`): **1 of 13**
   > (`evaluate_cf`); PARAM (deg_a > 0 actively dispatched):
   > **0 of 13**." (065 §2)

4. 066 V_quad row reframing
   `pcf1_v13_v_quad_row_reframing.md` (SHA `79933B694DD2BF99…`,
   24073 B), V_quad declaration verbatim from
   `algebraic_independence_audit.py` L37-40:

   > "`VQUAD_ALPHA = [1]`, i.e., a(n) ≡ 1, deg_a = 0"

   With row-membership re-attribution: V_quad's empirical A = 4 at
   d = 2 aligns with the deg_a = 0 row at A_naive = 2d = 4, not the
   α-direction row at A_naive = 3 (which had been the prior
   attribution under the three-convention enumeration of T1 Phase 2).

**Q.SUP answer: YES**

The SIARC stratum's operative row (the `(1, b)` PCF-2 corner where
a_n ≡ 1, equivalently deg_a = 0) IS in the four-row Phase A
enumeration of 064 §2.3, and that row carries A_naive = 2d at every
d ∈ {2, 3, 4} via the four-row enumeration (deg_a ∈ {0, d-1, d, d+1}).
Moreover, the closed-form general formula A_naive = 2d − d_a
(V6 L274-282) extends to general d ≥ 2 with d_a = 0, yielding
A_naive = 2d uniformly.

Per relay 068 §PHASE A.0 outcome (i):

> "Q.SUP = YES (064 deg_a=0 row gives A_naive=2d on the operative row):
> the M4 closure is ALREADY achieved at the algebraic-combinatorial
> level. This phase still runs Phases B/C/D as a SECONDARY formal-
> asymptotic-level verification (Costin Gevrey-1 sectorial-summability
> + B-T fractional rank cross-check), NOT as the primary closure
> mechanism. Verdict defaults to UPGRADE_FULL_VIA_DEG_A_ZERO_ROW with
> Costin/B-T as confirming evidence."

**Default verdict path (subject to Phase E re-evaluation under the
5-item HALT_068_OVER_CLAIM checklist):**
`UPGRADE_FULL_VIA_DEG_A_ZERO_ROW`.

`HALT_068_PHASEA_REFRAMING_CONFLICT`: NOT TRIGGERED.

---

## A.1 T1 Phase 2 substrate readback (P2 gate)

**Bridge anchor:** `37c939f`
(`T1-BIRKHOFF-PHASE2-LIFT-LOWER`, deposit at
`siarc-relay-bridge/sessions/2026-05-03/T1-BIRKHOFF-PHASE2-LIFT-LOWER/`).

### A.1.1 Verdict tag

`UPGRADE_PARTIAL_FORMAL_LEVEL` (Phase D verdict at
`phase_d_verdict.md` SHA `7145A00D62B9716C…`).

Verbatim from L57-79 of `phase_d_verdict.md`:

> "Phase A + B establish the formal Newton-polygon baseline
> A_naive ≤ d+1 (naive Wimp-Zeilberger normal case), recovering only
> the LOWER end of the literature bracket A ∈ [d, 2d]. The lift to
> A = 2d at d ≥ 3 requires the SIARC PCF stratum to sit at the
> BORDERLINE case deg_a = 2 deg_b of Wimp-Zeilberger 1985 (equivalently,
> the anormal / fractional rank q ≥ 2 case of B-T 1933 §1) OR at an
> exceptional locus of the normal case where leading coefficients
> cancel."

### A.1.2 Phase A naive Wimp-Zeilberger Newton-polygon result

Phase A summary (`phase_a_summary.md` SHA `71CAC875C98A6CE8…`)
L34-44 enumerates **three** SIARC conventions
(α/symmetric/δ-direction) at deg_a ∈ {d-1, d, d+1}:

| d | Convention   | deg a | deg b | μ_dom | μ_sub | A_naive |
|---|--------------|-------|-------|-------|-------|---------|
| 2 | α-direction  | 1     | 2     | 2     | −1    | 3       |
| 2 | symmetric    | 2     | 2     | 2     |  0    | 2       |
| 2 | δ-direction  | 3     | 2     | 2     |  1    | 1       |
| 3 | α-direction  | 2     | 3     | 3     | −1    | 4       |
| 3 | symmetric    | 3     | 3     | 3     |  0    | 3       |
| 3 | δ-direction  | 4     | 3     | 3     |  1    | 2       |
| 4 | α-direction  | 3     | 4     | 4     | −1    | 5       |
| 4 | symmetric    | 4     | 4     | 4     |  0    | 4       |
| 4 | δ-direction  | 5     | 4     | 4     |  1    | 3       |

Phase 2 maximum row entry: A_naive = 5 at d=4 α-direction. Maximum
under three-convention enumeration: A_naive ≤ d+1 (the Phase 2
formal-baseline upper bound).

### A.1.3 Phase B sweep d ∈ [3, 8]

Phase B sweep (`phase_b_extended_sweep.py` execution; output at
`phase_b_run_output.txt`) records structural uniformity: the three-row
maximum A_naive = d + 1 holds uniformly for d ∈ {3, 4, 5, 6, 7, 8}
under the α-direction convention. No row in the three-convention
enumeration carries A_naive = 2d at d ≥ 3. The structural lift to
A = 2d under that enumeration would have required the BORDERLINE
case (deg_a = 2 deg_b) or the EXCEPTIONAL locus (leading coefficient
cancellation), per Phase D verdict §70-79.

### A.1.4 Phase C B-T 1933 §§7-9 verbatim (existence + factorization)

Phase C reads B-T 1933 §§7-9 verbatim; produces extracts C.1-C.5 in
`phase_c_literature_verification.md` (SHA `C6CC2B1AC437647F…`):

- C.1 §7 Theorem II (point-of-division + completely-proper product;
  OCR L1686-1730);
- C.2 §8 Lemma 10 (extension to wider sub-region; OCR L2249-2253);
- C.3 §9 Fundamental Theorem (each quadrant completely proper;
  OCR L2700-2705);
- C.4 §9 Definition 10 (point of separation / Q*-factorization;
  OCR L2723-2730);
- C.5 §11 Theorem III (converse / existence direction; OCR L2692-2705).

Phase C verdict: `C_LITERATURE_UNIFORM_AT_NORMAL_CASE` — the §§7-9
machinery applies to the SIARC stratum at the existence /
factorization / sectorial-realization level, but does NOT identify
A = 2d specifically.

### A.1.5 Strategic implication carried forward

The three-convention enumeration of Phase 2 (`phase_a_summary.md`
L34-44) **excluded the deg_a = 0 corner** by ASSUMPTION (the SIARC
α/symmetric/δ-direction convention triple covered deg_a ∈
{d-1, d, d+1} only). Phase 2 verdict identified the lift gap as
requiring either borderline mechanism (i') or exceptional-locus
mechanism (ii'); the LANE-2 cascade (064 + 066 + 067) reframed the
gap by extending the enumeration to four rows including deg_a = 0
(LANE-2 R3). Under the four-row enumeration, the deg_a = 0 row
carries A_naive = 2d uniformly across d ∈ {2, 3, 4} (and, by V6 L274-282,
across general d ≥ 2 with d_a = 0).

This is the supersession path of A.0 outcome (i): the formal-baseline
gap closes at the algebraic-combinatorial level via the four-row
enumeration, without invoking borderline mechanism (i') or
exceptional-locus mechanism (ii').

---

## A.2 G24 A_fit definition gate (P6)

**Substrate:** `PCF2-V13-AFIT-DEFINITION-READBACK` deposit at
`siarc-relay-bridge/sessions/2026-05-04/PCF2-V13-AFIT-DEFINITION-READBACK/handoff.md`
(L1-120 cited).

**Verdict:** `UPGRADE_G24_DEFINITIONS_MATCH_PHASE2_ANOMALY_REAL`.

Verbatim from G24 readback handoff L21-26 + L97-103:

> "PCF-2 v1.3 measures A as the (negative) coefficient of n log n in
> the asymptotic expansion of log|δ_n| where δ_n = p_n/q_n − L,
> which is structurally μ_dom − μ_sub — the same quantity Phase A
> computes from Newton-polygon balance."

> "The PCF-2 v1.3 A_fit corresponds to choice (a): the n log n
> coefficient in the asymptotic of log|δ_n|, which equals
> μ_dom − μ_sub when δ_n is read as the subdominant-over-dominant
> ratio of the recurrence solution pair. This is the SAME quantity
> Phase A (`T1-BIRKHOFF-PHASE2-LIFT-LOWER` Phase A) computes."

PCF-2 v1.3 eq. (B4) verbatim
(`pcf2_program_statement.tex` SHA `82FE2315CFDA2047…` L459-466):

> "the convergent residual δ_n = p_n/q_n − L has leading WKB
> asymptotic … log|δ_n| = −A n log n + α n − β log n + γ + o(1)
> (n → ∞), with the sharp identification A = 2d"

**P6 gate:** PASSES. A_fit (PCF-2 v1.3 eq. (B4)) ≡ μ_dom − μ_sub
≡ A_naive (Phase A Newton-polygon balance) ≡ A_naive at deg_a = 0
under the four-row enumeration of 064 §2.3.

`HALT_068_A_FIT_DEFINITION_DRIFT`: NOT TRIGGERED.

---

## A.3 Synthesis paragraph

**Pre-LANE-2-cascade state (T1 Phase 2 verdict, bridge `37c939f`):**

- Formal baseline: A_naive ≤ d+1 (naive WZ Newton-polygon, three-
  convention enumeration α/symmetric/δ at deg_a ∈ {d-1, d, d+1}).
- Empirical: A_fit ≈ 2d at d ∈ {3, 4} (110/110 at dps ∈ {800, 1200}
  per PCF-2 v1.2 release).
- Gap = 2d − (d+1) = d − 1 at the borderline; framed structurally as
  requiring mechanism (i') (borderline deg_a = 2 deg_b) or mechanism
  (ii') (exceptional locus where leading coefficients cancel).

**Post-LANE-2-cascade state (064/066/067 + V6 substrate):**

- Closed-form general formula: A_naive = 2d − d_a (V6, §V6 Step 4,
  L274-282, derived independently from quadratic-formula ratio
  analysis + Stirling's approximation + Birkhoff-Trjitzinsky two-
  solution structure).
- At deg_a = 0 (the SIARC stratum's operative row per LANE-2 P1
  + 065 audit + 066 V_quad row-membership): A_naive = 2d at general
  d ≥ 2.
- Gap closes at the algebraic-combinatorial level via the four-row
  enumeration; mechanism (i') and mechanism (ii') are NOT required.
- 067 v1.0 follow-up note (5 pp) records the four-row enumeration
  and the V_quad row-membership re-attribution as additive extension
  to bt_baseline_note v1.0.

**Phase A → Phase B/C/D handoff:**

Per A.0 outcome (i), Phases B/C/D run as SECONDARY formal-asymptotic-
level verification, NOT as primary closure mechanism:

- Phase B (Costin Borel-Laplace radius theorem + Gevrey-1 sectorial-
  summability) → corroborates that the formal series for the SIARC
  stratum at deg_a = 0 sits in the Gevrey-1 / Borel-summable class
  in the nonresonant two-solution sense, with Stokes-ray /
  resurgent-singularity radius bounded below by the smallest
  exponential gap |λ_1|.
- Phase C (B-T 1933 §1 anormal q=2 ansatz) → corroborates that the
  canonical formal-solution form e^{Q(x)} s(x) is consistent with
  the four-row
  enumeration; the deg_a = 0 row is the **normal-case** entry
  (p = 1; γ = log γ_dom = log(c_b e^{−d}) per V6 §V6 Step 2),
  NOT an anormal q=2 entry. The borderline q=2 ansatz is therefore
  not the operative closure mechanism for the SIARC stratum;
  the four-row deg_a = 0 closure is normal-case throughout.
- Phase D (M4 closure attempt) → assembles the closure: A = 2d at
  general d ≥ 3 via the deg_a = 0 row of 064 §2.3 + V6 closed-form,
  cross-checked numerically at d ∈ {3, 4} against PCF-2 v1.2 empirics.

---

## A.4 Phase A handoff signal

| Gate | Status | Detail |
|------|--------|--------|
| P1 (rule5 grounding) | PASSES | All claims cite SHA + line range |
| P2 (T1 Phase 2 substrate) | PASSES | Bridge `37c939f` deliverables present at SHA prefixes listed in `substrate_anchor_shas.md` §1.1 |
| P3 (Costin chap5 on disk) | PASSES | SHA `93F1E9BF0A5FC4F6…` verified; Theorem 4.147 + Theorem 5.11 line ranges captured |
| P4 (B-T 1933 §1 ansatz) | PASSES | OCR text dump SHA `5FBB3E2FDC7AC71E…` verified; canonical-form ansatz at L107-118 + normal/anormal classification at L131-142 |
| P5 (PCF-2 R1.1+R1.3+Q1 empirics) | PASSES | Cubic 5.978±0.026 dps=800 + quartic 7.954±0.0037 dps=1200; PCF-2 v1.2 claims SHA referenced |
| P6 (G24 A_fit definition) | PASSES | UPGRADE_G24_DEFINITIONS_MATCH_PHASE2_ANOMALY_REAL verdict at bridge `8ed7417` |
| P7 (forbidden-verb hygiene) | DEFERRED to STEP 6a | Self-check after deliverable bundle complete |
| P8 (verdict-ladder honesty) | DEFERRED to STEP 6b | Self-check after Phase E |
| P9 (d=2 V_quad sanity) | PASSES | V_quad sits at deg_a=0 row at d=2 per 066; A=4=2d aligns; no incompatibility with V_quad d=2 empirical Stokes data |
| P10 (064/066/067 supersession) | Q.SUP = YES | A.0 outcome (i): UPGRADE_FULL_VIA_DEG_A_ZERO_ROW path |

Phase A halts: 0.

Proceed to Phase B.

---

*End of `phase_a_substrate_readback.md`.*
