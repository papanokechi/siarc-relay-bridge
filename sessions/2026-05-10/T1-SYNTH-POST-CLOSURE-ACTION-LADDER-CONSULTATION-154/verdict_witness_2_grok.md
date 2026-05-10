# Witness 2 -- grok-xai-2026-05-10 (xAI)

**LABEL:** ACTION_LADDER_RECOMMENDATION
**BAND:** MEDIUM
**WITNESS:** single-witness grok-xai-2026-05-10

---

### Q1_RESPONSE
**Q1a:** Confirm the Option α ordering: PCF-2 v1.4 -> Umbrella v2.2 ->
Picture-chain v1.20+. No strong governance or cross-citation reason to
reorder; PCF-2 is the most self-contained core artefact and provides the
cleanest base for subsequent IsSupplementTo links. Picture-chain v1.20+
**should be deposited separately** as a distinct closure-outlook /
consolidation narrative artefact rather than fully subsumed. It serves a
different communicative function (high-level synthesis) and benefits from
its own version-DOI for downstream referencing in talks or M11/M12 cover
letters.

**Q1b:** Cadence recommendation: same-day for all three if final polish
is complete (minimal risk of DOI settlement issues for internal
cross-links), or PCF-2 today + Umbrella + Picture within 24h. Prioritize
settling PCF-2 first.

**Q1c:**
  - **PCF-2 v1.4**: Minimal updates required post-S153. Add a short
    post-closure note in zenodo_description_v1.2.txt referencing S153
    quad-witness CONFIRM_CLOSURE (bridge 4761392) and the M8b d>=3
    caveat. Update submission_log_patch_item15.txt with final closure
    status. No content changes to core PDFs/tex.
  - **Umbrella v2.2**: Yes — apply b_amendment_v22.diff, generate clean
    v22.tex/pdf with updated metadata page referencing full M1-M12
    scoreboard from S153.
  - **Picture-chain v1.20+**: Deposit the consolidated
    M1_M12_CLOSURE_OUTLOOK_*.md series (or a single master outlook.md
    assembled from them) plus any key figures.

**Q1d:** IsSupplementTo graph (concept-DOIs only):
  PCF-2 (10.5281/zenodo.19936297) IsSupplementTo PCF-1 (10.5281/zenodo.19931635).
  Umbrella v2.2 IsSupplementTo PCF-2.
  Picture-chain v1.20+ IsSupplementTo Umbrella v2.2 (and optionally PCF-2).

### Q2_RESPONSE
**Q2a:** Immediately post-lift (within 1-3 days of Zenodo cascade
completion) while momentum is high, but after Zenodo DOIs are live for
clean referencing.

**Q2b:** Yes — use t2b degree-(2,1) Trans-stratum (zenodo 19915689 /
concept 19783311) as the primary anchor. It appears strongest for
math.NT. Surface t2a degree-(4,2) stratum as secondary/supporting preprint.

**Q2c:** Pre-submission discipline: (1) Conservative abstract framing
that clearly distinguishes math-content closures (M4/M9 etc.) from
tooling-state progress (M10); (2) Prominent Reproduction Appendix for
M8b caveat; (3) Clean math.NT categorization with minimal Lean-specific
jargon in first 1-2 pages; (4) Explicit forward-looking statement on M10
status-report commitment without overclaiming. First-impression risk is
moderate—lean toward understatement on formalization completeness.

### Q3_RESPONSE
**Q3a:** Recommended ordering: Item 8 (Finite-depth transient rigidity)
-> Item 9 (t2a) -> Item 10 (t2b) -> Item 7 (AI Peer Review). This builds
progressive subject-area and citation bootstrap (rigidity -> strata ->
broader implications).

**Q3b:**
  - Item 8: Experimental Mathematics (strong fit for computational/rigidity results).
  - Item 9/10: International Journal of Number Theory or Ramanujan Journal
    (stratum / trans-stratum work).
  - Item 7: Compositio or a philosophy-of-math / AI+math venue if
    available; fallback to ExpMath.

**Q3c:** Highest desk-reject risk: Item 7 (AI Peer Review Founding
Position) due to interdisciplinary nature and prior AFM-style snap
rejection memory. Mitigation: Extremely tight abstract (first 150 words
purely mathematical or methodological), clear positioning as "founding
position" rather than empirical claim, and pre-circulation to 1-2 friendly
readers if possible.

### Q4_RESPONSE
**Q4a:** Cadence: Bi-weekly Lean compile + blocker progress log
(artefact: build_status_YYYY-MM-DD.md) through 2026-08-02, with one
deeper monthly review.

**Q4b:** Systematic blocker-by-blocker on WallisFamily.lean; prioritize
Mathlib version pin upgrade where safe before axiom-mode fallback. For
the 3 sorries: prefer Pattern alpha (refactor) where feasible; beta
(hypothesis replacement) only for irreducible residuals. Track in
dedicated sorry_discharge_log.md.

**Q4c:** Minimum content for 2026-08-02 report: (1) Current build status
summary, (2) Discharged sorries list with diffs, (3) Remaining blockers
with ETA, (4) Reproduction notes for any numerical claims tied to M4 V0.
Cover both Lean and any supporting numerical validation. Suggested
template: Status_Report_M10_20260802.md with sections Overview, Progress
Metrics, Blockers & Mitigation, Next Milestones.

### Q5_RESPONSE
**Q5a:** M8b caveat template (adaptable):
> "Note on M8b: The V0 result carries a d>=3 caveat. Numerical reproductions
>  and parameter ranges are provided in the Reproduction Appendix. This
>  remains an active area for future tightening."

Place in Zenodo descriptions, cover letters, and arXiv abstracts (shorter version).

**Q5b:** Linguistic firewall:
  - SAFE: "M10 sorry-discharge work-stream / Lean formalization progress
    is advancing toward the 2026-08-02 status-report commitment."
  - UNSAFE: Any phrasing implying "M10 closed", "M10 V0 achieved", or
    treating it as math-content equivalent to M4/M9.

**Q5c:** Reproduction Appendix template (append to deposits):
  - Links to numerical scripts (exact commit SHAs).
  - Parameter ranges used.
  - Exact M4 V0 anchor values.
  - M8b d>=3 caveat statement.
  - Environment / Mathlib version pin.
  - Expected outputs / checksums where practical.

### AMENDMENTS
None material. Minor clarification: explicitly flag Picture-chain as
"consolidation narrative" rather than primary research paper in its
Zenodo metadata.

### ANOMALIES
None detected in provided substrate summary. OP-DP0 Path B appears
well-supported by prior verdicts.

### ABSORPTION_GUIDANCE
CLI agent should: (1) Write verdict.md + cascade_record.md + claims.jsonl
in the 154 bridge folder; (2) Create/update the three recommended
final-polish artefacts (PCF-2 note, umbrella v22 assembly, Picture master
outlook); (3) Draft M10 bi-weekly log template and Reproduction Appendix
stub; (4) Trigger follow-up fire for post-Zenodo M11 endorsement package
review. No immediate dual-witness needed.

### ONE-LINE TAKEAWAY
Disciplined, caveat-preserving ladder: Zenodo cascade first, then parallel
M11/M12 + M10 maintenance.
