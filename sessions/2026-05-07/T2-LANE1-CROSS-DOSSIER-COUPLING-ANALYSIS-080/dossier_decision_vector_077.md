# Dossier Decision Vector — 077 (Portfolio Bundling)

**Dossier ID:** [DOSSIER-077]
**Title:** T2-PORTFOLIO-BUNDLING-DOSSIER-ASSEMBLY-077
**Source decision packet:** `w21_lane1_portfolio_decision_packet.md`
  (SHA `D6AF151A91296AE7…`, 8119 B, 120 lines)
**Source handoff:** `handoff.md`
  (SHA `B7C6D6AF9389094C…`, 10171 B, 79 lines)
**Bridge landing commit:** `49f3423`
**Verdict tag (verbatim, ≤ 50 words):**

> "DOSSIER_COMPLETE"

(1 word; from handoff "Verdict" line; ≤ 50-word ceiling PASS.)

---

## §1 — Identifier + provenance

[DOSSIER-077] is the portfolio-bundling decision substrate dossier
covering 5 candidate bundle configurations (B1-B5) across 7
feasibility dimensions; 6 paper profiles (PCF-1, PCF-2, CT v1.3,
D2-NOTE v2.1, T2B v3.0, umbrella v2.0); cross-bundle compatibility
surface; emits a 10-option synth menu in §F.E for W21 LANE-1.

## §2 — Verdict tag (verbatim from handoff)

> "DOSSIER_COMPLETE"

(handoff §"Status / Verdict" header.)

## §3 — Menu-option enumeration table

The 10 options enumerated verbatim in
`w21_lane1_portfolio_decision_packet.md` §F.E:

| Option-tag | Structural-summary (verbatim ≤ 30 words) | Operator-OOB-gates | Operator-pre-flight gates | Synth-blocking conditions |
|---|---|---|---|---|
| `PICK_B1` | "adopt B1 PCF-stratification monograph" (PCF-1 v1.3 + PCF-2 v1.3 + T2B v3.0; ~37–41 pp; math.NT; YELLOW) | bundle reweave / page-count / venue selection | none | YELLOW feasibility per `bundle_feasibility_matrix.md` D.8 |
| `PICK_B2` | "adopt B2 Asymptotic-channels paper" (CT v1.4 post-G17-close + D2-NOTE v2.1; ~25–27 pp; math-ph; YELLOW) | G17 close gate; D2-NOTE template draft | CT v1.4 publication state | gated on G17-close per D.7 |
| `PICK_B3` | "adopt B3 Trans-stratum focus" (PCF-2 v1.3 + T2B v3.0; ~25–27 pp; math.NT; YELLOW) | bundle reweave | none | YELLOW |
| `PICK_B4` | "adopt B4 SIARC research-monograph" (all 6 papers; ~57–66 pp; math.NT + math-ph cross; YELLOW) | major reweave | umbrella reissue | YELLOW; largest scope-of-work |
| `PICK_B5` | "adopt B5 status quo" (each paper to its own venue; 6 standalone; ~80–84 pp aggregate; GREEN) | none | none | GREEN per D.8 OVERALL |
| `PICK_PAIR_B1+B2` | "adopt the 5-record-coverage compatible pair" (B1 + B2; P1 + P2 + P5 ∪ P3 + P4 → 5/6) | both B1 and B2 OOB gates | both B1 and B2 pre-flight gates | YELLOW × 2 |
| `PICK_PAIR_B1+B5` | "adopt B1 + standalone-dispatch of P3 + P4 + P6" | B1 OOB gates | B1 pre-flight gates | YELLOW + GREEN |
| `PICK_OTHER_PAIR` | "synth specifies a different pair (tie-break required)" | synth-named pair gates | tie-break declaration | synth must specify pair |
| `DEFER` | "defer to a later W2x cadence; surface gating reason" | gating reason supplied by synth | none | named-event resolution |
| `OBJECT` | "synth requests dossier amendment (077R re-fire) before deciding" | amendment scope from synth | 077R re-fire window | re-fire cycle |

## §4 — PARTIAL / AMBIGUOUS-option flag-set

- `PICK_B2` is conditional on G17-close gate (per D.7
  GATED-ON-X trigger; flagged in `bundle_feasibility_matrix.md`).
  CT v1.4 is in-flight (TeX present; no Zenodo deposit yet) per
  judgment call J2.
