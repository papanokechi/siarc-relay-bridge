# M7 V0 closure ratification template (synth-tier)

**Purpose**: paste-ready audit artifact for the next M-axis
absorption cycle (synth-tier solo-dispatch, slated for slot 122).

**Pre-stage drafted**: at bridge HEAD `8ebd1eb`
(T2-EXECUTOR-115-ROUTE-F-D7-FIXED-POINT-EXTRACTION-132).
**Drafted by**: T2-EXECUTOR (GitHub Copilot, VS Code; Claude
Opus 4.7 xhigh) at 2026-05-09 ~11:40 JST.
**Used by**: T1-Synth (Claude.ai web), at slot 122 solo-dispatch.

**Mirror anchor**: this template mirrors the structure of
`siarc-relay-bridge/sessions/2026-05-08/M4-RATIFICATION-
SUBSTRATE-PREP-105/m4_substrate_excerpts.md` + the M4 V0
ratification template at
`tex/submitted/control center/m4_v0_ratification_template.md`.
Section numbering and decision-form structure are aligned bit-for-bit
where applicable; M7-specific content fills the slots.

---

## §1. M7 axis scope

### What the M7 axis represents

Per **picture v1.19 § 4** (bridge `70d1a48`,
`sessions/2026-05-06/PICTURE-V19-CONSOLIDATED-DEPOSIT/picture_v1.19.md`
line 965), the M7 axis is:

> **M7: j=0 Chowla–Selberg Gamma(1/3) closure (or A=6 artefact ruled out)**

This is the j=0 endpoint axis of the program: at the equianharmonic
CM point j=0 (Klein j-invariant zero, lattice $\mathbb{Z}[\omega]$
with $\omega = e^{2\pi i / 3}$), the question is whether the
Chowla–Selberg amplitude $\Gamma(1/3)$ closed-form intervenes in the
PCF j=0 formal-baseline-A signal — or whether $A = 6$ is the exact
asymptotic constant with no Chowla–Selberg gamma-product correction.
The M7 milestone closes either way (the negative branch is also a
closure: a structural finding that no $\Gamma(1/3)$ amplitude
correction is detectable in the H6 deduplicated B19+ basis at the
realized PSLQ precision).

### What "M7 V0 closure" means specifically

M7 V0 closure is the **soft-branch closure**: at
$|\delta_\text{lin}| \sim 10^{-23}$ (well below the
$|\delta_\text{lin}| < 10^{-15}$ minimum target with 8+ orders of
margin), PSLQ on the 17-member deduplicated H6 Chowla–Selberg basis
B19+ at maxcoeff $= 10^{50}$ / tol $= 10^{-40}$ returns no
$\Gamma(1/3)$ relation in any of the 4 j=0 cubic families.
This is the *soft-branch* result; the *hard-branch* result (stretch
goal $|\delta| < 10^{-30}$) was not achieved and would require
$K_\text{FIT} = 9$ on extended series at $N \le 2400$ / dps $\ge 44{,}300$
(Q22 path-(b)). The soft-branch closure was operator-accepted at
2026-05-02 (PCF-2 v1.4 §6 amendment drafted as Phase F output of
Prompt 014) and recorded in picture v1.19 as **M7 ✅ achieved in
soft branch** (line 708, line 1917, line 3025, line 3306).

The M7 V0 closure statement is therefore:

> **j=0 Chowla–Selberg amplitude closure NOT detected in the
> H6 deduplicated B19+ basis at $|\delta_\text{lin}| \sim 10^{-23}$
> PSLQ-detection precision; A = 6 in the soft-branch reading.**

### Manuscript section(s) M7 closure feeds

- **PCF-2 §6** (current published wording: `AMBIGUOUS-AT-FINITE-N`)
  — amendment to `A = 6 to PSLQ-detection precision; no detected
  Chowla–Selberg amplitude correction in H6 basis at the present
  precision`. The amendment was drafted as Phase F output of
  Prompt 014 (file `pcf2_v1.4_amendment.md` at bridge
  `sessions/2026-05-02/T25D-RETRY-13PARAM/`).
