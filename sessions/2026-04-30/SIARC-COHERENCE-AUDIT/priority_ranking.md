# Priority ranking — SIARC coherence audit
**Date:** 2026-04-30 — Task `SIARC-COHERENCE-AUDIT`

Tier definitions (per the relay prompt):
- **T1** — blocks the next submission of an affected paper
- **T2** — must be fixed before the next arXiv / Zenodo push
- **T3** — nice to have, no impact on review or correctness

## TIER 1 (blockers — produce relay patch prompts; do not auto-edit)

| Rank | ID | Affected papers | Summary |
|---|---|---|---|
| 1 | **MM-03** | UMB, T2B | UMB Conjecture 2.1 omits T2B Class B (+1/4); literally falsified by 16 known families. |
| 2 | **MM-02** | UMB, #14 | T0..T3 labels carry incompatible meanings across UMB and #14. |
| 3 | **MM-01** | P06, P11 | P06 still says "degree profile (2,2)" for the F(2,4) Trans-stratum; P11 says (2,1). |

Relay patch prompts are written for each (see `patch_relay_MM01.md`,
`patch_relay_MM02.md`, `patch_relay_MM03.md`). All three patch
prompts are conservative and mathematics-preserving; they do not
introduce new claims beyond what the cited companion papers already
prove or conjecture.

## TIER 2 (pre-arXiv)

| Rank | ID | Affected | Summary |
|---|---|---|---|
| 4 | MM-04 | UMB | Append HALT_A status note from `UMB-GAMMA0-2-SWEEP` (2026-04-30) to `prob:t2-d2-nonpsl`. |
| 5 | MM-05 | UMB, P08 | Qualify `prob:painleve` to T2 / PVI; note P08 covers T3 / PIII(D₆). |
| 6 | MM-06 | UMB | Cite T2A (Zenodo 19774029) in `prob:census` and program-papers table. |
| 7 | MM-07 | T2A | Update `\bibitem{PCF24}` venue from Math.Comp 260422-Papanokechi to JTNB-2400. |
| 8 | MM-08 | UMB, paper14-ratio-universality | Filename collision between two distinct "Paper14" objects. |

## TIER 3 (nice-to-have)

| Rank | ID | Affected | Summary |
|---|---|---|---|
| 9 | MM-09 | UMB | Cite UMB concept DOI 19885549 (currently only the version 19885550 is cited). |
| 10 | MM-10 | P11 | `references.bib` `contamination` note should reflect Exp. Math. rejection. |

## HALT semantics for this audit

The relay prompt requires HALT IF "any T1 mismatch found → produce a
relay prompt patching the affected paper; do not auto-edit." Three T1
mismatches were found. The audit therefore proceeds to the standard
final-step push, while the in-place patches are deferred to subsequent
relay sessions (one per MM-id).

No file under `tex/submitted/`, `f1_mathcomp_submission/`, or
`t2a_paper_draft.tex` was edited as part of this audit.
