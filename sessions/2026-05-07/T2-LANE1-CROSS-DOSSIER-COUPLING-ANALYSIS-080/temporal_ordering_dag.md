# Temporal-Ordering DAG — 080

**Phase:** D
**Scope:** event DAG covering the W21 LANE-1 quintet+1 (074/075/077/
078/079 + 076 GATED) and the post-LANE-1 dispatch / landing chain
derivable from the 5 dossier handoffs + 076 GATED preflight envelope.

> [META-policy] Per HALT_080_TIMING_FABRICATION discipline every
> edge in this DAG cites a substrate anchor in the corresponding
> dossier handoff / decision packet / 076 GATED envelope. Edges
> not directly substrate-anchored are marked `<derivation gap>`
> per envelope §2.D and surfaced in `cross_dossier_amendment_notes.md`.

> [META-policy] Per envelope §2.D this DAG includes only events
> derivable from the 5 dossier handoffs + 076 GATED preflight
> envelope. Post-LANE-1 events that the relay-080 envelope §7
> mentions but that are not anchored in dossier substrate (e.g.,
> arXiv mirror submission, Zenodo umbrella v2.1) are documented
> as `<derivation gap>` edges in §D.4 below.

---

## §D.1 — Event types

- **D-event:** decision absorption (synth picks an option at W21
  LANE-1).
- **X-event:** dispatch fire (post-LANE-1 envelope fires; operator
  side).
- **L-event:** external landing (paper deposited / endorsed /
  submitted; outside agent control).

---

## §D.2 — Node table

### D-events (W21 LANE-1 absorption — Mon 2026-05-12 AM JST)

| ID | Event | Origin dossier | Substrate anchor | Preconditions | Postconditions |
|---|---|---|---|---|---|
| `[D1]` | 074 verdict absorption (RATIFY / RATIFY_WITH_AMENDMENT / DEFER / OBJECT) | 074 | `w21_lane1_m4_dispatch_packet.md` §E.5 | none at LANE-1 | `[X1]` `[X2]` `[X3]` `[X4]` (X1/X2/X3 conditional) |
| `[D2]` | 075 verdict ratification + OQ-W21-LITERATURE-ALTERNATIVE resolution | 075 | `synthesizer_decision_packet.md` §E.6 + handoff §"Recommended next step" §1/§2 | none at LANE-1 | `[X5]` (gated on lit-alternative resolution = LIT_HUNT_PATH_DELTA) |
| `[D3]` | 077 portfolio bundle pick (PICK_Bn / PICK_PAIR / PICK_OTHER_PAIR / DEFER / OBJECT) | 077 | `w21_lane1_portfolio_decision_packet.md` §F.E | none at LANE-1 | downstream portfolio reweave / deposit (NOT explicitly substrate-named as a discrete X-event) |
| `[D4]` | 078 endorser pick (APPROACH_* / WAIT_FOR_TIER2_CONFIRM / DEFER / OBJECT) | 078 | `w21_lane1_endorser_decision_packet.md` §F.6 | `[D3]` (DECISION-COUPLED via [COUPLING-C4]) | `[X6]` `[X7]` (per APPROACH_* selection) |
| `[D5]` | 079 Lean venue pick (PICK_<vid> / PICK_OTHER / DEFER / WITHDRAW_PERMANENTLY) | 079 | `w21_lane1_lean_relaunch_decision_packet.md` "7-option synth menu" | none at LANE-1 (Lean disjoint from SIARC scope) | `[X8]` `[X9]` `[X10]` |

### X-events (post-LANE-1 dispatch — operator-side)

