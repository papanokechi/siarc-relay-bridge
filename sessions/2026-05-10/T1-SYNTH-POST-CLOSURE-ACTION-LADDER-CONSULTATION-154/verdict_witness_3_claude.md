# Witness 3 -- claude-2026-05-10 (Anthropic)

**LABEL:** ACTION_LADDER_RECOMMENDATION
**BAND:** MEDIUM-HIGH
**WITNESS:** single-witness claude-2026-05-10

---

### Q1_RESPONSE -- Zenodo deposit cascade

**Recommendation (Q1a).** Keep the **PCF-2 v1.4 -> Umbrella v2.2 ->
Picture-chain v1.20+** ordering but *treat picture-chain as optional
separate deposit*. If picture-chain is primarily a closure-outlook
narrative, **subsume it into the Umbrella v2.2 deposit as an appendix**
unless there is a clear reason to expose it as a standalone artefact
(e.g., separate authorship, independent reproducibility scripts). This
preserves the governance clarity of the three-step cascade while avoiding
proliferation of low-value standalone deposits.

**Cadence (Q1b).** Stagger deposits to allow Zenodo concept/version
metadata to settle:
  - **PCF-2 v1.4:** deposit **Day 0 (post-lift)**.
  - **Umbrella v2.2:** deposit **Day 1-3** (24-72 hours after PCF-2).
  - **Picture-chain:** deposit **Day 3-7** only if standalone; otherwise
    include in Umbrella v2.2.

**Final-polish checklist (Q1c).**
  - **PCF-2 v1.4:** update front matter to note *post-lift* status and
    include an explicit **M8b caveat** pointer and reproduction appendix;
    confirm that the release_v12 directory contains the final PDF and
    zenodo_description_v1.2.txt updated with post-lift status.
  - **Umbrella v2.2:** apply b_amendment_v22.diff to umbrella_v21.tex,
    compile to produce v2.2 .tex/.pdf, and include a short "Amendment
    summary" file listing diffs; ensure umbrella concept-DOI is verified
    before IsSupplementTo linking.
  - **Picture-chain v1.20+:** if kept separate, assemble a single PDF
    that consolidates M1_M12_CLOSURE_OUTLOOK_*.md into a coherent
    narrative + a small reproduction appendix (scripts + parameter
    ranges). If subsumed, include the assembled picture-chain appendix
    inside Umbrella v2.2.

**Cross-citation discipline (Q1d).** Use **concept-DOI** targets for
IsSupplementTo (not version DOIs).
  - PCF-2 (concept 10.5281/zenodo.19936297) <- Umbrella v2.2
    IsSupplementTo PCF-2 concept DOI.
  - Picture-chain (if separate) IsSupplementTo Umbrella concept DOI (or
    PCF-2 if it is directly supplementing PCF-2).

### Q2_RESPONSE -- M11 arXiv endorsement

**Timing (Q2a).** **Delay endorsement push until after the Zenodo cascade
settles** (i.e., after Umbrella v2.2 is live and DOIs are stable). This
gives the endorsement request a stable reference set and avoids
first-impression confusion.

**Anchor paper (Q2b).** Use **t2b (zenodo 19915689, concept 19783311)**
as the primary endorsement anchor for math.NT. Surface also **t2a
(19774029)** as a secondary candidate.

**Pre-submission discipline (Q2c).**
  - Produce a **one-page cover note** that frames the submission in
    standard math.NT terms.
  - Ensure the **abstract** is mathematically focused (no tooling-state claims).
  - Include **Zenodo concept DOIs** and a short "closure status" paragraph
    using the D-153-3 linguistic firewall.
  - Have a trusted endorser preview the packet.

### Q3_RESPONSE -- M12 4-paper resubmission cadence

**Ordering (Q3a).** Prioritize by (a) strongest math fit and (b)
potential to bootstrap citations:
  1. **t2b (degree-(2,1) Trans-stratum)** -- submit first.
  2. **t2a (degree-(4,2) stratum)** -- submit second.
  3. **Finite-depth transient rigidity (ExpMath candidate)** -- submit third.
  4. **AI Peer Review Founding Position** -- submit last.

**Venue recommendations (Q3b).**
  - **t2b:** Journal of Number Theory (JNT) or Compositio.
  - **t2a:** Experimental Mathematics (ExpMath) or Ramanujan Journal.
  - **Finite-depth transient rigidity:** Experimental Mathematics or
    specialized topology/geometry journal.
  - **AI Peer Review Founding Position:** Philosophy/Science policy outlets
    or commentary section in computational-science journal; consider
    Episciences or open-review venue.

**Risk catalogue (Q3c).** Highest desk-reject risk: **AI Peer Review
Founding Position** (venue mismatch) and **Finite-depth transient rigidity**
(if presentation is too tooling- or numerics-heavy). Mitigations: tailor
each submission; produce crisp cover letter; ensure abstract+intro match
venue's expected framing; pre-check editorial table-of-contents.

### Q4_RESPONSE -- M10 sorry-discharge maintenance

