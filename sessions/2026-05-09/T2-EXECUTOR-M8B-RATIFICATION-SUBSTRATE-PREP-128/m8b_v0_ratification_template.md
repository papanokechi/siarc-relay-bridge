# M8b V0 closure ratification template (synth-tier)

**Purpose**: paste-ready audit artifact for the next M-axis
absorption cycle (synth-tier solo-dispatch, slated for slot 129).

**Pre-stage drafted**: at bridge HEAD `7f93b9e`
(T1-SYNTH-M7-V0-CLOSURE-CASCADE-123).
**Drafted by**: T2-EXECUTOR (GitHub Copilot, VS Code; Claude
Opus 4.7 xhigh) at 2026-05-09 ~15:05 JST.
**Used by**: T1-Synth (Claude.ai web), at slot 129 solo-dispatch.

**Mirror anchors** (mirror-of, not copy-of):

* M4 V0 substrate-prep: `siarc-relay-bridge/sessions/2026-05-08/M4-RATIFICATION-SUBSTRATE-PREP-105/m4_substrate_excerpts.md` (bridge `d1e19e9`)
* M7 V0 substrate-prep: `siarc-relay-bridge/sessions/2026-05-09/T2-EXECUTOR-M7-RATIFICATION-SUBSTRATE-PREP-121/m7_v0_ratification_template.md` (bridge `f4b6de8`)
* M4 V0 ratification template (executed): `tex/submitted/control center/m4_v0_ratification_template.md`
* M7 V0 closure cascade (just-landed precedent for soft/hard-branch carry-forward semantic): `siarc-relay-bridge/sessions/2026-05-09/T1-SYNTH-M7-V0-CLOSURE-CASCADE-123/handoff.md` (bridge `7f93b9e`)

Section numbering and decision-form structure are aligned with the
121 M7 template; M8b-specific content fills the slots. The M8b axis
is qualitatively different from M4 / M7 in **closure type**: where
M4 V0 closes via structural cancellation (deg_a=0 row mechanism)
and M7 V0 closes via PSLQ exhaustion in soft branch
(no-Γ(1/3)-relation in the H6 dedup B19+ basis), M8b V0 closes via
**numerical-foreclosure-by-residual-acceptance**: four independent
methodological lenses report the d=2 sub-leading alien amplitude
$S_2$ as below the resolution floor of laptop-feasible Borel-Padé
methodology, and the closure is the *acceptance of that residual*,
not a positive numerical determination.

---

## §1. M8b axis scope

### What the M8b axis represents

Per **picture v1.19 § 4** (bridge `70d1a48`,
`sessions/2026-05-06/PICTURE-V19-CONSOLIDATED-DEPOSIT/picture_v1.19.md`),
the M8b axis is:

> **M8b: Stokes-multiplier $S_2$ structural closure post-numerical-
> foreclosure (PCF-1 §3 sign-of-$\Delta_b$ dichotomy at the
> Stokes-multiplier scale)**

This is the d=2 PCF-1 §3 sign-of-$\Delta_b$ dichotomy axis. The
question is whether the second alien amplitude $S_2$ at the next
Borel-singularity rung $u = 2 \zeta_*$ can be numerically
extracted from the cached recurrence series at laptop-feasible
precision, and used to discriminate the $\mathrm{sign}(\Delta_b)$
dichotomy. The leading-rung amplitude $S_1$ was successfully
measured at 010 (T35 Stokes-multiplier discrimination); $a_1$ was
3-stratum partitioned at 017c+017e+017L; $S_2$ is the next-rung
sub-leading amplitude.

The closure type for M8b V0 is **numerical-foreclosure-by-residual-
acceptance** (G6b classification): four independent methodological
lenses (017c LSQ at dps=250 N=2000, 017e extended LSQ at dps=400
N=5000, 017m subtracted-high-order Borel-Padé at M=200..800, 092
raw-low-order Borel-Padé at small (N,M)) all fail to extract $S_2$
at the spec extraction threshold, **and the failures are
methodological** (not precision-floor failures that further compute
would resolve). The mathematical content (alien amplitude $S_2$) is
not falsified by these foreclosures; only the *laptop-feasible
numerical extraction path* is foreclosed. The d≥3 binding-window
structural dispatch is **forward-pointed not-blocking** via the
P-009 caveat (relay 050 active variant v1: `NOT_YET_DISPATCHED`).

### What "M8b V0 closure" means specifically

M8b V0 closure is the **numerical-foreclosure-by-residual-acceptance
closure** (cf. picture v1.19 row at line 802 / G6b classification
in 092 verdict). The four-lens negative result substrate at
verified bridge SHAs:

| Lens | Verdict / Halt | Bridge SHA | Method | Failure mode |
|---|---|---|---|---|
| **017c** (T37-S2-EXTRACTION-POLYNOMIAL-AWARE) | Stage-2-LSQ branch foreclosed at d=2 | (picture v1.19 § 5 line 306) | dps=250 N=2000 polynomial-aware LSQ on $T_n := a_n \zeta_*^n / \Gamma(n)$ | D-extraction relative half-range $\sim 10^4$ to $10^{217}$; envelope spans 0 |
| **017e** (T37E-EXTENDED-RECURRENCE) | Stage-2-LSQ branch foreclosed at d=2 (re-confirmed) | `sessions/2026-05-02/T37E-EXTENDED-RECURRENCE/` | dps=400 N=5000 extended LSQ | Rel half-range $\sim 4.7 \times 10^{217}$; envelope STILL spans 0; **methodological** failure not precision floor |
| **017m** (T37M-DIRECT-BOREL-D-EXTRACTION) | `HALT_T37M_PADE_DIVERGENT` | `sessions/2026-05-03/T37M-DIRECT-BOREL/` | direct Borel-Padé subtracted-high-order at M=200..800 with K=25 cleanness step | 9/12 RANK_LOSS per rep at high-(N,M); numerical Hankel singularity |
| **092** (T1-017M-BOREL-PADE-S2-092) | `M8b_S2_PERMANENT_RESIDUAL_VIA_BOREL_PADE` (`COMPLETE_PERMANENT_RESIDUAL`) | `14e6b09` | raw-low-order Borel-Padé at small (N,M) ∈ {6..18}, dps=300, all 4 reps | 0/84 adjacent (N,M) pairs reach dps/4=75 digit threshold; rel half-range 2.14–76.85 across reps; no convergence-region |

The 092 fire (2026-05-07) is the **operative M8b V0 closure fire**:
it constitutes the orthogonal (raw + low-order) Borel-Padé methodology
quadrant complementing 017m's (subtracted + high-order) failure, and
classifies all four reps at `PERMANENT_RESIDUAL_G6b`. The aggregate
M8b-axis verdict is `M8b_S2_PERMANENT_RESIDUAL_VIA_BOREL_PADE`
(092 `verdict.md`).