| ID | Event | Origin dossier | Substrate anchor | Preconditions | Postconditions |
|---|---|---|---|---|---|
| `[X1]` | PCF-1 v1.4 amendment cycle | 074 | handoff §"Recommended next step" §a | `[D1]` = RATIFY or RATIFY_WITH_AMENDMENT (per Q-D4-2 forward-pointer) | `[L2]` |
| `[X2]` | Picture v1.20 deposit cycle | 074 | handoff §"Recommended next step" §b | `[D1]` (any of RATIFY-class) ∧ Q-D4-3 absorption choice | `[L3]` |
| `[X3]` | Wasow §X.3 OCR acquisition | 074 | handoff §"Recommended next step" §c | `[D1]` = RATIFY_WITH_AMENDMENT (with HIGH-upgrade amendment per Q-D4-1) | `[L4]` |
| `[X4]` | BT 1933 §§7-9 readthrough relay (075-class) | 074 | handoff §"Recommended next step" §d (forward-pointed by 073) | none (parallel to LANE-1; can fire in W21 LANE-2) | (075-class extension) |
| `[X5]` | 076 path-δ literature acquisition reconnaissance | 075 / 076 | `synthesizer_decision_packet.md` §E.5 + 076 GATED preflight envelope §0 | `[D2]` = LIT_HUNT_PATH_DELTA resolution; identifier pre-verification (post-031 rule) | `[L1]` |
| `[X6]` | 078 G1 Mazzocco endorsement send | 078 | `w21_lane1_endorser_decision_packet.md` §F.6 (APPROACH_PCF2_MAZZOCCO option) | `[D4]` = APPROACH_PCF2_MAZZOCCO; no OOB gate (Mazzocco email VERIFIED) | (endorsement landing) |
| `[X7]` | 078 G2/G3/G4/G5 endorsement sends (Garoufalidis / Sauzin / Costin / Beukers) | 078 | `w21_lane1_endorser_decision_packet.md` §F.6 | `[D4]` = APPROACH_<G2..G5> AND OOB handle recovery for Tier-2 (Sauzin / Costin / Beukers) AND emeritus eligibility (Beukers only) | (endorsement landings) |
| `[X8]` | 079 Lean venue dispatch envelope (cover-letter finalize + portal walkthrough) | 079 | `w21_lane1_lean_relaunch_decision_packet.md` "Per-option trigger" block | `[D5]` = PICK_<vid> (one of JFR / LMCS / MCS / TCS / OTHER) | (venue submission landing) |
| `[X9]` | 079 Item-26 splice into submission_log.txt | 079 | `submission_log_item26_splice_spec.md` (SHA `732ED67856165923…`) | `[D5]` = PICK_<vid> AND venue submission landing | (submission_log.txt edit) |
| `[X10]` | 079 WITHDRAW_PERMANENTLY sub-envelopes (Zenodo metadata update + arXiv decision) | 079 | `w21_lane1_lean_relaunch_decision_packet.md` "Per-option trigger" / WITHDRAW_PERMANENTLY block | `[D5]` = WITHDRAW_PERMANENTLY | Zenodo record 10.5281/zenodo.19834824 metadata update + Item 25 update |

### L-events (external landings — outside agent control)

| ID | Event | Origin dossier | Substrate anchor | Preconditions | Postconditions |
|---|---|---|---|---|---|
| `[L1]` | 076 reconnaissance dossier landing | 075 / 076 | 076 GATED preflight envelope §0 GOAL | `[X5]` complete | (M6.CC R1-closure path candidate) |
| `[L2]` | PCF-1 v1.4 deposit landing | 074 | handoff §"Recommended next step" §a | `[X1]` complete | (PCF-1 v1.4 absorbable in 077 paper-profile re-pin) |
| `[L3]` | Picture v1.20 deposit landing | 074 | handoff §"Recommended next step" §b + 070 PICTURE-V120-LATE-FIRE-PREFLIGHT | `[X2]` complete | (074 absorbable; v1.19 → v1.20 transition) |
| `[L4]` | Wasow §X.3 OCR landing | 074 | handoff §"Recommended next step" §c + Q-D4-1 | `[X3]` complete | (MEDIUM-HIGH → HIGH upgrade path enabled) |

---

## §D.3 — DAG visualisation (Mermaid graph TD source)

```mermaid
graph TD
    %% W21 LANE-1 absorption (D-events; same-cadence)
    D1[D1: 074 absorb<br/>RATIFY / RATIFY_WITH_AMENDMENT<br/>/ DEFER / OBJECT]
    D2[D2: 075 absorb<br/>verdict ratify +<br/>OQ-W21-LIT-ALT resolve]
    D3[D3: 077 absorb<br/>PICK_Bn / PICK_PAIR<br/>/ PICK_OTHER / DEFER / OBJECT]
    D4[D4: 078 absorb<br/>APPROACH_* / WAIT<br/>/ DEFER / OBJECT]
    D5[D5: 079 absorb<br/>PICK_vid / PICK_OTHER<br/>/ DEFER / WITHDRAW]

    %% Cross-dossier coupling at LANE-1
    D3 -->|DECISION-COUPLED<br/>per [COUPLING-C4]| D4

    %% Post-LANE-1 dispatch (X-events)
    X1[X1: PCF-1 v1.4<br/>amendment cycle]
    X2[X2: Picture v1.20<br/>deposit cycle]
    X3[X3: Wasow X.3<br/>OCR acquisition]
    X4[X4: BT 1933 §§7-9<br/>readthrough 075-class]
    X5[X5: 076 path-δ<br/>literature recon]
    X6[X6: 078 G1<br/>Mazzocco send]
    X7[X7: 078 G2-G5<br/>Garoufalidis/Sauzin/<br/>Costin/Beukers sends]
    X8[X8: 079 Lean<br/>venue dispatch]
    X9[X9: 079 Item-26<br/>splice into<br/>submission_log.txt]
    X10[X10: 079 WITHDRAW<br/>Zenodo+arXiv subs]

    %% D-event → X-event edges
    D1 -->|RATIFY or<br/>RATIFY_WITH_AMENDMENT| X1
    D1 -->|any RATIFY-class<br/>+ Q-D4-3 absorb| X2
    D1 -->|RATIFY_WITH_AMENDMENT<br/>+ HIGH-upgrade| X3
    D2 -->|LIT_HUNT_PATH_DELTA<br/>resolution| X5
    D4 -->|APPROACH_PCF2_MAZZOCCO| X6
    D4 -->|APPROACH_G2..G5<br/>+ OOB recovery| X7
    D5 -->|PICK_vid| X8
    D5 -->|PICK_vid + landing| X9
    D5 -->|WITHDRAW_PERMANENTLY| X10

    %% Parallel/independent
    X4 -.->|parallel to LANE-1<br/>via 073 forward-pointer| D1

    %% L-events (external landings)
    L1[L1: 076 recon<br/>dossier landing]
    L2[L2: PCF-1 v1.4<br/>deposit landing]
    L3[L3: Picture v1.20<br/>deposit landing]
    L4[L4: Wasow X.3<br/>OCR landing]

    X1 --> L2
    X2 --> L3
    X3 --> L4
    X5 --> L1

    %% Downstream coupling: PCF-1 v1.4 → 077 paper-profile re-pin
    L2 -.->|OUTPUT-COUPLED<br/>per [COUPLING-C2]<br/>affects PICK_B1/B4/pairs| D3

    classDef dEvent fill:#e1f5ff,stroke:#0277bd,stroke-width:2px
    classDef xEvent fill:#fff4e1,stroke:#e65100,stroke-width:1px
    classDef lEvent fill:#e8f5e9,stroke:#2e7d32,stroke-width:1px
    class D1,D2,D3,D4,D5 dEvent
    class X1,X2,X3,X4,X5,X6,X7,X8,X9,X10 xEvent
    class L1,L2,L3,L4 lEvent
```

