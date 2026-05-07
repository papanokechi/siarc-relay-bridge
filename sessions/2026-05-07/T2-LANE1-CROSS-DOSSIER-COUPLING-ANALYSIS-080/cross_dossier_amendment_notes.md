# Cross-Dossier Amendment Notes — 080

**Phase:** F
**Scope:** numbered amendment notes for AMBIGUOUS cells in the
Phase C matrix and `<derivation gap>` edges in the Phase D DAG,
plus structural-label declarations from Phase B / E.

> [META-policy] Per HALT_080_NEW_QUESTION_INTRODUCED discipline
> every note traces back to an AMBIGUOUS cell, a `<derivation
> gap>` edge, or a structural-label declaration documented in
> Phase B / E. No question is introduced that does not derive
> from Phase C / D / B / E outputs.

> [META-policy] Per FIXED ENTRY TEMPLATE in envelope §2.F each
> note's "Synth question" is one of:
>   - "Does &lt;X&gt; constrain &lt;Y&gt; under condition &lt;Z&gt;?"
>   - "Should &lt;event-A&gt; precede &lt;event-B&gt;?"

---

## N-080-1 — [COUPLING-C3] 074 → 078 AMBIGUOUS strength

- **Coupling-or-edge identifier:** [COUPLING-C3] (Phase C
  cross_dossier_coupling_matrix.md §C.3)
- **Substrate gap:** the coupling chain 074 RATIFY → PCF-1 v1.4
  amendment → PCF-1 mirror status → 078 G2 OPTIONAL fire spans 3
  synth-pick mediations (074 verdict-class pick + RATIFY_WITH_
  AMENDMENT scope choice + PCF-1 mirror page-count-drift outcome).
  Strength of the coupling cannot be resolved from substrate at
  fire time.
- **Synth question:** "Does 074 RATIFY (or RATIFY_WITH_AMENDMENT)
  constrain 078 APPROACH_PCF2_GAROUFALIDIS under the condition
  that the PCF-1 mirror page-count-drift outcome is observed
  post-LANE-1 dispatch?"
- **Origin dossier:** 074
- **Target dossier (or post-LANE-1 envelope):** 078 (in-matrix
  target); X1 PCF-1 v1.4 amendment cycle (post-LANE-1 envelope)
- **Resolvability:** SYNTH_PICK_CLOSES (LANE-1.1 + LANE-1.4 picks
  jointly resolve the chain; W21 LANE-1 in-cadence)
- **Suggested LANE-1 disposition tag:** TRIAGE (synth absorbs but
  does not necessarily commit at LANE-1; can defer 078 G2 fire
  decision to W22+ if PCF-1 mirror status remains uncertain)

---

## N-080-2 — `<gap-1>` arXiv mirror submission (envelope §7)

- **Coupling-or-edge identifier:** `<gap-1>` (Phase D
  temporal_ordering_dag.md §D.4)
- **Substrate gap:** relay-080 envelope §7 lists "arXiv mirror
  submission (gated on endorsement send landings)" as a post-
  LANE-1 envelope but no mention exists in any of 074/075/077/
  078/079 handoffs or in 076 GATED preflight envelope.
- **Synth question:** "Should the arXiv mirror submission event
  precede or follow the corresponding endorsement landings (per
  envelope §7 wording 'gated on endorsement send landings')?"
- **Origin dossier:** N/A (envelope §7 only)
- **Target dossier (or post-LANE-1 envelope):** future 081+
  envelope (post-W21 LANE-1 dispatch)
- **Resolvability:** REQUIRES_NEW_SUBSTRATE (a new dossier or
  spec amendment must inventory the arXiv mirror event as
  post-LANE-1 X-event with explicit dossier anchoring)
- **Suggested LANE-1 disposition tag:** DEFER (W22+ relay envelope
  to inventory arXiv mirror as discrete X-event)

---

## N-080-3 — `<gap-2>` Zenodo umbrella v2.1 deposit (envelope §7)

- **Coupling-or-edge identifier:** `<gap-2>` (Phase D §D.4)
- **Substrate gap:** envelope §7 lists "Zenodo umbrella v2.1
  deposit (gated on 077 PICK_Bn + Lean venue landing)" as a post-
  LANE-1 envelope. 077 D-077-3 raises the umbrella v2.0 reissue
  question for synth review but does NOT name a v2.1 version or
  forward-point a deposit cycle.
- **Synth question:** "Does 077 PICK_Bn (any of B1/B2/B3/B4/B5/
  pairs) constrain Zenodo umbrella v2.1 deposit timing under the
  condition that Lean venue landing precedes the deposit?"
- **Origin dossier:** 077 (umbrella v2.0 substrate); 079 (Lean
  venue landing precondition per envelope §7)
- **Target dossier (or post-LANE-1 envelope):** future 081+
  envelope
- **Resolvability:** SYNTH_PICK_CLOSES (LANE-1.3 PICK_Bn determines
  whether umbrella v2.1 is in scope; OBJECT or DEFER would suspend
  the deposit) AND REQUIRES_NEW_SUBSTRATE (v2.1 numbering /
  deposit-cycle envelope text needs to be drafted)
