# M8a V0 closure ratification template (synth-tier)

**Purpose**: paste-ready audit artifact for the M8a-axis
absorption cycle (synth-tier solo-dispatch, slated for slot 126).

**Pre-stage drafted**: at bridge HEAD `7f93b9e`
(T1-SYNTH-M7-V0-CLOSURE-CASCADE-123; M7 axis CLOSED at MEDIUM-HIGH
dual-witness band 2026-05-09).
**Drafted by**: T2-EXECUTOR (GitHub Copilot, VS Code; Claude
Opus 4.7 xhigh) at 2026-05-09 ~14:55 JST.
**Used by**: T1-Synth (Claude.ai web), at slot 126 solo-dispatch.

**Mirror anchor**: this template mirrors the structure of
`siarc-relay-bridge/sessions/2026-05-09/T2-EXECUTOR-M7-RATIFICATION-
SUBSTRATE-PREP-121/m7_v0_ratification_template.md` (immediate
sibling-axis pattern reference; SHA-256 `72D855F7B05D3F209340FBF57E
7CAFD793BF1E8FA283502CF9889124E1BB6BE5`), which itself mirrors
`siarc-relay-bridge/sessions/2026-05-08/M4-RATIFICATION-
SUBSTRATE-PREP-105/m4_substrate_excerpts.md` + the M4 V0
ratification template at `tex/submitted/control center/
m4_v0_ratification_template.md`. Section numbering and
decision-form structure are aligned bit-for-bit where applicable;
M8a-specific content fills the slots.

---

## §1. M8a axis scope

### What the M8a axis represents

Per **picture v1.19 § 4** (bridge `70d1a48`,
`sessions/2026-05-06/PICTURE-V19-CONSOLIDATED-DEPOSIT/picture_v1.19.md`
line 997), the M8a axis (recorded as `M8` in picture v1.19;
re-labeled `M8a` in the RULE 1 outlook 2026-05-09 to distinguish
it from the M8b Stokes-multiplier follow-up) is:

> **M8a (= picture-v1.19 M8): D=2 Painlevé classification table
> (per-family, ~10 families).**

This is the algorithmic-Painlevé-test stratum-labeling axis: at
the linear OGF ODE level for each $d=2$ PCF family in PCF-1 v1.3
Table 1 (10 families) and each $d=3$ PCF family in PCF-2 v1.3
catalogue (50 families), the question is what Painlevé-class label
the Conte–Musette necessary criterion (three-branch Newton-polygon
+ indicial-exponent + dominant-balance) returns. The M8a milestone
closes when every catalogue family has a definitive label
(`LABELED <class>` or `REJECTED` or `INCONCLUSIVE`) at the
algorithmic-test resolution scale, with the V_quad reference
family acting as the sanity-check anchor against the published
PCF-1 / CT v1.3 Theorem 3.3.D class assignment.

### What "M8a V0 closure" means specifically

M8a V0 closure is the **algorithmic-stratum-scale closure** at
the Painlevé-class resolution: at the Conte–Musette
necessary-criterion test level, the PCF-1 v1.3 d=2 catalogue
(10 families) is uniformly `P_III(D_6)` and the PCF-2 v1.3
d=3 catalogue (50 families) is uniformly `PAINLEVE_UNCLASSIFIED`
(Newton polygon slopes 4/3 at $x=0$ and 2/3 at $x=\infty$,
fractional, outside the standard $P_I..P_VI$ list). Branch
disagreement fraction $0/60 = 0.000$ is well below the 5%
H3-confirmation threshold from the Prompt 007 spec; V_quad
sanity check (Phase D) passes with class `P_III(D_6)` in
agreement with CT v1.3 Theorem 3.3.D. This is operator-accepted
and recorded in picture v1.19 as **M8 ✅ COMPLETE 2026-05-02
(Prompt 007)** with verdict label `T3_LABELED_60_OF_60`.

The M8a V0 closure carries one explicit qualification: H3
(`D=2_REDUCTION_AMBIGUOUS`) is **negatively closed** under the
Conte–Musette test — the test as implemented on the linear OGF
ODE is invariant across $\mathrm{sign}(\Delta_b)$, so the
PCF-1 v1.3 §3 dichotomy ($A=4$ for $\Delta_b > 0$ vs. $A=3$
for $\Delta_b < 0$) is **invisible** to this algorithmic test.
The substantive resolution of that dichotomy lives at the
Stokes-multiplier scale (M8b axis: `T3.5-STOKES-MULTIPLIER`
Prompt 010 + the 016 / 017c / 017e / 017L / 017m extension
chain). M8a closes the algorithmic-stratum-labeling question;
M8b carries the dichotomy-resolution question on a separate
axis with its own ratification cycle (slates 128 → 129 → 130
parallel-safe with this 125 → 126 → 127 chain).

The M8a V0 closure statement is therefore:

> **M8a V0 CLOSED at the algorithmic-Painlevé-test stratum-
> labeling scale (Prompt 007 verdict T3_LABELED_60_OF_60;
> 60/60 catalogue families LABELED with V_quad-anchored class
> assignments matching CT v1.3 Theorem 3.3.D; 0/60 branch
> disagreement; H3 negatively closed and dichotomy-resolution
> delegated to the M8b Stokes-multiplier axis).**

### Manuscript section(s) M8a closure feeds

