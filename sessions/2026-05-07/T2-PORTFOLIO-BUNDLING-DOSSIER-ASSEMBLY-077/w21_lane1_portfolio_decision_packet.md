# W21 LANE-1 Portfolio-Bundling Decision Packet — 077

**Session:** T2-PORTFOLIO-BUNDLING-DOSSIER-ASSEMBLY-077
**Compiled:** 2026-05-07
**Cadence target:** W21 LANE-1 Mon 2026-05-12 AM JST
**Bridge URL (077 dossier):** `https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-05-07/T2-PORTFOLIO-BUNDLING-DOSSIER-ASSEMBLY-077/`

---

## Portfolio-bundling decision request (W21 LANE-1)

[ROLE-NAMING] **T1-Synthesizer (Claude.ai LANE-1) is the deciding party**
for portfolio-architecture this cycle. The 077 dossier (this session)
is a substrate-inventory artefact assembled by the T2 mechanical
relay agent; the agent does not assert which configuration the
synthesizer adopts. Per spec §F.1 the verb-set used by the agent
is restricted to the inventory tags below; synth supplies the
selection verb at W21 LANE-1.

[OPERATOR-QUOTE-VERBATIM] Operator framing question (2026-05-07
~14:11 JST chat transcript verbatim, 14 words; this is the one
permitted over-claiming verb in the entire dossier per spec §6.F.2):
> "help assess if we can combine multiple papers into a larger picture for submission"

[QUOTE-LENGTH-CHECK] 14 words ≤ 50 word cap → spec §8 HALT_077_QUOTE_LENGTH not triggered.

---

## §F.A — 077 dossier reference

The 077 dossier comprises 14 deliverable files plus the 4-element
AEAL quartet (claims.jsonl + halt_log.json + discrepancy_log.json
+ unexpected_finds.json). Synth-relevant entry points:

- `bundle_configuration_matrix.md` — 5 bundle compositions × 7 dimensions × cross-reference 6×6 matrix
- `bundle_feasibility_matrix.md` — 5 × 7 + OVERALL_FEASIBILITY_TAG
- `cross_bundle_compatibility.md` — pairings + 3-bundle stacks + standalone-strength inventory
- `paper_profile_pcf1_v13.md` … `paper_profile_umbrella_v20.md` — 6 per-paper profiles
- `portfolio_substrate_anchor_shas.md` — substrate SHA + DOI cross-check
- `handoff.md` — judgment calls + anomalies + open questions for synth

---

## §F.B — 5-bundle inventory summary table

| Bundle | Composition | Records | ~pp | Primary cat | OVERALL tag |
|---|---|---:|---:|---|---|
| [BUNDLE-B1] | PCF-1 v1.3 + PCF-2 v1.3 + T2B v3.0 | 3 | 37–41 | math.NT | YELLOW |
| [BUNDLE-B2] | CT v1.4 (post-G17-close) + D2-NOTE v2.1 | 2 | 25–27 | math-ph | YELLOW |
| [BUNDLE-B3] | PCF-2 v1.3 + T2B v3.0 | 2 | 25–27 | math.NT | YELLOW |
| [BUNDLE-B4] | umbrella v2.0 + PCF-1 + PCF-2 + CT v1.4 + D2-NOTE v2.1 + T2B v3.0 | 6 | 57–66 | math.NT (+ math-ph cross) | YELLOW |
| [BUNDLE-B5] | each paper to its own venue (status quo) | 6 (standalone) | 80–84 (aggregate) | per-record | GREEN |

Per `bundle_feasibility_matrix.md` D.8 NOTE-077-D-1, no bundle
scores RED; B5 scores GREEN by virtue of D.7 IMMEDIATE
(no-bundling-work configuration). All B1/B2/B3/B4 score YELLOW
on a combination of NEEDS-REWEAVE / EXISTING+EXTEND / GATED-ON-X
triggers.

---

## §F.C — Feasibility matrix link

Full 5 × 7 inventory: see `bundle_feasibility_matrix.md` in this
session directory. Trigger-pattern column reproduces the
dimension labels that produced each bundle's OVERALL tag. Per
spec §6.F.1 + HALT_077_BUNDLE_SELECTION_OVERREACH, the dossier
does not aggregate the matrix into a synth-ready ranking.

---

## §F.D — Cross-bundle compatibility surface

From `cross_bundle_compatibility.md` E.1–E.4:

[BUNDLE-PAIRING-INVENTORY] Two MUTUALLY COMPATIBLE pairs (non-overlapping records):

1. **B1 + B2** = P1 + P2 + P5 (B1) ∪ P3 + P4 (B2) → 5/6 record coverage; P6 umbrella v2.0 standalone or absorbed
2. **B2 + B3** = P3 + P4 (B2) ∪ P2 + P5 (B3) → 4/6 record coverage; P1 + P6 standalones

[BUNDLE-PAIRING-CONFLICTS] All other 8 pairings have non-empty
record overlap; tie-break is operator/synth scope.

