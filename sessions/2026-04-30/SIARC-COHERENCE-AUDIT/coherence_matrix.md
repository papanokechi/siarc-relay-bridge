# Coherence Matrix — SIARC 7-paper portfolio

**Audit date:** 2026-04-30
**Task:** SIARC-COHERENCE-AUDIT (P-10)
**Scope:** UMB, #14, T2A, T2B, P06, P08, P11

## 0. Paper map (canonical .tex sources)

| Tag | Title | File | sha12 |
|---|---|---|---|
| UMB | The SIARC umbrella program | `tex/submitted/umbrella_program_paper/main.tex` | 75485e5bbd9b |
| #14 | PSL₂(ℤ) and a Four-Tier Obstruction Hierarchy | `tex/submitted/paper4_takeuchi_outline.tex` | 9a7a04baaadb |
| T2A | 2k-Degree Conjecture at k=2 (F(4,3)/(4,2)) | `t2a_paper_draft.tex` | 6d07e458ab12 |
| T2B | Trans-Stratum −2/9 (Class A/B census + Stieltjes) | `tex/submitted/t2b_paper_draft_v5_withauthor.tex` | d7630e6b2548 |
| P06 | Desert (4,3)/(5,3) negative result | `tex/submitted/p06_desert_ijnt_submission/pcf_desert_negative_result.tex` | 1c5616e09589 |
| P08 | Painlevé III(D₆) + V_quad resurgence (R2) | `tex/submitted/vquad_resurgence_R2.tex` | 2bda5a8e4732 |
| P11 | Complete Arithmetic Stratification of F(2,4) (R1) | `f1_mathcomp_submission/main_R1.tex` | 37a36a4a1684 |

> **Disambiguation note.** A second file `tex/submitted/paper14-ratio-universality-SUBMISSION.tex` carries `paper14` in its name but is the **Ratio Universality / Meinardus partition** paper (CMB row P13, Acta Arith), unrelated to the SIARC PCF programme's `Paper14` reference. UMB's bib entry `\bibitem{Paper14}` in `main.tex` line 390 is the four-tier classification paper — i.e. `paper4_takeuchi_outline.tex`. We adopt that mapping for "#14" throughout this audit. The naming clash is itself logged as `MM-08`.

## 1. Probe matrix (raw counts)

(See `probe_matrix.md` for the auto-generated full table; reproduced highlights below.)

| probe                | UMB | #14 | T2A | T2B | P06 | P08 | P11 |
|---                   |---|---|---|---|---|---|---|
| `(2,1)` deg          | 8 | 0 | 0 | 11| 3 | 0 | 6 |
| `(2,2)` deg          | 0 | 0 | 0 | 0 | **1** | 0 | 0 |
| `(3,1)` deg          | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| `(4,2)` deg          | 0 | 0 | 18| 0 | 0 | 0 | 0 |
| `(4,3)` / `(5,3)`    | 0 | 0 | 4 | 0 | 13 + 12 | 0 | 0 |
| `F(2,4)` literal     | 0 | 0 | 3 | 0 | 3 | 0 | 19|
| ratio `−2/9`         | 12| 0 | 2 | 7 | 0 | 0 | 3 |
| ratio `+1/4`         | 0 | 0 | 3 | 10| 0 | 0 | 0 |
| Class A / Class B    | 0 | 0 | 0 | 13/32| 0 | 0 | 0 |
| Tier T0..T3 (UMB-style)| 8/6/9/8 | 20/12/11/8 | – | – | – | – | – |
| DOI 19783311 (T2B concept) | 4 | 0 | 0 | 0 | 0 | 0 | 0 |
| DOI 19801038 (T2B v2)      | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| DOI 19885549 (UMB concept) | **0** | 0 | 0 | 0 | 0 | 0 | 0 |
| DOI 19885550 (UMB version) | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| DOI 19774029 (T2A v1)      | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| Math.Comp wording          | 0 | 0 | **3** | 0 | 0 | 0 | 0 |
| JTNB wording               | 0 | 0 | 0 | 0 | 1 | 0 | 0 |

## 2. Concept × paper coverage matrix

`✓` = stated/proved; `cite` = referenced as companion only; `∅` = silent; `≠` = mismatched usage.

