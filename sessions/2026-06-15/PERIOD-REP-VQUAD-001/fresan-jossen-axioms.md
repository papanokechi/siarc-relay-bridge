# Stage 2 — Fresán–Jossen exponential-period axioms (authoritative summary)

**Chain:** PERIOD-REP-VQUAD-001 · **Stage:** 2 · **Date:** 2026-06-15

**Reference (verified).** Javier Fresán & Peter Jossen, *Exponential Motives*,
book in preparation. Draft PDF (public, author's site):
`http://javier.fresan.perso.math.cnrs.fr/expmot.pdf` (301 pp). **All page/eq
references below are to that PDF.** (The PDF was consulted during the session;
the third-party book file is **not** committed to the slot — only precise
page/equation locators are recorded here, per copyright hygiene.)

> **AEAL note — reference verification.** The task prompt and a web search each
> suggested an arXiv id (`2306.04269`, `1612.04872`). **Both are FALSE** — they
> resolve to unrelated papers. The authoritative source is the **book**, not an
> arXiv preprint. This matches the corpus warning about hallucinated FJ arXiv ids.
> Do **not** cite an arXiv number for Fresán–Jossen exponential motives.

---

## 2.1 What is an exponential motive `(X, f, ω)`?

- **Datum.** An *exponential motive* is built from a pair **`(X, f)`** — a
  "variety with a potential": **`X`** a smooth algebraic variety over a base
  field `k ⊆ ℂ`, and **`f : X → 𝔸¹`** a regular function (the *potential*).
  (Intro §1.1; the tannakian category `Mexp(k)` is built from such pairs,
  Intro §1.3.)
- **de Rham side.** `H^n_dR(X, f) = H^n(X, DR(E_f))`, the algebraic de Rham
  cohomology of the **twisted** connection `E_f = (O_X, d − df∧·)`. Concretely a
  class is represented by an algebraic `n`-form `ω` modulo the twisted
  differential `d_f ω = dω − df ∧ ω` (eq 1.1.2 region; for `X` affine, global
  algebraic forms).
- **Betti / rapid-decay side.** `H_n^{rd}(X, f)` — rapid-decay homology (§2.2).
- A *cohomology class of the exponential motive* is the pair
  `([ω] ∈ H^n_dR, [γ] ∈ H_n^{rd})`; the motive `M = H^n(X,f)` is the object
  packaging these two realisations plus the comparison between them.

## 2.2 Rapid-decay cycle `γ` — precise definition

**Definition 3.1.1.1 (pdf p.91).** For `r ∈ ℝ` let `S_r = { z ∈ ℂ : Re(z) ≥ r }`.
For a triple `[X, Y, f]` (`Y ⊆ X` closed, here `Y = ∅`),
```
  H_n^{rd}(X, f) = lim_{r → +∞}  H_n( X(ℂ),  f^{−1}(S_r);  ℚ ),
```
the limit over the transition maps from `f^{−1}(S_t) ⊆ f^{−1}(S_r)` (`t ≥ r`).

- **Concretely** a rapid-decay cycle is a compatible system `γ = (γ_r)` of
  (relative) singular `n`-chains whose boundary is pushed into `f^{−1}(S_r)`,
  i.e. the chain may be **unbounded only in directions where `Re(f) → +∞`**.
- **Finiteness (§3.1.2, pdf p.92):** by Ehresmann + resolution, for `r ≥ r_0`
  the transition maps are isomorphisms; `H_n^{rd}` and `H^n_{rd}` are
  finite-dimensional and mutually dual.
- **"Thimble" picture (Examples 1.1.4–1.1.5):** the basic rapid-decay cycles are
  *Lefschetz thimbles* / steepest-descent rays running to `∞` along the
  directions of fastest growth of `Re(f)`.

## 2.3 Period pairing and exponential periods

**Period pairing (eq 1.1.2.1).**
```
  H^n_dR(X, f)  ⊗  H_n^{rd}(X, f)  →  ℂ ,     [ω] ⊗ [γ]  ↦  ∫_γ e^{−f} ω .
```
- **Convergence is automatic** (this is the *point* of rapid decay): along the
  unbounded part of `γ` one has `Re(f) → +∞`, so `|e^{−f}| = e^{−Re f}` decays
  faster than any polynomial; the integral is **absolutely convergent**.
- **Sign convention (load-bearing for V_quad).** FJ use **`e^{−f}`**. The task
  writes `C = ∫_γ e^{+f} g dt`. These are the **same object** with
  **`f_task = − f_FJ`**; keep this flip explicit downstream.
- **Exponential period** = a value of this pairing when **`k ⊆ ℚ̄`** (the base
  field is algebraic over `ℚ`). Equivalently a period of an exponential motive
  over a number field (Intro §1.1, §1.3).

**Canonical examples (the V_quad-relevant ones).**
- **Ex. 1.1.4 (gamma / Gaussian).** `X = 𝔸¹`, `f = x^n` (`n ≥ 2`),
  `ω = x^{j−1}dx`, `γ =` thimble. Periods `= Γ(j/n)` (and `√π` for `n=2`).
  These generate the **gamma-motive** `M_n = H^1(𝔸¹, x^n)` (Intro §1.3.3).
- **Ex. 1.1.5 (Bessel — the structural template for V_quad).**
  `X = 𝔾_m`, `f = (z/2)(x − 1/x)`, forms `x^{−n−1}dx`, `x^{−n}dx`. The period
  satisfies the **Bessel** ODE `u'' + (1/z)u' + (1 − n²/z²)u = 0` — a **rank-2**
  connection with a **regular** singular point at `0` and an **irregular** point
  (Poincaré rank 1) at `∞`; the period matrix entries are the Bessel functions
  `J_n`, `H_n`. **This is exactly the [regular + irregular-rank-1] rank-2 shape of
  a Painlevé-V / V_quad linear problem.** *Caveat:* Bessel is **rigid**; V_quad is
  **non-rigid** (a transcendental accessory parameter), so it is at best a
  "Bessel-with-an-extra-modulus" analogue, not literally Ex. 1.1.5.

## 2.4 The conjecture (transcendence / algebraic independence)

**Conjecture 1.3.2 (Exponential period conjecture, cf. Conj. 8.2.6; pdf p.17).**
For an exponential motive `M` over a **number field**,
```
  trdeg_ℚ ⟨ periods of M ⟩  =  dim G_M ,
```
where `G_M ⊆ GL(R_B(M))` is the *motivic exponential Galois group* of `M` (the
tannakian group of `⟨M⟩^⊗`; Prop. 1.3.1). `dim G_M` is always an **upper bound**
for the transcendence degree (uncond.); equality is the conjecture. Instances:
Lindemann–Weierstrass (§12.1); Lang's gamma-value conjecture via the gamma-motive
`M_n`, with `0 → μ_n → G_{M_n} → S_{ℚ(μ_n)} → 0`, `dim G_{M_n} = 1 + φ(n)/2`
(Intro §1.3.4).

## 2.5 Auxiliary conditions that are **easy to miss** (the paper must verify)

These are the conditions a downstream V_quad paper must explicitly discharge; they
are precisely where a "looks like an exponential period" claim can silently fail.

1. **Algebraicity of the base field — `k ⊆ ℚ̄`.** The *only* way the integral is an
   *exponential period* (vs. an arbitrary transcendental integral) is that **`X`,
   `f`, and `ω` are all defined over a number field.** ⇐ **The load-bearing axiom
   for V_quad:** the Painlevé-V accessory parameter is *transcendental*
   (EBR-II §5), so any model carrying it as a coefficient is **not** over `ℚ̄`.
2. **Smoothness of `X`** (de Rham realisation as stated needs `X` smooth; the
   singular case is handled only via §7.1 with extra care).
3. **`f` a genuine regular function** with the right behaviour at infinity, so the
   nearby-fibre-at-infinity / `Perv_0` machinery (Ch. 2) applies; the critical
   locus of `f` controls the rank of `H_n^{rd}` (Ehresmann, §3.1.2).
4. **`ω` an algebraic de Rham class** for the *twisted* differential `d_f`, i.e.
   `ω` must represent a class in `H^n(X, DR(E_f))` — not merely be *some* form
   whose integral converges.
5. **Perfect comparison / dimension match.** `H^n_dR` and `H_n^{rd}` must have
   **equal (finite) dimension** and the period pairing be perfect (Ch. 7
   comparison isomorphism; the concrete instrument is **Hien's** rapid-decay
   pairing). A rank mismatch ⇒ no clean period matrix.
6. **Motive over a number field for the conjecture.** Conjecture 1.3.2 needs
   `M / number field` and an *identified* `G_M`; "differential Galois `= SL(2)`"
   is the **local** (Picard–Vessiot) group, **not** `G_M` — the two must not be
   conflated when invoking transcendence.

## 2.6 Is Fresán–Jossen the right target? (cross-check)

- **Yes, for the *definition* of "exponential period".** FJ is the standard
  modern framework and is exactly what the parent program (and the proven EBR cc3
  sibling) already targets.
- **The concrete *instrument* is Hien's rapid-decay pairing** (M. Hien,
  *Periods for flat algebraic connections*, Invent. Math. 178 (2009) 1–47,
  DOI 10.1007/s00222-009-0196-4) — FJ's `H_n^{rd}` is its homological packaging.
  EBR cc3 already used Hien directly. For V_quad the practical computation will be
  a Hien pairing, *interpreted* in the FJ motive framework.
