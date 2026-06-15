# Stage 2 — V_quad structural data for the Fresán inquiry

**Chain:** FRESAN-JOSSEN-INQUIRY-001 · **Stage:** 2 · **Date:** 2026-06-15
**Sources:** PERIOD-REP-VQUAD-001/002/003 + VQUAD-PERIODREP-PAPER-001 §6.
Every datum below carries its parent-slot locator (AEAL).

---

## 1. The exponential-motive data `M = (X, f, ω, γ)`

| Object | Value | Source |
|---|---|---|
| **`X`** | `𝔸¹_ξ ∖ {0, −ξ₀}`, the affine line minus two points, with `ξ₀ = 2/√3` | PAPER §6; VQUAD-002 §4.0b |
| **`f`** | `f = −ξ` (linear potential; **no interior critical point**). FJ convention is `e^{−f}`, so `e^{−f}=e^{+ξ}` matches the paper's `∫_γ e^{ξ} B̂ dξ` | PAPER §6; FJ-axioms §2.3 |
| **`ω`** | `ω = B̂(ξ) dξ`, `B̂` the Borel transform of the V_quad asymptotic series (the holomorphic, exponent-0 local solution at `ξ=0`) | PAPER §6; VQUAD-003 §1 |
| **`γ`** | rapid-decay cycle detecting the branch at `−ξ₀`; a thimble running to `Re(ξ)→−∞` (= `Re(f)→+∞`) | PAPER §6; FJ-axioms §2.2 |
| **base field `k`** | **`ℚ(√3)`** exactly (`ξ₀=2/√3`, all `L_V`/`L_φ` coefficients over `ℚ(√3)`) | VQUAD-002 §4.0a/§4.0b |

**Period (the connection coefficient).**
`C = ⟨[γ]_rd, [ω]_dR⟩ = |Γ(β)|·K = |A|/|β|`, with the exact bridge to the Stokes
constant `S/C = 2π/|Γ(β)|` (residual 0; re-confirmed ~46 digits). Period matrix
`P(M) = [[1, 0], [1/Γ(1+β), 2πi]]`, `det = 2πi`. (PAPER §6 eq:periodmatrix; VQUAD-001
`numerical-check.md`.)

---

## 2. Differential Galois data (the de Rham / Picard–Vessiot side)

### 2a. `L_φ` (order 2, regular side) — **rigorously `SL(2,ℂ)`**
- `G(L_φ) = SL(2,ℂ)` over `ℚ(√3)(z)`, by **two agreeing methods**: Kovacic
  case-elimination (Cases 1,2,3 excluded → Case 4) **and** a structural
  trace-free + exponential-torus + Stokes generation argument.
- Source: VQUAD-003 `kovacic-verification.md` (HALT GATE 2 PASS; gap G-KOVACIC closed);
  matches the deposited V_quad paper's "SL(2) by exact Kovacic" (zenodo.20455090).
- **This identification is firm.**

### 2b. `L_V` (order 4, Borel/Laplace dual) — **structurally pinned, NOT single-named**
- `G_V ⊆ GL(4)` is identified **structurally** by its generators and their Zariski
  closures:
  - `ξ=0`: **apparent** (consecutive-integer exponents `{−1,0,1,2}`, meromorphic,
    trivial contribution);
  - `ξ=−ξ₀`: a **rank-1 torus `𝔾_m`** from the single **irrational** local exponent
    `−(1+β) = −1+√3/9` (monodromy eigenvalue `e^{2πi√3/9}`, **infinite order**);
  - `ξ=∞`: **exponential torus + formal monodromy + non-trivial Stokes** (slope-1
    irregular block), the **Borel-dual of `L_φ`'s `SL(2)`** structure; the Stokes
    constant `S=2πK≠0` lives here.
- So `G_V = ` Zariski-closure `⟨ 𝔾_m(−ξ₀), T_∞, Stokes_∞, formal-monodromy_∞ ⟩`:
  a reductive (`𝔾_m × T_∞`) × unipotent (Stokes) structure.
- Source: VQUAD-003 `galois-LV-verification.md` (two methods agree, residuals
  `1.6·10⁻⁴⁶`; HALT GATE 3 PASS).