| Concept                                         | UMB | #14 | T2A | T2B | P06 | P08 | P11 |
|---                                              |-----|-----|-----|-----|-----|-----|-----|
| degree-(2,1) PCF families                       | ✓ | ∅ | ∅ | ✓ | **(2,2)≠** | ∅ | ✓ |
| F(2,4) ambient (deg=2, coeff bound 4)           | ∅ | ∅ | cite| ∅ | cite| ∅ | ✓ |
| Trans-stratum exponent c = −2/9                 | ✓ (Conj 2.1) | ∅ | cite | ✓ (cor:k=2) | ∅ | ∅ | ✓ (prop:ratio) |
| Class A (a₂/b₁²=−2/9) ∪ Class B (a₂/b₁²=+1/4)   | **omitted Class B** | ∅ | ratio not predictive obs:rho-flat | ✓ (Conj completeness) | ∅ | ∅ | ∅ |
| Tier T0 (UMB sense: algebraic)                  | ✓ def | **≠ modular non-CM** | ∅ | ∅ | ∅ | ∅ | ∅ |
| Tier T1 (UMB sense: transcendental Mahler)      | ✓ def | **≠ cuspidal arithmetic** | ∅ | ∅ | ∅ | ∅ | ∅ |
| Tier T2 (UMB sense: trans-stratum)              | ✓ def | **≠ non-arith Fuchsian** | ∅ | implicit | ∅ | ∅ | ∅ |
| Tier T3 (UMB sense: barrier)                    | ✓ def | **≠ irregular conf-Heun** | ∅ | ∅ | ∅ | ∅ | ∅ |
| 5-stratum decomp (Rat∪Log∪Alg∪Trans∪Des)        | ∅ | ∅ | ∅ | ∅ | cite (target null) | ∅ | ✓ thm:complete |
| Painlevé linkage                                | OP `prob:painleve` ⇒ **PVI** | (T3 := confluent Heun) | ∅ | ∅ | ∅ | thm:painleve = **PIII(D₆)** | ∅ |
| Γ₀(2) / Hecke triangle question                 | OP `prob:t2-d2-nonpsl` (open) | ∅ | ∅ | ∅ | ∅ | ∅ | ∅ |

## 3. Bidirectional citation graph

| from \\ to | UMB | #14 | T2A | T2B | P06 | P08 | P11/synthesis |
|-----------|-----|-----|-----|-----|-----|-----|---------------|
| UMB    | self | `\cite{Paper14}` (post-acceptance DOI TBA) | ∅ | `\cite{T2B}` 19783311 | ∅ | `\cite{P08}` draft | ∅ |
| #14    | ∅ | self | ∅ | ∅ | ∅ | ∅ | ∅ |
| T2A    | ∅ | ∅ | self | ∅ | ∅ | ∅ | `\cite{PCF24}` ⇒ "Math.Comp 260422-Papanokechi" **stale: now JTNB-2400** |
| T2B    | ∅ | ∅ | ∅ | self | ∅ | ∅ | ∅ |
| P06    | ∅ | ∅ | ∅ | ∅ | self | ∅ | `\cite{P11}` (footnote: degree (2,2) — incorrect) |
| P08    | ∅ | ∅ | ∅ | ∅ | ∅ | self | ∅ |
| P11    | ∅ | `\cite{spectral}` (JNTH-D-26-00480) | ∅ | ∅ | ∅ | `\cite{painleve}` (NON-110708) | self + `\cite{synthesis}` (preprint) |

## 4. Open-Problems list (UMB §5) — current status

| # | UMB problem | Status as of 2026-04-30 |
|---|---|---|
| `prob:31`  | Degree-(3,1) classification | OPEN. Not addressed by any companion paper in audit set. |
| `prob:t2-d2-nonpsl` | Trans-stratum at d=2 for Γ₀(2)/G_q | **PARTIAL NEGATIVE** — `UMB-GAMMA0-2-SWEEP` (2026-04-30, bridge) returned 0 Trans across Γ₀(2), G₄, G₅, G₆, G₈ at predicted ratios (HALT_A). UMB still lists as open. → **MM-04** |
| `prob:painleve` | Painlevé VI ↔ trans-stratum PCF | OPEN. P08 establishes **PIII(D₆)** for V_quad (a T3, not T2 family); UMB's open problem is for T2/PVI. Phrasing collision noted as **MM-05**. |
| `prob:effective` | Effective T0/T1 boundary | OPEN. |
| `prob:t3` | T3 nonemptiness (UMB sense) | Implicitly satisfied by P08 V_quad if paper4's T3 is identified with UMB's T3 — but **the two T3 definitions diverge** (see MM-02). |
| `prob:mahler` | Mahler–Nesterenko gap | OPEN. |
| `prob:census` | Census beyond degree-(2,1) | T2A (degree-(4,2)) extends the census. UMB does not yet cite T2A. **MM-06** |

## 5. Deliverable cross-references
- Raw extracted claims: `extracted_claims.md`, `claims.json`
- Probe matrix: `probe_matrix.md`, `probe_matrix.json`
- Mismatches & suggested fixes: `mismatches_list.md`
- Triage: `priority_ranking.md`
- Patch relay prompts (T1): `patch_relay_*.md`
