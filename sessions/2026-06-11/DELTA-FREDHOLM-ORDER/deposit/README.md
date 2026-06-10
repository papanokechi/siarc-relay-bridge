# Deposit: A Fredholm-determinant representation of the pcf-delta growth constant

**Author:** Papanokechi (ORCID 0009-0000-6192-8273) · **License:** CC BY 4.0 (text) / MIT (code)
**Session:** DELTA-FREDHOLM-ORDER · **Date:** 2026-06-11

> **READY-STATE — NOT UPLOADED, NOT COMMITTED.** This `deposit/` directory is assembled to
> ready-state for operator review. The actual Zenodo upload and any git commit are
> **operator-gated, irreversible actions** and have **not** been performed by this session.
> See *Operator steps* at the bottom.

---

## 1. Abstract

Let $b(k)=Ak^2+Bk+C$ be a positive quadratic and $u_n=1/(b(n-1)b(n))$ for $n\ge2$. The pcf-delta
growth constant of the running family $(A,B,C)=(1,0,1)$ is $\delta=\log R_\infty(1)$, where
$R_\infty(\lambda)$ is the weighted independence (sparse-subset) polynomial of the half-infinite path
with vertex weight $\lambda u_i$. The note gives a self-contained account of the Fredholm-determinant
representation $\delta=\tfrac12\log\det(I+T^2)$ ($T$ the edge-weighted path operator, off-diagonal
$\sqrt{u_{j+1}}$). Two finite identities are machine-checked in Lean 4 / Mathlib; the Fredholm
representation is confirmed to 65 digits by two independent channels (conjectural as a theorem); and the
entire function $R_\infty$ is determined to have **order $\rho=1/(2d)=1/4$** and **genus $0$**.

## 2. Verdict and four-class summary

| Item | Class | Where |
|---|---|---|
| **Theorem 1** $\det A_M=c_M$ | **PROVEN** (Lean, clean cone) | `lean/PcfFredholm/Core.lean` (`T_DET`) |
| **Theorem 2** $c_M=R_M$ | **PROVEN** (Lean, clean cone) | `lean/PcfFredholm/Core.lean` (`T_COMB`) |
| Prop 3 determinant factorisation | STRUCTURAL | note §3 |
| Theorem 4 trace-class (uniform $S\le1/6$ on integer family; conditional for general real $b$) | STRUCTURAL + VERIFIED | note §3, `phaseA/thm4_S.py` |
| Theorem 5 two-channel $\delta_A=\delta_B$ (65 digits) | VERIFIED | `p0/` |
| Conjecture 6 exact Fredholm identity | CONJECTURED | note §4 |
| **Prop 7 order $\rho=1/(2d)=1/4$, genus $0$** | STRUCTURAL bracket + VERIFIED sharp value | note §5, `phaseA/` |

**PROVEN is reserved for the two Lean theorems only.** The order/genus result is the headline of this
session: the draft's "order $\le1/(2d)$, genus $0$" is **correct and upgraded to the equality**
$\rho=1/(2d)$, with the Hadamard product $R_\infty^2=\prod_k(1+\lambda s_k^2)$ written exponential-factor-free.

## 3. File manifest

```
deposit/
  README.md                     this file
  delta_fredholm_note.md        corrected manuscript (canonical source)
  delta_fredholm_note.tex       generated LaTeX (pandoc + theorems.lua + preamble.tex)
  delta_fredholm_note.pdf       compiled PDF (5 pp, 0 undefined refs)
  preamble.tex, theorems.lua    LaTeX preamble + pandoc div->amsthm filter (build inputs)
  zenodo_metadata.json          Zenodo metadata draft (DOIs flagged for operator)
  claims.jsonl                  this session's claims (Phase-A computations + build), sha256 hashes
  LICENSE-TEXT                  CC BY 4.0 (manuscript/prose/data)
  LICENSE-CODE                  MIT (Lean + Python source)

  lean/                         COPY of the LEAN-CORE project (Theorems 1-2 PROVEN, clean cone)
    PcfFredholm/Core.lean, PcfFredholm.lean, SCOPE.md, README.md,
    lake-manifest.json, lakefile.toml, lean-toolchain, claims.jsonl
  p0/                           COPY of the DELTA-FREDHOLM-P0 numerics (delta to 65 digits)
    t0_convention_lock.py, t2_spectral_channel.py, t2_trace_channel.py,
    t4_pslq_probe.py, assemble_results.py, write_claims.py,
    results.json, claims.jsonl, README.md, out/
  phaseA/                       THIS session's order/genus computations
    ORDER_VERDICT.md            A4 verdict (order/genus + corrected Prop 5 text + S<1 + edit flags)
    order_coefficients.py       coefficient-route order (dps 220)
    eigenvalue_route.py         eigenvalue-route convergence exponent + genus
    thm4_S.py                   S telescoping bound + integer-grid scan (125 triples, uniform S<=1/6)
    out/                        result JSONs (sha256 in claims.jsonl)
```

