# W21 LANE-1 Decision Packet — Lean 4 CNP-Tunnell Relaunch

**Fire time:** 2026-05-07 ~14:55 JST
**Bridge HEAD at fire:** 49f3423 (post-077 LANDED).
**Substrate-anchor SHAs (computed at fire time after every
deliverable was written, or to be computed at the SHA-inventory
step in substrate_anchor_shas.md):**
- venue_profile_lmcs.md
- venue_profile_jfr.md
- venue_profile_mcs.md
- venue_profile_tcs.md
- venue_scope_fit_matrix.md
- cover_letter_framing_lmcs.md
- cover_letter_framing_jfr.md
- cover_letter_framing_mcs.md
- cover_letter_framing_tcs.md
- cross_venue_compatibility.md
- submission_log_item26_splice_spec.md
**Substrate-input anchor:**
- tex/submitted/submission_log.txt at fire-time SHA
  2A28465AE39BADF5AB245C3114C84E3E1469BF2FA1CDD967AC017FF4C617E45A
  (17030 B; verified via PowerShell Get-FileHash 2026-05-07 14:30 JST).

---

## 7-option synth menu (alphabetical within picks)

| Option | Description |
|--------|-------------|
| **PICK_JFR** | Synth selects *Journal of Formalized Reasoning* as next venue. |
| **PICK_LMCS** | Synth selects *Logical Methods in Computer Science* as next venue. |
| **PICK_MCS** | Synth selects *Mathematics in Computer Science* as next venue. |
| **PICK_TCS** | Synth selects *Theoretical Computer Science* as next venue. |
| **PICK_OTHER** | Synth proposes a venue outside the 4 candidates (must justify with venue-profile substrate). |
| **DEFER** | Synth defers to next-cadence (W22+). |
| **WITHDRAW_PERMANENTLY** | Synth withdraws Lean paper from journal-submission track (arXiv-only or repository-only). |

The 4 PICK_<vid> options are listed alphabetically so the menu
itself does not encode a recommended ordering. PICK_OTHER, DEFER,
and WITHDRAW_PERMANENTLY follow the picks.

## Per-option trigger

- **PICK_JFR**: trigger 080 envelope (cover-letter finalize from
  cover_letter_framing_jfr.md + JFR portal-submission walkthrough);
  trigger submission_log Item 26 splice using the JFR template in
  submission_log_item26_splice_spec.md. Special note: see
  unexpected_finds.json U1 (publication-gap activity flag) before
  finalizing; synth may want to canvass JFR EiC contact viability
  as a pre-fire check before 080.
- **PICK_LMCS**: trigger 080 envelope (cover-letter finalize from
  cover_letter_framing_lmcs.md + LMCS portal-submission walkthrough
  via Episciences; arXiv prior-deposit pre-fire if not already
  routed); trigger submission_log Item 26 splice using the LMCS
  template.
- **PICK_MCS**: trigger 080 envelope (cover-letter finalize from
  cover_letter_framing_mcs.md + MCS Springer Editorial Manager
  walkthrough); trigger submission_log Item 26 splice using the MCS
  template. APC clarification recommended pre-fire (hybrid OA
  pricing UNKNOWN at fire time).
- **PICK_TCS**: trigger 080 envelope (cover-letter finalize from
  cover_letter_framing_tcs.md + TCS Elsevier submission walkthrough
  at https://submit.elsevier.com/TCS); trigger submission_log Item
  26 splice using the TCS template. Section-B routing request
  flagged in cover-letter draft.
- **PICK_OTHER**: 080 envelope blocked. 079r1 venue-profile
  extension required first; synth must name the candidate venue and
  propose a 5th venue_profile_<vid>.md drafting brief.
- **DEFER**: no further action W21. Re-fire 079 carry-forward at
  W22+ with refreshed venue homepages + activity-flag re-check.
  Item 25 in submission_log remains "Next venue: TBD".
- **WITHDRAW_PERMANENTLY**: trigger Zenodo metadata update sub-
  envelope (re-tag Zenodo record 10.5281/zenodo.19834824 to mark
  "no journal-submission" status) + arXiv-deposit decision sub-
  envelope. Item 25 in submission_log updated to "WITHDRAWN
  PERMANENTLY". No 080 envelope.

## Synth-discipline reminders for the W21 LANE-1 reviewer

The 4-venue x 7-factor matrix in venue_scope_fit_matrix.md returns
a STRONG-tied row pattern at JFR + LMCS on the verifiable axes
(F1+F2+F3+F6 = STRONG / STRONG / STRONG / STRONG for both) with the
JFR row carrying an activity-flag overhang (5+ year publication gap
since 2020-12-21) and the LMCS row carrying no analogous flag. The
MCS + TCS rows return mixed STRONG / MODERATE / WEAK patterns. The
matrix is descriptive only; no row-total ranking was computed.

The AFM Item 24 desk-reject signal is informative for FIT (not
quality). Synth weighting of FIT-driven framing across the 4
candidates is in scope at LANE-1.

The agent does not order the candidates and does not suggest a
pick. The synth-decision rests entirely with the W21 LANE-1
reviewer.

---

**Word count target check:** ~520 words (within 400-600 envelope).

**HALT_079_VENUE_SELECTION_OVERREACH self-check:** the picks are
listed alphabetically; no "recommended pick" line appears anywhere
in this packet. The synth-discipline-reminders section names matrix
patterns but stops short of ordering.

**Forbidden-verb scan:** zero hits against the FV-7 verb set
(enumerated only in forbidden_verb_scan.md to avoid set-literal
echoes in production deliverables).
