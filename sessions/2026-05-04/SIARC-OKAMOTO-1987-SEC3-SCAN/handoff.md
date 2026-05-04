# Handoff — SIARC-OKAMOTO-1987-SEC3-SCAN

**Date:** 2026-05-04
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~30 minutes
**Status:** COMPLETE

## What was accomplished

Executed prompt 036 in full: a targeted §§3+ + appendices readback
of Okamoto 1987 (slot 07) to determine whether the cokernel
generator π : (v_1, v_2) ↦ (−1 − v_1, v_2) of 033's
homomorphism appears as a named element of Okamoto's symmetry
group `G ≅ W^aff(B_2)` or its enlargement `G_*`.  Complete
enumeration of every named parameter transformation in the paper
(13 entries; A.2 of `extract_okamoto_sec3_pi.md`) plus a sympy
lattice-classification check (`verify_pi_outside_W_aff.py`)
confirms π is **not** in any Okamoto-listed generator nor any
composition thereof, and identifies the cokernel Z/2 with
`P^∨(B_2) / Q^∨(B_2)` (the standard B_2-centre Z/2).
Outcome: `CONFIRM_M6_PHASE_B5_INDEX2_FINAL` (spec §7); 033's
INDEX-2 finding is final at the Okamoto-paper level.

## Key numerical findings

- Okamoto 1987 §§3+ readback exhaustive: NO transformation
  with action (v_1, v_2) ↦ (−1 − v_1, v_2) in §§1.3, 2.1, 2.3,
  2.5, 2.6, 3.1–3.5, 4.1–4.3.  Closest candidate `s` (§1.3 (ii))
  acts as (v_1, v_2) ↦ (−v_1 − 2, v_2) — differs by a
  Z/2-class translation (sympy verified).
- `T_{(−1, 0)} ∉ Q^∨(B_2)`: sympy solves
  `(m, 2n − m) = (−1, 0)` over integers, no solution; cross-check
  confirms ℓ-shift (1, 1) and ℓ̃-shift (1, −1) ARE in Q^∨.
  (script: `verify_pi_outside_W_aff.py`, log line 6.)
- `Q^∨(B_2)` parity rule:  `{(a, b) ∈ Z² : a + b even}`;
  `P^∨(B_2)` = full Z²; index 2 (= centre of Spin(5) = Sp(2)).
- π is an involution: sympy verifies π² = id (log line 24).
- π = s ∘ T_{(−1, 0)} ∈ W^ext(B_2) \ W^aff(B_2);
  this **is** the cokernel Z/2 of 033's φ.

## Judgment calls made

- Spec §2 PHASE A.1 referred to "§3+ likely contains: Bäcklund
  transformation tables (T_1, T_2, T_3, ...)".  No such tables
  exist in the paper; §3 is about Toda equation + τ-function
  iteration of the §2 generators.  I treated this as confirming
  the negative-finding path, not as a halt.
- The paper has no appendix.  I treated this as part of the
  exhaustive §§3+ scan completing (rather than as a halt for
  missing appendix material).
- Phase B option B.2 (non-promotion) selected per spec; wrote
  `non_promotion_index2_final.md` rather than
  `promotion_to_strict_iso.md`.
- AEAL-level extension: I added the lattice-theoretic
  `P^∨/Q^∨` explanation (B.3.a + verify script Phase v) as a
  beyond-spec elaboration that strengthens 033's classification
  with a 1-line topological reason.  Logged as Unexpected
  Find #1.

## Anomalies and open questions

- **Lattice-theoretic re-framing.**  The cokernel Z/2 of 033's
  φ is exactly `P^∨(B_2) / Q^∨(B_2)`, the centre of
  `Spin(5) = Sp(2)`.  This was implicit in 033 but is now
  explicit (Unexpected Find #1).  Suggests CT v1.4 §3.5 / M6
  spec language could be tightened by naming this directly.
- **Okamoto's `−2` vs `−1` shift convention.**  Okamoto §1.3
  (ii) defines `s : θ_0 ↦ −θ_0 − 2` rather than the algebraically
  natural `−θ_0 − 1`.  This is a **deliberate** choice to keep
  `s` inside `W^aff(B_2)`; Sakai's framework needs the `−1`
  variant via the `Aut(D_6^(1))` factor.  Logged as Unexpected
  Find #2.  This is not a defect, but it is a piece of
  methodological context worth including in the picture v1.18+
  M6 row notes.
- **No appendix in slot 07 source.**  Confirmed by exhaustive
  grep on slot 07 .txt; reference list begins at L2342.  This
  is a feature of the paper itself, not an artefact of the
  pdftotext extraction.

## What would have been asked (if bidirectional)

- "Should the v1.18 picture M6 row text be re-phrased now to
  name `P^∨/Q^∨ ≅ Z/2` directly, or kept at INDEX-2 with a
  lattice-theory footnote?"  (Operator + Claude reconcile;
  recommendation in B.4 of `non_promotion_index2_final.md`.)
- "Is there value in repeating the §§3+ scan against Okamoto's
  P_VI 1987 or P_IV 1986 papers, where the analogous index-N
  obstruction would be different (P_VI: F_4 → D_4^(1)
  related)?"  (Out of scope for 036; logged here for synthesis
  awareness.)

## Recommended next step

If the operator decides to absorb 036 into v1.19 of the picture:
draft a 2-line line-edit for the M6 row Anchors/Notes column
naming `P^∨(B_2)/Q^∨(B_2) ≅ Z/2` as the cokernel (text in
B.4 of `non_promotion_index2_final.md`).  Otherwise no
v1.18 amendment is needed — 035 v1.18 deposit decision is
independent of 036's verdict.

## Files committed

All under `sessions/2026-05-04/SIARC-OKAMOTO-1987-SEC3-SCAN/`:
  - `extract_okamoto_sec3_pi.md`           (Phase A primary deliverable)
  - `non_promotion_index2_final.md`        (Phase B writeup)
  - `verify_pi_outside_W_aff.py`           (sympy lattice-classification)
  - `verify_pi_outside_W_aff.log`          (sympy run output)
  - `claims.jsonl`                         (8 AEAL entries)
  - `halt_log.json`                        (empty `{}` — no halts)
  - `discrepancy_log.json`                 (empty `{}` — no discrepancies)
  - `unexpected_finds.json`                (2 finds — lattice re-framing,
                                            Okamoto shift convention)
  - `prompt_spec_used.md`                  (execution parameters)
  - `handoff.md`                           (this file)

## AEAL claim count

8 entries written to `claims.jsonl` this session.
