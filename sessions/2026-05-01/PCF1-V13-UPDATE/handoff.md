# Handoff -- PCF1-V13-UPDATE
**Date:** 2026-05-01
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~25 minutes
**Status:** COMPLETE

## What was accomplished
Folded Sessions D, E, and E' results into the PCF-1 paper, producing
v1.3 of `p12_pcf1_main.tex`. Variant **A (BOTH ARTEFACT)** of the
E-prime decision matrix was applied: the FLAG line at the top of
`sessions/2026-05-01/BOREL-CHANNEL-K-SCAN/handoff.md` reads
"BOREL CHANNEL CONFIRMED ANOMALOUS" with QL15 and QL26 both
classified ARTEFACT in the K-scan summary, so neither marginal
hit was promoted to a confirmed Painleve reduction in the Borel
channel. Conjecture A part (iv) was restated under Variant A as
the channel-scoped sporadic-V_quad version. Compiled twice (then
once more for cross-refs); 16 pp, 0 errors, 0 undefined refs.

## Variant decision and rationale
- FLAG read: "BOREL CHANNEL CONFIRMED ANOMALOUS"
  (BOREL-CHANNEL-K-SCAN/handoff.md, line "## Final flag" block).
- K-scan classifications: QL15 = ARTEFACT, QL26 = ARTEFACT
  (residual fails to scale with K; Pade nearest-pole radius spreads
  by 2.95-3.95; best-fit Painleve flips between consecutive K).
- Decision: **Variant A (BOTH ARTEFACT)**.
- Conjecture A part (iv) accordingly bumped to "v6, part (iv)
  [revised]" with channel-scoped V_quad-as-sporadic wording.
- No promotion of QL15 or QL26 to confirmed Painleve reduction.
- Paper version bumped 1.2 -> 1.3 (no Theorem 5.ter, so no v2.0).

## Edits applied
1. `\thanks{...}` block: added Version 1.3 entry; appended
   acknowledgement that Sessions D, E, E' were executed via
   Anthropic Claude and GitHub Copilot agents.
2. `\date{April 30, 2026}` -> `\date{May 1, 2026}`.
3. Abstract: appended sentence
   "Version 1.3 folds in the WKB exponent identity (Theorem 5.bis.1)
   and revised Conjecture A part (iv) per Sessions D, E, E'."
   (with `\ref{thm:wkb}` for the theorem reference).
4. NEW Section "The WKB Exponent Identity" (label `sec:wkb`) inserted
   between sec:structural and sec:vquad, containing:
     - Theorem 5.bis.1 (`thm:wkb`) with closed-form
       alpha = A - 2 log c_b + log|c_a|, A in {3,4}.
     - Empirical 6-row verification table (`tab:wkb-exponents`)
       transcribed from `wkb_exponent_table.tex`.
     - Remark (`rem:wkb-formal`) flagging this as a formal
       Domb-Sykes statement and leaving rigorous WKB proof open.
     - Remark (`rem:wkb-channel`) on channel-independence.
     - Provenance paragraph crediting Sessions E and E'.
5. NEW subsection "Channel scope of the prototype role"
   (label `ssec:vquad-channel-scope`) appended to Section
   "V_quad as the Explicit Prototype", recording:
     - Session D failure on V_quad (recurrence-parameter channel,
       1.064e-4 flat under precision escalation).
     - Sessions E + E' failure on V_quad (Borel-resummation channel,
       gate residual 7.2e-3 -> 9.9e-2 under K-extension; Pade
       nearest-pole radius diverges 2.17 -> 4.59).
     - Conclusion: V_quad's P-III(D6) reduction lives in a third
       channel (Borel transform of Stokes-constant ODE) not
       operationalized here.
6. Conjecture A part (iv) (`conj:A4`) replaced with the Variant A
   wording: channel-scoped, V_quad as unique sporadic instance,
   channel structure itself open.
7. Section "Open Questions" (`sec:open`):
     - Bullet 2 expanded with the Session D negative result on QL06
       (PV in L(t) channel ruled out at depth 3000 / dps 400) and
       a forward reference to `op:borel-channel`. Label
       `op:non-piii` added.
     - NEW bullet 6 added with label `op:borel-channel`, recording
       the V_quad gate failure, the QL15/QL26 K=12 marginals being
       artefacts, and the open question of constructing a
       Stokes-constant ODE Borel channel.
     - Existing bullets 1, 3, 4, 5 retained verbatim; bullet 1
       received label `op:family-painleve` for completeness.

## Compile output
- 3 pdflatex passes (final pass added to resolve cross-references).
- Final: 16 pages, 392886 bytes.
- 0 errors, 0 undefined references.
- Cosmetic warnings only: hyperref unicode (V$\_$quad in section
  title) and one `h` -> `ht` float specifier downgrade. Same
  warnings as v1.2.

## Files committed
- p12_pcf1_main.tex (v1.3 source, ~46 KB)
- p12_pcf1_main.pdf (16 pp, ~393 KB)
- handoff.md (this file)

## AEAL claim count
0 entries written to claims.jsonl this session (all numerical
content is sourced from prior sessions D, E, E' which already
have AEAL entries; v1.3 is a writing/integration session, not a
new computation).

## Anomalies and open questions
- The PCF-1 v1.2 source (`sessions/2026-04-30/P12-PCF1-ZENODO/p12_pcf1_main.tex`)
  did NOT already contain `op:non-piii` or `op:borel-channel` labels.
  Those labels exist only in the parallel JOURNAL DRAFT
  (`tex/submitted/p12_journal_main.tex`). The prompt step 4 said
  "KEEP the v1.2 micro-patch wording" assuming those bullets were
  present; they were not. Pragmatic interpretation: the labels were
  ADDED in v1.3 with content derived from the journal draft's
  micro-patched bullets, which is what the prompt presumably
  intended. Worth noting so Claude can confirm.
- Conjecture A4 was previously a numbered conjecture object; Variant A
  rewording keeps the same `\begin{conjecture}[A v6, part (iv): ...]`
  numbering ("[Theorem 6.x]" in TeX numbering since the conjecture
  environment shares the `theorem` counter). The text below
  Conjecture A4 contains a `Remark` (`rem:prototype`) that softened
  the original V_quad-only claim; that remark is now technically
  redundant under Variant A but was left in place as it remains
  informationally consistent. Flag for Claude review.

## What would have been asked (if bidirectional)
- Should `rem:prototype` be deleted now that Conjecture A4 itself
  carries the channel-scope caveat?
- Should the WKB Theorem 5.bis.1 be split into a stronger version
  for V_quad (where A=4 has a structural reason via b(x) = a'(x))
  versus the QL01-QL26 family (where A=3 is the generic case)?
  Currently bundled as one statement.

## Recommended next step
Forward `p12_pcf1_main.pdf` to human for visual review of the new
Section 5 (WKB Identity) and Section 6.1 (Channel scope subsection).
After human OK, push to Zenodo as new version of record 19934553
(human will use the "New version" button manually per prompt H
instructions). DO NOT auto-upload.
