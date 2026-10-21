# DERIVATION.md — closed form for the leading amplitude K

Session: `CT-S3B-RINF` (P3 Part B step 1).
Label of the end result: **STRUCTURAL** (symbolic derivation with one asymptotic
step used without an explicit error-term proof; see Gap G1 below).
The *numerical confirmation* of the end result is **VERIFIED** (Part B step 2).

---

## 0. Setting and notation

Let `b ∈ ℂ[n]` have degree `d ≥ 1`, leading coefficient `β_d ≠ 0`, and write

    b(n) = Σ_{k=0}^{d} β_k n^k = β_d ∏_{i=1}^{d} (n − r_i)

with roots `r_1,…,r_d` (with multiplicity). Define the recurrence

    Q_n = b(n) Q_{n−1} + Q_{n−2},    Q_{−1} = 0,  Q_0 = 1.

Standing assumptions for this derivation:

* **(A1)** `b(k) ≠ 0` for every integer `k ≥ 1`.
* **(A2)** No root `r_i` is a positive integer — equivalently `Γ(1 − r_i)` is
  finite. (`Γ` has poles at `0, −1, −2, …`, so `Γ(1 − r_i)` is singular exactly
  when `r_i ∈ {1, 2, 3, …}`.) This is enforced by `root_precheck` in the scripts;
  it correctly halted two points of the P2 vacuity grid where `b(1) = 0`.
* **(A3)** `r_∞ := lim_{n→∞} Q_n / ∏_{k=1}^{n} b(k)` exists and is **nonzero**.

The claim to be derived is

    Q_n / Γ(dn+1)  =  K · (β_d / d^d)^n · n^s · (1 + O(1/n))

with

    s = β_{d−1}/β_d + (d−1)/2                                            (S)
    K = r_∞ · (2π)^((d−1)/2) · d^(−1/2) / ∏_{i=1}^{d} Γ(1 − r_i)         (K)

---

## 1. Step 1 — reduce `Q_n` to a product

By definition of `r_n := Q_n / ∏_{k=1}^{n} b(k)` we have exactly

    Q_n = r_n · ∏_{k=1}^{n} b(k),

and by (A3), `r_n → r_∞ ≠ 0`. Hence

    Q_n = r_∞ · ∏_{k=1}^{n} b(k) · (1 + o(1)).                            (1)

This step is exact; the only input is (A3). *(Complete.)*

**Remark (rate).** The recurrence for `r_n` is
`r_n = r_{n−1} + r_{n−2} / (b(n−1) b(n))`, obtained by dividing the `Q`
recurrence by `∏_{k≤n} b(k)`, with `r_0 = r_1 = 1` (from `Q_{−1} = 0`).
Since `b(n−1)b(n) ~ β_d² n^{2d}`, the increments are `O(n^{−2d})` and therefore

    r_∞ − r_n = O(n^{−(2d−1)}).                                          (1r)

This is the reason the tail converges only *polynomially*, which is the source
of finding **S3B-F1** (see PREREG.md §1): the prompt's `10^−3000` tail bound at
`d = 2` would require `N ≈ 10^999.5`.

---

## 2. Step 2 — the product of `b(k)` in terms of Gamma functions

Using the factorisation `b(k) = β_d ∏_i (k − r_i)`,

    ∏_{k=1}^{n} b(k) = β_d^n ∏_{i=1}^{d} ∏_{k=1}^{n} (k − r_i).

For each root, telescoping the functional equation `Γ(x+1) = x Γ(x)`:

    ∏_{k=1}^{n} (k − r_i) = (1−r_i)(2−r_i)⋯(n−r_i) = Γ(n + 1 − r_i) / Γ(1 − r_i),

which is finite and nonzero by (A2). Therefore

    ∏_{k=1}^{n} b(k) = β_d^n ∏_{i=1}^{d} Γ(n + 1 − r_i) / Γ(1 − r_i).     (2)

This step is exact and elementary. *(Complete.)*

Combining (1) and (2):

    Q_n = r_∞ · β_d^n · [ ∏_i Γ(n+1−r_i) / Γ(1−r_i) ] · (1 + o(1)).       (3)

---

## 3. Step 3 — Gamma ratio asymptotics

The standard ratio asymptotic (a special case of the Gamma-ratio expansion,
equivalently Stirling applied twice) is

    Γ(n + 1 − r) / Γ(n + 1) = n^{−r} (1 + O(1/n)).                        (4)

Applying (4) to each root and multiplying the `d` relations:

    ∏_{i=1}^{d} Γ(n+1−r_i) = Γ(n+1)^d · n^{−Σ_i r_i} · (1 + O(1/n)).      (5)

By Vieta applied to `b(n) = β_d ∏(n − r_i)`, the coefficient of `n^{d−1}` gives

    Σ_{i=1}^{d} r_i = − β_{d−1} / β_d.                                    (6)

So the exponent in (5) is `−Σ r_i = + β_{d−1}/β_d`. Substituting (5)–(6) into (3):

    Q_n = r_∞ · β_d^n · Γ(n+1)^d · n^{β_{d−1}/β_d} / ∏_i Γ(1−r_i)
          · (1 + O(1/n)).                                                 (7)

