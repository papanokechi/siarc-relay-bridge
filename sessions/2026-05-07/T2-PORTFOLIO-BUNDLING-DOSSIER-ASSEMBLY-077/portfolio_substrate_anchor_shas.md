# Portfolio Substrate Anchor SHAs — 077

**Session:** T2-PORTFOLIO-BUNDLING-DOSSIER-ASSEMBLY-077
**Compiled:** 2026-05-07 ~14:30 JST
**Bridge HEAD at fire:** `3410e5d` (T1-PHASE-3-BT-1933-SECTIONS-4-6-READTHROUGH-073)
**Scope:** Phase A SHA anchors for all substrate consumed in 077.

All hashes are SHA-256 (first 16 hex chars displayed for compact reference;
full hashes derivable on demand via `Get-FileHash -Algorithm SHA256`).

---

## §A.1 — Six paper-source anchors

| # | Paper label | Path (workspace-relative) | Bytes | Lines | SHA-256 (16) |
|---|---|---|---:|---:|---|
| P1 | PCF-1 v1.3 (TeX source) | `tex/submitted/p12_journal_main.tex` | 72311 | 1674 | `82173A09521D6676` |
| P1 | PCF-1 v1.3 (PDF) | `tex/submitted/p12_journal_main.pdf` | 508059 | — | `EC7C1DD25D2B39E7` |
| P2 | PCF-2 v1.3 (TeX source) | `tex/submitted/pcf2_program_statement.tex` | 75098 | 1450 | `82FE2315CFDA2047` |
| P2 | PCF-2 v1.3 (PDF) | `tex/submitted/pcf2_program_statement.pdf` | 558153 | — | `87B845A8E382F3C1` |
| P3 | CT v1.3 (TeX source) | `siarc-relay-bridge/sessions/2026-05-02/CHANNEL-THEORY-V13-RELEASE/channel_theory_outline.tex` | 70178 | 1594 | `59C5352795F8D63D` |
| P3 | CT v1.3 (PDF) | `siarc-relay-bridge/sessions/2026-05-02/CHANNEL-THEORY-V13-RELEASE/channel_theory_outline.pdf` | 581459 | — | `DF3B90E808E49E84` |
| P3' | CT v1.4 (in-flight TeX) | `siarc-relay-bridge/sessions/2026-05-03/CT-V14-NARRATIVE-DRAFT/ct_v1.4_main.tex` | 91605 | 2050 | `0600A4456803A43D` |
| P3' | CT v1.4 (in-flight PDF) | `siarc-relay-bridge/sessions/2026-05-03/CT-V14-NARRATIVE-DRAFT/ct_v1.4_main.pdf` | 645939 | — | `4435BC0C2DDE4D78` |
| P4 | D2-NOTE v2.1 (TeX source) | `siarc-relay-bridge/sessions/2026-05-03/D2-NOTE-V2-1-WASOW-FULL-CLOSURE/d2_note_v2_1.tex` | 38311 | 908 | `840120E73534DA8E` |
| P4 | D2-NOTE v2.1 (PDF) | `siarc-relay-bridge/sessions/2026-05-03/D2-NOTE-V2-1-WASOW-FULL-CLOSURE/d2_note_v2_1.pdf` | 443759 | — | `A8B6026A3453F901` |
| P5 | T2B v3.0 (TeX source) | `tex/submitted/t2b_paper_draft_v5_withauthor.tex` | 28635 | 381 | `9BDD6A5D799BD8FE` |
| P5 | T2B v3.0 (PDF) | `tex/submitted/t2b_paper_draft_v5_withauthor.pdf` | 331769 | — | `7AC8F204289409B5` |
| P6 | SIARC umbrella v2.0 (TeX) | `tex/submitted/umbrella_program_paper/main.tex` | 44935 | 937 | `612F732EBE2D8BAB` |
| P6 | SIARC umbrella v2.0 (PDF) | `tex/submitted/umbrella_program_paper/main.pdf` | 455178 | — | `24382421290318AE` |

[NOTE-077-SHA-1] CT v1.4 listed as supplementary `P3'` because the prompt §3 spec references "CT v1.4 (post-G17-close)" as the bundle-B2 component. CT v1.3 remains the canonical Zenodo-published version (concept DOI `19941678`, version DOI `19972394`); CT v1.4 is the in-flight successor. Both anchored.

---

## §A.2 — Auxiliary substrate anchors

| Source | Path | Bytes | Lines | SHA-256 (16) |
|---|---|---:|---:|---|
| Submission log | `tex/submitted/submission_log.txt` | 17030 | 284 | `2A28465AE39BADF5` |
| CMB.txt | `tex/submitted/CMB.txt` | 94201 | 2066 | `AE1D3B7A53D46A2F` |
| 2026-05-04 portfolio inventory (5-record × 3-endorser) | `siarc-relay-bridge/sessions/2026-05-04/ENDORSEMENT-CHAIN-INVENTORY-CONSOLIDATE/portfolio_inventory.md` | 14680 | — | `25B4C96DC15A85A3` |
| 2026-05-04 candidate dossier | `siarc-relay-bridge/sessions/2026-05-04/ENDORSER-HANDLE-ACQUISITION/candidate_dossier.md` | 10784 | — | `315410D80EDC92C5` |

