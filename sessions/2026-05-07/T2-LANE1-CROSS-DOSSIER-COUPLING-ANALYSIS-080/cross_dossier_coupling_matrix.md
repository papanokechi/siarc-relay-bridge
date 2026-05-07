# Cross-Dossier Coupling Matrix — 080

**Phase:** C
**Scope:** 5 × 5 ordered-pair coupling matrix across the 5 LANE-1
quintet dossiers (074 / 075 / 077 / 078 / 079).
**Cell tags:** {DECISION-COUPLED, OUTPUT-COUPLED, TEMPORAL-COUPLED,
INDEPENDENT, AMBIGUOUS, NULL-DIAGONAL}.

> [META-policy] Per HALT_080_COUPLING_FABRICATION discipline every
> non-INDEPENDENT and non-NULL cell carries a substrate-anchor
> citation pointing at a specific dossier handoff or decision-packet
> line / SHA-anchored deliverable. Couplings derived without
> substrate citation are not asserted.

---

## §C.1 — Cell-tag definitions (per envelope §2.C)

| Tag | Definition (verbatim from envelope §2.C) |
|---|---|
| `DECISION-COUPLED` | Origin's pick DIRECTLY constrains target's pick set. |
| `OUTPUT-COUPLED` | Origin's verdict-output is INPUT to target's decision (data-flow coupling, not pick-set constraint). |
| `TEMPORAL-COUPLED` | Origin must complete (decision absorbed and dispatched) BEFORE target can fire its decision or its dispatch. |
| `AMBIGUOUS` | Coupling derivable but its strength is conditional on a synth-pick that itself is in scope. Surfaced as residual question in `cross_dossier_amendment_notes.md`. |
| `INDEPENDENT` | No coupling derivable from substrate. |
| `NULL-DIAGONAL` | A dossier does not couple to itself (matrix diagonal). |

---

## §C.2 — Matrix (rows = origin → columns = target)

| **Origin \\ Target** | **→ 074** | **→ 075** | **→ 077** | **→ 078** | **→ 079** |
|---|---|---|---|---|---|
| **074 →** | NULL-DIAGONAL | OUTPUT-COUPLED | OUTPUT-COUPLED | AMBIGUOUS | INDEPENDENT |
| **075 →** | INDEPENDENT | NULL-DIAGONAL | INDEPENDENT | INDEPENDENT | INDEPENDENT |
| **077 →** | INDEPENDENT | INDEPENDENT | NULL-DIAGONAL | DECISION-COUPLED | INDEPENDENT |
| **078 →** | INDEPENDENT | INDEPENDENT | INDEPENDENT | NULL-DIAGONAL | INDEPENDENT |
| **079 →** | INDEPENDENT | INDEPENDENT | INDEPENDENT | INDEPENDENT | NULL-DIAGONAL |

**Cell counts:** 1 DECISION-COUPLED + 2 OUTPUT-COUPLED + 0 TEMPORAL-
COUPLED + 1 AMBIGUOUS + 16 INDEPENDENT + 5 NULL-DIAGONAL = 25 cells.

---

## §C.3 — Non-NULL non-INDEPENDENT cell documentation

### [COUPLING-C1] 074 → 075 — OUTPUT-COUPLED

- **Cell tag:** OUTPUT-COUPLED
- **Origin-side trigger condition:** `RATIFY` or
  `RATIFY_WITH_AMENDMENT` from 074 dispatch packet §E.5.