**Cadence (Q4a).**
  - **Weekly:** Lean compile attempts with short CI log entry.
  - **Biweekly:** Blocker-resolution updates and PRs for each attempted fix.
  - **Monthly:** Compiled status snapshot. Artefacts: weekly_compile.log,
    blocker_resolution.md, monthly_status_snapshot.pdf.

**Toolchain approach (Q4b).** Use **systematic blocker-by-blocker** with
parallel branches. Recommended order:
  1. reproduce each blocker in minimal test case
  2. attempt refactor (Pattern alpha) if structural
  3. attempt hypothesis replacement (Pattern beta) only if refactor fails

**Avoid axiom-mode** except as a last-resort documented fallback; prefer
pinned Mathlib version testing.

**Status-report template (Q4c).** Minimum content to satisfy PATH_B
Option α:
  - **Executive summary (1 paragraph)**: current state vs commitment.
  - **Progress log**: list of sorries with status, commits/PRs, dates.
  - **Blocker table**: blocker id; reproduction; attempted fixes; next action.
  - **Artifacts attached**: weekly_compile.log; minimal failing examples;
    CI badges.
  - **Scope:** include both Lean-only and numerical items if relevant.

### Q5_RESPONSE -- M8b caveat preservation & D-153-3 linguistic firewall

**Caveat templates (Q5a).**
  - **Zenodo deposit description (short):** "This deposit preserves the
    M8b d>=3 caveat: certain numerical/assumption regimes remain identified
    as future-work; see Reproduction Appendix for parameter ranges and
    anchor values."
  - **Venue cover letter (short):** "We note an explicit M8b d>=3 caveat
    carried from the post-lift record; relevant reproduction details and
    parameter ranges are provided in the enclosed appendix."
  - **arXiv submission abstract (one-line addition):** "Note: this
    submission preserves an M8b d>=3 caveat from the project closure
    record; reproduction details are in the linked repository."
  - **Conference talk/poster (slide footnote):** "M8b d>=3 caveat
    preserved -- see reproduction appendix (link)."

**Linguistic firewall (Q5b).** Use **SAFE** phrasings and avoid closure language:
  - **SAFE examples:** "M10 sorry-discharge work-stream is on track for
    the 2026-08-02 status-report milestone"; "M10 remains an active
    tooling-state work-stream."
  - **UNSAFE examples (avoid):** "M10 closed"; "M10 V0 achieved"; "M10
    resolved as mathematical theorem."

**Reproduction Appendix template (Q5c).** Include the following fields:
  - **Exact M4 V0 anchor values:** list numeric anchor constants and
    commit SHA.
  - **Numerical scripts:** link(s) to scripts, runtime environment, seed values.
  - **Parameter ranges:** enumerated ranges and sampling strategy.
  - **Execution instructions:** minimal commands and expected outputs.
  - **Data and DOI references:** Zenodo concept DOIs and file-level checksums.

Attach this appendix as a separate file in each Zenodo deposit and
reference it in the deposit description.

---

### AMENDMENTS
- **AMENDMENT 1:** Require that every Zenodo deposit include an explicit
  **"Governance and Caveats"** section that reproduces the M8b caveat
  verbatim and points to the Reproduction Appendix. *Rationale:*
  preserves Q4(4c) mitigation and aligns with RULE 1.
- **AMENDMENT 2:** Delay arXiv endorsement push until Umbrella v2.2 DOI
  is live. *Rationale:* stable references improve endorsement success
  probability.

### ANOMALIES
- **ANOMALY 1:** OP-DP0 packet is HALTED at Phase 2 (literal-trigger
  ambiguity). This consultation is conditional on Path B lift; if
  operator chooses Path A, the ladder must be re-evaluated.
- **ANOMALY 2:** Picture-chain deposit class is ambiguous (closure-outlook
  vs consolidated-narrative); decision required to subsume or separate.

### ABSORPTION_GUIDANCE
**Files to create under**
sessions/2026-05-10/T1-SYNTH-POST-CLOSURE-ACTION-LADDER-CONSULTATION-154/:
  1. verdict.md -- verbatim packet (this file).
  2. cascade_record.md -- single-witness aggregation entry summarizing
     LABEL/BAND.
  3. claims.jsonl -- ~12 meta-claims (e.g., "PCF-2 deposit Day 0
     recommended", "M8b caveat must be preserved").
  4. discrepancy_log.json -- note HALTED OP-DP0 and picture-chain ambiguity.
  5. halt_log.json -- {} (no halt).
  6. unexpected_finds.json -- include OP-DP0 Phase 2 HALT note.
  7. handoff.md -- include next actions: operator adjudicate Path B;
     prepare PCF-2 deposit; assemble Umbrella v2.2; prepare M10 weekly
     CI schedule.

**SQL / TODO updates:** create TODOs for: deposit_pcf2_day0,
assemble_umbrella_v22, decide_picture_chain_subsumption,
prepare_arxiv_endorsement_packet_after_umbrella.

**Follow-up fires:** trigger T1 fire for ZENODO_DEPOSIT_EXECUTION once
operator confirms Path B; trigger T1 M10_STATUS_REPORT_PREP 2 weeks before
2026-08-02.

### ONE-LINE TAKEAWAY
Preserve M8b caveat; stagger PCF-2 -> Umbrella; delay arXiv until DOIs settle.
