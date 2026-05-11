# S154 Post-RULE-1-Lift Admin Runbook

**Source:** slot 154 verdict (bridge `26d7bf5`; QUAD-WITNESS ACTION_LADDER_RECOMMENDATION_WITH_AMENDMENT @ MEDIUM)
**Compiled:** 2026-05-11
**Compiled-by:** T2-Executor slot 186 (PROMPT 186 in-CLI single-turn fire)
**Status:** ready-for-execution post RULE 1 lift (2026-05-10 via Path B documented-commitment)

---

## Purpose

Consolidate the 5 aggregated S154 amendments (W1+W3+W4 union) into a single executable checklist with verbatim template references. Canonical reference for every post-RULE-1-lift dissemination artefact (Zenodo deposits, arXiv submissions, venue cover letters, conference talks).

---

## Amendment checklist

### Amendment 1 -- Picture-chain default = SUBSUME

* **Decision rule:** any new picture-chain content defaults to subsumption into the parent artefact (Umbrella v2.3 Appendix-C per Q-v23-2 = A FOLD) rather than independent Zenodo mint.
* **Trigger:** any picture-chain content accumulation (new chapter, new section, new visual).
* **Action:** incorporate into Umbrella v2.3 Appendix-C. Flag for separate-deposit re-vet ONLY if BOTH (i) content matures past meta-only AND (ii) operator explicitly requests.
* **Coupling:** ratified via slot 183 Pick 2 (UF-167-1 DEFER). C-183-1 mandatory re-vet gate does NOT apply (Q-v23-2 was operator-confirmed pre-waiver).
* **Status:** ACTIVE

### Amendment 2 -- Delay arXiv push until Zenodo DOIs stabilize

* **Decision rule:** do not push to arXiv until ALL referenced Zenodo deposits have stabilized DOIs (i.e., zero pending Edit operations).
* **Current Zenodo state (2026-05-11):**
  * PCF-2 v1.4 (`10.5281/zenodo.20114315`): PENDING 3 Edit operations per `slot-155-followup-zenodo-edit-pcf2-v14`
  * Branch-W (Zenodo record TBC): PENDING 4 Edit operations per `branch-w-zenodo-cosmetic-edits`
  * Umbrella v2.2 (`10.5281/zenodo.20114861`): STABLE
  * PCF-1 v1.3 (`10.5281/zenodo.19937196`): STABLE
* **Action gate:** Zenodo Edits MUST land BEFORE any arXiv push that references either PCF-2 v1.4 or branch-W.
* **Status:** ACTIVE (blocked until both Zenodo Edit cascades complete)

### Amendment 3 -- Mandatory linguistic firewall paragraph

* **Decision rule:** every Zenodo deposit description + every paper section-1 includes the D-153-3 canonical firewall paragraph distinguishing M10 (tooling-state work-stream; deferred-with-commitment) from M1-M9 (mathematical-content closure; achieved in V0).
* **Template:** bridge `26d7bf5` `templates/d_153_3_firewall_template.md` (canonical sentence + SAFE/UNSAFE phrasings) -- inlined verbatim below as **Template 2**.
* **Action:** copy canonical sentence + SAFE variant into deposit metadata; NEVER use UNSAFE variant.
* **Status:** ACTIVE for all future deposits

### Amendment 4 -- Pin Mathlib / toolchain during M10 discharge

* **Decision rule:** when M10 V0 Lean discharge resumes (post 148R iter-14-class remediation), the Mathlib commit SHA + lean-toolchain version MUST be pinned and recorded in the discharge commit message header.
* **Reason:** prevents the iter-14 import-substitute failure mode from recurring; preserves reproducibility.
* **Action gate:** 148R iter-14 remediation fire MUST record pinned-commit + pinned-toolchain in commit message header AND in any Zenodo deposit Section 5 (Execution environment).
* **Status:** PENDING-EXECUTION (no M10 discharge fire active; gate triggers on next 148R-class fire)

### Amendment 5 -- Mandatory M8b caveat section in every Zenodo deposit

* **Decision rule:** every Zenodo deposit description includes a section noting the M8b sub-leading Stokes constant PERMANENT_RESIDUAL classification.
* **Template:** bridge `26d7bf5` `templates/m8b_caveat_template.md` (4 context variants + composite single-paragraph fallback) -- inlined verbatim below as **Template 1**.
* **Action:** select the context-matching variant; paste into deposit description ABOVE the firewall paragraph.
* **Status:** ACTIVE for all future deposits