- **Target-side affected option(s):** All 075 OQ-class items
  inherit the M9-gating frame change. After 074 RATIFY, the M9
  gating set reduces to `{M6.CC}` (075's scope only). 075 verdict
  (STRUCTURAL_MISMATCH) is unchanged at LANE-1 absorption, but its
  downstream weight as the "sole remaining M9 gate" is set by
  074's verdict-output.
- **Substrate anchor:** 074 dispatch packet
  `w21_lane1_m4_dispatch_packet.md` §E.5 verbatim:
  > "synthesizer accepts the 068 verdict at MEDIUM-HIGH confidence
  >  as-is and authorises the M9 gating-set reduction
  >  `{M4, M6.CC} → {M6.CC}`."

  (28 words; ≤ 50-word ceiling PASS.)
  Cross-anchor: 075 `synthesizer_decision_packet.md` §E.6 lists
  `OQ-W21-LITERATURE-ALTERNATIVE` strengthened to "path-δ literature
  acquisition is required" — this strengthening interacts with the
  M9 gate-reduction frame.

### [COUPLING-C2] 074 → 077 — OUTPUT-COUPLED

- **Cell tag:** OUTPUT-COUPLED (with TEMPORAL-COUPLED secondary
  reading documented in §C.4 below)
- **Origin-side trigger condition:** `RATIFY` or
  `RATIFY_WITH_AMENDMENT` from 074 dispatch packet §E.5; alternatively
  `DEFER` (delays the forward-pointer chain) or `OBJECT` (suspends
  the forward-pointer chain).
- **Target-side affected option(s):** `PICK_B1`, `PICK_B4`,
  `PICK_PAIR_B1+B2`, `PICK_PAIR_B1+B5` — all bundle options
  containing PCF-1 v1.3 — inherit a downstream PCF-1 v1.4 amendment
  cycle. `PICK_B5` status quo carries the M4 ratification quality
  forward as per-paper rationale credibility.
- **Substrate anchor:** 074 handoff §"Recommended next step" §a:
  > "PCF-1 v1.4 amendment cycle (G12 jurisdiction, Q-D4-2):
  >  forward-pointed if synthesizer issues `RATIFY` or
  >  `RATIFY_WITH_AMENDMENT`."

  (16 words; ≤ 50-word ceiling PASS.)
  Cross-anchor: 077 `paper_profile_pcf1_v13.md` (SHA
  `4E0E2FA5F515532F…`) anchors PCF-1 v1.3 as the current portfolio
  version; PCF-1 v1.4 amendment forward-pointed in 074 forward-
  pointer (a) would update this anchor.

### [COUPLING-C3] 074 → 078 — AMBIGUOUS

- **Cell tag:** AMBIGUOUS
- **Origin-side trigger condition:** `RATIFY` or
  `RATIFY_WITH_AMENDMENT` from 074 → triggers PCF-1 v1.4
  amendment cycle (per [COUPLING-ANCHOR-074a]) → may affect PCF-1
  mirror status → may activate `APPROACH_PCF2_GAROUFALIDIS` G2
  OPTIONAL framing in 078.
- **Target-side affected option(s):** `APPROACH_PCF2_GAROUFALIDIS`
  (G2) is the conditionally-firing option whose firing depends on
  whether "PCF-1 mirror is blocked by page-count-drift carry" per
  078 packet §F.6 verbatim.
- **Coupling-strength conditionality:** the coupling chain spans
  multiple synth-pick mediations (074 verdict-class pick + PCF-1
  amendment scope choice + downstream PCF-1 mirror page-count-
  drift outcome). All three are in-scope synth-side picks at or
  beyond W21 LANE-1.
- **Substrate anchor:** 078 packet
  `w21_lane1_endorser_decision_packet.md` §F.6 verbatim:
  > "operator sends G2 template … only needed if PCF-1 mirror
  >  is blocked by page-count-drift carry."

  (18 words; ≤ 50-word ceiling PASS.)
  Cross-anchor: 074 handoff §"Recommended next step" §a (PCF-1
  v1.4 amendment forward-pointer).
- **AMBIGUOUS rationale:** strength of the coupling depends on
  074's pick AND the operator-side PCF-1 mirror status that 080
  cannot resolve from substrate alone. Surfaced in
  `cross_dossier_amendment_notes.md` as note N-080-1.

### [COUPLING-C4] 077 → 078 — DECISION-COUPLED

- **Cell tag:** DECISION-COUPLED
- **Origin-side trigger condition:** any 077 PICK_Bn pick narrows
  the in-scope paper set, which directly narrows the 078
  endorser-paper pairing options.
  - `PICK_B1` (PCF-1 + PCF-2 + T2B) → in-scope endorser-paper
    pairs ⊆ {PCF-1, PCF-2, T2B} columns.
  - `PICK_B2` (CT v1.4 + D2-NOTE) → in-scope endorser-paper
    pairs ⊆ {CT, D2-NOTE} columns. APPROACH_PCF2_MAZZOCCO and
    APPROACH_PCF2_GAROUFALIDIS become out-of-bundle scope.
  - `PICK_B3` (PCF-2 + T2B) → in-scope ⊆ {PCF-2, T2B}.
  - `PICK_B4` (all 6 papers) → full coverage matrix in-scope.
  - `PICK_B5` (status quo) → full coverage matrix in-scope per
    each paper's standalone venue track.
- **Target-side affected option(s):** all 5 named APPROACH_*
  options. The narrowing is column-set narrowing on the 6 × 6
  coverage matrix.
- **Substrate anchor:** 078
  `endorser_paper_coverage_matrix.md` (SHA
  `A47F9C9686E6A1E2…`, 13129 B, 208 lines) — the 6 endorser × 6
  paper matrix with active-row tally 7 EXISTING + 5 GAP-CANDIDATE
  + 18 SKIP-FIT-WEAK; cross-anchor 077
  `bundle_configuration_matrix.md` (SHA `9188DEE5C576E832…`,
  12751 B) which enumerates which papers are in each bundle.
  Cross-coupling references: [COUPLING-ANCHOR-078b] (this dossier
  vector §7) + [COUPLING-ANCHOR-077b] / [COUPLING-ANCHOR-077c]
  (077 vector §7).

---

## §C.4 — Secondary readings (TEMPORAL aspect of [COUPLING-C2])

[COUPLING-C2] 074 → 077 admits a secondary TEMPORAL-COUPLED
reading: the post-LANE-1 dispatch chain is

  074 RATIFY (synth absorbed) → PCF-1 v1.4 amendment cycle
    (operator dispatches) → PCF-1 v1.4 deposit → portfolio reweave
    affects 077 B1/B4 final state

This temporal precedence is a substrate-derivable coupling, but
the OUTPUT-COUPLED reading (data-flow primacy) was selected as the
primary cell tag because the prompt's own §2.C example uses
074 → 077 for both readings. Documentation of both axes is
preserved here for synth review.

---

## §C.5 — INDEPENDENT cell rationale (16 cells)

The 16 INDEPENDENT cells split into 4 substrate-derivable rationale
groups:

### Group 1 — 075 row (4 INDEPENDENT cells: 075→074, 075→077, 075→078, 075→079)

075's STRUCTURAL_MISMATCH verdict is M6.CC scope and does not
constrain or feed any of 074's M4-ratification picks, 077's
portfolio bundle picks, 078's endorser picks, or 079's Lean venue
picks. The 075 → 076 forward-pointer (path-δ literature
acquisition gated on OQ-W21-LITERATURE-ALTERNATIVE) lies outside
the 5-dossier matrix scope (076 is GATED preflight).
Substrate anchor: 075 `synthesizer_decision_packet.md` §E.5 +
§E.6 (carry-forward OQs unchanged at 075 scope).

### Group 2 — 077 row (3 INDEPENDENT cells: 077→074, 077→075, 077→079)

077's portfolio pick does not constrain 074 (074 is locked at fire
time per 077 D-077-6 "077 dossier validity independent"); does not
constrain 075 (M6.CC scope is independent of portfolio
configuration); does not constrain 079 (Lean / Tunnell-CNP is
out-of-scope for 077 portfolio per [COUPLING-ANCHOR-077h]).
Substrate anchor: 077 `discrepancy_log.json` D-077-6 + 077 paper-
profile inventory (6 SIARC-track papers; Lean absent).

