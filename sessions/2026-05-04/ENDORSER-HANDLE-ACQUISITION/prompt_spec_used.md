# Prompt spec used (verbatim)

```
================================================================
SIARC RESEARCHER PROMPT 022 — ENDORSER-HANDLE-ACQUISITION
================================================================
TASK ID:        ENDORSER-HANDLE-ACQUISITION
COMPOSED:       2026-05-04 ~12:50 JST
DRAFTED-BY:     Copilot CLI (Claude Opus 4.7 xhigh)
AGENT:          Copilot researcher (web-search via arXiv author
                pages + Google Scholar; bibliographic candidate
                identification).
GATES:          NEW PROMPT (NOT YET QUEUED); closes G14
                (endorsement-request templates skeleton; no
                real endorser arXiv handles populated). Gates
                Prompt 002 (arXiv mirror runbook for math.NT
                records #2 + #4 = PCF-2 v1.3 + CT v1.3) re-fire
                downstream.
PRIOR ANCHORS:  002_arxiv_mirror_runbook_EXECUTED.txt 2026-05-02
                (verdict ARXIV_MIRROR_HALTED_PAGE_COUNT_DRIFT_2;
                4/5 OK; PCF-1 21pp local vs 16pp Zenodo);
                v1.17 picture §5 G14; existing endorsement-
                request templates at sessions/2026-05-02/ARXIV-
                MIRROR-RUNBOOK/.
COMPUTE BUDGET: ~1-2 hr researcher (3 candidate endorsers ×
                arXiv handle lookup + paper-recency check +
                bibliographic-citation alignment).
RUNTIME PROFILE:Web-fetch on arxiv.org/a/<handle> + Google
                Scholar profiles + author-paper-list cross-
                check. Per Rule 2: no auto-submission of
                endorsement requests; surface candidate list +
                populated templates only.
```

(Full §0–§8 body of prompt 022 transcribed verbatim from the relay
prompt; reproduced inside this session folder for provenance. The
text above is excerpted; the full prompt body is preserved by the
relay-prompt log on the operator side.)

## Spec drift acknowledged

The prompt §0 refers to **"PCF-2 v1.3 (record #2)"**. The runbook
deliverable that actually exists at
`sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/` is
`ENDORSEMENT_REQUEST_pcf1_v1.3.md` (record #2 = **PCF-1 v1.3**,
not PCF-2). PCF-2 v1.3 ships in 2026-05-02 ARXIV-MIRROR-RUNBOOK
without an endorsement-request template (the runbook covers PCF-1,
CT, T2B, SIARC umbrella, and PCF-2 — but only PCF-1 and CT have
endorsement-request templates because both target categories
(math.NT + math.CA) are first-time submissions for the SIARC
author; PCF-2 reuses the math.NT endorsement obtained for PCF-1).

Resolved by treating the existing two templates as canonical:

  - **Record #2** — `ENDORSEMENT_REQUEST_pcf1_v1.3.md` (math.NT)
  - **Record #4** — `ENDORSEMENT_REQUEST_ct_v1.3.md`    (math.CA)

The math.NT endorsement obtained for PCF-1 v1.3 will, per arXiv's
single-endorsement-per-category rule, also cover PCF-2 v1.3
(record #5 in the runbook, math.NT primary).

Drift is logged to `discrepancy_log.json` and surfaced in
`handoff.md` § Anomalies.
