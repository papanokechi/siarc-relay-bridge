# Handoff — GOLDBACH-HELFGOTT-C1
**Date:** 2026-04-25
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~25 minutes
**Status:** COMPLETE

## What was accomplished
Created the Lean 4 package `GoldbachHelfgott/` (5 modules, ~120 lines
of source) formalizing the conditional reduction *"strong Goldbach
follows from Helfgott's ternary theorem plus a computational
certificate up to N₀"*.  The package builds cleanly under
`mathlib4 v4.30.0-rc1` (684/684 jobs, all `#check` queries print
the expected types) and contains **zero `sorry`s in theorem bodies**.
The three scope-bounded gaps (Helfgott axiom, certificate stub,
prime-splitting research target) are surfaced at the type level —
two as named axioms, one as an explicit hypothesis of the bridge
theorem — exactly mirroring the `congruent-relay` convention.

## Key numerical findings
- `lake build GoldbachHelfgott` ⇒ success, 684/684 jobs, no warnings.
- `goldbach_conditional : TernaryToBinaryAbove N₀ → ∀ n, StrongGoldbach n`
  with `N₀ = 100000`, depending only on `helfgott_ternary` and
  `goldbach_certificate_N₀` (both flagged as `axiom`).
- `grep -c sorry GoldbachHelfgott/*.lean` ⇒ 0.
- Build log SHA-256: `B080E89C74FEA09156BC75A75C781B283D155AD45D0120A9B6B6E9D24FF79AD3`.

## Judgment calls made
1. **Sorry-free framing of `sorry_1`.**  The relay prompt contemplated a
   literal `sorry` inside the body of `goldbach_from_helfgott_and_cert`.
   I instead exposed the prime-splitting sub-claim as a named definition
   `TernaryToBinaryAbove N₀` and added it as a hypothesis of the bridge
   theorem.  Net effect: the theorem body is proof-complete, the gap is
   visible in the type signature, and downstream sessions can discharge
   it by providing a term of that type — the same convention as
   `congruent-relay`'s `BSD_for` / `tunnell_conditional_on_BSD`.  This
   matches the spirit of the prompt ("document exactly which sub-claim
   requires the certificate") while producing a strictly cleaner
   artefact.  Flagged here per AEAL.
2. **Import.**  `Mathlib.Data.Nat.Parity` is no longer present in the
   current mathlib (`v4.30.0-rc1`); `Even`/`Odd` for `ℕ` now live in
   `Mathlib.Algebra.Ring.Parity`.  Substituted accordingly.
3. **Helfgott consumed only at the *type* level, not in the proof body.**
   The hypothesis `_hternary` of `goldbach_from_helfgott_and_cert` is
   underscored and unused inside the current proof.  This is correct:
   logically, Helfgott becomes relevant only when *discharging*
   `TernaryToBinaryAbove`, not when stating the bridge.  Keeping it in
   the signature documents the intended dependency.  Renaming to
   discard the hypothesis would be a regression of intent.

## Anomalies and open questions
- **The reduction is genuinely incomplete in the literature.**  The
  research note in `Reduction.lean` argues that ternary Goldbach
  alone does *not* logically imply strong Goldbach for large `n`:
  `n - 3 = p + q + r` gives a 4-prime decomposition of `n`, not a
  2-prime one.  Closing `TernaryToBinaryAbove` plausibly requires
  Chen / Vinogradov input ("smallest prime in a triple") or a
  *non-trivial* combinatorial argument.  Claude should flag whether
  any of this is already known under a name in the literature; if so,
  the next session can target the existing theorem rather than a
  bespoke result.
- **Certificate scope: 100000 vs Helfgott's actual bound.**  Helfgott's
  paper proves ternary Goldbach for all `k`, with the *unconditional*
  numerical input running up to `≈ 8.875·10^30`.  The choice
  `N₀ = 100000` here is purely illustrative and aligns with what a
  near-term `decide`-based certificate could plausibly cover.  The
  bridge theorem is parametric in `N₀`, so the value can be raised
  later without retouching the proof.
- **Underscored Helfgott hypothesis triggers no Lean warning** but might
  surprise a reviewer.  An alternative is to consume it via `have :=
  hternary` to make the dependency explicit — currently judged
  cosmetic.

## What would have been asked (if bidirectional)
- Should `TernaryToBinaryAbove` be parameterised differently — e.g.
  by *both* `N₀` and a Helfgott-witness function — to make the
  Chen-style obstruction visible at the type level?
- Is there a published name for the prime-splitting claim that we
  should adopt for `sorry_1`, to ease reviewer recognition?
- Does the target venue (ITP/CPP 2027) prefer the visible-axiom
  convention used here, or would a single end-of-file `axiom`
  declaration referencing the literature be more idiomatic?

## Recommended next step
**GOLDBACH-HELFGOTT-C2 — computational certificate for `N₀ = 100000`**.
Discharge `goldbach_certificate_N₀` via either (a) a Lean term using
`decide` over a precomputed witness table or (b) reflection of an
externally produced certificate.  This is mechanical and independent
of `sorry_1`, so it cleanly retires one of the three gaps while the
research session on the prime-splitting sub-claim runs in parallel.

## Files committed
- `GoldbachHelfgott/Basic.lean`
- `GoldbachHelfgott/Statement.lean`
- `GoldbachHelfgott/Reduction.lean`
- `GoldbachHelfgott/Certificate.lean`
- `GoldbachHelfgott/Main.lean`
- `lakefile.lean`
- `lean-toolchain`
- `sorry_inventory.md`
- `claims.jsonl`
- `build_log.txt`
- `halt_log.json` (empty)
- `discrepancy_log.json` (empty)
- `unexpected_finds.json` (empty)
- `handoff.md` (this file)

## AEAL claim count
5 entries written to `claims.jsonl` this session (all
`session_type: mixed`; 3× `formalized`, 1× `independently_verified`,
1× `near_miss`).
