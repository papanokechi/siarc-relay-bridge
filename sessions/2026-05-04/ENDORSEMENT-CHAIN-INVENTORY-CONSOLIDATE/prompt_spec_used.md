# Prompt spec used — ENDORSEMENT-CHAIN-INVENTORY-CONSOLIDATE

(Verbatim of operator-dispatched spec 2026-05-04 ~17:59 JST.)

```
TASK: ENDORSEMENT-CHAIN-INVENTORY-CONSOLIDATE
TASK CLASS: data consolidation (pre-sequencing inventory)
PARALLEL-SAFE WITH: any task NOT touching the 037 endorsement
                    templates folder or the submission_log
COMPUTE: minimal (~5-10 min; pure file reads + table emission;
         no external API calls)
BRIDGE: sessions/2026-05-04/ENDORSEMENT-CHAIN-INVENTORY-CONSOLIDATE/

§0 CONTEXT
  Operator-side decision pending: which of the 5 arXiv-target
  records leads the endorsement-request chain. Per arXiv policy
  update 2025-12-10, auto-endorsement requires (1) institutional
  email AND (2) prior arXiv math authorship; operator meets
  neither. All 5 records require personal endorsement. The 037
  session emitted 9 templates; combined with 034's 6, the bridge
  has 15 total. First endorsement is strategically load-bearing.
  This task is pure inventory consolidation: aggregate metadata
  for synthesizer/operator-side sequencing review. NO Zenodo
  API calls. NO download/view metric pulls. NO endorser ranking.

§1 ANCHOR FILES
  - tex/submitted/control center/RESUME_AFTER_REBOOT_20260502.txt
  - tex/submitted/submission_log.txt
  - siarc-relay-bridge/sessions/2026-05-04/ARXIV-MIRROR-RUNBOOK-REFIRE/
  - siarc-relay-bridge/sessions/2026-05-04/ARXIV-ENDORSEMENT-TEMPLATES-EXPAND/

§2 STEPS
  1. Read 5 records from submission_log ZENODO section.
  2. Cross-check PCF-1 concept-vs-version DOIs across 3 sources
     (HALT_ENDORSEMENT_INVENTORY_DOI_INCONSISTENCY if mismatch).
  3. Enumerate 15 templates from 034 + 037
     (HALT_ENDORSEMENT_INVENTORY_TEMPLATE_COUNT_MISMATCH if !=15).
  4. Read fit ratings from 037 subject_fit_matrix.md; report
     034's matrix separately.
  5. Critical: check Zudilin template for stale Newcastle address.
  6. Filename consistency check: PCF-1 vs PCF-2 in Zudilin
     template body.
  7. Emit portfolio_inventory.md with master 5-row table +
     anomaly notes + operator decision prompt (no synthesizer
     recommendation; data-pull only).
  8. Append AEAL claims (4 spec-required + 1+ per anomaly).
  9. Standard bridge artefacts.
  10. git commit + push.

§3 HALT IF
  - HALT_ENDORSEMENT_INVENTORY_DOI_INCONSISTENCY
  - HALT_ENDORSEMENT_INVENTORY_TEMPLATE_COUNT_MISMATCH
  - HALT_ENDORSEMENT_INVENTORY_034_037_MISSING

§4 OUT OF SCOPE
  - Zenodo API calls / download/view metrics
  - Sequencing recommendation (operator data-pull-only request)
  - Endorser ranking
  - Drafting any new endorsement emails
  - Modifying any 034 or 037 artefact (read-only)
  - Sending any endorsement email

§5 STANDING FINAL STEP — output BRIDGE / CLAUDE_FETCH / VERDICT /
   ANOMALIES / STRATEGIC_IMPLICATION / TEMPLATE_COUNT /
   POST_DEC2025_POLICY_ACKNOWLEDGED / STALE_ADDRESS_FLAGS /
   FILENAME_ANOMALIES.
```

(Full spec preserved in operator-dispatch chat record 2026-05-04 ~17:59 JST.)

## Execution outcome

| Step | Outcome |
|---|---|
| 1. Read 5 records | ✓ All 5 records read from `submission_log.txt` ZENODO section + `RESUME_AFTER_REBOOT_20260502.txt` cheat-sheet lines 38-44 + 034 `zenodo_metadata_5_records.json`. |
| 2. DOI cross-check (3 sources) | ✓ PASS — all 10 DOIs (5 records × {concept, version}) consistent across all 3 sources. No `HALT_ENDORSEMENT_INVENTORY_DOI_INCONSISTENCY`. |
| 3. Template count = 15 | ✓ PASS — 6 from 034 + 9 from 037 = 15 exact. No `HALT_ENDORSEMENT_INVENTORY_TEMPLATE_COUNT_MISMATCH`. |
| 4. Fit rating extraction | ✓ 037 explicit (subject_fit_matrix.md): 6H+3M+0L on umbrella+CT+T2B. 034 implicit (math.NT primary aligned with all 3 endorsers): 6H+0M+0L on PCF-1+PCF-2. Combined: 12H+3M+0L; no L cells. |
| 5. Zudilin Newcastle check | NEGATIVE (premise falsified) — both Zudilin templates use placeholder pattern; zero `newcastle` matches. `STALE_ADDRESS_FLAGS=0`. |
| 6. Filename consistency | NEGATIVE (no anomaly) — 15/15 templates have body DOI matching filename label; the spec's "single Zudilin template" framing was based on synthesizer-misread of 034 inventory (which contains BOTH PCF-1 and PCF-2 Zudilin templates). `FILENAME_ANOMALIES=0`. |
| 7. Emit portfolio_inventory.md | ✓ 14,560 B at session root. |
| 8. AEAL claims | ✓ 7 claims (spec required ≥4; emitted 6 standard + 1 fit-distribution observation). |
| 9. Standard bridge artefacts | ✓ handoff.md, halt_log.json (`{}`), discrepancy_log.json (`{}`), unexpected_finds.json (`{}`), prompt_spec_used.md (this file). |
| 10. git commit + push | (executed by agent following this file's emission). |

No halts triggered. Both spec-expected anomalies (Newcastle
address, filename PCF-1/PCF-2) returned NULL findings — i.e.,
the synthesizer's defensive premises were over-conservative
and the artefacts were already clean. Both null findings are
recorded in `claims.jsonl` (`zudilin_address_stale_newcastle_NULL_finding`
+ `template_filename_body_consistency_15_of_15`).

## Out of scope (per spec §4)

Agent did NOT:
- Make any Zenodo API calls or download/view metric pulls
- Recommend any sequencing order
- Rank endorsers or recommend first-contact
- Draft any new endorsement emails (existing 15 templates suffice)
- Modify any 034 or 037 artefact (all reads were read-only)
- Send any endorsement email

All six are operator-side or separate-task scope.