### 2c. **STAGE 2.2 FLAG — `L_V` Galois identification is structural, not a single named group**
> `G_V` is **not** pinned to one finite-type algebraic-group label. A full
> Hrushovski-algorithm / `DifferentialGaloisGroup` run was **not available** (sympy-only
> environment, no Maple `DEtools`). The escape clause of HALT GATE 3 was invoked: the
> **Galois-equivariance of `C` is established directly** (the `−ξ₀`-branch monodromy
> factor `1−e^{2πi√3/9}≠0`, and the exact bridge `S/C=2π/|Γ(β)|`), which is what the
> period application needs — but a single-group identification of `G_V` was **not**
> attempted. (VQUAD-003 `galois-LV-verification.md` §2.5–§4.)
>
> **Consequence for the inquiry framing (per task STAGE 2.2):** ask the comparison
> question against **what is firmly known** — `G(L_φ)=SL(2)` (rigorous) and the
> **structural** description of `G_V` (`𝔾_m` from the irrational exponent + `SL(2)`-dual
> irregular block + non-trivial Stokes) — **not** against a claimed single-name `G_V`.
> The inquiry is framed as: *given this differential (Picard–Vessiot) data, does a
> monograph theorem identify or bound the **motivic** `G_M`?* This is honest and avoids
> overclaiming an `L_V` identification the corpus does not certify.

---

## 3. Numerical anchors (precision)

- `C`-bridge `S/C = 2π/|Γ(β)|`: residual **0** symbolically; re-confirmed to
  **~46 digits** (VQUAD-003 Stage 1.4). `L_V` exponent match residual `1.6·10⁻⁴⁶`.
- `K` deposited to 58 digits; `S=2πK=0.45790662…` (VQUAD-001; zenodo.20481592).
- `δ = log R_∞` Fredholm determinant verified to **65 digits** (zenodo.20624814) —
  context, not directly in the period pairing.

---

## 4. The branch exponent `β` (state both numbers, avoid the conflation)

- **Asymptotic-series branch parameter:** `β = −1/(3√3) = −0.192450…` (the `Γ(β)` in
  `C=|Γ(β)|·K`). (VQUAD-001.)
- **`L_V` local irrational exponent at `−ξ₀`:** `−(1+β) = −1 + √3/9 = −0.807550…`
  (the `𝔾_m`-generating monodromy `e^{2πi√3/9}`). (VQUAD-003 §1.)
- Both lie in `ℚ(√3)` (√3-irrational); both are over the number field `k=ℚ(√3)`.
  **Note:** the task brief's "branch exponent β = −1+√3/9" actually names `−(1+β)`,
  the `L_V` exponent — recorded here disambiguated so the email states it correctly.

---

## 5. The G-MOTGALOIS gap, stated precisely (what the inquiry resolves)

PAPER §6 invokes Conjecture 1.3.2 (`trdeg=dim G_M`) and then **assumes** the
differential Galois data of §2 above *represents the relevant quotient of* `G_mot(M)`
— i.e. that computing the Picard–Vessiot groups `SL(2)` / `G_V` controls `dim G_M`.
FJ-axioms §2.5 #6 flags exactly this Picard–Vessiot-vs-motivic conflation as the
easy-to-miss failure. The full Nori/Ayoub exponential-motive comparison for **this**
`M` is **not verified** in the corpus. The inquiry asks Fresán whether, for a genus-0,
linear-`f`, two-puncture, **non-rigid** motive of this exact shape, that comparison is
(a) a theorem, (b) covered by a known simplification (gamma/Bessel/L–W), or (c) still
the open conjecture — Frame C against Prop. 1.3.1 / Conj. 1.3.2 / Ex. 1.1.4–1.1.5.

---

### One-line summary
`M=(𝔸¹∖{0,−ξ₀}, f=−ξ, ω=B̂dξ, γ_rd)` over `k=ℚ(√3)`; `G(L_φ)=SL(2)` rigorous, `G_V`
**structural-only** (𝔾_m from `−1+√3/9` + `SL(2)`-dual irregular + Stokes `S=2πK`);
`C=|Γ(β)|K`, `β=−1/(3√3)`; period matrix `det=2πi`; the inquiry asks whether the
**differential** data licenses the **motivic** `G_M` of Conj. 1.3.2.
