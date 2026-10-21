# Deposit plan — standalone note

> ## ⚠ SUPERSEDED BY OPERATOR REVIEW #4 — THE STANDALONE NOTE IS DROPPED
>
> After gate 3 returned (Result 1 is Perron–Kreuser), the operator ruled that
> the residual contribution is too thin to carry a standalone note:
>
> * **`K` is thin on its own** — given the growth law it is a routine
>   product-of-Gammas computation. Its substance sits in `r_∞`, which has no
>   closed form (the PSLQ run was null). In the Birkhoff–Trjitzinsky / Wong–Li
>   framework the constant multiplying the dominant solution **is** the
>   undetermined connection constant, so if Wong–Li has the growth law, `K` in
>   some form is likely there too or is an immediate corollary. The one modest
>   novelty is that `r_∞` comes with a rapidly convergent explicit series.
> * **The Borel framing and the vacuity explanation are expository** — valuable
>   in context, not load-bearing enough to carry a note.
>
> **New route: Channel Theory v1.7**, as a correction-and-attribution notice.
> Draft: `DRAFT-CT-v1.7-NOTICE.md`.
>
> This also **removes the blocker**. A version notice can state plainly that
> whether the exponent formula is in print was not determined. A standalone note
> claiming a contribution could not honestly say that.
>
> The stronger publishable material is on the **Painlevé** side, and it corrects
> a deposited paper. Draft: `DRAFT-COMPANION-v1.3-NOTICE.md`.
>
> Everything below is retained as the record of how that conclusion was reached.

---

Prepared under operator review #3, ruling 5. **Nothing has been deposited,
committed, or submitted.** This records the chosen route and the gate status.

## 1. Route

**A standalone note**, with Channel Theory v1.7 citing it. Operator's reasoning:
it is self-contained, suits journal submission better than a record carrying six
versions of errata, and gives a clean citable result.

## 2. Contents — **REVISED after gate 3 returned**

The original list below is superseded. Gate 3 found that item 1 is classical,
so the contribution claim has been rewritten. See §4 for the revised framing and
`VERIFY-S8.md` for the evidence.

~~1. The **general-`d` radius theorem** under hypothesis (H).~~
→ **Corollary of Perron–Kreuser, to be presented with attribution.**

2. The **growth law** — *status undetermined* pending Wong & Li (1992a).
3. The **closed-form amplitude `K`**, labelled *derived and numerically
   verified* — not proven. **Now the strongest novelty candidate**, and
   independently reproduced by `CT-S8-LITCHECK`.
4. The **vacuity explanation** (the result reads only `β_d` and `β_{d−1}`) —
   unaffected by gate 3, and NOT FOUND in the literature searched.

Source: `sessions/2026-09-17/CT-S1-THEOREM/theorem.tex` (7 pp, compiles clean)
and `CT-S3B-RINF/DERIVATION.md`.

## 3. Gates — all three must close before any deposit

| # | Gate | Status | Owner |
|---|---|---|---|
| 1 | **Cold review** of part (i) Step 3 (the multinomial sandwich and its maximality sub-lemma) and the G1 argument | **CLOSED** — both passages cold-read SOUND after two citation repairs | `CT-S7-COLDREAD`, `CT-S10-COLDREAD2` |
| 2 | **No machine-checked claim.** 7 `sorry`s remain in `XiZero.lean`, so the note **must not** say it is formally verified | **OPEN — binding constraint on wording** | — |
| 3 | **Literature check** — the biggest risk | **RETURNED — NOT CLOSED.** Result 1 is **prior art** (Perron–Kreuser); Result 2 blocked on a paywalled paper | `CT-S8-LITCHECK` |

### Gate 1 — returned, and it earned its keep

`CT-S7-COLDREAD` read `theorem.tex` alone, with no access to `CT-R1-AUDIT/` or
any `REPORT.md`. Two verdicts:

* **`thm:radius` Step 3 — SOUND.** The multinomial sandwich, including the
  exchange-argument maximality sub-lemma added in round R1, is complete and
  correct as written. Claim **S1-03** is now `review: cold` — at the time, the
  first deposit-eligible proof claim in the corpus.
