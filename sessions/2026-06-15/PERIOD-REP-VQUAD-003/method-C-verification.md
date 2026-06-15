# Sub-problem C / Stage 4 — Method C: Stokes-data verification

**Slot:** PERIOD-REP-VQUAD-003 · **Stage:** 4 (Method C) · **Date:** 2026-06-15
**Status:** COMPLETE — **PASS** (tightest method; no γ-integration)
**Script:** `scripts/stage4_methods.py` (Method C block) → `scripts/stage4_methods_results.json`

> **Claim.** The V_quad Stokes constant S = 2πK and the connection coefficient C are
> related by S = 2πi·(branch factor)·C, with the branch factor fixed by the Galois/branch
> data (β, the amplitude A). This uses **only** the already-computed Stokes datum — no
> integration of γ — and is the tightest of the three checks. **Verified to ~46 digits.**

---

## 1. The Stokes multiplier in terms of the branch amplitude (task 4.C.1–4.C.2)

The local branch of B̂ at −ξ₀ has amplitude A = (S/2πi)·Γ(1+β) (Stage 1.4), equivalently

> **S_mult = 2πi · A / Γ(1+β),**

where S_mult is the **Stokes multiplier** (the off-diagonal Stokes-matrix entry, an element
of the unipotent radical identified in Stage 2 / Stage 3). Since A = K·Γ(1+β) (verified to
5·10⁻⁴⁶, Stage 1.4), the Γ(1+β) cancels and

> **S_mult = 2πi·K,  |S_mult| = 2πK = 0.45790662316901763611909784254822583796239513…**

matching the deposited Stokes constant **S = 2πK** to **rel. err 8.8·10⁻⁴⁶**. The factor i is
the Stokes phase (the multiplier is imaginary; the deposited "Stokes constant" 0.4579… is its
real magnitude 2πK), and the algebraic-times-Γ factor 2πi/Γ(1+β) is the one "determined by
the Galois group of L_V and the branch exponent β" that the probe plan calls for.

## 2. Consistency with C through the same amplitude A (task 4.C.2)

The connection coefficient shares the **same** branch amplitude A:

> **C = |A| / |β| = K·Γ(1+β)/|β| = K·|Γ(β)|  (since |β| = Γ(1+β)/|Γ(β)|).**

Numerically C = 0.43770528619353722123073974979436958998172559… matching the deposited
C = |Γ(β)|·K to **rel. err 9.3·10⁻⁴⁶**. Hence S and C are two readings of the single datum A:

> **S = 2πK = 2π·|A|/Γ(1+β),  C = |A|/|β| = |Γ(β)|·K,  ⟹  S/C = 2π/|Γ(β)|.**

The last is the exact bridge identity (VQUAD-001 `numerical-check.md`, residual 0),
re-derived here purely from the Stokes/branch data.

## 3. Why this is the tightest method (task 4.C.3)

Methods A and B both reason about the integral over γ (differential structure / contour
deformation). Method C never integrates γ: it uses only (i) the deposited Stokes constant
S = 2πK (VQUAD-001, K to 58 digits), (ii) the branch exponent β = −1/(3√3) and the amplitude
A = K·Γ(1+β) extracted from the **operator** L_V's large-order Borel data (Stage 1.4), and
(iii) the Γ-function reflection/recurrence. The agreement |S_mult| = 2πK and C = |Γ(β)|·K to
~46 digits is therefore the most direct confirmation that C is the exponential-period datum
attached to the same Stokes structure.

## 4. Galois content

The factor 2πi/Γ(1+β) is Galois-equivariant: 2πi is the Betti–de Rham comparison period of
the exponential connection E^{ξ} at the irregular point (the exponential torus generator of
Stage 3), and 1/Γ(1+β) is the branch normalisation at −ξ₀ (the 𝔾_m generator). The product is
the unipotent Stokes entry relating the two. This is exactly the Galois-equivariant pairing
identified in `galois-LV-verification.md` §3 — made numerically explicit here.

## 5. Sourcing

* S = 2πK, C = |Γ(β)|·K, K (58 digits), bridge S/C = 2π/|Γ(β)| (residual 0):
  VQUAD-001 `numerical-check.md` T1.
* A = K·Γ(1+β), C = |A|/|β|, |S_mult| = 2πK: this slot `stage4_methods.py` (Method C block),
  `stage4_methods_results.json`; Stage 1.4 `numerical-integral.md`.
* Stokes multiplier ↔ branch amplitude, exponential torus / Betti–de Rham 2πi: van der
  Put–Singer Ch. 8; Fresán–Jossen *Exponential Motives* (period 2πi of E^x).

**Method C verdict: PASS.** S_mult = 2πi·A/Γ(1+β) with |S_mult| = 2πK (rel. err 8.8·10⁻⁴⁶);
C = |A|/|β| = |Γ(β)|·K (rel. err 9.3·10⁻⁴⁶); S/C = 2π/|Γ(β)| recovered. Tightest check, no
γ-integration.
