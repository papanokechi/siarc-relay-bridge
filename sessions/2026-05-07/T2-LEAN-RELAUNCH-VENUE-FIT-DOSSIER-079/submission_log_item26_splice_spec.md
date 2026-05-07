# submission_log Item 26 Splice Spec (CONTINGENT)

**Fire time:** 2026-05-07 ~14:55 JST
**Status at fire:** SPEC ONLY. The actual edit of
`tex/submitted/submission_log.txt` fires at the W21+ post-pick
action, NOT at this T2 stage.
**Substrate-anchor:** `tex/submitted/submission_log.txt` at fire-
time SHA `2A28465AE39BADF5AB245C3114C84E3E1469BF2FA1CDD967AC017FF4C617E45A`
(17030 B; verified via PowerShell Get-FileHash 2026-05-07 14:30
JST).

---

## Splice plan

- **Target file:** `tex/submitted/submission_log.txt`.
- **Insertion point:** the new entry is appended after the current
  Item 25 block. The Item-25 block presently terminates at the
  approximate line range surfaced in submission_log.txt around
  L201 (the "OPEN QUESTION RESOLVED 2026-05-07 ~12:46 JST" line)
  + the trailing blank line. The exact target-after-line number
  must be re-computed at apply time against the live-tree
  submission_log.txt; a stale line-number anchor at this T2 stage
  would risk silent-drift (precedent: 060 OQ-paste exact-line spec
  required draft-time re-verification).
- **Item number:** **26** (next sequential after Item 25). The
  HALT_079_NUMBERING_OVERREACH discipline forbids any other number;
  the splice spec lists 26 only.

## 7 placeholder fields (all 4 PICK templates share schema)

The Item 26 entry follows the same 7-field schema as Items 22-25:

```
26. Filename: <FILENAME_PLACEHOLDER>
   Title: A Layered, Axiom-Isolated Lean 4 Formalization of the Congruent Number Problem up to Tunnell's Criterion
   Status: <STATUS_PLACEHOLDER>
   Submitted on: <DATE_PLACEHOLDER>
   Submission ID: <SUBMISSION_ID_PLACEHOLDER>
   Handling editor: <HANDLING_EDITOR_PLACEHOLDER>
   Verdict: <VERDICT_PLACEHOLDER>
   Notes: GitHub: github.com/papanokechi/tunnell-cnp-lean4
          Zenodo: 10.5281/zenodo.19834824
          Cover letter: <COVERLETTER_SHA_PLACEHOLDER>
          Prior venue history (carry-forward from Item 24 + Item 25): JAR (rejected for length), FAC (defunct), AFM Item 24 (afm:18102; DESK REJECTED ~8 min post-submission by editorial-board signed by Filippo Alberto Edoardo Nuccio Mortarino Majno di Capriglio; no review, no rationale, no handling-editor involvement; verdict notification re-sent 2026-05-07 ~12:46 JST), JAR-Elsevier withdrawal Item 25 (multidisciplinary scope-fit reassessment; cancellation 2026-05-07).
          Multi-submission policy: SINGLE-CHANNEL (this is the only active dispatch for this manuscript).
```

The 7 placeholders are: FILENAME / STATUS / DATE / SUBMISSION_ID /
HANDLING_EDITOR / VERDICT / COVERLETTER_SHA. Title + GitHub +
Zenodo + Multi-submission disclosure are constants; Prior-venue-
history line is also a constant (carry-forward from Items 24 + 25).

## 4 candidate venue-fill templates (one per LMCS/JFR/MCS/TCS)

### PICK_LMCS

```
   Filename: tunnell_lmcs_R1.pdf
   Status: Submitted to Logical Methods in Computer Science (LMCS, Episciences; diamond OA)
   Submitted on: <DATE>
   Submission ID: <LMCS_ID; typically lmcs:NNNNN format per Episciences convention>
   Handling editor: <to be assigned>
   Verdict: pending
   Cover letter: <SHA-256 of finalized cover_letter_lmcs.tex at apply time>
```

### PICK_JFR

```
   Filename: tunnell_jfr_R1.pdf
   Status: Submitted to Journal of Formalized Reasoning (JFR, UniBO; diamond OA, free APC)
   Submitted on: <DATE>
   Submission ID: <JFR_ID; OJS-assigned>
   Handling editor: <to be assigned>
   Verdict: pending
   Cover letter: <SHA-256 of finalized cover_letter_jfr.tex at apply time>
```

### PICK_MCS

```
   Filename: tunnell_mcs_R1.pdf
   Status: Submitted to Mathematics in Computer Science (MCS, Birkhauser/Springer; hybrid OA)
   Submitted on: <DATE>
   Submission ID: <MCS_ID; Springer Editorial Manager assigned>
   Handling editor: <to be assigned>
   Verdict: pending
   Cover letter: <SHA-256 of finalized cover_letter_mcs.tex at apply time>
   APC note: hybrid OA APC clarification at submission time required before any conditional-acceptance gold-track election.
```

### PICK_TCS

```
   Filename: tunnell_tcs_R1.pdf
   Status: Submitted to Theoretical Computer Science (TCS, Elsevier; hybrid OA; Section B routing requested)
   Submitted on: <DATE>
   Submission ID: <TCS_ID; Elsevier-assigned>
   Handling editor: <to be assigned>
   Verdict: pending
   Cover letter: <SHA-256 of finalized cover_letter_tcs.tex at apply time>
   Section routing: Logic and Semantics (Section B) requested in cover letter.
```

### PICK_OTHER + DEFER + WITHDRAW_PERMANENTLY

These 3 variants of the synth menu do not produce an Item 26
splice. PICK_OTHER triggers a 5th venue_profile draft instead.
DEFER leaves Item 25 unmodified ("Next venue: TBD"). WITHDRAW_
PERMANENTLY triggers a separate update to Item 25 (Status flip to
"WITHDRAWN PERMANENTLY") rather than a new Item 26.

## Apply-time discipline

When (and only when) the synth pick lands at W21+:

1. Re-compute the live-tree SHA-256 of submission_log.txt at apply
   time. The fire-time SHA above must NOT be re-used at apply time
   if other edits have landed between W20-Wed and W21+.
2. Recompute the exact target-after-line number against the live
   tree (precedent: 060 + 062 OQ-paste line-number drift).
3. Apply the chosen PICK template by replacing the 7 placeholders
   with concrete values + finalized cover-letter SHA.
4. Run a post-paste invariant suite (line-count delta + SHA change
   + token-uniqueness scan + tail-line check) before commit.

---

**HALT_079_NUMBERING_OVERREACH self-check:** the splice spec
proposes Item 26 only. No other Item-number variant is offered.

**HALT_079_VENUE_SELECTION_OVERREACH self-check:** the 4 PICK
templates are listed alphabetically (LMCS / JFR / MCS / TCS — note:
LMCS appears first alphabetically in this list because of "L" vs
"J"). Wait, alphabetical-by-acronym would order JFR / LMCS / MCS /
TCS. The list above re-orders to match the relay-prompt LMCS / JFR
/ MCS / TCS sequence, which is the substrate-prompt convention
(NOT a rank). Operator may re-sort to alphabetical-by-acronym
without semantic change.

**Forbidden-verb scan:** zero hits against the FV-7 verb set
(enumerated only in forbidden_verb_scan.md to avoid set-literal
echoes in production deliverables).
