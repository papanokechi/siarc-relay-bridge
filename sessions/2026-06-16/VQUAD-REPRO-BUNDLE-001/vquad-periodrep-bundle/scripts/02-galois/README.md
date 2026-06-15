# 02 — Galois: Kovacic for L_φ, and the L_V Galois structure

This stage determines the differential Galois groups.

- **$L_\varphi$ (order 2):** its differential Galois group is
  $\mathrm{SL}_2(\mathbb{C})$, proved by **Kovacic's algorithm** via
  case-elimination (no Liouvillian solution exists in Cases 1–3, so the group
  is all of $\mathrm{SL}_2$). This is the firm, load-bearing Galois result of
  the paper (§2, thm. galois; §A.2).
- **$L_V$ (order 4):** a **structural** identification of the Galois group
  (a $\mathbb{G}_m$ times a Stokes structure), used to frame the Fresán–Jossen
  application in §6. This identification is structural rather than a complete
  Picard–Vessiot computation; the paper is explicit about that scope, and the
  open motivic-comparison question is exactly what the Fresán inquiry targets.

## Scripts (standalone — no cross-imports)

| Script | Produces | What it shows (paper ref) |
|--------|----------|---------------------------|
| `stage2_kovacic.py` | console (stdout) | Kovacic case-elimination for $L_\varphi$ ⇒ $\mathrm{SL}_2(\mathbb{C})$ (§2, §A.2). |
| `stage2b_symsquare.py` | `stage2_kovacic_results.json` | Symmetric-square / invariant test backing the case-elimination certificate. |
| `stage3_galois_LV.py` | `stage3_galois_LV_results.json` | Structural Galois data for $L_V$ ($\mathbb{G}_m$ × Stokes structure) (§6). |
| `stage3b_frobenius_v2.py` | `stage3b_frobenius_results.json` | Frobenius solution at $-\xi_0$: **no logarithms**, residual $1.6\times10^{-46}$ (§A.3). Confirms the branch exponent $-(1+\beta)$ is non-resonant. |

Each script is self-contained (only `sympy`/`mpmath`/`json`) and may be run in
any order, **from this directory**:

```bash
cd scripts/02-galois
python stage2_kovacic.py
python stage2b_symsquare.py
python stage3_galois_LV.py
python stage3b_frobenius_v2.py
```

Outputs are written next to each script; compare against
[`../../data/`](../../data/).

> An optional independent cross-check (not required, not shipped) is Maple's
> `DEtools[DifferentialGaloisGroup]`, which reproduces the $\mathrm{SL}_2$
> verdict for $L_\varphi$. The case-elimination argument in §A.2 is
> self-contained and does not depend on it.

> `stage3b_frobenius_v2.py` is the corrected (v2) Frobenius script; the
> superseded v1 is intentionally **not** included in this bundle.
