# Dossier Decision Vector — 074 (M4 Ratification)

**Dossier ID:** [DOSSIER-074]
**Title:** T2-M4-RATIFICATION-DOSSIER-ASSEMBLY-074
**Source decision packet:** `w21_lane1_m4_dispatch_packet.md`
  (SHA `B45B595A50A71D9C…`, 7387 B, 140 lines)
**Source handoff:** `handoff.md`
  (SHA `72E69F7495F5FE7F…`, 10477 B, 171 lines)
**Bridge landing commit:** `9596c21`
**Verdict tag (verbatim, ≤ 50 words):**

> "DOSSIER_COMPLETE" (handoff "Verdict" line; 074 §F.1 Phase F self-checks PASS)

(2 words; ≤ 50-word ceiling PASS.)

---

## §1 — Identifier + provenance

[DOSSIER-074] is the M4 closure-path ratification substrate-inventory
dossier. It surfaces a 4-tag synth-decision menu in dispatch-packet
§E.5 and 18 residual questions in `m4_residual_questions.md` §D for
synth weighing.

## §2 — Verdict tag (verbatim from handoff)

> "DOSSIER_COMPLETE"

(handoff §"Status / Verdict" header; 1 word; ceiling PASS.)

## §3 — Menu-option enumeration table

The 4 options enumerated verbatim in `w21_lane1_m4_dispatch_packet.md`
§E.5:

| Option-tag | Structural-summary (verbatim ≤ 30 words) | Operator-OOB-gates | Operator-pre-flight gates | Synth-blocking conditions |
|---|---|---|---|---|
| `RATIFY` | "synthesizer accepts the 068 verdict at MEDIUM-HIGH confidence as-is and authorises the M9 gating-set reduction `{M4, M6.CC} → {M6.CC}`." | none asserted | none asserted | none in dispatch packet |
| `RATIFY_WITH_AMENDMENT` | "synthesizer accepts the 068 verdict with one or more named amendments (e.g., v1.20 absorption order, G12 PCF-1 v1.4 amendment cycle ordering, MEDIUM-HIGH → HIGH path selection)." | named amendment(s) supplied by synth | depends on amendment scope | synth must supply amendment text |
| `DEFER` | "synthesizer defers ratification pending one or more named events (e.g., Wasow §X.3 OCR acquisition, picture v1.20 deposit, additional W21 substrate)." | event-pending list (Wasow OCR / picture v1.20 / W21 substrate) | OCR acquisition path open per Q-D4-1 | named-event resolution required |
| `OBJECT` | "synthesizer rejects the 068 closure-path framing and surfaces a counter-claim or counter-substrate path for re-arbitration." | counter-claim / counter-substrate text from synth | re-arbitration request | re-arbitration cycle |

## §4 — PARTIAL / AMBIGUOUS-option flag-set

- `RATIFY_WITH_AMENDMENT` is conditional: the dossier surfaces 4
  named amendment-class candidates (Q-D4-1 Wasow OCR / Q-D4-2
  PCF-1 v1.4 / Q-D4-3 picture v1.20 / Q-D4-4 M9 effective-time)
  in `m4_residual_questions.md` §D-D4. The dossier does NOT
  assert that any of these MUST be applied; synth scope.
- `DEFER` is conditional on synth-named pending events.
- `OBJECT` requires synth-supplied counter-substrate.
- `RATIFY` is the only option without conditional dependencies.

## §5 — [NULL_DEFAULT] declaration

The 074 dispatch packet does not declare a default option. Per
§E.5 verbatim: "The 074 agent assembles the dispatch packet. The
W21 LANE-1 synthesizer arbitrates." Recorded as [NULL_DEFAULT].

## §6 — Option count + category breakdown

- Total options: 4
- Categories:
  - `RATIFY-class`: 2 (`RATIFY`, `RATIFY_WITH_AMENDMENT`)
  - `DEFER-class`: 1 (`DEFER`)
  - `OBJECT-class`: 1 (`OBJECT`)
- Operator-OOB-gates active on: `DEFER` (event-pending list);
  `RATIFY_WITH_AMENDMENT` (amendment text); `OBJECT` (counter-text)
- Operator-pre-flight gates active on: `RATIFY_WITH_AMENDMENT` (Q-D4-1
  Wasow OCR if HIGH-upgrade amendment is named)

---

## §7 — Cross-coupling indicators (substrate anchors only)

Anchors from dispatch packet §E.5 and handoff §"Recommended next step":

- [COUPLING-ANCHOR-074a] Forward-pointed dispatch (a) "PCF-1 v1.4
  amendment cycle (G12 jurisdiction, Q-D4-2): forward-pointed
  if synthesizer issues `RATIFY` or `RATIFY_WITH_AMENDMENT`."
  (handoff §"Recommended next step" §a)
- [COUPLING-ANCHOR-074b] Forward-pointed dispatch (b) "Picture v1.20
  deposit cycle (Q-D4-3): forward-pointed if synthesizer wishes M4
  ratification absorbed in v1.20."
  (handoff §"Recommended next step" §b)
- [COUPLING-ANCHOR-074c] Forward-pointed dispatch (c) "Wasow §X.3
  OCR acquisition (Q-D4-1): forward-pointed if synthesizer wishes
  MEDIUM-HIGH → HIGH upgrade path."
  (handoff §"Recommended next step" §c)
- [COUPLING-ANCHOR-074d] Forward-pointed dispatch (d) "BT 1933 §§7-9
  readthrough relay (075-class) (Q-D3-4): forward-pointed by 073
  itself; can fire in W21 LANE-2 parallel to LANE-1 ratification
  arbitration."
  (handoff §"Recommended next step" §d)
- [COUPLING-ANCHOR-074e] M9 gating-set reduction `{M4, M6.CC} →
  {M6.CC}` is gated on `RATIFY` per §E.5 verbatim — couples 074
  output to 075 (M6.CC) downstream.

---

End of `dossier_decision_vector_074.md`.
