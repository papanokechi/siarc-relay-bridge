# Post-deposit follow-on checklist -- D2-NOTE v1.0

**Source:** relay-083 `T1-D2-NOTE-ZENODO-UPLOAD-RUNBOOK-083` Phase D.
**Scope:** operator-action items that are unblocked once the v1.0
Zenodo deposit lands (Option B path). If the operator selects
Option A (DROP) or Option C (DEFER) per `zenodo_d2_note_runbook.md`
section 0, this file is moot; archive as substrate-only.

---

## Items unblocked by v1.0 deposit

### Item D.1 -- Q-Claude-30 + Q-Claude-31 send (operator-action)

- **SQL todo:** `q-claude-30-31-send-d2-note-v21` (pending per
  `tex/submitted/control center/sql_todos_snapshot_2026-05-07_18-40-JST.md`
  L138).
- **Description (verbatim from snapshot):** "Send Q-CLAUDE-30 +
  Q-CLAUDE-31 to Claude (D2-NOTE v2.1 self-containment + arXiv
  classification)".
- **Substrate inputs to forward to Claude:** v2.1 PDF
  (`siarc-relay-bridge/sessions/2026-05-03/D2-NOTE-V2-1-WASOW-FULL-CLOSURE/d2_note_v2_1.pdf`),
  Phase A* (`phase_a_revalidation.md` same dir),
  `phase_c3_bt1933_verification.md`, `phase_b_newton_polygon_lemma.md`,
  and Wasow §19 chain references in `annotated_bibliography.bib`
  (same dir).
- **Agent advisory (per snapshot row, not yet ratified):** Q-Claude-31
  arXiv classification = `math.CA` primary / `math.NT` cross-list.
  Defer ratification to Claude (W21 LANE-1 cadence at the latest).
- **Coupling to v1.0 deposit:** v1.0 deposit (Option B) does NOT
  alter the v2.1 substrate; Q-Claude-30/31 questions are about v2.1
  content. v1.0 deposit only adds an orphan-concept historical record
  to cite if the operator wants explicit reference to the 2026-05-02
  4-page draft as a separate citable artefact.
- **Action sequence:** (1) operator opens Claude.ai chat; (2) attaches
  v2.1 PDF + Phase A* + Phase B + Phase C3 markdowns; (3) frames
  Q-Claude-30 (self-containment of v2.1 vs v1.0) + Q-Claude-31 (arXiv
  classification math.CA primary, math.NT cross-list, agent advisory);
  (4) records reply at `siarc-relay-bridge/sessions/2026-05-XX/D2-NOTE-Q-CLAUDE-30-31-VERDICT/`.

### Item D.2 -- Umbrella v2.1 dispatch (operator + relay agent)

- **SQL todo:** `siarc-umbrella-v2-1-dispatch` (pending per
  sql_todos_snapshot L162).
- **Description (verbatim from snapshot):** "Operator + relay agent:
  bump SIARC umbrella v2.0 -> v2.1 to cite D2-NOTE v2.1. Concept DOI
  for umbrella: 19965041. Triggered post-Zenodo-deposit-of-D2-NOTE-v2.1."
- **Coupling to v1.0 deposit (Option B):** v1.0 orphan-concept DOI is
  NOT cited by the umbrella; the umbrella v2.1 amendment cites the
  canonical v2.x record at concept 10.5281/zenodo.19996689. The v1.0
  orphan record is a parallel archival artefact, not a structural
  citation target. (If Option B description includes the historical
  preface paragraph as recommended, the umbrella should not mention
  the orphan v1.0 to avoid confusion.)
- **Action sequence:** (1) operator authorises relay-NN draft for
  umbrella v2.1 amendment; (2) draft amends umbrella .tex to add a
  one-line cross-reference to D2-NOTE v2.1 at version DOI
  10.5281/zenodo.20015923 in the §4.4 ξ₀-axis discussion; (3) operator
  deposits as version 2.1 on Zenodo umbrella concept DOI 19965041;
  (4) cross-link refresh on PCF-1 v1.3 / PCF-2 v1.3 / CT v1.3 / D2-NOTE
  v2.x / D2-NOTE v1.0-orphan-if-Option-B Related Identifiers (the
  optional `w20-zenodo-iscitedby-polish-cycle3` SQL todo).

### Item D.3 -- arXiv mirror submission for D2-NOTE (operator)

- **SQL todo:** none directly named for D2-NOTE arXiv mirror; closest
  is the per-record arXiv mirror runbook substrate at
  `siarc-relay-bridge/sessions/2026-05-04/ARXIV-MIRROR-RUNBOOK-REFIRE/`
  (relay 034 LANDED; see `picture_revised_20260507.md` L265 lineage).
  Per the relay-084 audit (`siarc-relay-bridge/sessions/2026-05-07/T1-084-AMEND-ARXIV-METADATA-AUDIT/`)
  Item 24 of the close-out matrix records D2-NOTE inclusion in the
  mirror set as `R5` or equivalent; status PENDING_FIRST_SUBMISSION
  (no arXiv ID has minted for any SIARC own-record per relay-084
  audit conclusion).
- **Coupling to v1.0 deposit (Option B):** the arXiv mirror is for
  D2-NOTE v2.1 (the canonical v2.x record), not v1.0. v1.0 orphan
  concept does not require a parallel arXiv submission; if the
  operator wants v1.0 visible on arXiv, that would be a separate
  v1.0-orphan arXiv submission with its own classification + endorser.
- **Action sequence:** unchanged from the relay-034 runbook chain;
  v1.0 deposit does not advance or block the v2.1 arXiv mirror flow.
- **Endorser status:** PCF-1 v1.3 endorser code DS873D pending
  Zudilin (declined) -> Garoufalidis (active per
  `garoufalidis-endorsement-pivot` SQL todo L210). For D2-NOTE v2.1
  arXiv classification math.CA primary, the endorser pool is
  separate from the math.NT pool used for PCF-1.

---

## Items NOT unblocked

These are recorded only for clarity. None depends on the v1.0
deposit (Option B) actually landing.

- `pcf2-v1-4-deposit-decision-q22-gated` (blocked on Q22 LANE-1
  ratification at relay-099 memo).
- `g17-layer-separation-amend-ct14` (decision territory; not deposit-
  blocked).
- `vquad-pIII-norm-map-close` / `vquad-pIII-normalization-map`
  (blocked on G3b acquisition or Q21 path-(b) arbitration).

---

## Items moot under Option A (DROP)

If the operator selects Option A on `zenodo_d2_note_runbook.md`
section 0, items D.1, D.2, D.3 above remain on their existing
schedules (none change). The only material effect of Option A is
that:

- SQL todo `zenodo-upload-d2-note` flips to `done` with a
  `superseded_by` note (per Option A SQL update in runbook §0).
- No new arxiv:NNNN.NNNNN identifier is minted for v1.0.
- No submission_log Item 11 is spliced.
- D2-NOTE-DRAFT bridge session at sessions/2026-05-02/ remains the
  v1.0 archival record (already on the SIARC bridge).

End of follow-on checklist.
