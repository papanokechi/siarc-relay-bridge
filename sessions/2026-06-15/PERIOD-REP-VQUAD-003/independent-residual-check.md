# Stage 0.1 — Independent L_V residual confirmation

**Chain:** PERIOD-REP-VQUAD-003 · **Stage:** 0.1 (carryover spot-check) · **Date:** 2026-06-15
**Scripts:** `scripts/stage0_residual_check.py` → `scripts/stage0_residual_results.json`

## Purpose
VQUAD-002 verified `L_V · B̂ = 0` by a **hand-rolled ℚ(√3) (Fraction-pair) Gaussian
elimination / null-space** recognizer. HALT-GATE-0 requires an *independent*
re-confirmation. A literal second commercial CAS (Maple/Mathematica) is not
available in this environment, so independence is obtained from **two engines that
share no code with that recognizer**:

- **Method A — sympy exact symbolic** over ℚ(√3) (`sqrt(3)` kept symbolic, `Rational`
  arithmetic). Computes the residual `res_N = Σ_k Σ_i p_{k,i}·falling(N−i+k,k)·b_{N−i+k}`
  at the requested orders and checks it is **identically 0**.
- **Method B — mpmath high-precision numeric** (dps = 160), with the asymptotic
  coefficients `aₙ` regenerated **independently** from the deposited
  `REPRODUCE_stokes_2piK.py` Riccati recursion (not from the Q3 port).

`L_V`'s coefficients were **hand-transcribed** from VQUAD-002
`operator-verification.md` §4.0(b), so a vanishing residual also validates that
human-readable transcription.

## Inputs
`b_m = a_{m+1}/m!` (Borel-transform sequence). Orders checked: **N ∈ {10, 20, 30, 40, 50}**
(the task's five coefficients), each requiring `b_m` up to `m = N+4`.

## Results

| N | Method A (sympy exact) | Method B (mpmath, dps 160) relative residual |
|---|------------------------|----------------------------------------------|
| 10 | `0` (identically) | 6.0e-162 |
| 20 | `0` (identically) | 5.4e-162 |
| 30 | `0` (identically) | 0.0 |
| 40 | `0` (identically) | 1.7e-161 |
| 50 | `0` (identically) | 0.0 |

- **Method A:** residual is the symbolic integer `0` at every order — an exact
  algebraic identity over ℚ(√3).
- **Method B:** worst relative residual **1.7e-161**, i.e. at the dps-160 floor.

## Verdict
**CONFIRMED.** Two independent engines (exact-symbolic sympy; high-precision mpmath
with independently-generated `aₙ`) both confirm `L_V` annihilates `B̂` at all five
orders. The VQUAD-002 operator survives independent re-verification, and the
`operator-verification.md` transcription is correct. **HALT GATE 0 (residual): PASS.**
