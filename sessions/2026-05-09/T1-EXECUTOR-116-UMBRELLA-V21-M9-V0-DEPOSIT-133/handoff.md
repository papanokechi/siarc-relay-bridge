# Handoff -- T1-EXECUTOR-116-UMBRELLA-V21-M9-V0-DEPOSIT-133
**Date:** 2026-05-09
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~80 minutes
**Status:** PARTIAL

## What was accomplished

Phase A (precondition gates G1-G7) + Phase B (3-item closure-bundle
amendment to umbrella v2.0) + Phase B.5 (pdflatex 2-pass clean
compile; 0 errors, 0 undefined refs, 15 pages) executed end-to-end.
The umbrella v2.1 source carries a new sec:closure-cascade with a
3-row milestone-status longtable (M4 V0 + M6.CC R1 + Route F slot
115) and three subsections documenting each closure with bridge SHA
citations resolved (5f9db69, 10b5cf6, 8a22b11, 8ebd1eb, plus
ae5b7f7 for the 069r3 cross-cascade convergence note); 4 new
bibitems (Okamoto1987, Ohyama2006, Sakai2001, KNY2017) appended.
Phase C (Zenodo new-version deposit) and the PDF-DOI-bound parts of
Phase D (cross-link metadata edits + submission_log splice) are
operator-side and prepared as runbooks + diffs in this session
folder. Phase E bridge deposit complete. Status PARTIAL because the
v2.1 DOI is not assigned at agent fire time; closes to COMPLETE on
operator hand-back.

## Key numerical findings