---

## Composite execution checklist (for next Zenodo deposit)

### Pre-fire (all amendments)

- [ ] Select context-matching M8b caveat variant from **Template 1** below (Amendment 5)
- [ ] Select D-153-3 firewall canonical sentence + SAFE phrasing from **Template 2** below (Amendment 3)
- [ ] Verify any picture-chain content is destinated for Umbrella v2.3 Appendix-C (Amendment 1)
- [ ] Verify no concurrent arXiv push attempt for any artefact referencing pending-Edit Zenodo records (Amendment 2 gate)
- [ ] If Lean-content involved: pin Mathlib + lean-toolchain in deposit Section 5 + commit message (Amendment 4 gate)
- [ ] Attach a populated Reproduction Appendix (**Template 3** below) as a sibling file in the deposit

### Composition order (top-to-bottom in deposit description)

1. Header (title, version, abstract)
2. **M8b caveat section** (Amendment 5; one of 4 context variants from Template 1)
3. **Linguistic firewall paragraph** (Amendment 3; canonical sentence from Template 2)
4. Standard methodology summary
5. Reference to attached **Reproduction Appendix** (Template 3)
6. References + DOI cross-links

### Post-fire

- [ ] If arXiv push planned: confirm ALL referenced Zenodo DOIs stabilized (Amendment 2)
- [ ] Update SIARC governance ledger with deposit DOI + S154-compliance attestation (e.g., `S154-COMPLIANT: A1=SUBSUME, A2=zenodo-stabilized, A3=firewall-present, A4=mathlib-pinned, A5=m8b-caveat-present`)
- [ ] Apply Template 1 audit checklist + Template 2 audit checklist + Template 3 audit checklist (~25 items total)

---

## Halt conditions (runbook execution)

* ANY amendment cannot be executed mechanically for a specific deposit -- surface to operator
* Template content drifts from bridge `26d7bf5` baseline -- refresh from bridge
* S154 verdict re-vetted with amendment changes -- re-fire runbook
* New amendment surfaces from a future S-class consultation -- append (do not re-fire this runbook; amend in place with new SHA reference)

---

## Cross-references

* S154 verdict: `T1-SYNTH-POST-CLOSURE-ACTION-LADDER-CONSULTATION-154` bridge `26d7bf5`
* Slot 183 ratification (Pick 2 / Q-v23-2 / UF-167-1 DEFER): bridge `e175c7a`
* Cascade-132 PATH_B Option-alpha deposit chain: bridge `887981b` (slot 135 umbrella v2.2) / `45e236c` (slot 137 PCF-2 v1.4) / `b9aa881` (slot 136 picture-chain v1.20+)
* OP_A2 fleet.yaml commitment-flip: bridge `7786a67`
* Slot 139 BUNDLED-DEFERRED-NOTE (tooling-state-axis distinction): bridge `72bb2c2`
* RULE 1 lift (Path B documented-commitment): claude-chat `bfcfd92` (2026-05-10)

---

# Template 1 -- M8b caveat template (verbatim from bridge `26d7bf5`)

# M8b d>=3 Caveat Template (S154-synthesized)

**Source:** S154 quad-witness Q5a aggregate (Gemini / Grok / Claude / GPT-5.5)
**Purpose:** Preserve M8b d>=3 caveat across every post-lift dissemination artefact.
**Provenance:** synthesized from
sessions/2026-05-10/T1-SYNTH-POST-CLOSURE-ACTION-LADDER-CONSULTATION-154/verdict_witness_{1..4}_*.md Q5a sections.

---

## Context-1 -- Zenodo deposit description

> "Results involving the d>=3 regime remain subject to the M8b caveat
>  carried forward from the V0 closure substrate. Numerical and structural
>  observations are preserved as reported; higher-dimensional generalization
>  should be interpreted as future-work territory rather than finalized
>  universality claims. See the Reproduction Appendix for parameter ranges
>  and exact anchor values."

**Insertion point:** zenodo_description.txt, immediately following the
"Methods" or "Scope" paragraph; before the "Reproducibility" section.

---

## Context-2 -- Venue cover letter

