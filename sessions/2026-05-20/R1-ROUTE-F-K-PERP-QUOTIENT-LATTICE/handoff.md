# Handoff — R1-ROUTE-F-K-PERP-QUOTIENT-LATTICE
**Date:** 2026-05-20
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~70 minutes
**Status:** COMPLETE

## What was accomplished

Implemented cycle 3b of R1-ROUTE-F: identified the rank-2 quotient lattice
**Q := K_X^⊥ / L_δ** for the PIII(D_6) Sakai surface. Computed an explicit
Z-basis via Smith Normal Form of the 9×7 integer matrix whose columns are the
seven KNY simple roots δ_i in K_X^⊥ coordinates; pulled back the cokernel via
the unimodular U^{-1} from the SNF triple (D, U, V). Delivered the new
module `sakai_d6/quotient.py` with 22 new tests (147 passing total) and the
verifier CLI `python -m sakai_d6.quotient --analyze`. **The synthesizer's
pre-registered verdict `Q_LORENTZIAN` is FALSIFIED**; the actual verdict is
`Q_DEFINITE_NEGATIVE` with Gram matrix coinciding exactly with the A_2 root
lattice in negative-definite sign convention. Diagnosis of the
pre-registration error is recorded in three deliverables.

## Key numerical findings

- **Verdict:** `Q_DEFINITE_NEGATIVE` (5-branch enumeration; cycle-3b verifier, exact integer dps=0)
- **Z-basis of Q in Pic coords:** q_1 = E_4 − E_1, q_2 = E_8 − E_1 (cycle-3b verifier, dps=0)
- **Z-basis of Q in K_⊥ coords:** q_1 = b_5, q_2 = b_9 (i.e. unit vectors at positions 4 and 8 zero-indexed in the cycle-2 K-perp basis) (cycle-3b verifier, dps=0)
- **Gram(Q):** [[−2, −1], [−1, −2]] (cycle-3b verifier, dps=0)
- **Discriminant det(Gram(Q)):** 3 (cycle-3b verifier, dps=0)
- **Signature (p, n, z):** (0, 2, 0) — rank-2 negative-definite (cycle-3b verifier, dps=0)
- **Structural identification (NOT promoted to AEAL):** Gram(Q) is the A_2 root lattice Gram matrix in negative-definite sign convention; |disc(A_2)| = 3 matches; each q_i is a (−2)-vector with mutual 120° angle.
- **SNF decomposition contract:** D, U, V (sympy `smith_normal_decomp`) of A = M^T (9×7) satisfies U·A·V = D with det(U) = −1, det(V) = +1, D diagonal (1,1,1,1,1,1,1) + zero rows 7–8. Quotient basis = last two columns of U^{−1}, saturated by unimodularity of U.
- **−K_X projection to zero verified:** U·(−K_X in K-perp coords) = (1, −1, 2, 2, 1, 1, 1, 0, 0). The last two entries vanish, confirming −K_X ∈ col(A) = L_δ (cross-check of cycle-2 pinned identity ∑ a_i δ_i = −K_X with a = (1,1,2,2,2,1,1)).

SHA256 of `python -m sakai_d6.quotient --analyze` UTF-8 stdout:
`a3b766241e15f0cf474a77452758e9a66ed30bbbf08c2b6983a49256d9296812`

Pytest: **147 passed in 7.44s** (125 from cycles 1–3a + 22 new cycle-3b tests).

## Judgment calls made

1. **Pre-registered Q_LORENTZIAN in `test_quotient.py`** before any computation
   ran (`PREREGISTERED_VERDICT = "Q_LORENTZIAN"`, declared at top of file).
   Tests assert allowed-branch membership (5-branch enumeration), NOT the
   specific pre-registered branch — matching the brief's stated signature
   envelope p ∈ {0, 1}, n ∈ {0, 1, 2}. Result: the pre-registration was
   falsified by the substrate. No test failed because the falsification is
   a legitimate verdict-branch resolution (not a substrate contradiction
   and not a halt-condition trigger).

