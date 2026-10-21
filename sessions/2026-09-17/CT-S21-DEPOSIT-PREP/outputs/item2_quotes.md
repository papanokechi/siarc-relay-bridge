# CT-S21 item 2 — quote verification from page images

Ten page images were read, **one per message**, as the packet requires. No text
layer was used for any load-bearing quotation; the text layer was used once, to
locate a page before rendering it, and that use is marked below.

Status values are the packet's: **MATCHES** / **DIFFERS** (with the difference)
/ **NOT CHECKED**. Hypotheses were treated as in scope, not only theorem
statements.

## van der Put–Saito, Ann. Inst. Fourier 59 (2009) 7, 2611–2667

| # | page | what the notice (or letter) asserts | status |
|---|---|---|---|
| 1 | 2634 | trace-0 normalisation of the family; the strong-RH exception *"except possibly for (1/2,−,1/2) and (−,−,5/2)"*; the definition of `P`; Katz-invariant notation | **MATCHES** |
| 2 | 2635 | Table 2.1, caption *"Classification of Families"*, columns `r(0), r(1), r(∞), r(t), dim P`; `D̃₅`/PV = **(0,0,1)**, `dim P = 3`; `D̃₈`/PIII(D₈) = (1/2,−,1/2), `dim P = 0`; PVI row carries `r(t)=0`; *"R → P is a family of affine cubic surfaces"* | **MATCHES** |
| 3 | 2637 | the constraint the letter rests on: *"Further −θᵢ²/4 is the determinant of Aᵢ for i = 0, 1"*; `A∞ = (t/2)·diag(−1,1)`, `t ∈ ℂ*`; type (0,0,1) has a **positive** strong-RH answer | **MATCHES** |
| 4 | 2655 | `b(z)`'s first term prints `(p + ½(q−1)q)²` **without `t`**, while `B₁[1,2]` prints the same bracket **with `t`**; `c(z) = −(z−q)/(q−1)`; *"The first basis vector is chosen as cyclic vector … q is the unique zero of c(z) and p = a(q)"*; `U₀ ≅ ℂ × (ℂ∖{0,1})`; `A = z(z−1)(A∞ + A₀/z + A₁/(z−1))`, so `A(0) = −A₀` and `A(1) = A₁` | **MATCHES** |
| 5 | 2654 | — | **DIFFERS**, see below |

**Difference at row 5.** The letter and the notice both locate the family as
*"family (4.1) on p. 2655"*. The **label (4.1) is displayed on p. 2654**; only
the entries, including the `b(z)` being corrected, are printed on p. 2655. The
mathematics is unaffected and the entry is where the letter says it is, but a
letter to the authors should be exact. Suggested form:

> the entry `b(z)` of family (4.1) (displayed p. 2654), printed on p. 2655

p. 2654 also gives, in §4.3, the `(0,0,1)` exponent data `±θ₀/2, ±θ₁/2,
±(½tz + θ∞/2)`, which is the local formal type C3 appeals to.

## Jimbo, Publ. RIMS 18 (1982) 1137–1161

| # | page | assertion | status |
|---|---|---|---|
| 6 | 1152 | eigenvalues `±½θ_ν`; `α = ⅛(θ₀−θ_t+θ∞)²`, `β = −⅛(θ₀−θ_t−θ∞)²`, `γ = 1−θ₀−θ_t`, `δ = −½`; and the hypothesis **(A1)_PV: `θ₀, θ_t ∉ ℤ`**, printed *after* the dictionary | **MATCHES** |

This page also settles two OCR readings that CT-S15 had rejected: (3.1) prints
`diag(1,0)`, and (A1) constrains **only** `θ₀` and `θ_t`, not `θ∞`. Both
rejections were correct.

## Companion v1.2 (Zenodo 20481592)

