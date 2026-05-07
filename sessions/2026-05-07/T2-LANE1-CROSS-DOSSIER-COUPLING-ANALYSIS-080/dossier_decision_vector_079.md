# Dossier Decision Vector — 079 (Lean Relaunch Venue Fit)

**Dossier ID:** [DOSSIER-079]
**Title:** T2-LEAN-RELAUNCH-VENUE-FIT-DOSSIER-079
**Source decision packet:** `w21_lane1_lean_relaunch_decision_packet.md`
  (SHA `B4980C0A98C8FFD4…`, 5097 B, 92 lines)
**Source handoff:** `handoff.md`
  (SHA `FEA8194B9C3D96F8…`, 10025 B, 188 lines)
**Bridge landing commit:** `72f9850`
**Verdict tag (verbatim, ≤ 50 words):**

> "Status: COMPLETE … All 9 envelope halts return PASS; all 4
>  venue identifiers were live-pre-verified before fire (post-031
>  rule applied); the W21 LANE-1 synth menu emits 7 options
>  alphabetically without recommended-pick."

(38 words; from `handoff.md` §"What was accomplished" /
§"Status" excerpts, concatenated; ≤ 50-word ceiling PASS.)

---

## §1 — Identifier + provenance

[DOSSIER-079] is the post-AFM-desk-reject Tunnell-CNP Lean 4
manuscript relaunch venue-fit dossier covering 4 candidate venues
(LMCS / JFR / MCS / TCS), per-venue profiles, 4 × 7 scope-fit
matrix, 4 cover-letter framings, cross-venue compatibility, and
Item-26 splice spec; emits a 7-option synth menu for W21 LANE-1.

## §2 — Verdict tag (verbatim from handoff)

> "DOSSIER_COMPLETE" (handoff §"Status" line; alternative wording
> per relay-079 envelope; from commit message at bridge `72f9850`.)

## §3 — Menu-option enumeration table

The 7 options enumerated verbatim in
`w21_lane1_lean_relaunch_decision_packet.md` "7-option synth menu":

| Option-tag | Structural-summary (verbatim ≤ 30 words) | Operator-OOB-gates | Operator-pre-flight gates | Synth-blocking conditions |
|---|---|---|---|---|
| `PICK_JFR` | "Synth selects *Journal of Formalized Reasoning* as next venue." | JFR EiC contact viability check (per U1 publication-gap activity flag) | activity-flag re-check at 080 finalize | U1 5+ year publication gap |
| `PICK_LMCS` | "Synth selects *Logical Methods in Computer Science* as next venue." | none | arXiv prior-deposit pre-fire if not already routed; LMCS Episciences portal walkthrough | none beyond standard portal walkthrough |
| `PICK_MCS` | "Synth selects *Mathematics in Computer Science* as next venue." | APC clarification (hybrid OA pricing UNKNOWN) | MCS Springer Editorial Manager walkthrough | D4 Springer auth-gate information gap |
| `PICK_TCS` | "Synth selects *Theoretical Computer Science* as next venue." | USD 2,840 gold-OA APC; Section-B routing request | TCS Elsevier submission walkthrough | D1 APC; D3 turnaround-metric ambiguity |
| `PICK_OTHER` | "Synth proposes a venue outside the 4 candidates (must justify with venue-profile substrate)." | 079r1 venue-profile extension required | synth names candidate venue + 5th venue_profile drafting brief | 080 envelope blocked until 079r1 lands |
| `DEFER` | "Synth defers to next-cadence (W22+)." | none in W21; refresh venue homepages at re-fire | W22+ refresh of activity-flag re-check | named-event resolution |
| `WITHDRAW_PERMANENTLY` | "Synth withdraws Lean paper from journal-submission track (arXiv-only or repository-only)." | Zenodo metadata update sub-envelope (re-tag record 10.5281/zenodo.19834824); arXiv-deposit decision sub-envelope | Item 25 in submission_log updated to 'WITHDRAWN PERMANENTLY' | no 080 envelope; permanent-track decision |

## §4 — PARTIAL / AMBIGUOUS-option flag-set

- `PICK_JFR` carries U1 publication-gap activity flag (5+ year gap
  since 2020-12-21; editorial board current per fetch); D5 row-
  symmetry with LMCS on verifiable axes per §"Anomalies".
