# Decision-Tree Skeleton — 080

**Phase:** E
**Scope:** rooted decision-tree skeleton for synth Mon 2026-05-12
AM JST W21 LANE-1 absorption of the quintet+1 dossier set.

> [META-policy] Per HALT_080_DECISION_OVERREACH discipline this
> tree does NOT mark any leaf as "preferred" / "obvious" / "the
> right pick" / "default" / "recommended". Leaves are listed in
> the order each dossier's decision packet emits them; no leaf
> is pruned. Selection of any path through the tree = synth scope.

> [META-policy] Per HALT_080_OPTION_FABRICATION discipline every
> leaf-tag is verbatim from the corresponding dossier's
> `*_decision_packet.md`. The 075 sub-tree leaves are non-verbatim
> structural labels (`[VERDICT-RATIFY]`, etc.) because 075's
> packet does not enumerate a literal multi-option PICK-class
> menu (cf. 077/079); the structural-label decision is documented
> in `dossier_decision_vector_075.md` §3 + amendment note N-080-6.

---

## §E.1 — Tree topology

```
ROOT [W21 LANE-1 quintet+1 absorption — Mon 2026-05-12 AM JST]
  │
  ├── LANE-1.1  M4 ratification verdict (074)
  │     ├── RATIFY                       (gate-free; M9 reduce {M4,M6.CC}→{M6.CC})
  │     ├── RATIFY_WITH_AMENDMENT        (synth-named amendment scope)
  │     ├── DEFER                        (event-pending: Wasow OCR / picture v1.20 / W21 substrate)
  │     └── OBJECT                       (counter-claim / counter-substrate)
  │
  ├── LANE-1.2  M6.CC R1 chart-map verdict + OQ resolution (075)
  │     ├── [VERDICT-RATIFY-STRUCTURAL_MISMATCH] + LIT_HUNT_PATH_DELTA
  │     │     (synth ratifies STRUCTURAL_MISMATCH and resolves OQ-W21-
  │     │      LITERATURE-ALTERNATIVE = LIT_HUNT_PATH_DELTA → enables 076 fire
  │     │      after identifier pre-verification per copilot-instructions.md)
  │     ├── [VERDICT-RATIFY-STRUCTURAL_MISMATCH] + PATH_GAMMA_T1_SYNTH
  │     │     (synth ratifies STRUCTURAL_MISMATCH and pursues
  │     │      Path-γ T1-Synth analytic-guidance request alternative
  │     │      per 075 handoff §"Recommended next step" §2)
  │     ├── [VERDICT-RATIFY-STRUCTURAL_MISMATCH] + DEFER_OQ_TO_W22
  │     │     (synth ratifies verdict but defers OQ-W21-LITERATURE-
  │     │      ALTERNATIVE resolution to W22+; 076 fire blocked)
  │     └── [VERDICT-OBJECT-STRUCTURAL_FRAMING]
  │           (synth flags issue with the 7-primitive structural
  │            decomposition itself per OQ-075-PRIMITIVE-CANONICAL;
  │            potential 075R re-fire with alternative decomposition)
  │
  ├── LANE-1.3  Portfolio bundle pick (077)
  │     ├── PICK_B1                      (PCF-1 + PCF-2 + T2B; YELLOW)
  │     ├── PICK_B2                      (CT v1.4 + D2-NOTE; YELLOW; G17-close gate)
  │     ├── PICK_B3                      (PCF-2 + T2B; YELLOW)
  │     ├── PICK_B4                      (all 6 papers; YELLOW; major reweave)
  │     ├── PICK_B5                      (status quo; GREEN)
  │     ├── PICK_PAIR_B1+B2              (5/6 record coverage)
  │     ├── PICK_PAIR_B1+B5              (B1 + standalone P3+P4+P6)
  │     ├── PICK_OTHER_PAIR              (synth-named tie-break)
  │     ├── DEFER                        (W22+ cadence)
  │     └── OBJECT                       (077R re-fire amendment scope)
  │
  ├── LANE-1.4  Endorser pick (078)        [DECISION-COUPLED on LANE-1.3]
  │     ├── APPROACH_PCF2_MAZZOCCO       (G1; Mazzocco email VERIFIED; no OOB gate)
  │     ├── APPROACH_PCF2_GAROUFALIDIS   (G2 OPTIONAL; PCF-1-mirror-blocked contingency)
  │     ├── APPROACH_D2NOTE_SAUZIN       (G3; Tier-2 HANDLE_404 OOB recovery required)
  │     ├── APPROACH_D2NOTE_COSTIN       (G4; Tier-2 HANDLE_404 OOB recovery required)
  │     ├── APPROACH_T2B_BEUKERS         (G5; Tier-2 HANDLE_404 + emeritus-eligibility gates)
  │     ├── APPROACH_<other>             (synth-named pair; off the 5 GAP-CANDIDATE set)
  │     ├── WAIT_FOR_TIER2_CONFIRM       (W22 absorbs after OOB recovery)
  │     ├── DEFER                        (other reason; W22+)
  │     └── OBJECT                       (dossier amendment scope)
  │
  └── LANE-1.5  Lean venue pick (079)
        ├── PICK_JFR                     (JFR; U1 5+yr publication-gap activity flag)
        ├── PICK_LMCS                    (LMCS; D2 DOAJ-listing not directly confirmed)
        ├── PICK_MCS                     (MCS; D4 Springer auth-gate information gap)
        ├── PICK_TCS                     (TCS; D1 USD 2,840 APC; D3 turnaround ambiguity; U2 Section-B)
        ├── PICK_OTHER                   (079r1 + 5th venue profile required)
        ├── DEFER                        (W22+ refresh + activity-flag re-check)
        └── WITHDRAW_PERMANENTLY         (Zenodo metadata update + arXiv decision)
```

