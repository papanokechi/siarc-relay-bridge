# Handoff -- T1-D2-NOTE-ZENODO-UPLOAD-RUNBOOK-083
**Date:** 2026-05-07 (Thu, W20)
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~30 minutes
**Status:** COMPLETE -- substrate produced; deposit gated on operator decision (see Anomalies §1)
**Bridge HEAD at fire time:** `402c7de` (T2-FRD-EXPORT-FROM-M5-098 land)

## What was accomplished

Produced 3 production deliverables (`zenodo_d2_note_metadata.json`,
`zenodo_d2_note_runbook.md`, `post_deposit_followon.md`) + 4 AEAL
artefacts (`claims.jsonl` with 7 entries, `halt_log.json`,
`discrepancy_log.json`, `unexpected_finds.json`) per relay-083
envelope Phases 0-F. The runbook refreshes the 2026-05-02 D2-NOTE-DRAFT
runbook with current substrate hashes + a SUPERSESSION GATE section 0
that surfaces the structural conflict between the relay's stated
target (D2-NOTE v1.0 deposit per SQL todo `zenodo-upload-d2-note`)
and the picture-chain reality (D2-NOTE v2.0 + v2.1 already deposited
2026-05-03 / 2026-05-04 at concept DOI 10.5281/zenodo.19996689).
The agent did NOT pre-select a disposition; operator decides among
Options A (DROP, recommended for economy), B (DEPOSIT_AS_NEW_CONCEPT
orphan-concept route), or C (DEFER to W21 LANE-1). Phase F.1
forbidden-verb scan PASSED at 0 hits after 4 in-session mitigations.

## Key numerical findings

- D2-NOTE v1.0 PDF SHA-256 verified bit-identical to 2026-05-02
  D2-A6/A8 anchor: `f2be89c1...22bd94b8` (343419 B; 4 pages); no
  drift across 5-day interval (083-C1).
- D2-NOTE v1.0 .tex / .bib / .jsonl / description SHAs all
  bit-identical to 2026-05-02 freeze (083-C2).
- Sister-deposit count referenced in metadata.json
  `related_identifiers`: 8 Zenodo DOIs (4 concept + 4 version)
  covering PCF-1 / PCF-2 / Channel Theory / SIARC umbrella + 2
  isDocumentedBy URLs to bridge sessions; total 10 rows (083-C5).
- Two prior D2-NOTE deposits identified at concept DOI
  10.5281/zenodo.19996689 (v2.0 version 19996690 / 2026-05-03;
  v2.1 version 20015923 / 2026-05-04) per picture-chain memory +
  close_out_matrix L132 + sql_todos_snapshot L118 (083-C6).
- HALT_083_SUPERSEDED literal halt did NOT trigger -- SQL todo
  `zenodo-upload-d2-note` status is `pending`, not `done`. Structural
  supersession surfaced as runbook section 0 + anomaly D-1 + U-1
  for operator decision.
- Phase F.1 forbidden-verb scan: 0 hits PASS after 4 in-session
  mitigations (3 in runbook at lines L90 / L202 / L204 rewriting
  the words c-o-n-f-i-r-m / s-h-o-w / s-h-o-w-s to neutral
  alternatives; 1 in followon at L71 rewriting s-h-o-w-s to
  "records"). Pre-mitigation hit-count 4; post-mitigation 0.
- Phase F.2 quote-length scan: 0 hits >50-word non-META
  blockquotes. The single 81-word historical-preface paragraph in
  runbook §3 step 5 is META-class operator-action exempt per
  envelope.
- Phase F.3 metadata schema sanity: PASS -- every key in
  `zenodo_d2_note_metadata.json` carries a `_substrate_anchors`
  entry citing either a sister-deposit precedent or an explicit
  substrate path; `_supersession_warning` block fully grounded in
  picture-chain + close_out_matrix + sql_todos_snapshot.

## Judgment calls made

- **J1: Treated SQL todo `zenodo-upload-d2-note` as version-of-record
  authoritative over relay-083 prompt-body "v2.0" nomenclature.**
  The relay body internally drifts (Phase B.1 says "v2.0" while the
  closes-clause says "zenodo-upload-d2-note" which per snapshot L118
  is for v1.0). Resolved in favour of the SQL todo description
  (4-page / 343419 B / sha f2be89c1.. matches v1.0); produced v1.0
  deliverables. Rationale: the SQL todo row is the more specific
  artefact; the relay drafter likely had stale memory of which v#
  was deposited.
- **J2: Did NOT pre-select among Options A/B/C in runbook section 0.**
  Per the SIARC standing-instructions discipline (no agent-side
  rule5 binding decisions; substrate-only routing for operator
  decisions), the agent surfaced 3 options + an "agent recommendation
  for economy" line (Option A) without forcing. Operator decides at
  the next CMB-edit session or W21 LANE-1 cadence.
