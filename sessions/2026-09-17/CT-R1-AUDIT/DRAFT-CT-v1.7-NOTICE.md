# DRAFT — Channel Theory v1.7 correction and attribution notice

**STATUS: DRAFT FOR THE OPERATOR. Nothing has been deposited, committed, or
submitted. No Channel Theory source file has been edited.** This is a proposed
notice, following the pattern of the earlier Channel Theory errata.

Prepared under operator review #4, which directed: drop the standalone note, and
place this material in Channel Theory v1.7 instead.

> **Wording flagged `[WONG-LI]` below is NOT FINAL.** It depends on reading
> Wong & Li (1992a) — see §5. Two alternative phrasings are supplied for each
> such passage.

---

## Proposed notice text

### N1. Conjecture 3.3.A* is a known theorem — attribution and retirement of the conjecture label

What was recorded in earlier versions as **Conjecture 3.3.A\*** is not a
conjecture. For the recurrence

```
    Q_n = b(n) Q_{n-1} + Q_{n-2} ,    Q_{-1} = 0,  Q_0 = 1,
    b in C[n],  deg b = d >= 1,  leading coefficient beta_d != 0,
```

the statement

```
    lim |Q_n / (dn)!|^{1/n}  =  |beta_d| / d^d
```

is a corollary of two classical results:

* the **Perron–Kreuser theorem**, as presented in
  **W. Gautschi, "Computational Aspects of Three-Term Recurrence Relations",
  *SIAM Review* 9(1) (1967), Theorem 2.3(a), p. 35**; and
* **Pincherle's theorem** (ibid., Theorem 1.1, p. 31; see also DLMF §3.6(ii)).

Writing the recurrence in Gautschi's form `y_{n+1} + a_n y_n + b_n y_{n−1} = 0`
gives `a_n ∼ −β_d n^d` and `b_n ≡ −1`, so in his notation `α = d` and `β = 0`,
his hypotheses (2.2) and (2.8) hold, and the Newton–Puiseux point `P₁(1,d)`
lies above the segment `P₀(0,0)–P₂(2,0)` for every `d ≥ 1`. Case (a) of his
Theorem 2.3 then gives `Q_{n+1}/Q_n ∼ β_d n^d`, and Stirling's formula yields
the displayed limit.

**The conjecture label is retired.** The result is stated in this version as a
theorem with the attribution above.

### N2. This supersedes the EBR positivity upgrade as the grounding

Earlier versions grounded the result via an EBR positivity argument, which
required `b(n) > 0`. That grounding is **superseded** and is no longer needed.

The correct hypothesis is weaker and structural. Perron–Kreuser applies to this
recurrence **unconditionally**; what is needed in addition is only that `Q_n` is
**not the minimal solution** of the recurrence — equivalently, that

```
    r_inf  :=  lim_{n->oo}  Q_n / prod_{k<=n} b(k)   is nonzero.
```

This is exactly the **minimal/dominant dichotomy** of Pincherle's theorem. It
holds automatically when `b(n) > 0` for all `n ≥ 1`, which recovers the old
positivity case, but it holds far more generally: the result is valid for
**complex** `b`, including sign-changing and complex-coefficient cases.

Two points of care, both verified:

* Gautschi's hypothesis (2.8) requires `α, β` — the **exponents** — to be real.
  It imposes **no** reality condition on the coefficients. Complex `β_d` is
  therefore covered.
* Perron–Kreuser needs no analogue of the nonvanishing hypothesis; that
  hypothesis is doing exactly one job, namely selecting the dominant solution.

### N3. The amplitude and the `r_∞` series

Beyond the radius, the leading growth is

```
    Q_n / Gamma(dn+1)  =  K (beta_d/d^d)^n n^s (1 + O(1/n)),
    s = beta_{d-1}/beta_d + (d-1)/2,
```

with the amplitude available in closed form. Writing `b(n) = β_d ∏ᵢ (n − rᵢ)`,

```
    K  =  r_inf * (2 pi)^{(d-1)/2} / ( sqrt(d) * prod_i Gamma(1 - r_i) ).
```

This was derived via the Gauss multiplication formula and verified numerically
to over 100 digits across eight cases; it was subsequently **re-derived
independently** by a separate session with no access to the original
derivation. It is **derived and numerically verified, not proven**, and is
stated as such.

The remaining ingredient `r_∞` has no known closed form — a PSLQ search over a
pre-registered basis at 500, 1000 and 2000 dps returned a **null result** — but
it is given by the rapidly convergent explicit series