---

## §E.2 — Per-leaf annotations (downstream coupling + dispatch)

For each leaf, the downstream coupling and dispatch are derived
from Phase C matrix and Phase D DAG.

### LANE-1.1 (074) leaves

| Leaf | Downstream coupling (per [COUPLING-Cn]) | Downstream dispatch (per [Xn]) |
|---|---|---|
| `RATIFY` | [C1] OUTPUT-COUPLED to 075 (M9 gate-set reduces); [C2] OUTPUT-COUPLED to 077 (PCF-1 v1.4 forward-pointer); [C3] AMBIGUOUS to 078 | `[X1]` PCF-1 v1.4 cycle; `[X2]` Picture v1.20 cycle |
| `RATIFY_WITH_AMENDMENT` | same as RATIFY plus amendment-class downstream | `[X1]`; `[X2]`; `[X3]` Wasow OCR (if HIGH-upgrade amendment) |
| `DEFER` | suspends [C2] forward-pointer chain | named-event resolution; no immediate X-event |
| `OBJECT` | suspends [C1]+[C2]+[C3] chains; counter-substrate cycle | re-arbitration cycle (074R) |

### LANE-1.2 (075) leaves

| Leaf | Downstream coupling | Downstream dispatch |
|---|---|---|
| `[VERDICT-RATIFY-STRUCTURAL_MISMATCH] + LIT_HUNT_PATH_DELTA` | activates 076 fire path | `[X5]` 076 path-δ literature recon (gated on identifier pre-verification per copilot-instructions.md post-031 rule) |
| `[VERDICT-RATIFY-STRUCTURAL_MISMATCH] + PATH_GAMMA_T1_SYNTH` | activates Path-γ T1-Synth analytic-guidance branch (069r1 alternative) | future relay envelope `R1_CLOSURE_T1_SYNTH_ANALYTIC_GUIDANCE` (per 075 handoff §"Recommended next step" §2) |
| `[VERDICT-RATIFY-STRUCTURAL_MISMATCH] + DEFER_OQ_TO_W22` | blocks `[X5]` 076 fire; defers OQ-W21-LITERATURE-ALTERNATIVE | no 076 fire at W21+1; carry-forward to W22+ |
| `[VERDICT-OBJECT-STRUCTURAL_FRAMING]` | flags OQ-075-PRIMITIVE-CANONICAL; potential 075R | 075R re-fire with alternative 7-primitive decomposition |

### LANE-1.3 (077) leaves

| Leaf | Downstream coupling (per [COUPLING-C4] DECISION-COUPLED to 078) | Downstream dispatch |
|---|---|---|
| `PICK_B1` | narrows 078 to {Mazzocco, Garoufalidis, Beukers} via {PCF-1, PCF-2, T2B} columns | bundle reweave; per-paper venue selection |
| `PICK_B2` | narrows 078 to {Mazzocco (CT), Sauzin (D2-NOTE), Costin (D2-NOTE)} via {CT, D2-NOTE} columns | G17-close cycle; CT v1.4 publication; D2-NOTE template draft |
| `PICK_B3` | narrows 078 to {Mazzocco/Garoufalidis (PCF-2), Beukers (T2B)} via {PCF-2, T2B} columns | bundle reweave |
| `PICK_B4` | full coverage matrix in-scope (all 6 papers) | major reweave + umbrella reissue |
| `PICK_B5` | full coverage matrix in-scope (per-paper standalone) | none beyond per-paper standalone tracks |
| `PICK_PAIR_B1+B2` | union of B1 + B2 in-scope endorser-paper pairs | both B1 and B2 OOB gates |
| `PICK_PAIR_B1+B5` | B1 OOB gates + 3 standalone | B1 reweave; standalone tracks for P3 + P4 + P6 |
| `PICK_OTHER_PAIR` | synth-named pair scope | tie-break declaration |
| `DEFER` | no LANE-1 coupling activated | W22+ cadence |
| `OBJECT` | 077R re-fire | dossier amendment cycle |

