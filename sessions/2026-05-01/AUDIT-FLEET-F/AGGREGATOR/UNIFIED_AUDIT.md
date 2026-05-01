# Fleet-F Unified Audit — AGGREGATOR

**Status:** completed  
**Scope read:** `F1`–`F4` `handoff.md` and `findings.jsonl` under `sessions\2026-05-01\AUDIT-FLEET-F`.  
**Halt inheritance:** none. No sub-agent reported `INACCESSIBLE_PARTIAL`.

## Header

- **Reportable findings count:** 12
- **Raw JSONL records read:** 14
  - Supplemental/non-actionable records not counted in reportable buckets: `F1-02` (diagnostic limitation under schema drift) and `F2-L1` (DOI-resolution clean pass).

| Severity | Count |
|---|---:|
| CRITICAL | 0 |
| HIGH | 4 |
| MEDIUM | 3 |
| LOW | 1 |
| INFO | 4 |

## CRITICAL bucket

No CRITICAL findings exist across F1, F2, F3, and F4. No next-session global block is triggered by Fleet-F.

## HIGH bucket

### AEAL schema

- **F1-01 — AEAL schema drift** (`HIGH`)  
  **Scope:** `sessions/2026-05-01/**/claims.jsonl`  
  **Statement:** All 199 entries across 26 sessions use legacy schema `{claim, evidence_type, script, output_hash}` rather than canonical AEAL `{claim_id, type, statement, evidence, confidence}`; 995 field-level violations were counted. Because `claim_id` and `verdict` are absent, duplicate IDs, verdict contradictions, and confidence/evidence calibration cannot be audited.  
  **Recommendation:** Migrate to canonical schema or formally re-spec AEAL in PCF-2 v1.3.  
  **Blocks/caveat:** PCF2-V13 auditability re-claim should not silently proceed without addressing this.

### cite-not-defined

- **F4-H1 — `mpmath` cited but undefined** (`HIGH`)  
  **Scope:** `tex/submitted/p12_journal_main.tex`, `tex/submitted/rigidity_entropy_expmath_article.tex`, `tex/submitted/rigidity_entropy_expmath_resubmission*.tex`, `tex/submitted/vquad_resurgence_R1.tex`, `tex/submitted/vquad_resurgence_R2.tex`.  
  **Statement:** `mpmath` is cited but absent from scoped `.bib` files; affected compiles will produce `??`.  
  **Recommendation:** Add/verify canonical `@misc{mpmath,...}` entry before affected submissions.

- **F4-H2 — `olver1974` / `odlyzko1995` cited but undefined** (`HIGH`)  
  **Scope:** `tex/submitted/paper14-ratio-universality-SUBMISSION.tex`.  
  **Statement:** Both keys are cited but absent from the scoped bibliography.  
  **Recommendation:** Add verified book/collection entries before paper14 resubmission.

- **F4-H3 — `Okamoto1987` cited but undefined** (`HIGH`)  
  **Scope:** `tex/submitted/p12_journal_main.tex`.  
  **Statement:** `Okamoto1987` is cited but absent from the scoped bibliography.  
  **Recommendation:** Add verified `@article{Okamoto1987,... doi=10.1007/BF01762370}` before p12 resubmission.

## MEDIUM bucket

- **F2-M1 — reflexivity gap** (`MEDIUM`)  
  **Scope:** `PCF2-V12-RELEASE/zenodo_description_v1.2.txt:32-33` and `CHANNEL-THEORY-V12/zenodo_description_v1.2.txt:9`.  
  **Statement:** PCF-2 v1.2 declares `IsSupplementedBy` Channel Theory concept `19941678`, but Channel Theory v1.2 prose still says it supplements PCF-2 v1.1 (`19939463`) rather than v1.2 (`19951458`).  
  **Recommendation:** Update Channel Theory description body to point at the current PCF-2 version in the next reversion.

