# abstract.md — PCF-2 v1.4 abstract (polish-pass verdict)

## Synth verdict on the v1.3 abstract (inherited unchanged in v1.4)

**No re-write recommended.** The v1.3 abstract is fit-for-deposit and was correctly inherited unchanged in the v1.4 amendment.

The abstract correctly:

1. Frames the paper as a **program statement** (not a results paper). This framing is critical for Zenodo categorization (Preprint) and for reader expectation-setting; introducing definitive result claims into the abstract would create a scope/content mismatch.
2. Inherits **PCF-1's sharp degree-2 dichotomy** as foundational reference (30 families; sign of balanced discriminant Δ₂ predicts elementary closed form vs PSLQ-undetected limit; Stokes-exponent predicate S<1 across all 6 Δ<0 CM candidates).
3. Identifies the **cubic-discriminant Galois-structure obstruction** as the qualitative novelty between degree-2 (sign-of-Δ predicate) and degree-3 (sign + Galois-group structure together govern dichotomy).
4. Cites **Conjecture B₃** (cubic trichotomy) and **Conjecture B4** (sharp WKB exponent identity at d=3,4) as the central conjectures.
5. Discloses the **deep-WKB null at d=4** (Session R1.3) as the rule-out for verbatim degree-4 extension. This is the scope-limit-honesty signal that strengthens the program statement.

## Additions to the abstract in v1.4 (verified clean)

The v1.4 amendment adds a closing paragraph (after `\end{abstract}` block at L116-138 of `pcf2_program_statement_v14.tex`) titled "What changed between v1.3 and v1.4". The paragraph:

- Records exactly one Open-Problem-status update relative to v1.3: `op:j-zero-amplitude-h6` (j=0 amplitude / Chowla–Selberg closure).
- Cites Prompt 014 `PASS_A_EQ_6_ONLY` verdict (SIARC bridge SHA `e857172`, 2026-05-02).
- Cites M7 V0 cascade `T1-SYNTH-M7-V0-CLOSURE-CASCADE-123` (bridge SHA `7f93b9e`, 2026-05-09; aggregated MEDIUM-HIGH).
- Preserves verbatim annotation `(SOFT-BRANCH; HARD-BRANCH-PENDING)`.
- Records hard-branch stretch goal |δ| < 10⁻³⁰ as **forward-pointed under Q22 path-(b)** (NOT closed).
- States explicitly: "All other v1.3 content … is unchanged in v1.4".

**This closing paragraph is the canonical narrative for the v1.4 amendment scope.** No edits recommended.

## What the abstract does NOT contain (and should NOT for v1.5)

- ❌ M1-M12 narrative — belongs in Umbrella, not PCF-2.
- ❌ S153 quad-witness CONFIRM_CLOSURE narrative — program-tier governance, not PCF-2-scoped.
- ❌ M8b d≥3 caveat — outside PCF-2's degree-3 mathematical scope.
- ❌ M10 Lean formalization status — engineering work-stream, not math content.
- ❌ Direct claims of "M-axis closure" — UNSAFE per D-153-3 governance discipline.

## Recommendation for v1.5 abstract (if/when needed)

No re-write. If v1.5 records additional Open-Problem-status updates, append a v1.5 changelog paragraph following the v1.4 pattern (one paragraph after `\end{abstract}`, scoped to the new status updates only). Keep the v1.3-inherited main abstract body unchanged.

## Keywords (carried from verdict Q2b)

9-item array for Zenodo Edit (paste into Zenodo Keywords field as 9 separate entries):

1. continued fractions
2. cubic discriminant
3. WKB amplitude
4. Chowla–Selberg formula
5. Γ(1/3)
6. PSLQ
7. transcendence predicate
8. Galois group cubic
9. equianharmonic CM

Optional reduction to 8: drop `equianharmonic CM` (sub-specialty of `Chowla–Selberg formula` + `Γ(1/3)` coverage).
