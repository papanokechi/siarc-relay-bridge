# W21 LANE-1 Synth Absorption Aid — 080

**Phase:** G
**Target reader:** T1-Synth (Claude.ai LANE-1) for Sun 2026-05-11
evening JST pre-read so Mon 2026-05-12 AM JST is verdict-only.
**Source:** consolidated from Phase B/C/D/E/F outputs in this 080
session directory.

---

## §G.1 — W21 LANE-1 quintet+1 fire summary

Bridge HEAD at 080 fire time: **`72f9850`** (post-079 LANDED).

| Dossier | Verdict tag | Bridge commit | Decision packet | Options |
|---|---|---|---|---:|
| 074 | DOSSIER_COMPLETE | `9596c21` | `w21_lane1_m4_dispatch_packet.md` | 4 |
| 075 | STRUCTURAL_MISMATCH | `5137155` | `synthesizer_decision_packet.md` | 4 (structural-label; see N-080-6) |
| 077 | DOSSIER_COMPLETE | `49f3423` | `w21_lane1_portfolio_decision_packet.md` | 10 |
| 078 | DOSSIER_PARTIAL | `32b808b` | `w21_lane1_endorser_decision_packet.md` | 9 |
| 079 | DOSSIER_COMPLETE | `72f9850` | `w21_lane1_lean_relaunch_decision_packet.md` | 7 |
| 076 | PREFLIGHT_DRAFT (GATED) | (not landed) | `tex/submitted/control center/prompt/076_t3_path_delta_literature_recon.txt` | (n/a — fire-gated on LANE-1.2 resolution) |

Aggregate AEAL claims across 5 dossiers: **46** (10 + 10 + 7 + 9 + 10).
Aggregate halts triggered: **0 / 50** envelope halts evaluated.

---

## §G.2 — Top-3 strongest couplings (DECISION-COUPLED tier)

Per `cross_dossier_coupling_matrix.md` §C.6:

1. **[COUPLING-C4] 077 → 078 — DECISION-COUPLED**
   - 077 PICK_Bn narrows the 6 × 6 endorser-paper coverage matrix
     column-set, which directly narrows 078 APPROACH_* options.
   - Substrate anchors: `endorser_paper_coverage_matrix.md` (SHA
     `A47F9C9686E6A1E2…`) + `bundle_configuration_matrix.md`
     (SHA `9188DEE5C576E832…`).

2. **[COUPLING-C2] 074 → 077 — OUTPUT-COUPLED**
   - 074 RATIFY → PCF-1 v1.4 amendment cycle forward-pointer
     affects 4 of 5 PICK_Bn options (B1/B4/pairs containing B1).
   - Substrate anchors: 074 handoff §"Recommended next step" §a +
     077 `paper_profile_pcf1_v13.md` (SHA `4E0E2FA5F515532F…`).

3. **[COUPLING-C1] 074 → 075 — OUTPUT-COUPLED**
   - 074 RATIFY → M9 gating-set reduction `{M4, M6.CC} → {M6.CC}`,
     which sets the downstream weight of 075's STRUCTURAL_MISMATCH
     verdict as "sole remaining M9 gate".
   - Substrate anchors: 074 dispatch packet §E.5 + 075
     `synthesizer_decision_packet.md` §E.6 OQ-W21-LITERATURE-
     ALTERNATIVE strengthening.

[COUPLING-C3] 074 → 078 — AMBIGUOUS — surfaced separately as
amendment note N-080-1.

Cell distribution: 1 DECISION-COUPLED + 2 OUTPUT-COUPLED + 0
TEMPORAL-COUPLED + 1 AMBIGUOUS + 16 INDEPENDENT + 5 NULL-DIAGONAL
= 25 cells.

---

## §G.3 — Temporal DAG critical path

Per `temporal_ordering_dag.md` §D.5 longest-precedence chain:

  `[D1]` 074 absorb → `[X1]` PCF-1 v1.4 amendment cycle → `[L2]`
  PCF-1 v1.4 deposit landing → (re-fire 077R if synth chooses) →
  `[D3]'` 077 W22+ pick under v1.4 anchor

(4 nodes / 3 edges; spans the 074 → 077 OUTPUT-COUPLED chain.)