- **Alternatives considered and why FJ stays primary:**
  - *Kontsevich–Zagier periods (extended/“exponential”):* the informal ℰ𝒫 ring;
    FJ is its motivic refinement — subsumed.
  - *Brown–Dupont* (single-valued / de Rham periods of `e^{−f}`): a *computational*
    layer **on top of** FJ; relevant for sub-problem C (single-valued
    realisation), not for the existence question A. Note.
  - *Belkale–Brosnan / Gelfand–Kapranov–Zelevinsky:* relevant only if the period
    turns out hypergeometric-rigid; V_quad is **non-rigid**, so GKZ-rigidity tools
    do **not** apply directly. Flag.
  - **Conclusion:** target = **Fresán–Jossen**, computed via **Hien**; keep
    Brown–Dupont in reserve for the single-valued/period-conjecture sub-problem.

---

### One-line summary
An exponential period is `∫_γ e^{−f} ω` for `X` smooth `/ℚ̄`, `f` regular,
`ω` an algebraic `d_f`-class, `γ ∈ H_n^{rd}` a rapid-decay (thimble) cycle; the
**`k ⊆ ℚ̄` algebraicity of `(X,f,ω)`** is the load-bearing, easy-to-miss axiom,
and Conjecture 1.3.2 (`trdeg = dim G_M`) is the transcendence payload.
