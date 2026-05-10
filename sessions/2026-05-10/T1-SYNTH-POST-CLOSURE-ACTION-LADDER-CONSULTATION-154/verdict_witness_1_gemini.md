# Witness 1 -- Gemini-2026-05-10 (Google)

**LABEL:** ACTION_LADDER_RECOMMENDATION
**BAND:** MEDIUM-HIGH
**WITNESS:** single-witness Gemini-2026-05-10

---

## Q1_RESPONSE: Zenodo Deposit Cascade

**Q1a:** The sequence `PCF-2 v1.4 -> Umbrella v2.2 -> Picture-chain v1.20+`
remains structurally sound. The Picture-chain artefact should **not** be
subsumed into the umbrella. Subsuming an administrative "closure-outlook"
narrative into a primary mathematical peer-review target risks diluting
the rigor of the umbrella paper. Deposit the OUTLOOK_*.md series as a
discrete supplementary dataset.

**Q1b:** Recommended cadence is **24 hours** between deposits. This
interval is strictly necessary to allow Zenodo's indexing to settle,
ensuring the concept-DOI is fully propagated and reliable before injecting
it into the IsSupplementTo metadata field of the subsequent deposit.

**Q1c:** Final-polish requirements:
  * **PCF-2 v1.4:** Update the zenodo_description_v1.2.txt to inject the
    S153 Q4(4c) reproduction checklist and explicit M8b d>=3 caveats.
  * **Umbrella v2.2:** Final assembly is mandatory. Apply b_amendment_v22.diff
    and generate the final v22.tex/pdf locally. Do not upload raw diffs as
    primary manuscript files.
  * **Picture-chain v1.20+:** Consolidate the M1_M12_CLOSURE_OUTLOOK_*.md
    files into a single master PDF/Markdown pair to reduce reader friction.

**Q1d:** Cross-citation discipline confirmed:
  * PCF-2 v1.4 IsSupplementTo -> PCF-1 concept-DOI (10.5281/zenodo.19931635)
  * Umbrella v2.2 IsSupplementTo -> PCF-2 concept-DOI (10.5281/zenodo.19936297)
  * Picture-chain IsSupplementTo -> Umbrella concept-DOI (TBD from v2.1 record)

## Q2_RESPONSE: M11 arXiv Endorsement Workstream

**Q2a:** Delay the endorsement push until **48 hours after** the final
Zenodo picture-chain deposit settles. This allows you to cite the permanent,
resolved Zenodo concept-DOIs within the arXiv metadata and cover letter,
establishing immediate provenance and stability to the endorser/moderator.

**Q2b:** The **t2b degree-(2,1) paper** (Zenodo 19915689) is the optimal
anchor. It represents the highest mathematical density and cleanest
alignment with the math.NT category. Lead with this artefact for the
endorsement request.

**Q2c:** To mitigate one-shot endorsement rejection risk, implement strict
pre-submission discipline:
  * Ensure the abstract explicitly states the computational bounds and
    structural caveats (e.g., d>=3 limitations).
  * Do not mention "AI Peer Review" or internal project syntax (e.g.,
    "M1-M12", "sorries") in the abstract or arXiv comments field.
  * Frame the closure narrative purely in standard mathematical community
    terms (e.g., "We establish bounds for...").

## Q3_RESPONSE: M12 4-Paper Resubmission Cadence

**Q3a:** Recommended ordering:
  1. **Item 10 (t2b)**: Strongest artefact. Submitted first to establish momentum.
  2. **Item 8 (Finite-depth)**: High technical rigor; benefits from t2b being in peer-review.
  3. **Item 9 (t2a)**: Follows Item 8 closely.
  4. **Item 7 (AI Position)**: Highest risk; delay until mathematical papers
     are securely under review.

**Q3b:** Venue recommendations:
  * **t2b (degree-(2,1)):** Experimental Mathematics (ExpMath). Highly
    aligned with numerical bound verification and rigorous computational claims.
  * **Finite-depth / t2a:** Compositio Mathematica or International Journal
    of Number Theory (IJNT), depending on the length and theoretical
    density of the final drafts.
  * **AI Position:** Avoid standard math journals. Target broad-scope
    computational or meta-science venues to bypass the Episciences/AFM
    8-minute desk-reject pattern.

**Q3c:** **Item 7 (AI Position)** is the highest risk for desk-rejection
because it breaks the genre expectations of a standard mathematical journal.
Mitigation: Strip all internal "project management" jargon. Frame it
strictly as an epistemological analysis of automated proof verification in
number theory.

## Q4_RESPONSE: M10 Sorry-Discharge Maintenance

**Q4a:** Recommended cadence: **Bi-weekly Lean compile attempts** and a
**monthly** per-blocker discharge log committed to the bridge.

**Q4b:** Toolchain protocol for WallisFamily.lean:
  * Pin the Mathlib version immediately to prevent moving-target regressions.
  * Adopt parallel branches for the 5 enumerated blockers.
  * Apply **Pattern alpha (refactor)** for the two
    Thm66_ApparentSingularity.lean sorries, as singularities usually
    require structural algebraic refactoring.
  * Apply **Pattern beta (hypothesis replacement)** for proof_targets.lean.

**Q4c:** The 2026-08-02 status report must contain:
  1. A Lean-only delta report showing the sorry count reduction.
  2. A reproducible build matrix (OS, Lean version, Mathlib commit).
  3. Explicitly exclude any mathematical-content revisions (governance firewall).

## Q5_RESPONSE: Q4(4c) Mitigation + D-153-3 Governance

**Q5a:** M8b d>=3 Caveat Template:
> "Note: Rigorous bounds are established up to d=2. Numerical validation
>  for d>=3 retains structural caveats and is deferred to future work,
>  per V0 closure parameters."

**Q5b:** D-153-3 Linguistic Firewall Template:
> "The M10 tooling-state workstream is actively progressing toward its
>  2026-08-02 milestone. This tracks exclusively with Lean formalization
>  architecture and is fully decoupled from the foundational M1-M9
>  mathematical content closure, which was definitively achieved in V0."

**Q5c:** Reproduction Appendix Template:
```markdown
### Appendix: Reproduction Checklist
*   **Target:** M4 V0 Anchor Values
*   **Numerical Scripts:** [Insert URL/Path to Zenodo dataset]
*   **Parameter Ranges:** Verified for bounds d <= 2. Extrapolations for
    d >= 3 remain heuristically constrained.
*   **Execution Environment:** [Insert Python/C++ version, library dependencies]
```

---

### AMENDMENTS
* **M11 Timing Shift:** Adjusted the M11 arXiv endorsement push to occur
  *after* the Zenodo cascade fully settles, rather than running concurrently,
  to ensure metadata stability.

### ANOMALIES
* No critical anomalies detected in the provided substrate state. The
  dependency on operator adjudication for OP-DP0 Path B is noted and
  accepted as a precondition for this ladder.

### ABSORPTION_GUIDANCE
* CLI agent to write this output to verdict.md.
* Generate claims.jsonl extracting the 4 concrete venue recommendations,
  the 24-hour Zenodo cadence, and the M10 bi-weekly check interval.
* Stage SQL todo updates to flag t2b as the M11 anchor and queue the
  bi-weekly M10 chron-job.

### ONE-LINE TAKEAWAY
Execute 24h Zenodo cascade, anchor arXiv push on t2b, firewall M10
strictly to tooling.