### LANE-1.4 (078) leaves

| Leaf | Downstream coupling | Downstream dispatch |
|---|---|---|
| `APPROACH_PCF2_MAZZOCCO` | none in-matrix; LANE-1.3 PICK_B1/B3/B4/B5 / pairs containing PCF-2 keep this in-scope | `[X6]` G1 Mazzocco send |
| `APPROACH_PCF2_GAROUFALIDIS` | conditional on PCF-1-mirror-blocked (per [C3] AMBIGUOUS) | `[X7]` G2 OPTIONAL send |
| `APPROACH_D2NOTE_SAUZIN` | LANE-1.3 PICK_B2/B4/B5 / pairs containing D2-NOTE keep this in-scope | `[X7]` G3 Sauzin send (after Tier-2 OOB recovery) |
| `APPROACH_D2NOTE_COSTIN` | same as above | `[X7]` G4 Costin send (after Tier-2 OOB recovery) |
| `APPROACH_T2B_BEUKERS` | LANE-1.3 PICK_B1/B3/B4/B5 / pairs containing T2B keep this in-scope | `[X7]` G5 Beukers send (after Tier-2 OOB recovery + emeritus eligibility) |
| `APPROACH_<other>` | synth-named pair off the 5 GAP-CANDIDATE set | template-drafting cycle |
| `WAIT_FOR_TIER2_CONFIRM` | no immediate dispatch | W22 LANE-1 absorption |
| `DEFER` | no LANE-1 coupling activated | W22+ cadence |
| `OBJECT` | 078R re-fire | dossier amendment cycle |

### LANE-1.5 (079) leaves

| Leaf | Downstream coupling | Downstream dispatch |
|---|---|---|
| `PICK_JFR` | none in-matrix (Lean disjoint from SIARC scope per [COUPLING-ANCHOR-079c/d]) | `[X8]` JFR cover-letter finalize + portal walkthrough; `[X9]` Item-26 splice |
| `PICK_LMCS` | none in-matrix | `[X8]` LMCS cover-letter finalize + Episciences walkthrough; `[X9]` Item-26 splice |
| `PICK_MCS` | none in-matrix | `[X8]` MCS cover-letter finalize + Springer Editorial Manager; `[X9]` Item-26 splice |
| `PICK_TCS` | none in-matrix | `[X8]` TCS cover-letter finalize + Elsevier walkthrough; `[X9]` Item-26 splice |
| `PICK_OTHER` | none in-matrix; 079r1 dossier extension required | 079r1 cycle (5th venue profile + revised packet) |
| `DEFER` | none in-matrix | W22+ refresh |
| `WITHDRAW_PERMANENTLY` | none in-matrix | `[X10]` Zenodo metadata update + arXiv-deposit decision |

---

## §E.3 — Cross-leaf compatibility notes

The 5 LANE-1 sub-trees are NOT independent of each other: LANE-1.4
narrowing depends on LANE-1.3's pick (per [COUPLING-C4]
DECISION-COUPLED). The two natural sequencings within the
Mon-AM cadence are:

- **Sequencing-A** (per LANE-1 numbering): absorb LANE-1.1, then
  LANE-1.2, then LANE-1.3, then LANE-1.4, then LANE-1.5. Under
  this sequencing LANE-1.4 narrows after LANE-1.3 completes.
- **Sequencing-B** (DAG-topological): absorb LANE-1.1, LANE-1.2,
  LANE-1.3, LANE-1.5 in any order; LANE-1.4 absorbs last (or
  after LANE-1.3 specifically). Under this sequencing LANE-1.4 is
  the only leaf with an in-cadence dependency.

> [META-policy] The agent does not assert which sequencing synth
> applies. Both are substrate-compatible.

---

## §E.4 — Leaf count summary

| Sub-tree | Leaves | Source decision packet |
|---|---:|---|
| LANE-1.1 (074) | 4 | `w21_lane1_m4_dispatch_packet.md` §E.5 |
| LANE-1.2 (075) | 4 | (structural-label decision; see N-080-6) |
| LANE-1.3 (077) | 10 | `w21_lane1_portfolio_decision_packet.md` §F.E |
| LANE-1.4 (078) | 9 | `w21_lane1_endorser_decision_packet.md` §F.6 |
| LANE-1.5 (079) | 7 | `w21_lane1_lean_relaunch_decision_packet.md` |
| **Total** | **34** | |

Leaf-product cardinality (independent enumeration ignoring
DECISION-COUPLED narrowing): 4 × 4 × 10 × 9 × 7 = **10080** raw
combinations. After [COUPLING-C4] DECISION-COUPLED narrowing of
LANE-1.4 by LANE-1.3 the effective cardinality is reduced
(precise count is synth-scope and not asserted here per
HALT_080_DECISION_OVERREACH discipline).

---

End of `decision_tree_skeleton.md`.
