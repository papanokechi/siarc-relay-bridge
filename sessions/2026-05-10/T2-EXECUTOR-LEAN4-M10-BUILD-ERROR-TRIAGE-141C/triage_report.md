# Triage Report -- T2-EXECUTOR-LEAN4-M10-BUILD-ERROR-TRIAGE-141C

**Date:** 2026-05-10
**Slot:** 141C
**Class:** T2-Executor (read-only triage; classify-and-route only)
**M-axis:** M10
**Confidence band:** MEDIUM-HIGH (per slot 144 Change 2, 2330437)
**Bridge HEAD at draft:** 23304375 (slot 144 absorption)
**Lean toolchain:** leanprover/lean4:v4.30.0-rc1
**Mathlib pin:** v4.30.0-rc1

---

## Section 1 -- Executive summary

The M10 V0 substrate-prep stage (POST_SYNTH_REVIEW outlook sec 2.2 Phase C.1)
shows iteration-13 of an in-flight Lean-4 fix loop on `lean/WallisFamily.lean`.
Five enumerated build-blockers are reported by `build_errors_iter13.log`. Read-only
inspection at HEAD finds two project-side `sorry` sites (both in
`Thm66_ApparentSingularity.lean`, lines 118 and 120, both supplying the
`h_exact` argument to the `frobenius_double_root_at_apparent_singularity`
axiom). The slot 144 verdict reported a sorry count of 3; this triage finds 2
under the regex `\bsorry\b` after excluding comment-only mentions and
`lean/.lake/` package files. The discrepancy of 1 is logged in
`discrepancy_log.json` as item D-141C-1 (non-blocking; see Section 6).

Per-blocker classification:

| ID | Location | Class | Confidence |
| -- | -------- | ----- | ---------- |
| B1 | WallisFamily.lean:58 | trivial-repair | HIGH |
| B2 | WallisFamily.lean:114-118 | tactic-strategy | MEDIUM-HIGH |
| B3 | WallisFamily.lean:171-177 | tactic-strategy | MEDIUM-HIGH |
| B4 | WallisFamily.lean:216-312 (`nhds` notation) | trivial-repair | HIGH |
| B5 | WallisFamily.lean:243, 285 | tactic-strategy | MEDIUM |

Per-sorry classification:

| ID | Location | Routing | Confidence |
| -- | -------- | ------- | ---------- |
| S1 | Thm66_ApparentSingularity.lean:118 | axiom-shape reformulation (not direct discharge) | LOW |
| S2 | Thm66_ApparentSingularity.lean:120 | symmetric to S1 | LOW |

The triage outputs `blockers.json`, `sorries.json`, and `dependency_map.json`
as machine-readable input for the operator's iteration-14 discharge pass.

M10 V0 readiness state: not green; iteration-14+ build-fix iterations remain
the gating activity for Phase C.3 (commit) and Phase C.3+ (reproducibility check).

---

## Section 2 -- Per-blocker analysis

### B1 -- duplicate `WallisFamily.Solves` declaration (line 58:4)

The iter-13 log reports that `WallisFamily.Solves` has already been declared
when WallisFamily.lean reaches line 58. At HEAD, the file shows only
`def SolvesShifted` at lines 54-58 (the longer name), and the imported
sibling `WallisFamily.Solves` lives in `WallisFamily/ShiftConsistency.lean:45`.
A literal duplicate `def Solves` is not visible in the read-only inspection
of WallisFamily.lean at the current commit. The most parsimonious account is
that iter-13 captured a transient intermediate state in which the duplicate
had been re-introduced and then partially backed out. The fix-vector is to
ensure exactly one definition site for `WallisFamily.Solves` exists; if a
local variant is intended in WallisFamily.lean, rename to `SolvesAlt`. This
is a name-resolution repair, not a math-content gap. Confidence: HIGH.

### B2 -- malformed `hu (k+2) (by omega)` in `intertwining_lemma` (lines 114-118)