> "We note an explicit M8b d>=3 caveat carried from the post-lift project
>  record: the manuscript preserves caveat language regarding the d>=3
>  regime and does not claim complete higher-dimensional closure beyond
>  the validated substrate described herein. Relevant reproduction details
>  and parameter ranges are provided in the enclosed appendix."

**Insertion point:** cover letter, paragraph 2 or 3 (after summary of
contribution, before reviewer-suitability paragraph).

---

## Context-3 -- arXiv submission abstract / endorsement note

**Long form (abstract body, ~30 words):**
> "Note: this submission preserves an M8b d>=3 caveat carried from the
>  closure record; certain higher-dimensional extensions remain conditional
>  and are identified explicitly as caveated directions for future
>  investigation. Reproduction details are in the linked repository."

**Short form (one-line, for tight abstracts):**
> "Note: rigorous bounds are established up to d=2; numerical validation
>  for d>=3 retains structural caveats and is deferred to future work."

**Insertion point:** abstract, final sentence (before keyword list).

---

## Context-4 -- Conference talk / poster (slide footnote)

**Slide footnote form:**
> "M8b d>=3 caveat preserved -- see reproduction appendix (link)."

**Slide bullet form (when caveat itself is the topic):**
> "d>=3 behavior remains an open/caveated extension layer; numerical
>  reproductions and parameter ranges are provided in the Reproduction Appendix."

**Insertion point:** footnote of the slide that first asserts a d-dependent
result; bullet on a "Limitations / Future Work" slide.

---

## Composite single-paragraph fallback (for compact contexts)

When a single fixed paragraph must serve all four contexts:

> "Note on M8b: rigorous bounds are established up to d=2. Numerical
>  validation for d>=3 retains structural caveats and is deferred to
>  future work, per V0 closure parameters. Higher-dimensional
>  generalization should be interpreted as future-work territory rather
>  than finalized universality claims; reproduction details, parameter
>  ranges, and exact M4 V0 anchor values are provided in the Reproduction
>  Appendix (see linked repository)."

---

## Audit checklist (apply before each artefact upload)

- [ ] M8b caveat language present in deposit description / abstract / cover letter
- [ ] Caveat language references the Reproduction Appendix
- [ ] Caveat does NOT use closure-rhetoric ("M8b solved", "d>=3 resolved")
- [ ] Caveat is consistent across all parallel artefacts (Zenodo / arXiv / cover)
- [ ] Reproduction Appendix file is attached and link resolves


---

# Template 2 -- D-153-3 linguistic firewall template (verbatim from bridge `26d7bf5`)

# D-153-3 Linguistic Firewall Template (S154-synthesized)

**Source:** S154 quad-witness Q5b aggregate (Gemini / Grok / Claude / GPT-5.5)
**Purpose:** Maintain firewall between M10 (tooling-state work-stream;
deferred-with-commitment) and M1-M9 (mathematical-content closure;
definitively achieved in V0). Prevent governance ambiguity / reputational
coupling risk in post-lift dissemination artefacts.
**Provenance:** synthesized from
sessions/2026-05-10/T1-SYNTH-POST-CLOSURE-ACTION-LADDER-CONSULTATION-154/verdict_witness_{1..4}_*.md Q5b sections.

---

## Canonical firewall sentence (drop-in)

> "M10 refers exclusively to Lean formalization / tooling-state progress
>  toward the 2026-08-02 status-report milestone, and should not be
>  interpreted as an independent mathematical closure claim. The
>  foundational M1-M9 mathematical-content closure was definitively
>  achieved in V0 and is fully decoupled from M10."

**Insertion point:** every Zenodo deposit description; every venue cover
letter; every arXiv comments field referencing closure status; internal
summary documents that touch both M-axes.

---

## SAFE phrasings (use these)

| Domain                      | Phrase                                                              |
|----------------------------|---------------------------------------------------------------------|
| Tooling-state work          | "M10 tooling-state workstream"                                       |
| Progress framing            | "M10 sorry-discharge work-stream"                                    |
| Lean formalization scope    | "Lean formalization maintenance stream"                              |
| Time-anchored commitment    | "M10 status-report milestone (2026-08-02)"                           |
| Toolchain context           | "Lean/Mathlib toolchain stabilization"                               |
| Forward direction           | "actively progressing toward the 2026-08-02 milestone"               |
| Decoupling assertion        | "fully decoupled from the M1-M9 mathematical content closure"        |
| Substrate distinction       | "M10 is a tooling-state axis, not a math-content axis"               |

