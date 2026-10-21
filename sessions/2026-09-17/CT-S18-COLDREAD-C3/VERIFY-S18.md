# VERIFY-S18 — adopting `CT-S18-COLDREAD-C3` claim by claim

The cold read returned **ERROR** on C3. Its findings are adopted or rejected
**individually**, per the standing rule that a correct finding does not certify
the reasoning around it — and, here, that a wrong verdict does not discredit the
findings underneath it. Two of its three tasks are adopted in full, and one of
those is the more valuable result of the run.

Adjudication script: `../CT-S17-TRACEFREE-NORM/adjudicate_s18.py`,
output `outputs/adjudicate.out.txt`,
sha256 `80303623301ce1cb3f404ee48ff13a05bc06bb134a589266163704c8439d6e8c`.

---

## Task 1 — the typo. **ADOPTED IN FULL. This row is now `cold`.**

The reader, working only from the page images and without sight of
`TYPO-EVIDENCE.md`, independently:

* read `(p + ½(q−1)q)²` off p. 2655, with no `t`;
* derived the residual `−(q−1)(t−1)(4p + q²t + q² − qt − q)/4` — **the same
  factorisation, term for term**, that CT-S16 obtained;
* showed the corrected square makes `det A(1) + θ₁²/4` vanish identically;
* ran its own bogus-variant control (`U = t + 1`) and confirmed rejection.

This is a genuine independent reproduction: same reading, same residual, same
conclusion, different code. **The `C3 corrected b(z)` support row moves from
`self` to `cold`.** This was the load-bearing row — a correction to a published
formula — so this is the result the packet was commissioned for.

## Task 2 — hypotheses. **ADOPTED, except its final bullet.**

Independently corroborates parts of CT-S16: finite singularities only at `0, 1`
after the root-normalising change; indicial equation `ρ²` at each, hence
`θ₀ = θ₁ = 0`; nonzero finite limit `11/27` of the normal-form coefficient at
infinity, consistent with Katz invariant `1`; and a Riccati obstruction check
finding no rational solution, with a control that fired.

Its **last** bullet — "the open-chart requirement `q ∉ {0,1}` is not satisfied by
the direct `P,Q` comparison in Task 3" — is **rejected**, because it inherits
Task 3's error, and because it misstates even that: Task 3 found a `P` mismatch,
not a violation of `q ∉ {0,1}`. The located `q` is not in `{0,1}`, which the
adjudication re-confirms.

## Task 3 — the chart. **COMPUTATION ADOPTED; INFERENCE REJECTED.**

The reader computed

```
    P_U0 = (z² − 2qz + q) / (z(z−q)(z−1)) ,    P_U0 − P_C = −1/(z−q) .
```

**That computation is correct.** It is also not a computation of the same object
CT-S17 compared. The reason is visible in the code: the cold read forms

```
    Pfam = −n21′/n21        (n21 ∝ c(z))
```

whereas CT-S17 forms `P = D′/D − b′/b`, i.e. `−n12′/n12`, with `n12 ∝ b(z)`.

Part A of the adjudication derives both from the system **by elimination, with
no formula assumed**, and obtains

```
    route 1  (ODE for y₁):  P = −tr N − n12′/n12
    route 2  (ODE for y₂):  P = −tr N − n21′/n21
```

These are the scalar equations satisfied by the **two different components** of
the same solution vector. They are *both* correct reductions of *one* system, and
they differ by `d/dz log(c/b)`. Neither is "the" scalar equation of the
connection; a rank-2 system has two of them.

So the question "is System C this system?" cannot be settled by picking a
component arbitrarily. Part B settles it at the located point:

| | `P − P_C` | `Q − Q_C` |
|---|---|---|
| route 1 (`b`) | **0** | **0** |
| route 2 (`c`) | `−c′/c = −1/(z−q)` ≠ 0 | — |

and Part C supplies the **control that decides it without reference to either
prior session**: solve the *system* at an ordinary point and ask which scalar ODE
its `y₁` component actually satisfies. At dps 60, over two independent seeds:

```
    |route-1 residual| = 4.8e-61 , 6.9e-62        |route-2 residual| = 9.0e+00 , 4.0e+00
```

The control fires on both seeds. System C is route 1, exactly.

There is also a structural reason this is the right route, and it is the
paper's own: vdPS define `q` as **the unique zero of `c(z)`**, and the route-2
scalar equation has an apparent singularity exactly at `z = q`. That is the
standard Painlevé presentation, in which `q` *is* the apparent singularity of the
scalar equation. System C has no third finite singular point, so it cannot be
route 2 for any point of the chart. At the located point `b` is constant
(`db/dz = 0`, re-confirmed), so route 1 has no finite apparent singularity
either — which is precisely why it can be System C.

## Task 4 — the **ERROR** verdict. **REJECTED**, as resting entirely on Task 3.

The verdict's own wording makes the dependency explicit: *"In the printed `U_0`
chart, direct scalar re-substitution gives `P_U0 − P_C = −1/(z−q)`"*. With the
component choice corrected, its premise is gone.

---

## Two method defects in the cold read, recorded

1. **A control that could not fail.** The reader's `P` control was
   `assert simplify(Pfam - Pfam) == 0`. That is identically zero for any
   `Pfam` whatsoever. It certifies nothing, and it sits directly beneath the
   assertion that drove the ERROR verdict. This is the same defect family the P0
   amendments were written for — *a step that cannot fail cannot be trusted to
   report failure* — and it recurred in a session explicitly instructed to make
   every control an assertion that can fail.
2. **A test insensitive to its own question.** The mismatch was evaluated only at
   a **generic** sample (`q = 2/3, p = 1/5, t = 7/11`), never at the located
   point. Since the route-2 mismatch is `−1/(z−q)`, which has no zero in `z`, no
   choice of point could ever have made route 2 match. The test could only ever
   have returned "mismatch", whatever the truth was.

Neither defect touches Task 1, which was independently derived and controlled.

---

## Effect on the deposit

| Support row | Before | After |
|---|---|---|
| `C3 corrected b(z)` | `self` | **`cold`** — independently reproduced |
| `C3 moduli-space membership` | `self` | **`self`, unchanged** |

The membership row **does not** move. A challenge that was raised and then
resolved is not an independent confirmation, and the resolution was performed by
me, adjudicating a session of my own. The honest position is that this row has
now been *attacked and survived*, which is worth recording but is weaker than a
clean cold read.

**Recommendation to the operator:** the membership row is still the notice's one
substantive `self` claim. If it is to be cleared before deposit, a second cold
read should be commissioned with the component question **named explicitly** —
"a rank-2 system has two scalar reductions; identify which one System C is, and
justify the choice" — since the first reader had no way to know that choice was
the crux. Alternatively the notice can deposit as it stands, with the row openly
marked `self`, which is what it already says.