The 075 → 076 chain is shorter:

  `[D2]` 075 absorb + LIT_HUNT_PATH_DELTA resolution → `[X5]` 076
  path-δ literature recon → `[L1]` 076 reconnaissance dossier
  landing

(3 nodes / 2 edges.) `[X5]` is fire-gated on identifier
pre-verification per copilot-instructions.md post-031 rule.

`[D5]` 079 dispatch chain `[D5]` → `[X8]` → (venue first-decision)
→ `[X9]` is parallel to the SIARC-track chains and disjoint at
the paper-set level (Lean / Tunnell-CNP not in 077 / 078 scope).

---

## §G.4 — Decision-tree skeleton root + 5 LANE-1.* nodes

Per `decision_tree_skeleton.md` §E.1:

```
ROOT [W21 LANE-1 quintet+1 absorption — Mon 2026-05-12 AM JST]
  ├── LANE-1.1  M4 ratification verdict (074)              [4 leaves]
  ├── LANE-1.2  M6.CC R1 chart-map + OQ resolution (075)   [4 leaves]
  ├── LANE-1.3  Portfolio bundle pick (077)                [10 leaves]
  ├── LANE-1.4  Endorser pick (078) [DECISION-COUPLED ← 1.3] [9 leaves]
  └── LANE-1.5  Lean venue pick (079)                      [7 leaves]
```

Total leaves: 34. Leaf-product cardinality (independent
enumeration ignoring DECISION-COUPLED narrowing): 4 × 4 × 10 × 9
× 7 = **10080** raw combinations.

Two natural sequencings within the Mon-AM cadence:
- **Sequencing-A** (LANE-1 numbering order): 1.1 → 1.2 → 1.3 →
  1.4 → 1.5
- **Sequencing-B** (DAG-topological): 1.4 absorbs after 1.3;
  others in any order

The agent does not assert which sequencing applies.

---

## §G.5 — Outstanding amendment notes

Per `cross_dossier_amendment_notes.md` §F.9:

**Total:** 8 amendment notes.

Top-3 entries by LANE-1 immediacy (TRIAGE-tagged, in-cadence
resolvable):

1. **N-080-1** — [COUPLING-C3] 074 → 078 AMBIGUOUS strength
   (synth resolves at LANE-1.1 + LANE-1.4 jointly).
2. **N-080-6** — 075 sub-tree structural-label leaves
   (synth selects one of the 4 structural-label leaves at
   LANE-1.2 OR articulates a 5th not in the agent-emitted list).
3. **N-080-8** — 075 OQ-076-DRAFTING-LANE timing (synth's
   LIT_HUNT_PATH_DELTA / PATH_GAMMA / DEFER pick at LANE-1.2
   fixes this).

Disposition-tag breakdown: TRIAGE 5 / DEFER 1 / UNGATE 1 / HOLD 1.

---

## §G.6 — Pointers to full Phase B/C/D/E/F outputs

All in `sessions/2026-05-07/T2-LANE1-CROSS-DOSSIER-COUPLING-ANALYSIS-080/`:

- Phase A: `substrate_anchor_shas.md`
- Phase B: `dossier_decision_vector_074.md` /
  `dossier_decision_vector_075.md` /
  `dossier_decision_vector_077.md` /
  `dossier_decision_vector_078.md` /
  `dossier_decision_vector_079.md`
- Phase C: `cross_dossier_coupling_matrix.md`
- Phase D: `temporal_ordering_dag.md`
- Phase E: `decision_tree_skeleton.md`
- Phase F: `cross_dossier_amendment_notes.md`
- Phase H: `forbidden_verb_scan.md` /
  `quote_length_scan.md` / `coupling_overreach_scan.md`
- Phase I: `claims.jsonl` / `halt_log.json` /
  `discrepancy_log.json` / `unexpected_finds.json`
- Phase J: `handoff.md`

---

> [META-policy] Per HALT_080_DECISION_OVERREACH discipline this
> aid does not assert which combination of LANE-1.* leaves synth
> picks. Selection of any path through the coupling = synth
> scope at W21 LANE-1.

End of `w21_lane1_synth_absorption_aid.md`.