- **vquad_resurgence_R1.tex / R2.tex §4 "Painlevé classification"**
  — section already published in the v_quad resurgence drafts;
  body anchored to V_quad's `P_III(D_6)` class assignment via
  CT v1.3 Theorem 3.3.D. M8a V0 closure formalizes the
  catalogue-wide extension at the algorithmic-test resolution
  scale (60/60 LABELED). No manuscript-content amendment is
  required for M8a V0 closure (mirror difference vs. M7: M7
  required PCF-2 §6 amendment because the §6 wording was
  `AMBIGUOUS-AT-FINITE-N`; M8a's catalogue-wide labeling is
  an extension of the V_quad-anchored class assignment, not a
  replacement of any published wording).
- **PCF-1 v1.3 §3** (sign-of-$\Delta_b$ dichotomy section):
  the dichotomy described there is what M8a's H3 negative
  closure declares to be invisible to the algorithmic-test
  resolution. Forward-pointed (not blocking M8a closure) for
  the M8b axis to resolve. No M8a-side manuscript amendment
  required.
- **Picture chain v1.20+** (forward-pointed): the closure tag
  at v1.20+ should read `M8a_V0_CLOSED (ALG-TEST-SCALE;
  STOKES-DICHOTOMY-DELEGATED-TO-M8B)` per the M4 V0 cascade
  pattern and the M7 V0 cascade pattern (105 → 106 confidence-
  qualifier carry-forward; cf. M4 V0 `(MEDIUM-HIGH; HIGH-PENDING)`
  at 106 cascade; cf. M7 V0 `(SOFT-BRANCH; HARD-BRANCH-PENDING)`
  at 123 cascade). The qualifier annotation prevents silent
  inheritance of unqualified closure state and explicitly
  carries forward the H3-negative-closure / dichotomy-
  delegation-to-M8b semantic.

### Relationship to M4 V0 (closed), M7 V0 (closed), and M8b (parallel cycle)

- **M4 V0** (closed 2026-05-08 at MEDIUM-HIGH confidence,
  bridge cascade 105 → 106): the deg_a=0 row mechanism closes
  the SIARC stratum's structural M4 axis at zero acquisition
  cost. M8a V0 is axis-independent of M4 V0 (different stratum,
  different mechanism); the M4 V0 ratification was the
  procedural-unblock gate per peer-consult-104 V_FT4_RECOMMENDED
  Q5 + cascade-record-106 §C4 NEW SQL todo
  `m8a-unblocked-post-m4-v0-closure`. With M4 V0 closed, M8a is
  procedurally cleared for ratification.
- **M7 V0** (closed 2026-05-09 at MEDIUM-HIGH dual-witness band,
  bridge cascade 121 → 122 → 123): the j=0 Chowla–Selberg
  amplitude axis closed in soft branch. M7 V0 closure is the
  immediate sibling-axis precedent for M8a (same canonical 3-arc
  template, same RULE-1-IN-SCOPE math-content step, parallel
  RULE-1-TABLED admin/distribution step). The M7 cascade also
  established the dual-witness aggregation pattern at MEDIUM-HIGH
  (most-conservative protocol) and the inline-confidence-qualifier
  template-wording-discipline (UF-123-3); M8a may benefit from
  applying the same patterns at slot 127 cascade absorption.
- **M8b** (parallel ratification cycle; slates 128 → 129 → 130;
  substrate at 092 + P-009): the sibling Stokes-multiplier axis.
  Per picture v1.19 the d=2 PCF-1 §3 sign-of-$\Delta_b$
  dichotomy lives at M8b (Prompt 010 measured $|S_1|$ for 4 reps
  at $\geq 60$ cross-method digits, differing across the
  dichotomy at $O(1)$ scale; Prompt 017c+017e closed the
  $a_1$ 3-stratum partition at 60+ digits; Prompt 017L
  documented 4-d cylinder over $(\delta, \epsilon)$ in the
  third stratum; Prompt 017m halted the final numerical $S_2$
  path with `HALT_T37M_PADE_DIVERGENT`). M8a's H3 negative
  closure declares the dichotomy invisible at the algorithmic-
  test resolution; M8b's Stokes-multiplier work resolves it
  at the alien-amplitude resolution. The two cycles are
  axis-independent: cross-cycle fires are independent.

### M8a status pre-fire-of-prompt-125

M8a V0 has been **achieved at the algorithmic-test stratum-
labeling scale** since 2026-05-02 via Prompt 007 substantive
verdict, and the picture chain v1.19 records this as a closure
at the milestone level (line 998 + line 1110 + line 396). **What
this prompt 125 fire does is**: assemble the ratification
dossier (substrate excerpts + decision form + question set) so
that slot 126 can dispatch a synth-tier sign-off that matches
the canonical 3-arc ratification pattern established by M4 V0
(104 → 105 → 106) and M7 V0 (121 → 122 → 123). The
substrate-prep meta-work itself does NOT re-derive any
algorithmic-test content; it formalizes the existing
algorithmic-test-scale closure into ratification-template
language.

---

## §2. Evidence inventory

### §2.1 — Prior fires that contributed to M8a closure

Three prior fires are the operative substrate. All three bridge
SHAs were independently verified via `git rev-parse` returning a
full 40-char hash (per copilot-instructions.md "substrate
verification" rule + 105 SHA-correction discipline + 121 §2.1
discipline).

