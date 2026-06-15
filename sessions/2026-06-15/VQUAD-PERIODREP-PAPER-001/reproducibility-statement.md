# Reproducibility statement (Stage 5; mirrors paper §A.5)

Every computational claim in the paper is reproducible from open scripts in the
SIARC relay-bridge probe slots that produced this result. No proprietary
software is required.

## Probe slots (source of all computational claims)

| Slot | Role | BRIDGE URL |
|------|------|------------|
| PERIOD-REP-VQUAD-001 | Scoping: K/S/C/β/ξ₀ numerics, bridge identity, Fresán–Jossen axioms | https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-06-15/PERIOD-REP-VQUAD-001/ |
| PERIOD-REP-VQUAD-002 | Exact holonomic recognition over ℚ(√3); L_φ/L_V; indicial/exponents; finite resurgence | https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-06-15/PERIOD-REP-VQUAD-002/ |
| PERIOD-REP-VQUAD-003 | Cycle γ; rapid-decay; three verifications (Methods A/B/C); FJ application; Kovacic/Galois | https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-06-15/PERIOD-REP-VQUAD-003/ |
| VQUAD-PERIODREP-PAPER-001 | This paper draft (LaTeX source, build script) | https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-06-15/VQUAD-PERIODREP-PAPER-001/ |

## Parent deposits (read-only; not modified by this work)

- V_quad companion paper — Zenodo **10.5281/zenodo.20455090** (concept 10.5281/zenodo.20455089).
  Source of the V_quad PCF, the PV/D₅⁽¹⁾ identification, θ_∞, α.
- S = 2πK Stokes calibration — Zenodo **10.5281/zenodo.20481592**.
- δ Fredholm-determinant cross-check (context) — Zenodo 10.5281/zenodo.20624814.
- Sakai-stratification parent program — concept DOI **to be inserted by the
  operator at submission time** (not yet known in the corpus; see self-review item 3).

## Key scripts (by claim)

| Claim in paper | Script (slot) | Output |
|----------------|---------------|--------|
| a_n, b_m exact in ℚ(√3) (§2 eq:coeffstream) | `holonomic_recognition_q3.py` (002) | `holonomic_recognition_q3_results.json` |
| L_φ (ord 2, deg 4), L_V (ord 4, deg 2) exact; residual 0 (§2) | `extract_verify_operators.py`, `holonomic_recognition_q3.py` (002) | `operator_verification_results.json` |
| Singular locus {0, −ξ₀, ∞}; local exponents; branch −(1+β) (§2 prop:exponents) | `indicial_analysis.py` (002) | console + `operator_verification_results.json` |
| Frobenius solution at −ξ₀, no logs, residual 1.6e-46 (§A.3) | `stage3b_frobenius_v2.py` (003) | — |
| Kovacic SL₂(ℂ) by case-elimination (§2 thm:galois, §A.2) | `stage2_kovacic.py`, `stage2b_symsquare.py` (003) | `kovacic-verification.md` |
| Method A: M = h(z)·L_φ exact; 4-convention test (§5.1, §A.4) | `stage4a_methodA_v2.py` (003) | `stage4_methodA_results.json` |
| Method B: Hankel ⇒ S·e^{−ξ₀}, rel err 8.84e-46 (§5.2) | `stage4_methods.py`, `stage1_hankel_period.py` (003) | `stage4_methods_results.json` |
| Method C: |S_mult| = 2πK, C = |A|/|β|, rel err 9.31e-46 (§5.3) | `stage4_methods.py` (003) | `stage4_methods_results.json` |
| Large-order amplitude A extraction (§5.3) | `borel_pade_census.py` (002) | — |
| Operator residual sanity (§2) | `stage0_residual_check.py` (003) | — |

## Computational environment

- **Python** 3.12.10 (CPython, Windows x64).
- **mpmath** 1.3.0 — high-precision numerics; working precision dps = 160–260
  for the period/Stokes checks (46-digit agreements are stable well within this).
- **sympy** 1.14.0 — used as a cross-check; the load-bearing exact algebra is a
  hand-rolled ℚ(√3) field class (`Q3`, Fraction pairs p+q√3) in
  `holonomic_recognition_q3.py`, so the exactness does not depend on a CAS.
- **numpy** — only for numeric root-finding of indicial polynomials
  (`indicial_analysis.py`); exponents are confirmed exactly against the
  β-family predictions.
- Optional cross-check: **Maple** `DEtools[DifferentialGaloisGroup]` reproduces
  the Kovacic verdict; not required (open case-elimination + structural argument
  given in §A.2).

## Determinism / byte-reproducibility of the PDF

- LaTeX: **MiKTeX 25.12**, `pdflatex` run twice (no bibtex/latexmk; the
  bibliography is an inline `thebibliography`).
- Reproducible-output guards in the preamble: `\pdfinfoomitdate=1`,
  `\pdftrailerid{}`, `\pdfsuppressptexinfo=-1`; the build script sets
  `SOURCE_DATE_EPOCH` to a fixed value, so repeated builds from a clean tree
  produce a byte-identical PDF.
- Build entry point: `latex/build.py` (concatenates `preamble.tex` +
  `sections/section-{1..8}.md` + `section-9-references.md` + `\end{document}`,
  compiles, and reports PAGES / ERRORS / undefined refs).

## Exact constants (as certified; §A.3)

```
K   = 0.0728781025518669641294423633296525128045556892…   (58 digits)
S   = 2πK = 0.457906623169017636119097842548225837962395135…
β   = −1/(3√3) = −0.19245008972987525…
ξ₀  = 2/√3 = 1.1547005383792517…
C   = |Γ(β)|·K = 0.437705286193537221230739749794369589981725597…
−(1+β) = −1 + √3/9 = −0.80754991027…   (branch exponent)
bridge:  S/C = 2π/|Γ(β)|   (residual 0, exact)
```
