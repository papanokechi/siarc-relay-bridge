# Handoff — Q20-CONJ33A-PROOF-UPGRADE
**Date:** 2026-05-03
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~50 minutes
**Status:** PARTIAL (verdict `UPGRADE_PARTIAL_PENDING_LITERATURE`;
Phases A + B complete; Phase C halted at gate;
Phase E deferred per Q20 prompt §4)

## What was accomplished

Arbitrated Q20 (whether the Newton-polygon argument used in
Prompt 012 / XI0-D3-DIRECT constitutes a proof of D2-NOTE
Conj 3.3.A* at all `d ≥ 2`).  Phase A re-derives the
characteristic-root identity `ξ_0 = d / β_d^{1/d}` symbolically
in sympy at general d, with no case split, and verifies it
sympy/mpmath-exactly at `d ∈ {2, 3, 4}`
(verdict signal `A_DIRECT_IDENTITY`).  Phase B walks the
d=2 proof template (D2-NOTE v1 Prop 3.3.A + CT v1.3 Prop xi0)
line-by-line; every D2-SPECIFIC line in the ξ_0-only scope
has a clean parametric-in-d replacement reducing to the d=2
line at d=2 (verdict signal `B_TEMPLATE_PARAMETRIC` for
Conj 3.3.A*).  Phase C halts at the gate
(`HALT_Q20_LITERATURE_MISSING`): Wasow 1965 / Adams 1928 /
Birkhoff 1930 / Birkhoff–Trjitzinsky 1933 are flagged in
T1-BIRKHOFF-TRJITZINSKY-LITREVIEW (2026-05-02) as needed-but-
not-acquired primary sources at the operator side, so the
in-original-form Phases C/D/E are deferred.  Aggregate verdict
**`UPGRADE_PARTIAL_PENDING_LITERATURE`** (Outcome Ladder #3).

## Key numerical findings

- Phase A.2 (general d, sympy, no precision loss): closed-form
  `ξ_0 = d / β_d^{1/d}` for all `d ≥ 2`.
- Phase A.3 sanity checks (mpmath dps=50, all rel_error = 0):
  - d=2, β_2=3: max|root| = 2/√3 ≈ 1.15470053837925152901829756100…
  - d=3, β_3=1: max|root| = 3 exactly
  - d=4, β_4=1: max|root| = 4 exactly
- All three are consistent (rel_error < 1e-15) with the
  prior AEAL-anchored values:
  PCF-1 v1.3 / Prompt-005 (d=2, 250 digits),
  XI0-D3-DIRECT G2_CLOSED_AT_D3 (d=3, 80 algebraic digits),
  PCF2-SESSION-Q1 (d=4, spread 0 at 8 reps, dps=80).

## Judgment calls made

1. **Conj-3.3.A*-only scope vs full-Prop-3.3.A scope.**  Q20
   asks about Conj 3.3.A* (the ξ_0 identity) specifically.
   D2-NOTE v1's d=2 proof template (Prop 3.3.A) covers ξ_0,
   ρ, and the Birkhoff a_k recursion together.  I separated
   the verdict by scope: `B_TEMPLATE_PARAMETRIC` for the
   ξ_0-only scope (Conj 3.3.A*), `B_MACHINERY_NEEDED at d ≥ 3`
   for the broader ρ component (which is OPEN per
   D2-NOTE v1 §3 last paragraph).  This is a substantive
   judgment because the prompt's Outcome Ladder is binary
   per scope; I documented it in `phase_b_summary.md` and
   `phase_d_verdict.md`.

2. **PCF-1 v1.3 §5 source not in workspace.**  Q20 §1
   anchor 5 requires reading PCF-1 v1.3 §4 (Newton-polygon
   section).  PCF-1 v1.3 is the operator's local TeX and
   is not under the bridge or under `pcf-research/` in
   this workspace.  Per Q20 §4
   `HALT_Q20_PHASE_B_TEMPLATE_DRIFT`, missing the source
   could be a halt; I treated it as a **partial Phase B
   deferral** (not a halt) because D2-NOTE v1 and CT v1.3
   §3.3.A are both in workspace, internally agree on the
   d=2 statement and proof sketch, and both cite PCF-1
   v1.3 §5 with the same bib key.  Surfaced as a residual
   operator-side check in this handoff §"Anomalies".

3. **Phase C: hard halt at the gate, no second-pass
   paraphrase.**  T1-BIRKHOFF-TRJITZINSKY-LITREVIEW already
   established that paraphrased / secondary-source readings
   of the four citations exist and are useable for
   structural-picture purposes, but cannot resolve the
   Adams-vs-Wasow normalization ambiguity.  I did NOT use
   secondary-source paraphrases to fabricate a
   `C_LITERATURE_UNIFORM` verdict.  This is consistent with
   AEAL hygiene and with the Q20 prompt §5 forbidden-verb
   policy.

4. **No D2-NOTE v2 draft this session.**  Per Q20 prompt §4
   `HALT_Q20_LITERATURE_MISSING` handler: "skip Phases C,
   D, E in original form".  Phase D is produced (Outcome
   Ladder #3 `UPGRADE_PARTIAL_PENDING_LITERATURE`), but
   Phase E (D2-NOTE v2 .tex draft + pdflatex build) is NOT
   produced.  D2-NOTE v1 is unchanged.

## Anomalies and open questions

This is the most important section.

1. **Verdict scope split.**  Phase B reveals that the d=2
   proof template (Prop 3.3.A) bundles three statements:
   ξ_0 = 2/√β_2, ρ = -3/2 - β_1/β_2, and the Birkhoff
   recursion for a_k.  At general d, the ξ_0 statement has
   a clean parametric-in-d derivation (Phase A); the ρ
   statement does NOT (open per D2-NOTE v1 §3); the a_k
   statement is M-tagged (B–T 1933 §§4–6).  **Implication
   for the synthesizer:**  Conj 3.3.A* (which is ξ_0 only)
   is in much stronger structural shape than the
   D2-NOTE v1 §3 "heuristic structural picture" implies —
   the *only* gap to closing it as a theorem at general d
   is the literature-side uniformity of Wasow §X.3 + B–T
   1933.  This is a **strictly weaker** open question than
   "write out the d≥3 indicial polynomial".  Claude may
   want to consider whether the SIARC roadmap should
   separate "Conj 3.3.A* upgrade" from "Prop 3.3.A
   generalization" as two distinct M2-stratum tasks.

2. **PCF-1 v1.3 §5 source-drift residual check.**  Not
   discharged in this session (anchor source not in
   workspace).  Light operator-side action: open PCF-1
   v1.3 §5 (Theorem 5) and confirm the d=2 statement and
   proof sketch agree with D2-NOTE v1 Prop 3.3.A and
   CT v1.3 Prop xi0.  Risk is low (joint v1.3 release
   window) but not formally checked.

3. **Adams-vs-Wasow normalization ambiguity (carried over
   from T1-BIRKHOFF-TRJITZINSKY-LITREVIEW Q3).**  If the
   T1 PHASE 2 primary-source acquisition resolves in
   favour of the Adams reading rather than the Wasow
   reading, the d-range of the cited Newton-polygon
   theorems may differ from "all d ≥ 2"; this could in
   principle change the Q20 Phase D verdict from
   `UPGRADE_PARTIAL_PENDING_LITERATURE → UPGRADE_FULL`
   to `UPGRADE_PARTIAL_d_LE_d*` for some d* ≥ 4.  Phase
   A's symbolic derivation is unaffected by this ambiguity
   (it is internal to the L_d operator, not to the
   Newton-polygon theorem statement).

4. **Cross-degree linearity `c(d) = d`.**  An incidental
   structural observation surfaces from Phase A and
   Phase B taken together: the universality constant
   c(d) = d in `ξ_0 = c(d)/β_d^{1/d}` is the *unique*
   value consistent with the slope-1/d edge characteristic
   polynomial `1 + (-1)^{d+1} (β_d/d^d) c^d = 0`.  In
   particular, the v1.1 candidate `c(d) = 2√{(d-1)!}`
   (D2-NOTE v1 Remark 3.3.E) is structurally falsified
   by the symbolic derivation, not just empirically by
   the d=4 measurement.  This is consistent with what
   D2-NOTE v1 §3 "Heuristic structural picture" already
   says — but it's worth recording that the d=4 spread-0
   measurement is now redundant evidence for the linear
   form rather than the primary evidence.

## What would have been asked (if bidirectional)

- "Should the relay agent fabricate a Phase C verdict from
  paraphrased / secondary sources, given that
  T1-BIRKHOFF-TRJITZINSKY-LITREVIEW already worked from
  paraphrases?"  Resolved as: NO.  Q20 prompt §4
  HALT_Q20_LITERATURE_MISSING handler is explicit; AEAL
  hygiene forbids fabricating a literature-uniformity
  claim that is not reproducible from primary sources.
- "Should the verdict be split by scope (Conj 3.3.A* alone
  vs full Prop 3.3.A)?"  Resolved as: YES, surfaced in
  Anomalies (1) above.