## 4. Build and reproduce

**Manuscript PDF** (toolchain: pandoc + MiKTeX pdflatex):
```sh
pandoc delta_fredholm_note.md -s --lua-filter=theorems.lua -H preamble.tex \
       -V geometry:margin=1in -o delta_fredholm_note.tex
pdflatex delta_fredholm_note.tex   # x3 for cross-references
```
Clean 3-pass build: 5 pages, 0 undefined references, 0 warnings, 0 overfull hboxes > 50pt.
(The PDF embeds a build timestamp, so it is a fixity hash, not bit-reproducible.)

**Lean theorems 1-2** (pinned: `leanprover/lean4:v4.30.0`, Mathlib `v4.30.0`,
`lake-manifest.json` rev `c5ea00351c28e24afc9f0f84379aa41082b1188f`):
```sh
cd lean && lake exe cache get && lake build      # prints the axiom cones
```
Audit: both `T_DET` and `T_COMB` depend only on `{propext, Classical.choice, Quot.sound}`, no `sorryAx`.

**Phase-A numerics** (Python: mpmath 1.3.0, numpy 2.4.4, scipy 1.17.1):
```sh
cd phaseA && python order_coefficients.py && python eigenvalue_route.py && python thm4_S.py
```
Each writes `out/<name>_result.json` (LF newlines); `sha256sum` matches the `output_hash` in `claims.jsonl`.

**P0 two-channel numerics** (dps as CLI arg):
```sh
cd p0 && python t2_trace_channel.py 120 58 && python t2_spectral_channel.py 120 && python t0_convention_lock.py 120
```

## 5. References / DOIs (operator to confirm)

The manuscript References and `zenodo_metadata.json` carry **placeholder DOIs**
`10.5281/zenodo.XXXXXXXX` for: the pcf-delta concept record (`isContinuationOf`), and the
growth-law / EBR / ladder deposits (`references`). **These must be filled in by the operator before
upload** — this session did not resolve them.

## 6. Predeposit hygiene (B2) — self-check results

- **Overclaim scan:** PASS. "PROVEN" appears only on the two Lean theorems and their cone; rigorous
  by-hand bounds are graded STRUCTURAL; "VERIFIED" only on numerics; Conjecture 6 and O1–O3 are not
  asserted as results.
- **Four-class partition:** present in the status block and inline on every theorem/proposition.
- **PROVEN ↔ Lean cone:** exact match — Theorems 1 and 2 only (not Prop 3, not Theorem 4).
- **Stale surface language (PIII(D6)/D5/Painlevé/transcendent):** none (scanned; this note carries none).
- **DOIs:** 4 placeholders flagged above for operator resolution.

## 7. Operator steps (the only remaining actions — all manual, all operator-gated)

1. **Review** `delta_fredholm_note.pdf` and `phaseA/ORDER_VERDICT.md`.
2. **Resolve the placeholder DOIs** in `zenodo_metadata.json` and the manuscript References (§5 above).
3. **Create the Zenodo deposit**, upload the contents of `deposit/`, and set metadata from
   `zenodo_metadata.json`.
4. **Mint the version DOI** and add it back to the record.
5. **Hand-copy** this session folder to the bridge path
   `sessions/2026-06-11/DELTA-FREDHOLM-ORDER/` and **commit** by hand.

> This session performed **no** network upload, **no** Zenodo account action, and **no** git commit.
> Steps 3–5 are irreversible and are reserved for the operator.