## UNSAFE phrasings (avoid these)

| Phrase                                | Why unsafe                                                  |
|---------------------------------------|-------------------------------------------------------------|
| "M10 closed"                          | Falsely implies V0 closure parity with M1-M9                |
| "M10 V0 achieved"                     | Conflates tooling-state with math-content V0                |
| "M10 resolved as mathematical theorem"| Genre confusion; falsely promotes tooling status            |
| "formalization completed"             | Premature absent literal sorry-count = 0 + clean compile    |
| "M10 proved"                          | Category error; M10 is not a theorem                        |
| "M10 done"                            | Ambiguous; risks operator-tier governance ambiguity         |

---

## Standard placements

### Zenodo description
Insert canonical firewall sentence immediately after the "Scope of
contribution" paragraph; before the "Reproducibility" or "Methods" section.

### Venue cover letter
Insert canonical firewall sentence in the "Status of related work-streams"
paragraph (or create one if absent). Critical when the cover letter
references the broader project for context.

### arXiv abstract / comments
Use SHORT form in `\comments` field when overall comment field touches
on closure status:

> "M10 (Lean formalization) remains a tooling-state work-stream toward a
>  2026-08-02 status report; this submission concerns mathematical-content
>  results that are fully decoupled from M10."

### Internal documents (cli_log, weekly status, picture-chain)
Use canonical sentence in the abstract or executive summary of any
document that mentions both M1-M9 closure and M10 status.

---

## Audit checklist (apply before each artefact ships)

- [ ] No occurrence of "M10 closed" / "M10 V0 achieved" / similar UNSAFE phrasings
- [ ] Canonical firewall sentence present in every deposit description / cover letter that references closure status
- [ ] M10 always paired with "tooling-state" or "Lean formalization" qualifier
- [ ] M10 always references the 2026-08-02 milestone when discussing forward direction
- [ ] M1-M9 closure language stays distinct from M10 progress language
- [ ] Ensure caveat survives any LaTeX -> PDF compilation step (check final PDF)

---

## Cross-reference

* Original D-153-3 anomaly: T1-SYNTH-M1-M12-CLOSURE-CONFIRMATION-153 (bridge `4761392`)
* Cascade-132 PATH_B Option ╬▒ deposit chain: `887981b`/`45e236c`/`b9aa881`
* OP_A2 fleet.yaml flip = `COMMITTED-2026-05-10`: bridge `7786a67`
* Slot 139 BUNDLED-DEFERRED-NOTE establishing tooling-state-axis distinction: bridge `72bb2c2`


---

# Template 3 -- Reproduction appendix template (verbatim from bridge `26d7bf5`)

# Reproduction Appendix Template (S154-synthesized)

**Source:** S154 quad-witness Q5c aggregate (Gemini / Grok / Claude / GPT-5.5)
**Purpose:** Standardized reproducibility appendix attached to every
Zenodo deposit, arXiv submission, and venue submission in the post-lift
dissemination cascade. Preserves M8b d>=3 caveat with concrete parameter
ranges and exact M4 V0 anchor values.
**Provenance:** synthesized from
sessions/2026-05-10/T1-SYNTH-POST-CLOSURE-ACTION-LADDER-CONSULTATION-154/verdict_witness_{1..4}_*.md Q5c sections.

---

## File naming

* Recommended filename: `reproduction_appendix.md` (and parallel `.pdf`)
* Attach as a separate file in each Zenodo deposit (sibling to the main PDF/tex)
* Reference explicitly from the deposit description: "See reproduction_appendix.md / .pdf"

---

## 7-section structure

### Section 1 -- Repository snapshot
* Repository URL (e.g., github.com/papanokechi/pcf-research, papanokechi/wallis-pcf-lean4)
* Exact commit SHA (40-char) at the time of deposit
* Active branch
* Submodules (with their commit SHAs)
* Build artifacts hash (SHA-256 of the deposited PDF/tex)

### Section 2 -- Numerical scripts
* List of script paths (relative to repo root)
* Script execution order (numbered)
* Each script's purpose (one-line)
* Each script's expected runtime (order of magnitude)
* Each script's output filename(s)
* Random seed values (if stochastic)

