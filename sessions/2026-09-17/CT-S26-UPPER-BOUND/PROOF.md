# PROOF — the upper bound on `r_∞`

**Written before `scripts/upper_bound.py` was run.** The numerics that follow in
this session check this proof and its transcription; they are not its evidence.

Notation is that of `CT-S1-THEOREM/theorem.tex` §"Setup", reproduced here so
this file stands alone.

---

## Setup

Let `b` be a polynomial with real coefficients, `deg b = d >= 1`. Define

```
Q_{-1} = 0,   Q_0 = 1,   Q_n = b(n) Q_{n-1} + Q_{n-2}        (n >= 1)     (1)
B_n   = prod_{k=1}^{n} b(k),        r_n = Q_n / B_n          (n >= 0)     (2)
```

with `B_0 = 1` (empty product). **(A1)** is `deg b = d >= 1` and `b(n) != 0`
for every integer `n >= 1`. Dividing (1) by `B_n = b(n) B_{n-1} = b(n)b(n-1)B_{n-2}`
gives, exactly as at `theorem.tex` eq. `(rnrec)`,

```
r_n = r_{n-1} + r_{n-2} / ( b(n-1) b(n) )        (n >= 2),     r_0 = r_1 = 1. (3)
```

Throughout write

```
eps_n := 1 / ( b(n-1) b(n) )     (n >= 2).                                  (4)
```

---

## Lemma 1 (convergence of the defining sum)

*If `deg b = d >= 1` and `b(n) != 0` for all `n >= 1`, then
`Σ_{k>=1} 1/|b(k) b(k+1)| < ∞`.*

**Proof.** This is `theorem.tex` eq. `(eps)` verbatim, with the index shifted by
one. Since `deg b = d` with leading coefficient `β_d != 0`, there are `c > 0`
and `n_0` with `|b(n)| >= c n^d` for `n >= n_0`; hence for `k >= n_0`

```
1/|b(k) b(k+1)|  <=  c^{-2} k^{-d} (k+1)^{-d}  <=  c^{-2} k^{-2d} ,
```

and `2d >= 2 > 1`, so the tail converges by comparison with `Σ k^{-2d}`. The
finitely many terms `k < n_0` are finite because `b(k) != 0` there. ∎

*Remark.* Lemma 1 is exactly the summability already used by `prop:exists`
(`S1-01`); it is restated rather than assumed so that this file is closed.

---

## Proposition U (the upper bound)

*Let `b` satisfy (A1) and suppose in addition `b(n) > 0` for every integer
`n >= 1`. Then for every `n >= 1`*

```
r_n  <=  exp( Σ_{k=1}^{n-1} 1/( b(k) b(k+1) ) )                          (U-finite)
```

*and consequently, with `L := exp( Σ_{k>=1} 1/(b(k) b(k+1)) ) < ∞`,*

```
1  <=  r_∞  <=  L .                                                      (U-limit)
```

**Proof.**

*Step 1 — monotonicity and positivity.* This is `prop:positive` (`S1-02`,
PROVEN) and is used as a black box: under `b(n) > 0` for `n >= 1`, the sequence
`(r_n)_{n>=0}` satisfies `r_n > 0` for all `n >= 0`, and `(r_n)_{n>=1}` is
**strictly increasing** with `r_1 = 1`. In particular

```
0 < r_{n-2} <= r_{n-1}        for every n >= 3,                            (5)
```

and for `n = 2`, `r_0 = r_1 = 1` gives `r_0 <= r_1`, so (5) holds for all
`n >= 2`. **complete.**

*Step 2 — a multiplicative step bound.* Fix `n >= 2`. All of `b(n-1)`, `b(n)`
are positive, so `eps_n > 0`. Substituting (5) into (3),

```
r_n = r_{n-1} + eps_n r_{n-2}  <=  r_{n-1} + eps_n r_{n-1} = (1 + eps_n) r_{n-1}.
```

Since `1 + x <= e^x` for all real `x`,

```
r_n  <=  r_{n-1} exp(eps_n)        (n >= 2).                               (6)
```

**complete.**

*Step 3 — telescoping the step bound.* Iterating (6) from `n` down to `1`, and
using `r_1 = 1`,

```
r_n  <=  r_1 * prod_{m=2}^{n} exp(eps_m)  =  exp( Σ_{m=2}^{n} eps_m ) .
```

Re-indexing by `k = m - 1`, `eps_m = 1/(b(m-1)b(m)) = 1/(b(k)b(k+1))`, so

```
Σ_{m=2}^{n} eps_m = Σ_{k=1}^{n-1} 1/( b(k) b(k+1) ),
```

which is `(U-finite)`. For `n = 1` the right-hand side is `exp(0) = 1 = r_1`,
so `(U-finite)` holds there too, with equality. **complete.**

*Step 4 — passage to the limit.* By Lemma 1 the series
`Σ_{k>=1} 1/(b(k)b(k+1))` converges (its terms are positive here, so it
converges to a finite `Σ >= 0`), whence `L = exp(Σ) < ∞`. Its partial sums
increase to `Σ`, so `exp(Σ_{k=1}^{n-1} ...) <= L` for every `n`, and
`(U-finite)` gives `r_n <= L` for every `n >= 1`. By `prop:exists` (`S1-01`)
the limit `r_∞ = lim r_n` exists; passing to the limit in a non-strict
inequality preserves it, so `r_∞ <= L`. The lower bound `r_∞ >= 1` is
`prop:positive` (`S1-02`). **complete.** ∎

---

## What Proposition U does and does not say

- **It is strict in the interior.** `(U-limit)` is never an equality for
  `d >= 1`: `r_2 = 1 + 1/(b(1)b(2)) > 1` already, and Step 2's inequality
  `1 + x < e^x` is strict for `x != 0`, so `r_∞ < L` whenever at least one
  `eps_n > 0`, which is always. Both inequalities in `1 <= r_∞ <= L` are
  therefore strict for every admissible `b`. This is **not** used anywhere and
  is recorded only to forestall the reading that `L` might be attained.
- **Positivity is a hypothesis of Proposition U, not of `prop:exists`.**
  `(U-finite)` is stated only for `b > 0` on `n >= 1`. Step 1 is where that is
  consumed: without it `(5)` fails, and with `r_{n-2}` of either sign the
  substitution in Step 2 is not available. Nothing here shows the conclusion is
  *false* without positivity; arm **V6** of `PREREG.md` looks for a
  counterexample, and reports "not established" if it finds none.
- **It does not depend on `rem:pincherle`.** No minimal-solution or
  Perron–Kreuser input is used at any step. This matters for the same reason the
  §1 ¶2 correction mattered: the outline's §2.0 undertakes that nothing in the
  paper rests on Birkhoff–Trjitzinsky, and the growth material must be able to
  say so without qualification.
- **It must not be written citing `S1-02` alone.** `S1-02` supplies Step 1 and
  the lower bound only. The upper bound is this proposition, and at drafting it
  carries **this** session's claim id.

## Cost at drafting

One proposition, four steps, roughly fifteen lines of LaTeX, placed immediately
after `prop:positive` in `theorem.tex` and hypothesised identically to it. The
two then combine into the single two-sided statement the outline's §1 ¶2
already asserts, so no change to §1 ¶2 is required.
