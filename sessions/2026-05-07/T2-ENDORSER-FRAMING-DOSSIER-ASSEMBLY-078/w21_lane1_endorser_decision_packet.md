# W21 LANE-1 Endorser-Pivot Decision Packet [DECISION-PACKET] — 078

**Session:** T2-ENDORSER-FRAMING-DOSSIER-ASSEMBLY-078
**Compiled:** 2026-05-07
**Cadence target:** W21 LANE-1 Mon 2026-05-12 AM JST (per spec §6.F.1)
**Spec reference:** §6 SYNTHESIZER DECISION PACKET.

> **Format note.**  This file is a synthesizer-ready dispatch packet,
> formatted as the body of a future synth-prompt asking T1-Synth to
> identify which endorser-paper pair(s) the operator will approach.
> Per spec §6.F.2 +
> §8 HALT_078_ENDORSER_SELECTION_OVERREACH, this packet does NOT
> assert any endorser-paper assignment; it only surfaces coverage
> matrix + reframing-distance tags + handle-preverification status
> for the synthesizer's consumption.

---

## §F.1 — Decision request title

**Endorser-pivot decision request (W21 LANE-1).**

This is a decision request for the **synthesizer** (T1-Synth)
addressed to the operator, with paste-ready synth-track
formatting.  The agent prepared the substrate; the synthesizer
decides which endorser-paper pair(s) move forward at W21 LANE-1.

## §F.2 — Reference to the 078 dossier

Bridge URL (post-commit):
`https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-05-07/T2-ENDORSER-FRAMING-DOSSIER-ASSEMBLY-078/`

Key dossier deliverables:
- `endorser_paper_coverage_matrix.md` — 6 × 6 cell matrix (5
  active rows + Zudilin historical anchor)
- `endorser_profile_*.md` (×6) — per-endorser substrate readback
  with verbatim 2026-05-04 dossier anchors
- `tier2_handle_preverification.md` — HANDLE_404 status for
  Costin / Sauzin / Beukers
- 5 gap-templates: `endorsement_request_pcf2_mazzocco.md`
  (G1, MEDIUM), `endorsement_request_pcf2_garoufalidis.md`
  (G2, LIGHT, optional), `endorsement_request_d2note_sauzin.md`
  (G3, LIGHT-MEDIUM), `endorsement_request_d2note_costin.md`
  (G4, MEDIUM), `endorsement_request_t2b_beukers.md`
  (G5, MEDIUM)

## §F.3 — Coverage matrix summary

5 active endorser rows × 6 papers = 30 cells (Zudilin sixth row
HISTORICAL-ANCHOR).  Tag distribution across the 5 active rows:

- **EXISTING-TEMPLATE-ON-DISK**: 7 unique pairs (3 × CT v1.3 +
  3 × T2B v3.0 + 1 × umbrella v2.0 by Mazzocco/Garoufalidis +
  PCF-1 × Garoufalidis pivot in flight + 3 × umbrella).  Note
  that "existing template" file count on disk is 14 (counting
  duplicate CT files across 034 + 037 folders) per `endorser_substrate_anchor_shas.md` §A.1+§A.2.
- **GAP-CANDIDATE drafted in 078**: 5 (G1-G5 listed above).
- **SKIP-FIT-WEAK**: 18 cells (off-axis pairs with weak
  subject-fit per 2026-05-07 reverse-engineering pairing per
  spec §2.B.3).
- **SKIP-DECLINED-INHERIT**: 0 active-row cells (Zudilin row is
  HISTORICAL-ANCHOR; PCF-1 SKIP-DECLINED + PCF-2 inherit-decline
  is recorded in Zudilin row only).

Detailed cell-by-cell rationale: see
`endorser_paper_coverage_matrix.md` §C.3.

## §F.4 — Tier-2 handle pre-verification status

| Endorser | Standard slug | Resolution status | Verdict |
|---|---|---|---|
| Costin | `costin_o_1` | HTTP 404 (anchor 2026-05-04) | HANDLE_404 |
| Sauzin | `sauzin_d_1` | HTTP 404 (anchor 2026-05-04) | HANDLE_404 |
| Beukers | `beukers_f_1` | HTTP 404 (anchor 2026-05-04) | HANDLE_404 |

All 3 Tier-2 endorsers require operator OOB handle recovery before
their respective gap-templates (G3 Sauzin / G4 Costin / G5 Beukers)
can be sent.  Beukers additionally has an emeritus-eligibility gate
per spec §5.E.3 verbatim recall.  Per `tier2_handle_preverification.md`
§E.5 the dossier carries a **DOSSIER_PARTIAL** tag specifically for
these 3 endorsers.

## §F.5 — Reframing-distance summary (verbatim from spec §2.B.3, ~25 words)