- **Suggested LANE-1 disposition tag:** TRIAGE (synth absorbs the
  umbrella reissue question via 077 D-077-3 directly; v2.1
  numbering is post-LANE-1 substrate)

---

## N-080-4 — `<gap-3>` Item-N splice (envelope §7)

- **Coupling-or-edge identifier:** `<gap-3>` (Phase D §D.4)
- **Substrate gap:** envelope §7 names "Item-26 splice into
  submission_log.txt (gated on Lean venue landing)" — this maps
  to 079 X9 in the substrate-anchored DAG. Envelope §7 also
  alludes to "Item-N splice" with N unspecified, suggesting
  multiple submission_log entries may need updating across the 5
  dossiers (e.g., Item-25 update for WITHDRAW per 079, additional
  items for 077 portfolio dispatches if any).
- **Synth question:** "Should the Item-26 splice (079 X9) precede
  or follow any 077-side submission_log entries that may need
  updating under PICK_Bn?"
- **Origin dossier:** 079 (X9 substrate-anchored); 077 (potential
  unenumerated submission_log entries)
- **Target dossier (or post-LANE-1 envelope):** future 081+
  envelope (sequenced submission_log edits)
- **Resolvability:** SYNTH_PICK_CLOSES (LANE-1.3 + LANE-1.5 picks
  jointly resolve the sequencing) AND REQUIRES_NEW_SUBSTRATE
  (per-bundle Item-N splice spec needs drafting if 077
  PICK_Bn requires submission_log updates)
- **Suggested LANE-1 disposition tag:** UNGATE (Item-26 for 079
  is independent and can fire on D5+L-event; cross-coupling to
  077 can be deferred)

---

## N-080-5 — `<gap-4>` 077 portfolio reweave / deposit X-event

- **Coupling-or-edge identifier:** `<gap-4>` (Phase D §D.4)
- **Substrate gap:** 077 packet does not name a discrete X-event
  for any PICK_Bn deposit. The handoff says "Synthesizer review
  of 077 dossier at W21 LANE-1 to pick from the 10-option decision
  menu. If `OBJECT` is selected, a 077R amendment fires with
  synth-supplied scope; if `DEFER`, W22 LANE-1 (~2026-05-19 AM
  JST) is the next eligible cadence." But for the PICK_Bn options
  themselves, the post-LANE-1 dispatch is implicit.
- **Synth question:** "Should the 077 PICK_Bn dispatch envelope
  precede or follow the 074 RATIFY → PCF-1 v1.4 chain (X1)?"
- **Origin dossier:** 077
- **Target dossier (or post-LANE-1 envelope):** future 081+
  envelope (077 dispatch envelope per chosen bundle)
- **Resolvability:** SYNTH_PICK_CLOSES (LANE-1.1 + LANE-1.3 picks
  jointly determine whether v1.3 or v1.4 anchor binds the bundle)
- **Suggested LANE-1 disposition tag:** TRIAGE (synth weighs
  whether to pin 077 to v1.3 anchors at LANE-1 deposit time, or
  defer 077 deposit until PCF-1 v1.4 lands)

---

## N-080-6 — 075 sub-tree structural-label leaves

- **Coupling-or-edge identifier:** Phase B / E structural-label
  decision (`dossier_decision_vector_075.md` §3 + Phase E §E.1
  LANE-1.2 sub-tree)
