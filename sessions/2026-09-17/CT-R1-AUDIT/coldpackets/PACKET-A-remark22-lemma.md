# Cold packet A — a claimed lemma about apparent singularities

You are given a mathematical claim and its proof. Decide whether the proof is
correct. Nothing else in this packet is asserted to be true.

## Setting

Let `chi` and `c` be polynomials in `x` over the complex numbers. Consider the
second-order linear ODE

```
    chi(x) y'' + chi'(x) y' + c(x) y = 0
```

(note the exactness pattern: the coefficient of `y'` is the derivative of the
coefficient of `y''`). In standard form `y'' + p y' + q y = 0` this is

```
    p = chi'/chi ,        q = c/chi .
```

Let `s` be a **simple** root of `chi`, and assume `s` is a genuine singular
point of the equation.

## Claimed lemma

> For **any** simple root `s` of `chi`, and for **any** `c`, the point `s` is a
> regular singular point at which the indicial polynomial is `lambda^2`.
> Consequently the two local exponents are equal (both `0`), the second
> Frobenius solution contains a logarithm, and **`s` is never an apparent
> singularity**.

## Claimed proof

1. Since `s` is a simple root of `chi`, write `chi(x) = (x-s) h(x)` with
   `h(s) != 0`. Then `chi'(x) = h(x) + (x-s) h'(x)`, so

   ```
       (x-s) p(x) = (x-s) chi'/chi = chi'/h  ->  h(s)/h(s) = 1   as x -> s.
   ```

   Hence `p` has a simple pole at `s` with **residue exactly 1**.

2. `q = c/chi` has at most a **simple** pole at `s` (since `chi` has a simple
   root there and `c` is a polynomial). Therefore

   ```
       (x-s)^2 q(x)  ->  0    as x -> s.
   ```

3. By steps 1-2, `s` is a regular singular point, and the indicial equation is

   ```
       lambda(lambda-1) + p0*lambda + q0 = 0,   where  p0 = 1,  q0 = 0,
   ```

   i.e. `lambda(lambda-1) + lambda = lambda^2 = 0`. So both exponents are `0`.

4. At a regular singular point with a **repeated** exponent, the standard
   Frobenius theory gives a second solution of the form
   `y2 = y1*log(x-s) + (series)`, with the log coefficient nonzero. A point
   admitting a logarithmic local solution is not apparent.

5. Therefore no simple root of `chi` is ever an apparent singularity of this
   equation, **regardless of `c`**.

## What you are asked to do

1. Check each of steps 1-5. State for each: CORRECT, or ERROR (with the error).
2. Pay particular attention to step 4. Is "repeated exponent at a regular
   singular point" genuinely sufficient to force a logarithm, with **nonzero**
   coefficient? Either supply the standard justification or identify the gap.
3. Check the quantifier claim: is the lemma really independent of `c`? An
   earlier version of this lemma carried an extra hypothesis `c(s) != 0`.
   Decide whether dropping it is legitimate. Consider in particular whether
   `c(s) = 0` could make `s` a non-singular point, or otherwise invalidate the
   argument, and whether the lemma's own phrase "assume `s` is a genuine
   singular point" is doing hidden work.
4. Test the lemma on at least two concrete examples of your own choosing, by
   exact symbolic computation (SymPy). Include your script and its output.
5. Give a final verdict: SOUND / SOUND WITH CAVEAT / ERROR.

## Rules

- Work only inside `sessions/2026-09-17/CT-S11-COLDREAD3/` (create it).
- Do **not** read any other file under `sessions/2026-09-17/`. In particular do
  not open `CT-R1-AUDIT/`, `CT-S6-APPARENCY/`, or any `REPORT.md`, `AUDIT.md`,
  `VERIFY-*.md`, or `claims.jsonl`. This is a cold read; its value depends on
  your not seeing the derivation history.
- Do not commit, push, tag, or open a PR. Leave everything uncommitted.
- Write `REPORT.md` with your verdict, and `claims.jsonl` with one line per
  claim using labels PROVEN / VERIFIED / STRUCTURAL / CONJECTURED.
- If you find the packet ambiguous, say so rather than guessing.