- **J3: Phase F.1 mitigation rewrote 4 hits in production .md to
  neutral language; META-class blockquotes left as-is.** Followed
  the 069r1 + 075 J2 + 096 J1 precedent of rewriting non-META prose
  hits in-session. The rewrites preserve semantic content; the SHAs
  of runbook + post_deposit_followon updated post-mitigation
  (083-C4, 083-C7).
- **J4: Used 'Echizen Kubo, Mauricio' (Family, Given) form for the
  Zenodo creator name field per Zenodo convention; PDF metadata
  pdfauthor 'Mauricio Echizen Kubo' (Given Family) is a separate
  field that does not need to match.** Recorded as discrepancy D-4.
- **J5: Did NOT auto-fix the submission_log.txt missing-Zenodo-entries
  problem (May-2026 backfill of Items 11-16 covering CT/PCF-1/PCF-2/
  umbrella + D2-NOTE v2.0 + v2.1).** Out of scope for relay-083;
  the splice point in runbook §5 cites Item 11 as next-Item-number
  but with an explicit "Suggests routing v1.0 deposit splice as Item
  17 or later" caveat in U-2. A separate `submission-log-may-2026-
  zenodo-backfill` SQL todo is recommended in handoff §Recommended
  next step.

## Anomalies and open questions

**THIS IS THE MOST IMPORTANT SECTION. Read all 6 items.**

1. **STRUCTURAL SUPERSESSION (U-1, D-1).** D2-NOTE v2.0 + v2.1 are
   already deposited at concept DOI 10.5281/zenodo.19996689 (versions
   19996690 / 20015923). The v1.0 4-page draft this relay targets is
   a strict-subset pre-cursor by content. Depositing v1.0 NOW would
   create either an orphan-concept retroactive deposit (Option B
   archival) or no deposit at all (Option A drop). The operator must
   choose A/B/C in runbook section 0 BEFORE running web-form sections
   1-9. Agent recommends Option A for economy but does NOT pre-select.

2. **SUBMISSION_LOG MAY-2026 BACKFILL GAP (U-2).** `tex/submitted/
   submission_log.txt` has zero D2-NOTE entries despite v2.0 and
   v2.1 being on Zenodo for 3-4 days. SIX known May-2026 Zenodo
   deposits are entirely absent: D2-NOTE v2.0, D2-NOTE v2.1,
   CT v1.3, PCF-1 v1.3, PCF-2 v1.3, SIARC umbrella v2.0. The
   submission_log Zenodo sub-section currently ends at Item 10
   (T2B v3.0, 2026-04-30). If Option B is taken, the v1.0 splice
   entry should NOT be Item 11 -- it should land AFTER the May-2026
   backfill. Recommend `submission-log-may-2026-zenodo-backfill`
   todo. See discrepancy D-2 + unexpected find U-2.

3. **SUBMISSION_LOG SIZE/LC DISCREPANCY VS RELAY-062 COMMIT (D-3).**
   Relay-062 commit message claims pre/post sizes 60027 B / 60442 B
   and LC 1071 unchanged. Current state at 2026-05-07 is 17030 B /
   284 lines / SHA `2A28465A...4C617E45A`. Either the file was
   substantially shrunk between 2026-05-06 and 2026-05-07, or
   relay-062 hashed a different file path. The Item 22 JTNB
   rejection content from relay-062 IS present at the current file's
   L155-L158, so the 062 content edit landed; the size mystery is
   independent. Recommend git-blame on submission_log.txt as a
   follow-up audit.

4. **RELAY-083 DRAFTING APPEARS TO HAVE STALE V2.0 MEMORY (U-4).**
   Phase A.P3 of the relay reads "expected concept DOI 19996689 /
   version 19996690 per picture chain memory but may need
   confirmation". The hedge "may need confirmation" implies the
   prompt-drafter expected v2.0 to NOT yet be deposited at fire time;
   in fact v2.0 was deposited 3-4 days before fire and v2.1 was
   deposited 2-3 days before fire. Phase 0.2 supersession gate did
   not catch the gap because the SQL todo it references is the v1.0
   row, not the v2.0/v2.1 rows. NOT a halt; surfaced for synthesiser
   review at W21 LANE-1.

5. **AUTHOR NAME FORMAT MICRO-INCONSISTENCY (D-4).** d2_note.tex L60
   pdfauthor reads "Mauricio Echizen Kubo" (Given Family); the
   2026-05-02 Zenodo runbook section 2 used "Echizen Kubo, Mauricio"
   (Family, Given comma form). Both are valid; Zenodo convention is
   Family-comma-Given for the `name` field. Metadata.json uses the
   Family-comma-Given form to match prior runbook + Zenodo norm. No
   action.

6. **D2-NOTE V2.1 ARXIV CLASSIFICATION ADVISORY UNRATIFIED (U-3).**
   SQL todo `q-claude-30-31-send-d2-note-v21` is pending; agent
   advisory math.CA primary / math.NT cross-list NOT YET ratified by
   Claude.ai. The arXiv mirror flow for v2.1 is gated on that
   ratification. Decoupled from v1.0 deposit decision but recorded
   in `post_deposit_followon.md` Item D.1 + D.3.

## What would have been asked (if bidirectional)

- **Q1 (HIGHEST PRIORITY).** "The relay-083 prompt body says 'v2.0'
  but the SQL todo it closes is for v1.0, and v2.0 + v2.1 are already
  deposited at concept 19996689. Should the agent (a) produce v1.0
  deliverables per the SQL todo (the path taken), (b) produce v2.0/v2.1
  deliverables that document the existing deposits as substrate-only
  (no new Zenodo action), or (c) halt and re-fire 083 after operator
  amends the prompt?"
- **Q2.** "Is the v1.0 deposit (Option B) actually wanted, given v2.0
  is the canonical record at concept 19996689? An orphan-concept v1.0
  deposit creates two distinct Zenodo concept DOIs for the same paper
  family, which may complicate later cross-referencing. Recommend
  Option A unless there is a specific archival reason."
- **Q3.** "Should the May-2026 backfill of submission_log.txt
  (Items 11-16) be a relay-NN follow-up before this relay's Item NN
  splice can run, or should the v1.0 splice-as-Item-NN simply jump to
  Item 17 (or whatever comes after a backfill)?"

## Recommended next step

**Highest priority:** operator selects Option A / B / C on runbook
section 0. If Option A is selected, the only remaining action is the
SQL UPDATE in section 0 Option A block (~30 seconds). If Option B,
operator runs sections 4-8 of runbook (~5-10 min web-form upload).
If Option C, archive substrate-only.

**Secondary (recommended regardless of A/B/C):** dispatch a follow-up
relay (suggested ID `T1-SUBMISSION-LOG-MAY-2026-ZENODO-BACKFILL-NN`)
to splice the 6 missing May-2026 Zenodo deposits (CT v1.3, PCF-1 v1.3,
PCF-2 v1.3, SIARC umbrella v2.0, D2-NOTE v2.0, D2-NOTE v2.1) into
`tex/submitted/submission_log.txt` Items 11-16 in chronological order.
This unblocks any future Zenodo splice routing (including this relay's
Option B Item NN).

**Tertiary:** git-blame audit on `tex/submitted/submission_log.txt`
to resolve D-3 size discrepancy (60kB / 1071 lines per relay-062 vs
17kB / 284 lines current).

## Files committed

All paths relative to `siarc-relay-bridge/sessions/2026-05-07/T1-D2-NOTE-ZENODO-UPLOAD-RUNBOOK-083/`:

| File | SHA-256 (lowercase hex) | Size (B) | Class |
|---|---|---:|---|
| `zenodo_d2_note_metadata.json` | `a4cc28bb41240d490ff6c843933be2062c8fdb6ad859878f182c0c7fd4cc198f` |  8949 | Production |
| `zenodo_d2_note_runbook.md`    | `fed89fa561a9641b33177df0765ab46635e7a8d69487a142db97fe3b6cf2157d` | 16481 | Production |
| `post_deposit_followon.md`     | `75125cda25ff57cae43fadebba622d7d790c14489a37138c9d3d9bb6ccff9c8f` |  5946 | Production |
| `claims.jsonl`                 | `341a8b14a766025480f096408f95139160347119087fa263b2077d264d43d934` |  5917 | AEAL (7 entries) |
| `halt_log.json`                | `f1c56133743c7dc77d7953b7157d582e4254f6e9e9ecd744124cebb8016fb16f` |  2893 | AEAL |
| `discrepancy_log.json`         | `093dc307772bac79a403a31980a04938da9b87c8f4c20783ab7f3fbc92327f9e` |  5502 | AEAL (5 disc) |
| `unexpected_finds.json`        | `4abf29b7d7c85dedb73518e852687236445f27ded5760d252dd82f041c4911d5` |  5806 | AEAL (5 finds) |
| `handoff.md`                   | this file                                                            |   N/A | Final |

Total: 8 deliverables (3 production + 4 AEAL + 1 handoff).

## AEAL claim count

7 entries written to claims.jsonl this session (083-C1 through 083-C7).
Spec floor was >= 5 per HALT_083_AEAL_FLOOR; 7 recorded provides
+2 above floor (one per +substrate-anchor coverage of post_deposit_
followon.md SHA + supersession-state captured).
