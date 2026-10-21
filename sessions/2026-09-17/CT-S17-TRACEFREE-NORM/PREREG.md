# CT-S17-TRACEFREE-NORM — PRE-REGISTRATION

Written **before any computation**, per P0.

Session: `sessions/2026-09-17/CT-S17-TRACEFREE-NORM/`
Origin: operator review #13, the "up to rank-1 twist" caveat on CT-S16's
membership result.

---

## 1. The question

CT-S16 established membership by matching **projective normal potentials**:
System C's `r_z` equals the family's scalar-reduction potential `R` at an
explicit point of `U₀`. The potential `r` is an invariant of the *projective*
connection, so on its face the match determines the connection only up to a
rank-1 twist.

The operator's proposed reading is that this is a **normalisation remark, not a
gap**: a rank-1 twist changes the trace but not the projective connection, van
der Put–Saito classify trace-free connections, so each projective class should
contain exactly one trace-free representative.

## 2. Hypotheses

- **T1 (uniqueness under twist).** Among `{A + λI : λ a rational 1-form}` there
  is exactly one trace-free member.
- **T2 (no residual ambiguity).** Trace-freeness alone pins the representative
  down, i.e. a projective class contains at most one trace-free differential
  module up to isomorphism.
- **T3 (the decisive one).** The differential module of System C is isomorphic
  **as a differential module** — not merely projectively — to the family's
  module at the located point `(p,q,t,θ_∞)`.

T1 is expected to be trivially true. **T2 is pre-declared as DOUBTED**: tensoring
by a rank-1 module `L` with `L⊗L` trivial preserves both the projective class and
triviality of the determinant, so if a non-trivial 2-torsion `L` exists over
`C(z)` then T2 is false as stated and the operator's argument needs a sharper
hypothesis than trace-freeness. I record this expectation now so that confirming
it cannot be presented afterwards as having been obvious.

**T3 is the hypothesis that actually decides what the notice may say.** If T3
holds, the caveat disappears entirely and is replaced by a statement about the
actual connection; if T3 fails, the caveat is real and must stay.

## 3. Observables and falsifiers

- **T1**: solve `tr(A + λI) = 0`. Falsifier: more than one, or no, solution.
- **T2**: exhibit a rank-1 module `L = d + f` over `C(z)` with `L⊗L` trivial but
  `L` non-trivial, i.e. `f = −u′/2u` with `u` rational and `√u` **not** rational.
  Falsifier for T2: no such `L` exists.
- **T3**: compare the second-order scalar operators. A second-order operator is
  determined by its pair `(P, Q)`. Reduce both System C (in the `z` coordinate,
  `x = s₊ + δz`) and the family at the located point (cyclic vector `e₁`) to
  `∂² + P∂ + Q` and compare **both** coefficients as rational functions.
  - **T3 SATISFIED** iff `P_C ≡ P_fam` **and** `Q_C ≡ Q_fam` identically.
  - **Falsifier:** either coefficient differing by a non-zero rational function.
  - Threshold: exact symbolic equality, plus a numeric check at dps 60 with
    relative residual `< 1e-40` at five points. Matching `Q` alone, or `R` alone,
    does **not** count — that is precisely the projective-only statement CT-S16
    already had.

## 4. Vacuity pre-checks

1. **The comparison must be able to fail.** Perturb the located `q` by `10⁻³` and
   confirm the `(P,Q)` comparison then reports a non-zero difference. A test that
   passes for a wrong point is void.
2. **`P` must be able to differ.** Exhibit a second-order operator with the same
   `R` but a different `P`, and confirm the test separates it from System C.
   Without this, `P ≡ P` might hold trivially by construction rather than as a
   fact about these two objects.

Both controls are **assertions**; the run aborts if either misbehaves. This is
the standing lesson that a step which cannot fail cannot be trusted to report
failure.

## 5. Labels (fixed now)

- T1: **PROVEN** if exact.
- T2: **PROVEN** if a non-trivial 2-torsion `L` is exhibited explicitly.
- T3: **PROVEN** if both coefficients match identically and both controls fire
  correctly; **STRUCTURAL** if only a symbolic-plus-numeric match is obtained.
- Any consequence for the membership label from CT-S16: **STRUCTURAL at most**,
  and membership is **not** raised above STRUCTURAL in this session regardless of
  outcome, because the operator tied any such raise to step 3(b), which remains
  unrun.

## 6. Halt conditions

- T3 falsified ⇒ stop, report that the caveat is real, do not search for a
  weaker equivalence to rescue it.
- Either vacuity control failing ⇒ the run is void; report it as such.
- Any ambiguity in the family's coefficients traceable to the p.2655 `b(z)` typo
  ⇒ stop and report, rather than choosing a reading to suit the outcome.

## 7. Out of scope

No notice or conjecture file is edited by the computation in this session. The
C3 rewrite authorised in review #13 is a separate, operator-dictated text change
and is recorded independently of whatever T1–T3 return.
