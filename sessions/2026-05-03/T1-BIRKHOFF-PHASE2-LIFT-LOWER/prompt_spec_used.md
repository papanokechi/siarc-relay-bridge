# Phase 0.0 — Provenance: relay prompt spec used

**Task:** T1-BIRKHOFF-PHASE2-LIFT-LOWER
**Date:** 2026-05-03 / 2026-05-04 (JST)
**Agent:** GitHub Copilot (VS Code) — model: Claude Opus 4.7 (Extra high reasoning)
**Source:** operator-fired relay prompt 2026-05-04T06:53:26.787+09:00
**Standing rules consulted:**
- `tex/submitted/control center/prompt/_RULES.txt` (10 KB; §§A-J)
- `tex/submitted/CMB.txt` (project state)
- A-01 verdict (`sessions/2026-05-03/T1-A01-NORMALIZATION-RESOLUTION/handoff.md`)
- T1 Phase 1 dossier (`sessions/2026-05-02/T1-BIRKHOFF-TRJITZINSKY-LITREVIEW/`)
- v1.15 strategic picture (`tex/submitted/control center/picture_revised_20260503.md` SHA `89B12CC9...`)

## Verbatim relay prompt body (reference)

The operator-fired relay prompt body `T1-BIRKHOFF-PHASE2-LIFT-LOWER` (relay class:
relay-agent-invocation, AEAL-compliant; parallel-safe with any non-M4-touching task;
compute medium-high ~3-5 hr) defines six execution phases (0.0, 0.5, A, B, C, D, E
optional, F) targeting the lift of Conjecture B4 from the empirical+literature
bracket A ∈ [d, 2d] to A = 2d at d ≥ 3 via non-resonance / non-degeneracy of the
Birkhoff-Trjitzinsky reduction at irregular singularities of fractional rank q.

### Phase definition (verbatim from relay §2)

- **Phase 0.0** — provenance write-out (this file)
- **Phase 0.5** — bibkey collision preflight (see `bibkey_preflight.md`)
- **Phase A** — symbolic derivation of indicial polynomial chi_d(c) at d ∈ {2,3,4}
  - A.1 set up f(z) = z^c sum a_n z^{-n} per Birkhoff 1930 §2 Theorem I
  - A.2 apply L_d, collect leading terms in z^c
  - A.3 derive chi_d(c); compute degree in c
  - A.4 identify indicial exponents (roots)
  - A.5 verify against d=2 proof in PCF-1 v1.3 §6 Theorem 5
  - A.6/A.7 verify at d=3, d=4 against PCF-2 v1.3 / Q1 empirical
  - Verdict signal: `A_INDICIAL_VERIFIED_AT_d_le_4` (pass) or `A_INDICIAL_DRIFT_AT_d*` (halt)
- **Phase B** — extended sweep at d ∈ [3, d_max=8] with non-resonance + non-degeneracy
- **Phase C** — B-T 1933 §§7-9 literature anchoring (C.0 gate PASSES — PDFs on disk + SHA verified)
- **Phase D** — verdict aggregation (UPGRADE_FULL / UPGRADE_PARTIAL / HALT_T1P2_*)
- **Phase E** (conditional) — D2-NOTE v2.1-style upgrade artifact
- **Phase F** — handoff + AEAL claims (≥14 entries) + bridge commit + push

## Pre-execution scoping notes

The Phase 1 dossier (`bt1933_theorem_extraction.md` Q1.e) explicitly stated:

> "'B-T proves A = 2d for the SIARC PCF stratum at all d.' **FALSE — this is a
>  SIARC-internal statement.** B-T 1933 establishes the formal Newton-polygon
>  slope (which **predicts** A = 2d as a formal-asymptotic statement under a
>  specific normalisation of the SIARC asymptotic ansatz); the analytic upgrade
>  from formal slope to actual A_PCF(b) requires a post-1933 sectorial-asymptotic
>  result (Turrittin / Wasow / Immink) and a separate argument that the SIARC
>  normalisation matches the formal exponent without an O(1) shift. **This is
>  the gap that Phase 2 of T1 must address.**"

The agent's pre-execution rubber-duck consultation confirmed:
- (β) UPGRADE_PARTIAL_FORMAL_LEVEL is the AEAL-honest expected verdict
- Costin 2008 is ODE-focused, not a clean DE closure anchor
- B-T §§7-9 are factorization / proper-curve / complete-properness machinery,
  not the SIARC-specific A_PCF identification
- Phase A naive Newton-polygon analysis gives A = d (symmetric coeffs) or A = d+1
  (α-direction asymmetric) — **not A = 2d** at d ≥ 3 generically; the upper branch
  requires showing the SIARC stratum is at an **exceptional locus** where leading-
  edge coefficients vanish (P2.1 + P2.2 sub-claims of `gap_proposition_for_d_ge_3`)

## On-disk anchor verification (Phase C.0 pre-gate)

| File | SHA-256 prefix | Size | Status |
|------|---------------|------|--------|
| `01_birkhoff_1930_acta54.pdf` | `aeb5291e...` | 1.76 MB | ✓ verified |
| `03_birkhoff_trjitzinsky_1933_acta60.pdf` | `dcd7e3c6...` | 3.33 MB | ✓ verified |
| `04_wasow_1965_dover.pdf` | `f59d6835...` | 5.43 MB | ✓ on disk; **image-only, no OCR layer** |
| `06_costin_2008_chap5.pdf` | `436c6c11...` | 1.37 MB | ✓ on disk; ODE-focused |

Path: `tex/submitted/control center/literature/g3b_2026-05-03/`
SHA file: `SHA256SUMS.txt` (3712 B; generated 2026-05-03T04:21:06Z).

Phase C.0 gate **PASSES** — B-T 1933 PDF on disk with SHA-verified provenance.