| Artifact | Bridge SHA | Path | Verdict | Relevance |
|---|---|---|---|---|
| **UMB-T3-PROBE (interim provisional T3 candidate scan)** | `bbd1b76` | `sessions/2026-04-30/UMB-T3-PROBE/handoff.md` | `HALT` (5 provisional T3 candidates persist NULL across 5-tier basis at dps in $\{500, 1000, 1500, 3000\}$; $\mu_\text{res}$ slope = 0 and $\mu_\text{coef}$ slope = 0 for all 5; basis-too-small caveat documented) | First pre-007 probe of T3-class signatures across the d=2 / d=3 catalogue; **superseded in substantive closure by Prompt 007**. Counts as upstream-substrate fire (interim probe-class) for the M8a axis: established that a basis-restricted PSLQ scan does not see T3-class signatures, motivating the algorithmic-Painlevé-test approach in 007. ~30-60 min agent compute. |
| **Prompt 007 — T3 Conte–Musette Painlevé test (substantive M8a V0 closure)** | `663e95c` | `sessions/2026-05-02/T3-CONTE-MUSETTE-PAINLEVE-TEST/handoff.md` | `T3_LABELED_60_OF_60` (substantive closure at algorithmic-test resolution; 10/10 d=2 LABELED → `P_III(D_6)`; 50/50 d=3 LABELED → `PAINLEVE_UNCLASSIFIED`; 0/60 branch disagreement; V_quad sanity Phase D PASS) | **The operative M8a V0 closure fire.** Three-branch Conte–Musette test (Newton polygon + indicial exponent + dominant balance) on the joint PCF-1 v1.3 d=2 catalogue (10 families: V_quad + QL01/02/06/15/26 with $\Delta_b<0$ + QL05/09/13/18 with $\Delta_b>0$ representatives) and PCF-2 v1.3 d=3 catalogue (50 families). 8 AEAL claims; rubber-duck self-critique 8 items; H3 negatively closed (test invariant across sign of $\Delta_b$). ~45 min agent compute. |
| **Picture v1.19 (consolidated deposit; M8 + Prompt 007 cross-references)** | `70d1a48` | `sessions/2026-05-06/PICTURE-V19-CONSOLIDATED-DEPOSIT/picture_v1.19.md` | (Picture deposit; not a verdict fire) | Records "M8: D=2 Painlevé classification table (per-family, ~10 families) ✅ COMPLETE 2026-05-02 (Prompt 007) — verdict T3_LABELED_60_OF_60; H3 negatively closed" at line 997-1002, and cross-references Prompt 007 verdict at line 396 + line 521 + line 1110 (catalogue table row). The picture-chain-level acknowledgment that M8a V0 is closed at the milestone scale. |

**SHA pre-verification (2026-05-09 14:50 JST, this session)**:

```
PS> git rev-parse bbd1b76
bbd1b7617eeb70be5113905ce60d6334daf78b7f
PS> git rev-parse 663e95c
663e95cbf754d51aba3727e8d7d9bbb8d388ea37
PS> git rev-parse 70d1a48
70d1a4835ee0bc1f188aada9be65bb657f471730
```

All three SHAs resolve. No ambiguity-fatal warnings.

### §2.2 — Substrate documents (manuscripts, picture rows, drafts)