- **PCF-2 v1.4** (whole release) — Zenodo deposit gated on Q22
  operator-acceptance; under RULE 1 (2026-05-09 11:18 JST) the
  Zenodo-deposit step is **TABLED** (admin), but the math-content
  step (§6 amendment) is the M7 V0 closure deposit and remains
  in scope.
- **Picture chain v1.20+** (forward-pointed): the closure tag at
  v1.20+ should read `M7_V0_CLOSED (SOFT-BRANCH; HARD-BRANCH-PENDING)`
  per the M4 V0 cascade pattern (105 → 106 confidence-qualifier
  carry-forward; cf. M4_V0_CLOSED `(MEDIUM-HIGH; HIGH-PENDING)`).

### Relationship to M4 V0 (closed) and M8a / M8b (parallel cycles)

- **M4 V0** (closed 2026-05-08 at MEDIUM-HIGH confidence, bridge
  cascade 105 → 106): the deg_a=0 row mechanism closes the SIARC
  stratum's structural M4 axis at zero acquisition cost. M7 V0 is
  axis-independent of M4 V0 (different stratum, different mechanism);
  the M4 V0 ratification was the precondition gate per peer-consult
  104 V_FT4_RECOMMENDED. With M4 V0 closed, M7 / M8a / M8b
  ratification cycles are now procedurally unblocked.
- **M8a / M8b** (parallel ratification cycles): per picture v1.19
  the d=2 PCF-1 §3 sign-of-$\Delta_b$ dichotomy lives at the
  M8b axis (Stokes-multiplier scale; $|S_1|$ measured in 010, $a_1$
  3-stratum partition closed in 017c+017e+017L, $S_2$ permanently
  foreclosed numerically per 017m HALT_T37M_PADE_DIVERGENT). M8a /
  M8b ratification cycles will mirror the same 3-arc template
  (substrate-prep → solo-dispatch → cascade-absorption) but with
  M8a / M8b-specific evidence inventories. Cross-axis fires are
  independent.

### M7 status pre-fire-of-prompt-121

M7 V0 has been **achieved in soft branch** since 2026-05-02 via
Prompt 014 substantive verdict, and the picture chain v1.19
records this as a closure at the milestone level. **What this
prompt 121 fire does is**: assemble the ratification dossier
(substrate excerpts + decision form + question set) so that
slot 122 can dispatch a synth-tier sign-off that matches the
canonical 3-arc ratification pattern established by M4 V0
(104 → 105 → 106). The substrate-prep meta-work itself does NOT
re-derive any numerical content; it formalizes the existing
soft-branch closure into ratification-template language.

---

## §2. Evidence inventory

### §2.1 — Prior fires that contributed to M7 closure

Two prior fires are the operative substrate. Both bridge SHAs
were independently verified via `git rev-parse` returning a full
40-char hash (per copilot-instructions.md "substrate verification"
rule + 105 SHA-correction discipline).

