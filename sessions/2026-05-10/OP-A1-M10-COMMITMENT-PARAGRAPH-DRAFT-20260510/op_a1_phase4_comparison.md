# OP_A1 Phase 4 -- side-by-side comparison + full candidate text

**For:** operator selection (operator picks ONE -- A, B, or C -- and either
edits manually or instructs researcher to apply via Phase 5).
**Boundary:** researcher does NOT choose; researcher does NOT commit without
explicit operator selection.

---

## 1. Comparison table

  | axis                          | Candidate A (AGGRESSIVE)             | Candidate B (CONSERVATIVE)              | Candidate C (COLLABORATOR-DELEGATED)               |
  |-------------------------------|--------------------------------------|-----------------------------------------|----------------------------------------------------|
  | delivery field                | complete-by-2026-06-21               | report-status-by-2026-08-02             | complete-by-2026-07-05 OR report-status-by-2026-08-02 |
  | delivery class                | complete-by                          | report-status-by                        | hybrid (complete OR status)                        |
  | timeline                      | +6 weeks                             | +12 weeks                               | +8 weeks (complete) / +12 weeks (status fallback)  |
  | delegation field              | self                                 | self                                    | external-team                                      |
  | risk posture                  | aggressive (assumes Pattern alpha lands cleanly + WallisFamily 2-iter scoped repair) | defensive (R6 weakening risk explicit; status-only commitment) | resource-flexible (offloads agent-time risk; engagement-window contingency) |
  | iter-13 -> ?? path bound      | iter-13 -> iter-15 explicit          | iter-progression open                   | iter-progression open (external contributor scopes) |
  | R2 ladder reference           | explicit (heartbeat / alarm / ceiling) | implicit (status-report covers)        | implicit (external-team scoping decoupled)         |
  | Pattern beta fallback         | retained                             | central path option                     | retained                                           |
  | closure-statement assertion?  | NO (forward commitment to discharge work) | NO (status-of-tooling report)          | NO (forward commitment via external delivery)      |
  | RULE 1 leakage scan           | 0 hits                               | 0 hits                                  | 0 hits                                             |
  | FV strict-7 scan              | 0 hits                               | 0 hits                                  | 0 hits                                             |
  | line count (fenced block)     | 12                                   | 14                                      | 15                                                 |
  | required-references           | cascade-132 sec 5 + slot 139 BUNDLED-DEFERRED-NOTE | cascade-132 sec 5 + slot 139 BUNDLED-DEFERRED-NOTE | cascade-132 sec 5 + slot 139 BUNDLED-DEFERRED-NOTE |
  | status field                  | COMMITTED-2026-05-10                 | COMMITTED-2026-05-10                    | COMMITTED-2026-05-10                               |

---

## 2. Operator-selection considerations (informational; not advisory)

  - **Pick A if** the operator believes Pattern alpha is solid (slot 149 Q2
    sub-band HIGH) AND the WallisFamily.lean scoped repair path through the 5
    iter-13 blockers is clear within ~2 iterations AND operator has agent-time
    budget for +6 weeks of M10 fires.
  - **Pick B if** the operator wants to avoid asserting a complete-by date in
    case R6 weakening triggers OR if the WallisFamily.lean scoped repair turns
    out to require deeper imports / refactors (e.g. `Filter.Tendsto` neighborhood
    notation hygiene which has a non-trivial Mathlib import surface).
  - **Pick C if** the operator wants to free agent-time for non-M10 work
    (M2 / M3 / M5 / M11 / M12 still tabled) AND is willing to identify and
    onboard one external Lean-4 Mathlib contributor with the specified profile.
    Note that this candidate's success depends on operator-side recruiting,
    which is outside both researcher and slot-139-precedent scope.
  - **Edit-before-apply pattern.** Any of the three candidates may be
    operator-edited; common edits include: adjusting the date by +/- 2-4 weeks,
    swapping `complete-by` <-> `report-status-by`, adding a specific named
    collaborator (Candidate C), or trimming the notes prose. Operator should
    re-run the Phase 3 scans after editing if substantive prose changes.

---

## 3. Full text of each candidate (for operator copy-paste convenience)

### 3.1 Candidate A