---

## §A.3 — 074 + 075 status confirmation

[NOTE-077-SHA-2] Per spec §1.A.3, 077 dossier validity is independent of 074 + 075 outcomes; status is recorded for context.

| Session | Path | Status | handoff.md present? | Verdict (if landed) | Bridge-commit landed? |
|---|---|---|---|---|---|
| 074 | `sessions/2026-05-07/T2-M4-RATIFICATION-DOSSIER-ASSEMBLY-074/` | LOCAL_ASSEMBLED | YES | `DOSSIER_COMPLETE` (per `> **Status:** COMPLETE` line in handoff.md) | NO_PRE_COMMIT_IN_FLIGHT |
| 075 | `sessions/2026-05-07/T2-M6-CC-CHART-MAP-CANDIDATE-B1-CHECK-075/` | LOCAL_ASSEMBLY_NO_HANDOFF | NO | (mid-assembly; no handoff) | NO_PRE_COMMIT_IN_FLIGHT |

Bridge-HEAD `git log` for both directory paths returned empty,
confirming neither has been committed at fire time. 077 proceeds
under "PRE-COMMIT IN-FLIGHT" tag for both predecessors.

---

## §A.4 — DOI cross-check vs prompt §1 cited DOIs

[NOTE-077-SHA-3] Spec §1.A.1 lists candidate DOIs that the prompt-drafter
flagged as "or wherever the version-pin landed; verify via submission_log
Item N". 5 of the 6 prompt-cited DOIs differ from the canonical
2026-05-04 portfolio inventory anchor (5 records × 3 endorsers, SHA
`25B4C96DC15A85A3`). Discrepancy surfaced; not a halt because spec
itself preauthorises the on-disk verification step.

| Record | Prompt-cited DOI (concept / version) | Inventory-verified DOI (concept / version) | Match |
|---|---|---|---|
| PCF-1 v1.3 | `19931635` / (not cited) | `19931635` / `19937196` | concept ✓ |
| PCF-2 v1.3 | `19941678` / `19951331` | `19936297` / `19963298` | both ✗ |
| CT v1.3 | `19951330` / `19963297` | `19941678` / `19972394` | both ✗ |
| D2-NOTE v2.1 | `19996689` / `20015923` | `19996689` / `20015923` (per CC-VQUAD spec L46-48) | both ✓ |
| T2B v3.0 | `19783312` / (not cited) | `19783311` / `19915689` | concept ✗ (off by 1) |
| SIARC umbrella v2.0 | `19965040` / `19965041` | `19885549` / `19965041` | concept ✗ (umbrella v2.0 version DOI ✓) |

[NOTE-077-SHA-4] **HALT_077_SUBSTRATE_DRIFT not triggered.** The prompt itself
preauthorises on-disk verification; on-disk substrate is fully resolvable;
DOI drift logged in `discrepancy_log.json` (D-077-1) and surfaced
in `handoff.md` Anomalies as the operational anchor for any downstream
prompt that consumes 077's bundle inventory.

---

## §A.5 — 2026-05-07 portfolio-impact assessment + endorsement-fit assessment

[NOTE-077-SHA-5] Spec §1.A.1 references two artefacts cited in chat
transcript / session-state plan.md:

- 2026-05-07 portfolio-impact assessment (Tier 1: PCF-2 v1.3 → Constructive Approximation, D2-NOTE v2.1 → Asymptotic Analysis)
- 2026-05-07 endorsement-fit assessment (Tier 1: PCF-2 v1.3 + D2-NOTE v2.1; Tier 2: PCF-1 v1.3 + CT v1.4)

**On-disk search result:** No `*portfolio*impact*` file or `plan.md`
matching the citation. The 2026-05-04 portfolio inventory
(`portfolio_inventory.md`, SHA `25B4C96DC15A85A3`) and 2026-05-04
candidate dossier (`candidate_dossier.md`, SHA `315410D80EDC92C5`) are
on disk; their substantive content (15-template × 5-record fit
matrix; endorser dossier with 3 Tier-1 candidates) is the
load-bearing endorsement-fit substrate cited verbatim throughout 077.

The 2026-05-07 impact assessment is treated as
**ORAL-OR-TRANSCRIPT-ONLY** for 077; bundle profiles carry the
verbatim 2026-05-04 fit-assessment substrate plus on-disk paper
content. Surfaced in `discrepancy_log.json` D-077-2 and
`handoff.md` Anomalies; not a halt (spec §1 explicitly accepts
chat-transcript residence).

---

End of substrate anchor file.
