# CT-S17-TRACEFREE-NORM — REPORT

Session: `sessions/2026-09-17/CT-S17-TRACEFREE-NORM/`
Origin: operator review #13 — the "up to rank-1 twist" caveat on CT-S16.
Nothing committed, deposited or sent.

---

## 0. Headline

**Your conclusion is right. Your reasoning for it is not.**

- The caveat **is withdrawn**: System C's differential module is isomorphic to
  the van der Put–Saito family's module at the located point — not merely
  projectively isomorphic. Membership is about the actual connection.
- But it is **not** withdrawn for the reason given in review #13. Trace-freeness
  alone does **not** single out a representative of a projective class. That part
  is false, and I have a counterexample.

Per the P0 rule adopted in review #11 — *a correct finding does not certify the
reasoning around it; each adopted statement is verified on its own* — I am
applying that rule to the review itself.

---

## 1. T1 — what is true in the argument (PROVEN)

A rank-1 twist acts by `A ↦ A + λI` and changes the trace by `2λ`. So
`tr(A + λI) = 0` has the unique solution `λ = −tr(A)/2`. **Within the orbit of
one connection under rank-1 twists, the trace-free member is unique.** (`S17-01`)

## 2. T2 — what is false (PROVEN false, by counterexample)

The step from T1 to *"exactly one trace-free representative in each projective
class"* does not hold. Different projectively-equivalent connections need not lie
in a single twist orbit.

Take `L = d − 1/(2z)` over `C(z)`:

| | | |
|---|---|---|
| `L ⊗ L = d − 1/z` | **trivial** | witness `w = z`, and `2f + w′/w = 0` exactly |
| `L` itself | **non-trivial** | residue of `f` at `0` is `−1/2 ∉ Z`, so `f` is not the logarithmic derivative of a rational function |

So a **non-trivial 2-torsion** rank-1 module exists. Tensoring a trace-free module
by it preserves *both* the projective class *and* triviality of the determinant.
Hence a projective class can contain more than one trace-free module up to
isomorphism. (`S17-02`)

I **pre-registered T2 as doubted** in `PREREG.md` before computing, precisely so
that this could not be presented afterwards as having been obvious.

## 3. T3 — the decisive test (PROVEN)

A second-order operator is determined by the **pair** `(P, Q)` in `∂² + P∂ + Q`.
CT-S16 matched only `R = P²/4 + P′/2 − Q`, which is *blind* to a rank-1 twist.
Comparing **both** coefficients is not blind to it.

| | `P` | `Q` |
|---|---|---|
| System C in `z` | `(2z−1)/(z(z−1))` | `(22z²−22z−2i√11 z+5+i√11)/(54z(z−1))` |
| family at `(p,q,t,θ_∞)` | **identical** | **identical** |

`P_F − P_C = 0` and `Q_F − Q_C = 0` identically; worst relative residual `0` over
five points at dps 60. **The two differential modules are isomorphic.** (`S17-04`)

**Both vacuity controls fired** (assertions, per standing practice):

1. `q` perturbed by `10⁻³` → the comparison reports a non-zero difference, so the
   test can reject a wrong point.
2. An operator with the **same `R` but different `P`** is separated by the `(P,Q)`
   test and *not* by `R` — confirming the new test sees exactly what the old one
   could not.

### Why it works out — not a coincidence

`3x² + x + 1 = 3(x−s₊)(x−s₋) = 3δ²·z(z−1) = 3δ²D`. Hence System C's own Wronskian
coefficient is `P_C = δ(6x+1)/(3x²+x+1) = D′/D`; and the family's is
`P = D′/D − b′/b`, which equals `D′/D` exactly when `b` is constant — i.e. when
`b₁ = 0`, which is the condition CT-S16's match already forced. **The two objects
carry the same rank-1 twist**, so none has to be inserted between them. (`S17-05`)

## 4. What this does and does not change

- **Statement:** membership is now about System C's actual differential module.
  The phrase "up to rank-1 twist" should be **deleted**, not softened.
- **Label:** membership stays **STRUCTURAL**. You tied any raise to step 3(b),
  the monodromy/Stokes falsifier, which remains unrun. Pre-registered; not
  revisited after seeing the result. (`S17-08`)
- **Sharper wording available if you want it:** rather than *"its trace-free
  connection is a point of the moduli space"*, the provable statement is *"the
  differential module of System C **is** the module of the van der Put–Saito
  family at an explicit point of `U₀`"*. I applied your drafted wording as given;
  this is offered, not substituted.

## 5. Open question, deliberately not answered

Since trace-freeness alone is insufficient, **what is the correct sharper
hypothesis** under which a projective class has a unique representative in vdPS's
normalised form? A 2-torsion twist shifts local exponents by `½`, but individual
local exponents depend on the lattice, so whether the normalisation
"local exponents `±θᵢ/2`" excludes such twists needs an argument I did not make.
Flagged under the P0 halt rule rather than guessed. The membership result does
not depend on it. (`S17-07`)

## 6. Defect caught in this session's own first run

The first T2 run printed **"L ⊗ L trivial? False"** — which *contradicted the
conclusion drawn three lines later in the same block*. The test had compared `2f`
against `−v′/v` with `v = 1/u`, instead of asking whether `2f` is a logarithmic
derivative at all; the correct witness is `w = z`, not `1/z`.

Replaced with a residue-based test (poles simple, residues integral, witness
constructed **and verified**), self-checked in both directions before use. The
conclusion was unchanged — but the evidence as first printed did not support it,
and a printed line that contradicts its own conclusion must not be left standing.
(`S17-03`)

## 7. Uncommitted files

`sessions/2026-09-17/CT-S17-TRACEFREE-NORM/`: `PREREG.md`, `tracefree.py`,
`emit_claims.py`, `claims.jsonl` (8), `REPORT.md`, `outputs/tracefree.out.txt`,
`outputs/emit_claims.out.txt`.
