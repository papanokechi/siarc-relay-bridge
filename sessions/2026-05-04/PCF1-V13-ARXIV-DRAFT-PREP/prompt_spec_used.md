# Prompt spec used — PCF1-V13-ARXIV-DRAFT-PREP

(No formal task spec received; operator clarification
2026-05-04 ~18:18-18:19 JST: "help with arxiv draft submission
... corresponding to the earlier endorsement request email to
Zudilin".)

## Inferred goal

Pre-stage the PCF-1 v1.3 arXiv submission package
(corresponding to the Zudilin endorsement request sent at
~18:12 JST per ZUDILIN-SEND-EVENT-LOG bridge commit
`65dd9aa`) so the operator has a verification-ready package
to start the arxiv.org/submit web-form draft at any time.

Note: starting the arXiv draft is the action that
**generates** the 6-character endorsement code that Zudilin
needs. The operator can start the draft NOW (independent of
Zudilin's reply); the draft sits at "awaiting endorsement"
until Zudilin enters the code.

## Inferred deliverables

1. **Verified pack** (TeX + PDF + abstract + 00README) with
   hash invariants matching the Zenodo deposit and the
   canonical 2026-05-01 source.
2. **Submission worksheet** with all metadata fields
   pre-formatted for copy-paste (title, authors, abstract,
   classification, license, DOI, comments, MSC).
3. **Click-through guide** for arxiv.org/submit web form.
4. **Endorsement-code follow-up email template** for
   forwarding the 6-character code to Zudilin once arXiv
   issues it.
5. **Post-submission cross-link checklist** (Zenodo related
   identifiers, submission_log update, CMB update).
6. Standard bridge artefacts (handoff, claims, halt log,
   discrepancy log, unexpected finds, prompt spec).

## Out of scope (per standing Rule 2 + RACI)

- Submitting on operator's behalf
- Forwarding the endorsement code to Zudilin on operator's
  behalf
- Modifying the .tex source (manuscript content frozen at
  v1.3 / 2026-05-01)
- Pre-staging packs for the other 4 arXiv-target records
  (umbrella, PCF-2, CT, T2B); deferred until their respective
  endorsements land.

## Halt conditions used

Halt-and-surface (no auto-fix) if:
- The pack PDF SHA-256 differs from the 034-audit-confirmed
  hash for record 19937196
- The TeX SHA-256 differs from the 030/034-manifest-confirmed
  canonical hash
- Title / authors / DOI in the worksheet metadata differ
  from values cross-checked against the .tex + Zenodo metadata

(None of these halt conditions triggered during execution.
One anomaly surfaced — DOI typo in original 00README — was
fixed in a NEW pack rather than overwriting the original, per
AEAL deposit-time-snapshot discipline.)

## Execution outcome

| Step | Outcome |
|---|---|
| Pack hash verification | ✓ TeX SHA-256 `e83bb377...` PASS; PDF SHA-256 `63420dbf...` PASS; both byte-equal to canonical / Zenodo per 034 audit |
| 00README DOI typo detection | ✓ Found PCF-2 DOIs (19941678/19963298) where PCF-1 DOIs (19931635/19937196) belonged |
| 00README correction | ✓ Fixed in new session's pack with explicit ERRATUM note; original preserved at ARXIV-PACK-V13-RE-VERIFY for AEAL provenance |
| Submission worksheet | ✓ 10-section consolidated copy-paste sheet (~13 KB) with hash verification commands, file-attach checklist, classification, metadata, web-form click-through, follow-up email template, post-submission checklist, halt conditions, provenance, out-of-scope |
| Follow-up email template | ✓ Section 6 of worksheet, with placeholders preserved per Rule 2 |
| Standard artefacts | ✓ All 6 bridge files emitted |

## Verdict

`COMPLETE_DRAFT_READY_FOR_OPERATOR_WEBFORM`

The operator has everything needed to begin the arxiv.org/submit
draft. No agent-side blockers; only operator-side actions
remain (web-form click-through + endorsement-code follow-up
email + Zudilin's response window).
