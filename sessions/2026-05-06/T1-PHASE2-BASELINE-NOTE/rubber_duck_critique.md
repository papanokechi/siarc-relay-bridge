# Rubber-duck critique — T1-PHASE2-BASELINE-NOTE v1.0

This is the agent's pre-commit self-critique of `bt_baseline_note.tex`
(8 pp, SHA-256 `23022f0de77ac8388ed584b2196c0ab995cd8cf18b2dd71efbc0488a0f6e5b7c`)
before the session is committed to the bridge. It is the
mandatory rubber-duck pass that the relay 051 spec calls for: the
agent reads its own draft from the perspective of an unsympathetic
referee and records every weakness it can detect, with explicit
verification that the four-way epistemic partition (PROVEN /
VERIFIED / STRUCTURAL FRAMING / CONJECTURED) is intact in every
section. None of the items below are halt-worthy; they are
recorded for downstream review.

## Section-by-section epistemic-partition audit

### Section 0 (Abstract)
- The opening sentence states the formal-level baseline
  ($\Anaive \in \{d-1, d, d+1\}$) and attributes it to
  Theorem 1.1 — context (i) PROVEN. ✓
- "is verified at $80$ algebraic digits against PCF-1 v1.3 §6
  Theorem 5 lower branch" — context (ii) VERIFIED literature
  citation. The verb "verified" is permitted in (ii). ✓
- "lies strictly outside the formal baseline … two
  non-mutually-exclusive structural mechanisms are consistent
  with this gap" — context (iii) STRUCTURAL FRAMING. Verbs
  used: "lies outside", "consistent with". Both permitted. ✓
- "is consistent with — but does not establish — $A = 2d$" —
  the explicit non-extension to (iv) CONJECTURED. ✓
- "Conjecture B4 of [PCF-2 v1.3]" — context (iv) CONJECTURED;
  no closure verb used. ✓

### Section 1 (Setup and main results)
- §1.1 (PCF Wallis recurrence) — declarative setup. No
  epistemic-partition claims. ✓
- §1.2 (Wimp–Zeilberger ansatz) — declarative; introduces
  $\Anaive$ as Definition (i) PROVEN scope. ✓
- §1.3 (Main results):
  - **Theorem 1.1**: stated strictly in $\Anaive$ scope —
    "the formal asymptotic exponent $\Anaive$ satisfies
    $\Anaive \in \{d-1, d, d+1\}$ across the three SIARC
    conventions, uniformly for $d \in [2, 8]$". The theorem
    does NOT extend to $A$ or to Conjecture B4 anywhere.
    **THEOREM_OVERREACH halt-condition: NOT TRIGGERED.** ✓
  - **Proposition 1.2** (gap-framing): stated as STRUCTURAL
    FRAMING. The proposition asserts (a) the empirical record
    of [PCF-2 v1.3] lies outside the formal baseline; (b)
    two structural mechanisms are consistent with the gap;
    (c) distinguishing them is open. Verbs used: "lies
    strictly outside", "are consistent with", "is the open
    content". All permitted. ✓
  - "**[Theorem 1.1] is proven** in [§3]" — context (i)
    PROVEN; verb "proven" is permitted for the formal-level
    Theorem strictly scoped to $\Anaive$. ✓
  - "**[Proposition 1.2] is supported** in [§4]" — context
    (iii) STRUCTURAL FRAMING; "supported" is permitted.
    (Original draft used "is proven" — softened in the
    pre-commit pass to use the permitted verb "supported"
    out of an abundance of caution, even though Prop 1.2 is
    a mathematical proposition with a legitimate
    proof-style argument.) ✓
  - "is consistent with — but does not establish — $A = 2d$"
    — explicit non-extension to (iv). ✓
  - **Conjecture B4** stated; verbs "claim to prove or
    partially prove" used in negative form ("we do NOT
    claim to prove…") — meta-usage discussing what the
    note does NOT do. ✓