### Group 3 — 078 row (4 INDEPENDENT cells: 078→074, 078→075, 078→077, 078→079)

078's endorser pick is downstream of 077's bundle pick (077 → 078
DECISION-COUPLED). The reverse direction 078 → 077 is INDEPENDENT
because 078 does not unilaterally constrain bundle picks. 078 does
not affect 074 ratification (M4 closure-path scope) or 075 chart-
map verdict. 078 does not couple to 079 because Lean is out-of-
scope for 078 endorser coverage (per [COUPLING-ANCHOR-078c]).
Substrate anchor: 078 `endorser_paper_coverage_matrix.md` (Lean
absent from the 6-paper coverage axis).

### Group 4 — 079 row (4 INDEPENDENT cells: 079→074, 079→075, 079→077, 079→078)

079's Lean venue pick does not couple to any SIARC-track dossier
because the Lean/Tunnell-CNP paper is disjoint from the 6 SIARC
papers in 074/075/077/078 scope. Substrate anchor:
[COUPLING-ANCHOR-079c] + [COUPLING-ANCHOR-079d] (Lean is NOT in
the 077 paper-profile inventory and NOT in the 078 endorser
coverage matrix).

### Auxiliary — 074 → 079 INDEPENDENT (1 cell)

074's M4 ratification is M4-class scope (CT v1.3 / D2-NOTE
substrate); 079 is Lean / Tunnell-CNP relaunch. Disjoint scopes.
No substrate coupling at 080 fire time.

---

## §C.6 — Strongest couplings (DECISION-COUPLED tier)

Top-3 ranking by number of substrate anchors cited:

1. **[COUPLING-C4] 077 → 078 — DECISION-COUPLED** — 2 substrate
   anchors (`endorser_paper_coverage_matrix.md` 6×6 matrix +
   `bundle_configuration_matrix.md` 5-bundle composition); 5
   PICK_Bn options each map to a distinct in-scope endorser-paper
   pair set.
2. **[COUPLING-C2] 074 → 077 — OUTPUT-COUPLED** — 2 substrate
   anchors (074 handoff §"Recommended next step" §a + 077
   `paper_profile_pcf1_v13.md`); PCF-1 v1.4 amendment cycle
   forward-pointer affects 4 of 5 PICK_Bn options (B1/B4/pairs).
3. **[COUPLING-C1] 074 → 075 — OUTPUT-COUPLED** — 2 substrate
   anchors (074 dispatch packet §E.5 M9 gating-set reduction
   verbatim + 075 `synthesizer_decision_packet.md` §E.6
   OQ-W21-LITERATURE-ALTERNATIVE strengthening).

[COUPLING-C3] 074 → 078 — AMBIGUOUS — is excluded from the
strongest-couplings ranking because its strength is synth-pick-
mediated; it is enumerated in `cross_dossier_amendment_notes.md`
N-080-1 instead.

---

## §C.7 — Synth-pick selection scope reservation

> [META-policy] Per HALT_080_DECISION_OVERREACH discipline this
> matrix surfaces couplings as substrate-anchored facts. Selection
> of any path through the coupling = synth scope at W21 LANE-1.
> The matrix does not compute a "preferred" combination of options.
> The 1 DECISION-COUPLED cell + 2 OUTPUT-COUPLED cells + 1
> AMBIGUOUS cell are inventory-tier facts, not synth-side
> directives.

---

End of `cross_dossier_coupling_matrix.md`.