- **Substrate gap:** 075's `synthesizer_decision_packet.md` does
  not enumerate a literal multi-option PICK-class menu (cf. 077's
  10 options or 079's 7 options). The packet emits a single
  verdict (STRUCTURAL_MISMATCH) plus a contingent-076 forward-
  pointer plus 4 carry-forward + 2 NEW open questions. The 4
  LANE-1.2 leaves enumerated in `decision_tree_skeleton.md` are
  agent-constructed structural-label leaves derived from 075
  handoff §"Recommended next step" §1+§2 and 075 Anomalies "Open
  questions for Claude".
- **Synth question:** "Does the 4-leaf structural-label
  decomposition of 075 LANE-1.2 (LIT_HUNT_PATH_DELTA /
  PATH_GAMMA_T1_SYNTH / DEFER_OQ_TO_W22 / OBJECT_STRUCTURAL_FRAMING)
  capture the synth-side decision space adequately, or should 075
  emit a literal multi-option PICK-class menu in a future re-fire?"
- **Origin dossier:** 075
- **Target dossier (or post-LANE-1 envelope):** future 075R or
  envelope-spec amendment for 075-class dossiers
- **Resolvability:** SYNTH_PICK_CLOSES at LANE-1.2 absorption
  (synth selects one of the 4 structural-label leaves OR articulates
  a 5th not in the list); also REQUIRES_NEW_SUBSTRATE (a future
  spec revision for verdict-only dossiers may want to canonicalize
  the structural-label leaf set)
- **Suggested LANE-1 disposition tag:** TRIAGE

---

## N-080-7 — 075 OQ-075-PRIMITIVE-CANONICAL canonicalization scope

- **Coupling-or-edge identifier:** 075 Anomalies "Open questions
  for Claude" → OQ-075-PRIMITIVE-CANONICAL (handoff §"Anomalies
  and open questions" §"Open questions for Claude")
- **Substrate gap:** 075 used a 7-primitive decomposition
  {domain, codomain, functional form, cardinality, sectorial
  structure, constraint structure, mathematical type} for the
  Phase B + Phase C structural-form check. The handoff explicitly
  asks "is the 7-primitive decomposition the canonical
  operationalization of 'syntactic form' for chart-map ↔ substrate
  comparisons, or should W21 LANE-1 review propose an alternative
  decomposition?" This bears on the [VERDICT-OBJECT-STRUCTURAL_FRAMING]
  leaf.
- **Synth question:** "Does the 075 7-primitive decomposition
  constrain the synth's structural-form-comparison verdict under
  the condition that an alternative decomposition would yield a
  different match-vs-mismatch tally?"
- **Origin dossier:** 075
- **Target dossier (or post-LANE-1 envelope):** 075R (potential
  re-fire) or envelope-spec amendment for structural-form-check
  dossiers
- **Resolvability:** SYNTH_PICK_CLOSES (synth canonicalises or
  defers); also REQUIRES_NEW_SUBSTRATE if alternative decomposition
  is proposed
- **Suggested LANE-1 disposition tag:** HOLD (verdict ratification
  is independent of canonicalization; canonicalization can be
  deferred without affecting STRUCTURAL_MISMATCH outcome at
  substrate-inventory scope)

---

## N-080-8 — 075 OQ-075-076-DRAFTING-LANE timing

- **Coupling-or-edge identifier:** 075 Anomalies "Open questions
  for Claude" → OQ-075-076-DRAFTING-LANE
- **Substrate gap:** 075 handoff explicitly asks: "should 076
  drafting wait for W21 LANE-1 lit-alternative resolution, or can
  a substrate-inventory 076 (sans acquisition decision) fire
  immediately?" 076 GATED preflight envelope §0 GATES line says
  "FIRE-GATED on W21 LANE-1 (Mon 2026-05-12 AM JST) synthesizer
  resolution of OQ-W21-LITERATURE-ALTERNATIVE = LIT_HUNT_PATH_
  DELTA confirmation" — but the question of whether the 076 draft
  itself can be authored as substrate-only (without acquisition
  decision) remains open.
- **Synth question:** "Should the 076 substrate-only draft
  authoring precede the LANE-1 OQ-W21-LITERATURE-ALTERNATIVE
  resolution, or must it follow?"
- **Origin dossier:** 075
- **Target dossier (or post-LANE-1 envelope):** 076 (drafting
  timing); relay-prompt-drafter authority question
- **Resolvability:** SYNTH_PICK_CLOSES (LANE-1.2 absorption
  determines 076 fire path)
- **Suggested LANE-1 disposition tag:** TRIAGE (075 has already
  drafted the 076 envelope text as PREFLIGHT-DRAFT at SHA
  `6A33C3F16151CC33…`; the question is fire-permission, not
  authoring-permission)

---

## §F.9 — Amendment note count summary

| Note ID | Origin | Disposition tag | Resolvability |
|---|---|---|---|
| N-080-1 | [COUPLING-C3] AMBIGUOUS | TRIAGE | SYNTH_PICK_CLOSES |
| N-080-2 | `<gap-1>` arXiv mirror | DEFER | REQUIRES_NEW_SUBSTRATE |
| N-080-3 | `<gap-2>` Zenodo v2.1 | TRIAGE | SYNTH_PICK_CLOSES + REQUIRES_NEW_SUBSTRATE |
| N-080-4 | `<gap-3>` Item-N splice | UNGATE | SYNTH_PICK_CLOSES + REQUIRES_NEW_SUBSTRATE |
| N-080-5 | `<gap-4>` 077 reweave X-event | TRIAGE | SYNTH_PICK_CLOSES |
| N-080-6 | 075 structural-label leaves | TRIAGE | SYNTH_PICK_CLOSES + REQUIRES_NEW_SUBSTRATE |
| N-080-7 | 075 OQ-PRIMITIVE-CANONICAL | HOLD | SYNTH_PICK_CLOSES + REQUIRES_NEW_SUBSTRATE |
| N-080-8 | 075 OQ-076-DRAFTING-LANE | TRIAGE | SYNTH_PICK_CLOSES |

**Total amendment notes:** 8.
- TRIAGE: 5 (N-080-1, N-080-3, N-080-5, N-080-6, N-080-8)
- DEFER: 1 (N-080-2)
- UNGATE: 1 (N-080-4)
- HOLD: 1 (N-080-7)

Disposition-tag counts surfaced for synth weighing without
asserting a synth-side ranking.

---

End of `cross_dossier_amendment_notes.md`.