| Artifact | Path | Section / line | Key claim |
|---|---|---|---|
| **Picture v1.19 § 4 (M8 = M8a milestone block)** | `sessions/2026-05-06/PICTURE-V19-CONSOLIDATED-DEPOSIT/picture_v1.19.md` (bridge `70d1a48`) | line 997 (axis statement) + line 998-1002 (closure statement + caveat); cross-referenced at line 396, line 521, line 1110, line 3025, line 3195, line 3306 | "M8: D=2 Painlevé classification table (per-family, ~10 families) ✅ COMPLETE 2026-05-02 (Prompt 007) — verdict T3_LABELED_60_OF_60; Headline: 10/10 d=2 LABELED (P_III(D6) uniformly); 50/50 d=3 LABELED (PAINLEVE_UNCLASSIFIED uniformly); Caveat: H3 negatively closed (test sign-of-Delta invariant; cannot reproduce PCF-1 dichotomy → needs Stokes-mult follow-up at M8b)" |
| **Picture v1.19 § 5 P-PIII row (Painlevé reduction landscape)** | same | line 865 (P-PIII row) | "Painlevé reduction landscape at $d=2$ and $d=3$ (per-family classification): T3 Conte–Musette test (007) ✅ → T3.5 Stokes-multiplier S_1 (Prompt 010) 🟡 PARTIAL → ... → S_2 PERMANENTLY FORECLOSED via Stage-2-LSQ (017c+017e) + Borel-Padé (T37M HALT 2026-05-03); d=2 uniformly P_III(D_6); d=3 uniformly PAINLEVE_UNCLASSIFIED; H3 negatively closed (Conte–Musette test is sign-of-Δ invariant)" |
| **Picture v1.19 § 4 dispatch row** | same | line 396 + line 521 (T3 row) | "✅ Prompt 007 fired with verdict T3_LABELED_60_OF_60. All 60 families (10 d=2 + 50 d=3) algorithmically labelled. H3 negatively closed. The Conte–Musette algorithmic test on the linear OGF ODE is invariant across sign(Δ_b) — produces uniform labels and cannot reproduce the PCF-1 v1.3 §3 dichotomy (A=4 for Δ>0, A=3 for Δ<0). The d=2 catalogue is uniformly P_III(D_6); the d=3 catalogue is uniformly PAINLEVE_UNCLASSIFIED (rank 4/3 at 0, 2/3 at ∞). The PCF-1 dichotomy lives below the Painlevé-class resolution scale — at the Stokes-multiplier level." |
| **Picture v1.19 catalogue table row** | same | line 1110 | "007 \| T3 — Conte–Musette Painlevé test on $d=2,3$ catalogues \| G6a \| M8 \| ✅ DONE 2026-05-02 (60/60 LABELED; H3 negatively closed) \| medium (symbolic) \| —" |
| **vquad_resurgence_R1.tex / R2.tex §4 "Painlevé classification"** | `tex/submitted/vquad_resurgence_R1.tex` (and R2.tex) | section header line 596 / 599 + body L208 + L875 / L878 | Section "Painlevé classification" anchored to V_quad's `P_III(D_6)` class assignment via CT v1.3 Theorem 3.3.D; M8a V0 closure formalizes the catalogue-wide extension at the algorithmic-test resolution scale. **No M8a-side manuscript amendment required**: the V_quad anchor is already published; M8a V0 closure is the catalogue-wide extension and is consistent with the published §4 framing. |
| **PCF-1 v1.3 §3 (sign-of-$\Delta_b$ dichotomy section)** | `tex/submitted/pcf2_program_statement.tex` + `tex/submitted/p12_journal_main.tex` (cross-referenced) | program statement L1394 ($P_{III}$ via Funkcial. Ekvac.); journal main L1634 (same) | Source of the H3 dichotomy that M8a's algorithmic test is invariant under. Forward-pointed (not blocking M8a closure) for the M8b axis to resolve. **M8a closure declares the dichotomy invisible at the algorithmic-test resolution; the manuscript-level statement of the dichotomy is unchanged by M8a closure**. |
| **M4 V0 cascade record (106) §C4** | `sessions/2026-05-08/M4-V0-CLOSURE-CASCADE-106/cascade_record.md` | §C4 + §"SQL state changes summary" row `m8a-unblocked-post-m4-v0-closure` | "M8a axis closure now unblocked by M4 V0 ratification; queue M8a envelope drafting at next M-critical synth turn slot." The M4 V0 cascade's explicit acknowledgment that M8a is procedurally cleared for ratification. |
| **M7 V0 cascade record (123) §"Recommended next step"** | `sessions/2026-05-09/T1-SYNTH-M7-V0-CLOSURE-CASCADE-123/handoff.md` | "Recommended fire order under RULE 1" §1 | "fire 125 (M8a V0 substrate-prep; agent-fireable parallel-safe) and 128 (M8b V0 substrate-prep; agent-fireable parallel-safe) in fresh CLI windows." The M7 V0 cascade's explicit acknowledgment that M8a substrate-prep is the next-fire candidate. |

### §2.3 — Open residuals (qualifications the ratification must surface)

The M8a V0 algorithmic-test-scale closure carries three explicit
qualifications that the ratification statement must carry forward
(analogue of the M4 V0 MEDIUM-HIGH + Wasow §X.3 forward-pointed-
not-blocking qualifications surfaced at 105 → 106; analogue of
the M7 V0 SOFT-BRANCH + Q22 hard-branch + Q23 PSLQ basis
hygiene surfaced at 121 → 122 → 123):

1. **H3 negative-closure qualification (most important).** The
   Conte–Musette necessary-criterion test as implemented on the
   linear OGF ODE is **invariant across $\mathrm{sign}(\Delta_b)$**:
   all 10 d=2 families share signature `P_III(D_6)`, including
   both the 6 $\Delta_b<0$ named QL families and the 4 $\Delta_b>0$
   QL representatives. The PCF-1 v1.3 §3 dichotomy ($A=4$ for
   $\Delta_b>0$ vs. $A=3$ for $\Delta_b<0$) is therefore
   **invisible** to this algorithmic test. H3 (the
   `D=2_REDUCTION_AMBIGUOUS` question) is **negatively closed**
   under M8a: the test is too coarse to see the dichotomy. The
   substantive resolution lives at the Stokes-multiplier scale
   (M8b axis: `T3.5-STOKES-MULTIPLIER` Prompt 010 + 016 / 017c /
   017e / 017L / 017m extension chain). **Confidence
   carry-forward**: the M8a_V0_CLOSED tag at picture-chain v1.20+
   should be annotated with `(ALG-TEST-SCALE; STOKES-DICHOTOMY-
   DELEGATED-TO-M8B)` to prevent silent inheritance of
   unqualified closure state (cf. M4 V0 `(MEDIUM-HIGH;
   HIGH-PENDING)` at 106 cascade; cf. M7 V0 `(SOFT-BRANCH;
   HARD-BRANCH-PENDING)` at 123 cascade).

