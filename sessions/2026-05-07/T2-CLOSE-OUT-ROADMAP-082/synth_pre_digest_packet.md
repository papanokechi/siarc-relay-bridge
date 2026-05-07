# BUCKET-C synth pre-digest packet — W21 LANE-1 Mon AM JST input substrate

**Purpose**: synth Mon AM JST absorbs ~34 arbitrations as one packet rather than
reading individual SQL rows; LANE-1 throughput accelerator.

**Substrate**: `bucket_classification.md` Section C clusters C.1-C.6; plan.md
M1-M12 close-out section.

**Cross-references** to 080 cross-coupling matrix (`sessions/2026-05-07/T2-LANE1-CROSS-DOSSIER-COUPLING-ANALYSIS-080/`,
landed at bridge `9745b78`) noted per item where applicable.

---

## Cluster C.1 — W21 LANE-1 ratifications + DEFER + HOLD pickups (5 items)

These are the canonical W21 LANE-1 quintet from 080 5x5 coupling matrix.

### C.1.a — w21-lane1-ratify-068-m4-closure
- **Synth question**: RATIFY 068 verdict UPGRADE_FULL_VIA_DEG_A_ZERO_ROW at
  MEDIUM-HIGH→HIGH confidence; close M4 P-B4 PROVEN-at-d≥3 status.
- **Menu options** (per 068 handoff §"Recommended next step"):
  - ACCEPT (HIGH confidence + M4 closed at full status)
  - ACCEPT_WITH_REVISIONS (issue list for follow-up relay)
  - REVISE (verdict downgrade)
  - DEFER (W22 LANE-1)
  - OBJECT (074R amendment)
- **Substrate anchor**: bridge `e7bfe49` 068 handoff L28-32, L84-88 (T1-PHASE-3-COSTIN-BORDERLINE-M4-CLOSURE-068);
  Q1 + Q2 surfaced for synthesizer review per L85-88.
- **Gating relationship**: M9 SIARC-MASTER-V0 announcement gating remains open
  until ratified per 047 verdict.
- **080 coupling cell**: L1 (M4 ratification dossier).

### C.1.b — w21-lane1-ratify-069-m6cc-d2-persist
- **Synth question**: RATIFY 069 verdict UPGRADE_V1_0_PARTIAL_NUMERICAL_PERSIST
  after HALT_069_GAUGE_TRANSFORM_FAILURE fired at sub-step b (gauge transformation)
  blocked by R1 carry-forward (CT v1.3 §3.5 four-tuple → KNY (a_0, a_1, a_2)
  chart unreduced).
- **Menu options**:
  - (a) PERSIST verdict honesty + 4-item over-claim checklist re-selection PASS
  - (b) R1-closure preflight scope split (path α additional shift in (a_0, a_1, a_2)
    chart vs path β Okamoto §3 τ-function reparametrisation)
  - (c) BL2024 §4 connection-matrix path exhausted vs alternative numerical-cross-check
- **Substrate anchor**: bridge `05810a2` 069 handoff (CC-VQUAD-PIII-NORMALIZATION-MAP-PHASE-D-NUMERICAL).
- **Gating relationship**: 069r1 dispatch authorization gated until ratified;
  per 047 verdict M6.CC closure remains 🟡 PARTIAL.
- **080 coupling cell**: L2 (M6.CC chart-map B1 check; 075 STRUCTURAL_MISMATCH).

### C.1.c — w21-lane1-oq-061-d-pcf1-v_quad-errata
- **Synth question**: OQ-061-D — does V_quad upper-branch reinterpretation
  (A=4 = deg_a=0 row, NOT borderline) require formal errata to PCF-1 v1.3?
- **Menu options**:
  - errata required (Zenodo amendment)
  - errata not required (deposit-time-snapshot pinned; follow-up note suffices)
  - couple with Item 3 follow-up note authoring task
- **Substrate anchor**: LANE-2 handoff §Open questions OQ-061-D; V5 + P3 + U1
  (load-bearing per 067 BT-BASELINE-NOTE-FOLLOWUP-V1-0).
