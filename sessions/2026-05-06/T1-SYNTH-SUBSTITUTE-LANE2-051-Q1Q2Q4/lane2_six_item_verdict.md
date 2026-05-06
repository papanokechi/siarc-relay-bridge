# LANE-2 six-item adjudication — STEP 5

**Reviewer:** Copilot Researcher Agent (canonical T1-Synth-SUBSTITUTE-LANE-2).
**Date:** 2026-05-06 W19 Wed JST.
**Substrate:** anchor SHAs A1-A9; V1-V6 independent verification; STEP 3
adoption audit (8/8 ADOPTED); STEP 4 depth probes P1-P4.

For each of the 6 follow-up items per `synth_substitute_verdict.md`
§"Recommended canonical T1-Synthesizer follow-up" L386-410, this LANE-2
review issues a verdict with substrate-grounded reasoning, confidence
level, and dependency map.

---

## Item 1 — Mechanism arbitration: PROTOCOL_TO_STRATUM_MISMATCH_FIRST_PIVOT scope

**Synth-substitute proposal:** RATIFY for PCF-2 R1.1/R1.3/Q1 specifically;
PCF-1 / picture v1.20 / scope wording at MEDIUM confidence (synth-substitute L335).

**LANE-2 verdict:** **`RATIFY_WITH_NARROW_REVISION`**.

### Reasoning (substrate-grounded)

- **V1** (cf_value() at session_c1_wkb.py L78-86): canonical (1, b) recurrence;
  $a_n \equiv 1$ (deg_a = 0). Verbatim code block.
- **V2** (session_b_pslq.py L162-170 + quartic_tail_fit_all60.py L21-30):
  identical (1, b) recurrence; deg_a = 0 across all three pcf2 cubic + quartic
  pipelines.
- **V3** (pcf2_program_statement.tex L228-234): declared
  $a_n = \delta_1 n + \delta_0$, $\delta_1, \delta_0 \in \mathbb{Z}$, **no
  $\delta_1 \ne 0$ restriction imposed** — declared scope is deg_a $\in \{0, 1\}$
  formally, with the deg_a = 0 corner included.
- **V6** (independent WZ derivation): $A_{\rm naive} = 2d - d_a$;
  for deg_a = 0, $A_{\rm naive} = 2d$ uniform, $\gamma_{\rm sub} \propto -c_a/c_b$.
- **P1** (depth probe, repository sweep): UNIFORM (1, b) deg_a = 0 across
  **9 cf_value() implementations** in pcf-research/pcf2/, covering Sessions
  A2 + B + C1 + R1.1 + R1.2 + R1.3 + Q1 (full PCF-2 harvest).
- **P2** (depth probe): Phase A WZ table omits deg_a = 0 row by ASSUMPTION;
  one-row extension closes Phase D's "structural gap" without invoking
  borderline (i') or exceptional locus (ii').
- **P4** (depth probe): mismatch locus is intra-`pcf2_program_statement.tex`
  (§3 setup vs §6 B4), not "prose vs scripts" as currently worded by the
  synth-substitute.

The core finding (PROTOCOL_TO_STRATUM_MISMATCH at deg_a = 0 → $A_{\rm naive} = 2d$)
is independently confirmed at full coverage. **RATIFY** the synth-substitute's
Q1 verdict.

### Narrow revision (LANE-2-specified)

The scope of the mismatch finding is **EXPANDED**, not contracted, by LANE-2's
independent investigation:

1. **(P1 expansion)** Scope extends from "PCF-2 R1.1/R1.3/Q1" to **all of
   PCF-2's harvest** including Sessions A2 + B + C1 + R1.1 + R1.2 + R1.3 + Q1
   (all 9 cf_value() implementations use deg_a = 0).