## Recommended next step

**Two parallel routes**, both feeding into Q20 closure:

**Route 1 (operator-side, low compute, light scholarly
work):** Acquire Wasow 1965 §X.3, Adams 1928, Birkhoff 1930,
B–T 1933 (per T1-BIRKHOFF-TRJITZINSKY-LITREVIEW PHASE 2
recommended_next_phase_t1.md).  Then re-run Phase C / D / E
in original form.  Conditional on `C_LITERATURE_UNIFORM`,
the verdict UPGRADES to `UPGRADE_FULL` for Conj 3.3.A*
(ξ_0-only scope), and a D2-NOTE v2 draft can be produced
with Theorem 3.3.A replacing Conj 3.3.A*.

**Route 2 (relay agent, low compute, follow-up prompt):**
A separate Q21 task could attempt to write out the
parametric-in-d ρ_d formula at d ≥ 3, closing the broader
Prop 3.3.A scope.  This is independent of Route 1.  The
relevant calculation is the indicial polynomial at the
slope-1/d edge of L_d in u = z^{1/d}, at order u^1 in the
trans-series.

Of these, Route 1 has higher strategic value (closes M2
for Conj 3.3.A* in the strongest way) and is bounded in
operator effort (≤ 60 min per T1 PHASE 2 estimate).

