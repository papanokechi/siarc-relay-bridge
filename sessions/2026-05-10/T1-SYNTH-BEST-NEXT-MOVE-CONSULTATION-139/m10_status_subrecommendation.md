# M10 Status Sub-Recommendation (canonical operative text)

**Sub-recommendation:** `DEFERRED-OUT-OF-M9-SCOPE` (variant of BUNDLED-DEFERRED-NOTE; NOT SEPARATE-AXIS)
**Confidence band:** `MEDIUM-HIGH`
**Independence:** independent of slot 139 selected MOVE label per packet §5.4 verdict-template directive — i.e., this sub-recommendation stands whether MOVE_A / B / C / D / E / F was selected as the next-move
**Source:** R1 single-witness verdict §4 (verbatim verdict at `synth_verdicts_raw.txt`)
**Date:** 2026-05-10 ~08:15 JST

---

## 1. Operative recommendation

M10 (Lean-4 sorry-discharge / formalization) should be declared **out-of-scope for the M9 V0 announcement**, not closed via the M-axis 3-arc ratification template. Lift authorization for RULE 1 should be obtained via an **operator-issued one-paragraph documented commitment** (per cascade-132 documented-commitment-lift precedent), not via a closure cascade.

## 2. Reasoning (verbatim from verdict §4 with structural emphasis)

The §1.5 reality survey is decisive on this. M10 ≈ Lean-4 sorry-discharge is **not analogous** to M4/M7/M8a/M8b. Those four axes were **math-content axes** where the underlying mathematics had reached a state ready for peer-review and a closure-statement could be authored with content the synth could verdict on. M10 is a **formalization** axis — the mathematics it formalizes (Thm 6.6 apparent singularity; Wallis family; CardEvenOfInvolution helper) is **already covered under M2/M7/M8 closures**. M10 closure means "Lean-4 build is green and sorries are discharged," which is a **state-of-the-tooling claim**, not a state-of-the-mathematics claim.

Three observations push toward DEFERRED-OUT-OF-M9-SCOPE:

### (a) The 3-arc template is for math-content closure, not tooling-state