- **Gating relationship**: out-of-LANE-2 scope; surfaced for LANE-1 weekly
  arbitration at W21 cadence.
- **080 coupling cell**: L4 (endorser-framing dossier; relates to PCF-1 record #2 framing).

### C.1.d — w21-lane1-item6-pcf2-v3x-wording-revision
- **Synth question**: Item 6 HOLD — PCF-2 v3.x Zenodo amendment for S3 wording.
- **Menu options**:
  - (a) Zenodo amendment narrowing S3 deg_a in {0,1} setup to match S6 B4 verbatim
    "PCF (1, b)" notation
  - (b) hold pending more substrate
- **Substrate anchor**: LANE-2 OQ-061-B; U3 finding identifies S3 narrowing
  (NOT S6 expansion) as correct revision direction.
- **Gating relationship**: coupled to Item 4 rule5 vocab (C.1.e) and U3
  (PCF-2 v3.x S3 narrowing target).
- **080 coupling cell**: cross-cuts L1+L4.

### C.1.e — w21-lane1-item4-rule5-vocab-fold-in
- **Synth question**: Item 4 DEFER_TO_W21 — rule5 vocabulary fold-in for
  protocol-to-stratum mismatch.
- **Menu options**:
  - (a) fold into rule5 standing vocabulary
  - (b) keep as case-specific term
  - (c) reject
- **Substrate anchor**: LANE-2 OQ-061-A; per LANE-2 R2 the actual mismatch
  locus is INTRA-document (not "prose vs scripts").
- **Gating relationship**: coupled to Item 6 (C.1.d) and w20-lane2-r2-intra-document-mismatch-wording (C.6).

---

## Cluster C.2 — Q-series arbitrations Q20-Q34 (10 items)

### C.2.a — q20-conj33a-proof-upgrade-claude-arbitrate
- **Synth question**: Q20 — does the operator-level Newton-polygon characteristic-root
  argument (depending only on alpha_3) constitute a proof of Conj 3.3.A* modulo
  standard Newton-polygon / irregular-singular-point theorems?
- **Menu options**: yes (upgrade D2-NOTE Conj 3.3.A* d=3 DEFERRED→PROVEN, d=4
  EMPIRICAL→PROVEN, general-d CONJECTURED→PROVEN) / no (leave at EMPIRICAL).
- **Substrate anchor**: Prompt 012 + sessions/2026-05-02/XI0-D3-DIRECT/handoff.md (W1 finding).

### C.2.b — q21-013-refire-path-arbitrate
- **Synth question**: Q21 — operator + Claude pick 013 refire path.
- **Menu options** (paraphrased from SQL row description):
  - (a) full G15 — R5 acquisition → Prompt 015 G15 full closure → 013 refired
    with numerical 30-digit gate; stronger result
  - (b) symbolic-only PARTIAL — 013 reformulates to accept G15_PARTIAL with
    symbolic-only Borel sum modulo R2-R5; ships immediately
- **Substrate anchor**: sessions/2026-05-02/CC-FORMAL-BOREL-CLOSE/handoff.md
  §"What would have been asked".

### C.2.c — q22-014-stretch-goal-arbitrate
- **Synth question**: Q22 — 014 closure-threshold acceptance for PCF-2 v1.4
  deposit gating.
- **Menu options**:
  - (a) deposit `pcf2_v1.4_amendment.md` to Zenodo now (`|delta_lin|~1e-23` +
    no-CS-relation in H6 B19+ formally close G5+G16)
  - (b) fire 014b at K_FIT=9 with extended y_n at N up to 2400, dps≥44300
    (stretch goal `|delta|<1e-30` first)
- **Substrate anchor**: sessions/2026-05-02/T25D-RETRY-13PARAM/handoff.md.
- **Gating relationship**: M2 v1.4 deposit downstream per plan.md L77-L86;
  blocked SQL row pcf2-v1-4-deposit-decision-q22-gated awaits this verdict.

### C.2.d — q23-pslq-basis-hygiene-claude-arbitrate
- **Synth question**: Q23 — PSLQ basis hygiene rule for deep-WKB closures
  (codification candidate).
- **Menu options**: codify rule (pre-screen for Q-linear dependencies + emit
  deduplicated minimal basis) / case-specific only.
- **Substrate anchor**: T25D-RETRY-13PARAM handoff (literal 18-member B19+
  contained both `sqrt(3)` and `Gamma(1/3)Gamma(2/3)/(2*pi)` Q-equivalent).

### C.2.e — q24-d2-polynomial-correction-discrimination-claude-arbitrate
- **Synth question**: Q24 — does some invariant of polynomial corrections
  `(a_1, ..., a_K)` partition by Δ_b sign at d=2 at higher precision?
- **Menu options**: a_1 partitions / a_1/C ratio partitions / other invariant
  partitions / no clean partition (S_2 escalates to G6b_HARD).
- **Substrate anchor**: Prompt 016 HALT note; T36 measured a_1 to ~3-4 digits per rep.

### C.2.f — q32-h1-rearbitration-timing
- **Synth question**: Q32 — H1 re-arbitration timing.
- **Menu options**: post-Phase-2 verdict resolves to PROVEN / HEURISTIC / SPLIT.
- **Substrate anchor**: tied to h1-label-arbitration C.2.j.

### C.2.g — q33-pslq-basis-hygiene-s2-foreclosure
- **Synth question**: Q33 — PSLQ basis hygiene + S_2 foreclosure methodology
  declaration.
- **Menu options**: methodology declaration (audit-trail records what for
  permanent S_2 numerical foreclosure post-017m HALT).
- **Substrate anchor**: 017m HALT.

### C.2.h — q34-ct14-section-3-5-amend-timing
- **Synth question**: Q34 — when to amend CT v1.4 §3.5 to numerically-confirmed-at-108-digits
  (V_quad native; G22 residual flagged).
- **Menu options**: amend now / amend post-G22 closure / amend post-M6.CC closure / hold.
- **Substrate anchor**: §3.5 epistemic upgrade timing.

### C.2.i — h1-label-arbitration
- **Synth question**: arbitrate Theory-Fleet H1 label downgrade (HIGH).
- **Menu options**:
  - PROVEN (literature-proven; current label B4_PROVED_AT_d>=3)
  - HEURISTIC (downgrade per T1 reading flag)
  - SPLIT (proven for some d, heuristic for others)
- **Substrate anchor**: T1 Phase 1 action item A-02 / D-04;
  sessions/2026-05-02/T1-BIRKHOFF-TRJITZINSKY-LITREVIEW/handoff.md.
- **Gating relationship**: ties to umbrella v2.0 main.tex L295 phrasing
  disposition (currently blocked SQL row; depends on this Q).

### C.2.j — (placeholder; q-claude-30-31-send-d2-note-v21 listed under BUCKET-B)

---

## Cluster C.3 — q038 arbitrations A + C (2 items)

### C.3.a — q038-a-bibliographic-preverification-rule-scope
- **Synth question**: arbitrate Q-038-A/B — extend Bibliographic Pre-Verification
  rule to cover author-and-year-only references + rename-drift HALT loosening.
- **Menu options**:
  - Q-038-A: loosen §1 HALT_038_MISSING_ANCHOR to HALT_ON_CONTENT_MISMATCH
  - Q-038-B: extend post-031 rule to require canonical-ID pinning by prompt-drafter
    for ALL literature candidates (not just specific-ID candidate references)
- **Substrate anchor**: bridge sessions/2026-05-04/MILESTONE-RESIDUAL-GAP-SURVEY-M4-M7-M8B-M9/discrepancy_log.json
  DISC-038-1, DISC-038-2; unexpected_finds.json UF-038-1, UF-038-4.

### C.3.b — q038-c-partial-status-acceptance
- **Synth question**: accept or reject 038 dossier PARTIAL status (Q-038-C).
- **Menu options**:
  - accept (dossier feeds Q-CLAUDE-X scheduling; no follow-on)
  - reject (follow-on full-acquisition lit-hunt prompt fires)
- **Substrate anchor**: 038 dossier handoff; researcher under-spent ~3-4 hr
  budget at ~45 min in favour of on-disk corpus reuse.

---

## Cluster C.4 — Resubmit-target picks (4 items)

| id | paper | candidate venues (substrate-anchored only) | rejection event |
|---|---|---|---|
| painleve3d6-vquad-resurgence-resubmit-target-decision | Item 11 (Painlevé III(D6) / vquad resurgence) | Letters in Mathematical Physics / Communications in Mathematical Physics / IMRN / J. Phys. A / Constructive Approximation / Comptes Rendus | Nonlinearity 2026-04-29 desk-reject (Helen Davis EiC office; no math feedback; Sub ID NON-110708; 8-day turnaround) |
| psl2z-4tier-resubmit-target-decision | Item 14 (PSL2(Z) 4-Tier Obstruction) | IMRN / Mathematical Research Letters / Selecta Mathematica / Trans AMS / J Number Theory / Math Z / Bull LMS | Ramanujan Journal 2026-04-29 desk-reject (no reviewer comments; Sub ID 5448b2ad); avoid AMU Poznań ecosystem per pattern |
| ratio-universality-meinardus-g01-resubmit-target-decision | Item 17 (Ratio Universality / Meinardus / G-01) | JNT / IJNT / Acta Math Hungarica / Trans AMS / Bull LMS / Adv Math / Math Z / Israel J Math | Acta Arithmetica 2026-05-04 desk-reject (Secretary Radziejewski; AMU Poznań; backlog cited; 10-day turnaround); 3rd backlog desk-reject of round; 2nd AMU Poznań ecosystem rejection |
| stieltjes-pcf-resubmit-target-decision | Item 25 (Stieltjes Characterization of Integer PCFs) | Constructive Approximation / J. Approximation Theory / J. Math. Analysis Appl. / Acta Sci. Math. (Szeged) / Hungarian J Math / Indagationes Math. | Aequationes Mathematicae 2026-05-02 desk-reject (Managing Editor Attila Gilanyi; backlog; 3-day turnaround) |

**Cluster gating**: pcf1-meinardus-ramanujan-portfolio-collision-arbitration (C.6)
gates whether Item 17 → Ramanujan Journal collision is allowed.

---

## Cluster C.5 — Lean-relaunch venue pick (1 item)

### C.5.a — lean4-cnp-tunnell-venue-pivot-post-jadvres
- **Synth question**: pick relaunch venue for Lean 4 CNP/Tunnell formalization
  paper after AFM Episciences desk-reject 2026-05-07 (8-min turnaround;
  editorial-board-only; no review).
- **Menu options** (7-option from 079 dossier; alphabetical per 079 envelope
  discipline; no agent-side venue selection):
  - LMCS (Logical Methods in Computer Science) — diamond OA, free APC,
    CS-strict-rigor
  - JFR (Journal of Formalized Reasoning) — diamond OA, free APC,
    formalization specialty
  - MCS (Mathematics in Computer Science) — Birkhauser, math+CS bridge,
    paid OA
  - TCS (Theoretical Computer Science) — Elsevier hybrid, broader scope
  - WAIT_FOR_TIER2_CONFIRM (extra Tier-2 check before pick)
  - DEFER (W22 LANE-1)
  - OBJECT (079R amendment)
- **Substrate anchor**: bridge `72f9850` (079 §F.E `w21_lane1_lean_relaunch_decision_packet.md`).
- **Gating relationship**: post-pick, 089 envelope per plan.md L203 drafts the
  venue-specific submission package.
- **080 coupling cell**: L5 (Lean relaunch venue-fit dossier).

---

## Cluster C.6 — Other arbitrations (12 items)

### C.6.a — ct-v14-sec35-reading-decision
- **Synth question**: Reading A vs Reading B for CT v1.4 §3.5 G17 amendment.
- **Menu options**:
  - Reading A — apply patch as drafted at §3.5 (locked WKB exponent identity location)
  - Reading B — re-fire 026 with explicit §3.3 (V_quad CC algebraic-identity theorem) mandate
- **Substrate anchor**: 026 verdict UPGRADE_CTV14_SEC35_PATCH_PARTIAL_SECTION_NUMBERING_AMBIGUITY.

### C.6.b — g17-layer-separation-amend-ct14
- **Synth question**: should CT v1.4 amend §3.5 to spell out L-equation vs
  isomonodromic-deformation layer separation?
- **Menu options**: amend (CT v1.4 amendment candidate) / hold.
- **Substrate anchor**: sessions/2026-05-02/VQUAD-PIII-NORMALIZATION-MAP/handoff.md.

### C.6.c — g19-betaR-zero-d2-formalize
- **Synth question**: β_R=0 universal at d=2 — synthesizer formalization;
  structural consequence of P_III(D_6) class or coincidental at d=2?
- **Menu options**: structural (predict β_R nontrivial at d=3) / coincidental
  (no d=3 prediction).
- **Substrate anchor**: Prompt 010 PARTIAL + Prompt 016 HALT (sharpened to
  leading-Gamma-shift = 0 universal at d=2; polynomial corrections family-specific).

### C.6.d — m4-fractional-rank-borderline-anormal-gap-implication
- **Synth question**: M4 scheduling decision given UF-038-2 (fractional-rank q≥2
  borderline-anormal STRUCTURALLY ABSENT from Costin 2008 ch.5).
- **Menu options**:
  - (a) prioritize Wasow OCR retry
  - (b) commit to SIARC primary derivation track
  - (c) defer M4 indefinitely
  - (d) commission deeper-than-Costin lit-hunt (Loday-Richaud 2014 LNM 2154 / Iwaki et al / Mazzocco fractional-rank)
- **Substrate anchor**: 038 dossier UF-038-2.

### C.6.e — m4-m7-m8b-followon-lit-hunt-prompt-spec
- **Synth question**: follow-on lit-hunt envelope scope with operator-side ILL or
  browser-driver-mediated OA acquisition for full PDFs.
- **Menu options**: fire follow-on / defer / amend acquisition method.
- **Gating relationship**: gated on Q-038-B rule clarification (C.3.a).
- **Substrate anchor**: 038 dossier UF-038 / handoff §Anomalies §5.

### C.6.f — pcf1-meinardus-ramanujan-portfolio-collision-arbitration
- **Synth question**: PCF-1 + Item 17 dual-Ramanujan portfolio collision
  arbitration.
- **Menu options**:
  - (1) PCF-1 first → RJ + Item 17 → other
  - (2) Item 17 first → RJ + PCF-1 → other (re-litigates 19:11 JST close-out)
  - (3) sequential PCF-1 then Item 17 (~3d turnaround makes this viable)
  - (4) parallel both (anti-pattern; default-rejected)
- **Substrate anchor**: sessions/2026-05-04/SYNTHESIZER-Q38-AND-RAMANUJAN-VERIFY-ABSORB/portfolio_collision_flag.md.

### C.6.g — prompt-017g-amend
- **Synth question**: amend 017g gate set OR retire.
- **Menu options**:
  - (a) amend gate set to recognize T37_K_SENSITIVITY_DIVERGENT / T37_D_CONSISTENT_WITH_ZERO / T37E_PARTIAL_a_1_NULL_AT_HIGHER_PRECISION as alternate fire conditions
  - (b) retire 017g (route beta_2 question through 017m direct Borel-Padé extension)
- **Substrate anchor**: 017g HALT.

### C.6.h — sop-wording-availability-not-fire-authorization-candidate
- **Synth question**: standing-instructions append meta-rule — wording-availability ≠
  fire-authorization codification.
- **Menu options**: append / hold.
- **Substrate anchor**: synthesizer arbitration 2026-05-04 ~17:26 JST.

### C.6.i — synth-review-048R-5-day-early-refire-flag
- **Synth question**: T1 Synth review of 048R 5-day-early fire (W19-closing
  re-fire occurred 2026-05-06 Wed instead of scheduled 2026-05-11 Sun).
- **Menu options**:
  - (a) accept 048R as canonical W19 closing despite early-fire
  - (b) require 2026-05-10 addendum re-fire
  - (c) amend 048 prompt-spec to add early-fire branch contingency
- **Substrate anchor**: bridge `6bbd3f0` 048R handoff Anomalies; 056 substrate at
  sessions/2026-05-06/048R-EARLY-FIRE-DECISION-SUBSTRATE/.

### C.6.j — w20-lane2-r2-intra-document-mismatch-wording
- **Synth question**: revise mismatch-locus wording from "prose vs scripts" to
  "intra-document".
- **Menu options**: adopt / keep current.
- **Substrate anchor**: LANE-2 P4 finding (bridge `dee3c01`); coupled to U3
  (C.1.d Item 6) and Item 4 rule5-vocab (C.1.e).

### C.6.k — w20-synth-058-halt-name-prefix-convention
- **Synth question**: pin halt-name shorthand-vs-prefix convention.
- **Menu options**:
  - (a) future wrappers use exact halt names from spec verbatim
  - (b) HALT_NNN_HALT_NAME_DRIFT gate added to wrapper template
  - (c) status quo (executer leniency)
- **Substrate anchor**: 058 halt anomaly D3.

### C.6.l — w20-synth-arbitration-n3-coincidence
- **Synth question**: do (8,-4,0,7,4) ratio 8/49 and (-9,0,0,10,5) ratio -9/100,
  both yielding `L=3/log(2)`, share a structural identity?
- **Menu options** (substrate-anchored from N3-FOURTH-LAW-ARBITRATION-SUBSTRATE
  hypothesis catalogue):
  - H_BSW (Brouncker-Stieltjes-Wallis triangle extension)
  - H_BFP (Bauer-Forrester pencil at b1 ≠ ±6k)
  - H_C (new 4th-law family for v3.x)
  - coincidence (3/log(2) is small enough to be an attractor)
- **Substrate anchor**: bridge `fe15737` verdict.md + handoff.md + 044B verdict;
  sessions/2026-05-06/N3-FOURTH-LAW-ARBITRATION-SUBSTRATE/ (4 substrate documents
  35780 B; H_BSW + H_BFP + H_C unranked per HALT_055_RANK_DRIFT).

### C.6.m — w20-synth-arbitration-v3-1-wording-softening
- **Synth question**: T2B v3.1 b7-singular wording softening — does this require
  v3.2 amendment release on Zenodo or wait for v4.0?
- **Menu options**: v3.2 amendment now / wait for v4.0.
- **Substrate anchor**: bridge `fe15737` + 044B verdict; cli_log/2026-W21_wsb.md
  A.3 carry-forward.

---

## Synth absorption summary

| cluster | items | primary anchor |
|---|---|---|
| C.1 W21 LANE-1 ratifications | 5 | 080 coupling matrix (`9745b78`) |
| C.2 Q-series Q20-Q34 | 10 (C.2.a-i + C.2.j placeholder) | various T25D / 012 / 016 / 017 substrates |
| C.3 q038 arbitrations | 2 | 038 dossier handoff |
| C.4 resubmit-target picks | 4 | per-paper desk-reject events |
| C.5 Lean venue pick | 1 | 079 dossier (`72f9850`) |
| C.6 other arbitrations | 12 | various |
| **total** | **34** | |

**LANE-1 timing recommendation**: synth absorbs C.1 + C.5 + C.4 first (highest-leverage
6+4=10 items unlock M4/M6.CC/M10/M12 close-out), then C.2 Q-series (10), then C.3
q038 (2), then C.6 long-tail (12). Cluster C.6 items have flexible LANE-1 timing
(some at next SOP cycle, e.g. C.6.h, C.6.k).

End of synth pre-digest packet.
