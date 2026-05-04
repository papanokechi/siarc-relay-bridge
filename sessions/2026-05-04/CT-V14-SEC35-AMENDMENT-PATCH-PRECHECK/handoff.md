# Handoff — CT-V14-SEC35-AMENDMENT-PATCH-PRECHECK
**Date:** 2026-05-04
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~70 minutes
**Status:** COMPLETE
**Verdict:** `UPGRADE_CTV14_SEC35_PATCH_PARTIAL_SECTION_NUMBERING_AMBIGUITY`

## What was accomplished

Prepared a precheck artifact for a recommended CT v1.4 §3.5
amendment, following the G17-LAYER-SEPARATION-LIT-ANCHOR
verdict 2026-05-04 (`UPGRADE_G17_LIT_ANCHOR_FOUND_AMENDMENT_RECOMMENDED`).
Located the authoritative CT v1.4 in-flight TeX source,
extracted §3.5 verbatim (lines 948–995, "The locked WKB
exponent identity"), drafted a clean insertion-only unified
diff, validated cite-keys against the existing
`annotated_bibliography.bib`, and ran a static LaTeX hygiene
+ render dry-check on the proposed paragraph. Did **not**
auto-apply the patch (per Rule 2; operator commits manually
after Claude / human review).

## Key numerical findings

* CT v1.4 source: SHA-256 `0600A4456803A43D967788196C501534716852652030FC4225E6B42921AE77E1`, 91 605 bytes, 2 050 lines, `\def\version{1.4}` at line 52.
* §3.5 boundaries: lines 948–995 (subsection start through last line before next `\subsection` at 996).
* Patch shape: 1 insertion / 0 replace / 0 delete; new `\paragraph{Layer note (added v1.4).}` block ≈ 190 words.
* Bracket balance: 8 opens / 8 closes; 0 new environments; 0 new macros.
* Forbidden-verb scan: 0 hits across 9 patterns (per `_RULES.txt §D`).
* Cite-keys: 3/3 referenced bibkeys EXIST in `annotated_bibliography.bib` (`costin2008asymptotics`, `birkhofftrjitzinsky1932analytic`, `jimbomiwa1981monodromy`); 3 author-year plain-text references flagged as suggested-NEW for operator action (`okamoto1987studies`, `barhoumilisovyy2024transcendence`, `birkhoff1930generalized`); 0 collisions.

## Judgment calls made

1. **Insertion point: end of §3.5 (Reading A).** The G17
   Phase C.3 DRAFT references "CT v1.3 §3.5" but in CT
   v1.4 in-flight, §3.5 is "The locked WKB exponent
   identity" (which discusses the residual Laplace step
   → Stokes data, i.e. the *bridge* between the L-equation
   and isomonodromic-deformation layers), while the V_quad
   CC-channel "exact algebraic identity" theorem
   `\thm:vquad-cc` is in §3.3. The precheck adopts
   Reading A (insert at end of §3.5, cross-referencing
   `\Cref{thm:vquad-cc}` for the V_quad anchor) and
   surfaces Reading B (move insertion to end of §3.3
   after `\thm:vquad-cc`) as a deferred operator +
   Claude review decision. See `discrepancy_log.json`
   and `sec_35_side_by_side.md` §"§3.5-vs-§3.3 numbering
   note".
2. **Bibkeys: cite only existing keys; flag missing as
   plain-text.** Used only the 3 existing bibkeys
   (`costin2008asymptotics`, `birkhofftrjitzinsky1932analytic`,
   `jimbomiwa1981monodromy`) inside `\cite{...}` calls.
   Okamoto 1987, BLMP 2024 §4.1, and Birkhoff 1930 are
   in author-year plain-text form only — keeps the patch
   buildable as-is (no undefined-citation warnings) and
   surfaces the bibkey-addition decision to the operator
   as a separate action queued in `sec_35_cite_keys_check.md`.
3. **Wasow not cited.** Per G17 handoff Phase A.1 (Wasow
   slot 04 image-only) and the deprecated-verb guidance
   "Wasow §X.3 → Wasow Theorem 11.1 with explicit eq.
   reference", Wasow is omitted from the amendment
   citations; B-T 1933 + Costin 2008 ch.5 carry the
   L-equation anchor at theorem-grade quotes.
