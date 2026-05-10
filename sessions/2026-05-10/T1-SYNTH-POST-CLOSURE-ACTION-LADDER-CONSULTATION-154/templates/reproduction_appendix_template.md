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
