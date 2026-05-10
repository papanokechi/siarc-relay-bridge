# OP_A1 Phase 2 -- three candidate Section 3 fills

**Drafter:** GitHub Copilot (claude-chat repo, this session)
**Drafting basis:** prompt OP_A1 Phase 2 specification (axes A / B / C)
**Target file:** `tex/submitted/control center/picture/m10_documented_commitment.md`
Section 3 placeholder block
**All candidates:** ASCII-pure; reference cascade-132 sec 5 precedent +
slot 139 BUNDLED-DEFERRED-NOTE verdict; carry `status: COMMITTED-2026-05-10`;
within 3-15 line size envelope.

NOTE: each candidate replaces the entire fenced block in Section 3 of the
scaffold (lines 137-149 of the current file). The leading word `COMMITMENT`
is reused; the parenthetical changes from "(operator to fill)" to
"(operator-issued)" to record that the fill has now occurred.

---

## Candidate A -- AGGRESSIVE (6-week, self, iter-13 -> iter-15 path)

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

Line count: 12. Date arithmetic: +6wk from 2026-05-10 = 2026-06-21.

---

## Candidate B -- CONSERVATIVE (12-week status-report, self, R6 risk emphasis)

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

Line count: 14. Date arithmetic: +12wk from 2026-05-10 = 2026-08-02.

---

## Candidate C -- COLLABORATOR-DELEGATED (8-week complete-by OR 12-week status, external-team)

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

Line count: 15. Date arithmetic: +8wk = 2026-07-05; +12wk = 2026-08-02;
+2wk engagement window = 2026-05-24.

---

## Notes on drafting choices

  - All three candidates rephrase "(operator to fill)" -> "(operator-issued)"
    in the leading line so the block self-identifies as filled rather than a
    template. Operator is free to revert if a different convention is preferred.
  - All three candidates use `M10 sorry-discharge / formalization work-stream`
    as the canonical axis label per `m10_documented_commitment.md` sec 1
    scope statement (and per slot 139 verdict sec 4 tooling-state framing).
  - All three candidates reference both the cascade-132 sec 5 precedent and
    the slot 139 verdict label (BUNDLED-DEFERRED-NOTE family with
    DEFERRED-OUT-OF-M9-SCOPE variant), satisfying the prompt's "MUST reference"
    requirement.
  - Pattern alpha vs Pattern beta is mentioned in all three candidates because
    slot 149 Q2 ratified Pattern alpha at sub-band HIGH with a known
    R6-fallback trigger condition (slot 149 C-149-1 sub-checks 3a/3b/3c).
  - Candidate A is most concrete (binds the iter-13 -> iter-15 path explicitly);
    Candidate B is most defensive (status-report only, R6 risk emphasis);
    Candidate C is most resource-flexible (external-team option with engagement
    window contingency).
  - None of the candidates assert closure; all are forward commitments to a
    state-of-the-tooling status (per slot 139 verdict tooling-state framing).

*End of phase 2. Operator-selection input required.*