```
COMMITMENT (operator-issued):
  delivery: complete-by-2026-06-21
  delegation: self
  notes: M10 sorry-discharge / formalization work-stream landed via cascade-132
    sec 5 documented-commitment-lift precedent and slot 139 BUNDLED-DEFERRED-NOTE
    verdict (DEFERRED-OUT-OF-M9-SCOPE variant). Plan: (a) slot 148 Pattern alpha
    axiom-signature refactor at lean/Thm66_ApparentSingularity.lean L118 + L120;
    (b) iter-13 -> iter-15 scoped repair on lean/WallisFamily.lean against the 5
    blockers in build_errors_iter13.log. Iter-counter tracked against R2 ladder
    (iter-18 heartbeat, iter-24 alarm, iter-30 ceiling); Pattern beta fallback
    retained if slot 149 C-149-1 R6 sub-checks 3a/3b/3c trigger.
  status: COMMITTED-2026-05-10
```

### 3.2 Candidate B

```
COMMITMENT (operator-issued):
  delivery: report-status-by-2026-08-02
  delegation: self
  notes: M10 sorry-discharge / formalization work-stream landed via cascade-132
    sec 5 documented-commitment-lift precedent and slot 139 BUNDLED-DEFERRED-NOTE
    verdict (DEFERRED-OUT-OF-M9-SCOPE variant). Conservative path: attempt slot
    148 Pattern alpha refactor at lean/Thm66_ApparentSingularity.lean L118 + L120,
    falling back to Pattern beta (h_exact replaced with a math-content-equivalent
    dischargeable hypothesis) if slot 149 C-149-1 R6 sub-checks 3a/3b/3c trigger.
    The +12wk checkpoint is a status-of-the-tooling report only (not a closure
    assertion); covers iter-progression on lean/WallisFamily.lean against the
    5 blockers in build_errors_iter13.log plus any axis-level re-scoping (e.g.
    SEPARATE-AXIS-DEFERRED downgrade per slot 140 sec 5 outlook).
  status: COMMITTED-2026-05-10
```

### 3.3 Candidate C

```
COMMITMENT (operator-issued):
  delivery: complete-by-2026-07-05  OR  report-status-by-2026-08-02
  delegation: external-team
  notes: M10 sorry-discharge / formalization work-stream landed via cascade-132
    sec 5 documented-commitment-lift precedent and slot 139 BUNDLED-DEFERRED-NOTE
    verdict (DEFERRED-OUT-OF-M9-SCOPE variant). Operator to engage one external
    contributor; profile: Lean-4 Mathlib contributor with prior work on
    apparent-singularity / Frobenius-method formalization, Filter.Tendsto +
    neighborhood-notation hygiene, and Wallis-class PCF identities. Scope:
    (a) slot 148 Pattern alpha axiom refactor at Thm66_ApparentSingularity.lean
    L118 + L120 (Pattern beta fallback if slot 149 C-149-1 R6 sub-checks trigger);
    (b) iter-progression on WallisFamily.lean against the 5 blockers in
    build_errors_iter13.log. 8-week complete-by if engagement lands within +2wk;
    else 12-week status-only fallback report.
  status: COMMITTED-2026-05-10
```

---

## 4. Operator action items

  1. Read all three candidates above + read the Phase 3 scan results
     (`op_a1_phase3_scan_results.md`).
  2. Read the iter-13 state summary (`op_a1_phase1_iter13_summary.md`) to
     calibrate timeline confidence.
  3. Select ONE candidate (or modified version thereof).
  4. Either:
     (a) edit `tex/submitted/control center/picture/m10_documented_commitment.md`
         Section 3 directly (copy-paste the chosen block, replacing the
         placeholder block at lines 137-149 with delimiters intact), commit
         with message "M10-COMMITMENT-FILLED -- operator-issued delivery
         commitment", push to origin/main; OR
     (b) instruct researcher (Phase 5) to apply chosen candidate.
  5. After the fill is committed, update `.fleet.yaml` `commitments[]` block
     to flip the status from `COMMITMENT-PARAGRAPH-PENDING-OPERATOR` to
     `COMMITTED-2026-05-10` per the m10 scaffold sec 5 directive.
  6. Confirm slot 152 (synth-review) input by sharing the chosen candidate
     plus its scan-results delta (if any operator edits were made) with the
     synth.

---

*End of phase 4. Awaiting operator selection or close-without-action.*
