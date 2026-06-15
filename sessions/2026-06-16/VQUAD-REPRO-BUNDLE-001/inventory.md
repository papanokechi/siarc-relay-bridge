# Stage 1 — Reproducibility artifact inventory

**Chain:** VQUAD-REPRO-BUNDLE-001 · **Date:** 2026-06-16
**Bundle target:** `vquad-periodrep-bundle/`

> **PREREQUISITE NOTE (read first).** Two stated prerequisites are **not yet met**:
> `VQUAD-PAPER-CORRECTIONS-001` does **not exist** (repo HEAD is `f3dd3a4`, the paper-draft
> commit; no corrections cycle has run) and the **cold-read verdict is not recorded**
> (`VQUAD-REVIEW-PREP-001` holds only the cold-read *framework*). The Fresán inquiry is
> **confirmed-pending** (drafted/HELD, `FRESAN-JOSSEN-INQUIRY-001`). This bundle is therefore
> assembled against the **current byte-reproducible paper draft** (23 pp, PDF 698 730 bytes,
> SHA-256 `359D1172…`) as a **ready-state HELD** deliverable. If the cold-read + corrections
> cycle changes the paper text, `paper/` and the PDF SHA must be refreshed before deposit.
> See `prerequisite-check.md`.

---

## 1. Source slots (BRIDGE-linked, copied-from, never modified)

| Slot | Role |
|---|---|
| PERIOD-REP-VQUAD-001 | Scoping: K/S/C/β/ξ₀ numerics, bridge identity, FJ axioms |
| PERIOD-REP-VQUAD-002 | Exact holonomic recognition over ℚ(√3); L_φ/L_V; indicial; finite resurgence |
| PERIOD-REP-VQUAD-003 | Cycle γ; rapid-decay; Methods A/B/C; Kovacic/Galois; FJ application |
| VQUAD-PERIODREP-PAPER-001 | Paper LaTeX source, build.py, sections, claims |
| VQUAD-PAPER-CORRECTIONS-001 | **ABSENT** — does not exist yet (prerequisite gap) |

Authoritative claim→script map: `VQUAD-PERIODREP-PAPER-001/reproducibility-statement.md`.

---

## 2. ESSENTIAL scripts (produce claims cited in the paper) → bundled

| Bundle dir | Script (origin slot) | Produces (cited claim) | Output JSON |
|---|---|---|---|
| 01-algebraicity | `holonomic_recognition_q3.py` (002) | ℚ(√3) field class; a_n,b_m exact; L_φ/L_V (§2) | holonomic_recognition_q3_results.json |
| 01-algebraicity | `extract_verify_operators.py` (002) | L_φ (ord 2 deg 4), L_V (ord 4 deg 2) exact, residual 0 (§2) | operator_verification_results.json |
| 01-algebraicity | `indicial_analysis.py` (002) | Singular locus {0,−ξ₀,∞}; exponents; branch −(1+β) (§2 prop:exponents) | indicial_results.json |
| 01-algebraicity | `borel_pade_census.py` (002) | Large-order amplitude A (§5.3) | borel_pade_results.json |
| 02-galois | `stage2_kovacic.py` (003) | Kovacic case-elimination ⇒ SL₂(ℂ) (§2 thm:galois, §A.2) | (stdout verdict) |
| 02-galois | `stage2b_symsquare.py` (003) | Case-2 symmetric-square exclusion (§A.2) | stage2_kovacic_results.json |
| 02-galois | `stage3_galois_LV.py` (003) | G_V structure: 𝔾_m(−ξ₀) + irregular/Stokes (§2, §A) | stage3_galois_LV_results.json |
| 02-galois | `stage3b_frobenius_v2.py` (003) | Frobenius soln at −ξ₀, no logs, residual 1.6e-46 (§A.3) | stage3b_frobenius_results.json |
| 03-verification | `stage4a_methodA_v2.py` (003) | Method A: M=h(z)·L_φ exact; 4-convention test (§5.1, §A.4) | stage4_methodA_results.json |
| 03-verification | `stage4_methods.py` (003) | Method B (Hankel⇒S·e^{−ξ₀}) & Method C (\|S_mult\|=2πK) (§5.2–5.3) | stage4_methods_results.json |
| 03-verification | `numcheck_period_rep.py` (001) | 46-digit numerics; C=\|Γ(β)\|·K; bridge S/C=2π/\|Γ(β)\| (§1,§5) | numcheck_period_rep_results.json |
| 03-verification | `stage0_residual_check.py` (003) | Operator residual sanity for L_V (§2) | stage0_residual_results.json |
| 03-verification | `q3_foundation.py` (003) | **SUPPORT module** imported by stage0_residual_check (byte-identical to holonomic_recognition_q3.py) | (none) |
| 04-cycle | `stage1_hankel_period.py` (003) | Hankel-thimble period; rapid-decay; \|A\|=K·Γ(1+β) (§4, §5.2) | stage1_hankel_results.json |

