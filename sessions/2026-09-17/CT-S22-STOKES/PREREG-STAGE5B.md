# PREREG — CT-S22-STOKES, Stage 5B: corrected search space for `S_{ζ*}`

Written **after** the Stage-5A search of `PREREG-STAGE5.md` returned a **VOID**
result, and **before** any Stage-5B number has been seen.

`PREREG-STAGE5.md` is **not edited**. Its §5 says a widened or altered space
requires a new, separately pre-registered search; this is that file.

---

## 0. Naming prohibition (unchanged, binding)

> **`K` is the amplitude at `ξ₀ = 2/√3`. `S_{ζ*}` is the Stokes constant at
> `ζ* = 2ξ₀ = 4/√3`.** Different objects, a factor of 2 apart in the action.
> Neither name may be used for the other, in code, output, or prose.

## 0.1 The normalisation caveat (unchanged, still not resolved)

`C` is read from the 2026-05-02 fire in **V_quad native normalisation**,
`S_{ζ*} = 2πiC`, convention `leading B[Φ]=1`. The `V_quad → P-III(D6)`
normalisation map **remains OPEN**. Anything found here is a closed form *of
that number in that normalisation*, and may not be compared with the Stage-1–4
quantities of this session, which live in the vdPS sectorial basis of
`PREREG.md` §2.1–§2.2.

---

## 1. Why Stage 5A is VOID rather than NEGATIVE

The Stage-5A space was

```
    v = [ log C, log 2, log 3, log π, log Γ(1/3), log Γ(1/6), 1 ].
```

PSLQ returned, for **`C` and for all three decoys alike**, the identical
relation

```
    -2·log 2 + 3·log 3 - 3·log π + 12·log Γ(1/3) - 6·log Γ(1/6)  =  0,
```

whose coefficient on `log C` is **zero**.

That relation is a classical identity, not a discovery:

```
    Legendre duplication at z = 1/6 :  Γ(1/6) Γ(2/3) = 2^{2/3} √π Γ(1/3)
    reflection at 1/3            :  Γ(1/3) Γ(2/3) = π / sin(π/3) = 2π/√3
    hence                            Γ(1/6) = 2^{2/3} √3 Γ(1/3)² / (2 √π)
    i.e.        6 log Γ(1/6) = -2 log 2 + 3 log 3 - 3 log π + 12 log Γ(1/3).
```

Label: **PROVEN** (two classical identities), and **VERIFIED** numerically —
`|Γ(1/6) − 2^{2/3}√3 Γ(1/3)²/(2√π)| = 6.2e-61` at dps 60, and the relation's
residual is `1.24e-60`.

**Consequence.** `Γ(1/6)` is not independent of `{2, 3, π, Γ(1/3)}`
multiplicatively. The Stage-5A basis was **linearly degenerate**, so PSLQ's
smallest relation was a relation *among the basis constants themselves*. The
search therefore **never tested `C` at all**. Its "NOT FOUND" line excludes
nothing and is withdrawn.

### 1.1 Why the Stage-5A vacuity pre-check did not catch it

`PREREG-STAGE5.md` §6 checked that the space does **not** fit arbitrary numbers
(3 decoys rejected) and **does** fit a known one (control accepted). Both
conditions were met — **for the wrong reason**. The decoys were rejected because
PSLQ handed back a `C`-free relation, not because the space discriminates. A
check that passes for the wrong reason is the recurring defect of this whole
run, and this is another instance of it.

The pre-check tested *the space against numbers*. It did not test *the space
against itself*. §4 below adds the missing check.

---

## 2. The corrected search space, fixed now

`Γ(1/6)` is **removed as redundant** (not "added to"; the space is strictly
smaller). The space is the 6-vector

```
    v = [ log C, log 2, log 3, log π, log Γ(1/3), 1 ]
```

seeking integers `(m, a, b, c, d, f)`, `m ≠ 0`, with

```
    m·log C + a·log 2 + b·log 3 + c·log π + d·log Γ(1/3) + f = 0,
```

i.e. `C = ± 2^{a'} 3^{b'} π^{c'} Γ(1/3)^{d'} e^{f'}` with rational exponents of
denominator dividing `m`.