The iter-13 log indicates an unsolved-goals failure in `intertwining_lemma`
attributed to a malformed application of the recurrence hypothesis with an
`(by omega)` side argument. Inspection at HEAD shows the proof using
`hu k` and `hu (k+1)` directly with no inequality side argument, which
matches the type signature of `Solves m u = forall n : N, pcf_rec m n u`
imported from ShiftConsistency.lean. If the iter-13 working tree carried an
older shape, repairing to the visible HEAD shape resolves the literal
`omega`-argument issue. A residual unsolved-goals shape may then surface
from the `linear_combination` ansatz coefficients on line 125 or from
`simp only [Lm, intertwinerA, intertwinerB, ...]` not unfolding through
the `n+1` constructor branch of `Lm`. Recommended diagnostic: enable
`set_option pp.all true` on the failing goal to inspect the unreduced term.
This is a tactic-strategy issue rather than a missing math lemma.
Confidence: MEDIUM-HIGH.

### B3 -- `positivity` / rational identity failure in `ratio_step_m0` (lines 171-177)

`ratio_step_m0` shows three `positivity` goals (`(2*k+1) != 0`,
`(2*k+3) != 0`, and a factored form via `mul_ne_zero` on `(4*(k+1)^2 - 1) != 0`),
followed by `field_simp; push_cast; ring`. The iter-13 log marks this region
as a positivity / rational identity failure. The likely failure mode is that
`positivity` is presented with a goal where the natural cast `(k : R)` has
been absorbed into a more complex term and Mathlib's positivity extension
loses sight of `Nat.cast_nonneg`. Fix-vectors: replace `positivity` with
explicit `linarith [Nat.cast_nonneg (k : N)]`; or swap order to
`push_cast; field_simp; ring` (cast normalization first). Routing target:
`Nat.cast_nonneg`, `Nat.cast_pos`. Confidence: MEDIUM-HIGH.

### B4 -- unknown / unimported `nhds` notation (lines 216-312)

The iter-13 log flags multiple `Filter.Tendsto` target failures from an
unresolved scoped-Topology notation in the L216-312 region. At HEAD the file
opens `scoped Topology` at line 11 (after `namespace WallisFamily` at line 9),
and all visible Tendsto lemmas in that region (L218, L226, L261, L262, L265,
L276, L324) use the spelled-out `nhds` form rather than the scoped notation.
If iter-13 introduced the scoped notation in a fresh region without it being
in scope at the use site, the lowest-effort repair is uniform replacement
back to the spelled-out form. Alternatively, ensuring `open scoped Topology`
sits inside the namespace block addresses the resolution. Import chain check:
`import Mathlib` at line 1 is broad enough to bring `Mathlib.Topology.Basic`
into scope; no import is missing. Confidence: HIGH (lowest-effort blocker).

### B5 -- `linarith` and rewrite failures at lines 243 and 285

Line 243 sits inside the body of `reciprocalWallis_succ`, where the goal
shape involves casts of `Nat.centralBinom` and the predecessor identity
`Nat.succ_mul_centralBinom_succ`. Line 285 sits in the bridging step between
the induction step and the closed-form lemma. Both line numbers are in the
cast-normalization glue rather than in the math-content of the recurrence.
The likely failure mode is mismatched `(m+1 : R)` vs `((m : R) + 1)` casts
across the `simpa` call. Fix-vector: extract a stand-alone lemma
`centralBinom_cast_succ` with proof `field_simp; push_cast; ring`, then
rewrite at the failing site. This is a tactic-strategy issue.
Confidence: MEDIUM (the proof structure is correct in shape but the cast
plumbing is fragile).

---

## Section 3 -- Per-sorry analysis

### S1 -- Thm66_ApparentSingularity.lean:118

The sorry supplies the `h_exact` hypothesis in the `frobenius_double_root_at_apparent_singularity` axiom application
for the first indicial root `s_1`. Per the iteration-12 fix_pass_log entry:
the goal `forall x, HasDerivAt (fun x => a x * deriv id x) (a x) x` is an
artefact of the axiom formulation and cannot be discharged for the specific
`a = a_coeff_c` (it would require `a(x) = C * exp(x)`). Routing target is
NOT direct sorry discharge; routing target is axiom reformulation: split
`frobenius_double_root_at_apparent_singularity` into a version that takes
only `(ha_root, ha_simple)` and absorbs the derivative-shape hypothesis
internally. Mathlib lemma family for the eventual reformulated proof:
`Mathlib.Analysis.Calculus.Deriv.Basic`, `Deriv.Mul`, `Deriv.Pow`. AEAL-status:
blocked-by-design at the axiom layer. Confidence: LOW.