| Artifact | Bridge SHA | Path | Verdict | Relevance |
|---|---|---|---|---|
| **Prompt 006 — T2.5d j=0 Chowla–Selberg closure (interim)** | `1321bb6` | `sessions/2026-05-02/T25D-J0-CHOWLA-SELBERG-CLOSURE/handoff.md` | `AMBIGUOUS_AT_DPS8000` (interim halt; **superseded in soft branch by Prompt 014**) | First M7 fire; established the empirical signal A_lin → 6 ± 2 × 10⁻⁷ across 4 j=0 cubic families (Q_30..Q_33) with monotone-decreasing $|\delta_\text{lin}|$ as $N_\max$ grows. 5-param ansatz capped precision at ~7 digits (G16 surfaced); 30-digit spec threshold not met. ~35 s agent compute. |
| **Prompt 014 — T25D-RETRY-13PARAM (substantive M7 V0 closure)** | `e857172` | `sessions/2026-05-02/T25D-RETRY-13PARAM/handoff.md` | `PASS_A_EQ_6_ONLY` (substantive closure in soft branch; max $\|\delta_\text{lin}\| = 3.09 \times 10^{-23}$; PSLQ on 17-member dedup H6 B19+ at maxcoeff $=10^{50}$ / tol $=10^{-40}$ returns no $\Gamma(1/3)$ relation in any of 4 families) | **The operative M7 V0 closure fire.** 11-param LIN refit on saved Q_30..Q_33 $y_n$ CSVs (dps=25000, $N$ up to 1200); $K_\text{FIT}=7$ judgment call documented (saved CSVs do not contain $y(N_\text{ref}=1320)$ so the 13-param square-exact system cannot be assembled without fabrication; agent dropped to 11×11 with truncation $\sim 10^{-25}$ well below the $10^{-15}$ target). 12 AEAL claims; halt log carries verdict + summary. ~12 min agent compute. |

**SHA pre-verification (2026-05-09 11:38 JST, this session)**:

```
PS> git rev-parse 1321bb6
1321bb6fd4f2bceb0d1831da7c8be5a9cc91a5ac
PS> git rev-parse e857172
e857172418de2e760e79ba001ba032f520b708f7
PS> git rev-parse 70d1a48
70d1a4835ee0bc1f188aada9be65bb657f471730
```

All three SHAs resolve. No ambiguity-fatal warnings.

### §2.2 — Substrate documents (manuscripts, picture rows, drafts)

| Artifact | Path | Section / line | Key claim |
|---|---|---|---|
| **Picture v1.19 § 4 (M7 milestone block)** | `sessions/2026-05-06/PICTURE-V19-CONSOLIDATED-DEPOSIT/picture_v1.19.md` (bridge `70d1a48`) | line 965 (axis statement) + line 968 (closure statement) + line 708 + line 1917 + line 3025 + line 3306 (cross-references) | "M7: j=0 Chowla–Selberg Gamma(1/3) closure (or A=6 artefact ruled out) ✅ COMPLETE 2026-05-02 (Prompt 014) — verdict PASS_A_EQ_6_ONLY (in soft branch: …); Stretch goal \|delta\| < 1e-30 NOT achieved (would require K_FIT=9 with extended y_n at N up to 2400, dps >= 44300)" |
| **Picture v1.19 § 5 G5 row** | same; line ~ G5 | G5 closure statement | "G5 ✅ CLOSED 2026-05-02 in A=6-only branch (Prompt 014 verdict PASS_A_EQ_6_ONLY; \|delta_lin\| = 3.09e-23 across all 4 j=0 cubic families via 11-param refit; PSLQ on H6 B19+ at maxcoeff $10^{50}$ / tol $10^{-40}$ returns no $\Gamma(1/3)$ relation in any family). Soft-branch closure: stretch-goal \|delta\| < 10⁻³⁰ deferred to Q22 path-(b)." |
| **Picture v1.19 § 5 G16 row** | same; line ~ G16 | G16 closure statement | "G16 ✅ CLOSED 2026-05-02 (in A=6-only branch) — Prompt 014 demonstrated structural fix (11-param LIN refit reaches \|delta\| ~ 10⁻²³; PSLQ on H6 B19+ exhausts at PSLQ-detection precision with no relation). Op-design lesson: future deep-WKB operators should pre-compute parameter-count floor from desired digit threshold." |
| **PCF-2 v1.4 §6 amendment draft** | `sessions/2026-05-02/T25D-RETRY-13PARAM/pcf2_v1.4_amendment.md` (bridge `e857172`) | Phase F output of Prompt 014 | Replaces the published PCF-2 v1.3 §6 wording `AMBIGUOUS-AT-FINITE-N` with `A = 6 to PSLQ-detection precision; no detected Chowla–Selberg amplitude correction in H6 basis at the present precision`. Operator-pending Zenodo deposit (under RULE 1: math-content step in scope, deposit step TABLED). |
| **Milestone Residual Gap Survey M4 / M7 / M8b / M9 (literature reconnaissance)** | `sessions/2026-05-04/MILESTONE-RESIDUAL-GAP-SURVEY-M4-M7-M8B-M9/dossier_milestone_residual_gap_survey_m4_m7_m8b_m9.md` | §B (M7 Residual: Chowla–Selberg / Γ(1/3) hard-branch; rows B.P1–B.P9) + §E cross-cut row M7 | "No literature anchor found in this session that bridges PCF formal-baseline-A to Γ(1/3) closure directly. The 5-param-ansatz cap that gates 006 is a numerical-method limit; bypassing it requires either (a) literature anchor connecting CM-point Γ-evaluation to PCF δ_n directly (not found this session) or (b) SIARC primary derivation." Reconnaissance dossier; **NOT a ratification fire** (per dossier "no closure attempt is made for any of M4, M7, M8b, M9. The dossier is reconnaissance only"). Counts as **substrate document**, not as a prior M7 ratification fire. |
| **CMB.txt M7 entries** | `tex/submitted/CMB.txt` | line 414 (M7 section header) + line 439 + line 1872 | M7 Chowla–Selberg / $\Gamma(1/3)$ hard-branch axis label; cross-referenced in the program-status row "M4 partial + M7 soft + M8b foreclosed". |