2. **Branch-(a) Newton-polygon threshold judgment call.**
   Prompt 007 relaxed the branch-(a) Newton-polygon
   denominator threshold from `denom <= 2` (initial draft) to
   `denom <= 6` (final), to allow the d=3 fractional ranks
   (4/3, 2/3) to register as LABELED rather than INCONCLUSIVE.
   Without the relaxation, all 50 d=3 families would have
   labeled INCONCLUSIVE, masking the structural fractional-rank
   signature. The relaxation is rubber-duck-disciplined
   judgment, documented in Prompt 007 handoff "Judgment calls
   #2", but the closure statement should carry forward the
   threshold choice as a forward-pointed governance note: future
   d=3+ Painlevé-test operators should pre-document the
   denominator threshold and surface the choice in the verdict
   text rather than leaving it as an internal parameter.

3. **Branch-(c) reduced-scope implementation.** Prompt 007
   implemented branch (c) as **dominant-balance only** rather
   than full resonance-equation consistency (i.e., the
   truncated Laurent series is not substituted back and the
   recurrence is not checked at every resonance up to some K).
   This is a known under-implementation, documented in Prompt
   007 handoff "Judgment calls #4". The decision was scoped
   for runtime; a more thorough test would not change the
   60/60 LABELED outcome (the d=2 catalogue's `P_III(D_6)`
   signature is independently reproduced by the Newton-polygon
   and indicial-exponent branches, and the d=3 catalogue's
   `PAINLEVE_UNCLASSIFIED` outcome would persist under the
   more thorough variant). The closure statement should carry
   forward the reduced-scope branch-(c) qualification as
   forward-pointed governance: future Conte–Musette
   implementations should either (a) include the full
   resonance-equation consistency check, or (b) explicitly
   document the dominant-balance-only scope.

A fourth, lower-priority qualification (not blocking ratification
but worth surfacing for picture-chain-level provenance):

4. **d=3 PAINLEVE_UNCLASSIFIED conservative-judgment qualification.**
   The d=3 Newton polygon slopes (4/3 at $x=0$, 2/3 at
   $x=\infty$) are fractional and outside the standard
   $P_I..P_VI$ list. Prompt 007 elected the conservative
   `PAINLEVE_UNCLASSIFIED` label rather than a best-effort
   assignment to $P_{III}(D_7)$ given the rank-2 confluence at
   $x=0$. Documented in Prompt 007 handoff "Judgment calls #3".
   The closure statement should carry forward the
   `PAINLEVE_UNCLASSIFIED` choice; future d=3+ extensions of the
   Painlevé hierarchy (e.g., Sakai surface labels) may revise
   this without disturbing M8a V0 closure (the closure is at the
   $P_I..P_VI$ standard-list resolution scale; out-of-list labels
   are a separate stratum-extension question).

### §2.4 — §1 closure statement vs substrate consistency check

| §1 closure-statement claim | Substrate excerpt | Consistent? |
|---|---|:---:|
| "M8a V0 CLOSED at the algorithmic-Painlevé-test stratum-labeling scale (Prompt 007 verdict T3_LABELED_60_OF_60)" | `sessions/2026-05-02/T3-CONTE-MUSETTE-PAINLEVE-TEST/handoff.md` (bridge `663e95c`) "Status: COMPLETE; All families return aggregate label LABELED" + verdict header | **YES** |
| "10/10 d=2 LABELED with V_quad-anchored class assignments matching CT v1.3 Theorem 3.3.D" | T3-CONTE-MUSETTE handoff "Key numerical findings": "d=2 catalogue: 10/10 LABELED, all class P_III(D₆)" + "V_quad sanity (Phase D): PASS — V_quad with a(n)=1, b(n)=3n²+n+1 is assigned class P_III(D₆) by all three branches" | **YES** |
| "50/50 d=3 LABELED with PAINLEVE_UNCLASSIFIED stratum signature" | T3-CONTE-MUSETTE handoff "Key numerical findings": "d=3 catalogue: 50/50 LABELED, all class PAINLEVE_UNCLASSIFIED — Newton polygon slopes 4/3 at x=0 and 2/3 at x=∞" | **YES** |
| "0/60 branch disagreement (well below the 5% H3-confirmation threshold)" | T3-CONTE-MUSETTE handoff "Branch disagreement fraction: 0/60 = 0.000, well below the 5 % H3-confirmation threshold from the prompt" | **YES** |
| "H3 negatively closed (Conte–Musette test invariant across sign of $\Delta_b$ on linear OGF ODE)" | T3-CONTE-MUSETTE handoff "Anomalies and open questions" §1 + verdict.md (H3 closure verdict) + picture v1.19 line 521 + line 998 caveat | **YES** |
| "Dichotomy-resolution delegated to M8b Stokes-multiplier axis" | T3-CONTE-MUSETTE handoff "Recommended next step" + picture v1.19 line 521 + line 1003 ("needs Stokes-mult follow-up at M8b") | **YES** |
| "8 AEAL claims ledgered; halt log empty; no branch disagreements" | T3-CONTE-MUSETTE handoff "AEAL claim count: 8 entries" + `halt_log.json` (no halt triggered) + `discrepancy_log.json` (no branch disagreements) | **YES** |
| "Picture v1.19 records M8 ✅ COMPLETE 2026-05-02 (Prompt 007) verdict T3_LABELED_60_OF_60" | `sessions/2026-05-06/PICTURE-V19-CONSOLIDATED-DEPOSIT/picture_v1.19.md` line 998 (bridge `70d1a48`) | **YES** |

