# Cold packet B — a claimed contradiction in a Painlevé V parameter assignment

You are given a chain of reasoning. Decide whether it is correct. Nothing in
this packet is asserted to be true except the two quoted source facts in §1,
which you should verify against the supplied page image.

## 1. Source facts (verify these)

From **Jimbo, "Monodromy Problem and the Boundary Condition for Some Painlevé
Equations", Publ. RIMS, page 1152**. A rendered image of that page is at
`sessions/2026-09-17/CT-S9-PVPARAMS/outputs/jimbo_page16-16.png`. You may open
**that image only**.

Quoted:

* The Lax system (3.1) is
  `dY/dx = ( A_0/x + A_t/(x-t) + diag(1,0) ) Y`, with singular points
  `0`, `t`, `infinity`.
* "the eigenvalues of `A_nu(t)` are `+/- theta_nu / 2`" for `nu = 0, t`.
* The Painlevé V parameter dictionary:

  ```
      alpha =  (1/8) (theta_0 - theta_t + theta_inf)^2
      beta  = -(1/8) (theta_0 - theta_t - theta_inf)^2
      gamma =  1 - theta_0 - theta_t
      delta = -1/2
  ```

Confirm both quotations are accurate. Also report whether the page states any
standing assumption on `theta_0` and `theta_t`, and if so, quote it.

## 2. The operator under study ("System C")

```
    a(x) y'' + a'(x) y' + c(x) y = 0 ,      a = 3x^2 + x + 1 ,   c = -x^2 .
```

## 3. Claimed chain

**(C1)** In standard form `y'' + p y' + q y = 0` with `p = a'/a`, `q = c/a`, the
normal-form potential `R = p^2/4 + p'/2 - q` satisfies

```
    R = (12x^4 + 4x^3 + 4x^2 + 11) / ( 4 (3x^2 + x + 1)^2 ).
```

**(C2)** At each root `s` of `a`, `lim (x-s)^2 R = -1/4`, so the exponent
difference there is `sqrt(1 + 4*(-1/4)) = 0`. Hence `theta_0 = theta_t = 0`.

**(C3)** `R -> 1/3` as `x -> infinity`, so the two WKB exponentials at infinity
are `exp(+/- x/sqrt(3))` and their exponent difference is `(2/sqrt(3)) x`.

**(C4)** Substituting `theta_0 = theta_t = 0` into the dictionary gives
`alpha = theta_inf^2/8`, `beta = -theta_inf^2/8` (so `beta = -alpha`
identically), `gamma = 1`, `delta = -1/2`.

**(C5)** A published source assigns this operator the parameter tuple
`(alpha, beta, gamma, delta) = (1/6, 0, 0, -1/2)`. By (C4) this is
contradictory: `beta = 0` forces `theta_inf = 0` hence `alpha = 0`, which
contradicts `alpha = 1/6`; and separately `gamma = 1` contradicts `gamma = 0`.

**(C6)** The contradiction is not a matter of convention. Under the rescaling
`z -> c z`, the Painlevé V parameters transform as
`(alpha, beta, gamma, delta) -> (alpha, beta, c*gamma, c^2*delta)`. Holding
`delta = -1/2` therefore forces `c^2 = 1`, i.e. `c = +/-1`, so `gamma` is fixed
up to sign. `gamma = 1` cannot be rescaled to `gamma = 0`.

**(C7)** Jimbo normalises the irregular part at infinity so that its exponent
difference is exactly `z`. Matching System C via an affine map `z = k(x - s0)`
therefore forces `k = 2/sqrt(3)`. Since the two finite singular points of
System C are the roots `s_+`, `s_-` of `a`, the Painlevé V time is then
**determined**:

```
    t = k (s_mp - s_pm) = -/+ 2i sqrt(33) / 9 ,     |t| = 2 sqrt(33)/9 .
```

So System C is a single fibre: it has no free deformation parameter.

## 4. What you are asked to do

1. Verify the two quotations in §1 against the page image, and report any
   standing assumption you find there.
2. Recompute (C1), (C2), (C3) from scratch by exact symbolic computation
   (SymPy). Include your script and output.
3. Check (C4) and (C5) arithmetically.
4. **Check (C6) independently.** Derive the scaling behaviour of the Painlevé V
   parameters yourself from the Painlevé V equation

   ```
     w'' = (1/(2w) + 1/(w-1)) (w')^2 - w'/z
           + (w-1)^2 (alpha*w + beta/w) / z^2 + gamma*w/z + delta*w(w+1)/(w-1)
   ```

   under `z -> c z`. Do not take the stated transformation law on trust: it is
   the single load-bearing step of the argument. State whether it is correct.
5. Check (C7). Is `k` genuinely forced? Is the identification of System C's two
   finite singular points with Jimbo's `0` and `t` legitimate, or is it an
   assumption? Say which.
6. Final verdict on the claimed contradiction: SOUND / SOUND WITH CAVEAT /
   ERROR, with reasons. Also state separately whether (C7)'s conclusion
   ("a single fibre, no free deformation parameter") follows.

## Rules

- Work only inside `sessions/2026-09-17/CT-S12-COLDREAD4/` (create it).
- Do **not** read any file under `sessions/2026-09-17/` other than the single
  page image named in §1. In particular do not open `CT-R1-AUDIT/`,
  `CT-S9-PVPARAMS/REPORT.md`, or any `AUDIT.md`, `VERIFY-*.md`, or
  `claims.jsonl`. This is a cold read.
- Do not reconstruct any published result from memory. If you need a source you
  cannot obtain, say what is missing and stop.
- Do not commit, push, tag, or open a PR. Leave everything uncommitted.
- Write `REPORT.md` with your verdict, and `claims.jsonl` with one line per
  claim using labels PROVEN / VERIFIED / STRUCTURAL / CONJECTURED.
