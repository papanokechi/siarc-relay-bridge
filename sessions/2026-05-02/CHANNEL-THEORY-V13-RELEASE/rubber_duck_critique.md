# Rubber-duck critique — CHANNEL-THEORY-V13-RELEASE

Per Phase F instructions; ≥7 explicit checks of v1.3.

## C1 — Is the H4 phrasing AEAL-honest?

PASS. Every mention of median resurgence in v1.3 is explicitly framed as
*theoretical prediction* / *predicts at HIGH confidence* / *forecast*:

- Abstract: "...the Theory-Fleet H4 prediction... that median Écalle
  resurgence at 5000 coefficients delivers..."  (present tense
  *predicts*-style, matches H4 verdict.md exactly).
- §3.5 Remark `rem:h4-median`: opens with the literal phrase
  "Theory-Fleet H4 \cite{siarc_theory_fleet_h4} is a *theoretical
  prediction at HIGH confidence* — not an executed measurement —..."
- §9 op:cc-median-resurgence-execute: "Theory-Fleet H4 \cite{...}
  *predicts at HIGH* confidence..."
- §9 op:cc-formal-borel: "**Status (v1.3):** PARTIALLY DIAGNOSED by
  Theory-Fleet H4 \cite{...}, which *predicts at HIGH confidence*..."
- §1 "What is new in v1.3" paragraph: "predicts at HIGH confidence".

`grep -P '\bconfirms\b|\bdemonstrates\b|\bproves the.*alien|\bshows.*30.*digit'`
on the v1.3 source returns 0 matches. The forbidden over-claim verbs are
absent.

## C2 — Is the bibliography concept-vs-version DOI distinction correct?

PASS. Audit:

- `siarc_umbrella_v2.note`: "Version DOI 10.5281/zenodo.19965041 (v2.0,
  current); concept DOI 10.5281/zenodo.19885549 (cite-all)." ✓
- `siarc_pcf2_v13.note`: "Version DOI 10.5281/zenodo.19963298 (v1.3,
  current); concept DOI 10.5281/zenodo.19936297 (cite-all)." ✓
- §10 v1.3 subsection bullets: SIARC umbrella v2.0 carries concept
  19885549 and version 19965041; PCF-2 v1.3 carries concept 19936297 and
  version 19963298. ✓
- submission_log_patch_item19 "Concept DOI preserved" line uses
  19941678 (the Channel Theory concept) — NOT 19951331 (which is the v1.2
  *version* DOI). ✓
- zenodo_description_v1.3 final paragraph: "Concept DOI preserved
  (10.5281/zenodo.19941678); v1.0, v1.1, and v1.2 are superseded" — ✓.
- zenodo_notes_v1.3: same concept DOI 19941678 used. ✓

The "umbrella v2 patch" gotcha (concept-vs-version confusion) does NOT
recur at v1.3.

## C3 — Are all four new bib entries cited at least once in the v1.3 body?

PASS.

- `siarc_umbrella_v2`: cited in abstract, §1 "What is new in v1.3", §1
  Strategic position, §3.6, §4 Channel functor, §9 op:bridge-witness-tier
  (via `siarc_pcf2_v13`), §10 v1.3 subsection.
- `siarc_pcf2_v13`: cited in §1 "What is new in v1.3", §1 Strategic
  position, §3.6 (twice), §9 op:bridge-witness-tier, §9
  op:cc-channel-existence, §10 v1.3 subsection, AI Disclosure.
- `siarc_pcf2_session_t2`: cited in §1 Strategic position, §3.6, §10 v1.3
  subsection.
- `siarc_theory_fleet_h4`: cited in abstract, §1 "What is new in v1.3",
  §3.4 forward-link paragraph, §3.5 (twice), §9
  op:cc-median-resurgence-execute, §9 op:cc-formal-borel, §10 v1.3
  subsection, AI Disclosure.

## C4 — Does the new §3.5 / §3.6 placement break any prior cross-reference?

PASS. The new subsections are inserted **inside** the existing
§3 (Catalogue of channels in the SIARC stack) container, AFTER §3.4
(`ssec:wkb`) and BEFORE §4 (`sec:functor`). The existing `\Cref` /
`\ref` targets in the v1.2 body are:

- `sec:position`, `sec:def`, `sec:catalogue`, `sec:functor`, `sec:nogo`,
  `sec:bridge`, `sec:related`, `sec:implications`, `sec:open` — all
  preserved.