### S2 -- Thm66_ApparentSingularity.lean:120

Symmetric counterpart of S1 for the second indicial root `s_2`. Same
structural blocker (axiom-shape mismatch). Treat S1 and S2 as a single
discharge unit, not two independent ones: the axiom reformulation that
closes S1 closes S2 by the same edit. Confidence: LOW.

---

## Section 4 -- Dependency map prose summary

The M10-relevant node set comprises seven `.lean` files: `WallisFamily.lean`
(top-level), three sibling files under `WallisFamily/`
(`ShiftConsistency.lean`, `CasoratianPi4.lean`, `LemmaK.lean`),
`Thm66_ApparentSingularity.lean`, `proof_targets.lean`, and
`CardEvenOfInvolution.lean`.

Within the node set, the only intra-set imports are: `WallisFamily.lean ->
{ShiftConsistency, CasoratianPi4}` and `proof_targets.lean -> {LemmaK}`.
The remaining files are leaves. There are no circular imports.

The lakefile declares two relevant `lean_lib` targets: a `WallisFamily`
default-target (covering `WallisFamily.lean` and `WallisFamily/*`) and a
`Thm66` target with root `Thm66_ApparentSingularity`. Two project-side
files (`proof_targets.lean` and `CardEvenOfInvolution.lean`) are not
declared in any `lean_lib` root, suggesting they are staging or
unit-test-style files reached only via explicit invocation.

A possibly-dead import: `WallisFamily.lean` imports
`WallisFamily/CasoratianPi4` but no symbol from CasoratianPi4
(`raw_casoratian_step`, `reduced_casoratian_step`, `casoratian_closed_form`,
`pi4_series_of_bridge`) is referenced by name in the visible body of
`WallisFamily.lean` at HEAD. The import may be retained for future use or
may be removable. Removal is OUT OF SCOPE for this triage (per E5).

`WallisFamily/LemmaK.lean` is a leaf in the M10 graph and is not on the
critical build path of the `WallisFamily` lean_lib target. Build failures
in `WallisFamily.lean` cannot be caused by `LemmaK.lean`. Conversely,
`proof_targets.lean` depends on `LemmaK.lean` compiling, so a green
WallisFamily build does not transitively imply a green proof_targets.

---

## Section 5 -- Prioritized fix-plan

Recommended fix-order, trivial-first heuristic:

1. **B4 (HIGH, trivial-repair):** Replace any `nhds` scoped-notation usage
   in WallisFamily.lean L216-312 with spelled-out `nhds`, or move
   `open scoped Topology` inside the namespace block. Should resolve the
   most numerous error count per the iter-13 log ("multiple Filter.Tendsto
   target failures").

2. **B1 (HIGH, trivial-repair):** Audit WallisFamily.lean for any duplicate
   `def Solves`. Either remove the duplicate or rename. Single-line repair.

3. **B2 (MEDIUM-HIGH, tactic-strategy):** Verify that `intertwining_lemma`
   uses `hu k` / `hu (k+1)` directly (not `hu (k+2) (by omega)`). If the
   shape is already correct at HEAD, run with `set_option pp.all true` to
   inspect any residual unsolved-goals shape from the `linear_combination`
   coefficients.

4. **B3 (MEDIUM-HIGH, tactic-strategy):** Address the positivity / rational
   identity failure in `ratio_step_m0` by reordering `push_cast; field_simp;
   ring` or by replacing `positivity` with explicit
   `linarith [Nat.cast_nonneg (k : N)]`.

5. **B5 (MEDIUM, tactic-strategy):** Extract a `centralBinom_cast_succ`
   lemma discharged once with `field_simp; push_cast; ring`, then rewrite at
   the L243 and L285 sites. This is the most fragile of the five blockers.

Sorry-discharge plan (separate from build-fix iteration):

- S1 + S2 together require axiom reformulation in
  `Thm66_ApparentSingularity.lean`. This is a SEPARATE work item from the
  WallisFamily build-fix loop and need not block iteration-14. Suggested
  ordering: green WallisFamily first (Phase C.1), then commit (Phase C.3),
  then take up the axiom reformulation as a follow-up sorry-discharge fire
  (slot 142-class agent fire).

---

## Section 6 -- Open questions for operator

### Q1. Sorry-count discrepancy

Slot 144 verdict (line 51 of `synth_verdicts_raw.txt`) reports
"Sorry count = 0 across project-side `.lean` files (currently 3)". This
triage's regex `\bsorry\b` scan finds 2 project-side `by sorry` instances
(Thm66:118, Thm66:120). Possibilities: (a) the slot 144 count includes a
comment-only sorry mention as a count-bearing item (e.g., the `-- SORRY:`
header at Thm66:63 or the `-- Iteration 12 replaces the generated sorry
placeholders` comment at proof_targets.lean:2); (b) the slot 144 count was
forward-looking under an iter-13 working-tree state that introduced a
third sorry now removed; (c) the slot 144 count includes the
`GoldbachHelfgott/Reduction.lean` axiom-stub which the file's own header
notes is sorry-free in body. Open question: which interpretation does the
operator regard as canonical? Logged as D-141C-1 in discrepancy_log.json.

### Q2. CasoratianPi4 import in WallisFamily.lean

`WallisFamily.lean` imports `WallisFamily/CasoratianPi4` but no symbol from
CasoratianPi4 is referenced by name in the visible body at HEAD. Is this
import intentional (future use) or removable? Removal is out of scope for
this triage.

### Q3. lakefile orphan files

`proof_targets.lean` and `CardEvenOfInvolution.lean` are not declared in
any `lean_lib` root. Are these files meant to be in the build path, or
are they staging artefacts? If in scope, suggest adding to lakefile.lean.
Not actionable here; surfaced for operator review.

### Q4. Iteration-13 log staleness

The HEAD source for `WallisFamily.lean` shows several details (e.g., the
`hu k` calling convention without `omega`, spelled-out `nhds`) that appear
to differ from the iter-13 build-error log. The agent cannot run
`lake build` (per E3); pattern-matching from logs alone leaves residual
uncertainty. Recommendation: operator should re-run `lake build` at the
current working-tree state and compare the new error log against this
triage; persistent blockers should be re-fired as 141D-class triage on
the iteration-14 log.

### Q5 (RULE-1-tabled note)

The slot 144 verdict (line 60-70) and sec 4 of the POST_SYNTH_REVIEW outlook
restrict 141C scope to "classify-and-route only" without sorry-discharge
candidate proof generation. This triage observes the restriction. No
candidate proofs for any sorry site appear in this report or in the
JSON deliverables.

---

## Appendix A -- Inputs read (read-only)

Governance:
- `tex/submitted/control center/picture/M1_M12_CLOSURE_OUTLOOK_20260510_POST_SYNTH_REVIEW.md` (sec 4)
- `tex/submitted/control center/picture/M1_M12_CLOSURE_OUTLOOK_20260510_POST_LEAN_REALITY.md`

Build-error + iteration:
- `lean/build_errors_iter13.log`
- `lean/fix_pass_log.md`

Lean source (read-only, no edits):
- `lean/WallisFamily.lean`
- `lean/WallisFamily/ShiftConsistency.lean`
- `lean/WallisFamily/CasoratianPi4.lean`
- `lean/WallisFamily/LemmaK.lean`
- `lean/Thm66_ApparentSingularity.lean`
- `lean/proof_targets.lean`
- `lean/CardEvenOfInvolution.lean`
- `lean/lakefile.lean`
- `lean/lean-toolchain`

Auxiliary substrate (best-effort; available):
- `lean/sorry_log.json`, `lean/triage.json`, `lean/proof_status.json`,
  `lean/lean4_claims.jsonl`, `lean/thm66_lean4_summary.md`,
  `lean/lemma_k_scoping.md`, `lean/full_build.log`, `lean/build_errors.log`,
  `lean/build_log.txt`, `lean/shift_build.log`

Cross-reference:
- `siarc-relay-bridge/sessions/2026-05-10/T1-SYNTH-M1-M12-ROADMAP-CONSULTATION-144/synth_verdicts_raw.txt`

No file under `lean/` was modified by this fire (per E2).
No `lake build` / `lake check` / `lean --run` executed (per E3).