The 3-arc ratification template (substrate-prep → solo-dispatch → cascade-absorption) was designed for math-content closure. Using it on tooling-state ("build is green; 0 sorries") forces the synth to verdict on something the synth has limited access to verify (the synth doesn't run Lean; can only read sorry-count snapshots). The forecast verdict for a premature M10 cascade would be `(SORRY-DISCHARGE-INCOMPLETE; LEAN-V0-PARTIAL)` — honest but produces a closure SHA whose annotation contradicts the word "closure." This is **epistemically worse than no closure SHA at all**.

### (b) M9 V0 announcement does not require Lean-4 verification

The bootstrap closure-outlook §5 listed M10 as an active operator decision, which implicitly assumed the synth would help frame the choice. The synth's framing: M9 V0 announcement substrate (umbrella v2.2, PCF-2 v1.4, picture v1.20+) does not require Lean-4 verification of its mathematical claims; the math is established by the cited papers. **M10 is a parallel verification track** whose value is referee-confidence-amplification, not foundational closure. As such, **it should not gate M9 V0 announcement**.

### (c) Documented-commitment precedent applies (citation corrected)

> **AGENT-SIDE NOTE (rubber-duck QA per packet §10):** the verdict §4(c) cited "cascade-131 §1.4 last paragraph" as the documented-commitment-lift precedent. Direct grep of both artefacts during slot 139 absorption found the precedent text exclusively in **cascade-132** = `m9_v0_closure_path_decision.md` §5: *"Operator-discretion permits lift before M10 with documented commitment."* The verdict's substantive claim (documented-commitment lift is precedented) is **CORRECT**; the citation is misattributed (cascade-131 = the prompt slot; cascade-132 = the resulting bridge SHA `fd669d3` — easy slip given the slot/SHA naming overlap). Logged as `discrepancy_log.json` D-139-1 LOW.

The corrected-citation reasoning: cascade-132 (`fd669d3`) §5 records the documented-commitment-lift precedent for cases where an axis is foundationally needed but not yet complete. M10 fits this precedent well: document the commitment to discharge sorries on a separate work-stream, lift RULE 1 on the M9 V0 announcement substrate, and let M10 close on its own timeline post-lift.

## 3. Recommended commitment paragraph format (per verdict open-question)

If operator accepts this sub-recommendation, the documented-commitment paragraph should consist of:

```
M10 Lean-4 sorry-discharge is delegated to the post-RULE-1-lift work-stream.

Current state (snapshot 2026-05-10):
  build_errors_iter{N}.log  (N = 13 at slot 139 draft time; verify pre-fire)
  uncommitted lean/ working-tree (108-line WallisFamily.lean diff;
    Thm66_ApparentSingularity.lean untracked with 2 sorries;
    proof_targets.lean untracked with 1 sorry;
    GoldbachHelfgott/, WallisFamily/ untracked)

Commitment: complete-by-{operator-date}  OR  report-status-by-{operator-date}
Cross-references:
  - cascade-132 §5 lift-precedent: bridge `fd669d347967db2e854f8e9d3725f625bf9fbc2a`
  - this slot 139 cascade SHA: <bridge-pending>
```

**Format proposal (verdict §6 open-question):** 3-line YAML block in `.fleet.yaml` under a new `commitments:` subsection, cross-linked to a one-page `m10_documented_commitment.md` substrate. The YAML block is operator-issued; agent should not pre-fill the commitment text — only the format scaffold.

## 4. Alternative recommendations (if operator overrides)

| Operator decision | Triggered slot guidance |
|---|---|
| `SEPARATE-AXIS-NOW` (override) | slot 141 = MOVE_A T2-Executor M10 V0 substrate-prep (commit lean/ work + sorry-count snapshot + closure-statement draft); proceed through 3-arc template with anticipated `(SORRY-DISCHARGE-INCOMPLETE; LEAN-V0-PARTIAL)` annotation |
| `SEPARATE-AXIS-DEFERRED` (preferred alternative) | functionally equivalent lift mechanics; differs from BUNDLED-DEFERRED-NOTE only in post-lift framing (separate axis with own ratification timeline vs. bundled-as-deferred-note within M9). Operator's call on the framing |
| `BUNDLED-DEFERRED-NOTE` (verdict's recommendation) | this sub-recommendation; documented-commitment paragraph + RULE 1 lift |
| `RE-CONSULT MULTI-WITNESS` | slot 141 = T1-Synth dual-/triple-witness re-fire of slot 139; recommend if operator considers MEDIUM-HIGH band insufficient for the M10 decision |

## 5. Risks of accepting this sub-recommendation

| Risk | Likelihood | Mitigation |
|---|---|---|
| Operator-issued commitment paragraph is read as "soft" by external referees | MEDIUM | cite cascade-132 §5 precedent directly in the commitment paragraph; the precedent is internal-SIARC-governance, not external-referee-facing |
| Forking M-axis taxonomy (math-content vs tooling-state) could be a slippery slope (M11/M12 also tooling-state?) | LOW-MED | filed as UF-139-1 (synth's §6 closing observation); consider meta-consultation if M11/M12 turn out similar |
| Sorry-discharge ends up taking longer than commitment-by-date | MEDIUM | operator can use `report-status-by-{date}` form rather than `complete-by-{date}`; reframes commitment as transparency, not deadline |
| External readers see M10 as "incomplete" in M9 V0 announcement context | LOW | M10 is not cited in the M9 V0 announcement substrate (umbrella v2.2 / PCF-2 v1.4 / picture v1.20+) per cascade-132 §3.1 deposit-ordering; only `m10_documented_commitment.md` would surface it, and that's an internal artefact |

## 6. Risks of REJECTING this sub-recommendation (i.e., picking SEPARATE-AXIS-NOW)

| Risk | Likelihood | Severity |
|---|---|---|
| Premature closure cascade produces SHA with self-contradicting annotation | HIGH | MEDIUM (epistemic; closure SHA is permanent) |
| 3-5 hr agent time spent on cascade with weak verdict forecast | MEDIUM | LOW (sunk cost) |
| Cascade-132 chain re-opens with M10 follow-on amendments to umbrella v2.2 / PCF-2 v1.4 / picture v1.20+ Amendment Logs (4th amendment to all 3) | MEDIUM-HIGH | MEDIUM (log-bloat per C-A4) |
| Parallel-CLI fire collision risk over 3 closure-cascade fires | MEDIUM | MEDIUM (n=3 pattern already) |

---

**End of m10_status_subrecommendation.md.**