- `ssec:lt`, `ssec:bot`, `ssec:cc`, `ssec:comparison`, `ssec:wkb` — all
  preserved.
- `prop:xi0`, `prop:xi0-d4`, `prop:noninj`, `prop:wkb`, `thm:vquad-cc`,
  `conj:xi0-univ`, `conj:nogo`, `conj:bridge`, `conj:chi`, `def:channel`
  — all preserved.

The new labels `ssec:h4-median`, `ssec:invariant-triple`,
`rem:h4-median`, `ssec:sessions-v13` are additive only.
Pass-3 pdflatex log reports zero "Reference ?? on page N undefined"
warnings (verified via Select-String on channel_theory_outline.log).

## C5 — Does op:cc-median-resurgence-execute correctly point to the H4 evidence chain?

PASS. The op:cc-median-resurgence-execute entry in §9 cites
`\cite{siarc_theory_fleet_h4}` (which resolves to the H4 bridge URL
`sessions/2026-05-01/THEORY-FLEET/H4/`), NOT to the umbrella v2.0
\S4.4 paragraph. The entry quotes the H4 verdict's exact numerical
parameters (5000 coefficients, dps 250, ζ* = 4/√3, 30–50 digits, ~40
digit central forecast) and cross-references the algorithmic recipe
(branch exponent fit, half-Stokes prescription, local Borel
singular-germ fitting) from H4 verdict.md / summary.md. The umbrella
v2.0 \S4.4 cite handle is reserved for the *invariant-triple framing*
in §3.6 and the abstract.

## C6 — Does v1.3 preserve every theorem / proposition / conjecture of v1.2 verbatim?

PASS. `git diff --no-index archive/channel_theory_outline_v1.2_baseline.tex
channel_theory_outline.tex > build_diff.txt` shows that:

- All `\begin{theorem}` / `\begin{proposition}` / `\begin{conjecture}` /
  `\begin{problem}` / `\begin{remark}` / `\begin{definition}` blocks from
  v1.2 appear verbatim in v1.3. The diff additions are confined to:
  abstract sentence (1 line), §1 "What is new in v1.3" paragraph, §1
  Strategic position paragraph, §3.4 forward-link paragraph, §3.5 (new
  subsection + remark), §3.6 (new subsection, no theorem), §4 cite
  swap (`siarc_umbrella` → `siarc_umbrella_v2`), §9 prepended
  op:cc-median-resurgence-execute + four status-prefix appends, §10 v1.3
  subsection (new), AI Disclosure paragraph (new), bib (4 new entries),
  version macro / date.

No v1.2 theorem / proposition / conjecture statement is altered. The
build_diff.txt is committed alongside this critique for reviewer audit.

## C7 — Does v1.3's open-problems list have exactly one new entry?

PASS. v1.2 §9 had 11 problem entries. v1.3 §9 has 12 entries: the
single new entry is `op:cc-median-resurgence-execute` placed FIRST.
Modifications to the four pre-existing entries (op:cc-formal-borel,
op:xi0-d3-direct, op:bridge-witness-tier, op:cc-channel-existence
(legacy)) are *prefix* / *append* status notes — they do not increase
the entry count.

`grep -c '\\begin{problem}\[\\textsf{op:' channel_theory_outline.tex`
returns 12; the v1.2 baseline returns 11.

## C8 (extra) — Halt-threshold sanity check

PASS. All Phase B halt thresholds satisfied:

- pass-3 log has 0 unresolved citations / 0 undefined references.
- PDF page count = 17 ∈ [15, 22].
- Source file size = 70170 B ≥ 1.05 × 54961 = 57709 B (1.277× growth).
- AEAL-honesty grep: no over-claim verbs in v1.3 prose.
- Concept DOI 19941678 used as concept only, never as a version DOI.

## C9 (extra) — Operator-handoff cleanliness

PASS. submission_log_patch_item19.txt uses `__VERSION_DOI__` placeholder
(matching the umbrella v2.0 / PCF-2 v1.3 patch convention); 11-space
continuation indentation matches the live submission_log.txt at item 18;
insertion zone correctly identified as "after current line 577 / before
current line 578"; concept DOI preserved across versions.

---

Overall: v1.3 ships at verdict `CT_V13_BUILT_AND_STAGED` (PARTIAL —
awaits operator Zenodo upload + Item-19 DOI back-fill).
