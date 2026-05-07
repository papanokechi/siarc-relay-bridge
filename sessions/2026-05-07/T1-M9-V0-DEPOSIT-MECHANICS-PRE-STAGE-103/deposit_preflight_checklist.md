# Deposit pre-flight checklist -- M9 SIARC-MASTER-V0

**Task ID**: T1-M9-V0-DEPOSIT-MECHANICS-PRE-STAGE-103
**Fire date**: 2026-05-07
**Bridge HEAD at fire time**: 402c7de

This file produces a GO / NO_GO matrix for the M9 V0 announcement
Zenodo deposit. Each pre-condition has an evidence column (where to
look) and a recovery-path column (what to do if it fails).

The fire-time snapshot below is **NO_GO** by design -- the M4 + M6.CC
ratifications are scheduled for W21 LANE-1 Mon 2026-05-12 and
mid-week. NO_GO at fire time is the EXPECTED state. The operator
re-runs this checklist at deposit time (target W21 end Fri 2026-05-15)
and proceeds to deposit only after all rows flip to GO.

---

## Pre-conditions matrix

| # | Pre-condition | Evidence source | Fire-time state | Recovery if NO_GO |
|---|---|---|---|---|
| 1 | M4 ratification: 068 ACCEPT verdict from W21 LANE-1 (synth tier) | bridge `git log --oneline \| Select-String 068` and inspect verdict body | NO_GO (068 not landed; expected W21 LANE-1 Mon 2026-05-12) | Route to LANE-1 follow-up; if 068 lands ACCEPT_WITH_REVISIONS, address revision items first; if 068 lands REVISE, downgrade M9 to M9-V0-pre and defer |
| 2 | M6.CC R1-closure: 058 main-fire-V3 GO verdict | bridge `git log --oneline \| Select-String "058.*V3\|MAIN-FIRE-V3"` and inspect verdict body | NO_GO (069r1 NO_GO_SUBSTRATE_INSUFFICIENT at 601500b; 069r2 + 058 V3 still pending W21 mid-week) | If 058 V3 lands NO_GO, route to 069r2 retry path; if Path \u03b1 (analytic-guidance) blocked, switch to Path \u03b2 (literature acquisition Jimbo-Miwa 1981 / Conte-Musette 2008 / Forrester-Witte 2002 per 102 envelope) |
| 3 | P-008 SYNTH draft on disk OR substrate-equivalent on disk | search `tex/submitted/control center/synthesizer_inbox/` for `p008*` or `m9_v0_announcement*`; OR verify 096 phi_assignment_statement.md \u00a75 V0 announcement skeleton on bridge | PARTIAL (no on-disk P-008 draft; 096 \u00a75 V0 skeleton on bridge does cover the substrate per relay 103 envelope framing "P-008 SYNTH + 096 substrate pre-stage") | If at deposit time P-008 still has no on-disk draft, the operator can compose the deposit description from 096 phi_assignment_statement.md \u00a75 directly (this is the relay 103 fallback path and is supported by the metadata template's `__SLOT_DESCRIPTION__` slot) |
| 4 | 096 TIER-A substrate landed in bridge | `Test-Path siarc-relay-bridge/sessions/2026-05-07/T2-M9-V0-SUBSTRATE-PRE-STAGE-096/handoff.md` and verify SHA-16 4F31AC3026FB6C34 | GO (verified at fire time) | Re-fire 096 if file disappears (highly unlikely; bridge commits are immutable history) |
| 5 | Zenodo concept DOI ready to mint at deposit | Operator opens https://zenodo.org dashboard, signed in as `papanokechi` | GO (Zenodo dashboard accessible per RESUME L208-209) | If Zenodo dashboard unreachable, route to operator-side Zenodo support; deposit blocked until access restored |
| 6 | Operator ORCID + affiliation confirmed | ORCID `0009-0000-6192-8273` verified across 7 sources (submission_log L284, lean4/manuscript.tex L66, pcf2_program_statement.tex L40, bt_baseline_note.tex L74, etc.); affiliation `Independent researcher` consistent | GO (verified at fire time) | None needed; data is canonical |
| 7 | Cross-deposit DOIs verified (umbrella v2.0 + PCF-1 v1.3 + PCF-2 v1.3 + CT v1.3 + T2B v3.0 + D2-NOTE v2.1) | All 12 DOIs (6 concept + 6 version) verified via zenodo_upload_ct_v13_runbook.md L113-117 + RESUME L37-43 + zenodo_postpublish_edits_ct_v13.md L4-5 | GO (verified at fire time) | If any DOI fails to resolve at deposit time, drop from `related_identifiers` and surface in handoff Anomalies; deposit can proceed without 100% cross-link coverage |
| 8 | submission_log.txt structural integrity | `Test-Path tex/submitted/submission_log.txt` and verify SHA-16 + line count + Section-2 header `Recorded Submissions (https://zenodo.org/)` at L203 + `Note:` line at L280 | GO (verified at fire time; SHA-16 2A28465AE39BADF5; 17030 B; 284 lines) | If `Note:` line jumps by >5 from L280 by deposit time, manually re-locate splice window per submission_log_item_m9v0_template.txt drift-detection block |
| 9 | RESUME_AFTER_REBOOT_*.txt accessible | freshest `RESUME_AFTER_REBOOT_<YYYYMMDD>.txt` under `tex/submitted/control center/` | GO (RESUME_AFTER_REBOOT_20260502.txt verified at fire time; 22886 B; 344 lines; SHA-16 C3ED55B8EE0BBBFF) | If no RESUME file exists by deposit time, create fresh `RESUME_AFTER_REBOOT_<YYYYMMDD>.txt` with M9 V0 section as \u00a71 (per resume_update_m9v0_template.txt fallback note) |
| 10 | CMB.txt SYNTH-TRACK insertion convention valid | `Get-Content tex/submitted/CMB.txt -Tail 5` ends with the trailing 64-char `=` banner of the prior SYNTH-TRACK note | GO (verified at fire time; SHA-16 90020008A52325AC; 95983 B; 1757 lines; last note relay 081) | If CMB.txt structure has materially diverged by deposit time, fall back to "Notes:" section convention or open a new `## Note <DATE>` heading per cmb_notes_m9v0_template.md insertion-location section |

---

## GO / NO_GO computation rules

**GO** if ALL 10 rows = GO.

**NO_GO** if ANY row = NO_GO. Enumerate which rows are NO_GO and route
each to its recovery path. Do not proceed to deposit until all rows
flip to GO.

**PARTIAL_PROCEED** allowed only for row #3 (P-008 draft) when 096
\u00a75 substrate is in scope as the deposit substrate. Mark "PARTIAL"
in the row state and proceed; this is an intentional fallback that
the relay 103 envelope supports.

---

## Fire-time snapshot

| # | State |
|---|---|
| 1 | NO_GO (068 not landed) |
| 2 | NO_GO (058 V3 not landed; 069r1 NO_GO at 601500b) |
| 3 | PARTIAL (096 \u00a75 substrate covers; on-disk P-008 absent) |
| 4 | GO |
| 5 | GO |
| 6 | GO |
| 7 | GO |
| 8 | GO |
| 9 | GO |
| 10 | GO |

**Aggregate (fire time)**: NO_GO -- 2 rows blocking (rows 1 + 2).

This is the EXPECTED state at fire time. Both blocking rows are
scheduled to flip to GO during W21:
- Row 1 (M4): W21 LANE-1 Mon 2026-05-12 (synth-tier, ~30 min absorption)
- Row 2 (M6.CC): W21 mid-week Wed-Thu 2026-05-13/14 (after 069r2 + 058 V3 fire chain)

Once both flip GO, deposit window opens (target W21 end Fri 2026-05-15).

---

## Operator action sequence at deposit time

1. Re-run all 10 rows of the matrix above. Confirm aggregate state = GO.
2. Open `templates/zenodo_metadata_m9_v0.json`. Fill all `__SLOT_*__`
   fields per slot-fill notes inside the file.
3. Open Zenodo dashboard. Click "New upload" (or "New version" of an
   M9-pre concept if a v0.x preprint was staged earlier).
4. Upload `m9_v0_announcement.pdf` (and `.tex` source bundle if
   applicable). Paste filled metadata. Verify all `related_identifiers`
   resolve.
5. Click "Publish". Capture concept DOI + version DOI immediately.
6. Splice `tex/submitted/submission_log.txt` per
   `templates/submission_log_item_m9v0_template.txt`. Use the
   `Section 2 / Item N+1` insertion path.
7. Append `tex/submitted/control center/RESUME_AFTER_REBOOT_<YYYYMMDD>.txt`
   per `templates/resume_update_m9v0_template.txt`. Append as \u00a78
   "M9 SIARC-MASTER-V0 ANNOUNCEMENT -- DEPOSITED ...".
8. Append `tex/submitted/CMB.txt` SYNTH-TRACK note per
   `templates/cmb_notes_m9v0_template.md`. End-of-file append.
9. Commit + push to bridge. Capture commit short SHA. Backfill the
   short SHA into the three template artefacts above (replace
   `__DEPOSIT_BRIDGE_SHA__` with the captured short SHA).
10. Update SQL todos:
    - `siarc-master-v0` -> done
    - `siarc-umbrella-v2-1-dispatch` -> ready (next op)
    - `m13-categorical-coherence-followup` -> pending (M13 leg)

**Operator estimate**: 30-60 minutes total. With the templates +
checklist pre-staged, the deposit becomes a fill-in-the-slots
operation rather than a 2-3 hr scramble across 4 destination files.

---

## End of checklist