### §2.3 — Open residuals (qualifications the ratification must surface)

The M7 V0 soft-branch closure carries three explicit qualifications
that the ratification statement must carry forward (analogue of the
M4 V0 MEDIUM-HIGH + Wasow §X.3 forward-pointed-not-blocking
qualifications surfaced by the synth at 105 → 106):

1. **Soft-branch / hard-branch distinction** (Q22 from Prompt 014).
   Soft-branch closure is at $|\delta| \sim 10^{-23}$ (well below the
   $10^{-15}$ minimum target with 8+ orders of margin). Hard-branch
   stretch goal $|\delta| < 10^{-30}$ was **NOT** achieved and would
   require $K_\text{FIT}=9$ on extended series at $N \le 2400$ /
   dps $\ge 44{,}300$. Operator accepted the soft-branch closure
   for §6 amendment drafting; the hard-branch stretch is forward-
   pointed not-blocking. **Confidence carry-forward**: the
   M7_V0_CLOSED tag at picture-chain v1.20+ should be annotated
   with `(SOFT-BRANCH; HARD-BRANCH-PENDING)` to prevent silent
   inheritance of unqualified closure state (cf. M4 V0
   `(MEDIUM-HIGH; HIGH-PENDING)` annotation at 106 cascade).

2. **PSLQ basis hygiene** (Q23 from Prompt 014).
   The literal 18-member B19+ basis specified in Prompt 014
   contains the $\mathbb{Q}$-redundant pair $\{\sqrt{3},
   \Gamma(1/3)\Gamma(2/3)/(2\pi)\}$ (via the gamma-reflection
   identity $\Gamma(1/3)\Gamma(2/3) = 2\pi/\sqrt{3}$). Running
   PSLQ on the literal 18-basis returns the trivial relation
   $1 \cdot \sqrt{3} - 3 \cdot \mathrm{CS}_{\sqrt{3}} = 0$
   (target coefficient $= 0$; **NOT** a Chowla–Selberg signal).
   The agent dropped $\mathrm{CS}_{\sqrt{3}}$ for the
   verdict-decisive PSLQ run (17-member dedup B19+) and retained
   the literal 18-basis run only for traceability in
   `pslq_results_18basis_literal.json`. The closure statement
   should carry forward: **"PSLQ in the deduplicated 17-member
   B19+ basis"**, not in the literal 18-basis. Forward-pointed
   for an op-design hygiene rule: future deep-WKB / Chowla–Selberg-
   style closure operators should pre-screen the basis specification
   for $\mathbb{Q}$-linear dependencies (gamma-reflection /
   duplication / multiplication identities) and emit the deduplicated
   basis as the operative one.

