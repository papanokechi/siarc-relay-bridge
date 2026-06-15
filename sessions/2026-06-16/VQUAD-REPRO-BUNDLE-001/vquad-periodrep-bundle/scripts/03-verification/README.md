# 03 — Verification: three independent checks of the identity

The central identity $C=|\Gamma(\beta)|K$ is verified **three structurally
independent ways**, all agreeing to 46 digits. Independence is the point: the
three methods use different mathematics, so their agreement is strong evidence
the identity is not an artefact of any single computational pathway.

| Method | Mathematics | Script | Result (paper ref) |
|--------|-------------|--------|--------------------|
| **A** | Differential-equation / operator duality | `stage4a_methodA_v2.py` | $M=h(z)\cdot L_\varphi$ **exactly**; survives a 4-convention anti-fluke test (§5.1, §A.4). |
| **B** | Borel–Laplace contour deformation | `stage4_methods.py`, `stage1_hankel_period.py`* | Hankel period $\Rightarrow S\,e^{-\xi_0}$, rel. err. $8.84\times10^{-46}$ (§5.2). |
| **C** | Stokes-data / large-order | `stage4_methods.py` | $|S_{\mathrm{mult}}|=2\pi K$, $C=|A|/|\beta|$, rel. err. $9.31\times10^{-46}$ (§5.3). |

\* `stage1_hankel_period.py` lives in [`../04-cycle/`](../04-cycle/) (it also
defines the cycle); Method B's contour value is cross-checked there.

## Method A and the kernel convention

Method A is where the **Borel-sum kernel convention** matters. The corrected
script `stage4a_methodA_v2.py` uses the kernel $e^{-\xi/z}$ with the operator
duality $D_\xi\mapsto +1/z$, $\xi\mapsto +z^2 D_z$, giving the exact operator
factorisation

$$ M \;=\; h(z)\,L_\varphi,\qquad
   h(z)=\frac{27\,(649+30\sqrt3)}{418501\,z^2\,(2\sqrt3-3)} . $$

An earlier convention choice gave a spurious mismatch; the **4-convention
anti-fluke test** in this script enumerates the sign/kernel variants and
confirms only the $e^{-\xi/z}$ convention reproduces the exact factorisation.
This is documented in full in [`../../docs/CONVENTIONS.md`](../../docs/CONVENTIONS.md).
The `_v2` suffix marks the corrected script; the pre-correction version is not
shipped. The inline Method-A self-check inside `stage4_methods.py` (below) uses
the **same corrected $+1/z$ convention** in this bundle, so it independently
reports `methodA = True` / `all_three = True`.

## Scripts

| Script | Produces | Role |
|--------|----------|------|
| `stage4a_methodA_v2.py` | `stage4_methodA_results.json` | Method A (operator duality, 4-convention test). |
| `stage4_methods.py` | `stage4_methods_results.json` | Methods B and C (Borel–Laplace + Stokes-data), 46-digit agreement. |
| `numcheck_period_rep.py` | `numcheck_period_rep_results.json` | The bridge numerics $K,S,C,\beta,\xi_0$ and $C=|\Gamma(\beta)|K=|A|/|\beta|$ (§4–§5). Already uses a relative output path. |
| `stage0_residual_check.py` | `stage0_residual_results.json` | Operator residual sanity check (§2). Imports `q3_foundation`. |
| `q3_foundation.py` | — (support module) | The $\mathbb{Q}(\sqrt3)$ field + recognition machinery imported by `stage0_residual_check.py`. **Byte-identical** to `../01-algebraicity/holonomic_recognition_q3.py`; present here so this directory is self-contained. |

## How to run

```bash
cd scripts/03-verification
python numcheck_period_rep.py        # the headline constants + bridge identity
python stage4a_methodA_v2.py         # Method A
python stage4_methods.py             # Methods B and C
python stage0_residual_check.py      # residual sanity (imports q3_foundation)
```

Run **from this directory** so `stage0_residual_check.py` finds
`q3_foundation.py`. Each script writes its `*_results.json` next to itself;
compare against [`../../data/`](../../data/). Working precision is dps = 160–260;
the 46-digit agreements are stable well within that.