### Section 3 -- Parameter regimes
* Tested parameter ranges (table form: param_name | min | max | step | rationale)
* Excluded parameter ranges (with rationale)
* Caveated parameter ranges (with caveat reference, e.g., "M8b d>=3 caveat")
* Default parameter values used in headline results

### Section 4 -- Anchor values (M4 V0)
* Exact M4 V0 anchor constants (numeric values to full precision)
* Initialization conditions (where stochastic init applies)
* Source of anchor values (cascade reference, e.g., "cascade 106 / bridge 5f9db69")
* Anchor-value verification steps (how to recompute)

### Section 5 -- Execution environment
* Operating system + version (e.g., "Windows 11 Pro 24H2", "Ubuntu 24.04")
* Python version (e.g., "3.12.3")
* Python package versions (mpmath, numpy, sympy, etc. with exact versions)
* Lean toolchain version (e.g., "leanprover/lean4:v4.x.x")
* Mathlib commit SHA (pinned)
* C++ compiler / Fortran compiler / hardware notes (if relevant)
* `requirements.txt` or `lean-toolchain` file paths

### Section 6 -- Rebuild instructions
* Exact commands to reproduce (copy-paste-runnable)
* Expected outputs (filenames + content fingerprints / SHAs)
* Expected runtime (wall-clock, on stated hardware)
* Common error modes + resolution (e.g., "If mpmath dps default is too low, set mp.dps=300")
* Verification commands (e.g., "diff -q output.txt expected_output.txt")

### Section 7 -- Known limitations
* M8b d>=3 caveat (verbatim from m8b_caveat_template.md context-1)
* Unresolved formalization blockers (M10 status reference; not closure status)
* Numerical precision sensitivities (e.g., "results stable to dps=200; degraded below dps=80")
* Hardware sensitivities (if any)
* Cross-reference to D-153-3 linguistic firewall (templates/d_153_3_firewall_template.md)

---

## Composition order (for assembly)

1. Start with Section 1 (repo snapshot) -- pin all SHAs first
2. Then Section 5 (environment) -- pin all versions
3. Then Section 4 (anchor values) -- pull from M4 V0 substrate
4. Then Section 3 (parameter regimes) -- map to anchor values
5. Then Section 2 (scripts) -- align to parameter regimes
6. Then Section 6 (rebuild) -- compose execution sequence
7. Finally Section 7 (limitations) -- copy from m8b_caveat_template.md and D-153-3 firewall

---

## Audit checklist (before attaching to deposit)

- [ ] All 7 sections present
- [ ] Repository SHA is exact 40-char (not abbreviated)
- [ ] All version numbers are exact (not "latest" or "recent")
- [ ] M8b caveat is present in Section 7 (not just implied)
- [ ] Rebuild commands have been actually executed and verified to produce stated outputs
- [ ] Output checksums in Section 6 are correct
- [ ] No SIARC/cascade/M-axis governance jargon leaks into Section 7 (use canonical firewall sentence)
- [ ] References to numerical precision are stated in dps (decimal places) not bits
- [ ] No reference to "M10 closed" / "M10 V0 achieved" anywhere in the appendix

---

## Reuse guidance

This template is the canonical reproduction appendix for the post-lift
dissemination cascade. Copy this file to the per-paper repository, fill in
the 7 sections with paper-specific content, and attach the result to:

* Zenodo deposit (as a separate file)
* arXiv submission (as ancillary file or linked from comments field)
* Venue submission (as supplementary material)
* Conference talk repository (as README addendum)

Update the canonical firewall sentence (Section 7) and M8b caveat
(Section 7) by reference to the master templates in this directory,
not by independent re-authoring.


---

## Provenance attestation

This runbook was synthesized in T2-Executor slot 186 (PROMPT 186 fire 2026-05-11) by mechanical inlining of bridge `26d7bf5` templates and composition of the 5 amendment specifications per slot 154 verdict aggregate (W1+W3+W4 union). Inlined template contents are byte-identical to bridge `26d7bf5` originals (verified at compile-time via `git show 26d7bf5:.../templates/<name>.md`); independent re-authoring was NOT performed.

If any inlined template drifts from the bridge `26d7bf5` baseline due to subsequent S-class re-verdicting, refresh by re-running PROMPT 186 against the new substrate SHA.
