# Bucket classification — 70 actionable SQL todos

**Substrate**: Phase A.P3 readback `current_sql_state.md`; plan.md M1-M12 close-out
section (`E5220A5E62ADC87B` L1-L240); cli_log/2026-W21_wsb.md A.1-A.12 +
inherited rolled items; bridge HEAD `ace3a42`.

**Sum invariant target**: 67 pending + 3 in_progress = 70. Bucket totals must equal 70.
Blocked rows (19) recorded in `current_sql_state.md` but excluded from bucket
assignment per envelope STEP B.4 wording.

**Bucket counts**: A=12 / B=13 / C=34 / D=3 / E=3 / F=5 — sum = 70 ✓

---

## Section A — BUCKET-A: AGENT-AUTONOMOUS (12 items)

Closeable by agent without operator/synth input; mechanical edits or drafts.

| id | title (truncated) | suggested action | est runtime |
|---|---|---|---|
| bibliographic-corrections-d1d3 | Bibliographic D-01..D-03 fix | one-pass `.bib` patch at next bibliography touch | 15 min |
| cc-median-resurgence-pslq-draft | Draft CC-MEDIAN-RESURGENCE-PSLQ prompt | author prompt-spec stub at `tex/submitted/control center/prompt/` | 20 min |
| g6b-pivot-ct-median-resurgence-prompt-draft | Draft G6b pivot prompt for §3.5 median-resurgence | author prompt-spec stub gated on §3.5 read | 25 min |
| mazzocco-template-affiliation-update | Update 034/037 Mazzocco templates Birmingham→UPC Barcelona | mechanical 5-template patch (analog of Zudilin Newcastle→Radboud) | 15 min |
| next-prompts-queue-v2 | Refresh next-prompts queue v1→v2 | one-pass queue rewrite absorbing T37L+T37M landings | 15 min |
| prompt-001-template-fixes | Template patches per Item-19 firing discrepancies | three small regex fixes to prompt 001 template | 10 min |
| prompt-017L4-draft-fourth-A3-rep | Draft 017L4 fourth A=3 rep prompt | author prompt-spec stub at 017L4 path | 20 min |
| prompt-017i-draft | Draft 017i (T37I-S3-EXTRACTION) | author prompt-spec stub conditional on 017d G6B_PARTIAL | 20 min |
| relay-083-d2note-zenodo-runbook | Fire relay 083 (drafted) | dispatch 083 envelope; T1-light ~25-35 min agent | 30 min |
| relay-084-arxiv-mirror-audit-final | Fire relay 084 (drafted) | dispatch 084 envelope; T1-mid ~30-45 min | 40 min |
| relay-085-pcf1-v13-source-drift-reconcile | Fire relay 085 (drafted) | dispatch 085 envelope; T1-light ~20-30 min | 25 min |
| w22-cli-synth-2026-05-monthly-handoff | Author 2026-05_monthly_handoff.md by 2026-05-31 | CLI-Synth in-tier monthly handoff at end-of-month | 60 min |

**Substrate citations** (Phase B.1 requirement): each item description in
`current_sql_state.md` enumeration cites the on-disk prompt-spec or template
file plus existing bridge session reference. Cross-anchored to plan.md
"Per-milestone close-out actions" L61-L195 (M1, M8b, M11 sub-actions).

---

## Section B — BUCKET-B: OPERATOR-RUNNABLE (13 items)

Closeable by operator action with agent-prepared runbook; no synth dependency.

