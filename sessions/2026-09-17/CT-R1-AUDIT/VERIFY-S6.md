# CT-R1-AUDIT R2 — independent spot-check of `CT-S6-APPARENCY`

Script: `verify_s6.py` · output: `verify_s6.out` / `verify_s6.log`

Nothing was imported from the CT-S6 session. Every object was rebuilt from the
companion paper's equation (6)–(7) and from CT-S5B's published normal form for
System B, then recomputed exactly in SymPy, and each step was also done by hand.

## 1. Confirmed

| CT-S6 claim | independent result | verdict |
|---|---|---|
| System C is exact, `b = a'` | `b − a' = 0` | **confirmed** |
| System C `s± = (−1 ± i√11)/6` have exponents `[0,0]` | indicial polynomial is exactly `λ²`; `p₀ = 1`, `q₀ = 0` | **confirmed** |
| `s±` are **NOT APPARENT** | normal-form residue `−1/4` ⇒ `λ(λ−1) = −1/4` ⇒ `λ = 1/2` **doubled**; a repeated exponent at a genuine regular singular point always forces a log | **confirmed** |
| System C `≅` inverted System B | both normal forms equal `(12x⁴+4x³+4x²+11) / (4(3x²+x+1)²)`, **identically** | **confirmed** |
| System C at `∞` is unramified Katz 1 | pole order 4 in `t = 1/x` ⇒ Katz `4/2 − 1 = 1`, integer ⇒ unramified | **confirmed** |

The companion's own claim that `s±` have exponents `{0,1}` with `θ₁ = θ₂ = 0`
is **refuted**: the exponents are `{0,0}`.

### By hand, for the record

At a simple root `s` of `a`, `p = a'/a` has residue exactly `1` and
`(x−s)²q → 0`, so the indicial polynomial is `λ(λ−1) + λ + 0 = λ²`.
For the normal form, with `a = 3x²+x+1` and `3s²+s+1 = 0`:
`a'(s)² = (6s+1)² = 36s² + 12s + 1 = −12(s+1) + 12s + 1 = −11`, while
`4N(s) = 12s⁴+4s³+4s²+11 = 11`. Hence the residue is `(11/4)/(−11) = −1/4`,
giving `(λ − 1/2)² = 0`. Both computations agree with the script exactly.

## 2. Strengthening: Remark 2.2 is refuted in general, not just by examples