2. **(V5 / P3 expansion)** Scope extends to include **PCF-1 v1.3 §6 Theorem 5
   V_quad upper branch** (`algebraic_independence_audit.py` L37-40 confirms
   V_quad uses $a(n) = 1$, deg_a = 0). bt_baseline_note v1.0 §4.2's
   mechanism-(i') attribution for V_quad's $A = 4$ is substrate-level WRONG;
   V_quad is fully recovered by the deg_a = 0 row of the WZ normal case
   ($A_{\rm naive} = 2d = 4$ at $d = 2$).
3. **(P4 wording refinement)** Mismatch locus is **intra-`pcf2_program_statement.tex`**
   (§3 setup at L228-234 declares $a_n = \delta_1 n + \delta_0$;
   §6 B4 at L457 uses verbatim "PCF (1, b)" notation). The scripts implement
   §6's stratum exactly; the inconsistency is between §3 and §6, not between
   prose and scripts. This is a wording-level refinement to the
   synth-substitute's framing that should propagate into the rule5 vocabulary
   discussion (Item 4).

### Confidence

**HIGH** (substrate-grounded at full coverage; V1 + V2 + V6 + P1 + P2 + P4
mutually consistent; no counter-evidence).

### Dependencies

- **Gates Item 3** (bt_baseline_note revision scope): a RATIFY here authorises
  the bt_baseline_note follow-up note approach.
- **Gates Item 5** (picture v1.20 absorption): a RATIFY here unlocks
  ANOMALY_ENTRY status for picture v1.20.
- **Gates Item 6** (PCF-2 v3.x wording): a RATIFY here is necessary but not
  sufficient for a Zenodo amendment.
- **Independent of Items 2 (Phase 3 sub-tasks) and 4 (rule5 vocab)** in the
  sense that those can proceed in parallel.

---

## Item 2 — Authorize/defer T1 Phase 3 sub-tasks 3-A through 3-E

**Synth-substitute proposal:** AUTHORIZE all 5 sub-tasks (synth-substitute
L171-180 + L264-271).

**LANE-2 verdict:** **`SPLIT`** (3-A AUTHORIZE; 3-B AUTHORIZE; 3-C DEFER;
3-D AUTHORIZE; 3-E DEFER).

### Reasoning (per sub-task)

#### 3-A — Extend WZ table to deg_a = 0: **AUTHORIZE**.

**Substrate:** P2 (depth probe) has already PRODUCED the substantive content
of 3-A (the deg_a = 0 row extension to Phase A's table) and verified it
against PCF-2 R1.1+R1.3+Q1 + d=2 V_quad empirics. Sub-task 3-A is now a
**write-up task**, not a derivation task.

**Confidence:** HIGH (substrate already produced).

**Output target:** Extension to `phase_a_summary.md` or new
`phase_a_supplementary_deg_a_zero.md` in
`siarc-relay-bridge/sessions/<future-date>/T1-PHASE3-3A-WZ-EXTENSION/`.

#### 3-B — Convergent-residual fit-protocol audit: **AUTHORIZE**.

**Substrate:** Mechanism (ii') (definitional slippage) remains audit-worthy
per synth-substitute L156-167. The harvest scripts fit
$\log|\delta_n|$ where $\delta_n = L_N - L_{\rm ref}$ is the convergent
residual; the WZ leading-coefficient correspondence ($-A_{\rm naive}$
coefficient of $n \log n$ in $\log|\delta_n|$) is mechanical, but
finite-$N$ tail-window bias must be quantified.

**Confidence:** MEDIUM (definitional audit scope is well-defined but execution
requires fresh numerics over $N_{\rm ref} \in \{300, 600, 1200\}$).

#### 3-C — Note revision: **DEFER** (blocked by Item 3).

**Substrate:** 3-C is contingent on 3-A + 3-B verdicts AND on Item 3's
revision scope decision. LANE-2's Item 3 verdict is `LEAVE_V1_0_CANONICAL_WITH_VERDICT_AS_FOLLOW_UP_NOTE`,
which **redirects 3-C from "v1.x revision" to "follow-up note authoring"**.
3-C should be re-scoped accordingly before authorisation.

**Confidence:** MEDIUM (blocked on Item 3).

#### 3-D — Costin sectorial upgrade: **AUTHORIZE**.

**Substrate:** Q4 verdict (synth-substitute L262 + L268-271):
WASOW_CANONICAL_TARGET_WITH_COSTIN_OPERATIONAL_SUBSTITUTE. Costin 2008 ch.5
is on-disk at
`tex/submitted/control center/literature/g3b_2026-05-03/06_costin_2008_chap5.txt`.
The Borel-Laplace radius theorem provides the Gevrey-1 sectorial-summability
upgrade for the Wallis recurrence's formal series at $\mu_{\rm dom} = d$,
$\mu_{\rm sub} = -d$ (PCF-2 R1.1/R1.3/Q1 stratum).

3-D is **independent of Item 1's outcome** (Q4 finding is independent of Q1
per synth-substitute L240).

**Confidence:** MEDIUM-HIGH (Costin substrate is on-disk; sectorial-upgrade
hypotheses verifiable without OCR-clean Wasow access).

#### 3-E — Wasow OCR resolution: **DEFER**.

**Substrate:** Wasow PDF on disk is image-only with no OCR per A-01 verdict
(synth-substitute L249-251). 3-E is contingent on a separate OCR-acquisition
effort (re-scan or alternate edition acquisition). This is an
acquisition-class task, lower priority than 3-D's Costin operational
substitute, which can proceed without 3-E.

**Confidence:** MEDIUM (acquisition-class; benefits from 3-D first).

### Dependencies

- 3-A authorised regardless of Item 1 outcome (P2 has produced the
  derivation; 3-A is now write-up).
- 3-C deferred pending Item 3 outcome.
- 3-D, 3-E independent of Q1 per synth-substitute Q4 verdict.

---

## Item 3 — bt_baseline_note v1.x revision scope

**Synth-substitute proposal:** "v1.0 deposit can stand canonical" with
this verdict recorded as a follow-up note (synth-substitute L186-189).

**LANE-2 verdict:** **`LEAVE_V1_0_CANONICAL_WITH_VERDICT_AS_FOLLOW_UP_NOTE`**.

### Reasoning (substrate-grounded)

- **bt_baseline_note v1.0 Theorem 1.1 is correct AS STATED** for the band
  $\deg_a \in \{d-1, d, d+1\}$ (per V4 + bt_baseline_note.tex L388-389
  symmetric row $\deg_a = d, \mu_{\rm sub} = 0$; the band's bounds are
  literally the three SIARC conventions of Phase A).
- The deg_a = 0 row is an **ADDITIVE EXTENSION**, not a correction. v1.0
  does not need retraction.
- **§4.2's mechanism-(i') attribution for V_quad** (P3 finding) is
  substrate-level wrong, BUT the §4.2 prose phrases this as conditional/
  open-content language: "consistent with the borderline-locus mechanism
  (i') ... the closure of which is the open content of §6 Q[mechanism]"
  (bt_baseline_note.tex L484-487). The wording is **forward-looking
  conjecture-class**, not asserted-as-fact. So §4.2 is not retroactively
  wrong — it is open-conjecture content that LANE-2 now resolves
  (Q[mechanism] closes via deg_a = 0 row, not via mechanism (i')).
- v1.1_ADDITIVE_DEG_A_ZERO_ROW (a Zenodo deposit revision) creates
  **canonical-version ambiguity** — citers must specify v1.0 vs v1.1
  in references, which is logistically expensive for an additive
  extension.
- v1.1_SECTION_5_REFRAMING is **heavier intervention than substrate
  justifies** — §5's gap-framing remains correct for $\deg_a \in \{d-1, d, d+1\}$
  scope.
- **A separate follow-up note** (e.g., `bt_baseline_note_followup_v1.0.tex`
  in the bridge) cleanly absorbs the LANE-2 + P2/P3 findings as
  ADDITIVE content without disturbing v1.0's canonical citation.

### Confidence

**MEDIUM-HIGH** (ratifies synth-substitute's recommended approach;
LANE-2 P3 finding adds V_quad scope to the follow-up note).

### Dependencies

- **Depends on Item 1** (RATIFY required to authorise the follow-up note).
- **Depends on Item 4** (rule5 vocab): the follow-up note uses the term
  "protocol-to-stratum mismatch" which is pending rule5-vocab ratification.
  If Item 4 is DEFER_TO_W21, the follow-up note can use the term with
  a footnote flagging "pending rule5 ratification".

---

## Item 4 — rule5 amendment vocabulary fold-in

**Synth-substitute proposal:** "flagged for canonical T1-Synth assent at
next ISO week to either ratify the new label or fold it back into rule5's
existing terminology" (synth-substitute L308-310).

**LANE-2 verdict:** **`DEFER_TO_W21`**.

### Reasoning (substrate-grounded)

- The "protocol-to-stratum mismatch" label is novel and substrate-grounded
  (V3 + V4 + V5 + P4) but its acceptance into the rule5 amendment vocabulary
  has **repo-wide implications** for all future SIARC dispatches (cross-tier
  classifier-label hygiene, SYNTH-TRACK CMB rendering rules, etc.).
- LANE-2 review is by a **Copilot Researcher Agent**, distinct from
  canonical T1-Synth (Claude.ai weekly cadence). Per the relay 061 prompt's
  governance note, LANE-2 carries the same epistemic weight as a canonical
  T1-Synth weekly verdict UNLESS the operator flags need for LANE-1
  ratification.
- Rule5 vocabulary changes are precisely the class of decision that
  benefits from LANE-1 (Claude.ai) ratification at the next available
  weekly cadence. **W20 (Mon 2026-05-11) is unavailable** for LANE-1
  per operator chat 2026-05-06 ~17:46 JST. The next earliest LANE-1
  cadence is **W21 (Mon 2026-05-18)**.
- Until W21 LANE-1 ratifies, the term "protocol-to-stratum mismatch"
  may be used in LANE-2-class deliverables (Item 3 follow-up note,
  Item 5 picture v1.20 anomaly entry) with a footnote: "Term pending
  W21 canonical T1-Synth (LANE-1) rule5-vocabulary ratification".

### Alternatives considered

- **FOLD_IN now** (LANE-2 authority): rejected — LANE-2 should not
  unilaterally extend rule5 vocabulary; this is canonical-Synth
  jurisdiction.
- **REJECT_FOLD_IN**: premature without LANE-1 review; the substrate
  basis for "protocol-to-stratum mismatch" is strong (V3+V4+V5+P4),
  so rejection is unwarranted at this stage.

### Confidence

**MEDIUM** (LANE-2 epistemic-floor decision; intentional escalation to
canonical LANE-1 cadence).

### Dependencies

- Independent of Items 1, 2, 3, 5, 6 — can be deferred without blocking.
- Item 3 follow-up note may use the term with a "pending W21" footnote.

---

## Item 5 — picture v1.20 absorption decision

**Synth-substitute proposal:** "Decide whether picture v1.20 (LATE-FIRE
post-W20) absorbs this finding as an anomaly entry or as a primary
substrate row" (synth-substitute L401-403); rated MEDIUM confidence
on picture v1.20 implications (synth-substitute L335).

**LANE-2 verdict:** **`ANOMALY_ENTRY`**.

### Reasoning (substrate-grounded)

- The protocol-to-stratum mismatch finding is INSTRUCTIVE but the
  cross-document scope (PCF-1 V_quad reinterpretation per V5/P3 +
  Phase A baseline extension per P2 + intra-document mismatch locus
  per P4) is not yet AUDITED at PRIMARY-ROW status.
- LANE-2 P2/P3 findings extend the synth-substitute's scope but
  do NOT escalate confidence to HIGH on the cross-document
  implications (synth-substitute self-rates MEDIUM at L335).
- A primary substrate row in picture v1.20 implies "load-bearing,
  fully audited, cross-checked" content. The PCF-1 V_quad
  reinterpretation in particular requires:
  - A dedicated V_quad re-derivation under the deg_a = 0 reading.
  - Cross-check against the QL01-QL26 / V_quad split-confidence claim
    in PCF-1 v1.3 §6 Theorem 5 prose.
  - Confirmation that no other PCF-1 d=2 specimens exhibit the
    same deg_a = 0 corner-case treatment.
- These are precisely 3-A / 3-B Phase 3 sub-tasks. Picture v1.20
  primary-row status should be GATED on 3-A + 3-B completion.
- Until that gate clears: ANOMALY_ENTRY is the right level — log
  the finding visibly, with "promotion to primary-substrate-row gated
  on Phase 3 sub-task 3-A + 3-B" disposition.

### Alternatives considered

- **PRIMARY_SUBSTRATE_ROW**: rejected — confidence not yet HIGH
  on cross-document implications; gates not clear.
- **DEFERRED_TO_V1.21**: rejected — too far; finding is concrete
  and load-bearing for ongoing T1 Phase 3 dispatch.

### Confidence

**MEDIUM** (matches synth-substitute self-assessment for picture
v1.20 implications).

### Dependencies

- **Depends on Item 1** (RATIFY required to authorise anomaly entry).
- **Promotion to primary-row gated on Item 2 sub-tasks 3-A + 3-B**
  (Phase 3 dispatch).

---

## Item 6 — PCF-2 v3.x scope-statement wording revision

**Synth-substitute proposal:** "Decide whether PCF-2 v3.x scope-statement
wording requires updating to clarify the implemented stratum ($a_n \equiv 1$)
vs the declared stratum ($a_n = \delta_1 n + \delta_0$)" (synth-substitute
L405-410); rated MEDIUM confidence.

**LANE-2 verdict:** **`HOLD`**.

### Reasoning (substrate-grounded)

- **V3 + P4 finding**: the mismatch locus is **intra-`pcf2_program_statement.tex`**
  (§3 at L228-234 declares $a_n = \delta_1 n + \delta_0$;
  §6 B4 at L457 uses "PCF (1, b)" verbatim). The wording revision question
  is therefore: **clarify §3 to match §6 B4's actual stratum, OR clarify
  §6 B4 to match §3's declared scope?**
- The HARVEST scripts (V1+V2+P1) implement §6 B4's "(1, b)" exactly. So
  the empirical record supports CLARIFYING §3 (narrow it to deg_a = 0
  to match §6 + harvest), not EXPANDING §6 B4.
- A Zenodo amendment to PCF-2 v3.1 (or wording revision in v3.x preprint)
  is a SUBSTANTIVE document change with **DOI versioning + citation impact**
  — heavyweight machinery. LANE-2 (Copilot Researcher Agent) should NOT
  authorise a Zenodo amendment without LANE-1 (Claude.ai) ratification,
  particularly given that:
  - The mismatch is a **wording inconsistency, not an empirical error** —
    PCF-2 v3.x's central conjectures (B4, B4''s falsification) remain
    correct under deg_a = 0.
  - Citers reading v3.x in the deg_a = 1 reading will reach exactly the
    same numerical conclusions ($A = 2d$ at $d=3,4$, B4' falsified)
    as readers in the deg_a = 0 reading. The prose-vs-implementation
    discrepancy does NOT propagate to a citation-quality difference.
- HOLD: defer Zenodo amendment decision to W21 LANE-1 (Claude.ai).
  In the interim, **add an internal note to PCF-2 v3.x manuscript-tracking**
  that §3/§6 wording reconciliation is pending. This note can be a
  comment in `tex/submitted/pcf2_program_statement.tex` near L228 or
  L457 (without modifying compiled output).

### Alternatives considered

- **REVISE_NOW** (operator-side Zenodo amendment): rejected —
  out-of-scope for LANE-2; canonical-Synth (LANE-1) jurisdiction.
- **DEFER_TO_V4**: rejected — too vague; v4.x release timeline not pinned;
  HOLD with explicit W21 LANE-1 deadline is more concrete.

### Confidence

**MEDIUM** (LANE-2 epistemic-floor; canonical LANE-1 jurisdiction for
Zenodo amendment authorisation).

### Dependencies

- **Independent of Items 1-5** — HOLD pending W21 LANE-1.
- **Coupled to Item 4 outcome**: if Item 4 W21 LANE-1 ratifies the
  "protocol-to-stratum mismatch" rule5-vocab fold-in, that ratification
  also informs the §3 vs §6 wording revision target language.

---

## Six-item adjudication summary

| Item | Topic | LANE-2 verdict | Confidence | Dependencies |
|------|-------|----------------|------------|--------------|
| 1 | PROTOCOL_TO_STRATUM_MISMATCH scope | **RATIFY_WITH_NARROW_REVISION** | HIGH | Gates Items 3, 5, 6 |
| 2 | Phase 3 sub-tasks 3-A..3-E | **SPLIT**: 3-A AUTHORIZE / 3-B AUTHORIZE / 3-C DEFER (blocked on Item 3) / 3-D AUTHORIZE / 3-E DEFER | HIGH (3-A); MEDIUM (3-B); MEDIUM-HIGH (3-D); MEDIUM (3-C, 3-E) | 3-C blocked on Item 3 |
| 3 | bt_baseline_note v1.x revision | **LEAVE_V1_0_CANONICAL_WITH_VERDICT_AS_FOLLOW_UP_NOTE** | MEDIUM-HIGH | Depends on Items 1, 4 |
| 4 | rule5 vocab fold-in | **DEFER_TO_W21** | MEDIUM | Independent |
| 5 | picture v1.20 absorption | **ANOMALY_ENTRY** | MEDIUM | Depends on Item 1; promotion gated on Item 2 (3-A + 3-B) |
| 6 | PCF-2 v3.x wording revision | **HOLD** | MEDIUM | Independent; coupled to Item 4 outcome |

**Aggregate verdict-tag string** (for AEAL claim C5):
`Item 1: RATIFY_WITH_NARROW_REVISION; Item 2: SPLIT; Item 3: LEAVE_V1_0_CANONICAL_WITH_VERDICT_AS_FOLLOW_UP_NOTE; Item 4: DEFER_TO_W21; Item 5: ANOMALY_ENTRY; Item 6: HOLD`.

**Pattern observation:** Items 1, 2, 3 are SUBSTANTIVELY decided by
LANE-2 (RATIFY / AUTHORIZE / specific revision scope). Items 4, 5, 6
are intentionally DEFERRED or HELD pending W21 LANE-1 (Claude.ai)
ratification, reflecting LANE-2's epistemic-floor discipline: LANE-2
decides the script-and-derivation-grounded findings in scope, but
escalates repo-wide vocabulary changes (Item 4), picture-row promotions
(Item 5 promotion gate), and Zenodo amendments (Item 6) to the
canonical weekly cadence.
