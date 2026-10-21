# CT-S54 — PREREG: is Method B independent of the Stokes datum?

Written **before** any computation in this session. Reading of existing files
had already happened; no number below is fitted to a result.

## Hypothesis under test

**H.** The paper's §5.3 sentence — *"Method B is independent of the Stokes
datum: it derives S e^{−ξ₀} from the cycle and the branch exponent, rather
than assuming S"* — and Table 2's row *"B … Independent of: the Stokes datum"*
are **overclaims with respect to the derivation as printed and the script as
cited**, because eq. (26) substitutes A = (S/2πi)Γ(1+β), and
`stage4_methods.py` sets `A_amp = K*G1pb` with S = 2πK.

## Observables

| id | observable | computed from |
|---|---|---|
| **O1** | `relB` = ‖A e^{−ξ₀}·2πi/Γ(1+β)‖ vs S e^{−ξ₀}, relative | corpus formulas, `A_amp = K·Γ(1+β)` |
| **O2** | `relC1` = ‖2πi A/Γ(1+β)‖ vs S, relative | same |
| **O3** | `relC2` = (‖A‖/‖β‖) vs deposited C, relative | same |
| **O4** | `relB_indep` = Method B rebuilt on the **independently extracted** A of Stage 1.4 (`numerical-integral.md` §2), vs S | A_extracted, which is fitted to b_m and never sees S |

## Predictions, fixed now

1. **P1.** O1 and O2 are *the same quantity*: relB ≡ relC1 algebraically, the
   factor e^{−ξ₀} cancelling. Both print 8.84×10⁻⁴⁶.
2. **P2.** Perturbing S alone moves O1 and O2 **identically** (same value to
   every digit), and does **not** move O3.
3. **P3.** Perturbing K alone moves all of O1, O2, O3.
4. **P4.** O4 ≠ O1. Stage 1.4 reports the independent period reconstruction at
   **3.7×10⁻⁴⁶** on a row distinct from the **8.8×10⁻⁴⁶** row, which is the
   *symbolic collapse* 2KΓ(1+β)Γ(−β)|sin π(1+β)| = 2πK.

P1–P4 are recorded before running. P4's two figures are transcribed from
`numerical-integral.md` §3, not predicted by me.

## Falsifiers, with thresholds

- **F1.** If P2 fails — i.e. perturbing S moves O1 and O2 by *different*
  relative amounts (differing by more than 1×10⁻⁴⁰ of each other) — then B and
  C are not the same comparison and **H is false**; report that.
- **F2.** If perturbing S leaves O1 unmoved (relative change < 1×10⁻⁴⁰), then
  Method B really is independent of the Stokes datum and **H is false**.
- **F3.** If O4 agrees with O1 to within 1×10⁻⁴⁸ relative, then the
  independent route reproduces the same figure and the distinction drawn in
  P4 is empty; report that the finding is weaker than stated.
- **F4.** If the independently extracted A of Stage 1.4 cannot be located or
  does not reproduce, **halt** — the "rescue" route is unavailable and the
  finding is a retraction rather than a rewording.

## Vacuity pre-check

The observable must move when the data the hypothesis is about moves. The
discriminating form here is not "does anything move" but **which things move
together**:

- O3 must be **insensitive** to a perturbation of S (it depends on K, β, C).
- O1 and O2 must be **sensitive** to it, and by the same amount.

If *everything* moves, or *nothing* moves, the instrument cannot separate
"shared input" from "common dependence" and the pre-check fails.

**Ordering.** Per CT-S47's finding, the observable is evaluated **first**; the
vacuity block runs after and, if the observable has already fired, is reported
as moot rather than being allowed to convert a finding into a refusal.

## Controls that can fail

- **A0 positive baseline.** A construction known to be genuinely independent
  of S must be exhibited and must show insensitivity — O3 plays this role. If
  O3 moves with S, the instrument is broken.
- **Negative control.** A construction known to depend on S — O2, which is
  explicitly `|2πiA/Γ(1+β)|` against S — must show sensitivity.

## Scope, and what this cannot settle

This session tests the **independence claim** only. It does **not** re-derive
the main identity, does not touch Part A's ξ = 0 result, and does not revise
the manuscript. A conclusion drawn from reading definitions and re-running
corpus formulas is **STRUCTURAL** at most for the independence question, and
**VERIFIED** for any numerical coincidence, with dps and residual stated.

## Halt conditions

Per P0: a falsifier fires, a convention is ambiguous, required data is
missing, or runtime exceeds 3× budget.

## Governance

Nothing committed, sent, deposited or submitted. No earlier session's files
are modified; corpus scripts are **read and re-implemented here**, never
edited in place.
