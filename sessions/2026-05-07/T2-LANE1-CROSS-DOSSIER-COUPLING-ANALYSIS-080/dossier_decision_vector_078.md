# Dossier Decision Vector — 078 (Endorser Framing)

**Dossier ID:** [DOSSIER-078]
**Title:** T2-ENDORSER-FRAMING-DOSSIER-ASSEMBLY-078
**Source decision packet:** `w21_lane1_endorser_decision_packet.md`
  (SHA `42426E6BDA7D7AA3…`, 7940 B, 144 lines)
**Source handoff:** `handoff.md`
  (SHA `DC2045DBF3B3F5A5…`, 12078 B, 208 lines)
**Bridge landing commit:** `32b808b`
**Verdict tag (verbatim, ≤ 50 words):**

> "DOSSIER_PARTIAL because 3 of the 5 active gap-template
>  candidates (G3 Sauzin, G4 Costin, G5 Beukers) each have a
>  HANDLE_404 status and one (G5 Beukers) additionally has an
>  emeritus-eligibility gate."

(36 words; from `w21_lane1_endorser_decision_packet.md` §F.8;
≤ 50-word ceiling PASS.)

---

## §1 — Identifier + provenance

[DOSSIER-078] is the endorser-framing substrate dossier covering
6 endorser profiles (Mazzocco / Garoufalidis / Costin / Sauzin /
Beukers / Zudilin-historical-anchor) × 6 SIARC papers; 5 active
gap-templates G1–G5; Tier-2 handle pre-verification (3 of 3
HANDLE_404 against the standard slug pattern); emits a 9-option
synth menu in §F.6 for W21 LANE-1.

## §2 — Verdict tag (verbatim from handoff)

> "DOSSIER_PARTIAL"

(handoff §"Status / Verdict" header.)

## §3 — Menu-option enumeration table

The 9 options enumerated verbatim in
`w21_lane1_endorser_decision_packet.md` §F.6:

| Option-tag | Structural-summary (verbatim ≤ 30 words) | Operator-OOB-gates | Operator-pre-flight gates | Synth-blocking conditions |
|---|---|---|---|---|
| `APPROACH_PCF2_MAZZOCCO` | "operator sends G1 template (`endorsement_request_pcf2_mazzocco.md`); Mazzocco is the only Tier-1 endorser whose email is VERIFIED; reframing-distance MEDIUM; no OOB gate." | none (Mazzocco email verified per memory) | G1 template ready; no pre-flight gate | none |
| `APPROACH_PCF2_GAROUFALIDIS` | "operator sends G2 template (`endorsement_request_pcf2_garoufalidis.md`); optional cross-check of the in-flight PCF-1 Garoufalidis pivot; only needed if PCF-1 mirror is blocked by page-count-drift carry." | Garoufalidis Tier-1 email pending operator confirm | G2 OPTIONAL framing | PCF-1 pivot in-flight |
| `APPROACH_D2NOTE_SAUZIN` | "operator sends G3 template AFTER OOB handle recovery; reframing-distance LIGHT-MEDIUM; HANDLE_404 gate active." | Tier-2 handle recovery (sauzin_d_1 HANDLE_404) | G3 template draft | OOB recovery required |
| `APPROACH_D2NOTE_COSTIN` | "operator sends G4 template AFTER OOB handle recovery; reframing-distance MEDIUM; HANDLE_404 gate active." | Tier-2 handle recovery (costin_o_1 HANDLE_404) | G4 template draft | OOB recovery required |
| `APPROACH_T2B_BEUKERS` | "operator sends G5 template AFTER OOB handle recovery AND emeritus eligibility confirmation; reframing-distance MEDIUM; HANDLE_404 + emeritus gates active." | Tier-2 handle recovery + emeritus eligibility (beukers_f_1 HANDLE_404) | privileges pre-flight at arxiv.org/auth/show-privileges | OOB recovery + emeritus active-status |
| `APPROACH_<other>` | "synthesizer names a different endorser-paper pair not in the 5 GAP-CANDIDATE set above (e.g., fallback to (Costin, CT v1.3) or (Sauzin, CT v1.3) if the D2-NOTE route fails); operator drafts a fresh template at that point." | synth names pair | template-drafting cycle | synth specifies pair |
| `WAIT_FOR_TIER2_CONFIRM` | "synthesizer holds the W21 decision pending operator OOB handle recovery for one or more of Costin / Sauzin / Beukers; the W22 cadence absorbs the decision after recovery." | none in W21; OOB recovery before W22 | n/a | W22 LANE-1 absorption |
| `DEFER` | "synthesizer holds the W21 decision for any other reason; W22 LANE-1 takes the issue." | synth-named gating reason | none | named-event resolution |
| `OBJECT` | "synthesizer flags an issue with the 078 dossier itself (e.g., spec-axis ambiguity raised in `discrepancy_log.json` D-078-4) and requests operator intervention." | dossier amendment scope | none | re-fire cycle |

