# 01 — Algebraicity: holonomic recognition over ℚ(√3)

This stage establishes that the Borel transform of the $V_{\mathrm{quad}}$
asymptotic series is **holonomic with coefficients in the real quadratic field
$\mathbb{Q}(\sqrt3)$**, and extracts the two differential operators the rest of
the paper uses:

- $L_\varphi$ — order 2, polynomial degree 4 — annihilates the asymptotic
  series $\varphi$;
- $L_V$ — order 4, polynomial degree 2 — annihilates the Borel transform
  $\widehat B$.

## Approach

The load-bearing computation is **exact**, not floating point. A hand-rolled
$\mathbb{Q}(\sqrt3)$ field class (`Q3`, pairs $p+q\sqrt3$ of `fractions.Fraction`)
in `holonomic_recognition_q3.py` performs a rational-kernel search over ansätze
of bounded order $r$ and degree $d$ for an operator that annihilates the
coefficient stream exactly (residual identically $0$ in $\mathbb{Q}(\sqrt3)$).
Because the field arithmetic is exact, the holonomicity claim does **not** rely
on any computer-algebra system. A Borel–Padé census (`borel_pade_census.py`)
then locates the dominant Borel singularity and rules out an infinite resurgent
tower.

## Scripts (run order matters — later scripts import earlier ones)

| # | Script | Produces | What it shows (paper ref) |
|---|--------|----------|---------------------------|
| 1 | `holonomic_recognition_q3.py` | `holonomic_recognition_q3_results.json` | Exact $a_n,b_m\in\mathbb{Q}(\sqrt3)$; an order-4 holonomic ODE is **found** (§2, eq. coeffstream). Run this **first**. |
| 2 | `extract_verify_operators.py` | `operator_verification_results.json` | Re-derives and verifies $L_\varphi$, $L_V$; confirms coefficient field $=\mathbb{Q}(\sqrt3)$; operator residual $0$ (§2). |
| 3 | `indicial_analysis.py` | `indicial_results.json` (+ console) | Singular locus $\{0,-\xi_0,\infty\}$; local exponents at $0$; the branch exponent $-(1+\beta)$ at $-\xi_0$ (§2, prop. exponents). |
| 4 | `borel_pade_census.py` | `borel_pade_results.json` | Dominant Borel singularity on the negative axis at $-\xi_0$; order-4 holonomicity ⇒ **finite** resurgence (§5.3). |

`extract_verify_operators.py`, `indicial_analysis.py` and `borel_pade_census.py`
all `import holonomic_recognition_q3`; scripts 3 and 4 also import
`extract_verify_operators`. They therefore must stay co-located in this
directory (they are). Run each script **from this directory** so the sibling
imports resolve.

## How to run

```bash
cd scripts/01-algebraicity
python holonomic_recognition_q3.py     # ~3–4 min: the ansatz search
python extract_verify_operators.py     # < 1 min
python indicial_analysis.py            # < 1 min
python borel_pade_census.py            # < 1 min
```

Each script writes its `*_results.json` **next to itself**. Compare against the
reference copies in [`../../data/`](../../data/) — they should match.

> Note: `holonomic_recognition_q3.py` is byte-identical to
> `../03-verification/q3_foundation.py`. The duplicate is intentional: the
> module is needed as an importable dependency in **both** directories so each
> can be run standalone.