> "Mazzocco | PCF-2 v1.3 | MEDIUM
>  Garoufalidis | PCF-1 v1.3 | LIGHT (in flight)
>  Costin | D2-NOTE v2.1 | MEDIUM
>  Sauzin | D2-NOTE v2.1 | LIGHT-MEDIUM
>  Beukers | PCF-1 + T2B v3.0 | MEDIUM"

## §F.6 — Decision request

The synthesizer is asked to mark one or more of the following
options, with multi-mark possible (per spec §6.F.1 ladder).  No
agent-side endorser-paper assignment is asserted (HALT_078_ENDORSER_SELECTION_OVERREACH
discipline applied; agent surfaces only).

Options enumerated:

  - **APPROACH_PCF2_MAZZOCCO** — operator sends G1 template
    (`endorsement_request_pcf2_mazzocco.md`); Mazzocco is the
    only Tier-1 endorser whose email is VERIFIED (per memory
    `endorsement workflow`); reframing-distance MEDIUM
    (Painlevé-D6 Trans-stratum framing); no OOB gate.

  - **APPROACH_PCF2_GAROUFALIDIS** — operator sends G2 template
    (`endorsement_request_pcf2_garoufalidis.md`); optional
    cross-check of the in-flight PCF-1 Garoufalidis pivot; only
    needed if PCF-1 mirror is blocked by page-count-drift carry.

  - **APPROACH_D2NOTE_SAUZIN** — operator sends G3 template
    (`endorsement_request_d2note_sauzin.md`) AFTER OOB handle
    recovery; reframing-distance LIGHT-MEDIUM (Écalle-resurgence +
    BT 1933 substrate); HANDLE_404 gate active.

  - **APPROACH_D2NOTE_COSTIN** — operator sends G4 template
    (`endorsement_request_d2note_costin.md`) AFTER OOB handle
    recovery; reframing-distance MEDIUM (connection-problem +
    generalized Borel-Laplace); HANDLE_404 gate active.

  - **APPROACH_T2B_BEUKERS** — operator sends G5 template
    (`endorsement_request_t2b_beukers.md`) AFTER OOB handle
    recovery AND emeritus eligibility confirmation; reframing-
    distance MEDIUM (Apéry-tradition + irrationality-measure
    framing); HANDLE_404 + emeritus gates active.

  - **APPROACH_<other>** — synthesizer names a different
    endorser-paper pair not in the 5 GAP-CANDIDATE set above
    (e.g. fallback to (Costin, CT v1.3) or (Sauzin, CT v1.3)
    if the D2-NOTE route fails); operator drafts a fresh
    template at that point.

  - **WAIT_FOR_TIER2_CONFIRM** — synthesizer holds the W21
    decision pending operator OOB handle recovery for one or
    more of Costin / Sauzin / Beukers; the W22 cadence absorbs
    the decision after recovery.

  - **DEFER** — synthesizer holds the W21 decision for any
    other reason; W22 LANE-1 takes the issue.

  - **OBJECT** — synthesizer flags an issue with the 078
    dossier itself (e.g., spec-axis ambiguity raised in
    `discrepancy_log.json` D-078-4) and requests operator
    intervention.

## §F.7 — Cadence framing

W21 LANE-1 cadence: Mon 2026-05-12 AM JST (per spec §6.F.1).
This 078 dispatch packet is **W21-pre-cadence substrate**; the
synthesizer's decision is reserved for the standard W21 weekly
cycle and is not requested earlier.  The 078 deliverables
remain valid through the cadence window unless 074 / 075 / 077
verdicts overturn substrate before W21 (none expected at fire
time).

---

## §F.8 — Verdict tag (per spec §10)

**DOSSIER_PARTIAL** because 3 of the 5 active gap-template
candidates (G3 Sauzin, G4 Costin, G5 Beukers) each have a
HANDLE_404 status and one (G5 Beukers) additionally has an
emeritus-eligibility gate.  All 5 gap-templates are nevertheless
drafted with placeholder discipline; the operator can advance
them through OOB recovery without 078 re-fire.  Per spec §10
DOSSIER_PARTIAL "synth decision packet emitted with explicit
'PARTIAL' tag and named gaps":

- **PARTIAL gap 1:** Costin standard slug HANDLE_404; OOB
  recovery required.
- **PARTIAL gap 2:** Sauzin standard slug HANDLE_404; OOB
  recovery required.
- **PARTIAL gap 3:** Beukers standard slug HANDLE_404 +
  emeritus eligibility gate; OOB recovery + privileges
  pre-flight required.

Tier-1 (Mazzocco / Garoufalidis) endorsers are NOT subject to
PARTIAL tag — both have HANDLE_VERIFIED + email status (verified
for Mazzocco; standard placeholder for Garoufalidis) at the
spec §7 non-negotiable discipline level.

End of decision packet.
