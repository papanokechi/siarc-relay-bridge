# Stage 1 — Fresán–Jossen monograph mapping (sections to cite in the inquiry)

**Chain:** FRESAN-JOSSEN-INQUIRY-001 · **Stage:** 1 · **Date:** 2026-06-15

**Reference (verified).** Javier Fresán & Peter Jossen, *Exponential Motives*,
book in preparation. Draft PDF (author's CNRS page):
`http://javier.fresan.perso.math.cnrs.fr/expmot.pdf` (301 pp). **All page/§/eq
references below are to that PDF.** Locators are transcribed from the AEAL-verified
summary in `PERIOD-REP-VQUAD-001/fresan-jossen-axioms.md` (which consulted the PDF
directly); the third-party book file is not held in-corpus, only precise locators.

> **AEAL warning (do not regress).** Do **not** cite an arXiv id for Fresán–Jossen
> exponential motives. `arXiv:2306.04269` and `arXiv:1612.04872` are FALSE (unrelated
> papers). The authoritative source is the **book**. The inquiry email must reference
> the **monograph by section/page**, never an arXiv number.

---

## A. The three section clusters the inquiry must cite

### A1. Definition of the motivic (exponential) Galois group `G_M`
- **Prop. 1.3.1** — `G_M ⊆ GL(R_B(M))` is the **Tannakian group of `⟨M⟩^⊗`**
  (the motivic exponential Galois group of `M`), built inside the tannakian
  category `Mexp(k)`.
- **Intro §1.3** — construction of `Mexp(k)` from pairs `(X, f)`; `R_B` the Betti
  (rapid-decay) fibre functor.
- *Why cited:* this is the object the paper's §6 must compare its **differential**
  Galois data against. The inquiry's whole subject is "does the differential datum
  compute `G_M`?"

### A2. The comparison / period conjecture
- **Conjecture 1.3.2** (Exponential period conjecture; **cf. Conj. 8.2.6**;
  **pdf p.17**):
  ```
  trdeg_ℚ ⟨ periods of M ⟩  =  dim G_M       (M over a number field).
  ```
- **`dim G_M` is an unconditional UPPER BOUND** for the transcendence degree;
  equality is the conjecture. (Intro §1.3 / Conj. 1.3.2 surrounding text.)
- *Why cited:* the paper's §6 transcendence statement is *conditional on this
  conjecture* AND on identifying `G_M`. Framing the question against Conj. 1.3.2
  (not against "is C transcendental?") is the Frame-C move.

### A3. The local-vs-global Galois distinction (the actual gap)
- **Auxiliary condition #6** (transcribed in `fresan-jossen-axioms.md` §2.5, sourced
  to Conj. 1.3.2 / Prop. 1.3.1 hypotheses): *"differential Galois `= SL(2)` is the
  **local (Picard–Vessiot)** group, **not** `G_M` — the two must not be conflated
  when invoking transcendence."*
- *Why cited:* **this is the G-MOTGALOIS gap verbatim.** The paper computes
  Picard–Vessiot groups (`SL(2)` for `L_φ`; a structurally-pinned `G_V ⊆ GL(4)` for
  `L_V`) and *assumes* they represent `G_M`. FJ flag exactly this conflation as the
  easy-to-miss failure point. The inquiry asks whether, for this **specific** motive,
  the conflation is in fact licensed (a theorem) or remains a genuine assumption.

---

## B. Known-simplification cases to name (the Frame-C "does theorem Y apply?")

The inquiry asks whether V_quad's motive falls into a class where `G_M` is already
controlled. Candidates, in monograph order:

| Case | Locator | Structure | Relevance to V_quad |
|---|---|---|---|
| **Gamma-motive `M_n`** | **Ex. 1.1.4**; **Intro §1.3.3–§1.3.4** | `X=𝔸¹`, `f=xⁿ`, periods `Γ(j/n)`; `0→μ_n→G_{M_n}→S_{ℚ(μ_n)}→0`, `dim G_{M_n}=1+φ(n)/2` | `C` involves `Γ(β)`; the V_quad period matrix has a `1/Γ(1+β)` entry. The gamma-motive is the closest case where `G_M` is **explicitly computed**. Does an analogous exact sequence pin `G_M` here? |
| **Bessel motive** | **Ex. 1.1.5** | `X=𝔾_m`, `f=(z/2)(x−1/x)`; **rank-2, regular at 0 + irregular Poincaré-rank-1 at ∞**; periods `J_n, H_n` | This is the **structural template** for a Painlevé-V/`L_φ` linear problem: exactly the [regular + irregular-rank-1] rank-2 shape. **Caveat: Bessel is rigid; V_quad is non-rigid** (transcendental accessory parameter). Does the `G_M` control for Ex. 1.1.5 survive the loss of rigidity? |
| **Lindemann–Weierstrass** | **§12.1** | Exponential periods of `0`-dimensional / linear-`f` motives | Precedent that linear potentials `f` give controllable `G_M`; V_quad's `f` is **linear** (`f=−ξ`), so this is the relevant flavour. |

These three are the theorems to phrase the question against: *"Does the `G_M`
computation of Ex. 1.1.4 / Ex. 1.1.5 / §12.1 extend to a genus-0, linear-`f`,
two-puncture motive with one irrational local exponent and a rank-1 irregular point?"*

---

## C. Supporting locators (background, cite only if needed)

- **Exponential motive `(X,f,ω)` definition:** Intro §1.1, §1.3; twisted connection
  `E_f=(O_X, d−df∧·)`, de Rham class `ω` mod `d_f` (eq 1.1.2 region).
- **Rapid-decay homology `H_n^{rd}`:** **Definition 3.1.1.1 (pdf p.91)**; finiteness
  / duality **§3.1.2 (pdf p.92)**.
- **Period pairing `∫_γ e^{−f} ω`:** **eq 1.1.2.1**. *FJ sign convention is `e^{−f}`*;
  the V_quad paper writes `e^{+ξ}`, so `f_FJ = −ξ` (= the paper's potential up to sign).
- **Concrete instrument:** **Hien**, *Periods for flat algebraic connections*,
  Invent. Math. **178** (2009) 1–47, DOI `10.1007/s00222-009-0196-4` — FJ's `H_n^{rd}`
  is its homological packaging; the V_quad pairing is a Hien pairing read in FJ terms.

---

## D. What NOT to claim in the email (AEAL guardrails)

1. Do not assert the comparison **holds**; ask whether a **named theorem applies**.
2. Do not cite an **arXiv id** for FJ (see warning above) — cite the **book** + §.
3. Do not claim V_quad **is** Ex. 1.1.5 — it is a **non-rigid** analogue (extra
   transcendental modulus); state the analogy with the rigidity caveat.
4. Do not claim `G_M` is **known**; the paper's `dim G_M` is at best the unconditional
   **upper bound** of Conj. 1.3.2 until Fresán confirms a stronger statement.

---

### One-line summary
The inquiry cites **Prop. 1.3.1** (`G_M`), **Conjecture 1.3.2 / p.17** (comparison),
and the **local-vs-global caveat** (FJ-axioms §2.5 #6), then asks whether the
`G_M`-control of **Ex. 1.1.4 (gamma)**, **Ex. 1.1.5 (Bessel)**, or **§12.1
(Lindemann–Weierstrass)** extends to V_quad's genus-0, linear-`f`, non-rigid motive.
