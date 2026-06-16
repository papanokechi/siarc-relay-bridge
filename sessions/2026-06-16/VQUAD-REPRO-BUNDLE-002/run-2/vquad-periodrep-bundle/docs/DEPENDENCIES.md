# DEPENDENCIES

The bundle was produced and verified in the environment below. The numerical
results are not sensitive to minor version differences (the load-bearing exact
algebra is a hand-rolled $\mathbb{Q}(\sqrt3)$ field, not a CAS), but this is the
exact environment of record.

## Python

| Component | Version (of record) | Role |
|-----------|---------------------|------|
| CPython | **3.12.10** (Windows x64) | interpreter |
| `mpmath` | **1.3.0** | arbitrary-precision numerics; working precision `mp.dps = 160–260` for the period / Stokes checks (46-digit agreements are stable well within this) |
| `sympy` | **1.14.0** | symbolic cross-checks only; the exactness of the holonomic recognition does **not** depend on it |
| `numpy` | **2.4.4** | numeric root-finding of indicial polynomials only (`indicial_analysis.py`); exponents are confirmed exactly against the $\beta$-family predictions |

Standard-library modules used: `fractions` (the $\mathbb{Q}(\sqrt3)$ field is
built on `Fraction`), `json`, `os`, `sys`, `pathlib`, `cmath`, `itertools`.

### Install

```bash
python -m venv .venv
# Windows:  .venv\Scripts\activate     |   POSIX:  source .venv/bin/activate
pip install "mpmath==1.3.0" "sympy==1.14.0" "numpy==2.4.4"
```

Any Python 3.10+ with recent `mpmath`/`sympy`/`numpy` should reproduce the
numerical claims; the versions above are simply what was used.

## LaTeX (only needed to rebuild the PDF)

| Component | Version (of record) |
|-----------|---------------------|
| MiKTeX | **25.12** |
| `pdflatex` (MiKTeX-pdfTeX) | **4.23** |

Rebuild: `python paper/build.py`. The script concatenates `preamble.tex` with
the section sources and runs `pdflatex` **twice** (no `bibtex`/`latexmk`; the
bibliography is an inline `thebibliography`). For a **byte-identical** PDF the
preamble sets `\pdfinfoomitdate=1`, `\pdftrailerid{}`,
`\pdfsuppressptexinfo=-1`, and the build sets `SOURCE_DATE_EPOCH` to a fixed
value. A full TeX Live (2023+) with `pdflatex` also works for a visually
identical PDF, though the exact byte hash is only guaranteed under the recorded
MiKTeX build.

> Note: in this bundle, `paper/` ships the **assembled** `*.tex` and
> `preamble.tex` plus `build.py`. If you rebuild and your TeX distribution lays
> out fonts/timestamps differently, the PDF will be visually identical but may
> differ in byte hash; the recorded target hash is reproducible under the
> environment of record.

## Optional (not required, not shipped)

- **Maple** `DEtools[DifferentialGaloisGroup]` independently reproduces the
  $\mathrm{SL}_2(\mathbb{C})$ verdict for $L_\varphi$. The Kovacic
  case-elimination in §A.2 is self-contained and does not need it.

## Operating system notes

- Developed and verified on **Windows 11 (x64)**. All scripts are
  OS-independent: every output path is resolved relative to the script's own
  location via `os.path.dirname(os.path.abspath(__file__))` (or `pathlib`), so
  the scripts run unchanged on Linux/macOS.
- Run each script **from its own directory** (`cd scripts/0X-...`) so that
  intra-directory imports resolve via the script-directory entry that Python
  places on `sys.path`.
- No network access is required at runtime.