## Files committed

In `sessions/2026-05-03/Q20-CONJ33A-PROOF-UPGRADE/`:
- `phase_a_handoff_quote.md`       Phase A.1 verbatim quotes
- `phase_a_symbolic_derivation.py` Phase A.2 sympy script
- `phase_a_run.log`                Phase A run terminal capture
- `phase_a_summary.md`             Phase A summary (`A_DIRECT_IDENTITY`)
- `phase_b_d2_proof_template.md`   Phase B.1 d=2 template (D2-NOTE + CT v1.3)
- `phase_b_proof_diff.md`          Phase B.3–B.4 line-by-line diff
- `phase_b_summary.md`             Phase B summary (`B_TEMPLATE_PARAMETRIC`)
- `phase_c_literature_verification.md`  Phase C halt detail
- `phase_c_summary.md`             Phase C summary (`HALT_Q20_LITERATURE_MISSING`)
- `phase_d_verdict.md`             Phase D aggregate (`UPGRADE_PARTIAL_PENDING_LITERATURE`)
- `claims.jsonl`                   15 AEAL entries
- `halt_log.json`                  HALT_Q20_LITERATURE_MISSING with detail
- `discrepancy_log.json`           empty `{}` (no discrepancy)
- `unexpected_finds.json`          empty `{}` (no unexpected finds)
- `handoff.md`                     this file

NOT produced (per Q20 prompt §4):
- `d2_note_v2_main.tex`            (Phase E deferred)
- `q20_rationale_no_upgrade.md`    (verdict is not REJECTED)

## What this means for SIARC

- **G1** (algebraic ξ_0 identity at general d): structural
  evidence STRENGTHENED.  Phase A AEAL-anchors the symbolic
  uniformity statement; status string still "proven at d=2,
  verified at d∈{3,4}, conjectured at d≥5" but with stronger
  structural backing.
- **G2** (closed at d=3 per Prompt 012): unchanged.
- **M2** (Conj 3.3.A* upgrade decision): partial.
  UPGRADE_FULL for the ξ_0-only scope is conditional on
  T1 PHASE 2 literature acquisition.  M2 is NOT yet done.
- **M9** (SIARC-MASTER-V0 gating set): unchanged this
  session (M2 partial, not done; M9 still gated on
  {M2, M4, M6}).
- **CT v1.4 amendment recommendation:** add a
  "Conj 3.3.A* upgrade conditional on T1 PHASE 2
  literature acquisition" footnote to §3.3.A; cite Phase A
  symbolic derivation script
  (`phase_a_symbolic_derivation.py`) and `phase_a_summary.md`
  as the structural-uniformity anchor.  The d=4 spread-0
  measurement (PCF2-SESSION-Q1) becomes redundant
  empirical evidence rather than primary evidence.

## What's the next operator action

**Per Outcome Ladder #3 (UPGRADE_PARTIAL_PENDING_LITERATURE):**
the operator should acquire Wasow 1965 §X.3, Adams 1928,
Birkhoff 1930, B–T 1933 (T1-BIRKHOFF-TRJITZINSKY-LITREVIEW
PHASE 2 acquisition target), then re-relay Q20 Phase C
(only Phase C; Phases A and B do NOT need to be re-run).
Conditional on `C_LITERATURE_UNIFORM` at general d, Q20
verdict UPGRADES to `UPGRADE_FULL` for the ξ_0-only scope
and D2-NOTE v2 can be drafted in a follow-up session.

PCF-1 v1.3 §5 source-drift check (light, ≤ 10 min) can be
done by the operator in parallel.

## AEAL claim count

15 entries written to `claims.jsonl` this session
(meets the §3 minimum of 12).  Breakdown:
- 5 Phase A (closed-form identity + 3 sanity checks + verdict signal)
- 6 Phase B (5 parametric replacements L1/L2/L4/L5/L6 + verdict signals + scope-split rho gap)
- 1 Phase C (halt evidence)
- 1 Phase D (aggregate verdict)
- 1 Phase B.2 (PCF-1 v1.3 source-drift residual check)
- 1 implicit overlap (L9 scope coverage; covered under Phase B verdict)

Note: claims with `output_hash = "n/a-document"` are
synthesis claims (non-computational) anchored to a markdown
document; the document itself is the reproducibility witness,
not an output hash of a script run.  Claims tied to
`phase_a_symbolic_derivation.py` carry SHA-256
`8e6f9ebde933652e2581578d282163f0220091ea0ee4adbd6754bd53458f7496`.