Because `Γ(1/6)` was expressible in the remaining generators, **no closed form
representable in the Stage-5A space is lost by this removal.** That is the
reason the correction is a removal and not a widening, and it is stated before
running.

### 2.1 Bounds — unchanged from Stage 5A, deliberately

- `|coeff| ≤ H = 10^6`;
- `|m| ≤ 12`, and `m ≠ 0`;
- working `dps = 120`, input `C` truncated to `D_trust = 100` digits;
- digit cost `cost = n_nonzero · log10(max|coeff|) ≤ 0.40 · D_trust = 40`.

Nothing is loosened. The only change is the removal of a redundant generator.

---

## 3. Acceptance criterion (all four required, unchanged)

1. PSLQ returns a relation within §2.1;
2. `cost ≤ 40`;
3. **stability**: the identical relation at input truncated to 90 and 80 digits;
4. **reconstruction**: independent evaluation at `dps = 150` reproduces `C` to
   `≥ 95` digits.

Label if all four hold: **VERIFIED**. **Not PROVEN** — a PSLQ hit is a
recognition, not a derivation. Fixed now; not raisable.

---

## 4. Pre-checks — BOTH must pass, and they run BEFORE the search

### 4.1 Degeneracy pre-check (NEW — the one Stage 5A lacked)

Run PSLQ on the basis **with `log C` removed**:

```
    [ log 2, log 3, log π, log Γ(1/3), 1 ]
```

at the identical bounds and precision.

**FIRES (Stage 5B void, halt) if any relation is returned within the bounds.**
A relation here means the constants are not independent, and any relation found
with `C` present could be that one in disguise.

This is the check that would have caught Stage 5A, and it is stated as a
*falsifier with a numeric bound*, not as an inspection.

### 4.2 Vacuity pre-check (carried from Stage 5A §6)

Decoys, identical pipeline and bounds:

- `C_d1 = C · (1 + 10^{-30})`
- `C_d2 = ` `8.1` followed by the digits of `π` after the decimal point
- `C_d3 = C + 1/7`

Positive control: `C_k = 4π²/(3Γ(1/3))`, which lies in the corrected space.

**Required outcome: 3 decoys rejected, 1 control accepted.** Any other outcome
halts Stage 5B.

**Additional condition, added because of the Stage-5A failure:** every
rejection must be recorded together with the returned relation, and a decoy
rejected because PSLQ returned a relation with `m = 0` **does not count as a
rejection** — it counts as a degeneracy and fires §4.1.

---

## 5. What a NEGATIVE result looks like, pre-registered

If no relation satisfies §3, the reported claim is exactly:

> **NOT FOUND.** No multiplicative relation
> `C = ± 2^a 3^b π^c Γ(1/3)^d e^f` exists with all coefficients bounded by
> `10^6`, `1 ≤ |m| ≤ 12`, and digit cost `≤ 40`, against `C` known to 100
> decimal digits. Search space: the 6-vector of §2, whose constants were first
> shown independent by §4.1. This **excludes that space**; it is **not**
> evidence that `C` has no closed form, and says nothing about spaces
> containing other gamma values, other algebraic irrationalities,
> polylogarithms, or `ζ(3)`.

Label: **VERIFIED** — a verified statement about a search, not about `C`.

The negative result must report the search space, the bounds, `D_trust`, and
the smallest digit cost achieved by any rejected candidate.

A negative result is reported with the same prominence as a positive one.
Any further widening requires another separately pre-registered file.

---

## 6. Halt conditions

`P0`'s four, plus:

- §4.1 fires (the constants are dependent) → **void, halt, report**;
- §4.2 fires (a decoy accepted, or the control rejected) → **void, halt**;
- a relation satisfies §3.1–§3.3 but fails reconstruction §3.4 → **halt and
  report the discrepancy**, do not retune;
- the two stored copies of `C` disagree within `D_trust` → **halt**; `C` is
  not re-derived in this session;
- runtime beyond 3× budget.

## 7. Prohibitions

No commits, pushes, tags, PRs, deposits, uploads, submissions or emails. The
2026-05-02 and 2026-05-13 fire folders are read-only; `C` is read from the file,
never retyped. Every script reads back what it wrote. Symbolic equality by
simplify-to-zero **and** a numeric check.
