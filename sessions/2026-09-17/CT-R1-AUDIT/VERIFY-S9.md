# CT-R1-AUDIT R5 — independent check of `CT-S9-PVPARAMS`

Script: `verify_s9.py` · output: `verify_s9.out` / `verify_s9.log`

CT-S9 did **not** halt — it found a quotable convention and reported a
contradiction with the companion's parameter tuple. Because that is a strong
claim resting entirely on one dictionary, the dictionary and the inference were
re-checked from the primary source.

## 1. The Jimbo quote is exact

Verified by reading the page image `CT-S9-PVPARAMS/outputs/jimbo_page16-16.png`
— Jimbo, *Monodromy Problem and the Boundary Condition for Some Painlevé
Equations*, PRIMS, **p. 1152**. Verbatim:

> the eigenvalues of `A_ν(t) = ± ½ θ_ν`  (ν = 0, t)
>
> `α = ⅛(θ₀ − θ_t + θ_∞)²`,  `β = −⅛(θ₀ − θ_t − θ_∞)²`,
> `γ = 1 − θ₀ − θ_t`,  `δ = −½`.

CT-S9 transcribed this correctly. Since the eigenvalues of `A_ν` are `±½θ_ν`,
the **exponent difference at ν is exactly `θ_ν`**, so reading `θ` off an
exponent difference is legitimate — and exponent differences are invariant under
rank-1 twisting, which is what makes the scalar-to-connection step safe here.

## 2. The computation reproduces

| quantity | CT-S9 | independent re-derivation | |
|---|---|---|---|
| normal form | `(12x⁴+4x³+4x²+11)/(4(3x²+x+1)²)` | same | ✓ |
| residue at `s±` | `−1/4` | `−1/4` | ✓ |
| exponent difference at `s±` | `0` | `√(1+4·(−1/4)) = 0` | ✓ |
| `R(∞)` | leading coeff `1/3` | `R → 1/3` | ✓ |
| WKB exponentials at `∞` | `exp(±√3x/3)` | `exp(±√3x/3)` | ✓ |
| dictionary at `θ₀=θ_t=0` | `α=θ∞²/8, β=−θ∞²/8, γ=1, δ=−1/2` | same | ✓ |

So `β = −α` **identically**, and the companion's `β = 0` forces `θ∞ = 0`, hence
`α = 0`, contradicting `α = 1/6`; and `γ = 1` contradicts `γ = 0`.

## 3. Addition 1 — the contradiction is genuine, not conventional

A referee's first move would be to ask whether `γ` can simply be rescaled. It
cannot, once `δ` is pinned. Under `z ↦ cz` the PV equation transforms as

```
(α, β, γ, δ)  ->  (α, β, cγ, c²δ)
```

so holding `δ = −1/2` forces `c² = 1`, i.e. `c = ±1`, and `γ` is fixed up to
sign. **`γ = 1` cannot be rescaled to `γ = 0`.** The companion's `γ = 0` is a
genuinely different equation, not the same one in other units. Label: PROVEN
(elementary scaling computation).

## 4. Addition 2 — Jimbo's standing assumption (A1)_PV is VIOLATED

Immediately below the dictionary on the same page, Jimbo assumes

> **(A1)_PV**  `θ₀, θ_t ∉ ℤ`.

Our local data gives `θ₀ = θ_t = 0 ∈ ℤ`. CT-S9 did not flag this.

Two consequences, pulling in opposite directions:

* The **dictionary itself is stated before (A1)_PV** and is not conditional on
  it, so the parameter computation in §2 stands.
* But everything Jimbo derives **after** that line — the monodromy
  parametrisation and the connection/asymptotic analysis — is outside its stated
  hypotheses for our case. Any attempt to push further into Jimbo's machinery
  for System C is **not covered by the source**.

This is also a coherence check that comes out right: integer `θ` is exactly the
resonant case, and resonance is exactly when logarithms can appear. We
independently found logarithms at both finite points. The local data is
self-consistent, and it sits precisely on Jimbo's excluded locus.

## 5. Addition 3 — the PV time `t` is not free; it is FIXED

The operator asked: *System C has no free parameter as written — where would the
PV time variable come from?* It can now be answered concretely.

Jimbo's system (3.1) has singular points `0`, `t`, `∞`, with the irregular part
at `∞` normalised to `exp(x·diag(1,0))`, whose **exponent difference is exactly
`x`**. Matching System C requires an affine map `z = k(x − s₀)` carrying one
finite singular point to `0`, the other to `t`, and fixing `∞`.

* The shift `s₀` is free (it only relabels which point is `0`).
* The **scale `k` is forced**: System C's exponent difference at `∞` is
  `2√3x/3`, so `k = 2√3/3 = 2/√3` is the unique scale making it `z`.

Therefore

```
t = k (s∓ − s±) = ∓ 2i√33 / 9 ,      |t| = 2√33/9 ≈ 1.2766
```

**There is no free deformation parameter.** System C corresponds to a *single
value* of the PV time, determined by its own coefficients — the two choices
differing only by the labelling of `s+` and `s−`, i.e. by `t ↦ −t`.

This sharpens the operator's caveat rather than defeating it. It says exactly
what would have to be produced for a membership claim: not a fibre, but a
**family** — a curve `t ↦ L_t` of connections, isomonodromic in `t`, whose fibre
at `t = ∓2i√33/9` is System C. Nothing in this run exhibits such a family, and
its existence is **NOT FOUND in the inspected sources by the methods used**.
Label: STRUCTURAL.

## 6. Net position on Conjecture 4.1

| parameter | companion | this analysis | status |
|---|---|---|---|
| `α = 1/6` | claimed | `α = θ∞²/8`, `θ∞` not fixed by local data | **UNDETERMINED** |
| `β = 0` | claimed, from apparency | `β = −α`, so `β = 0 ⟺ α = 0` | **CONTRADICTED** jointly with `α = 1/6` |
| `γ = 0` | claimed, from apparency | `γ = 1 − θ₀ − θ_t = 1` | **CONTRADICTED**, and not rescalable |
| `δ = −1/2` | claimed | Jimbo's normalisation | **CONSISTENT** (conventional) |

The earlier finding stands and hardens: **right row, wrong reason** — the
`(0,0,1)` Katz multiset still matches the D̃5 / PV row of van der Put–Saito, but
the parameter tuple attached to it in Conjecture 4.1 does not survive contact
with the correct local data.

**No conjecture file was edited.** Reported to the operator only.