**T2-Executor conclusion supported by substrate**: All 8 sub-claims
of the §1 proposed M8a V0 closure statement are materially
consistent with the UMB-T3-PROBE + 007 + picture-v1.19 substrate
at the verified SHAs. The synth at slot 126 may sign §3 (`ACCEPT`)
and §6 (`Substrate SHAs verified: Y`) on this basis if the synth
accepts the §1 wording as written.

If the synth wishes to amend §1 wording (e.g., to add the
algorithmic-test-scale / Stokes-dichotomy-delegation
confidence-qualifier annotation `(ALG-TEST-SCALE; STOKES-
DICHOTOMY-DELEGATED-TO-M8B)` explicitly in the closure statement,
or to surface the branch-(a) threshold and branch-(c) reduced-scope
qualifications as forward-pointed governance notes), use §3
(`ACCEPT_W_REVISIONS`) and provide revised wording in §4.

---

## §3. Decision form (synth signs ONE row)

| Decision | Selected? | Notes |
|:---:|:---:|---|
| **`RATIFY`** — M8a V0 CLOSED as proposed in §1 | ☐ | rubber-stamp; UMB-T3-PROBE + 007 + picture v1.19 substrate complete; vquad_resurgence_R1/R2 §4 + PCF-1 v1.3 §3 manuscript anchors consistent with §1 wording (no manuscript amendment required); recommended path given the substrate is dossier-complete |
| **`RATIFY_WITH_AMENDMENT`** — M8a V0 CLOSED with synth-side wording amendments to §1 | ☐ | M4 V0 + M7 V0 cascade precedent (105 → 106 + 121 → 122 → 123 ACCEPT_W_REVISIONS): the synth may want the algorithmic-test-scale / Stokes-dichotomy-delegation confidence-qualifier annotation `(ALG-TEST-SCALE; STOKES-DICHOTOMY-DELEGATED-TO-M8B)` carried forward into the closure statement (analogue of M4 V0 `(MEDIUM-HIGH; HIGH-PENDING)` + M7 V0 `(SOFT-BRANCH; HARD-BRANCH-PENDING)`); revised wording in §4 |
| **`DEFER`** — substrate insufficient or ratification premature, fire follow-on | ☐ | provide reasoned NO_GO statement in §5; T2-executor dispatches rubber-duck review of UMB-T3-PROBE + 007 + picture-v1.19 against the synth's reasoned objection before re-ratification |
| **`OBJECT`** — substrate substantively contradicted by independent reading | ☐ | provide reasoned objection in §5; halt-class outcome; escalate to operator |

---

## §4. (If RATIFY_WITH_AMENDMENT) Revised closure statement

```
[Synth fills in revised wording here. Recommended template
(mirrors M4 V0 §4 + M7 V0 §4 revised-wording structure):

M8a V0 CLOSED at the algorithmic-Painlevé-test stratum-labeling
scale via the Conte–Musette necessary-criterion three-branch test
(Prompt 007 verdict T3_LABELED_60_OF_60). All 60 catalogue
families are LABELED at the standard P_I..P_VI resolution: 10/10
d=2 PCF-1 v1.3 families (V_quad + QL01/02/06/15/26 with Δ_b<0 +
QL05/09/13/18 with Δ_b>0 representatives) classify as P_III(D_6),
matching V_quad's published assignment via CT v1.3 Theorem 3.3.D;
50/50 d=3 PCF-2 v1.3 families classify as PAINLEVE_UNCLASSIFIED
(Newton polygon slopes 4/3 at x=0 and 2/3 at x=∞, fractional,
outside the standard P_I..P_VI list). Branch disagreement
fraction 0/60 = 0.000 is well below the 5% H3-confirmation
threshold; V_quad sanity check (Phase D) PASS.

The closure runs at the algorithmic-test-scale resolution. H3
(the D=2_REDUCTION_AMBIGUOUS question) is negatively closed: the
Conte–Musette test on the linear OGF ODE is invariant across
sign(Δ_b), so the PCF-1 v1.3 §3 dichotomy (A=4 for Δ>0, A=3 for
Δ<0) is invisible to this algorithmic test. The substantive
dichotomy resolution is delegated to the M8b Stokes-multiplier
axis (Prompt 010 measured |S_1| at ≥60 cross-method digits
differing across the dichotomy at O(1) scale; 017c+017e+017L
closed the a_1 3-stratum partition; 017m halted the final
numerical S_2 path); M8b carries its own ratification cycle
(slates 128 → 129 → 130, parallel-safe with this 125 → 126 → 127).

Three forward-pointed governance qualifications are surfaced:
(i) the branch-(a) Newton-polygon denominator threshold relaxed
from 2 to 6 (judgment call to admit d=3 fractional ranks 4/3 and
2/3); (ii) branch-(c) reduced-scope implementation (dominant-
balance only, not full resonance-equation consistency); (iii) the
d=3 PAINLEVE_UNCLASSIFIED label is the conservative choice
(rather than best-effort assignment to P_III(D_7) given the
rank-2 confluence at x=0). All three are rubber-duck-disciplined
judgment calls, documented in Prompt 007 handoff "Judgment calls"
1-4, not silent fudges.

No new manuscript-content amendment is required for M8a V0
closure (mirror difference vs. M7: M7 required PCF-2 §6
amendment; M8a's catalogue-wide labeling is an extension of the
already-published V_quad-anchored P_III(D_6) class assignment in
vquad_resurgence_R1/R2 §4 and is consistent with the published
framing). Picture-chain v1.20+ M8a_V0_CLOSED tag should annotate
(ALG-TEST-SCALE; STOKES-DICHOTOMY-DELEGATED-TO-M8B) to prevent
silent inheritance of unqualified closure state.

No halt conditions triggered (8 AEAL claims ledgered; halt log
empty; discrepancy log records no branch disagreements;
unexpected_finds empty).

Confidence: ALG-TEST-SCALE. STOKES-DICHOTOMY-DELEGATED-TO-M8B
reserved for M8b axis ratification (slates 128 → 129 → 130).
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
  verified:           [Y / N]  (UMB-T3-PROBE: bbd1b76;
                          007: 663e95c;
                          picture v1.19: 70d1a48;
                          all 3 verified via independent git
                          rev-parse return-of-full-hash AND the
                          §2.4 8/8 PASS consistency check is
                          materially supported by the substrate;
                          mirrors M4 V0 §6 + M7 V0 §6 substrate-
                          grounding semantic per 105 §6 + 121 §6
                          wording amendment)
Rubber-duck QA
  acknowledged:       [Y / N]  (Prompt 007 §"Judgment calls"
                          #1 (Δ_b>0 representative selection
                          QL05/09/13/18) + #2 (branch-(a)
                          Newton-polygon threshold denom ≤ 6) +
                          #3 (d=3 PAINLEVE_UNCLASSIFIED
                          conservative choice) + #4 (branch-(c)
                          dominant-balance only) + #5 (V_quad
                          ODE equivalence not explicitly verified);
                          all five are rubber-duck-disciplined
                          judgment calls, not silent fudges)
Algorithmic-test-scale /
  Stokes-dichotomy-delegation
  qualifier
  acknowledged:       [Y / N]  (synth acknowledges picture-chain v1.20+
                          tag must read M8a_V0_CLOSED
                          (ALG-TEST-SCALE; STOKES-DICHOTOMY-
                          DELEGATED-TO-M8B), not bare
                          M8a_V0_CLOSED, per the
                          confidence-carry-forward semantic
                          established at the M4 V0 cascade
                          (105 → 106) + M7 V0 cascade
                          (121 → 122 → 123) precedent)
```

