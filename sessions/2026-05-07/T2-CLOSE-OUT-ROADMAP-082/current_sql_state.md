# Phase A.P3 substrate readback — current SQL todo state

**Source**: `tex/submitted/control center/sql_todos_snapshot_2026-05-07_18-40-JST.md`
(76089 B / 290 lines / SHA16 `60DD655EA1880BF0`); pre-exported by parallel
prompt-drafting CLI session at bridge HEAD `ace3a42`.

**Pointer**: `tex/submitted/control center/082_sql_seed_pointer.txt`
(1983 B / SHA16 `FE9998CE4AA34E59`).

**Phase A.P3 redirect rationale**: firing CLI session has no SQL/sqlite/MCP-todo-DB
tool exposed; snapshot serves as Phase A.P3 substrate per pointer-file §"Phase A.P3
instructions for the 082 agent when SQL is unavailable" item 1. See discrepancy_log.json
D-N (non-blocking) and unexpected_finds.json for protocol detail.

---

## Status counts

| status | count |
|---|---|
| pending | 67 |
| in_progress | 3 |
| blocked | 19 |
| done | 233 |
| **total** | **322** |

**Phase B.4 sum invariant**: actionable = 67 + 3 = **70**. Blocked rows (19) excluded
per envelope STEP B.4 wording (`pending + in_progress count read in P3`).

---

## Phase A.P4 — plan.md latest snapshot read

**File**: `C:\Users\shkub\.copilot\session-state\5d95be1e-c815-4f0e-997d-851b858c1d99\plan.md`
(209372 B / SHA16 `E5220A5E62ADC87B`).

**Section read**: lines 1-240 — `## Status snapshot (2026-05-07 ~18:32 JST,
M1-M12 CLOSE-OUT ROADMAP)`.

**M1-M12 milestone summary verbatim**:
- M1, M3, M5, M6 (=M6.H4 leg), M7, M8 — done
- M4 — substrate-ratified (074 dossier; W21 LANE-1 absorption pending)
- M6.CC R1 — blocked (R5 = Okamoto 1987 §§2-3 + Conte-Musette 2008 ch.7)
- M2 — downstream (PCF-2 v1.4 deposit Q22-gated)
- M8b — future / partial (017m Borel-Padé S_2 path drafted)
- M9 — gated (downstream of {M4, M6.CC} unconditionally)
- M10 / M11 / M12 — operational pending W21 LANE-1 (079 / 078 / 077)

**Per-milestone close-out actions table**: plan.md L61-L195 — directly informs
bucket assignment for ~30 of the 70 actionable rows.

**Concrete envelope queue 086-095 sketch (M-tagged)**: plan.md L198-L213 — feeds
Phase D drain plan + Phase E runbook slates.

**Risk register (close-out blockers)** R1-R5: plan.md L214-L235.

---

## Phase A.P5 — cli_log/2026-W20.md + cli_log/2026-W21_wsb.md A-class carry-forwards

**A.1** W21 LANE-1 dossier-set absorption — substrate at bridge SHAs `9596c21` (074)
+ `5137155` (075) + `49f3423` (077) + `32b808b` (078) + `72f9850` (079). Maps to SQL
ids w21-lane1-ratify-068 + w21-lane1-ratify-069 + lean4-cnp-tunnell-venue-pivot +
endorser-pivot pair + portfolio resubmit-target items.

**A.2** T1 Synth weekly arbitration on n=3 fourth-law candidate — substrate at
`siarc-relay-bridge/sessions/2026-05-06/N3-FOURTH-LAW-ARBITRATION-SUBSTRATE/`
(35780 B). Maps to SQL id w20-synth-arbitration-n3-coincidence.

**A.3** PCF-2 v3.x wording softening to two known data points at h≤10⁹ — substrate
at 044B handoff §"Recommended next step". Maps to SQL id
w20-synth-arbitration-v3-1-wording-softening.

**A.4** 049 P11-SICF Option-3 post-verdict execution — 30-day binding-window
operator-conceptual; substrate at sessions/2026-05-06/P11-SICF-DECISION-W20-REFIRE/.

**A.5** CC-VQUAD-PIII-NORMALIZATION-MAP main fire (M6.CC) — gated on R5 acquisition.
Maps to SQL ids w20-relay-058-cc-vquad-piii-main-relay (blocked), vquad-pIII-norm-map-close
(blocked), vquad-pIII-normalization-map (blocked).

**A.6** Picture v1.20 deposit decision — gated on operator-side W20-Wed cascade absorption.

**A.7** 080 cross-dossier coupling matrix — landed at `9745b78` post-081.

**A.8** P-008 §7 substrate refresh via 047 — fire window W21-Thu.

**A.9** 050 P-009 active-variant re-render triggers — defensive only; trigger-gated.

**A.10** OQ-W21-Q22 PCF-2 v1.4 deposit decision — substrate at
sessions/2026-05-02/T25D-RETRY-13PARAM/pcf2_v1.4_amendment.md L3 status `DRAFT`.
Maps to SQL ids pcf2-v1-4-deposit-decision-q22-gated (blocked) + q22-014-stretch-goal-arbitrate.

**A.11** OQ-W21-LITERATURE-ALTERNATIVE → 076 path-δ lit-hunt — substrate at 075
handoff §U3 + §D4. Maps to SQL id relay-076-path-delta-lit-recon (blocked).