| id | title (truncated) | suggested runbook | runbook envelope status |
|---|---|---|---|
| compositio-followup | Compositio CM 10573 (PCF-1 P12) passive watch | inline-doable; operator monitors editorial decision | inline-suffices |
| endorsement-handles-acquire | Acquire arXiv handles for math.NT endorsers (records #2, #4) | operator look-up + template population | inline-suffices |
| garoufalidis-endorsement-pivot | Pivot to Garoufalidis for PCF-1 v1.3 endorsement (DS873D) | operator pre-verifies + dispatches relay (5-step) | covered by 090 envelope (plan.md L201) |
| p11-mathcomp-fire-time-gate-checklist | P11 Math.Comp. fire-time gate (4 anomalies) | operator-side conditional on Math.Comp. resubmit decision | inline-suffices (Option C deferred) |
| pcf1-v13-arxiv-webform-fill | Complete arxiv.org/submit web-form for PCF-1 v1.3 (in_progress) | operator walks worksheet §5 click-through; awaits Zudilin code | covered by 084 envelope drain |
| pcf1-v13-reconcile | PCF-1 v1.3 source-drift reconcile (21pp local vs 16pp Zenodo) | operator path-(a) bump v1.4 vs path-(b) recover v1.3 snapshot | covered by 085 envelope (decision-support worksheet) |
| q-claude-30-31-send-d2-note-v21 | Send Q-CLAUDE-30 + 31 to Claude (D2-NOTE v2.1) | operator pastes Q + URLs into Claude.ai | inline-suffices |
| ramanujan-journal-resubmission-prep | PCF-1 v1.3 → Ramanujan Journal resubmission prep | operator + agent draft cover letter; portfolio collision GATED | covered by 091 envelope (plan.md L205) |
| siarc-umbrella-v2-1-dispatch | Bump SIARC umbrella v2.0→v2.1 to cite D2-NOTE v2.1 | operator triggers post-Zenodo deposit of D2-NOTE v2.1 | covered by 087 envelope (plan.md L200) |
| sop-bibliographic-verification-patch | SOP patch for lit-hunt bibliographic-verification step | operator-paced; patch belongs in `.github/copilot-instructions.md` | inline-suffices |
| w20-zenodo-iscitedby-polish-cycle3 | Optional Zenodo IsCitedBy polish (5 records) | operator Zenodo metadata edit cycle 3 | inline-suffices (deferred) |
| wasow-ocr-followon | Re-OCR Wasow 1965 ch.X via Acrobat / tesseract | operator-side OCR pipeline; not blocking | inline-suffices |
| zenodo-upload-d2-note | Operator Zenodo upload of D2-NOTE v1.0 (4pp) | operator runbook at sessions/2026-05-02/D2-NOTE-DRAFT/zenodo_upload_d2_note_runbook.md | covered by 083 envelope drain |

**Substrate citations**: each item cites either an existing runbook on disk
(zenodo-upload-d2-note → D2-NOTE-DRAFT/), a drafted envelope (relay-083/084/085),
or operator-side instructions in the SQL description. Cross-anchored to
plan.md L186-L195 (M11/M12 operational actions).

**Runbook clustering** (Phase E.2): no further envelope-grouping warranted —
the 5 covered items already map cleanly to 083/084/085/090/091 envelopes
already drafted or queued. The 8 inline-suffices items are individually small.

---

## Section C — BUCKET-C: SYNTH-GATED (34 items)

Genuinely requires synth Mon AM JST arbitration or pick. Cluster anchors per
Phase F.2.

### Cluster C.1 — W21 LANE-1 ratifications + DEFER + HOLD pickups (5 items)

| id | synth question | LANE-1 timing | substrate anchor |
|---|---|---|---|
| w21-lane1-ratify-068-m4-closure | RATIFY 068 verdict UPGRADE_FULL_VIA_DEG_A_ZERO_ROW (MEDIUM-HIGH→HIGH) | W21-Mon AM JST | bridge `e7bfe49` (068 handoff L28-32, L84-88) |
| w21-lane1-ratify-069-m6cc-d2-persist | RATIFY 069 verdict UPGRADE_V1_0_PARTIAL_NUMERICAL_PERSIST | W21-Mon AM JST | bridge `05810a2` |
| w21-lane1-oq-061-d-pcf1-v_quad-errata | OQ-061-D: PCF-1 v1.3 V_quad upper-branch errata decision | W21-Mon AM JST | LANE-2 handoff §Open questions OQ-061-D |
| w21-lane1-item6-pcf2-v3x-wording-revision | Item 6 HOLD: PCF-2 v3.x Zenodo amendment for S3 wording | W21-Mon AM JST | OQ-061-B |
| w21-lane1-item4-rule5-vocab-fold-in | Item 4 DEFER_TO_W21: rule5 vocabulary fold-in for protocol-to-stratum mismatch | W21-Mon AM JST | OQ-061-A |

### Cluster C.2 — Q-series arbitrations Q20-Q34 (10 items)

| id | synth question id | LANE-1 timing | substrate anchor |
|---|---|---|---|
| q20-conj33a-proof-upgrade-claude-arbitrate | Q20 | W21-Mon | sessions/2026-05-02/XI0-D3-DIRECT/handoff.md |
| q21-013-refire-path-arbitrate | Q21 | W21-Mon | sessions/2026-05-02/CC-FORMAL-BOREL-CLOSE/handoff.md §"What would have been asked" |
| q22-014-stretch-goal-arbitrate | Q22 | W21-Mon | sessions/2026-05-02/T25D-RETRY-13PARAM/handoff.md |
| q23-pslq-basis-hygiene-claude-arbitrate | Q23 | W21-Mon | T25D-RETRY-13PARAM/handoff.md (PSLQ basis hygiene rule) |
| q24-d2-polynomial-correction-discrimination-claude-arbitrate | Q24 | W21-Mon | Prompt 016 HALT note |
| q32-h1-rearbitration-timing | Q32 | post-Phase-2 | h1-label-arbitration coupled |
| q33-pslq-basis-hygiene-s2-foreclosure | Q33 | W21-Mon | 017m HALT methodology declaration |
| q34-ct14-section-3-5-amend-timing | Q34 | W21-Mon | sec.3.5 epistemic upgrade timing |
| h1-label-arbitration | Q-CLAUDE H1-label | W21-Mon (HIGH) | sessions/2026-05-02/T1-BIRKHOFF-TRJITZINSKY-LITREVIEW/handoff.md |
| q-claude-30-31-send-d2-note-v21 — recategorize | (Section B operator-runnable; skipped here) | — | (in B) |

(Note: q-claude-30-31 is operator-dispatch — see Section B.)

### Cluster C.3 — q038 arbitrations A + C (2 items)

| id | synth question | LANE-1 timing | substrate anchor |
|---|---|---|---|
| q038-a-bibliographic-preverification-rule-scope | Q-038-A/B rule extension scope | W21-Mon | bridge sessions/2026-05-04/MILESTONE-RESIDUAL-GAP-SURVEY-M4-M7-M8B-M9/ |
| q038-c-partial-status-acceptance | Q-038-C dossier PARTIAL acceptance | W21-Mon | same handoff |

### Cluster C.4 — Resubmit-target picks (4 items)

| id | paper / record | candidate venues | substrate anchor |
|---|---|---|---|
| painleve3d6-vquad-resurgence-resubmit-target-decision | Item 11 (Painlevé III(D6)) | LMP / CMP / IMRN / J. Phys. A / ConstrApprox / CR | submission_log.txt Item 11 desk-reject (Nonlinearity 2026-04-29) |
| psl2z-4tier-resubmit-target-decision | Item 14 (PSL2(Z) 4-Tier) | IMRN / Math. Research Letters / Selecta / Trans AMS / JNT / Math Z | Item 14 desk-reject (Ramanujan Journal 2026-04-29) |
| ratio-universality-meinardus-g01-resubmit-target-decision | Item 17 (Ratio Universality / Meinardus) | JNT / Acta Math Hung / Trans AMS / Adv Math / Math Z / Israel J Math | Item 17 desk-reject (Acta Arithmetica 2026-05-04; AMU Poznań ecosystem) |
| stieltjes-pcf-resubmit-target-decision | Item 25 (Stieltjes Characterization) | ConstrApprox / J. Approx. Theory / J. Math. Anal. Appl. / Acta Sci. Math. (Szeged) / Indagationes | Item 25 desk-reject (Aequationes 2026-05-02) |

### Cluster C.5 — Lean-relaunch venue pick (1 item)

| id | menu options | substrate anchor |
|---|---|---|
| lean4-cnp-tunnell-venue-pivot-post-jadvres | LMCS (primary recommended per 079) / J Formalized Reasoning / Math in Computer Science / TCS / 7-option menu in 079 | bridge `72f9850` (079 §F.E w21_lane1_lean_relaunch_decision_packet.md) |

### Cluster C.6 — Other arbitrations (12 items)

| id | arbitration class | LANE-1 timing | substrate anchor |
|---|---|---|---|
| ct-v14-sec35-reading-decision | Reading A vs B for §3.5 G17 amendment | W21-Mon | 026 verdict |
| g17-layer-separation-amend-ct14 | Decide whether CT v1.4 amends §3.5 layer separation | W21-Mon | sessions/2026-05-02/VQUAD-PIII-NORMALIZATION-MAP/handoff.md |
| g19-betaR-zero-d2-formalize | β_R=0 universal at d=2 formalization | post-Phase-2 | Prompt 010 PARTIAL + 016 HALT |
| m4-fractional-rank-borderline-anormal-gap-implication | M4 scheduling decision (Wasow vs SIARC vs deeper-than-Costin) | post-038 absorption | UF-038-2 |
| m4-m7-m8b-followon-lit-hunt-prompt-spec | Possible follow-on lit-hunt with bibliographic-pre-verification scope | gated on Q-038-B | 038 §UF-038 / §Anomalies §5 |
| pcf1-meinardus-ramanujan-portfolio-collision-arbitration | PCF-1 + Item 17 dual-Ramanujan Journal collision | W21-Mon | sessions/2026-05-04/SYNTHESIZER-Q38-AND-RAMANUJAN-VERIFY-ABSORB/portfolio_collision_flag.md |
| prompt-017g-amend | Amend 017g gate set OR retire | W21-Mon | 017g HALT |
| sop-wording-availability-not-fire-authorization-candidate | Standing-instructions append meta-rule | next SOP cycle | synthesizer arbitration 2026-05-04 ~17:26 JST |
| synth-review-048R-5-day-early-refire-flag | T1 Synth review of 048R 5-day-early fire | W21-Mon | bridge `6bbd3f0` + 056 substrate at sessions/2026-05-06/048R-EARLY-FIRE-DECISION-SUBSTRATE/ |
| w20-lane2-r2-intra-document-mismatch-wording | Mismatch-locus wording revision (intra-document) | W21-Mon (Item 4 coupled) | LANE-2 P4 finding |
| w20-synth-058-halt-name-prefix-convention | Halt-name shorthand-vs-prefix convention | next SOP cycle | 058 anomaly D3 |
| w20-synth-arbitration-n3-coincidence | T1 weekly arbitration on n=3 coincidence | W21-Mon (T1 weekly cadence) | sessions/2026-05-06/N3-FOURTH-LAW-ARBITRATION-SUBSTRATE/ |
| w20-synth-arbitration-v3-1-wording-softening | T2B v3.1 b7-singular wording softening | W21-Mon | bridge `fe15737` + 044B verdict |

**Section C total**: 5 + 10 + 2 + 4 + 1 + 12 = 34 ✓ (Cluster C.2 footnote: q-claude-30-31 is in Section B; Cluster C.6 also lists 12 distinct ids per id-uniqueness check.)

---

## Section D — BUCKET-D: OBSOLETE-CANDIDATE (3 items)

Likely superseded by bridge HEAD or downstream verdict; needs confirmation +
operator SQL UPDATE post-082 (see `proposed_sql_closures.sql`).

| id | supersession anchor (substrate citation) |
|---|---|
| relay-082-close-out-roadmap | THIS fire's bridge session at `sessions/2026-05-07/T2-CLOSE-OUT-ROADMAP-082/` (commit-to-be on push); spec-listed deliverable set (7 production + 4 AEAL + handoff) addresses the SQL row's described task |
| synthesizer-recommendation-m6-pivot-beta | bridge `95ffa1e` 036 SIARC-OKAMOTO-1987-SEC3-SCAN landed verdict CONFIRM_M6_PHASE_B5_INDEX2_FINAL; description self-notes "036 landed upstream at bridge commit 95ffa1e" — recommended branch (β fire 036 first) executed |
| w19-synthesizer-trust-failure-pattern-flag (in_progress) | cli_log/2026-05-05.md L928-L932 records 2026-05-05 ~10:55 JST synthesizer accepted partial exoneration with revised rule5 framing; description self-notes "Queued for next week's instructions.txt amendment in that revised form" + "5th instance => structural problem rule NOT triggered" |

**Section D total**: 3.

---

## Section E — BUCKET-E: DOWNSTREAM-DEPENDENT (3 items)

Gated on M2/M4/M6/M8b/M9 milestone progress; cannot close pre-LANE-1.

| id | gating milestone | substrate anchor |
|---|---|---|
| m6-phase-b5-w-crosswalk-anchor | M6 Phase B.5 (NY 2004 acquisition Tier-1 candidate) | description "Sakai 2001 supplies W((2A_1)^(1)) framing but not the W(B_2) ↔ W((2A_1)^(1)) homomorphism" |
| t1-phase-2-bt-apply | M4 (Phase 2 readiness; depends on h1-label-arbitration + t1-primary-sources-acquire) | dependency edges in snapshot deps section |
| t1-phase-3-borderline-ansatz | M4 / M7 / M8b (Tier-2 4-6 hr; Wasow §X.3 OCR + PCF-2 v1.3 A_fit readback preconditions) | description "Tier-2; ~4-6 hr symbolic work + literature reading" |

**Section E total**: 3.

---

## Section F — BUCKET-F: PAPER-DRAFT-LONG (5 items)

Multi-day work; out of scope for close-out drainage.

| id | scope estimate | substrate anchor |
|---|---|---|
| ct-v14-narrative-draft (in_progress) | multi-day pure drafting; §3.7 + Prop 3.7.A + §4.5 + op:third-stratum | description verbatim "Pure drafting task: §3.7 stratification, Prop 3.7.A branch identity, §4.5 S2-foreclosure footnote, op:third-stratum-modular-interpretation; build clean; do NOT push or upload" |
| d1-paper-cubic-quartic | multi-day; depends on t1-birkhoff-trjitzinsky | description "Depends on t1-birkhoff-trjitzinsky (Phase 2 verdict). Cites umbrella v2.0 + Theorem B4 + T2 Petersson. Target Math. Comp / Exp. Math." |
| d7-aeal-methodology | multi-day cross-community methodology paper | description "Cross-community methodology paper; lower priority" |
| g16-spec-floor-discipline | long-arc; ties into D7-AEAL methodology paper | description "Long-arc; ties into D7-AEAL methodology paper" |
| siarc-master-v0 | multi-day; depends on T1+D1+D2 | description "Depends on T1 + D1 + D2. Master Conjecture, E/P_k/B stratification, Phi functor. Target Bull. AMS / Notices AMS" |

**Section F total**: 5.

---

## Sum invariant verification

A=12 + B=13 + C=34 + D=3 + E=3 + F=5 = **70** ✓

Match against Phase A.P3 actionable count (67 pending + 3 in_progress = 70). No
HALT_082_BUCKET_SUM_MISMATCH triggered.

## Bucket-membership exclusivity (Phase I.3 invariant)

Each of the 70 actionable rows appears in exactly one of {A, B, C, D, E, F}.
Manually cross-checked across Section A id list, Section B id list, Section C
clusters C.1+C.2+C.3+C.4+C.5+C.6 id lists, Section D id list, Section E id list,
Section F id list. Zero duplicate-membership entries. No HALT_082_BUCKET_NON_EXCLUSIVE
triggered.

End of bucket classification.