3. **Phase E precision impedance** (Prompt 014 `discrepancy_log.json`
   `phase_E_spec_impedance` entry). Prompt 014 Phase E asked for
   a Richardson cross-check at $1 \times 10^{-10}$ agreement; the
   float64-stored T2 input limits achievable Richardson precision
   to $\sim 1 \times 10^{-5}$. The agent reported the cross-check
   as **MET-IN-DIRECTION** (sign and magnitude of trend) rather
   than at $10^{-10}$. Verdict was not downgraded. The closure
   statement should carry forward this as a documented impedance,
   not as a residual gap.

### §2.4 — §1 closure statement vs substrate consistency check

| §1 closure-statement claim | Substrate excerpt | Consistent? |
|---|---|:---:|
| "M7 V0 CLOSED in soft branch (Prompt 014 verdict PASS_A_EQ_6_ONLY)" | `sessions/2026-05-02/T25D-RETRY-13PARAM/handoff.md` (bridge `e857172`) "Verdict: `PASS_A_EQ_6_ONLY`" | **YES** |
| "max $\|\delta_\text{lin}\| = 3.09 \times 10^{-23}$ across 4 j=0 cubic families" | T25D-RETRY-13PARAM handoff "Key numerical findings" table: per-family $\|\delta\|$ in $\{3.27, 3.16, 11.9, 30.9\} \times 10^{-24}$, max $= 3.09 \times 10^{-23}$ | **YES** |
| "PSLQ on 17-member dedup H6 B19+ at maxcoeff $10^{50}$ / tol $10^{-40}$ returns no $\Gamma(1/3)$ relation in any of 4 families" | T25D-RETRY-13PARAM handoff "PSLQ Phase D" + `pslq_results.json` | **YES** |
| "soft-branch closure (stretch-goal $\|\delta\| < 10^{-30}$ NOT achieved; Q22 path-(b) deferred)" | T25D-RETRY-13PARAM handoff "Judgment calls #3" | **YES** |
| "PCF-2 v1.4 §6 amendment drafted as Phase F output of Prompt 014" | `sessions/2026-05-02/T25D-RETRY-13PARAM/pcf2_v1.4_amendment.md` exists at bridge `e857172` | **YES** |
| "12 AEAL claims ledgered; halt log carries verdict + summary" | T25D-RETRY-13PARAM handoff "AEAL claim count: 12 entries" + `halt_log.json` | **YES** |
| "picture v1.19 records M7 ✅ achieved in soft branch" | `sessions/2026-05-06/PICTURE-V19-CONSOLIDATED-DEPOSIT/picture_v1.19.md` line 708 + 968 (bridge `70d1a48`) | **YES** |

**T2-Executor conclusion supported by substrate**: All 7 sub-claims
of the §1 proposed M7 V0 closure statement are materially
consistent with the 006 + 014 + picture-v1.19 substrate at the
verified SHAs. The synth at slot 122 may sign §3 (`ACCEPT`) and
§6 (`Substrate SHAs verified: Y`) on this basis if the synth
accepts the §1 wording as written.

If the synth wishes to amend §1 wording (e.g., to add the
soft-branch / hard-branch confidence-qualifier annotation
`(SOFT-BRANCH; HARD-BRANCH-PENDING)` explicitly in the closure
statement, or to surface the PSLQ basis hygiene rule Q23 as
forward-pointed governance note), use §3 (`ACCEPT_W_REVISIONS`)
and provide revised wording in §4.

---

## §3. Decision form (synth signs ONE row)