[BUNDLE-3-STACK-INVENTORY] Spec §5.E.3 examples confirmed:
(a) B1 + B2 + umbrella-standalone → 6/6 in 3 artefacts;
(b) B3 + PCF-1-standalone + B2 → 5/6 in 3 artefacts (loses PCF-1 ↔ PCF-2 bundling synergy per spec §5.E.3 verbatim).

[STANDALONE-STRENGTH-INVENTORY] Per E.4, substrate-anchored
standalone-strength tags (theorem-count + endorsement-fit basis):

- HIGH: D2-NOTE v2.1, T2B v3.0
- MEDIUM-to-HIGH: CT v1.3
- MEDIUM: PCF-1 v1.3
- PROGRAM-STATEMENT-STANDALONE: PCF-2 v1.3, umbrella v2.0

---

## §F.E — Decision request

[DECISION-VERB-INVENTORY] Per spec §6.F.1, the synth decision
verb-set is reproduced verbatim below. The agent emits no
verb; synth supplies one (or a hybrid + a deferral).

The synth decision-options enumerated in the prompt body are:

- `PICK_B1` — adopt B1 PCF-stratification monograph
- `PICK_B2` — adopt B2 Asymptotic-channels paper
- `PICK_B3` — adopt B3 Trans-stratum focus
- `PICK_B4` — adopt B4 SIARC research-monograph
- `PICK_B5` — adopt B5 status quo
- `PICK_PAIR_B1+B2` — adopt the 5-record-coverage compatible pair
- `PICK_PAIR_B1+B5` — adopt B1 + standalone-dispatch of P3 + P4 + P6
- `PICK_OTHER_PAIR` — synth specifies a different pair (tie-break required)
- `DEFER` — defer to a later W2x cadence; surface gating reason
- `OBJECT` — synth requests dossier amendment (077R re-fire) before deciding

[DECISION-RESERVATION] The agent makes no decision-verb selection.
Per HALT_077_BUNDLE_SELECTION_OVERREACH, the decision-input row
is left blank for synth. Per HALT_077_VENUE_TIE_BREAK, the
candidate-journal lists in §F.B are inventory-only; synth
supplies any venue-tie-break.

---

## §F.F — Cadence framing

W21 LANE-1 Mon 2026-05-12 AM JST is the next-window timestamp
for synth-tier decision per CMB.txt L1957–1985 cadence row +
spec §0 GOAL anchor. If synth chooses `DEFER`, a 077-amendment
(077R) re-fire window opens at W22 LANE-1 (~2026-05-19 AM JST).
If synth chooses `OBJECT`, the dossier returns to T2 with
amendment scope from synth.

---

## §F.G — Anomalies surface (read-by-synth before decision)

From `handoff.md` §"Anomalies and open questions" + `discrepancy_log.json`:

- **D-077-1 (DOI drift):** prompt §1.A.1 cites 5 DOIs that differ from canonical 2026-05-04 portfolio inventory. Substrate is on-disk and resolved; prompt-spec DOIs reframed in `portfolio_substrate_anchor_shas.md` §A.4.
- **D-077-2 (oral-only impact assessment):** spec §1.A.1 references a 2026-05-07 portfolio-impact assessment + endorsement-fit assessment that resides in chat transcript / session-state plan.md only; not on disk. 077 substrate derived from on-disk 2026-05-04 anchors instead.
- **D-077-3 (CT v1.2 stale-cite in umbrella):** umbrella v2.0 abstract L63 cites Channel Theory v1.2; CT v1.3 was issued 2026-05-02 (post-umbrella v2.0 deposit). Surfaced for synth awareness; no dossier action.
- **D-077-4 (T2B Zenodo DOI inconsistency):** CMB.txt L31 shows P-T2B at version DOI 19801038; portfolio inventory + submission_log Item 10 anchor 19915689 (v3.0). Surfaced; not a halt.
- **D-077-5 (E.4 standalone-strength deviation):** spec §5.E.4 anticipates "PCF-2 v1.3 + D2-NOTE v2.1 both Tier-1 standalone-strong"; on-disk substrate places PCF-2 at PROGRAM-STATEMENT-STANDALONE and D2-NOTE at HIGH. Substrate-anchored deviation; synth decides whether spec-anchor or on-disk-substrate-anchor binds.
- **D-077-6 (074 + 075 PRE-COMMIT IN-FLIGHT):** both predecessor sessions assembled-but-not-committed at 077 fire; 077 dossier validity independent per spec §1.A.3.

---

## §F.H — Verbatim non-overreach declaration

[NON-OVERREACH-DECLARATION] This decision packet contains no
verbs from the forbidden set {recommend, select, pick, choose,
prefer, advise, conclude}. The verb "advise" appears nowhere in
agent-authored prose. The verb "recommend" appears nowhere in
agent-authored prose. The verb "pick" appears only inside
spec-quoted decision-option labels (PICK_B1 etc.) and inside
spec verbatim quotes. The verbs "choose" / "prefer" / "select" /
"conclude" appear nowhere in agent-authored prose. See
`forbidden_verb_scan.md` (D11) for the mechanical scan
producing this declaration.

---

End of decision packet.