## §4 — PARTIAL / AMBIGUOUS-option flag-set

- `APPROACH_PCF2_GAROUFALIDIS` is OPTIONAL per spec §4.D.3 second
  item; only fires if PCF-1 mirror is blocked.
- `APPROACH_D2NOTE_SAUZIN` / `APPROACH_D2NOTE_COSTIN` /
  `APPROACH_T2B_BEUKERS` all carry HANDLE_404 + OOB-recovery gates
  per `tier2_handle_preverification.md` §E.5.
- `APPROACH_T2B_BEUKERS` additionally carries emeritus-eligibility
  gate.
- `APPROACH_<other>` requires synth pair-specification.
- `WAIT_FOR_TIER2_CONFIRM` defers to W22 LANE-1 by definition.
- `OBJECT` requires synth-supplied amendment scope.
- `APPROACH_PCF2_MAZZOCCO` is the only option without any active
  OOB / pre-flight gate at fire time (Mazzocco email VERIFIED per
  memory `endorsement workflow`).

## §5 — [NULL_DEFAULT] declaration

The 078 packet §F.6 asserts: "Per HALT_078_ENDORSER_SELECTION_
OVERREACH discipline, the agent does not assert which option is
preferred." No default option declared. Recorded as [NULL_DEFAULT].

> [META-policy] Per HALT_080_DECISION_OVERREACH discipline this
> vector neither orders the 5 APPROACH_* options nor characterises
> any as "the obvious / right" pair. The Mazzocco asymmetry per
> handoff Anomalies A1 ("only verified email of the 5 active
> endorsers") is documented as a substrate-anchored fact about
> gate-status, not as a synth-side ranking signal.

## §6 — Option count + category breakdown

- Total options: 9
- Categories:
  - `APPROACH-class`: 6 (5 named pairs + `APPROACH_<other>`)
  - `WAIT-class`: 1 (`WAIT_FOR_TIER2_CONFIRM`)
  - `DEFER-class`: 1 (`DEFER`)
  - `OBJECT-class`: 1 (`OBJECT`)
- Operator-OOB-gates active on: 4 of 5 named APPROACH_* options
  (only `APPROACH_PCF2_MAZZOCCO` is gate-free at fire time);
  `APPROACH_<other>` (synth pair-specification);
  `OBJECT` (amendment scope).
- Operator-pre-flight gates active on: `APPROACH_T2B_BEUKERS`
  (privileges pre-flight); `APPROACH_PCF2_GAROUFALIDIS` (G2 OPTIONAL
  framing carries page-count-drift contingency).
- Tier-2 handle pre-verification: 3/3 standard slugs HANDLE_404
  per 2026-05-04 dossier anchor.

---

## §7 — Cross-coupling indicators (substrate anchors only)

Anchors from `w21_lane1_endorser_decision_packet.md` §F.3 + §F.5
and `endorser_paper_coverage_matrix.md`:

- [COUPLING-ANCHOR-078a] Endorser ↔ paper coverage matrix is 6 ×
  6 = 36 cells with 5 active rows (Zudilin row HISTORICAL-ANCHOR);
  active-row tally: 7 EXISTING pairs + 5 GAP-CANDIDATE (G1-G5) +
  18 SKIP-FIT-WEAK + 0 SKIP-DECLINED-INHERIT (per §F.3).
- [COUPLING-ANCHOR-078b] Endorser-paper pairing is gated by 077
  bundle pick: B1/B3 (PCF-2 in scope) → APPROACH_PCF2_MAZZOCCO or
  APPROACH_PCF2_GAROUFALIDIS; B2 (D2-NOTE in scope) →
  APPROACH_D2NOTE_SAUZIN or APPROACH_D2NOTE_COSTIN; B5 status quo
  enables full APPROACH_* set per existing per-paper venue
  rationale.
- [COUPLING-ANCHOR-078c] Tunnell-CNP Lean paper is OUT-OF-SCOPE
  for 078 (handoff §"Files committed" — endorser_paper_coverage_
  matrix only inventories the 6 SIARC-track papers, not Lean);
  078 does NOT couple to 079 venue-fit through the endorsement
  axis at endorser-level.
- [COUPLING-ANCHOR-078d] D-078-2 DOI drift inherits the 077 D-077-1
  drift; both anchor on-disk substrate per shared judgment call J2.
- [COUPLING-ANCHOR-078e] U-078-2 Mazzocco UPC email verification
  is a memory-anchored fact (`endorsement workflow`), not a
  fire-time pre-verification.
- [COUPLING-ANCHOR-078f] G2 PCF-2 × Garoufalidis OPTIONAL framing
  forward-points to in-flight PCF-1 Garoufalidis pivot per spec
  §4.D.3 second item — couples to operator-side parallel pivot
  state.

---

End of `dossier_decision_vector_078.md`.
