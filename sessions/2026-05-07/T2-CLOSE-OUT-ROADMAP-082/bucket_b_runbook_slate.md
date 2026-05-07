# BUCKET-B operator-runnable runbook slate (13 items)

**Substrate**: `bucket_classification.md` Section B; plan.md M1-M12 close-out
section L61-L213 (envelope queue 086-095 sketch); existing on-disk runbooks.

---

## B-1. compositio-followup — passive watch

- **Operator action**: monitor Compositio Mathematica 10573 editorial decision.
- **Pre-fire bridge readback**: none — passive.
- **Envelope-needed**: inline-suffices (no envelope; tracker-only update on
  decision arrival).

## B-2. endorsement-handles-acquire — operator handle look-up

- **Operator action**: identify ~3 plausible math.NT endorsers (e.g., authors of
  cited PCF-related papers with arXiv accounts), look up arXiv user-id strings,
  populate Prompt 002 ENDORSEMENT_REQUEST_<short>.md templates.
- **Pre-fire bridge readback**: review existing 034 + 037 templates at
  `siarc-relay-bridge/sessions/2026-05-04/ARXIV-MIRROR-RUNBOOK-REFIRE/` and
  `sessions/2026-05-04/ARXIV-ENDORSEMENT-TEMPLATES-EXPAND/` (commit `9292a8f`).
- **Envelope-needed**: inline-suffices (operator-paced; can run in parallel with
  pcf1-v13-reconcile and ct-v13-author-placeholder-fix per description).

## B-3. garoufalidis-endorsement-pivot — operator pre-verify + dispatch relay

- **Operator action**: 5-step sequence per description: (1) pre-verify Garoufalidis
  institutional email + arXiv handle; (2) dispatch relay analogous to
  `ZUDILIN-ENDORSEMENT-DRAFT-FINALIZE`; (3) synthesizer pre-send review;
  (4) operator sends from own mail client with code DS873D + Zenodo concept DOI
  19931635; (5) agent deposits `ZUDILIN-DECLINE-GAROUFALIDIS-PIVOT` bridge session.
- **Pre-fire bridge readback**: review 034 template T06
  `endorsement_template_pcf1_v1.3_garoufalidis.md`.
