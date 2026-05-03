# Phase A — Re-validation of Q20A Phase A* Sweep (no re-run)

**Task:** D2-NOTE-V2-1-WASOW-FULL-CLOSURE  (QS-2)
**Date:** 2026-05-03
**Verdict signal:** `A_PHASE_A_STAR_VERIFIED`

---

## A.1 — Read and thread forward (no re-run)

The Q20A Phase A* artefacts are read verbatim and threaded
forward. No SymPy / mpmath script is re-executed in this
relay.

| artefact                                            | SHA-256 (full)                                                       | size   |
| --------------------------------------------------- | -------------------------------------------------------------------- | ------ |
| `phase_a_symbolic_derivation.py` (Q20 anchor core)  | `8e6f9ebde933652e2581578d282163f0220091ea0ee4adbd6754bd53458f7496`   | (Q20)  |
| `phase_a_star_extended_sweep.py`                    | `06d87de35ee3bf62e848283ba703d63d88307e08f8f2a44389765c10810ac277`   | 9 071  |
| `phase_a_star_results.json`                         | `7cb00221313122b3…` (prefix only here; full in claims.jsonl)         | 5 534  |
| `phase_a_star_summary.md`                           | `b1db14121ee0eaf9…` (prefix only here; full in claims.jsonl)         | 5 247  |

Wrapper SHA `06d87de…0ac277` matches anchor exactly.
Anchor core SHA `8e6f9eb…f7496` matches anchor exactly.

## A.2 — Cross-check the symbolic-identity content

For every d ∈ {2,3,…,10} and every β_d test point, the slope-1/d
edge characteristic polynomial of L_d (eq. (1) of v2) is

    χ_d(c) = 1 − (β_d / d^d) c^d

and the unique positive real root pins

    c(d) = d / β_d^{1/d}.

Cached values (transcribed from `phase_a_star_summary.md`):

| d  | β_d | computed max\|root\|              | rel_err   |
| -- | --- | --------------------------------- | --------- |
| 2  | 3   | 1.154700538379251529018297561…    | 0         |
| 2  | 7   | 0.755928946018454454429033072468  | 0         |
| 3  | 1   | 3.0                               | 0         |
| 3  | 5   | 1.75441064292771963930407241608   | 1.52e-51  |
| 4  | 1   | 4.0                               | 0         |
| 4  | 9   | 2.30940107675850305803659512201   | 0         |
| 5  | 1   | 5.0                               | 0         |
| 5  | 11  | 3.09521960341922786443260685649   | 1.73e-51  |
| 6  | 1   | 6.0                               | 0         |
| 6  | 13  | 3.91285743800967605994223485127   | 0         |
| 7  | 1   | 7.0                               | 0         |
| 7  | 15  | 4.75428270822048742611863219756   | 0         |
| 8  | 1   | 8.0                               | 0         |
| 8  | 17  | 5.61414818760147699187561645114   | 0         |
| 9  | 1   | 9.0                               | 0         |
| 9  | 19  | 6.48871614570268011275830210887   | 0         |
| 10 | 1   | 10.0                              | 0         |
| 10 | 23  | 7.30848258425932731110055681816   | 0         |

PASS rate: 18 / 18.
AEAL cross-checks (independent values at d ∈ {2,3,4}): 3 / 3 PASS.

## A.3 — Cite anchor

The v2.1 `\cite` anchor for the Phase A* sweep is the same as
v2's: the Q20A bridge session
`siarc-relay-bridge/sessions/2026-05-03/Q20A-PHASE-C-RESUME/`
(`\cite{siarc_q20a_phase_c_resume}` in `annotated_bibliography.bib`).
v2.1 demotes the role of the sweep from "the source of the
identity" (v2 framing) to "a numerical verification of the
Newton-polygon Lemma at d ∈ {2,…,10}" (v2.1 framing — see
Phase B). The cite anchor itself is unchanged.

## A.4 — Verdict

**`A_PHASE_A_STAR_VERIFIED`** — Phase A* artefacts re-validated
verbatim by SHA. 18 / 18 sweep PASS at d ∈ {2..10}; 3 / 3 AEAL
cross-checks PASS. The relay agent did not re-run any
numerical pipeline (per spec §8 OUT OF SCOPE). The script
SHAs and the JSON content are byte-identical to the Q20A
deposit.