> **Gap G1.** Equation (4) is quoted as a standard asymptotic rather than
> proved here, and the `o(1)` of (1) is merged into an `O(1/n)` in (7). Merging
> is legitimate only if `r_∞ − r_n = O(1/n)`, which (1r) supplies for `d ≥ 1`
> (indeed `O(n^{−(2d−1)})`, far stronger). The remaining unproved ingredient is
> therefore only the classical (4). This is why the result is labelled
> **STRUCTURAL** and not PROVEN.

---

## 4. Step 4 — Gauss multiplication for `Γ(dn+1)`

The Gauss multiplication formula is

    Γ(dz) = (2π)^((1−d)/2) d^(dz − 1/2) ∏_{j=0}^{d−1} Γ(z + j/d).

We need `Γ(dn+1) = dn · Γ(dn)`. Put `z = n`:

    Γ(dn) = (2π)^((1−d)/2) d^(dn − 1/2) ∏_{j=0}^{d−1} Γ(n + j/d).

Now compare `∏_{j=0}^{d−1} Γ(n + j/d)` with `Γ(n+1)^d = Γ(n)^d n^d`. Using (4)
in the form `Γ(n + a)/Γ(n) = n^{a}(1 + O(1/n))` for each `j`:

    ∏_{j=0}^{d−1} Γ(n + j/d) = Γ(n)^d · n^{Σ_{j=0}^{d−1} j/d} (1 + O(1/n))
                             = Γ(n)^d · n^{(d−1)/2} (1 + O(1/n)),

since `Σ_{j=0}^{d−1} j/d = (d−1)/2`. Hence

    Γ(dn) = (2π)^((1−d)/2) d^(dn−1/2) Γ(n)^d n^{(d−1)/2} (1 + O(1/n)),

and multiplying by `dn` and using `Γ(n+1)^d = n^d Γ(n)^d`:

    Γ(dn+1) = (2π)^((1−d)/2) d^(dn+1/2) Γ(n+1)^d n^{−(d−1)/2} (1 + O(1/n)).  (8)

*(Complete, modulo the same classical (4) already recorded as Gap G1.)*

---

## 5. Step 5 — divide and collect

Divide (7) by (8):

    Q_n / Γ(dn+1)
      = r_∞ / ∏_i Γ(1−r_i)
        · β_d^n · Γ(n+1)^d · n^{β_{d−1}/β_d}
        · (2π)^((d−1)/2) · d^(−dn−1/2) · Γ(n+1)^{−d} · n^{(d−1)/2}
        · (1 + O(1/n)).

The two factors `Γ(n+1)^{±d}` cancel exactly — this cancellation is the whole
point of normalising by `Γ(dn+1)` rather than by `n!` — leaving

    Q_n / Γ(dn+1) = [ r_∞ (2π)^((d−1)/2) d^(−1/2) / ∏_i Γ(1−r_i) ]
                    · (β_d / d^d)^n
                    · n^{ β_{d−1}/β_d + (d−1)/2 }
                    · (1 + O(1/n)),

which is exactly (K) together with (S). ∎ (modulo Gap G1)

---

## 6. Consistency checks performed

1. **The exponent `s` is reproduced independently.** (S) here falls out of
   Vieta (6) plus the `(d−1)/2` from Gauss multiplication. In session
   `CT-S2-RHO-D4` the same `s` was measured numerically for eight `d = 4`
   representatives with worst residual `7.12e−16`. The two routes share no code.
2. **`|β_d| / d^d` is the growth base**, so `lim |Q_n/(dn)!|^{1/n} = |β_d|/d^d`
   and the Borel radius in `w` is `d^d/|β_d|` — this is the input to P4 (i).
3. **`K` is numerically confirmed** (Part B step 2) to 109.66–114.69 digits over
   eight cases spanning `d = 2, 3, 4`, including negative `K` and sign-changing
   `b`. The pre-registered vacuity control — recomputing `K` with the
   `∏_i Γ(1−r_i)` factor omitted — collapses agreement to `≤ 0.75` digits,
   confirming the Gamma product is doing real work and the test is not vacuous.
4. **Degenerate case `d = 1`**: (K) reduces to `K = r_∞ / Γ(1−r_1)` with `s = β_0/β_1`,
   and `(2π)^0 · 1^{−1/2} = 1`, so the formula is consistent at `d = 1`.

## 7. What this does NOT establish

* It does not determine the **analytic type** of the Borel singularity at `ξ₀`.
  (K) is a coefficient-asymptotics statement only.
* It does not identify `K` with any Stokes constant. Per the P1 finding
  (`CT-S3A-ZETA-AUDIT`, classification **(b)**), the singularity pinned by
  `ζ* = 4/√3` is the **action difference** `|c₊ − c₋| = 2ξ₀`, *not* the
  radius-of-convergence singularity at `ξ₀ = 2/√3`. Any germ coefficient
  extracted from (K) must be stated against the `ξ₀` singularity and must **not**
  be called `S_{ζ*}`.
* It gives no information about `β_0 … β_{d−2}`: (K) depends on them only
  through `r_∞` and `∏Γ(1−r_i)`, while `s` depends on `β_d, β_{d−1}` alone.
  This is the structural reason behind the reported vacuity of exponent-only
  tests.