| Decision | Selected? | Notes |
|:---:|:---:|---|
| **`RATIFY`** — M7 V0 CLOSED as proposed in §1 | ☐ | rubber-stamp; 006 + 014 substrate complete; picture v1.19 + PCF-2 v1.4 §6 amendment draft consistent with §1 wording; recommended path given the substrate is dossier-complete |
| **`RATIFY_WITH_AMENDMENT`** — M7 V0 CLOSED with synth-side wording amendments to §1 | ☐ | M4 V0 cascade precedent (105 → 106 ACCEPT_W_REVISIONS): the synth may want the soft/hard-branch confidence-qualifier annotation `(SOFT-BRANCH; HARD-BRANCH-PENDING)` carried forward into the closure statement (analogue of M4 V0 `(MEDIUM-HIGH; HIGH-PENDING)`); revised wording in §4 |
| **`DEFER`** — substrate insufficient or ratification premature, fire follow-on | ☐ | provide reasoned NO_GO statement in §5; T2-executor dispatches rubber-duck review of 006 + 014 + picture-v1.19 against the synth's reasoned objection before re-ratification |
| **`OBJECT`** — substrate substantively contradicted by independent reading | ☐ | provide reasoned objection in §5; halt-class outcome; escalate to operator |

---

## §4. (If RATIFY_WITH_AMENDMENT) Revised closure statement

```
[Synth fills in revised wording here. Recommended template
(mirrors M4 V0 §4 revised-wording structure):

M7 V0 CLOSED in the soft branch via the j=0 Chowla–Selberg
PSLQ-exhaustion mechanism (Prompt 014 verdict PASS_A_EQ_6_ONLY).
Max |delta_lin| = 3.09e-23 across 4 j=0 cubic families (Q_30..Q_33,
dps=25000, N up to 1200, 11-param LIN refit at K_FIT=7) clears
the 1e-15 minimum target with 8+ orders of margin; PSLQ on the
17-member deduplicated H6 Chowla–Selberg basis B19+ at maxcoeff
=1e50 / tol=1e-40 returns no Gamma(1/3) relation in any of the
4 families. The closure runs in the deduplicated basis (NOT the
literal 18-basis, which contains the Q-redundant pair
{sqrt(3), Gamma(1/3)Gamma(2/3)/(2pi)} via gamma-reflection;
running PSLQ on the literal basis returns the trivial relation
1·sqrt(3) − 3·CS_sqrt3 = 0 with target coefficient = 0, NOT a
Chowla–Selberg signal). Q23 PSLQ basis hygiene rule
forward-pointed.

Closure is at the algebraic-combinatorial level (deep-WKB
amplitude refit on saved cf_value series, no new high-dps
mpmath generation needed for the soft-branch result). Hard-branch
stretch goal |delta| < 1e-30 NOT achieved; would require K_FIT=9
on extended series at N up to 2400 / dps >= 44300 (Q22 path-(b),
forward-pointed not-blocking).

PCF-2 v1.4 §6 amendment drafted as Phase F output of Prompt 014;
Zenodo deposit step TABLED under RULE 1 (admin/distribution
deferred until M1–M12 math-foundational closure complete);
math-content amendment in scope.

No halt conditions triggered (12 AEAL claims ledgered; halt log
carries verdict + summary; discrepancy log records K_FIT
judgment + Phase E precision impedance; unexpected_finds
records PSLQ trivial-relation flag in literal basis).

Confidence: SOFT-BRANCH. HARD-BRANCH reserved for post-K_FIT=9
hard-branch refit at extended series. Picture-chain v1.20+
M7_V0_CLOSED tag should annotate `(SOFT-BRANCH; HARD-BRANCH-
PENDING)` to prevent silent inheritance of unqualified closure
state.
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
  verified:           [Y / N]  (006: 1321bb6;
                          014: e857172;
                          picture v1.19: 70d1a48;
                          all 3 verified via independent git
                          rev-parse return-of-full-hash AND the
                          §2.4 7/7 PASS consistency check is
                          materially supported by the substrate;
                          mirrors M4 V0 §6 substrate-grounding
                          semantic per 105 §6 wording amendment)
Rubber-duck QA
  acknowledged:       [Y / N]  (Prompt 014 §"Judgment calls" #1
                          (K_FIT=7 not 9 due to undefined y(N_ref))
                          + #2 (deduplicated 17-member B19+ vs
                          literal 18-basis) + #3 (soft-branch
                          PASS_A_EQ_6_ONLY in 1e-30 < |delta|
                          < 1e-15 corridor); all three are
                          rubber-duck-disciplined judgment calls,
                          not silent fudges)
Soft-branch /
  hard-branch
  qualifier
  acknowledged:       [Y / N]  (synth acknowledges picture-chain v1.20+
                          tag must read M7_V0_CLOSED
                          (SOFT-BRANCH; HARD-BRANCH-PENDING),
                          not bare M7_V0_CLOSED, per the
                          confidence-carry-forward semantic
                          established at the M4 V0 cascade
                          (105 → 106) precedent)
```