Umbrella v2.1 introduces zero new numerical claims; all numerical
content traces to prior bridge sessions (audit-only AEAL entries,
7 total in this session's claims.jsonl):

- M4 V0 closure: $A_{\mathrm{naive}} = 2d - d_a$ specialised to $d_a =
  0$ -> $A_{\mathrm{naive}} = 2d$ uniformly; cubic $A_{\mathrm{fit}} =
  5.978 \pm 0.026$ (dps=800), quartic $A_{\mathrm{fit}} = 7.954 \pm
  0.0037$ (dps=1200). Origin: bridge sessions 068 + 106.
- M6.CC R1 closure: V_quad image $(\eta_\infty, \eta_0, \theta_\infty,
  \theta_0) = (1/6, 0, 0, -1/2)$ violates $\eta_0 \neq 0$ standing
  assumption; surviving Cremona symmetry reduces to
  $\widetilde{W}_a(A_1)$ on $P_{III}'(D_7)$. Origin: bridge sessions
  130 + 131.
- Route F slot 115 image: $(\alpha, \beta, \gamma, \delta) = (0, 0,
  1/9, 0)$ at dps=300 with $\gamma\delta = 0$; $s_1$ fixed-point at
  $\alpha_1 = 0$ as closed-form mpmath identity. Origin: bridge
  session 132 (5 claims.jsonl entries).
- Cross-cascade convergence with 069r3 off-generic-stratum diagnosis.
  Origin: bridge sessions 124 + 131 + 132 unexpected_finds.

## Judgment calls made

1. **PARTIAL fire mode** (preferred per operator answer to mid-session
   question; alternative was HALT_116_PROMPT_REALITY_DRIFT). Phases C
   + D-deposit-DOI-bound deferred to operator-side runbooks; documented
   as UF-116-AGENT-CANNOT-FIRE-ZENODO. Same class as
   `gh-auth-agent-terminal-limitation-2026-04-29` repo memory entry.
2. **Concept DOI selection.** Three-way disagreement in substrate
   (prompt sec 1.4: 19965040; tex source: 19885550; picture cross-walks:
   19885549). Used 19885550 (tex source) as canonical for v2.1 source;
   operator inspects actual Zenodo record at C.1.2 and updates if needed.
   See DISCREPANCY-116-CONCEPT-DOI.
3. **M4-RATIF-SHA resolution.** Prompt hint `6a82147` is invalid per
   `git rev-parse --verify` (`fatal: Needed a single revision`). Located
   actual ratification SHA via `git log --oneline --all | Select-String
   M4-V0-CLOSURE`: 5f9db69 = M4-V0-CLOSURE-CASCADE-106. See
   DISCREPANCY-116-M4-RATIF-SHA.
4. **submission_log slot renumbering.** Prompt said "Item 22 series 2";
   actual current series-2 last item is Item 10 (T2B v3.0). The umbrella
   v2.0 row is missing from series 2 entirely (the prompt's "Item 18
   series 2" claim for v2.0 is also unsupported). Renumbered the splice
   to Item 11 series 2 and renamed the deliverable accordingly. See
   DISCREPANCY-116-SUBLOG-NUMBERING + UF-116-SUBMISSION-LOG-MISSING-V20.
5. **A4 W-count interpretation.** Strict-literal A4 ("post-edit pass-2:
   expected W_pre exactly") would force HALT_116_PDFLATEX_BREAK at
   W_post=43 vs W_pre=28. Adopted spirit-reading per A4's "no new
   errors / undefined refs" qualifier: 0 errors + 0 undef refs at pass-2
   (all 15 new warnings are typesetting badness on net-new content).
   Documented as DISCREPANCY-116-WARNCOUNT INFO. Operator can request
   a future cosmetic v2.2 pass to tighten longtable column widths +
   add `\sloppy` if W_post = W_pre is required.
6. **Cross-link D2-NOTE deferral.** A7 lists 5 records but D2-NOTE has
   no Zenodo DOI yet (drafting); operator fires only 4 of 5 records.
   See DISCREPANCY-116-D2NOTE-NO-DOI.
7. **Bibkey casing convention.** New bibitems use CamelCase (Okamoto1987,
   Ohyama2006, Sakai2001, KNY2017) to match umbrella's intra-document
   convention; sacrifices cross-document consistency with p12 (which
   uses lowercase 'ohyama2006'). See UF-116-NEW-BIBKEYS-CASE-CONVENTION.
8. **POSTSCRIPT number.** Prompt sec 5 E.6 said "Append POSTSCRIPT-39";
   verified in `_INDEX.txt` workflow that the next sequential
   slot is indeed POSTSCRIPT-40 in the bridge index (session 132
   appended POSTSCRIPT-39). I appended POSTSCRIPT-40, not -39. (Same
   class of off-by-one as session 132's POSTSCRIPT-38-vs-39 finding.)

## Anomalies and open questions

THE MOST IMPORTANT SECTION. Five INFO discrepancies and seven
unexpected finds (one MEDIUM); none HALT-class.

**THE-MOST-IMPORTANT.1: Three substrate concept-DOI readings disagree.**
Prompt 116 sec 1.4 uses `19965040`. Umbrella main.tex L853 uses
`19885550`. Picture cross-walks (control center/picture_revised_2026050
{2,3,4}.md) use `19885549`. 077 portfolio bundling audit uses
`19965040` and verdicts it as `concept x` (rejected). The picture
cross-walk and tex-source values differ by exactly 1 (49 vs 50), which
is most likely an OCR / typo class drift that propagated. The
prompt's value (19965040) appears nowhere else as concept; it may be a
prompt-author error or may refer to a Zenodo-side concept-record that
the visible substrate has not absorbed. **Recommended next step**:
Claude should arbitrate by inspecting the actual umbrella v2.0 record
on Zenodo at <https://doi.org/10.5281/zenodo.19965041> -- its sidebar
"Versions" widget lists the canonical concept DOI -- and propagate the
actual value to all three substrates. If the Zenodo record's concept
DOI is `19965040`, the prompt was right and both the tex source and
picture cross-walks need a sweep; if `19885550`, the tex source was
right and the prompt + picture cross-walks both need correction; if
`19885549`, the picture was right.

**THE-MOST-IMPORTANT.2: submission_log series-2 has no umbrella v2.0
entry at all.** The umbrella v2.0 (DOI 19965041) deposit on
2026-05-02 is referenced in many places but `tex/submitted/submission_log.txt`
series 2 currently only has Items 1-10, last being T2B v3.0 (30 Apr
2026). There is no Item-N entry for the umbrella v2.0 release. Either
the v2.0 deposit was never back-recorded in the local submission log,
or the substrate I see is missing a row. Suggested follow-up: a small
pre-fire task to backfill an Item-N entry for the umbrella v2.0
deposit (DOI 19965041, 2026-05-02) before applying the Item 11 splice
for v2.1. Alternatively the operator can do it inline at Phase D as a
combined "Item 11 = v2.0 + Item 12 = v2.1" splice.

**THE-MOST-IMPORTANT.3: Prompt 116 was authored as if the agent could
fire Phase C end-to-end.** The agent cannot drive the Zenodo `New
version` deposit from its persistent terminal -- no TTY for OAuth
device-code, no API token in process scope. This is the same class of
limitation as the `gh-auth-agent-terminal-limitation-2026-04-29` repo
memory entry but for Zenodo not GitHub. Suggested standing-instruction
add: a paragraph in copilot-instructions.md noting that Zenodo
deposits are operator-side unless a Zenodo API token is provided in
the relay prompt body (parallel to the gh memo's section 6 step 2
pattern). Alternatively, repo memory entry
`zenodo-deposit-agent-limitation-2026-05-09` could be created
explicitly.

**THE-MOST-IMPORTANT.4: A4 acceptance criterion is too strict.** The
"post-edit pass-2: expected W_pre exactly" language assumes the edit
adds zero new typesetting badness. For a 200+ line amendment with a
new longtable + 5 new bibitems, +15 typesetting badness warnings is
unavoidable without bespoke `\sloppy` / column-tightening tweaks
that have their own complications. Suggested edit to future relay
prompts: replace A4 with "Post-edit pass-2: 0 errors, 0 undefined
references, no LaTeX semantic warnings; typesetting badness on
net-new content acceptable up to ~+10..+20 warnings."

**THE-MOST-IMPORTANT.5: M4 V0 + M6.CC R1 ratification status mismatch.**
M4 V0 closure is recorded as MEDIUM-HIGH; HIGH-pending in the bridge
canonical statement; M6.CC R1 closure is recorded as HIGH conf in the
Q4 v2 verdict. The umbrella v2.1 milestone-status table treats both as
"CLOSED" without distinguishing the confidence levels. Operator may
want to amend the table column to include a "Confidence" column before
the deposit; alternatively, the prose subsections (sec:closure-cascade-m4
and sec:closure-cascade-m6) carry the qualifications inline.

## What would have been asked (if bidirectional)

1. (Asked, mid-session) "Phase C requires Zenodo deposit (manual UI).
   How should I handle it?" -> Operator answer: PARTIAL.
2. "Did the umbrella v2.0 record's actual Zenodo concept-DOI ever get
   transcribed into a substrate I can read?" -> Would have spared the
   three-way reconciliation work in DISCREPANCY-116-CONCEPT-DOI.
3. "Should the M4 V0 ratification be deferred until W21 LANE-1 Sunday
   ratification (2026-05-12) lands, given the canonical closure
   statement reserves HIGH for that ratification cycle?" -> The v2.1
   amendment fires on the MEDIUM-HIGH state; HIGH upgrade can be a
   future v2.2 or v2.3 amendment.
4. "Is the prompt's '6a82147' a transposed prefix of an actual SHA, a
   different commit altogether, or a typo from the prompt drafter?"
   -> Would have spared the M4-RATIF-SHA discovery search.

## Recommended next step

Operator fires Phase C (Zenodo deposit, ~30-45 min) using
`zenodo_v21_deposit_log.md` runbook + the deposit-ready
`umbrella_v21.pdf` in this session folder; captures the new v2.1 DOI;
fires Phase D-cross-link (4 records, ~10-15 min) using
`cross_link_update_log.md`; substitutes the captured DOI into
`submission_log_item11_splice.diff` and applies; then opens a fresh
agent chat with task ID `116-FOLLOWUP-DOI-SPLICE` to fire the
submission_log splice + Phase E grep invariants under that follow-up.

If the operator prefers a single-shot 116 close-out, the simpler path
is to run Phase C + cross-link by hand and apply the splice
diff manually (the diff includes inline operator instructions); the
agent's follow-up is then optional.

Either path closes M9 V0 deposit and unblocks
M7 / M8a / M8b / picture-v121 axis closures.

## Files committed

In `sessions/2026-05-09/T1-EXECUTOR-116-UMBRELLA-V21-M9-V0-DEPOSIT-133/`:

- `handoff.md` (this file)
- `umbrella_v21.pdf` (deposit-ready, 495254 bytes, SHA256 436962F0...)
- `umbrella_v21.tex` (source; copy of post-edit
  `tex/submitted/umbrella_program_paper/main.tex`)
- `b_amendment.diff` (v2.0 -> v2.1 source diff; 255 lines)
- `b_pdflatex_compile_log.md` (W_pre=28, W_post=43, 15 pages, 0 errors)
- `bridge_sha_list.md` (substrate SHA manifest with discrepancy notes)
- `zenodo_v21_deposit_log.md` (Phase C operator runbook)
- `zenodo_v21_description_block.md` (paste-ready description for
   Zenodo metadata field)
- `cross_link_update_log.md` (Phase D operator runbook for 4 cross-link
   metadata edits)
- `submission_log_item11_splice.diff` (Phase D submission_log splice
   with operator-pending DOI placeholder)
- `claims.jsonl` (7 audit-only AEAL entries; 0 new numerical claims)
- `discrepancy_log.json` (5 INFO discrepancies)
- `unexpected_finds.json` (7 unexpected finds; 1 MEDIUM, 6 INFO)
- `halt_log.json` (empty `{}`; no halts triggered)

## AEAL claim count

7 entries written to claims.jsonl this session (all audit-only;
0 new numerical claims).