CT-S6 refuted companion **Remark 2.2** ("the finite singularities — the roots of
`χ` — are always apparent") by exhibiting two counterexamples, `b = x+1` and
`b = x²+1`. The refutation is in fact **complete and structural**:

> For `χ(x)y'' + χ'(x)y' + c(x)y = 0` at **any** simple root `s` of `χ`, the
> residue of `p = χ'/χ` is exactly `1` and `q = c/χ` has at most a simple pole,
> so `(x−s)²q → 0`. The indicial polynomial is therefore `λ²` **for every such
> `χ` and `c`**. A repeated exponent at a genuine regular singular point always
> produces a log term in the second Frobenius solution. **No such point is ever
> apparent.**

> **Generalised, operator review #3.** The condition `c(s) ≠ 0` stated in the
> first version of this lemma is **unnecessary and has been dropped**. Once `p`
> has residue `1` and `q` has at most a simple pole, the indicial polynomial is
> `λ²` whatever `c(s)` is, and equal exponents then force the log term. The
> lemma is strictly more general than first recorded.

Label: **PROVEN** (elementary, fully symbolic, no case analysis).

The exactness identity `b = a'` — the very feature the companion highlights — is
what *forces* the residue to be 1 and hence forces the repeated exponent. So
Remark 2.2 is not merely unsupported; the structure it appeals to implies the
**opposite** of what it asserts.

This matters because **Conjecture 4.1 uses apparency as a premise**: it argues
`β = γ = 0` because *"both finite singularities are apparent"*. That premise is
false. No conjecture file was edited; this is reported to the operator only.

## 3. Correction to CT-S6 claim S6-C7

CT-S6 reports two results that cannot both stand as stated:

* **S6-C7 (STRUCTURAL):** System B's effective Katz multiset is `(1,0,0,0)`,
  which matches no Table 2.1 row.
* the relation claim (**PROVEN**): System C equals inverted System B in normal
  form — and System C's multiset is `(0,0,1)`, the D̃5/PV row.

Equivalent operators cannot have different multisets. The tension resolves in
favour of `(0,0,1)`, and the defect is in S6-C7:

System B's fourth point is `z = ∞`, with exponents `1 − √3/18` and `2 − √3/18`.
CT-S6 ruled it NOT APPARENT **because the exponents are not integers** — a test
that does not permit a rank-1 twist. But the exponents differ by exactly `1`,
and the normal-form reduction `y = exp(−½∫p)·v` is precisely such a twist. Under
`z ↦ 1/x` the point becomes `x = 0`, and the script confirms

```
R_Binv(0) = 11/4        (finite)
```

so `x = 0` is an **ordinary point of the normal form**. The twist shifts the
exponents by the common constant `√3/18 − 1` to `{0, 1}`, and with no log term
both local solutions are holomorphic. The point carries **no moduli**.

Since the twist at `z = ∞` is of regular-singular type `z^λ` (the `exp(−√3x/3)`
factor in CT-S6's gauge is holomorphic and non-vanishing there), it cannot
change any Katz invariant. Twisting by a rank-1 connection is a standard
normalisation and induces an isomorphism of the moduli of connections, so it is
legitimate for reading Table 2.1.

**Corrected statement (STRUCTURAL):** System B's effective Katz multiset, **up to
a rank-1 twist**, is `(0,0,1)` — identical to System C's, as the proven
equivalence requires. S6-C7's `(1,0,0,0)` and its "no matching row" conclusion
are **artefacts of an apparency test that disallows twisting**, and are
superseded.

> **Qualification, operator review #3.** "Ordinary after twist" is equivalence
> **up to a rank-1 twist**, not equivalence of the operators themselves. That
> distinction must appear in the claim text. It is nevertheless the right setting
> here, because van der Put–Saito Table 2.1 classifies **trace-free rank-2
> connections** — precisely the up-to-twist category — so System B's `(0,0,1)`
> is valid *there*, and only there.

CT-S6's *other* apparency verdicts are unaffected: `ρ±` and `s±` have **repeated**
exponents, and no twist can separate a repeated exponent or remove a log.

## 4. What this does and does not do for Conjecture 4.1

* **Does:** the Katz multiset of System C — the operator Conjecture 4.1 is
  actually about — is `(0,0,1)`, which **is** the D̃5 / PV row of van der Put–Saito
  Table 2.1, p. 2635. The conjecture's *conclusion* is consistent with the
  better source.
* **Does not:** establish the conjecture. Two independent obstacles stand.
  1. The operator's caveat, reproduced verbatim: *a matching Katz multiset is
     necessary but not sufficient; Table 2.1 classifies families of connections,
     and a single fixed operator matching a row does not make it a member of
     that isomonodromic family until the deformation parameter is specified.*
  2. The conjecture's stated **reason** is now known to be **false** — the finite
     singularities are not apparent — so the argument for `β = γ = 0` does not
     go through, even though the surface type it lands on survives.

So the position is: **right row, wrong reason, membership still open.** That is a
sharper and more useful outcome than either a confirmation or a refutation.

## 5. Relation to the System A result

System A is unaffected. Its Katz multiset `(1/2, −, 1/2)` is **ramified**, and
half-integer Katz invariants are invariant under twisting, so no normalisation
of the kind used in §3 can move System A into the `(0,0,1)` row. CT-S6 also
settled the `−` slot: it marks an **absent** singular point, not a dropped
regular or apparent one (claim S6-C9, PROVEN), which closes the premise flagged
in `CLASSIFICATION-TABLE.md` §5.3.

System A and System C therefore sit in **different rows**, and the *"two objects,
two surfaces"* reading of the Sakai Stratification note stands.