4. **No `\label{}` on the new paragraph.** The amendment
   is a clarifying note, not a numbered statement;
   non-labelled keeps it consistent with v1.4's "purely
   additive" framing (line 241).

## Anomalies and open questions

* **§3.5-vs-§3.3 anchor ambiguity (PRIMARY review item).**
  Operator + Claude should decide between Reading A
  (precheck-default, insertion at end of §3.5 / locked WKB)
  vs. Reading B (alternative, insertion at end of §3.3
  after `\thm:vquad-cc`). Reading B may match the
  G17-handoff intent more literally; Reading A keeps the
  amendment topically adjacent to the residual-Laplace-
  step → Stokes data discussion that already gestures at
  the layer separation. Both readings preserve all
  existing v1.4 wording. This is the only blocking
  question for `git apply`.
* **Suggested-NEW bibkey decision.** Operator may either
  (a) leave Okamoto / BLMP / Birkhoff 1930 as plain-text
  author-year references (current patch state), or (b) add
  bibkeys `okamoto1987studies`, `barhoumilisovyy2024transcendence`,
  `birkhoff1930generalized` to `annotated_bibliography.bib`
  and upgrade the plain-text mentions to `\cite{...}`
  before final apply. Recommended: option (b) for
  refereed-paper polish, but not blocking for a v1.4
  precheck-stage commit.
* **Reading-B alternative patch not produced.** If
  operator + Claude decide to switch to Reading B, a
  separate refire of this task with an explicit
  Reading-B mandate would produce the §3.3 / `thm:vquad-cc`-
  end variant of the .patch artifact.

## What would have been asked (if bidirectional)

* "Is the G17 'CT v1.3 §3.5' reference (a) the v1.4
  numbering of the locked-WKB section (Reading A), (b) the
  v1.3-published-PDF numbering of what is now §3.3 in
  v1.4 (Reading B), or (c) a paraphrase that the operator
  +Claude would adapt to either?"
* "Should the suggested-NEW bibkeys
  (`okamoto1987studies`, `barhoumilisovyy2024transcendence`,
  `birkhoff1930generalized`) be added to `annotated_bibliography.bib`
  inside this same precheck, or as a separate `bibkey-add`
  task?"

## Recommended next step

Operator + Claude review the four artifacts (`sec_35_amendment.patch`,
`sec_35_side_by_side.md`, `sec_35_cite_keys_check.md`,
`sec_35_hygiene_report.md`) and pick **Reading A** (apply
the patch as drafted) or **Reading B** (refire this task
with an explicit Reading-B mandate). After review, run
`git apply siarc-relay-bridge/sessions/2026-05-04/CT-V14-SEC35-AMENDMENT-PATCH-PRECHECK/sec_35_amendment.patch`
on a clean working copy of `ct_v1.4_main.tex`, run
`pdflatex` to confirm render-clean, then commit and stage
for v1.4 release-candidate.

## Files committed

* `prompt_spec_used.md` — full relay-prompt spec
* `sec_35_current_verbatim.tex` — §3.5 verbatim extraction (lines 948–995, 48 lines)
* `sec_35_amendment.patch` — unified-diff insertion-only patch (1 hunk)
* `sec_35_side_by_side.md` — current ↔ proposed comparison + numbering-ambiguity note
* `sec_35_cite_keys_check.md` — bibkey existence + collision audit
* `sec_35_hygiene_report.md` — bracket-balance + forbidden-verb dry-check
* `claims.jsonl` — 6 AEAL entries
* `discrepancy_log.json` — §3.5-vs-§3.3 numbering anchor ambiguity
* `halt_log.json` — empty (no halt condition met)
* `unexpected_finds.json` — empty (no unexpected positive result)
* `handoff.md` — this file

## AEAL claim count

6 entries written to `claims.jsonl` this session
(Phase A: source identification; Phase B: §3.5 verbatim;
Phase C: patch artifact provenance; Phase C.3: cite-keys
gate; Phase D: hygiene dry-check; Phase E: verdict).
