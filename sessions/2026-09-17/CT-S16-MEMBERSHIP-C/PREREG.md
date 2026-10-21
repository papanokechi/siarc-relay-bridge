# PREREG — CT-S16-MEMBERSHIP-C

Written **before** any computation in this session, per P0.

Session: `sessions/2026-09-17/CT-S16-MEMBERSHIP-C/`
Date: 2026-09-17

---

## The question

Does the rank-2 connection defined by **System C** (companion v1.2 normalisation,
coordinate `x`) satisfy the hypotheses under which van der Put–Saito build the
moduli space `M` for the `(0,0,1)` row?

This is deliberately *not* "guess a deformation and test it". The operator's
reframing: in a moduli-space framework the Painlevé equation is the isomonodromy
foliation on `M`, so every point of `M` already lies on a leaf. Membership then
reduces to a hypothesis check, and a negative answer is a finding rather than the
failure of one ansatz.

**The framework reading above is from the operator's memory and is NOT assumed.**
Step 1 must confirm it from page images. If van der Put–Saito do not state (b) in
that form, this session HALTS at step 1 and reports what the paper does say.

## The object

System C, from companion v1.2:

> `A W'' + A′ W' + C W = 0`,  `A = 3x² + x + 1`,  `A′ = 6x + 1`,  `C = −x²`

Singular points: the roots `s± = (−1 ± i√11)/6` of `A` (regular singular), and
`x = ∞` (irregular, Katz invariant 1). Multiset `(0,0,1)`.

Prior finding carried in (cold, `R1-83`/C1): at `s±` the indicial polynomial is
`λ²`, exponents `[0,0]`, and a log term is **forced**, so the local monodromy is
**unipotent and ≠ I**.

## Hypotheses to be tested (step 2)

| # | Hypothesis | Observable | Verdict values |
|---|---|---|---|
| H-a | local data at `s±` are of the kind `M` admits | residue matrices; diagonalisability; resonance; monodromy Jordan type | SATISFIED / VIOLATED / UNDECIDED |
| H-b | the connection is irreducible | does `L` factor over `C(x)`; existence of `exp(∫ r)` solutions | SATISFIED / VIOLATED / UNDECIDED |
| H-c | the time invariant is well defined and matches | `t` computed from the configuration per 1(b) vs the companion's `t = ∓2i√33/9` | SATISFIED / VIOLATED / UNDECIDED |

**Pre-declared expectation** (recorded so it cannot be retro-fitted): H-a is the
one at risk, because resonance with a log term is exactly the situation in which
Jimbo's `(A1)` fails. I expect H-a to be VIOLATED or UNDECIDED. If instead every
hypothesis is SATISFIED, step 3 runs.

## Falsifier (step 3b) — numeric, threshold fixed now

Only runs if **all** of H-a, H-b, H-c are SATISFIED.

- Integrate PV from `(t₀, q, p)` to `t₁ = t₀ + ε`, for **two** values of `ε`
  (`ε = 10⁻³` and `ε = 10⁻⁴`), at dps ≥ 40.
- Rebuild the linear system at `t₁`; compute monodromy and Stokes data.
- **Threshold: agreement with C's data at `t₀` to ≥ 30 significant digits.**
- Anything worse **falsifies the construction** (the normal form / leaf
  placement), NOT membership in general. This distinction is pre-declared.

## Vacuity pre-checks

1. **Step 3c (declared, runs only with step 3).** Perturb `(q, p)` off the leaf by
   `10⁻⁶`; the monodromy data must then change by **more than** the 30-digit
   threshold. If perturbing does not move the observable, the falsifier is
   vacuous and the result is void.

2. **Step 2 vacuity (runs regardless).** The hypothesis check is only meaningful
   if the tests can return both answers. Therefore:
   - *H-a:* apply the same residue/monodromy computation to a **control** operator
     with known semisimple, non-resonant local data, and confirm the test reports
     it as such. If the test says "resonant" for everything, it is vacuous.
   - *H-b:* apply the factorisation test to a **known reducible** operator and to
     a **known irreducible** one, and confirm the test separates them.

## Halt conditions (P0, plus session-specific)

- Step 1(b) not stated in the moduli/foliation form → **HALT**, report.
- Any hypothesis UNDECIDED → step 3 does **not** run; report UNDECIDED.
- A convention needed for `t` is ambiguous → HALT rather than choose silently.
- Page images unreadable → HALT (an agent that cannot view an image must say so;
  OCR does not satisfy the reading rule).

## Labels (fixed now)

- Framework quotes: **INSPECTED**.
- Hypothesis verdicts: **PROVEN** only where the test is fully exact (symbolic,
  no numerics); otherwise VERIFIED or STRUCTURAL.
- Membership: **STRUCTURAL at most**, and only if steps 1 and 2 both pass.
- Step 3 results: **VERIFIED**.

## Prohibitions

No commits, deposits, submissions. Do not edit any notice or conjecture file.
Symbolic equality is established by simplifying the difference to zero **and** a
high-precision numeric check — never by `==` on unevaluated radicals.