- **F2-M2 — stale citation in historical v1.1 record** (`MEDIUM`)  
  **Scope:** `CHANNEL-THEORY-V11/zenodo_description_v1.1.txt:9`.  
  **Statement:** Channel Theory v1.1 still cites PCF-2 v1.1 even though v1.2 supersedes it. This is acceptable for the v1.1 record itself but should be visible in reflexivity tracking.  
  **Recommendation:** Flag in reflexivity table; no direct edit required to the historical record.

- **F2-M3 — stale citation in v1.2 source/prose** (`MEDIUM`)  
  **Scope:** `CHANNEL-THEORY-V12/zenodo_description_v1.2.txt:9` and `PCF2-V12-RELEASE/zenodo_description_v1.2.txt:43`.  
  **Statement:** Channel Theory v1.2 prose still cites PCF-2 v1.1. PCF-2 v1.2's `isNewVersionOf` pointer to v1.1 is structurally correct, but prose and metadata can read as inconsistent.  
  **Recommendation:** Update prose to PCF-2 v1.2/v1.3 where appropriate; preserve structurally correct predecessor metadata.

## LOW bucket

- **F4-L1 — missing DOI** (`LOW`)  
  **Scope:** `tex/submitted/SpectralClasses/pcf_spectral_refs.bib:13-20`.  
  **Statement:** `@book{costin2008asymptotics}` has no DOI field.  
  **Recommendation:** Add DOI if/when this bibliography is next touched.

## INFO bucket

- **F2-I1 — no arXiv mirrors found** (`INFO`)  
  **Scope:** all SIARC papers scanned.  
  **Statement:** No arXiv mirror evidence was found for the four published Zenodo records (`19885550`, `19937196`, `19951458`, `19951331`).  
  **Recommendation:** Track arXiv mirroring as a separate todo.

- **F3-01 — B4 consistency pass** (`INFO`)  
  **Scope:** PCF-2 v1.2 and Q1 handoff.  
  **Statement:** B4 is stated as `A = 2d` in PCF-2 v1.2 source and aligns with Q1 d=4 (60/60) verification. No HIGH/CRITICAL issue.

- **F3-02 — conjecture versioning pass** (`INFO`)  
  **Scope:** Channel Theory v1.1 → v1.2.  
  **Statement:** Universal form `c(d)=d` explicitly supersedes the v1.1 candidate `2*sqrt((d-1)!)`; no silent demotion was found.

- **F4-I1 — defined-not-cited library bib** (`INFO`)  
  **Scope:** `tex/submitted/SpectralClasses/pcf_spectral_refs.bib`.  
  **Statement:** Eleven entries are defined but not cited in `tex/submitted/*.tex`: `poincare1885`, `frobenius1873`, `apery1979`, `ronveaux1995`, `wall1948`, `lorentzen2008`, `raayoni2021`, `cohen2024database`, `pcf_unified_2026`, `ratio_universality_2026`, `pcf_bifurcation_2026`.  
  **Recommendation:** Likely a future-use library bib; no fix required now.

## Supplemental raw JSONL observations

These were read from JSONL but are not counted as reportable findings in the requested Fleet-F buckets:

- **F1-02** (`INFO`): duplicate `claim_id`s and verdict contradictions cannot be enumerated until F1-01 is resolved.
- **F2-L1** (`LOW`): all 11 checked DOIs resolved HTTP 200 and concept/version usage was otherwise consistent.

## Cross-sub-agent correlations

- **F1 schema drift × F3 conjecture consistency:** F3 is clean partly because B-numbering does not depend on AEAL `claim_id` mapping. If F1's AEAL migration or re-spec happens, re-run conjecture/claim cross-checks to ensure B-numbering and claim records still align.
- **F2 stale citations × F4 bib hygiene:** Not coupled in this round. F2 issues live in `zenodo_description_*.txt` prose/metadata, not `.bib` files.
- **F4 cite-not-defined × F1 AEAL:** Any future session that runs `pdflatex` to verify a claim should add a precondition that the relevant bibliography is clean, otherwise proof/audit claims may be polluted by unresolved `??` references.