**Note on the L2 → D3 dotted edge:** the PCF-1 v1.4 deposit landing
post-074 dispatch will affect 077 paper-profile if/when 077 is
re-fired (077R) at a future cadence; at W21 LANE-1 the v1.3 anchor
is the substrate. The dotted edge documents the OUTPUT-COUPLED
post-LANE-1 path per [COUPLING-C2].

---

## §D.4 — `<derivation gap>` edges

The following 4 edges / events the relay-080 envelope §7
mentions but that are NOT substrate-anchored in any of the 5
dossier handoffs or 076 GATED preflight envelope at fire time:

| Gap-edge ID | Event mentioned | Substrate-citation status | Surfaced as |
|---|---|---|---|
| `<gap-1>` | arXiv mirror submission (envelope §7) | NOT anchored in 074/075/077/078/079 handoffs nor in 076 GATED envelope | amendment note N-080-2 |
| `<gap-2>` | Zenodo umbrella v2.1 deposit (envelope §7) | 077 D-077-3 mentions umbrella v2.0 reissue as a synth-review question, but NOT as a forward-pointer; no v2.1 named anywhere in dossier substrate | amendment note N-080-3 |
| `<gap-3>` | Item-N splice into submission_log.txt (envelope §7) | 079 has Item-26 splice for Lean (X9 above); 077/074 do NOT specify a submission_log Item-N splice | amendment note N-080-4 |
| `<gap-4>` | 077 portfolio reweave / deposit as a discrete X-event | 077 packet does not name a discrete X-event for any PICK_Bn deposit; only "Synthesizer review of 077 dossier at W21 LANE-1 to pick from the 10-option decision menu" (handoff §"Recommended next step") | amendment note N-080-5 |

These gaps are surfaced for synth review without asserting their
membership in the temporal DAG.

---

## §D.5 — Critical path (longest-precedence chain)

The longest substrate-anchored precedence chain in the DAG is:

  `[D1]` → `[X1]` → `[L2]` → (re-fire 077R if synth chooses) → `[D3]'`

  (4 nodes / 3 edges)

This chain spans the 074 → 077 OUTPUT-COUPLING per [COUPLING-C2]:
074 RATIFY → PCF-1 v1.4 amendment cycle → PCF-1 v1.4 deposit
landing → 077 re-fire at W22+ cadence with v1.4 anchor.

The 075 → 076 chain `[D2]` → `[X5]` → `[L1]` is shorter (3 nodes /
2 edges) but is the active OQ-W21-LITERATURE-ALTERNATIVE-bound
chain at fire time.

The 079 dispatch chain `[D5]` → `[X8]` → (venue first-decision)
→ `[X9]` is parallel to the SIARC-track chains and disjoint at
the paper-set level.

---

## §D.6 — Parallel-firing groups

At W21 LANE-1 absorption, the following events are parallel-safe:

- `[D1]`, `[D2]`, `[D3]`, `[D4]`, `[D5]` are absorbed in the
  single Mon 2026-05-12 AM JST cadence; relative ordering within
  the cadence is synth-internal (cf. Phase E decision-tree
  skeleton).
- `[D4]` carries a DECISION-COUPLED dependency on `[D3]` (per
  [COUPLING-C4]) — synth absorbs `[D3]` first within the cadence,
  then narrows the `[D4]` option-set.
- `[X4]` (BT 1933 §§7-9 readthrough) can fire in W21 LANE-2 in
  parallel with LANE-1 absorption per 074 handoff §"Recommended
  next step" §d.

Post-LANE-1 dispatches `[X1]`, `[X2]`, `[X3]`, `[X5]`, `[X6]`,
`[X7]`, `[X8]`, `[X9]`, `[X10]` are operator-sequenced; the DAG
permits parallel firing of any X-events whose D-event preconditions
are satisfied.

---

End of `temporal_ordering_dag.md`.
