================================================================
SIARC RESEARCHER PROMPT 021 — ADAMS-1928-FINAL-ACQUISITION-PROBE
================================================================
TASK ID:        ADAMS-1928-FINAL-ACQUISITION-PROBE
COMPOSED:       2026-05-04 ~12:45 JST
DRAFTED-BY:     Copilot CLI (Claude Opus 4.7 xhigh)
AGENT:          Copilot researcher (web-search across OA
                routes; possibly Tier-1 ILL recommendation
                if no OA succeeds).
GATES:          NEW PROMPT (NOT YET QUEUED); closes G3b residual
                (ii) "Adams 1928 NIA on disk" per A-01 verdict.
                Parallel-safe with all other v1.17 tasks.
PRIOR ANCHORS:  T1-A01-NORMALIZATION-RESOLUTION verdict
                `A01_WASOW_READING_CONFIRMED` 2026-05-03 (bridge
                `bbc905d`); transitive evidence (via Birkhoff /
                B-T) sufficient for current scope; primary Adams
                remains nice-to-have for tighter verdicts.
                Lessons-learned from R5 retries 2026-05-04
                (R5-OKAMOTO-NUMDAM-RETRY SHA `65294fbc`):
                Japanese-math-society convention surfaced for
                Okamoto FE 30; analogous direct-publishing-
                institution route may apply to Adams 1928.
COMPUTE BUDGET: ~1-2 hr researcher (multiple-OA-route survey;
                URL discovery + status-check + acquisition
                if route found).
RUNTIME PROFILE:Web-fetch primarily. Per Rule 2: no on-behalf
                ILL submission; no browser-driver. Per Rule 1:
                no API keys.

[Body of prompt as supplied by operator; full text matches the
relay-prompt body delivered to the agent on 2026-05-04 ~12:45 JST.
Reproduced verbatim above the §1 / §2 / ... section breaks.
See the conversation log for the canonical copy. This file
serves as the per-task provenance anchor per Phase 0.]

================================================================
§0 GOAL
================================================================

Adams "On the irregular cases of the linear ordinary difference
equation", Trans. AMS 30 (1928), pp. 507-541, is the cited
σ-normalization primary source in T1 lit-review and T1-A01.
T1-A01 verdict A01_WASOW_READING_CONFIRMED (2026-05-03) closed
the G3b residual via TRANSITIVE evidence (Birkhoff 1930 + B-T
1933 + Wasow 1965); Adams 1928 was NIA on disk. This prompt is
the FINAL OA acquisition probe.

================================================================
§1 ANCHOR FILES
================================================================

  sessions/2026-05-02/T1-BIRKHOFF-TRJITZINSKY-LITREVIEW/handoff.md
  sessions/2026-05-03/T1-A01-NORMALIZATION-RESOLUTION/handoff.md
  tex/submitted/control center/literature/g3b_2026-05-03/SHA256SUMS.txt
  tex/submitted/control center/picture_revised_20260504.md  (§5 G3b row)

================================================================
§2 PHASES
================================================================

  PHASE 0 — provenance write-out (this file).
  PHASE A — bibliographic confirmation.
  PHASE B — survey OA routes (AMS, JSTOR, zbMATH-Open, EuDML,
            Internet Archive, Project Euclid, Brown, archives).
  PHASE C — validate + acquire (if any route succeeds) or
            recommend ILL (operator-side; per Rule 2).
  PHASE D — verdict aggregation + cross-validation against
            transitive evidence (T1-A01 baseline).
  PHASE E — handoff.md + AEAL claims (≥ 5).

================================================================
§3 AEAL CLAIMS MINIMUM
================================================================

≥ 5 entries.

================================================================
§4 HALT CONDITIONS
================================================================

  HALT_ADAMS_DIRECT_DISAGREES_WITH_TRANSITIVE
  HALT_ADAMS_TEXT_LAYER_BAD
  HALT_ADAMS_ALL_OA_ROUTES_FAIL
  HALT_ADAMS_AMS_API_PAYWALL

================================================================
§5 FORBIDDEN-VERB HYGIENE  (per _RULES.txt §D)
================================================================

  Standard hygiene; quotes ≤ 30 words; "agrees to N-units" /
  "is consistent with"; never "shows" / "confirms" / "proves".

================================================================
§6 OUT OF SCOPE
================================================================

  No browser auth, no on-behalf ILL, no API keys, no T1-A01
  re-run unless HALT_ADAMS_DIRECT_DISAGREES triggers.

================================================================
§7 OUTCOME LADDER
================================================================

  UPGRADE_ADAMS_ACQUIRED_AGREES_WITH_TRANSITIVE
  UPGRADE_ADAMS_AMS_ROUTE_ACQUIRED
  UPGRADE_ADAMS_NIA_ILL_RECOMMENDED_<library>
  HALT_ADAMS_DIRECT_DISAGREES_WITH_TRANSITIVE
  HALT_ADAMS_* (other; see §4)

================================================================
§8 STANDING FINAL STEP  (B1-B5 per _RULES.txt §H)
================================================================