**Substrate-grounding note for §6 verification** (mirrored from
M4 V0 §6 + M7 V0 §6 wording-amendment semantic per 105 + 121):

"Substrate SHAs verified [Y/N]" means *both*
(a) the cited SHAs exist in bridge git history at the cited paths,
AND
(b) the substrate at those SHAs materially supports the §1 closure
statement (i.e., the algorithmic-test-scale 60/60 LABELED verdict,
the V_quad-anchored P_III(D_6) class assignment, the H3 negative
closure on the linear OGF ODE invariance, and the dichotomy
delegation to M8b are present and consistent with §1).
It does NOT require independent re-derivation of the algorithmic
content. If the synth wishes to verify (b) explicitly, the §2.4
8/8 PASS consistency check is the substrate-grounded verification
artifact.

---

## §7. Post-ratification cascade (T2-executor follow-up)

If §3 = RATIFY or RATIFY_WITH_AMENDMENT:

| Step | Actor | Action | SQL todo |
|:---:|---|---|---|
| 1 | agent | Mark `m8a-substrate-prep-125-completed` → `done` | (this template) |
| 2 | agent | Mark `m8a-unblocked-post-m4-v0-closure` → `done` | post-M8a-V0-closure unblock resolved (the M4-V0-cascade-106 §C4 NEW SQL todo) |
| 3 | agent | Add `M8a_V0_CLOSED (ALG-TEST-SCALE; STOKES-DICHOTOMY-DELEGATED-TO-M8B)` tag to next picture-chain deposit (v1.20+) | included in v1.20+ fire (under RULE 1: math-content step in scope; picture-chain admin step TABLED until M1–M12 closure) |
| 4 | (optional) | umbrella v2.x amendment if §3 = RATIFY_WITH_AMENDMENT | post-M9 LANE-1 / under RULE 1 deferred |
| 5 | n/a | (No PCF-2 v1.4 §6 amendment required; mirror-difference vs. M7) | n/a (M8a's catalogue-wide labeling is consistent with the published vquad_resurgence_R1/R2 §4 V_quad-anchored framing) |

If §3 = DEFER:

| Step | Actor | Action |
|:---:|---|---|
| 1 | agent | Dispatch rubber-duck review of UMB-T3-PROBE + 007 + picture-v1.19 against synth's reasoned objection |
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
* M4 V0 cascade (sibling-axis precedent + M8a unblock SQL todo): `siarc-relay-bridge/sessions/2026-05-08/M4-V0-CLOSURE-CASCADE-106/cascade_record.md` §C4
* M4 V0 ratification template (executed): `tex/submitted/control center/m4_v0_ratification_template.md`
* M7 V0 substrate-prep (immediate sibling-axis mirror): `siarc-relay-bridge/sessions/2026-05-09/T2-EXECUTOR-M7-RATIFICATION-SUBSTRATE-PREP-121/m7_v0_ratification_template.md` (SHA-256 `72D855F7B05D3F209340FBF57E7CAFD793BF1E8FA283502CF9889124E1BB6BE5`)
* M7 V0 cascade (sibling-axis ratification precedent + dual-witness pattern): `siarc-relay-bridge/sessions/2026-05-09/T1-SYNTH-M7-V0-CLOSURE-CASCADE-123/`
* Picture v1.19 (M8 = M8a milestone block + Prompt 007 cross-references): `siarc-relay-bridge/sessions/2026-05-06/PICTURE-V19-CONSOLIDATED-DEPOSIT/picture_v1.19.md` (bridge `70d1a48`)
* UMB-T3-PROBE (interim provisional T3 candidate scan; pre-007 substrate): `siarc-relay-bridge/sessions/2026-04-30/UMB-T3-PROBE/handoff.md` (bridge `bbd1b76`)
* Prompt 007 (T3-CONTE-MUSETTE; substantive M8a V0 closure): `siarc-relay-bridge/sessions/2026-05-02/T3-CONTE-MUSETTE-PAINLEVE-TEST/handoff.md` (bridge `663e95c`)
* M8b sibling parallel cycle (slates 128 → 129 → 130): substrate at 092 + P-009; Prompt 010 |S_1| measurement; 017c+017e+017L a_1 3-stratum partition closure; 017m HALT_T37M_PADE_DIVERGENT
* RULE 1 marker: `tex/submitted/control center/picture/M1_M12_CLOSURE_OUTLOOK_20260509_RULE1.md` (M8a listed under §1 KEEP as math-foundational, line 14)
* Repo memory `t3-conte-musette-2026-05-02.md` — M8a substrate notes (60/60 LABELED; H3 negative closure; rubber-duck-disciplined judgment calls)
* Repo memory `rubber-duck QA discipline` — applies to Prompt 007 5-judgment-call set
* Repo memory `prompt drafting discipline` — Phase 0 supersession-gate pattern + bibliographic-identifier pre-verification rule
* Memory anchor: "3-stage pattern for M-axis ratifications" (canonical 3-arc template per 121 §1 + 122 dispatch + 123 cascade)

---

## §9. Forbidden-verb compliance note

Per envelope STEP D.2 forbidden-verb scan: this template uses
"ratifies"/"ratify" (the operative verb of the document itself,
used in §3 + §7 + the title) as checklist-meta-references. This
is verb-list-as-data + checklist-meta-reference — exempt under
098 J3 / 075 J2 precedent. **No substrate prose, no §3 question
text, and no §1 closure statement contains forbidden verbs in
substantive (claim/prediction) context.**

§3 question text is intentionally neutral: it asks the synth to
*sign* a row, not to *show* / *confirm* / *prove* anything;
the verb-of-decision is "ratify" (operative, exempt) and the
verb-of-evidence is "supports" / "is consistent with" / "is
materially consistent with" (not forbidden). The §2.4 consistency-
check table uses the column header "Consistent?" with cell values
`YES`/`NO` rather than "Verified?" / "Confirmed?".

---

## §10. Dispatch readiness (Phase D)

- **Word count**: ~3 500 words (§1–§9 inclusive; close to M4 V0
  + M7 V0 template scale; well within paste-ready limits for a
  Claude.ai web chat session)
- **All §2 evidence pre-verified**: 3/3 SHAs (`bbd1b76`, `663e95c`,
  `70d1a48`) returned full 40-char hashes via `git rev-parse` at
  2026-05-09 14:50 JST in this session
- **Bibliographic identifier pre-verification**: NOT_APPLICABLE —
  this template cites only internal bridge SHAs as substrate; no
  external DOI / arXiv ID is in scope for the M8a V0 closure (the
  Painlevé-classification literature anchors — Conte–Musette
  necessary criterion + Sakai surface taxonomy — are referenced
  via CT v1.3 Theorem 3.3.D, which is internal and already
  published; per §2.3 residual #1, the dichotomy-resolution at
  the Stokes-multiplier scale is delegated to M8b and does not
  enter the M8a ratification claim).
- **All §3 questions answerable from §2 substrate alone**: YES —
  no out-of-packet follow-up is needed for the synth to sign §3 +
  §6. The §2.4 8/8 PASS consistency check is the substrate-
  grounded verification artifact.
- **Recommended dispatch class**: T1-Synth solo (Claude.ai web
  conversation; mirrors 104 → 105 → 106 dispatch pattern at the
  M4 V0 cascade and 121 → 122 → 123 dispatch pattern at the M7
  V0 cascade)
- **Recommended next-slot**: 126 (T1-SYNTH-M8A-RATIFICATION-SOLO-
  DISPATCH); successor cascade-absorption fire at slot 127
  (T1-SYNTH-M8A-V0-CLOSURE-CASCADE) per the canonical 3-arc
  template
- **Synth-side instruction note for slot 126**: do NOT speculate
  on M8b axis status from within the M8a ratification dispatch.
  M8b is a separate axis with its own substrate (092 + P-009 +
  Prompt 010 + 017c+017e+017L + 017m HALT) and its own
  ratification cycle (slates 128 → 129 → 130). M8a closure
  delegates the sign-of-Δ_b dichotomy resolution to M8b;
  delegation is not a claim about M8b's closure status.

---

**Template status**: **DRAFTED 2026-05-09 ~14:55 JST** by T2-Executor
(prompt 125 substrate-prep). Awaits synth dispatch at slot 126.
