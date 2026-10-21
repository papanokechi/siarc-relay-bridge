# CT-R1-AUDIT R6 — independent check of `CT-S8-LITCHECK` (deposit gate 3)

Gate 3 was the operator's "biggest risk". It returned a **hit**: the radius
theorem is prior art. Because that finding is the one most likely to change the
deposit, its load-bearing citation was re-verified from the page image rather
than from the agent's transcription or from OCR.

## 1. The Gautschi quote is exact — but OCR corrupts the *hypotheses*

`CT-S8` quoted Theorem 2.3 from `g1967_p35_mid.png`. Read directly, that image
confirms the statement verbatim, including the parenthetical `(i.e., σ > τ)` and
the conclusion `y_{n+1,1}/y_{n,1} ~ −a n^σ`.

However, the surrounding hypotheses were only available via a lossy OCR layer,
and OCR rendered `(2.8)` ambiguously — it dropped the Greek letters and produced
`"ab 0; a, real"`. That admits two readings with **very different consequences**:

* `ab ≠ 0; a real` — would restrict the leading coefficient to be **real**, and
  our theorem allows `b ∈ ℂ[n]`, i.e. **complex `β_d`**; or
* `ab ≠ 0; α, β real` — restricts only the **exponents**.

Journal p. 34 was therefore re-rendered from the PDF at 3× (`refs/gautschi_p34_bot.png`).
The true text is:

> **(2.8)**  `a_n ∼ a n^α`,  `b_n ∼ b n^β`,  `ab ≠ 0;  α, β  real;  n → ∞.`
>
> The asymptotic structure of the solutions now depends on the *Newton-Puiseux*
> diagram formed with the points `P₀(0,0)`, `P₁(1,α)`, `P₂(2,β)`. This is the
> broken line `P₀P₁P₂`, if `P₁` is above the straight line joining `P₀` with `P₂`;
> otherwise it [is the segment `P₀P₂`].

**The reality condition is on the exponents `α, β`, not on the coefficients.**
So Perron–Kreuser covers complex `β_d`, and it covers the *full* generality of
our Result 1. The restrictive reading is refuted. (Gautschi then sets `σ` =
slope of `P₀P₁` = `α` and `τ` = slope of `P₁P₂` = `β − α`, so `σ > τ` ⟺ `2α > β`
⟺ `P₁` above `P₀P₂` — the parenthetical is self-consistent.)

## 2. The application checks out

Our recurrence `Q_n = b(n)Q_{n−1} + Q_{n−2}` written in Gautschi's form
`y_{n+1} + a_n y_n + b_n y_{n−1} = 0` (his (2.1), confirmed at (6.1) on p. 55):

```
Q_{n+1} − b(n+1) Q_n − Q_{n−1} = 0
  =>  a_n = −b(n+1) ∼ −β_d n^d   (a = −β_d, α = d)
      b_n = −1                    (b = −1,   β = 0)
```

* `(2.2)` `b_n ≠ 0`: holds, `b_n ≡ −1`.
* `(2.8)` `ab ≠ 0`: holds since `β_d ≠ 0`. `α = d`, `β = 0` are real. ✓
* Case **(a)**: `P₁(1,d)` above the segment `(0,0)–(2,0)` ⟺ `d > 0` ✓ for all `d ≥ 1`.

Conclusion: `Q_{n+1}/Q_n ∼ −a n^α = β_d n^d`, whence
`Q_n ≍ β_d^n (n!)^d` and

```
|Q_n / (dn)!|^{1/n}  ->  |β_d| · (n/e)^d / (dn/e)^d  =  |β_d| / d^d.
```

That is **exactly Result 1**. Label: **STRUCTURAL** (a short derivation from a
quoted classical theorem; not re-proved here).

## 3. The sharp point: what hypothesis (H) is actually doing

Perron–Kreuser applies to our recurrence **unconditionally** — it needs no
analogue of (H). What it delivers is a *pair* of solutions, with `y_{n,2}`
minimal and `y_{n,1}` dominant, and the ratio law holding for `y_{n,1}` and
hence for any solution with a nonzero `y_{n,1}` component.

**(H) is precisely the statement that `Q_n` is not the minimal solution.** So the
decomposition of our Result 1 into known parts is complete and tight:

| ingredient | status |
|---|---|
| ratio law for the dominant solution | Perron–Kreuser (Gautschi Thm 2.3(a), p. 35) |
| "(H) ⟺ `Q_n` non-minimal" | Pincherle (Gautschi Thm 1.1, p. 31) + DLMF §3.6(ii) |
| ratio law ⇒ radius, via Stirling | routine |

There is no residue of Result 1 left over as new.

## 4. Status of the other three results

| result | CT-S8 verdict | audit position |
|---|---|---|
| 1. radius / nth-root | **PRIOR ART** | **CONFIRMED** — §§1–3 above |
| 2. growth law, explicit `s` | **PARTIAL, one blocking gap** | accepted; see §5 |
| 3. explicit `K` | **NOT FOUND** — strongest novelty candidate | accepted, with the caveat in §6 |
| Borel framing | **PARTIAL, weakest** | accepted |
| hypothesis (H) | classical (Pincherle) | accepted |

CT-S8 also **independently re-derived** `K = r_∞ (2π)^{(d−1)/2} / (√d ∏ᵢ Γ(1−rᵢ))`
and checked it numerically at 60 dps. This is an independent reproduction of
P3's closed form by a session that did not have P3's derivation, which
materially strengthens the `K` result even as it weakens Result 1.

## 5. The blocking gap — Wong & Li (1992a), NOT OBTAINED

DLMF §2.9 gives explicit exponents only for bounded coefficients, and
**explicitly defers** the case `w(n+2) + n^P f(n) w(n+1) + n^Q g(n) w(n) = 0`
(eq. 2.9.14 — ours is `P = d`, `Q = 0`) to **Wong & Li, *Stud. Appl. Math.*
87(4) (1992), 289–324**. That paper is **paywalled (Wiley HTTP 403) and was not
obtained**; the agent correctly declined the mirror sites the search surfaced.

So it is **NOT ESTABLISHED** whether `s = β_{d−1}/β_d + (d−1)/2` is already in
print. Under the INSPECTED convention this is recorded as
**"NOT FOUND in the sources obtained, by the methods used"** — *not* as "new".

**This is the one item that must be closed before deposit**, and it cannot be
closed from open sources. It needs operator action: institutional access, an
interlibrary copy, or a direct request to the authors.

## 6. A caveat on the `K` novelty claim

`K` was NOT FOUND, and Nemes (arXiv:2508.15246v2) supplies positive evidence
that connection constants are usually left as unknowns. But note the asymmetry:
Result 1 was found to be classical *only after* the right search term
("Perron–Kreuser") surfaced, and Wong & Li — the one source most likely to
contain Result 2, and plausibly related material on `K` — was never read. A
NOT FOUND verdict on `K` therefore carries **less weight than it appears to**
until §5 is closed.

## 7. Net effect on the deposit

The note's contribution claim as drafted is **no longer supportable** and must be
rewritten. Recommended framing, subject to §5:

* Result 1 — present **as a corollary of Perron–Kreuser, with attribution**, not
  as new. Its value is the packaging: the `(dn)!` normalisation and the explicit
  Borel radius.
* Result 2 — status **undetermined** pending Wong & Li.
* Result 3 (`K`) — the strongest candidate, now independently reproduced.
* The vacuity explanation (only `β_d`, `β_{d−1}` are read) — unaffected by any
  of this, and NOT FOUND in the literature searched.

This is a demotion, and it is the correct outcome of the gate the operator
insisted on.