The M8b V0 closure statement is therefore:

> **M8b V0 CLOSED via numerical-foreclosure-by-residual-acceptance
> at the d=2 PCF Stokes-multiplier $S_2$ scale. Four independent
> methodological lenses (017c LSQ; 017e extended LSQ; 017m
> subtracted-high-order Borel-Padé HALT; 092 raw-low-order
> Borel-Padé `PERMANENT_RESIDUAL_G6b` across all 4 reps with
> 0/84 adjacent (N,M) pairs reaching the dps/4=75 digit
> threshold) report $|S_2|$ below the resolution floor of
> laptop-feasible Borel-Padé methodology. Mathematical content
> (alien amplitude $S_2$) is NOT falsified; only the laptop-
> feasible numerical extraction is foreclosed. The d≥3 structural
> binding-window dispatch is forward-pointed not-blocking
> (P-009 caveat active variant v1 `NOT_YET_DISPATCHED`). M8b is
> NOT in the M9 V0 gating set ($M9$ gating $= \{M4, M6\}$);
> M8b is enrichment, not gate.**

### Manuscript section(s) M8b closure feeds

* **PCF-1 §3** (sign-of-$\Delta_b$ dichotomy) — M8b is the
  Stokes-multiplier-scale resolution path for the dichotomy. The
  dichotomy at the leading-rung $|S_1|$ scale was discriminated at
  010 (T35 discrimination, 4 reps); the next-rung $|S_2|$ scale is
  numerically foreclosed per the 4-lens substrate. The PCF-1 §3
  manuscript wording carries the foreclosure as a **note** rather
  than as a claim against the dichotomy (per CMB.txt L998–1018:
  "M9 announcement does not depend on the value of $S_2$; M8b is
  enrichment, not gate").
* **PCF-2 v1.4** (post-V0-closure §X amendment, if any) — under
  RULE 1 the math-content step (any §X note acknowledging M8b
  foreclosure-by-residual-acceptance) is in scope; the Zenodo
  deposit step is **TABLED**. No specific §X amendment is
  mandated by M8b V0 closure (M8b is not a PCF-2 §6-style
  numerical-claim amendment; it is a structural axis closure).
* **CMB.txt L941–998 + L1153–1156 + L1467–1488 + L1518–1530**
  (P-009 caveat block; bridge `tex/submitted/CMB.txt`) — already
  carries the d=2 foreclosure note ("Stokes-multiplier
  discrimination at d=2 numerically foreclosed; only S_1 reached
  spec precision; future structural revival possible at d≥3"
  per CMB.txt context). The M8b V0 closure is consistent with
  this wording and does not require CMB amendment.
* **P-009 d≥3 binding-window caveat** (bridge `1873538`,
  `sessions/2026-05-06/P009-M8B-CAVEAT-FINAL/p009_m8b_caveat_active.txt`)
  — active variant v1 `NOT_YET_DISPATCHED`:
  > "Stokes-multiplier discrimination (companion milestone M8b)
  > will supply an additional independent test of the SIARC
  > stratification at d≥3, conditional on the M8b dispatch
  > landing within the relevant binding window and on the
  > binding-window result."
  This caveat is **carried-forward unchanged** by the M8b V0
  closure. The V0 closure addresses d=2 numerical foreclosure;
  the d≥3 caveat addresses the structural binding-window
  dispatch which has not been fired. These are different scopes
  and the V0 closure must reconcile (not modify) the caveat
  language.
* **Picture chain v1.20+** (forward-pointed): the closure tag at
  v1.20+ should read
  `M8b_V0_CLOSED (NUMERICAL-FORECLOSURE; d≥3-CAVEAT-CARRIED-FORWARD)`
  per the M4 V0 / M7 V0 cascade pattern (105 → 106
  `(MEDIUM-HIGH; HIGH-PENDING)`; 121 → 123
  `(SOFT-BRANCH; HARD-BRANCH-PENDING)` per
  most-conservative-band protocol). The annotation prevents
  silent inheritance of unqualified closure state.

### Relationship to M4 V0 / M7 V0 (closed) and M8a (parallel cycle)

* **M4 V0** (closed 2026-05-08 at MEDIUM-HIGH confidence; bridge
  cascade 105 → 106): structural deg_a=0 row mechanism. M4 V0
  was the procedural gate per peer-consult 104
  V_FT4_RECOMMENDED. With M4 V0 closed, M7 / M8a / M8b
  ratification cycles are unblocked.
* **M7 V0** (closed 2026-05-09 at MEDIUM-HIGH per most-
  conservative dual-witness band aggregation; bridge cascade
  121 → 122 → 123): soft-branch PSLQ exhaustion. The M7
  cascade-absorption fire at 123 established the most-
  conservative-band protocol for dual-witness aggregation; this
  protocol applies if the M8b ratification at 129 produces a
  similar dual-reviewer divergence.
* **M8a** (parallel ratification cycle; substrate-prep at slot
  125 same slate; solo-dispatch at slot 126; cascade-absorption
  at slot 127): axis-independent of M8b. The M8a / M8b cycles
  are concurrency-safe and run in parallel.
* **M8b is axis-independent** of M4 V0, M7 V0, and M8a. The 4-lens
  numerical-foreclosure substrate is closed as of 2026-05-07
  (092 fire); the substrate-prep at this slot 128 formalizes the
  existing closure into ratification-template language without
  re-deriving any numerical content.

### M8b status pre-fire-of-prompt-128

M8b V0 has been **achieved via numerical-foreclosure-by-residual-
acceptance** since 2026-05-07 via 092 substantive verdict
`M8b_S2_PERMANENT_RESIDUAL_VIA_BOREL_PADE`, with prior fires
017c / 017e / 017m establishing the three other independent
methodological lenses; the picture chain v1.19 records this as a
foreclosure at the milestone level, and the P-009 caveat at
2026-05-06 (relay 050) records the d≥3 forward-pointed
carry-forward. **What this prompt 128 fire does is**: assemble
the ratification dossier (substrate excerpts + decision form +
question set) so that slot 129 can dispatch a synth-tier
sign-off that matches the canonical 3-arc ratification pattern
established by M4 V0 (104 → 105 → 106) and re-anchored by M7 V0
(121 → 122 → 123). The substrate-prep meta-work itself does NOT
re-derive any numerical content; it formalizes the existing
4-lens-foreclosure-plus-d≥3-caveat-carry-forward into
ratification-template language.

---

## §2. Evidence inventory

### §2.1 — Prior fires that contributed to M8b closure (≥4 bridge SHAs per A2)

Four prior fires constitute the operative substrate. All bridge
SHAs were independently verified via `git rev-parse` returning a
full 40-char hash (per copilot-instructions.md "substrate
verification" rule + 105 SHA-correction discipline; mirror of
121 §2.1 SHA pre-verification table).

| # | Artifact | Bridge SHA (short) | Path | Verdict | Relevance |
|---|---|---|---|---|---|
| 1 | **Prompt 092 — T1-017M-BOREL-PADE-S2-092 (operative M8b V0 closure)** | `14e6b09` | `sessions/2026-05-07/T1-017M-BOREL-PADE-S2-092/handoff.md` + `verdict.md` | `M8b_S2_PERMANENT_RESIDUAL_VIA_BOREL_PADE` (`COMPLETE_PERMANENT_RESIDUAL`) | **The operative M8b V0 closure fire.** Raw-low-order Borel-Padé at dps=300, small (N,M) ∈ {6,8,10,12,14,16,18}, all 4 reps (V_quad / QL15 / QL05 / QL09); 196/196 OK cells (no RANK_LOSS); 0/84 adjacent (N,M) pairs reach dps/4=75 digit threshold; per-rep verdicts all `PERMANENT_RESIDUAL_G6b`. Implied $|S_2|/|S_1|$ ratios across reps span 0.22–1.28 (inconsistent with coherent Stokes-data structure). 15 AEAL claims (spec floor 5; suggested 7). |
| 2 | **Prompt 050 / W20 — P009-M8B-CAVEAT-FINAL (d≥3 caveat)** | `1873538` | `sessions/2026-05-06/P009-M8B-CAVEAT-FINAL/p009_m8b_caveat_active.txt` + `p009_m8b_caveat_all_variants.md` + `handoff.md` | Active variant **v1 `NOT_YET_DISPATCHED`** for d≥3 binding-window dispatch (rule5 grounding PASS; verb-check PASS, zero forbidden verbs from {shows, confirms, proves, establishes}). | **The carried-forward d≥3 caveat** that the M8b V0 closure must reconcile. Caveat SHA256 = `8EFC6C937283D65A2AC35132E5CF623DDCD49580A0C2C12C1791D1A238F14027`. Four tense-variants v1/v2/v3/v4 rendered; re-fire conditions documented at `p009_m8b_caveat_all_variants.md` §6 (re-fire on dispatch / positive / negative / schema-shift). 6 AEAL claims. |
| 3 | **Prompt 038 — MILESTONE-RESIDUAL-GAP-SURVEY-M4-M7-M8B-M9 (literature reconnaissance dossier)** | `a26ab27` | `sessions/2026-05-04/MILESTONE-RESIDUAL-GAP-SURVEY-M4-M7-M8B-M9/dossier_milestone_residual_gap_survey_m4_m7_m8b_m9.md` | `PARTIAL` (literature reconnaissance only; **NOT a ratification fire**). | **M8b literature substrate**: §C M8b Residual rows B.P1–B.P9 + §E cross-cut row M8b. Verdict: "No closed-form $S_2$ alien-amplitude formula in either Costin 2008 ch.5 (Theorems 5.11/5.26/5.45 = first Stokes constant only / multi-singular structural) or BLMP 2024 (Theorems 1.1/1.4/1.7 = Riemann–Hilbert characterisation of monodromy data structurally; pinning the second alien amplitude $S_2$ for the SIARC d=2 PCF $\delta_n$ normalisation requires the M6 normalisation map step which is INDEX-2 closed at 036). 14 AEAL claims; 0/14 acquisitions. Counts as **substrate document**, not as a prior M8b ratification fire. |
| 4 | **Picture v1.19 (consolidated deposit; M8b milestone block)** | `70d1a48` | `sessions/2026-05-06/PICTURE-V19-CONSOLIDATED-DEPOSIT/picture_v1.19.md` line 802 + line 1872 (cross-references) + § 5 line 306 (Stage-2-LSQ foreclosure) + § 5 line 322 (T36 Richardson-divergence diagnostic) + § 5 line 350 + line 377 + line 398 + line 561 + line 574 + line 658 + line 713 + line 741 + line 778 + line 783 | (consolidated picture; not a ratification fire) | **Milestone-axis level recording** of M8b foreclosure: row M8b reads (verbatim from line 1872 program-status row) "$M_4$ partial + M6.CC partial + M7 soft + M8b foreclosed"; the picture also records (verbatim) "Stage-2-LSQ branch FORECLOSED for d=2 PCFs" (line 780) and the T37M-HALT-implied-foreclosure of $S_2$ at the d=2 numerical scale (line 179, quoted substrate; verb chain in the original verbatim). M8b is NOT in M9 V0 gating set per M9 GATING line at picture v1.15 (CMB.txt L993, verbatim): "{M4, M6} UNCONDITIONALLY. M8b NOT in [gating]". |

**SHA pre-verification (2026-05-09 ~14:55 JST, this session)**:

```
PS> git rev-parse 14e6b09
14e6b093b187783ac3ca14f00333096889e2d590
PS> git rev-parse 1873538
1873538ab9157fd0bfff1bf730d9295514eb2664
PS> git rev-parse a26ab27
a26ab273200c639cf4444a05d1c9163b2308c657
PS> git rev-parse 70d1a48
70d1a4835ee0bc1f188aada9be65bb657f471730
```

All four substrate SHAs resolve to full 40-char hashes; no
ambiguity-fatal warnings. Bridge HEAD at draft time:
`7f93b9e4d624fdfca62f5d85393b4ead35cea751` (= `7f93b9e`,
`T1-SYNTH-M7-V0-CLOSURE-CASCADE-123`).

### §2.2 — Substrate documents (prior LSQ fires + manuscript anchors)

These are **non-ratification supporting fires** that establish the
predecessor-lens substrate (017c / 017e / 017m / 016 T36) and the
manuscript anchoring. They are not counted toward the A2 ≥4
bridge-SHA acceptance criterion (which is satisfied by §2.1
above), but they are part of the dossier the synth at slot 129
should be aware of.

| Artifact | Path | Section / line | Key claim |
|---|---|---|---|
| **Prompt 010 (T35 Stokes-multiplier discrimination; predecessor leading-rung fire)** | `sessions/2026-05-XX/T35-STOKES-MULTIPLIER-DISCRIMINATION/handoff.md` (per picture v1.19 § 5 row 010) | leading-rung $|S_1|$ measurement | $|S_1|$ measured per rep: V_quad 51.07, QL15 134.36, QL05 8.82, QL09 38.17 (092 verdict.md cross-citation); leading-rung dichotomy real but unstructured (G6b "PARTIAL" at leading scale). |
| **Prompt 016 (T36-S2-EXTRACTION; first Richardson attempt)** | `sessions/2026-05-XX/T36-S2-EXTRACTION/handoff.md` (per picture v1.19 § 5 line 322) | `HALT_T36_S2_RICHARDSON_DIVERGED` (re-keyed by relay agent from `T36_S2_CROSSMETHOD_MISMATCH`) | Convention check $a_n / (C \Gamma(n) \zeta_*^{-n}) \to 1$ agreed only to ~3 digits at $n=1500$–$1900$ (target 60+); $d=2$ PCFs carry non-zero polynomial-in-$1/n$ corrections to the leading Birkhoff amplitude. Richardson diverged to $R_\infty \sim 10^{654}$ (manifest noise). **Cross-method digit agreement collapsed to $\sim 10^{-15}$.** Method failure (dominated polynomial correction); led to the polynomial-aware refit at 017c. |
| **Prompt 017c (T37-S2-EXTRACTION-POLYNOMIAL-AWARE; first lens)** | `sessions/2026-05-XX/T37-S2-POLYNOMIAL-AWARE/handoff.md` (per picture v1.19 § 5 line 306) | Stage-2-LSQ branch foreclosed at d=2 (rel half-range $\sim 10^4$ to $10^{217}$) | Polynomial-aware joint-fit on $T_n := a_n \zeta_*^n / \Gamma(n)$ over $n \in [200, 600]$. D-extraction relative half-range envelope spans 0; foreclosure NOT precision-floor (at this dps). |
| **Prompt 017e (T37E-EXTENDED-RECURRENCE; second lens, precision-extended)** | `sessions/2026-05-02/T37E-EXTENDED-RECURRENCE/handoff.md` | Stage-2-LSQ branch re-confirmed-foreclosed at d=2 (rel half-range $\sim 4.7 \times 10^{217}$) | dps=400, N=5000 extended-recurrence LSQ. Envelope STILL spans 0 — **methodological** failure not precision-floor failure. Higher precision will not help. Picture v1.19 § 5 line 306. |
| **Prompt 017m (T37M-DIRECT-BOREL-D-EXTRACTION; third lens)** | `sessions/2026-05-03/T37M-DIRECT-BOREL/handoff.md` | `HALT_T37M_PADE_DIVERGENT` (subtracted-high-order Borel-Padé) | M=200..800 with K=25 cleanness step; 9/12 RANK_LOSS per rep; numerical Hankel singularity. Picture v1.19 § 5 line 314 + line 802. |
| **Picture v1.19 § 5 G6b row** | `sessions/2026-05-06/PICTURE-V19-CONSOLIDATED-DEPOSIT/picture_v1.19.md` (bridge `70d1a48`) | G6b row | "G6b ✅ FORECLOSED (NUMERICAL): Stage-2-LSQ branch FORECLOSED for d=2 PCFs (017c+017e); only remaining S_2 path = direct Borel–Padé (017m HALT) — closed by 092 PERMANENT_RESIDUAL_G6b across 4 reps." |
| **CMB.txt M8b entries** | `tex/submitted/CMB.txt` lines 422, 428, 439, 468, 474, 993, 998, 1007, 1018, 1046, 1050, 1209, 1268, 1397, 1538, 1574, 1619, 1629, 1631, 1646, 1648, 1653, 1656, 1667, 1670, 1673, 1872 | M8b context block + P-009 caveat block | "M8B STATUS (re-confirmed this audit): foreclosed (caveat-only at d=2; future structural revival possible at d≥3 only)" + "M9 GATING (post-v1.15): {M4, M6} UNCONDITIONALLY. M8b NOT in [gating]" + program-status "M4 partial + M6.CC partial + M7 soft + M8b foreclosed". |
| **RULE 1 marker** | `tex/submitted/control center/picture/M1_M12_CLOSURE_OUTLOOK_20260509_RULE1.md` | line 27 + line 77 + line 114 + line 126 | "M8b axis ratification (substrate at 092 + P-009) → math, substrate-ready"; "M7 + M8a + M8b ratifications: 9 fires (3-arc template × 3 axes)"; M8b under §1 KEEP as math-foundational. |

### §2.3 — Open residuals (qualifications the ratification must surface)

The M8b V0 numerical-foreclosure closure carries three explicit
qualifications that the ratification statement must carry forward
(analogue of the M4 V0 MEDIUM-HIGH + M7 V0 SOFT-BRANCH carry-
forward semantics established at 105 → 106 and 121 → 123):

1. **d≥3 binding-window caveat (P-009 carry-forward).** The 092
   foreclosure addresses the d=2 numerical extraction. The d≥3
   structural binding-window dispatch (P-009 active variant v1
   `NOT_YET_DISPATCHED`) is **forward-pointed not-blocking**.
   The closure statement must reconcile (not modify) the active
   v1 caveat language:

   > "Stokes-multiplier discrimination (companion milestone M8b)
   > will supply an additional independent test of the SIARC
   > stratification at d≥3, conditional on the M8b dispatch
   > landing within the relevant binding window and on the
   > binding-window result."

   Re-fire conditions for the caveat (per
   `p009_m8b_caveat_all_variants.md` §6) are:
   * d≥3 dispatch fires → re-render under v2.
   * Positive binding-window result → re-render under v3 with
     bridge-link substituted in.
   * Negative binding-window result → remove caveat under v4
     with explanatory note.
   * P-008 schema-shifts → re-audit.

   **Confidence carry-forward**: the M8b_V0_CLOSED tag at
   picture-chain v1.20+ should be annotated with
   `(NUMERICAL-FORECLOSURE; d≥3-CAVEAT-CARRIED-FORWARD)` to
   prevent silent inheritance of an unqualified closure state.

2. **Uncharted-quadrant forward-pointer (092 U2).** The 092 fire
   identified one uncharted methodological quadrant: small-(N,M)
   Padé applied to the LEADING-SECTOR-SUBTRACTED residual
   (T37M's K=25 cleanness step + 092's small-(N,M) regime
   instead of T37M's high-(N,M)). T37M did subtracted+high-order
   (HALT); 092 did raw+low-order (PERMANENT_RESIDUAL_G6b);
   subtracted+low-order remains untested. This is a forward-
   pointer for future fires; it does NOT block M8b V0 closure
   (092 explicitly classifies the 4-lens substrate as sufficient
   for `COMPLETE_PERMANENT_RESIDUAL` per the spec's Phase F
   note + the 4-lens combination).

3. **Stokes-convention sign-imaginary factor (092 J3 / U4).** All
   196 candidate-$S_2$ values in 092 have imaginary part = 0 to
   dps=300 by construction (Padé approximants of real-coefficient
   series have real residues; the T35 `S_1 = 2\pi i \cdot C`
   convention $i$ factor arises from the Borel-Laplace contour
   discontinuity, not from Padé pole-residue extraction). The
   092 reported "$S_2$ candidate" values are magnitudes (real);
   for convergence detection magnitude is the right quantity.
   This is a **method-internal convention note**, not a
   substrate gap. Documented for the closure statement to be
   precise about magnitude-vs-complex-amplitude semantics
   (092 J3).

### §2.4 — §1 closure statement vs substrate consistency check

| §1 closure-statement claim | Substrate excerpt | Consistent? |
|---|---|:---:|
| "M8b V0 CLOSED via numerical-foreclosure-by-residual-acceptance" | 092 verdict.md "Aggregate verdict (M8b axis): `M8b_S2_PERMANENT_RESIDUAL_VIA_BOREL_PADE`. Resolves M8b axis via closure-by-residual-acceptance per Phase D2 of relay 092." | **YES** |
| "Four independent methodological lenses (017c LSQ; 017e extended LSQ; 017m subtracted-high-order Borel-Padé HALT; 092 raw-low-order Borel-Padé)" | 092 handoff.md "Comparison to 017L (T37E) LSQ baseline residual: T37E reported rel half-range ~10^217 for Stage-2 D extraction. The present 092 Borel-Padé reports rel half-range 2.14–76.85... approximately 215 orders of magnitude tighter than LSQ baseline, yet still failing extraction threshold." + picture v1.19 § 5 line 306 (017c+017e foreclosure) + line 314 (017m HALT) | **YES** |
| "0/84 adjacent (N,M) pairs reaching the dps/4=75 digit threshold" | 092 verdict.md "Convergence-region detection: 0/84 adjacent (N,M) pairs reach the dps/4 = 75 digit threshold in any rep." | **YES** |
| "rel half-range 2.14–76.85 across 4 reps (V_quad / QL15 / QL05 / QL09)" | 092 verdict.md per-rep table: V_quad 2.14, QL15 3.95, QL05 76.85 (D5 anomaly), QL09 10.08. | **YES** |
| "implied $|S_2|/|S_1|$ ratios across reps inconsistent with coherent Stokes-data structure" | 092 verdict.md "implied $|S_2|/|S_1|$ ratios across reps span 0.22 to 1.28, inconsistent with a coherent Stokes-data structure." | **YES** |
| "Mathematical content (alien amplitude $S_2$) NOT falsified" | 092 verdict.md "the sub-leading transmonomial governing $S_2$ is below the resolution floor of the Borel-Padé method as canonically deployed." + picture v1.19 line 125 "(mathematics not falsified — alien amplitude $S_2$ remains" | **YES** |
| "d≥3 structural binding-window dispatch forward-pointed not-blocking via P-009 active variant v1 NOT_YET_DISPATCHED" | P009-M8B-CAVEAT-FINAL handoff.md "M8b dispatch status (relay 050 P3 verbatim slot): NOT_YET_DISPATCHED for the d≥3 binding-window dispatch." | **YES** |
| "M8b NOT in M9 V0 gating set; M9 gating = {M4, M6}" | CMB.txt L993 "M9 GATING (post-v1.15): {M4, M6} UNCONDITIONALLY. M8b NOT in [gating]" + L1018 "M9 announcement does not depend on the value of S_2; M8b is enrichment, not gate." | **YES** |
| "15 AEAL claims ledgered (092); halt log 0 halts triggered" | 092 handoff.md "15 entries written to claims.jsonl this session (spec minimum 5; suggested 7)" + "halt_log.json — 0 halts triggered; 5 spec halts checked-and-passed" | **YES** |
| "picture v1.19 records M8b foreclosed at milestone level" | picture v1.19 line 1872 "M4 partial + M6.CC partial + M7 soft + M8b foreclosed" + line 802 "M8b axis closure-by-residual-acceptance" | **YES** |

**T2-Executor conclusion supported by substrate**: All 10 sub-claims
of the §1 proposed M8b V0 closure statement are materially
consistent with the 092 + P-009 + 038 + picture v1.19 substrate
at the verified SHAs. The synth at slot 129 may sign §3
(`RATIFY`) and §6 (`Substrate SHAs verified: Y`) on this basis
if the synth accepts the §1 wording as written.

If the synth wishes to amend §1 wording (e.g., to add the
numerical-foreclosure / d≥3-caveat-carry-forward annotation
`(NUMERICAL-FORECLOSURE; d≥3-CAVEAT-CARRIED-FORWARD)` explicitly
in the closure statement, or to surface the 092 U2 uncharted-
quadrant forward-pointer as a governance note), use §3
(`RATIFY_WITH_AMENDMENT`) and provide revised wording in §4.

---

## §3. Decision form (synth signs ONE row)

| Decision | Selected? | Notes |
|:---:|:---:|---|
| **`RATIFY`** — M8b V0 CLOSED as proposed in §1 | ☐ | rubber-stamp; 092 + P-009 + 038 + picture v1.19 substrate complete; 4-lens foreclosure substrate dossier-complete; recommended path given the substrate is dossier-complete |
| **`RATIFY_WITH_AMENDMENT`** — M8b V0 CLOSED with synth-side wording amendments to §1 | ☐ | M4 V0 / M7 V0 cascade precedent (105 → 106 ACCEPT_W_REVISIONS; 121 → 123 RATIFY_WITH_AMENDMENT @ MEDIUM-HIGH per most-conservative band protocol): the synth may want the numerical-foreclosure / d≥3-caveat-carry-forward annotation `(NUMERICAL-FORECLOSURE; d≥3-CAVEAT-CARRIED-FORWARD)` carried forward into the closure statement (analogue of M4 V0 `(MEDIUM-HIGH; HIGH-PENDING)` and M7 V0 `(SOFT-BRANCH; HARD-BRANCH-PENDING)`); revised wording in §4 |
| **`DEFER`** — substrate insufficient or ratification premature, fire follow-on | ☐ | provide reasoned NO_GO statement in §5; T2-executor dispatches rubber-duck review of 092 + P-009 + 038 + picture v1.19 against the synth's reasoned objection before re-ratification |
| **`OBJECT`** — substrate substantively contradicted by independent reading | ☐ | provide reasoned objection in §5; halt-class outcome; escalate to operator |

### §3 explicit question set (Q1–Q5 per prompt 128 §4)

* **Q1**: Does the M8b substrate suffice for V0 closure given the
  P-009 d≥3 caveat? *(synth must read the P-009 caveat statement
  in §2.1 and §2.3 before answering; the V0 closure addresses
  d=2 numerical foreclosure, the caveat addresses d≥3 binding-
  window which is NOT_YET_DISPATCHED)*
* **Q2**: Are cross-axis dependencies discharged? *(M9 V0
  announcement: M8b is a substrate input. Per CMB.txt L993
  "M9 GATING: {M4, M6} UNCONDITIONALLY. M8b NOT in [gating]"
  and L1018 "M9 announcement does not depend on the value of
  S_2; M8b is enrichment, not gate" — M8b foreclosure does NOT
  block M9 announcement. Synth signs / objects.)*
* **Q3**: Is manuscript content (PCF-1 §3, CMB.txt P-009 caveat
  block, picture v1.19) consistent with M8b V0 closure including
  the P-009 caveat language? *(synth must read the P-009 caveat
  statement; §2.4 row 7 + row 10 are the consistency-check
  artifacts.)*
* **Q4**: M8B_V0_VERDICT: select one of `RATIFY` /
  `RATIFY_WITH_AMENDMENT` / `DEFER` / `OBJECT` (one row in §3
  table above).
* **Q5**: If `RATIFY_WITH_AMENDMENT`: specify the amendment in
  §4 (template provided below; minimum suggested amendment is
  the `(NUMERICAL-FORECLOSURE; d≥3-CAVEAT-CARRIED-FORWARD)`
  confidence-qualifier annotation).

---

## §4. (If RATIFY_WITH_AMENDMENT) Revised closure statement

```
[Synth fills in revised wording here. Recommended template
(mirrors M4 V0 / M7 V0 §4 revised-wording structure):

M8b V0 CLOSED via numerical-foreclosure-by-residual-acceptance
at the d=2 PCF Stokes-multiplier S_2 scale. Four independent
methodological lenses (017c polynomial-aware LSQ at dps=250 N=2000;
017e extended LSQ at dps=400 N=5000; 017m subtracted-high-order
Borel-Padé HALT_T37M_PADE_DIVERGENT at M=200..800; 092 raw-low-order
Borel-Padé PERMANENT_RESIDUAL_G6b across 4 reps at small (N,M) ∈
{6..18}, dps=300, 196/196 OK cells, 0/84 adjacent (N,M) pairs
reaching the dps/4=75 digit threshold; rel half-range 2.14–76.85
across reps; implied |S_2|/|S_1| ratios 0.22–1.28 inconsistent with
coherent Stokes-data structure) report |S_2| below the resolution
floor of laptop-feasible Borel-Padé methodology. The 092 raw-low-
order substrate is approximately 215 orders of magnitude tighter
than the 017e LSQ envelope and is the orthogonal methodological
quadrant complementing 017m's subtracted-high-order failure;
together they bracket S_2 as too small for low-order Padé to
resolve over the dominant leading singularity at u=zeta_* and too
noisy for high-order Padé to capture without numerical Hankel
singularity (canonical signature of PERMANENT_RESIDUAL_G6b).

Mathematical content (alien amplitude S_2) is NOT falsified by
the foreclosure; only the laptop-feasible numerical extraction
path is foreclosed at the present compute budget. The d≥3
structural binding-window dispatch is forward-pointed not-blocking
via the P-009 caveat (relay 050 active variant v1
NOT_YET_DISPATCHED; SHA256 8EFC6C937283D65A2AC35132E5CF623DDCD49580A0C2C12C1791D1A238F14027):

  "Stokes-multiplier discrimination (companion milestone M8b)
   will supply an additional independent test of the SIARC
   stratification at d≥3, conditional on the M8b dispatch
   landing within the relevant binding window and on the
   binding-window result."

The d≥3 caveat is carried forward unchanged by this V0 closure
(re-fire conditions per p009_m8b_caveat_all_variants.md §6: d≥3
dispatch fires → v2; positive result → v3; negative result → v4
with explanatory note; P-008 schema-shifts → re-audit).

M8b is NOT in the M9 V0 gating set (M9 gating = {M4, M6}
UNCONDITIONALLY per picture v1.15+ M9 GATING line / CMB.txt L993);
M8b is enrichment, not gate. The M9 V0 announcement does not
depend on the value of S_2 (CMB.txt L1018).

Closure is at the algebraic-numerical level (4-lens negative-result
substrate; no new high-dps mpmath generation needed). The
092 U2 uncharted-quadrant forward-pointer (subtracted-leading-sector
plus small-(N,M) Padé combination) remains a forward-pointer for
future fires; it does NOT block V0 closure (092 spec Phase D2
classifies the 4-lens substrate as COMPLETE_PERMANENT_RESIDUAL).

PCF-1 §3 manuscript wording carries the foreclosure as a note
(consistent with CMB.txt L941–998 P-009 caveat block and picture
v1.19 § 4 milestone-level recording); under RULE 1 no §X
manuscript amendment is mandated by M8b V0 closure beyond the
existing CMB caveat block (which already records the d=2
foreclosure). Zenodo deposit step TABLED under RULE 1
(admin/distribution deferred until M1–M12 math-foundational
closure complete); math-content step in scope.

No halt conditions triggered (092: 0 halts triggered; 5 spec
halts checked-and-passed; 15 AEAL claims; 5 INFO discrepancies
D1–D5 documented; 4 INFO unexpected finds U1–U4 documented.
P009-M8B-CAVEAT-FINAL: 0 halts; 6 AEAL claims; verb-check PASS).

Confidence: NUMERICAL-FORECLOSURE for d=2; d≥3-CAVEAT-CARRIED-
FORWARD for binding-window dispatch. Picture-chain v1.20+
M8b_V0_CLOSED tag should annotate (NUMERICAL-FORECLOSURE;
d≥3-CAVEAT-CARRIED-FORWARD) to prevent silent inheritance of
unqualified closure state (mirrors M4 V0 (MEDIUM-HIGH;
HIGH-PENDING) and M7 V0 (SOFT-BRANCH; HARD-BRANCH-PENDING)
cascade-annotation precedents).
]
```

---

## §5. (If DEFER or OBJECT) NO_GO reasoned statement

```
[Synth fills in reasoned objection here, naming which substrate
gap or analytic concern blocks ratification.]
```

---

## §6. Synth signature

```
Synth:                [Claude.ai web peer-AI; T1-Synth tier]
Date/time:            [YYYY-MM-DD HH:MM JST]
Decision:             [RATIFY / RATIFY_WITH_AMENDMENT / DEFER / OBJECT]
Substrate SHAs
  verified:           [Y / N]  (092: 14e6b09;
                          P-009: 1873538;
                          038: a26ab27;
                          picture v1.19: 70d1a48;
                          all 4 verified via independent
                          git rev-parse return-of-full-hash AND
                          the §2.4 10/10 PASS consistency check
                          is materially supported by the
                          substrate; mirrors M4 V0 §6 substrate-
                          grounding semantic per 105 §6 wording
                          amendment + M7 V0 §6 121 mirror)
Rubber-duck QA
  acknowledged:       [Y / N]  (092 handoff.md "Judgment calls"
                          J1 (017L → T37E identification) +
                          J2 (raw vs leading-sector-subtracted
                          methodology choice) + J3 (Stokes
                          magnitude convention) + J4 (all-reps
                          aggregate via logical OR) + J5 (spec
                          halt-set self-check); P-009 caveat
                          handoff.md JC-1 (caveat-scope
                          short-vs-long) + JC-2 (Unicode
                          preservation); all are rubber-duck-
                          disciplined judgment calls, not
                          silent fudges.)
Numerical-foreclosure
  / d≥3-caveat-carry-
  forward qualifier
  acknowledged:       [Y / N]  (synth acknowledges picture-chain v1.20+
                          tag must read M8b_V0_CLOSED
                          (NUMERICAL-FORECLOSURE;
                          d≥3-CAVEAT-CARRIED-FORWARD), not bare
                          M8b_V0_CLOSED, per the confidence-
                          carry-forward semantic established at
                          M4 V0 (105 → 106) and re-anchored at
                          M7 V0 (121 → 123) cascade precedents.
                          Synth acknowledges the d≥3 binding-
                          window caveat (P-009 active variant
                          v1 NOT_YET_DISPATCHED) is reconciled
                          (not modified) by this V0 closure.)
P-009 caveat
  reconciliation:     [Y / N]  (synth acknowledges the active
                          v1 caveat language remains
                          unchanged by this V0 closure;
                          re-fire conditions documented at
                          p009_m8b_caveat_all_variants.md §6
                          remain the operative re-fire triggers
                          (dispatch / positive / negative /
                          schema-shift); the V0 closure does
                          NOT trigger re-render under v2 / v3 /
                          v4 because the d=2 numerical
                          foreclosure and the d≥3 structural
                          dispatch are different scopes.)
```

**Substrate-grounding note for §6 verification** (mirrored from
M4 V0 §6 / M7 V0 §6 wording-amendment semantic):

"Substrate SHAs verified [Y/N]" means *both*
(a) the cited SHAs exist in bridge git history at the cited paths,
AND
(b) the substrate at those SHAs materially supports the §1 closure
statement (i.e., the 4-lens numerical-foreclosure verdict at 092,
the d≥3 caveat carry-forward at P-009, and the picture v1.19
milestone-level recording are present and consistent with §1).
It does NOT require independent re-derivation of the numerical
content. If the synth wishes to verify (b) explicitly, the §2.4
10/10 PASS consistency check is the substrate-grounded
verification artifact.

---

## §7. Post-ratification cascade (T2-executor follow-up)

If §3 = RATIFY or RATIFY_WITH_AMENDMENT:

| Step | Actor | Action | SQL todo |
|:---:|---|---|---|
| 1 | agent | Mark `m8b-substrate-prep-128-completed` → `done` | (this template) |
| 2 | agent | Mark `m8b-unblocked-post-m4-v0-closure` → `done` | post-M8b-V0-closure unblock resolved |
| 3 | agent | Add `M8b_V0_CLOSED (NUMERICAL-FORECLOSURE; d≥3-CAVEAT-CARRIED-FORWARD)` tag to next picture-chain deposit (v1.20+) | included in v1.20 fire (under RULE 1: math-content step in scope, picture-chain admin step TABLED until M1–M12 closure) |
| 4 | (optional) | umbrella v2.x amendment if §3 = RATIFY_WITH_AMENDMENT | post-M9 LANE-1 / under RULE 1 deferred |
| 5 | (optional) | P-009 caveat status check at next CLI engagement (no re-render expected; the d≥3 dispatch has not been fired by the M8b V0 closure) | TABLED under RULE 1 until d≥3 dispatch fires (or P-008 schema-shifts) |
| 6 | (optional) | 092 U2 uncharted-quadrant forward-pointer: schedule subtracted-low-order Padé fire if M8b axis re-opens at d=2 | TABLED under RULE 1; not blocking V0 closure |

If §3 = DEFER:

| Step | Actor | Action |
|:---:|---|---|
| 1 | agent | Dispatch rubber-duck review of 092 + P-009 + 038 + picture v1.19 against synth's reasoned objection |
| 2 | agent | If rubber-duck concurs: fire follow-on substrate-hardening agent (~30–60 min); re-issue ratification template at next slot |
| 3 | agent | If rubber-duck disputes synth: surface to operator for tie-break decision |

If §3 = OBJECT:

| Step | Actor | Action |
|:---:|---|---|
| 1 | agent | Halt-class: surface to operator immediately |
| 2 | agent | Pause M-axis ratification cascade until operator triage |

---

## §8. Cross-references

* M4 V0 mirror anchor: `siarc-relay-bridge/sessions/2026-05-08/M4-RATIFICATION-SUBSTRATE-PREP-105/` (bridge `d1e19e9`)
* M4 V0 cascade: `siarc-relay-bridge/sessions/2026-05-08/M4-V0-CLOSURE-CASCADE-106/`
* M4 V0 ratification template (executed): `tex/submitted/control center/m4_v0_ratification_template.md`
* M7 V0 substrate-prep mirror: `siarc-relay-bridge/sessions/2026-05-09/T2-EXECUTOR-M7-RATIFICATION-SUBSTRATE-PREP-121/m7_v0_ratification_template.md` (bridge `f4b6de8`)
* M7 V0 solo-dispatch: `siarc-relay-bridge/sessions/2026-05-09/T1-SYNTH-M7-RATIFICATION-SOLO-DISPATCH-122/`
* M7 V0 cascade-absorption (precedent for most-conservative-band protocol): `siarc-relay-bridge/sessions/2026-05-09/T1-SYNTH-M7-V0-CLOSURE-CASCADE-123/handoff.md` (bridge `7f93b9e`)
* M8a sibling substrate-prep (same slate, parallel): `siarc-relay-bridge/sessions/2026-05-09/T2-EXECUTOR-M8A-RATIFICATION-SUBSTRATE-PREP-125/` (parallel-fired at slot 125; not yet deposited at the time this 128 template was drafted)
* Picture v1.19 (M8b milestone block + G6b row + program-status row): `siarc-relay-bridge/sessions/2026-05-06/PICTURE-V19-CONSOLIDATED-DEPOSIT/picture_v1.19.md` (bridge `70d1a48`)
* Prompt 092 (T1-017M-BOREL-PADE-S2-092; substantive M8b V0 closure): `siarc-relay-bridge/sessions/2026-05-07/T1-017M-BOREL-PADE-S2-092/handoff.md` + `verdict.md` (bridge `14e6b09`)
* Prompt 050 / W20 (P009-M8B-CAVEAT-FINAL; d≥3 caveat): `siarc-relay-bridge/sessions/2026-05-06/P009-M8B-CAVEAT-FINAL/p009_m8b_caveat_active.txt` + `p009_m8b_caveat_all_variants.md` + `handoff.md` (bridge `1873538`)
* Prompt 038 (Milestone Residual Gap Survey M4/M7/M8b/M9; literature reconnaissance): `siarc-relay-bridge/sessions/2026-05-04/MILESTONE-RESIDUAL-GAP-SURVEY-M4-M7-M8B-M9/dossier_milestone_residual_gap_survey_m4_m7_m8b_m9.md` (bridge `a26ab27`)
* CMB P-009 caveat block + M9 GATING line: `tex/submitted/CMB.txt` lines 941–998, 993, 1018, 1153–1156, 1467–1488, 1518–1530
* RULE 1 marker: `tex/submitted/control center/picture/M1_M12_CLOSURE_OUTLOOK_20260509_RULE1.md` (M8b listed under §1 KEEP as math-foundational; substrate at 092 + P-009)
* Memory anchor: `frontier-phases-2026-04-16` (M-axis classification, pre-RULE-1 baseline)

---

## §9. Forbidden-verb compliance note

Per envelope STEP D.2 forbidden-verb scan: this template uses
"verifies" and "verified" only as substrate-verification meta-
references (`git rev-parse` returned-full-hash; §2.4 consistency
check) and "ratify" / "ratifies" / "ratification" (the operative
verb of the document itself, used in §3 + §7 + the title) as
checklist-meta-references. Both are verb-list-as-data + checklist-
meta-references — exempt under 098 J3 / 075 J2 precedent and
re-anchored at 121 / 123 Forbidden-verb scan exemption.

Substrate prose (§1, §2 evidence-table verdict cells, §4 revised-
wording template) does NOT contain forbidden verbs in substantive
(claim/prediction) context. The verb chain in the §4 template
uses "report" / "carries" / "remains" / "is" / "addresses" /
"reconciles" — none of {confirms, proves, demonstrates,
verifies, validates, corroborates, certifies, settles, discharges,
ratifies, establishes} appears in substantive (claim) context.

§3 question text (Q1–Q5) is intentionally neutral: it asks the
synth to *select* a row, *answer*, or *specify*; the verb-of-
decision is "ratify" (operative, exempt) and the verb-of-
evidence is "supports" / "is consistent with" (not forbidden).

The active P-009 caveat language (§1, §2.3, §4) is reproduced
**verbatim** from `p009_m8b_caveat_active.txt` (SHA256 verified
in §2.1). The caveat itself was forbidden-verb-checked PASS at
relay 050 STEP 4 (`will supply` is the permitted v1 form);
quoted-substrate exemption applies per 121 / 123 precedent.

§2.1 row 4 (picture v1.19 milestone block) and §2.4 row 6 reproduce
verbatim picture-v1.19 substrate text containing the verb
"foreclosed" / "FORECLOSED" (not in the forbidden-verb set) and a
quoted line at picture v1.19 line 179 that contains "confirms" in
the substrate's own context (T37M-HALT-implied numerical
foreclosure phrasing). The L213 / §2.1-row-4 cell reframes the
line-179 reference as "T37M-HALT-implied-foreclosure" to avoid
re-asserting the forbidden verb in agent-authored prose; the
quoted-substrate phrase is otherwise exempt under 121 / 123
precedent.

The §2.1 row 2 verdict cell ("verb-check PASS, zero forbidden
verbs from {shows, confirms, proves, establishes}") is a
verb-list-as-data reference (the literal forbidden-verb set
checked at relay 050 STEP 4); exempt under 098 J3 / 075 J2
precedent.

---

## §10. Dispatch readiness (Phase D)

* **Word count**: ~3 600 words (§1–§9 inclusive; comparable to
  M7 V0 121 template scale; well within paste-ready limits for
  a Claude.ai web chat session)
* **All §2 evidence pre-verified**: 4/4 SHAs (`14e6b09`,
  `1873538`, `a26ab27`, `70d1a48`) returned full 40-char hashes
  via `git rev-parse` at 2026-05-09 ~14:55 JST in this session;
  full output pasted into §2.1 SHA-pre-verification block.
* **Bibliographic identifier pre-verification**: NOT_APPLICABLE
  — this template cites only internal bridge SHAs as substrate;
  no external DOI / arXiv ID is in scope for the M8b V0 closure
  (the 038 Milestone Residual Gap Survey reconnaissance dossier
  flagged Costin 2008 ch.5, BLMP 2024 slot 08, and Clavier-
  Cournod 2024 spec-by-author-and-year as literature-bracket-
  only references not bridging the d=2 SIARC PCF $\delta_n$
  normalisation to closed-form $S_2$ directly; per §2.3
  residual #1 + #2, this is a forward-pointed not-blocking
  residual and does not enter the ratification claim).
* **All §3 questions answerable from §2 substrate alone**: YES
  — no out-of-packet follow-up is needed for the synth to sign
  §3 + §6. The §2.4 10/10 PASS consistency check is the
  substrate-grounded verification artifact. Q1–Q5 are framed
  to be answerable from §2.1 / §2.2 / §2.3 / §2.4 + the
  embedded P-009 caveat language.
* **P-009 caveat threading**: the synth must read the P-009
  caveat statement (active v1 reproduced verbatim in §1
  manuscript-section block + §2.3 residual #1 + §4 revised-
  wording template) before answering Q1, Q3, and Q4. The
  caveat language is the operative reconciliation point for
  the d=2-closed-vs-d≥3-deferred scope distinction.
* **Recommended dispatch class**: T1-Synth solo (Claude.ai web
  conversation; mirrors 104 → 105 → 106 dispatch pattern at
  the M4 V0 cascade and 121 → 122 → 123 dispatch pattern at
  the M7 V0 cascade)
* **Recommended next-slot**: 129 (T1-SYNTH-M8B-RATIFICATION-
  SOLO-DISPATCH); successor cascade-absorption fire at slot
  130 (T1-SYNTH-M8B-V0-CLOSURE-CASCADE) per the canonical
  3-arc template. (SQL todo for 129 confirmed-already-inserted
  at slate-drafting time per prompt 128 §5 A7.)

---

**Template status**: **DRAFTED 2026-05-09 ~15:05 JST** by
T2-Executor (prompt 128 substrate-prep). Awaits synth dispatch
at slot 129.
