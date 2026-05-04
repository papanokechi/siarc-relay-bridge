# Prompt spec used — PCF2-V13-AFIT-DEFINITION-READBACK

Verbatim relay prompt body (Phase 0 mandatory pre-step).
Composed 2026-05-04 ~12:30 JST by Copilot CLI (Claude Opus 4.7 xhigh).

---

================================================================
SIARC RESEARCHER PROMPT 018 — PCF2-V13-AFIT-DEFINITION-READBACK
================================================================
TASK ID:        PCF2-V13-AFIT-DEFINITION-READBACK
COMPOSED:       2026-05-04 ~12:30 JST
DRAFTED-BY:     Copilot CLI (Claude Opus 4.7 xhigh)
AGENT:          Copilot researcher (web-fetch + paper-skim;
                NOT a heavy-AEAL relay agent)
GATES:          DRAFT-PENDING in v1.17 §6 (Tier-2; G24 resolution
                candidate (ii) for Phase 2 Anomaly 2). Fires
                independently — parallel-safe with M6 spec QA
                wait + Wasow §X.3 OCR + T1 Phase 3.
PRIOR ANCHORS:  T1-BIRKHOFF-PHASE2-LIFT-LOWER verdict
                `UPGRADE_PARTIAL_FORMAL_LEVEL` 2026-05-04 (bridge
                `37c939f`); v1.17 picture §5 G24; Q35 ruling
                2026-05-04 (M6 / T1-Phase-3 / readback all
                parallel-safe).
COMPUTE BUDGET: ~1-2 hr researcher (paper readback + extraction).
RUNTIME PROFILE:Web-fetch + pypdf text extraction + targeted
                quote extraction. NO mpmath / symbolic compute.

§0 GOAL — Pin the EXACT measurement convention used by PCF-2
v1.3 §6 + R1.1 + R1.3 + Q1 for the empirical $A_\text{fit}$
value reported at $d \in \{3, 4\}$. Closes G24 by SOURCE
READBACK with verbatim quotes + page/equation anchors.

§1 ANCHOR FILES — PCF-2 v1.3 PDF candidates:
  - tex/submitted/pcf2_program_statement.pdf (workspace build)
  - sessions/2026-05-02/PCF2-V13-RELEASE/ (no PDF; .tex+build.log only)
  - Zenodo: concept DOI per submission_log; version DOI per V13-RELEASE

§2 PHASES — Phase 0 (provenance), Phase A (anchor PDF), Phase B
(extract A_fit definition with ≤30-word verbatim quotes), Phase C
(reconcile vs T1 Phase 2 baseline), Phase D (verdict
aggregation), Phase E (handoff + AEAL claims ≥ 5).

§3 AEAL CLAIMS — ≥ 5 entries (literature_quotation /
literature_citation / deposit_confirmation; reproducible: true).

§4 HALT CONDITIONS — HALT_G24_PCF2_V13_NOT_FOUND,
HALT_G24_PAGE_COUNT_DRIFT, HALT_G24_DEFINITION_NOT_LOCATED,
HALT_G24_RECONCILIATION_INCONSISTENT.

§5 FORBIDDEN-VERB HYGIENE — "trivial"/"obvious"/"clearly"/"easily
seen to" forbidden; "shows"/"confirms"/"proves" forbidden in
prediction-or-conjecture context; verbatim quotes ≤ 30 words.

§6 OUT OF SCOPE — re-measurement at fresh dps; modifying PCF-2
v1.3 source; T1 Phase 3 borderline-ansatz work; M6 / CC-VQUAD
work; browser-driven Zenodo fetches; API-key-requiring artifacts.

§7 OUTCOME LADDER —
  UPGRADE_G24_DEFINITIONS_MATCH_PHASE2_ANOMALY_REAL
  UPGRADE_G24_DEFINITIONS_DIFFER_<formula>
  UPGRADE_G24_PARTIAL_AMBIGUOUS
  HALT_G24_*

§8 STANDING FINAL STEP — B1–B5 per _RULES.txt §H.

(Body abbreviated for in-bridge deposit; full text in operator
relay logs. Phases / halts / outcome ladder reproduced
verbatim above.)