```
    r_n = r_{n-1} + r_{n-2} / ( b(n) b(n-1) ) ,
```

whose increments decay like `n^{−2d}`.

> `[WONG-LI]` **Alternative A (if Wong & Li 1992a does *not* contain the
> exponent formula):**
> "The exponent `s` and the amplitude `K` are stated here in explicit form. A
> literature search located the general framework in Birkhoff–Trjitzinsky and
> in Wong & Li (1992a), but did not find these explicit expressions in print."
>
> `[WONG-LI]` **Alternative B (if it does):**
> "The exponent `s` follows from Wong & Li (1992a, [precise result reference to
> be inserted]); it is restated here in the `(dn)!` normalisation used for the
> Borel radius. The explicit amplitude `K` and the `r_∞` series are given
> here in the form needed for that normalisation."

Whichever alternative is used, the relation of `K` to the connection constant of
the Birkhoff–Trjitzinsky / Wong–Li framework **must be stated**, since in that
framework the constant multiplying the dominant solution is precisely the
undetermined connection constant.

### N4. The `rem:d3-vacuous` vacuity finding now has a one-line explanation

The vacuity observed at `d = 3` is not an artefact. It follows immediately from
N1–N3:

> `ξ₀` reads only `β_d`, and `ρ` reads only `β_d` and `β_{d−1}`.

The leading Borel-plane data are therefore blind to `β_0, …, β_{d−2}`, so any
test built solely on `ξ₀` and `ρ` cannot distinguish polynomials sharing their
top two coefficients. This was confirmed by a pre-registered vacuity check:
varying `β_0 … β_{d−2}` on a grid left `s` unmoved beyond fit error, while
varying `β_{d−1}` moved it as predicted.

---

## 5. What blocks finalisation

Only the `[WONG-LI]` passages. DLMF §2.9(ii) gives explicit exponents only for
bounded coefficients and **explicitly defers** the case of its eq. (2.9.14) —

```
    w(n+2) + n^P f(n) w(n+1) + n^Q g(n) w(n) = 0
```

with `P = d`, `Q = 0` for us — to **Wong and Li (1992a)**.

**Exact citation, verified 2026-09-17 against `https://dlmf.nist.gov/bib/W`:**

> R. Wong and H. Li (1992a). *Asymptotic expansions for second-order linear
> difference equations.* **II**. *Studies in Applied Mathematics* **87**(4),
> pp. 289–324. ISSN 0022-2526.

**Caution — the DLMF suffix ordering is counterintuitive.** "1992a" is the paper
titled "**II**", in *Stud. Appl. Math.* The other one, Wong & Li **(1992b)**, is
*J. Comput. Appl. Math.* **41**(1–2), pp. 65–94, and covers the
**bounded-coefficient** case, which is **not** ours. A request quoting only
"Wong & Li 1992a" risks retrieving the wrong paper; quote the full citation.

The paper is paywalled (Wiley); it was not obtained, and no mirror or shadow
library was used. Access options, in the operator's order of preference:
purchase the single article from Wiley; the National Diet Library or a nearby
university library's visitor access (check 1992 holdings of *Studies in Applied
Mathematics*); or an author request, which is routinely granted for a paper of
this age.

## 6. Why v1.7 rather than a standalone note

The operator's reasoning, recorded here so the decision is auditable:

* `K` is thin as a standalone result — given the growth law it is a routine
  product-of-Gammas computation, and the substance sits in `r_∞`, which has no
  closed form. In the Birkhoff–Trjitzinsky / Wong–Li framework the constant
  multiplying the dominant solution is exactly the undetermined connection
  constant, so if Wong–Li contains the growth law, `K` in some form is likely
  there too or is an immediate corollary.
* The Borel framing and the vacuity explanation are **expository**: valuable in
  context, but not load-bearing enough to carry a note.
* A v1.7 notice **removes the blocker**. It can state plainly that whether the
  exponent formula is in print was not determined. A standalone note claiming a
  contribution could not honestly say that.

## 7. Provenance of the statements in this draft

Every substantive statement above traces to a recorded claim in
`sessions/2026-09-17/*/claims.jsonl`. Note in particular:

* The radius result carries **PROVEN** with `review: cold` — the proof was
  independently checked. Being classical does not make it wrong; priority is
  recorded on a separate axis.
* `K` carries **VERIFIED**, never PROVEN.
* Nothing here is machine-checked. Seven `sorry`s remain in the Lean
  development, and **this notice must not claim formal verification.**