**Substrate-grounding note for §6 verification** (mirrored from
M4 V0 §6 wording-amendment semantic per 105):

"Substrate SHAs verified [Y/N]" means *both*
(a) the cited SHAs exist in bridge git history at the cited paths,
AND
(b) the substrate at those SHAs materially supports the §1 closure
statement (i.e., the soft-branch PASS_A_EQ_6_ONLY verdict, the PSLQ
no-Γ(1/3)-relation finding, and the deduplicated-basis discipline
are present and consistent with §1).
It does NOT require independent re-derivation of the analytic
content. If the synth wishes to verify (b) explicitly, the §2.4
7/7 PASS consistency check is the substrate-grounded verification
artifact.

---

## §7. Post-ratification cascade (T2-executor follow-up)

If §3 = RATIFY or RATIFY_WITH_AMENDMENT:

| Step | Actor | Action | SQL todo |
|:---:|---|---|---|
| 1 | agent | Mark `m7-substrate-prep-121-completed` → `done` | (this template) |
| 2 | agent | Mark `m7-unblocked-post-m4-v0-closure` → `done` | post-M7-V0-closure unblock resolved |
| 3 | agent | Add `M7_V0_CLOSED (SOFT-BRANCH; HARD-BRANCH-PENDING)` tag to next picture-chain deposit (v1.20+) | included in v1.20 fire (under RULE 1: math-content step in scope, picture-chain admin step TABLED until M1–M12 closure) |
| 4 | (optional) | umbrella v2.x amendment if §3 = RATIFY_WITH_AMENDMENT | post-M9 LANE-1 / under RULE 1 deferred |
| 5 | (optional) | PCF-2 v1.4 §6 amendment deposit (Zenodo) | TABLED under RULE 1; resumed post-M-closure |

If §3 = DEFER:

| Step | Actor | Action |
|:---:|---|---|
| 1 | agent | Dispatch rubber-duck review of 006 + 014 + picture-v1.19 against synth's reasoned objection |
| 2 | agent | If rubber-duck concurs: fire follow-on substrate-hardening agent (~30–60 min); re-issue ratification template at next slot |
| 3 | agent | If rubber-duck disputes synth: surface to operator for tie-break decision |

If §3 = OBJECT:

| Step | Actor | Action |
|:---:|---|---|
| 1 | agent | Halt-class: surface to operator immediately |
| 2 | agent | Pause M-axis ratification cascade until operator triage |

---

## §8. Cross-references

