# introduction.md — PCF-2 v1.4 introduction (polish-pass verdict)

## Synth verdict on the v1.3 §1 introduction (inherited unchanged in v1.4)

**No re-write recommended for the PCF-2 manuscript itself.**

The §1 introduction is correctly scoped to:

- The cubic-discriminant problem framing (sign + Galois-group structure of Δ₃).
- The PCF-1 baseline as foundational reference (degree-2 sharp dichotomy).
- The qualitative-novelty argument (cubic case is NOT a sign-of-Δ predicate; requires Galois-group structure).
- Scope-limit honesty (deep-WKB null at d=4 from Session R1.3).
- AEAL/SIARC methodology disclosure (already in author footnote L42-52; not in §1 body).

## Q3a/Q3b: NO M1-M12 narrative insertion recommended

The slot 155 §Q3a question asked whether the introduction should integrate an M1-M12 closure narrative. **The synth verdict is NO.**

### Rationale

1. **PCF-2 is a math-content paper; Umbrella is the program-level paper.** Introducing M1-M12 narrative into PCF-2's introduction would dilute the paper's mathematical focus (cubic-discriminant Galois-structure obstruction) with program-tier governance material that belongs in the Umbrella program statement.

2. **M-axis closures other than M7 are out-of-scope for PCF-2's mathematical frame.** PCF-2 addresses the cubic-discriminant predicate (M-axis M7 territory). M4 V0 (cascade 106; bridge `5f9db69`) is a degree-2 result; M8a (cascade 127R; bridge `cb429e1`) is Painlevé-test catalogue labelling at degree-≤4; M8b (cascade 130R; bridge `74c5630`) is laptop-feasible numerical foreclosure of |S_2| at d=2. None of these are mathematically prerequisite to PCF-2's cubic-discriminant predicate; citing them in the PCF-2 introduction would be a categorical scope-mixing error.

3. **D-153-3 governance discipline.** Discussing M10 (Lean formalization work-stream) in the introduction risks SAFE-phrasing violation. Easier to avoid entirely.

4. **Bridge-SHA citations belong in the Zenodo description body, not the LaTeX introduction.** Bridge SHAs are not canonical academic citations; including them in the manuscript body is a meta-tier provenance signal that fits the deposit metadata but not the paper text. The live Zenodo description body for 20114315 ALREADY contains the relevant bridge SHA citations (e857172 / 7f93b9e), correctly placed.

### Q3b answer — methodology framing

The PCF-2 v1.4 manuscript already carries the **correct asymmetry**:

- **Math content** = primary frame (Introduction, §2-§8, Conjecture B₃, Conjecture B4, etc.).
- **SIARC pipeline** = methodological footnote (author footnote L42-52 AI-use disclosure cites P8AEAL; brief).

This asymmetry is CORRECT for a math-content paper. The reverse asymmetry (SIARC pipeline as primary frame; math content surveyed in §M-axis sections) is appropriate for the Umbrella program paper, not PCF-2.

## What the §1 introduction COULD optionally adjust in v1.5 (if needed)

Only items genuinely scoped to PCF-2's mathematical content:

- **§1.X (new sub-section, optional):** Brief paragraph noting that the v1.4 amendment now records `op:j-zero-amplitude-h6` resolved-in-soft-branch via M7 V0 cascade. This material is currently in the abstract closing paragraph (post-`\end{abstract}` insert) and in §7.5 status update; a §1 cross-reference is optional, not required.
- **§1 last paragraph:** Could add a one-line forward pointer "(See §7.5 for the v1.4 status update on `op:j-zero-amplitude-h6`)" if the operator wants the introduction to flag the amendment scope explicitly.

These are micro-edits, NOT load-bearing.

## What the §1 introduction should NEVER contain

Even at v1.5+:

- ❌ M1-M12 axis-coverage table (belongs in Umbrella, OR in PCF-2 Zenodo description body where it currently is for v1.4).
- ❌ Direct claims of "the M-axis closure cascade".
- ❌ References to S153 / cascade-132 / slot 154-160 / governance documents.
- ❌ Repository or bridge URLs in the body text (footnotes/citations only).

These are all program-tier and would cause scope-mixing.