2. **Did NOT promote the A_2 lattice identification to an AEAL claim.** Per
   the pre-registered `scope_extensions_explicitly_NOT_promoted_to_AEAL`
   list in `claim-r1-k-perp-quotient-001.json`. The identification is
   recorded as a structural hint in handoff (this file),
   `unexpected_finds.json`, and the claim file's
   `actual_lattice_identification_structural_hint`, but NOT in
   `claims.jsonl`. Synthesizer decides whether to dispatch a follow-on
   cycle 3c that promotes it.

3. **Used exact integer det/trace logic for verdict resolution** rather
   than numerical eigenvalues. For 2×2 symmetric integer Gram matrices,
   (det, trace) fully determines the signature; this sidesteps
   `HALTED_NUMERICAL_SIGNATURE_AMBIGUOUS` by construction.

4. **Substrate read directly from source.** Both `saturation.py` and
   `effectivity.py` were read in full before module code was written,
   and the SNF convention was independently verified via a one-shot
   smoke script (subsequently deleted) before being committed to
   `quotient.py`.

5. **Did NOT halt on the pre-registration falsification.** Per the brief's
   explicit invitation ("If the verdict is anything other than
   Q_LORENTZIAN, that's a finding worth recording prominently"), halt is
   reserved for substrate contradictions, not for verdict-branch
   resolutions to a different-than-expected allowed branch.

## Anomalies and open questions

**Anomaly — pre-registered Q_LORENTZIAN is falsified.** Diagnosis:

The synthesizer's pre-registration reasoning had an **off-by-one in the
isotropic-line signature reduction**. The synthesizer wrote:

> "Pic form restricted to K_X^⊥ has rank-1 radical spanned by −K_X, so the
> non-degenerate part has signature (1, 7) on the rank-8 lattice K_X^⊥ / ⟨−K_X⟩."

The correct rule: for an isotropic line L in a non-degenerate real symmetric
form of signature (p, q), the quotient L^⊥ / L has signature **(p − 1, q − 1)**,
not (p, q − 1). The positive direction is annihilated together with one negative
direction because the isotropic line L pairs with a transversal isotropic line
outside L^⊥ to form a hyperbolic plane. Specifically: Pic decomposes as
(hyperbolic plane ⟨L, L'⟩) ⊕ (orthogonal complement) where ⟨L, L'⟩ has
signature (1, 1) and the complement has signature (0, 8); and L^⊥ / L equals
that complement.

**Corrected accounting:**
- Pic (1, 9) → K_X^⊥ / ⟨−K_X⟩ has signature **(0, 8)** (not (1, 7))
- L_δ / ⟨−K_X⟩ = finite D_6 root lattice = (0, 6) (negative-definite)
- Q = (0, 8) − (0, 6) = **(0, 2)**, matching computed result.

The substrate (cycles 1, 2, 3a) is internally consistent. The
pre-registration was the error.

**Open question for synthesizer (structural).** Q is exactly the A_2 root
lattice (negative-definite sign convention). Candidate interpretations to
be evaluated externally:

1. **W(A_2) = S_3 reflection symmetry on Q.** Three reflections through
   q_1, q_2, and q_1 + q_2 = E_4 + E_8 − 2 E_1 generate S_3. Whether this
   S_3 symmetry has any meaning in the PIII(D_6) Bäcklund framework is
   open.
2. **Mismatch with the PIII(D_6) Bäcklund symmetry group.** The Bäcklund
   symmetry group for PIII(D_6) is W(A_1^{(1)}) (affine A_1), NOT A_2. So
   any naive identification Q ≅ "PIII(D_6) symmetry lattice" is wrong.
   The A_2 here is at a different level — possibly a sublattice or a
   transversal frame — and warrants separate interpretation by the
   synthesizer.
3. **Transversal frame between chain tips.** Geometrically, q_1 = E_4 − E_1
   and q_2 = E_8 − E_1 are the differences between chain-tip (−1)-curves
   of chains {3,4} and {5,6,7,8} relative to the head of chain {1,2}. The
   S_3 symmetry permuting the three chain heads/tips is suggestive but
   not pursued here.

**Open question for synthesizer (procedural).** Whether to dispatch a
follow-on cycle 3c that promotes the A_2 identification to its own AEAL
claim, OR to proceed directly to the V_quad connection per the original
three-cycle brief.

## What would have been asked (if bidirectional)

- "The pre-registered Q_LORENTZIAN looks falsified by the substrate (Gram
  is [[-2,-1],[-1,-2]], not indefinite). The synthesizer's signature
  reduction appears to have an off-by-one. Do you want me to halt and
  re-scope, or proceed with `Q_DEFINITE_NEGATIVE` as the actual verdict
  and document the falsification?" — Resolved autonomously per the brief's
  explicit invitation: the brief says "If the verdict is anything other
  than Q_LORENTZIAN, that's a finding worth recording prominently"; halt
  is reserved for substrate contradictions, not for verdict-branch
  resolutions.

## Recommended next step

**Pause for synthesizer digestion before connecting Q to V_quad.** The
falsification of the pre-registered verdict is a non-trivial input that
should be reviewed before any downstream cycle is dispatched.

Three plausible next moves, in order of agent recommendation:

1. **(Recommended) Cycle 3c — A_2 promotion.** Promote the A_2 identification
   to an AEAL claim with W(A_2) = S_3 symmetry explicitly checked on Q
   (verify each q_i acts as a reflection; the three reflections generate
   S_3; record on which Pic-class elements the group acts non-trivially).
2. **Cycle 4 — V_quad connection.** Skip A_2 promotion and proceed directly
   to the connection between Q (or equivalently the rank-2 lattice of
   "elliptic fibre transversal" classes) and the V_quad transcendent of
   the original R1-ROUTE-F brief.
3. **Cycle 3c' — synthesizer-side signature-accounting re-derivation.**
   Verify the (p − 1, q − 1) reduction independently and update the
   cycle-1/2/3a signature-accounting notes accordingly so downstream
   cycles inherit the corrected substrate.

Agent recommends option 1 (A_2 promotion) before option 2 (V_quad) to avoid
carrying a "structurally interesting unclassified output" forward
indefinitely.

## Files committed

`sessions/2026-05-20/R1-ROUTE-F-K-PERP-QUOTIENT-LATTICE/`

- `COMPLETION_REPORT.md` — cycle-3b completion report (overwritten from cycle-3a; cycle-3a version preserved at `sessions/2026-05-20/R1-ROUTE-F-EFFECTIVITY/`)
- `handoff.md` — this file
- `claims.jsonl` — 4 cumulative AEAL lines (cycles 1, 2, 3a, 3b)
- `claims/claim-r1-k-perp-quotient-001.json` — cycle-3b pre-registered AEAL claim with `actual_*` block including `actual_verdict_alignment_with_pre_registration: FALSIFIED` and full diagnosis
- `quotient_verdict.json` — computed verdict artefact
- `quotient_basis_provenance.json` — SNF construction provenance
- `unexpected_finds.json` — 4 cycle entries with cycle-3b headline finding + diagnosis
- `halt_log.json` — empty `{}` (no halt fired)
- `discrepancy_log.json` — empty `{}` (no discrepancy fired)
- `sakai_d6/quotient.py` — new module (~340 lines)
- `sakai_d6/tests/test_quotient.py` — new test file (~290 lines, 22 tests)

## AEAL claim count

**1** new entry written to `claims.jsonl` this session (`r1-k-perp-quotient-001`).
`claims.jsonl` cumulative total: **4** lines (cycles 1, 2, 3a, 3b).