* **`thm:growth` Step 3 / G1 — ERROR.** DLMF **(5.11.12)** was misquoted as the
  full `G_k` expansion. Confirmed independently against dlmf.nist.gov (page
  sha256 `929045c7…`): (5.11.12) is the plain ratio
  `Γ(z+a)/Γ(z+b) ∼ z^{a−b}`; the `G_k` expansion is **(5.11.13)** and
  `G_0(a,b) = 1` is **(5.11.15)**.

The **mathematics is unaffected** — the proof only ever needed (5.11.12), which
is precisely the statement that gives `h_∞ = 1`. The citation was corrected at
five sites and the document recompiles clean at 7 pages.

**Gate 1 is now CLOSED.** `CT-S10-COLDREAD2` re-read the repaired passage cold —
`theorem.tex` only, no access to `CT-R1-AUDIT/`, `CT-S7-COLDREAD/`, or any
`REPORT.md`. It found the Gamma-ratio proof, the algebra, the product/error
step, the hypotheses, the circularity check **and the corrected DLMF equation
numbers** all sound. Its only finding was a second, smaller citation defect: the
bibliography said **Release 1.2.4** while DLMF is **Version 1.2.8, release date
2026-09-15**. Confirmed independently from the stored page (sha256
`929045c7…`), corrected, recompiled clean at 7 pages.

**S1-04 is now `review: cold`**, so both deposit-worthy proof claims are
deposit-eligible.

### The pattern, stated plainly

Three independent reads of this document produced three defects — **all three in
citation metadata, none in the argument**. That is mildly reassuring about the
mathematics and unflattering about the bibliography discipline. It is also the
*same failure mode* as the stale `\bibitem{Vquad}` from ruling 2: a reference
carried forward from an earlier draft rather than re-checked.