- `PICK_B4` is conditional on umbrella v2.0 reweave + multi-paper
  coordination per D.7 NEEDS-REWEAVE.
- `PICK_PAIR_B1+B2` inherits both B1 and B2 conditional gates.
- `PICK_OTHER_PAIR` requires synth-supplied tie-break.
- `DEFER` requires synth-supplied gating reason.
- `OBJECT` requires synth-supplied amendment scope.
- All B1-B4 score YELLOW per `bundle_feasibility_matrix.md` D.8.
- B5 is the only GREEN.

## §5 — [NULL_DEFAULT] declaration

The 077 packet §F.E asserts `[DECISION-RESERVATION]`: "the
decision-input row is left blank for synth." Per HALT_077_BUNDLE_
SELECTION_OVERREACH discipline, the dossier does not declare a
default option. Recorded as [NULL_DEFAULT].

## §6 — Option count + category breakdown

- Total options: 10
- Categories:
  - `PICK-single-class`: 5 (`PICK_B1`, `PICK_B2`, `PICK_B3`,
    `PICK_B4`, `PICK_B5`)
  - `PICK-pair-class`: 3 (`PICK_PAIR_B1+B2`, `PICK_PAIR_B1+B5`,
    `PICK_OTHER_PAIR`)
  - `DEFER-class`: 1 (`DEFER`)
  - `OBJECT-class`: 1 (`OBJECT`)
- Operator-OOB-gates active on: `PICK_B1`, `PICK_B2`, `PICK_B3`,
  `PICK_B4`, both pair-class (B1+B2, B1+B5), and `PICK_OTHER_PAIR`,
  `DEFER`, `OBJECT`. Only `PICK_B5` is gate-free.
- Operator-pre-flight gates active on: `PICK_B2` (G17-close + CT
  v1.4 publication state), `PICK_PAIR_B1+B2` (inherits)
- Feasibility tag distribution: 1 GREEN (B5), 4 YELLOW (B1, B2,
  B3, B4), 0 RED.

---

## §7 — Cross-coupling indicators (substrate anchors only)

Anchors from `w21_lane1_portfolio_decision_packet.md` §F.D and §F.G
and `cross_bundle_compatibility.md` §E.4:

- [COUPLING-ANCHOR-077a] B5 status quo carries existing per-paper
  venue rationale and per-paper standalone-strength tags
  (HIGH/MEDIUM/PROGRAM-STATEMENT-STANDALONE per E.4); each
  standalone path can be coupled to 078 endorsement-pivot or 079
  Lean venue dispatch downstream.
- [COUPLING-ANCHOR-077b] B2 (CT v1.4 + D2-NOTE v2.1) constrains
  endorsement set to D2-NOTE-relevant endorsers (Costin / Sauzin)
  and CT-relevant endorsers (Mazzocco) per 078 coverage matrix.
- [COUPLING-ANCHOR-077c] B1 / B3 (PCF-2 in scope) constrains
  endorsement set to PCF-2-relevant endorsers (Mazzocco /
  Garoufalidis) per 078 coverage matrix.
- [COUPLING-ANCHOR-077d] B4 (all 6 papers) requires umbrella v2.0
  reissue per D-077-3 stale-cite of CT v1.2; couples to
  picture v1.20 absorption forward-pointer in 074-§"Recommended
  next step" §b.
- [COUPLING-ANCHOR-077e] D-077-1 DOI drift between prompt-spec
  and `portfolio_inventory.md`; substrate-anchored to
  on-disk DOIs per J1 judgment call.
- [COUPLING-ANCHOR-077f] D-077-6: "074 + 075 PRE-COMMIT
  IN-FLIGHT" at 077 fire — both 074 and 075 commits independent
  of 077 LANE-1 decision (per `discrepancy_log.json` D-077-6).
- [COUPLING-ANCHOR-077g] U-077-3: "B1 + B2 + P6-standalone
  three-stack pattern" structural insight — 6/6 record coverage
  in 3 artefacts; surfaced as inventory only.
- [COUPLING-ANCHOR-077h] Lean / Tunnell-CNP paper is NOT in the 6
  paper-profile inventory; 077 portfolio scope is the SIARC-track
  6 paper set, separate from 079 venue-fit dossier scope. (077
  paper-profile inventory: PCF-1 v1.3, PCF-2 v1.3, CT v1.3,
  D2-NOTE v2.1, T2B v3.0, umbrella v2.0.)

---

End of `dossier_decision_vector_077.md`.