### Section 2 (Wimp–Zeilberger ansatz and balance analysis)
- §2.1–§2.4 — pure formal-level (i) PROVEN scope. Verbs:
  "yields", "satisfies", "produces", "reproduces". ✓
- The per-convention table (§2.3) — formal-level data only;
  no extension to $\Afit$ or $A$. ✓
- The Phase A AEAL anchor (§2.4) — literature-citation /
  bridge-substrate provenance. The script SHA-256 is
  reproduced verbatim from the bridge handoff. ✓

### Section 3 (Proof of Theorem 1.1)
- §3.1 — closes the proof by per-degree case analysis.
  Verbs: "executes", "extends", "is realised exactly",
  "records". Context (i) PROVEN strictly scoped to
  $\Anaive$. ✓
- §3.2 (d=2 verification) — context (ii) VERIFIED.
  Verbatim quote from PCF-1 v1.3 §6 Theorem 5; verbs
  "verified at 80 algebraic digits", "recovers $\Anaive
  = 3$". Both permitted in (ii). ✓
- "The $d = 2$ upper branch $A = 4 = 2d$ … is **not**
  recovered by the formal-level baseline" — explicit
  partition-boundary statement; uses permitted verb
  "consistent with the borderline-locus mechanism (i$'$)
  of Prop 1.2 — the closure of which is the open content".
  Context (iii) STRUCTURAL FRAMING. ✓

### Section 4 (Structural framing of the gap to A=2d)
- Section title contains "to $A = 2d$" — flagged as
  context (iii)+(iv) target. Verbs in section: "frames",
  "does not close", "lies strictly outside", "is consistent
  with", "predicted by", "may exhibit", "would reflect",
  "are not mutually exclusive", "the closure of the gap
  is the open content". All permitted in (iii)/(iv).
  **EPISTEMIC_LANGUAGE_DRIFT halt-condition: NOT
  TRIGGERED.** ✓