- `PICK_LMCS` carries D2 DOAJ-listing not directly confirmed
  during pre-fire web-fetch.
- `PICK_MCS` carries D4 Springer auth-gate information gap (5 of
  7 scope-fit cells reflect this gap).
- `PICK_TCS` carries D1 (highest APC), D3 (turnaround ambiguity),
  U2 (Section-B routing strategic question).
- `PICK_OTHER` requires 079r1 + 5th venue profile.
- `DEFER` defers to W22+ by definition.
- `WITHDRAW_PERMANENTLY` is the irreversible-track option; flagged
  for synth-only consideration per spec.

## §5 — [NULL_DEFAULT] declaration

The 079 packet §"7-option synth menu" asserts: "The 4 PICK_<vid>
options are listed alphabetically so the menu itself does not
encode a recommended ordering. … The agent does not order the
candidates and does not suggest a pick. The synth-decision rests
entirely with the W21 LANE-1 reviewer."

Recorded as [NULL_DEFAULT].

## §6 — Option count + category breakdown

- Total options: 7
- Categories:
  - `PICK-venue-class`: 5 (`PICK_JFR`, `PICK_LMCS`, `PICK_MCS`,
    `PICK_TCS`, `PICK_OTHER`)
  - `DEFER-class`: 1 (`DEFER`)
  - `WITHDRAW-class`: 1 (`WITHDRAW_PERMANENTLY`)
- Operator-OOB-gates active on: `PICK_JFR` (EiC viability check),
  `PICK_MCS` (APC clarification), `PICK_TCS` (APC + Section-B
  routing), `PICK_OTHER` (079r1), `WITHDRAW_PERMANENTLY` (Zenodo
  + arXiv sub-envelopes).
- Operator-pre-flight gates active on: `PICK_LMCS` (arXiv prior-
  deposit), all 4 PICK_<vid> options (portal walkthroughs +
  cover-letter trim per J1 ~225–230 vs 150–220 envelope target).
- Scope-fit matrix totals (4 venues × 7 axes = 28 cells): 11
  STRONG, 6 MODERATE, 1 WEAK, 10 UNKNOWN.

---

## §7 — Cross-coupling indicators (substrate anchors only)

Anchors from `w21_lane1_lean_relaunch_decision_packet.md`
"Per-option trigger" + handoff §"Recommended next step":

- [COUPLING-ANCHOR-079a] Each PICK_<vid> triggers an 080 envelope
  (cover-letter finalize from corresponding `cover_letter_framing_
  <vid>.md` + venue portal walkthrough) per "Per-option trigger"
  block.
- [COUPLING-ANCHOR-079b] Each PICK_<vid> triggers a
  submission_log Item 26 splice using the corresponding template
  in `submission_log_item26_splice_spec.md`; couples to
  submission_log.txt edit at 080+ dispatch (out of 080 scope).
- [COUPLING-ANCHOR-079c] Lean paper is NOT in the 077 paper-profile
  inventory (077 covers 6 SIARC-track papers; Lean / Tunnell-CNP
  is separate per [COUPLING-ANCHOR-077h]); 079 venue-fit decision
  is therefore decoupled from 077 portfolio bundle pick at the
  paper-set level.
- [COUPLING-ANCHOR-079d] Lean paper is NOT in the 078 endorser-
  paper coverage matrix (078 covers the 6 SIARC papers; Lean is
  out-of-scope per [COUPLING-ANCHOR-078c]); 079 venue dispatch
  does not couple to 078 endorser pivot.
- [COUPLING-ANCHOR-079e] `WITHDRAW_PERMANENTLY` triggers Zenodo
  metadata update on record 10.5281/zenodo.19834824 — this is the
  Lean paper's existing Zenodo deposit, separate from the 6
  SIARC-track DOIs in 077.
- [COUPLING-ANCHOR-079f] AFM Item 24 desk-reject signal is "informa-
  tive for FIT (not quality)" per packet §"Synth-discipline
  reminders"; couples to cover-letter framing across the 4
  candidates but not to portfolio bundle pick.

---

End of `dossier_decision_vector_079.md`.