**Recommendation (operator's call):** before deposit, re-fetch and hash every
external citation in the note rather than trusting any that were transcribed
earlier in this run. That is cheap and it closes the only class of defect this
document has actually exhibited.

### Gate 3 — the scope

The growth law `Qₙ ~ r_∞ ∏ b(k)` is close to classical material. CT-S8 is
checking **Perron** (continued fractions; Poincaré–Perron for difference
equations), **Birkhoff** and **Birkhoff–Trjitzinsky** (normal solutions, which
have exactly the shape of the growth law), **Wong–Li** (the later rigorous
work), and **Pincherle/Gautschi** (for hypothesis (H)).

The operator's working hypothesis, which CT-S8 was told to try to **confirm**:

> the new contribution is probably the **Borel-radius framing**, the **explicit
> `K`**, and the **vacuity explanation** — not the growth law itself.

The specific thing to watch: classical difference-equation asymptotics typically
determines solutions only **up to an undetermined multiplicative constant**. If
that is so here, the closed-form `K` is the genuinely novel part. CT-S8 must
fetch only open-access sources into `refs/` with sha256, quote chapter and verse
with page numbers, and **never reconstruct a cited result from memory**.

The note must then **cite that prior work and state its contribution relative to
it.**

## 4. Wording constraints carried into the draft

* `K`: **derived and numerically verified** (110 digits across 8 cases) — never
  "proven".
* `r_∞`: **VERIFIED** to 2317.8 digits by agreement between extrapolation
  levels — explicitly *not* rigorous.
* No formal-verification claim anywhere.
* Hypothesis (H) stated with its Pincherle / minimal-solution reading, and with
  the fact that it holds automatically for `b(n) > 0`.
* The scope remark kept: the theorem gives radius and leading growth only, reads
  only `β_d` and `β_{d−1}`, and does **not** determine the analytic type of the
  Borel singularity.

## 5. Not in scope for this note

The surface-type material (Systems A/B/C, Table 2.1, Conjecture 4.1) belongs to
the correction note scoped in `CORRECTION-NOTE-SCOPE.md`, not here. Keeping them
separate is what avoids repeating the v1.4 conflation.

---

## 4. Gate 3 — returned, and it changed the deposit

`CT-S8-LITCHECK` ran the prior-art search the operator asked for. Its central
finding was re-verified independently (`VERIFY-S8.md`), including re-rendering
Gautschi p. 34 from the PDF because the OCR layer corrupted the hypotheses in a
way that would have produced the *wrong* conclusion.

### 4.1 Result 1 is prior art — CONFIRMED

The radius theorem is a corollary of **Perron–Kreuser**, as stated in
**Gautschi, *SIAM Review* 9(1) (1967), Theorem 2.3(a), p. 35**. In his form
`y_{n+1} + a_n y_n + b_n y_{n−1} = 0`, our recurrence gives `a_n ∼ −β_d n^d`,
`b_n ≡ −1`, so `α = d`, `β = 0`, and `P₁(1,d)` lies above `(0,0)–(2,0)` for
every `d ≥ 1`. Case (a) yields `Q_{n+1}/Q_n ∼ β_d n^d`, and Stirling gives the
radius.

The decomposition leaves **no new residue**:

| ingredient | status |
|---|---|
| ratio law for the dominant solution | Perron–Kreuser (Gautschi Thm 2.3(a), p. 35) |
| "(H) ⟺ `Q_n` non-minimal" | Pincherle (Gautschi Thm 1.1, p. 31) |
| ratio law ⇒ radius | routine Stirling |

Perron–Kreuser needs **no analogue of (H)** — it applies unconditionally, and
(H) is precisely what identifies `Q_n` as the dominant solution. The hypothesis
we thought was doing the work is the classical minimality dichotomy.

**`S1-03` keeps its PROVEN label and its cold review.** Those grade
*correctness*, and the proof is correct and independently checked. Novelty is a
separate axis, now recorded in a separate `audit_r6` field on that claim.

### 4.2 The blocking gap — Wong & Li (1992a)

DLMF §2.9 gives explicit exponents only for bounded coefficients and
**explicitly defers** our case (eq. 2.9.14 with `P = d`, `Q = 0`) to
**Wong & Li, *Stud. Appl. Math.* 87(4) (1992), 289–324**, which is **paywalled
(Wiley HTTP 403) and was not obtained**. The agent correctly declined the mirror
sites that search surfaced.

So whether `s = β_{d−1}/β_d + (d−1)/2` is already in print is **NOT
ESTABLISHED** — recorded as *NOT FOUND in the sources obtained, by the methods
used*, never as "new".

**This cannot be closed from open sources.** It needs the operator:
institutional access, an interlibrary copy, or a request to the authors. It is
the single item standing between here and a defensible contribution claim.

### 4.3 What gets stronger

`CT-S8-LITCHECK` independently derived and numerically verified

```
K = r_∞ (2π)^{(d−1)/2} / ( √d · ∏ᵢ Γ(1−rᵢ) )
```

at 60 dps for four polynomials (`d = 1, 2, 3`), **without access to P3's
derivation**. That is a genuine independent reproduction, and it makes `K` the
strongest remaining novelty candidate — supported further by Nemes
(arXiv:2508.15246v2), who states that connection constants are "often treated as
unknowns in other methods" and computes them only numerically.

### 4.4 The caveat that should temper §4.3

A NOT FOUND verdict on `K` is weaker than it looks while §4.2 is open. Result 1
was found to be classical only once the term "Perron–Kreuser" surfaced — an
example of exactly the failure mode a literature search is prone to — and
Wong & Li, the source most likely to bear on Result 2 and plausibly on `K`, was
never read.

## 5. Revised contribution claim (proposed, operator's decision)

> The note gives a self-contained treatment of `Q_n = b(n)Q_{n−1} + Q_{n−2}`.
> The radius statement is a **corollary of the Perron–Kreuser theorem**
> (Perron 1921; Kreuser 1914; as presented in Gautschi 1967, Thm 2.3), combined
> with **Pincherle's theorem**, under hypothesis (H) that `Q_n` is not minimal;
> it is recorded here in the `(dn)!` normalisation because that is the form the
> Borel radius needs. The contribution is **(a)** the explicit closed-form
> amplitude `K`, **(b)** the Borel-plane framing, and **(c)** the observation
> that the leading asymptotics read only `β_d` and `β_{d−1}`, which explains the
> v1.6 vacuity finding.

Item (b)'s strength depends on §4.2; item (a)'s on §4.4.

## 6. Gate summary as it stands

| gate | status | blocker |
|---|---|---|
| 1. Cold review | **CLOSED** | — |
| 2. No machine-checked claim | **OPEN BY DESIGN** | 7 `sorry`s; binding on wording |
| 3. Literature check | **RETURNED, NOT CLOSED** | Wong & Li (1992a) — needs operator access |

**Recommendation: do not deposit yet.** Gate 3's blocker is narrow, concrete,
and cheap for an operator with library access, but it is load-bearing for the
only claim the note would be making.