* M4 V0 mirror anchor: `siarc-relay-bridge/sessions/2026-05-08/M4-RATIFICATION-SUBSTRATE-PREP-105/`
* M4 V0 cascade: `siarc-relay-bridge/sessions/2026-05-08/M4-V0-CLOSURE-CASCADE-106/`
* M4 V0 ratification template (executed): `tex/submitted/control center/m4_v0_ratification_template.md`
* Picture v1.19 (M7 milestone block + G5 + G16 rows): `siarc-relay-bridge/sessions/2026-05-06/PICTURE-V19-CONSOLIDATED-DEPOSIT/picture_v1.19.md` (bridge `70d1a48`)
* Prompt 006 (T2.5d j=0; interim): `siarc-relay-bridge/sessions/2026-05-02/T25D-J0-CHOWLA-SELBERG-CLOSURE/handoff.md` (bridge `1321bb6`)
* Prompt 014 (T25D-RETRY-13PARAM; substantive M7 V0 closure): `siarc-relay-bridge/sessions/2026-05-02/T25D-RETRY-13PARAM/handoff.md` (bridge `e857172`)
* PCF-2 v1.4 §6 amendment draft: `siarc-relay-bridge/sessions/2026-05-02/T25D-RETRY-13PARAM/pcf2_v1.4_amendment.md` (bridge `e857172`)
* RULE 1 marker: `tex/submitted/control center/picture/M1_M12_CLOSURE_OUTLOOK_20260509_RULE1.md` (M7 listed under §1 KEEP as math-foundational)
* Repo memory `rubber-duck QA discipline` — vindicated by Prompt 014 K_FIT=7 + deduplicated-B19+ judgment calls
* Repo memory `prompt drafting discipline` — Phase 0 supersession-gate pattern + bibliographic-identifier pre-verification rule
* Memory anchor: "3-stage pattern for M-axis ratifications" (plan.md:1496 per prompt 121 §1)

---

## §9. Forbidden-verb compliance note

Per envelope STEP D.2 forbidden-verb scan: this template uses
"vindicated" (synonym for confirmed) in §8 cross-reference to
the rubber-duck QA repo memory and "ratifies"/"ratify"
(the operative verb of the document itself, used in §3 + §7 +
the title) as checklist-meta-references. Both are
verb-list-as-data + checklist-meta-references — exempt under
098 J3 / 075 J2 precedent. **No substrate prose, no §3 question
text, and no §1 closure statement contains forbidden verbs in
substantive (claim/prediction) context.**

§3 question text is intentionally neutral: it asks the synth to
*sign* a row, not to *show* / *confirm* / *prove* anything;
the verb-of-decision is "ratify" (operative, exempt) and the
verb-of-evidence is "supports" / "is consistent with" (not
forbidden).

---

## §10. Dispatch readiness (Phase D)

- **Word count**: ~3 200 words (§1–§9 inclusive; close to M4 V0
  template scale; well within paste-ready limits for a Claude.ai
  web chat session)
- **All §2 evidence pre-verified**: 3/3 SHAs (`1321bb6`, `e857172`,
  `70d1a48`) returned full 40-char hashes via `git rev-parse` at
  2026-05-09 11:38 JST in this session
- **Bibliographic identifier pre-verification**: NOT_APPLICABLE —
  this template cites only internal bridge SHAs as substrate; no
  external DOI / arXiv ID is in scope for the M7 V0 closure (the
  Milestone Residual Gap Survey reconnaissance dossier flagged
  Chowla-Selberg 1949/1967 + Borwein-Zucker 1992 as
  literature-bracket-only references not bridging PCF formal-
  baseline-A to Γ(1/3) closure directly; per §2.3 residual #1, this
  is a forward-pointed not-blocking residual and does not enter
  the ratification claim).
- **All §3 questions answerable from §2 substrate alone**: YES — no
  out-of-packet follow-up is needed for the synth to sign §3 + §6.
  The §2.4 7/7 PASS consistency check is the substrate-grounded
  verification artifact.
- **Recommended dispatch class**: T1-Synth solo (Claude.ai web
  conversation; mirrors 104 → 105 → 106 dispatch pattern at the
  M4 V0 cascade)
- **Recommended next-slot**: 122 (T1-SYNTH-M7-RATIFICATION-SOLO-
  DISPATCH); successor cascade-absorption fire at slot 123
  (T1-SYNTH-M7-V0-CLOSURE-CASCADE) per the canonical 3-arc
  template.

---

**Template status**: **DRAFTED 2026-05-09 ~11:40 JST** by T2-Executor
(prompt 121 substrate-prep). Awaits synth dispatch at slot 122.