**13 cited scripts + 1 support module.**

### Inter-script dependencies (govern co-location in bundle dirs)
- 01-algebraicity: `extract_verify_operators`, `indicial_analysis`, `borel_pade_census`
  all `import holonomic_recognition_q3`; `indicial_analysis`,`borel_pade_census` also
  `import extract_verify_operators`. ⇒ all four co-located in `01-algebraicity/`.
- 03-verification: `stage0_residual_check` `import q3_foundation`. ⇒ `q3_foundation.py`
  co-located in `03-verification/`.
- 02-galois, 04-cycle scripts import only `sympy`/`mpmath`/`json` (standalone).

### Path issue (fixed in bundle copies, Stage 2.3 / Stage 5.1)
Every cited script except `numcheck_period_rep.py` (which already uses
`Path(__file__).parent`) and `stage2_kovacic.py` (stdout only) writes its results JSON to a
**hardcoded absolute path** `C:\LocalWork\…`. The bundle copies are **path-relativized** to
write next to themselves via `os.path.dirname(__file__)`. This is the **only** change made to
the script bodies; parent slots are untouched.

---

## 3. AUXILIARY scripts (exploration / superseded / not cited) → EXCLUDED

| Script (slot) | Why excluded |
|---|---|
| `stage3b_frobenius.py` (003) | v1, superseded by `stage3b_frobenius_v2.py` (the cited one) |
| `port_crosscheck.py` (002) | Port cross-check; not in the cited claim table |
| `stage0_canonical_check.py` (003) | Canonical-form exploration; not cited; reads a parent JSON by absolute path |

---

## 4. Verification DATA (reference outputs) → `data/`

12 reference result JSONs (the certificates the scripts regenerate):
`holonomic_recognition_q3_results.json`, `operator_verification_results.json`,
`indicial_results.json`, `borel_pade_results.json`, `stage2_kovacic_results.json`,
`stage3_galois_LV_results.json`, `stage3b_frobenius_results.json`,
`stage4_methodA_results.json`, `stage4_methods_results.json`,
`numcheck_period_rep_results.json`, `stage0_residual_results.json`,
`stage1_hankel_results.json`.

---

## 5. Paper files → `paper/`

`vquad-periodrep-paper.pdf` (698 730 bytes, 23 pp), `vquad-periodrep-paper.tex`,
`preamble.tex`, `build.py`.
**No `.bib`** — the bibliography is an inline `thebibliography` in the `.tex`
(`reproducibility-statement.md` §"Determinism"). The task's ".bib" item is therefore N/A;
recorded here so its absence is intentional, not an omission.

---

## 6. Documentation → `docs/` + READMEs (Stages 3–4)

`README.md` (top), `scripts/0X-*/README.md` (×4), `docs/REPRODUCIBILITY.md`,
`docs/DEPENDENCIES.md`, `docs/SIARC_PROVENANCE.md`, `docs/CONVENTIONS.md`, `LICENSE` (CC-BY-4.0).