- §4.4 explicitly enumerates the forbidden verbs as a
  hygiene clause within the manuscript itself
  ("the wording shows / confirms / proves / demonstrates
  / establishes / verifies is reserved for…"). This is
  meta-usage and is correct. ✓

### Section 5 (Connection to Birkhoff–Trjitzinsky 1933)
- "provides the existence and factorization machinery"
  — about the literature, context (ii) VERIFIED. ✓
- "applies to the SIARC stratum uniformly in $d$ at the
  formal level and the sectorial realization level. It
  does not record that the machinery identifies $A = 2d$
  for the SIARC stratum specifically" — explicit
  non-extension to (iv). ✓
- "all pass for the SIARC stratum at the normal-case
  locus … with a caveat that the §7 Theorem II 'point of
  division' condition degenerates on the borderline locus"
  — context (iii) STRUCTURAL FRAMING with explicit
  caveat. ✓
- "the lift is open in this note" — explicit (iv)-open
  declaration. ✓

### Section 6 (Open questions)
- All four problems stated as Open problems with
  permitted verbs ("is open", "is the open content",
  "requires", "would supply", "may identify"). ✓
- Q1 (mechanism identification) — STRUCTURAL FRAMING
  (iii). ✓
- Q2 (borderline-Q algebraic ansatz) — STRUCTURAL
  FRAMING (iii) + (iv). The expected closed form
  $B = \sqrt{c_a}$ is stated with the verb "expected"
  / "by analogy with". Permitted. ✓
- Q3 (A_fit definitional audit) — STRUCTURAL FRAMING
  (iii). The verb "to support or rule out" is permitted.
  (Original draft used "to confirm or reject" — softened
  in pre-commit pass.) ✓
- Q4 (sectorial upgrade) — explicit declaration of
  open status; cites Wasow / Adams / Turrittin / Immink /
  Costin / Birkhoff 1930 / [siarc_t1_phase2 Phase D]. ✓

### AI Disclosure + Appendix A
- AI Disclosure paragraph reproduces the standard SIARC
  AI-disclosure template verbatim. ✓
- Related cross-cites block lists 6 SIARC Zenodo records
  for the Zenodo related-identifiers metadata field. ✓
- Appendix A bridge-session provenance lists 3 bridge
  sessions with SHA-256 hashes for the load-bearing
  scripts and verification documents. ✓

## Substantive concerns

1. **The formal-balance argument in §2.2 omits the
   secondary-indicial step.** §2.2 derives the $\mu$-pair
   $(\mu_{\mathrm{dom}}, \mu_{\mathrm{sub}})$ from balance
   (I) + (III); it does not derive $\rho_{\mathrm{dom}}$ or
   $\rho_{\mathrm{sub}}$, which would require the
   $n^{-1}$ correction in the edge equation. A determined
   referee may ask why the secondary indicial step is
   omitted. The honest answer is that the formal-level
   baseline of Theorem 1.1 is about $\Anaive = \mu_{\mathrm{dom}}
   - \mu_{\mathrm{sub}}$ specifically — the difference of
   the leading $\mu$-values — and is unaffected by the
   $\rho$-pair, which contributes only to the lower-order
   structure of the formal solutions. This is a stylistic
   simplification, not a hole in the proof.

2. **The Phase B sweep at $d \in [3, 8]$ is cited but not
   reproduced.** §3.1 cites
   `phase_b_extended_sweep.py` (SHA-256 `39e98db6…`)
   without reproducing the sweep table. A referee may
   ask for the per-$(d, \text{convention})$ table at
   $d \in [5, 8]$. The sweep is mechanically the same
   computation as §2.3's table at $d \in \{2, 3, 4\}$
   extended to $d \in [5, 8]$, with the same conclusion;
   reproducing the table would add ~0.5 pp of repetitive
   tabular content. Acceptable as a citation in the
   present note.

3. **The "borderline-locus mechanism (i$'$)" of §4.3 is
   stated but not derived.** The proposition states that
   the SIARC stratum may exhibit, on a sub-locus, a
   degeneracy of $c_b$ such that the effective $\dega
   = 2\degb$. The note does not derive the sub-locus or
   exhibit it explicitly. This is exactly the open
   content of Q2 (`q:borderline-Q`); the gap is honestly
   declared. ✓ This is the load-bearing structural
   honesty of the note.

4. **The "definitional mechanism (ii$'$)" of §4.3 is
   stated as a hypothesis without a formal definition of
   the alternative $\Afit$.** The note does not specify
   what the Stokes-constant exponent on $\log Q_n$ would
   be, beyond an informal pointer. This is also exactly
   the open content of Q3 (`q:Afit-def`); honestly
   declared.

5. **The PDF SHA-256 of [siarc_t2b_v3] is taken from
   the v3.0 deposit on disk** (`7ac8f204…`), not the
   v3.1 deposit named in the relay 051 prompt. The v3.1
   deposit is post-2026-05-04 and is not in the local
   bridge mirror at the time of preparation of this note;
   the v3.0 SHA-256 is the authoritative on-disk value.
   This affects only the Zenodo related-identifiers
   cross-cite block; no load-bearing claim of the note
   depends on it. The bibliography note in
   `annotated_bibliography.bib` documents the version
   discrepancy.

## Structural concerns

6. **Page count = 8 sits at the lower edge of the band
   [8, 12].** The HALT condition is `< 8 OR > 12`; 8 is
   admissible. A single added paragraph (e.g., the
   secondary-indicial step in §2.2 or a mini-table for
   $d \in [5, 8]$) would push to 9 and improve the
   robustness margin. Operator may consider a v1.1 if
   the lower-edge page count is uncomfortable. This
   discomfort is mentioned but is not a halt.

7. **The bibliography contains 15 entries**, comfortably
   above the relay 051 spec target of 12. Of these, 7
   are SIARC self-citations (with footnoted SIARC-disclosure
   per the umbrella-v2.0 / D2-NOTE v2.1 convention) and 8
   are primary literature anchors. ✓

## Editorial concerns

8. **The footnote `\thanks{}` AI-disclosure on the title
   page reproduces the standard SIARC long-form
   disclosure** rather than the relay 051 spec's
   short-form template. This is intentional: the
   long-form is the form actually in use across the
   v1.3 deposit cycle (PCF-1 v1.3, PCF-2 v1.3, CT v1.3,
   D2-NOTE v2.1). The short-form template
   ("During the preparation of this work the author
   used GitHub Copilot (Microsoft) and Anthropic Claude
   to assist with code generation, numerical computations,
   and manuscript drafting…") appears verbatim in the
   AI Disclosure section at the end of the manuscript,
   per the spec.

9. **One textual SHA-truncation `dcd7e3c6\dots d68fe6` in
   §5 and §AI-Disclosure** — LaTeX-compatible. The full
   hash `dcd7e3c6b2a12ae1ce917d322763ff9dde5ec69ab5f23080d043699822d68fe6`
   appears verbatim in the bibliography note for
   `birkhoff_trjitzinsky_1933`. ✓

10. **`cleveref` "always capitalise" info-message** in the
    pdflatex log is a configuration confirmation, not a
    warning or error; the package option `[capitalise]`
    is intentional (per D2-NOTE v2.1 and PCF-1 v1.3
    house-style).

## Forbidden-verb hygiene scan summary

A regex scan for `(shows|confirms|proves|proven|demonstrates|establishes|verifies|verified)`
on `bt_baseline_note.tex` returns 20 matches; sentence-by-sentence
classification gives:

- 0 matches in (iii) STRUCTURAL FRAMING contexts using a
  forbidden verb in the closure sense (after the pre-commit
  softening of the "Prop 1.2 is proven" → "Prop 1.2 is
  supported" and "to confirm or reject" → "to support or
  rule out" edits).
- 0 matches in (iv) CONJECTURED contexts using a forbidden
  verb.
- All remaining 20 matches are either:
  - in (i) PROVEN scope strictly about $\Anaive$ (5 matches:
    Thm 1.1 statements, §3 proof header, §3.1 case analysis);
  - in (ii) VERIFIED scope as literature citations (3
    matches: Abstract + §3.2 verbatim quote + §3.2
    attribution);
  - in §4.4 forbidden-verb hygiene clause as meta-usage
    enumerating the forbidden verbs (4 matches);
  - in the §1.3 negative-form statement "we do not claim to
    prove or partially prove Conjecture B4" (2 matches);
  - in literature attributions about Birkhoff–Trjitzinsky
    1933 verbatim ("verbatim", "extracts verbatim",
    "SHA-verified") (3 matches);
  - 3 matches in cross-reference verbs ("Theorem … establishes
    that the formal-level baseline …", in PROVEN scope strictly
    about $\Anaive$).

**EPISTEMIC_LANGUAGE_DRIFT halt-condition: NOT TRIGGERED.**
**THEOREM_OVERREACH halt-condition: NOT TRIGGERED.**

## Net assessment

The note crystallizes the T1 Phase 2 verdict
`UPGRADE_PARTIAL_FORMAL_LEVEL` (bridge commit `37c939f`,
2026-05-04) into a single citable artefact. The contribution
delta over the bridge handoff is structural exposition + clean
theorem statement (Theorem 1.1) + proposition-level gap
framing (Proposition 1.2) + literature positioning (§5),
not new computation. The four-way epistemic partition
(PROVEN / VERIFIED / STRUCTURAL FRAMING / CONJECTURED) is
intact in every section, with explicit non-extension of
load-bearing claims from $\Anaive$ to $A$ or to Conjecture
B4. Items 1–4 above are candidates for v1.1 strengthening
passes; item 6 is a structural margin observation; items
5, 7–10 are documentation-only. Build is clean: 8 pages,
0 unresolved citations, 0 undefined references.

The note is the SIARC counterpart of PCF-1 v1.3 §6 Theorem 5
lower branch — a positive formal-level result citable
independently of any subsequent lift to $A = 2d$.