**A.12** OQ-W21-PORTFOLIO-DOI-CANONICALIZATION — substrate at 077 D-077-1.

**Inherited rolled OQs**: OQ-W21-CHART-MAP, 069 D2/D3/D4, CT v1.4 in_progress.
Maps to SQL ids w21-lane1-oq-061-d-pcf1-v_quad-errata + w21-lane1-item4 + w21-lane1-item6
+ ct-v14-narrative-draft (in_progress) + g17-layer-separation-amend-ct14 +
w20-lane2-r2-intra-document-mismatch-wording.

---

## 70 actionable rows enumerated (id list; full description in snapshot)

**67 pending** (snapshot L77-L143):
bibliographic-corrections-d1d3 / cc-median-resurgence-pslq-draft / compositio-followup /
ct-v14-sec35-reading-decision / d1-paper-cubic-quartic / d7-aeal-methodology /
endorsement-handles-acquire / g16-spec-floor-discipline / g17-layer-separation-amend-ct14 /
g19-betaR-zero-d2-formalize / g6b-pivot-ct-median-resurgence-prompt-draft /
garoufalidis-endorsement-pivot / h1-label-arbitration / lean4-cnp-tunnell-venue-pivot-post-jadvres /
m4-fractional-rank-borderline-anormal-gap-implication / m4-m7-m8b-followon-lit-hunt-prompt-spec /
m6-phase-b5-w-crosswalk-anchor / mazzocco-template-affiliation-update / next-prompts-queue-v2 /
p11-mathcomp-fire-time-gate-checklist / painleve3d6-vquad-resurgence-resubmit-target-decision /
pcf1-meinardus-ramanujan-portfolio-collision-arbitration / pcf1-v13-reconcile /
prompt-001-template-fixes / prompt-017L4-draft-fourth-A3-rep / prompt-017g-amend /
prompt-017i-draft / psl2z-4tier-resubmit-target-decision / q-claude-30-31-send-d2-note-v21 /
q038-a-bibliographic-preverification-rule-scope / q038-c-partial-status-acceptance /
q20-conj33a-proof-upgrade-claude-arbitrate / q21-013-refire-path-arbitrate /
q22-014-stretch-goal-arbitrate / q23-pslq-basis-hygiene-claude-arbitrate /
q24-d2-polynomial-correction-discrimination-claude-arbitrate / q32-h1-rearbitration-timing /
q33-pslq-basis-hygiene-s2-foreclosure / q34-ct14-section-3-5-amend-timing /
ramanujan-journal-resubmission-prep / ratio-universality-meinardus-g01-resubmit-target-decision /
relay-082-close-out-roadmap / relay-083-d2note-zenodo-runbook / relay-084-arxiv-mirror-audit-final /
relay-085-pcf1-v13-source-drift-reconcile / siarc-master-v0 / siarc-umbrella-v2-1-dispatch /
sop-bibliographic-verification-patch / sop-wording-availability-not-fire-authorization-candidate /
stieltjes-pcf-resubmit-target-decision / synth-review-048R-5-day-early-refire-flag /
synthesizer-recommendation-m6-pivot-beta / t1-phase-2-bt-apply / t1-phase-3-borderline-ansatz /
w20-lane2-r2-intra-document-mismatch-wording / w20-synth-058-halt-name-prefix-convention /
w20-synth-arbitration-n3-coincidence / w20-synth-arbitration-v3-1-wording-softening /
w20-zenodo-iscitedby-polish-cycle3 / w21-lane1-item4-rule5-vocab-fold-in /
w21-lane1-item6-pcf2-v3x-wording-revision / w21-lane1-oq-061-d-pcf1-v_quad-errata /
w21-lane1-ratify-068-m4-closure / w21-lane1-ratify-069-m6cc-d2-persist /
w22-cli-synth-2026-05-monthly-handoff / wasow-ocr-followon / zenodo-upload-d2-note

**3 in_progress** (snapshot L75-L77):
ct-v14-narrative-draft / pcf1-v13-arxiv-webform-fill / w19-synthesizer-trust-failure-pattern-flag

**19 blocked** (excluded from bucket sum; snapshot L46-L74; recorded for completeness):
ct-v13-author-placeholder-fix / g22-vquad-piii-canonical-form-residual /
mazzocco-endorsement-pivot / pcf2-v1-4-deposit-decision-q22-gated /
prompt-017d-fire / prompt-017g-fire / relay-076-path-delta-lit-recon /
t25d-j0-chowla-selberg / umbrella-v2-l295-phrasing-disposition /
vquad-pIII-norm-map-close / vquad-pIII-normalization-map /
w19-relay-044-bzero-offset-log-sweep / w19-relay-044C-e2-escalation-CONTINGENT /
w20-058R-phase-d2-numerical-jacobian-completion / w20-bibtex-stub-bt-baseline-umbrella-v2x /
w20-lane2-item2-3c-bt-baseline-note-formal-amendment /
w20-lane2-item2-3e-extended-empirical-sweep /
w20-relay-058-cc-vquad-piii-main-relay /
w20-relay-063-p11-mathcomp-resubmission-package

---

## Bridge HEAD (Phase A.P2)

`ace3a42` (T1-W20-CLOSING-W21-WSB-081 push) at session start.

End of Phase A readback.
