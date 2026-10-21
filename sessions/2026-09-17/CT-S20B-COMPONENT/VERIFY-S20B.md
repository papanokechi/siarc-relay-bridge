# VERIFY-S20B — adjudication of CT-S20B-COMPONENT

*Operator review #17 commissioned an isolated cold check of the adjudication
that overruled CT-S18. This is the adjudication of its return, task by task,
per the P0 rule.*

**Verdict returned: CORRECT.**

## What CT-S20B was and was not independent of

| Independent of | Not independent of |
|---|---|
| CT-S16, CT-S17, CT-S18, CT-S19 — none were in its packet, and it was told not to read them | `inputs.md`, which **I** wrote: the entries of `A(z)`, the convention `N = -A/D`, the point of §3, and `P_C, Q_C` |
| `adjudicate_s18.py`, `adjudicate_s19.py` and every claim file | the *choice* of which point to test — it was given one, and did not locate its own |
| CT-S18's ERROR verdict and CT-S19's CORRECT verdict, both withheld | |

This is the right shape for the contested question. What CT-S18 got wrong was
**which scalar reduction to compare**, not which point to compare at. CT-S20B
was handed the point and asked to derive the routes itself, so it tested
exactly the disputed step and nothing else. It is **not** a second independent
location of a point of `U₀` — CT-S19 already is that.

## Task-by-task disposition

### Task 1 — the route difference. **ADOPTED.**

Derived by elimination from a generic `Y' = N Y`, assuming no formula:

    P_b = -(n11+n22) - n12'/n12      P_c = -(n11+n22) - n21'/n21
    P_b - P_c = d/dz log(n21/n12)

and under §1's common denominator, `= d/dz log(c/b)`, exact.

This reproduces `S17-09` from scratch and **adds two things it lacked**:

1. **Orientation.** It is b-route *minus* c-route that equals `+d/dz log(c/b)`.
   `S17-09` stated the magnitude and left the sign to be rederived. Amended —
   see below.
2. **A proviso.** Identifying `n21/n12` with `c/b` uses the fact that §1
   divides *both* off-diagonal entries by the same `D`. The route difference
   itself, `d/dz log(n21/n12)`, is convention-free. Neither `S17-09` nor
   `VERIFY-S18.md` said so.

### Task 2 — the comparison at the given point. **ADOPTED.**

| difference | exact | numeric, dps 40 |
|---|---|---|
| `P_b - P_C` | 0 | 2.0e-177 |
| `Q_b - Q_C` | 0 | 2.5e-175 |
| `P_c - P_C` | `-1/(z-q)` | 1.45 |
| `Q_c - Q_C` | nonzero | 8.1 |

Independently confirms `S17-10`. The exact test was `cancel(·, z,
extension=True)` over `Q(i,√3,√11)` — a different mechanism from
`adjudicate_s18.py`'s, and one that never compares radicals with `==`.

**This is the row that closes the gate.** The c-route residual came back as
exactly `-1/(z-q)`, the simple zero of `c(z) = -(z-q)/(q-1)` at `q` — the value
the gauge relation predicts, arrived at by a reader who had not been told to
expect it. It is also why CT-S18's test could never have fired: `-1/(z-q)` has
no zero in `z`, so a comparison against the c-route returns "mismatch" at every
sample point, at every parameter value, for ever.

### Task 2b — `thi` against System C at infinity. **ADOPTED, with its own caveat.**

Consistent. On the branch with rate `+t/2` the eigenvector is `e1 + O(1/z)`, so
the first component carries exponent `N11_1 = thi/2` with **no** shift for any
`thi`; System C demands `-1 - √3/18`, forcing `thi = -2 - √3/9`, the printed
value, residual 0 at dps 40. The subdominant branch was then *predicted* from
`ord_∞(N12) = 2` and matched exactly.

Caveat, which the reader itself raised: since task 2 already gives `P_b ≡ P_C`
and `Q_b ≡ Q_C` identically, agreement of every local datum **follows**. Task 2b
is corroboration by a second route, not an independent constraint. Recorded at
that strength and no higher.

### Task 3 — the verdict. **ADOPTED.** CORRECT.

## The two discarded attempts are method findings, not claims

Per the operator's ruling, these are adopted as findings about method and **not**
entered as claims about the mathematics.

1. Keeping `thi` symbolic inside the *scalar* reduction and reading its heads at
   `z = ∞`. Unsound: `deg_z b` drops from 1 to 0 at exactly the printed `thi`, so
   the head coefficients are discontinuous precisely at the point of interest.
2. Treating `μ(+) - μ(-)` as gauge-invariant between the system and a scalar
   reduction. False here: the two branches carry different powers of `z`, `0`
   and `-2`, so the difference is not invariant.

Attempt 2 **returned "inconsistent"** and would have reported `thi = √3/9` — wrong
by exactly the shift, 2. It was caught by an arithmetic control: the two scalar
exponents must sum to `-P1`. They summed to `-1` against System C's `-2`.

This belongs to the family already in the record under *"a step that cannot fail
cannot be trusted to report failure"*, but it is the **converse** instance and
the first of its kind here: not a control that could not fire, but a control that
**did** fire, on a real defect, in a check that would otherwise have returned a
confident wrong answer. That is why this return is worth more than its verdict.

## Amendment to `S17-09`

`S17-09` is amended in place to carry the orientation and the proviso, per the
operator's instruction that *"the claim text should carry the sign convention so
a future reader doesn't rederive it backwards."* The prior text is preserved in
`CT-S17-TRACEFREE-NORM/claims.jsonl.bak-r20` and quoted in `AUDIT.md` §R20. The
label is unchanged at PROVEN; the mathematics is unchanged; only the sign
convention and the denominator proviso are added.

## Effect on the record

`C3 moduli-space membership` moves to **`cold`** on an independent resolution of
the contested step. The support table keeps the full history — CT-S18 ERROR,
overruled, CT-S19, CT-S20B — so that a reader sees the gate was contested and
how it was settled.

Nothing here bears on `R1-57`, which remains the sole gap and carries no weight.
