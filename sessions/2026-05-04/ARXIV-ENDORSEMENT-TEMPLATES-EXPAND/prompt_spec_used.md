# Prompt Spec Used — ARXIV-ENDORSEMENT-TEMPLATES-EXPAND

Source: SIARC RESEARCHER PROMPT 037 — ARXIV-ENDORSEMENT-TEMPLATES-EXPAND
Composed: 2026-05-04 ~16:18 JST
Drafted-by: Copilot CLI (Claude Opus 4.7 xhigh)
Agent: Copilot researcher

Goal: emit 9 missing endorsement templates (3 records × 3 Tier-1
endorsers) for the non-math.NT records (umbrella v2.0 math.HO,
CT v1.3 math-ph, T2B v3.0 math.HO) per arXiv's per-subject-class
endorsement policy. Identical structure to 034 PHASE D; same
PII-placeholder hygiene; operator personalises before sending.

Phases:
  A — endorser-record subject-fit matrix (≤15 min)
  B — template emission (≤30 min)
  C — handoff (per SOP §B3)

AEAL claims minimum: 3 (this session: 4).
Halt conditions: HALT_ARXIV_POLICY_DRIFT_SINCE_034 /
HALT_NO_SUBJECT_FIT_FOR_RECORD / HALT_PII_LEAK_IN_DRAFT.
None triggered.

Outcome ladder target: COMPLETE_NINE_TEMPLATES_EMITTED (achieved).

Anchor sources used:
  - 034 ARXIV-MIRROR-RUNBOOK-REFIRE (2026-05-04 bridge `0a68c42`)
  - ENDORSER-HANDLE-ACQUISITION (2026-05-04 candidate_dossier.md)
  - 034's zenodo_metadata_5_records.json (Zenodo API readback)
  - arXiv help text policy snapshot from 034 PHASE D (re-cited)