- **Envelope-needed**: covered by 090 envelope per plan.md L201 ("post-LANE-1
  R.11 envelope: (a) update 034 templates ...; (b) operator-side endorser handle
  acquisition ...; (c) record #2 + #4 arXiv mirror submission via 084 runbook").

## B-4. p11-mathcomp-fire-time-gate-checklist — fire-time gate

- **Operator action**: 4 anomalies to resolve at submission time: (1) swap ¶5
  from suggested-referees to suggested-Editor model (HIGHEST PRIORITY); (2)
  preserve standalone copy of 2026-04-26 JTNB cover letter; (3) re-confirm 3
  Tier-1 endorser-track names; (4) Zudilin disclosure-at-submission.
- **Pre-fire bridge readback**: 046 P11-COVERLETTER-MATHCOMP-DEFENSIVE handoff
  Anomalies + operator_dispatch_checklist.md.
- **Envelope-needed**: inline-suffices (Option C deferred per OPT_C 2026-05-06
  ~20:38 JST — operator selected defer until further breakthroughs).

## B-5. pcf1-v13-arxiv-webform-fill — operator web-form (in_progress)

- **Operator action**: open `arxiv_submission_worksheet.md` from
  `PCF1-V13-ARXIV-DRAFT-PREP` bridge; visit arxiv.org/submit; walk worksheet
  §5 click-through 1-10. At step 7 copy 6-char endorsement code; at step 8 use
  worksheet §6 template to forward code to w.zudilin@math.ru.nl. Save draft;
  await Zudilin redemption at arxiv.org/auth/endorse.
- **Pre-fire bridge readback**: `PCF1-V13-ARXIV-DRAFT-PREP/arxiv_submission_worksheet.md`.
- **Envelope-needed**: covered by 084 envelope per plan.md L199 ("Drains
  pcf1-v13-arxiv-webform-fill (in_progress) + 5 record-level mirror submissions").
  Currently awaiting Zudilin code redemption (description verbatim: "draft is
  saved server-side at incomplete-awaiting-endorsement").

## B-6. pcf1-v13-reconcile — operator path selection

- **Operator action**: pick path-(a) bump v1.4 deposit on Zenodo + re-run Prompt 002
  against v1.4 DOI, OR path-(b) recover exact v1.3 16-page .tex snapshot from git
  history / Zenodo archive and rebuild `arxiv_pack_pcf1_v1.3` from snapshot.
- **Pre-fire bridge readback**: `PCF1-V13-SOURCE-RECOVERY-PROBE` substrate +
  v1.3 16pp Zenodo deposit hash.
- **Envelope-needed**: covered by 085 envelope (drafted at
  `tex/submitted/control center/prompt/085_t1_pcf1_v13_source_drift_reconcile.txt`).

## B-7. q-claude-30-31-send-d2-note-v21 — Claude.ai dispatch

- **Operator action**: send Q-CLAUDE-30 (D2-NOTE v2.1 self-containment) +
  Q-CLAUDE-31 (arXiv classification math.CA primary, math.NT cross-list) to
  Claude.ai. Q-CLAUDE-31 has agent advisory math.CA primary (was math.NT in v2).
- **Pre-fire bridge readback**: D2-NOTE v2.1 PDF + Phase A* + BT 1933 §§4-6 +
  Newton-polygon Lemma + Wasow §19 chain.
- **Envelope-needed**: inline-suffices; Claude.ai chat-paste only.

## B-8. ramanujan-journal-resubmission-prep — PCF-1 v1.3 → RJ prep

- **Operator action**: cover letter draft (Editor-targeted: Ono); arXiv mirror
  (Strategy α — arXiv first then RJ); Springer-Nature v3.0 style file;
  submission_log Item 23 update on submit.
- **Pre-fire bridge readback**: `sessions/2026-05-04/SYNTHESIZER-Q38-AND-RAMANUJAN-VERIFY-ABSORB/ramanujan_journal_verification.md`.
- **Envelope-needed**: covered by 091 envelope (M12 portfolio resubmit-target
  packaging) per plan.md L205. Portfolio-collision-with-Item-17 GATES finalization;
  see C.6 cluster pcf1-meinardus-ramanujan-portfolio-collision-arbitration.

## B-9. siarc-umbrella-v2-1-dispatch — umbrella version bump

- **Operator action**: deposit D2-NOTE v2.1 on Zenodo (concept DOI 19965041 for
  umbrella) → trigger v2.1 dispatch + new umbrella version pin + cross-cite
  refresh.
- **Pre-fire bridge readback**: post-Zenodo-deposit-of-D2-NOTE-v2.1 trigger;
  prior siarc-umbrella-v2-1-cite-d2-note-v2 todo (now obsolete).
- **Envelope-needed**: covered by 087 envelope per plan.md L200 ("074-NEXT
  post-RATIFY: PCF-2 v1.4 amendment cycle + Wasow §X.3 OCR acquisition substrate").

## B-10. sop-bibliographic-verification-patch — SOP file edit

- **Operator action**: per 031 verdict META-LESSON, patch `.github/copilot-instructions.md`
  OR per-prompt-drafting checklist to require both DOI + arXiv ID cross-check
  for lit-hunt prompts.
- **Pre-fire bridge readback**: 031 verdict at
  `sessions/2026-05-04/WITTE-FORRESTER-2010-ACQUISITION/`.
- **Envelope-needed**: inline-suffices (operator-paced; not a relay-agent task).

## B-11. w20-zenodo-iscitedby-polish-cycle3 — optional Zenodo metadata edit

- **Operator action**: edit existing Zenodo records (PCF-1 v1.3 / PCF-2 v1.3 /
  CT v1.3 / SIARC umbrella v2.0 / D2-NOTE v2.1) to add IsCitedBy
  10.5281/zenodo.20048196 in Related Identifiers.
- **Pre-fire bridge readback**: prior cycle convention (D2-NOTE v2.1 amendment
  block follow-up (ii)).
- **Envelope-needed**: inline-suffices (deferred consistent with v2.1-cycle posture).

## B-12. wasow-ocr-followon — operator OCR pipeline

- **Operator action**: ABBYY FineReader / Acrobat OCR / tesseract pipeline on
  existing `literature/g3b_2026-05-03/04_wasow_1965_dover.pdf` (5.4 MB,
  image-only no text layer).
- **Pre-fire bridge readback**: 009 verdict carried without Wasow direct via
  transitive BT+Birkhoff evidence.
- **Envelope-needed**: inline-suffices; not blocking for Phase 2 (nice-to-have
  for verbatim §X.3 polynomial-coefficient slope-bound citation).

## B-13. zenodo-upload-d2-note — operator Zenodo upload

- **Operator action**: upload D2-NOTE v1.0 (4 pages, 343419 B,
  sha256 `f2be89c1...22bd94b8`, 8 AEAL claims D2-A1...D2-A8, 0 unresolved
  citations) per runbook at `sessions/2026-05-02/D2-NOTE-DRAFT/zenodo_upload_d2_note_runbook.md`.
- **Pre-fire bridge readback**: D2-NOTE-DRAFT runbook (post-upload, draft
  submission_log Item 20 splice prompt).
- **Envelope-needed**: covered by 083 envelope per plan.md L199 ("T1-light
  D2-NOTE Zenodo upload runbook").

---

## Runbook envelope summary

| envelope # | items drained | when |
|---|---|---|
| 083 (drafted) | B-13 (zenodo-upload-d2-note) | pre-LANE-1 (W20 Fri-Sun fire) |
| 084 (drafted) | B-5 (pcf1-v13-arxiv-webform-fill) | pre-LANE-1 (W20 Fri-Sun fire) |
| 085 (drafted) | B-6 (pcf1-v13-reconcile) | pre-LANE-1 (W20 Fri-Sun fire) |
| 087 (sketch) | B-9 (siarc-umbrella-v2-1-dispatch) | post-LANE-1 W21 (Tue 2026-05-13) |
| 090 (sketch) | B-3 (garoufalidis-endorsement-pivot) + cluster with mazzocco-template-affiliation-update (BUCKET-A A-4) | post-LANE-1 W21 |
| 091 (sketch) | B-8 (ramanujan-journal-resubmission-prep) | post-LANE-1 W21 |

**Inline-suffices items** (7 of 13): B-1 / B-2 / B-4 / B-7 / B-10 / B-11 / B-12.
No new envelope drafts needed; operator dispatches at convenience.

**Envelope clustering** (Phase E.2): the 6 envelope-covered items map cleanly
to existing 083/084/085/087/090/091 numbered envelopes per plan.md L198-L213
sketch. No further grouping warranted.

End of BUCKET-B operator-runnable runbook slate.