| # | printed page | assertion | status |
|---|---|---|---|
| 7 | 3 | `a = 3x²+x+1`, `b = 6x+1`, `c = −x²`; roots `(−1 ± i√11)/6`; identity (8) `b = a′` | **MATCHES** |
| 8 | 4 | Remark 2.2 verbatim, ending *"the finite singularities of the ODE — the roots of χ — are always apparent"*; the Stokes gap `σ₊ − σ₋ = 2/√3` | **MATCHES** |
| 9 | 6 | Conjecture 4.1's tuple `(1/6, 0, 0, −1/2)`; *"The vanishing β = γ = 0 reflects the fact that both finite singularities are apparent"*; the derivation's *"θ₁ = θ₂ = 0 (apparent)"*; the scaling `(α,β,γ,δ) ↦ (α,β,cγ,c²δ)` with `c = √3`; the citations to **DLMF §32.2** and **§32.2(vi), Eq. 32.2.33**; and the admission that the `D₅^(1)` determination *"rests on a match against the Jimbo–Miwa–Ueno classification table [5] and is not yet corroborated by an independent Lax-pair derivation"* | **MATCHES** |
| 10 | 10 | §7.1 *"Summary of the identification obstruction"*; *"…together provide a complete explanation for the failure of identification searches"*; item 1 *"The finite singularities are apparent (trivial monodromy), so V_quad cannot arise as a period or CM value at these points."* | **MATCHES** |
| 11 | 5 | **not previously quoted by the notice** — Theorem 3.1 and its proof | **MATCHES**, and see the finding below |
| 12 | 7 | **not previously quoted by the notice** — Remark 4.2, Remarks 4.3–4.5, Theorem 5.1 | **MATCHES**, and see the finding below |
| 13 | 8 | C5 row 4: Remark 6.1's *"derived from the WKB and apparent-singularity data"* | **MATCHES** — printed verbatim as *"the parameters α = 1/6, β = γ = 0 are derived from the WKB and apparent-singularity data, but the surface-type determination `D₅^(1)` rests on a match against the Jimbo–Miwa–Ueno classification table [5] and awaits an independent Lax-pair derivation (Remark 4.5)"* |

Printed p. 5 was not in the cold packet. It was rendered from the local v1.2 PDF
— which is byte-identical to the file Zenodo serves and is **CC-BY-4.0**, so
rendering it raises no licence question — to `pages/companion_v12_printed5.png`.
The PDF text layer was used **only** to confirm which page index to render; every
quotation below is read from the image.

### Finding: C5's tabulation is incomplete, and it is incomplete in the companion's favour

C5 states that the passages depending on the apparency claim *"were located by a
full-text pass over v1.2 and read from page images."* The notice's C5 table lists
five: §4 Conjecture 4.1, the §4 derivation, the §4 opening, §6 Remark 6.1, and
§7.1 item 1. A grep of the notice finds **no mention anywhere of Theorem 3.1,
Remark 3.2, Remark 4.2, or Remark 6.7**. All four bear on apparency:

- **Remark 4.2** (printed p. 7) — *"In the present case θ₁ = θ₂ = 0 (apparent
  singularities), the standard connection formula degenerates, and the resulting
  expression for `M₁₁` is not immediately computable in closed form. This is
  consistent with the failure of all tested PSLQ identification bases."* This is
  a **load-bearing** use: it is the companion's explanation of the PSLQ nulls,
  and it rests on `θ₁ = θ₂ = 0` being justified by apparency. **Missing from C5.**
- **Remark 6.7** (printed p. 10) asserts the finite singularities *are apparent
  (trivial local monodromy … Theorem 3.1)* and draws the CM/Γ-value consequence
  from it. This is the same dependency as §7.1 item 1 and is **missing from C5**.
- **Remark 3.2** (printed p. 6) states that the monodromy at the finite
  singularities *is exactly trivial by algebra*. That is false on C1's evidence —
  and, more pointedly, it is inconsistent with the companion's **own** Theorem
  3.1 Step 4. **Missing from C5.**
- **Theorem 3.1** (printed pp. 4–5) is the load-bearing one, and the notice as
  drafted would mislead a reader about it.

**What Theorem 3.1 actually says and proves.** Its two parts are

> (i) At both finite singularities `s₁,₂ = (−1 ± i√11)/6`, the indicial equation
> is `ρ² = 0`, giving a double root `ρ = 0`.
>
> (ii) The monodromy around each `s_k` fixes `M₁₁ = V_quad`; the effective
> monodromy on the connection coefficient is trivial.

and the proof computes `p₀ = lim (x−s_k)P(x) = a′(s_k)/a′(s_k) = 1` and
`q₀ = 0`, giving `I(ρ) = ρ(ρ−1) + p₀ρ + q₀ = ρ² = 0`; then obtains the second
Frobenius solution `y₂ = y₁ log ζ + Σ dₙζⁿ` and notes *"The logarithm appears
only in y₂, not in y₁"*; then, in Step 4, **displays the monodromy explicitly**:

> `(y₁, y₂) ↦ [[1, 2πi], [0, 1]] (y₁, y₂)`

This matters in three ways, none of which the notice currently records:

1. **The companion already proves C1's lemma.** Residue 1, `ρ² = 0`, double root,
   logarithm in the second solution — Theorem 3.1's Step 1 and Step 3 are C1's
   local analysis, reached independently in v1.2. C1 is a correction to **Remark
   2.2's general claim** about the roots of `χ`, not a discovery that §3 missed.
2. **The companion already exhibits the non-trivial monodromy.** `[[1, 2πi],
   [0, 1]]` is unipotent and ≠ `I`. The notice's C1 says the structure *"implies
   the opposite of what it asserts"*; that is right about Remark 2.2, but v1.2's
   §3 had the matrix on the page.
3. **Theorem 3.1(ii) is not the apparency claim and may well survive C1.** It
   claims the *effective* monodromy **on the connection coefficient `M₁₁`** is
   trivial — because the unipotent action fixes `y₁`, whose coefficient `M₁₁` is.
   That is strictly weaker than, and logically independent of, *"the singularity
   is apparent"*. A reader of the notice as drafted would reasonably conclude
   that §3 falls together with Remark 2.2. On this evidence it does not.

This is **STRUCTURAL**: it follows from reading the printed statement and proof
against C1's statement. Whether Theorem 3.1(ii)'s conclusion is *correct* was not
re-derived in this session and is not asserted here; what is asserted is that it
is a **different claim** from the one C1 refutes, and that the notice does not
distinguish them.

## DLMF

| # | item | recorded |
|---|---|---|
| 12 | DLMF §32.2, cited by v1.2 for the PV normalisation and, at §32.2(vi) Eq. 32.2.33, for the PV→PIII degeneration | section, **Version 1.2.8**, **release date 2026-09-15**, sha256 of the page as served — in `REFS-MANIFEST.md` |

## Not checked

- Every quotation the notice draws from sources other than the five above.

### A defect I introduced and then caught

The first draft of this file recorded **Remark 6.1 (C5 row 4) as NOT CHECKED**,
on the stated ground that *"the cold-packet image `companion_v12_p7.png`
corresponds to printed p. 8"* and so Remark 6.1's page was unavailable. I had not
opened the image. Listing the directory and reading it showed Remark 6.1 printed
on that very page, and its quotation matches. The reasoning was sound, the
mapping `printed = N + 1` was right, and the conclusion was still wrong, because
I inferred a page's contents from its number instead of looking.

This is the **NOT CHECKED** analogue of the failure mode the sixth and seventh P0
amendments cover: a status that certifies nothing was about to be recorded as
though it were a finding about the evidence, when it was only a finding about my
own inattention. A **NOT CHECKED** row is only honest when something was actually
attempted and failed; otherwise it should say *not attempted*. Recommend an
eighth P0 line to that effect.

## Incidental, and outside this packet: the Borel normalisation is printed on p. 8

Printed p. 8 states the companion's Stokes-constant convention in full:

> (S_+ - S_-)[phi](z) = 2*pi*i*S*exp(-xi_0/z)*z**beta_exp*(1+O(z)), with Borel
> transform B[phi](xi) = sum_{n>=1} a_n xi**(n-1)/Gamma(n) (**Gamma(n), not n!**),
> the **full** Stokes jump (**not** the half-Stokes prescription), xi_0 = 2/sqrt(3),
> beta_exp = -1/(3*sqrt(3)).

Remark 6.2 records that v1.0's Stokes constant was wrong precisely because a
normalisation prefactor Gamma(beta_exp) = -6.00599... was used where the
universal resurgence factor 2*pi = 6.28319... belonged, and that *because the
two agree to 4.4% the slip survived the internal multi-method consensus*.

Neither fact is used in this packet and no claim is made from them. They are
recorded because the open zeta* = 4/sqrt(3) vs xi_0 = 2/sqrt(3) question (P1)
turns on exactly this: which Gamma normalisation, whole or half jump, and which
uniformiser. The half-vs-full Stokes prescription is a factor of 2, and
zeta* = 2*xi_0. That is a lead for the P1 successor, **not** a result.
