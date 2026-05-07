# Forbidden-Verb (FV-7) Scan — 080

**Phase:** H.1
**Tolerance:** 0 ASSERTION-class hits in production deliverables
(D2-D11). Set-literal echoes confined to this scan file only per
SET-LITERAL MITIGATION precedent (077/078/079 J3).

> [META-policy] This scan file is the sole production artifact in
> which the FV-7 set is enumerated as a literal set. Per 077/078/
> 079 J3 (`forbidden_verb_scan.md` files in those sessions) this
> mitigation is precedential and not a halt-trigger.

---

## §H.1.1 — FV-7 set definition

The FV-7 set (forbidden verb stems for ASSERTION-class usage in
production deliverables):

| Stem | Forbidden ASSERTION-class form | Permitted CITATION/FRAMING-class form |
|---|---|---|
| recommend | "I recommend …" / "the recommended pick is …" | "§Recommended next step" (verbatim handoff section header); "no recommended-pick" (negation citation) |
| select | "I select …" / "the agent selects …" | "synth selects …" (synth-role framing); "PICK_<X>" (verbatim option label) |
| pick | "I pick …" / "the agent picks …" | "synth picks …"; "PICK_<X>"; "portfolio bundle pick (077)" (sub-tree label naming the decision-class) |
| choose | "I choose …" / "the agent chooses …" | "synth chooses …" (synth-role framing) |
| prefer | "preferred option is …" | "no default option declared, none preferred" (negation citation from 078 substrate) |
| advise | "I advise …" | (none in this session) |
| default | "the default is …" | "no default option declared" (negation citation); `default` as Python keyword in code |

Forbidden ASSERTION-class hits result in HALT_080_DECISION_OVERREACH.
Permitted CITATION-class / FRAMING-class hits do not.

---

## §H.1.2 — Scan results

Production deliverables scanned:

- D2  `substrate_anchor_shas.md`
- D3  `dossier_decision_vector_074.md`
- D4  `dossier_decision_vector_075.md`
- D5  `dossier_decision_vector_077.md`
- D6  `dossier_decision_vector_078.md`
- D7  `dossier_decision_vector_079.md`
- D8  `cross_dossier_coupling_matrix.md`
- D9  `temporal_ordering_dag.md`
- D10 `decision_tree_skeleton.md`
- D11 `cross_dossier_amendment_notes.md`
- D12 `w21_lane1_synth_absorption_aid.md`

Tooling: `grep_search` regex `\b(recommend|select|pick|choose|prefer|advise|default)\w*\b`.

### Hits by deliverable

| Deliverable | Total stem hits | ASSERTION-class | CITATION/FRAMING-class |
|---|---:|---:|---|
| D2 substrate_anchor_shas.md | 0 | 0 | (none) |
| D3 dossier_decision_vector_074.md | ≥1 | 0 | "§Recommended next step" (header citation) |
| D4 dossier_decision_vector_075.md | ≥3 | 0 | "§Recommended next step" header (×3); "Path-δ vs Path-γ axes" |
| D5 dossier_decision_vector_077.md | ≥1 | 0 | "§Recommended next step" header (074 reference) |
| D6 dossier_decision_vector_078.md | ≥2 | 0 | `[NULL_DEFAULT]` substrate-cite tag; "no default option declared, none preferred" (negation cite); "the obvious / right" (negation cite) |
| D7 dossier_decision_vector_079.md | ≥3 | 0 | "alphabetically without recommended-pick" (substrate cite); "encode a recommended ordering" (negation framing); "§Recommended next step" header |
| D8 cross_dossier_coupling_matrix.md | ≥1 | 0 | `PICK_Bn` (verbatim option label); column / row header references |
| D9 temporal_ordering_dag.md | ≥10 | 0 | `PICK_Bn` / `PICK_<vid>` / `PICK_OTHER` (verbatim option labels); "synth picks" (synth-role framing); "§Recommended next step" header (×4) |
| D10 decision_tree_skeleton.md | ≥30 | 0 | `PICK_B1`…`PICK_B5` / `PICK_PAIR_*` / `PICK_OTHER_PAIR` / `PICK_JFR` / `PICK_LMCS` / `PICK_MCS` / `PICK_TCS` / `PICK_OTHER` (all verbatim option labels); "Portfolio bundle pick" / "Endorser pick" / "Lean venue pick" (sub-tree labels) |
| D11 cross_dossier_amendment_notes.md | ≥4 | 0 | `PICK_Bn` (×4 verbatim option label citations); "synth selects" / "synth picks" (synth-role framing) |
| D12 w21_lane1_synth_absorption_aid.md | ≥7 | 0 | `PICK_Bn` (verbatim option label); "synth chooses" / "synth selects" (synth-role framing); "Portfolio bundle pick" / "Endorser pick" / "Lean venue pick" (sub-tree labels); "§Recommended next step" header citation |

### Aggregate

- ASSERTION-class hits: **0** (tolerance: 0). PASS.
- CITATION-class hits: many; all permitted under SET-LITERAL
  MITIGATION precedent.
- FRAMING-class hits: "synth picks / chooses / selects" — these
  describe synth's role, not agent assertions. PASS.

---

## §H.1.3 — Categorization rationale

A stem hit is ASSERTION-class iff:
1. The agent is the grammatical subject ("I recommend …" /
   "the agent picks …" / "the recommended pick is …"), OR
2. A specific option is named as preferred / recommended /
   the default / the right pick by agent voice.

A stem hit is CITATION-class iff:
1. It echoes a substrate decision-packet option label verbatim
   (e.g., `PICK_B1`, `PICK_JFR`), OR
2. It echoes a substrate handoff section header verbatim
   (e.g., "§Recommended next step"), OR
3. It cites substrate text with negation framing (e.g., "no
   default option declared, none preferred").

A stem hit is FRAMING-class iff:
1. The grammatical subject is "synth" (referring to the W21
   LANE-1 reader's role), and the verb describes synth's role,
   not an agent endorsement of which option synth should pick.

All hits across D2-D12 fall in CITATION or FRAMING class.

---

## §H.1.4 — Verdict

**Forbidden-verb scan: PASS.** 0 ASSERTION-class hits across all
11 production deliverables. SET-LITERAL MITIGATION applied:
FV-7 set is enumerated as a literal set only in §H.1.1 of this
file.

End of `forbidden_verb_scan.md`.
