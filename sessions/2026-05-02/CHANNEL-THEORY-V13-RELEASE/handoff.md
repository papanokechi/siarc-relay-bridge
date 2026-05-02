# Handoff — CHANNEL-THEORY-V13-RELEASE
**Date:** 2026-05-02
**Agent:** GitHub Copilot (VS Code, Claude Opus 4.7)
**Session duration:** ~45 minutes
**Status:** COMPLETE (verdict `CT_V13_BUILT_AND_STAGED`, PARTIAL —
awaits operator Zenodo upload + Item-19 DOI back-fill)

## What was accomplished

Built Channel Theory for Polynomial Continued Fractions v1.3 as a
purely additive framing revision of v1.2. Absorbed (i) the SIARC
umbrella v2.0 invariant-triple framing
$\Phi : \mathrm{PCF}(1,b) \mapsto (\Delta_d(b),\,\|\Delta\|_{\mathrm{Pet}}(\tau_b),\,\xi_0(b))$,
(ii) the PCF-2 v1.3 / PCF2-SESSION-T2 cubic-modular Petersson-height
result ($\rho = +0.638$, $p_{\mathrm{Bonf}} = 8.6\times 10^{-6}$ at
$n=50$, beats $\log|j|$ by $\sim 30\times$), and (iii) the
Theory-Fleet H4 HIGH-confidence theoretical prediction
`MEDIAN_RESURGENCE_GIVES_30+_DIGITS` for $V_{\mathrm{quad}}$. Reframed
`op:cc-formal-borel` as PARTIALLY DIAGNOSED with a sharper sub-problem
`op:cc-median-resurgence-execute` (new, first entry of §9). Built
clean (3 pdflatex + 1 bibtex; 17 pp; 0 unresolved citations / 0
undefined refs in pass 3), staged all 16 deliverables under
`sessions/2026-05-02/CHANNEL-THEORY-V13-RELEASE/`, and authored an
Item-19 patch for `tex/submitted/submission_log.txt` with a
`__VERSION_DOI__` placeholder for operator post-execution.

## Key numerical findings

(v1.3 introduces no new numerical findings of its own; it cites and
folds in the post-T2 cohort.)

- Petersson-height correlation $\rho = +0.638$,
  $p_{\mathrm{Bonf}}(K{=}14) = 8.6\times 10^{-6}$ on $n=50$ cubic
  families (cited from `sessions/2026-05-02/PCF2-SESSION-T2/verdict.md`,
  Phase B/C; PCF-2 v1.3, [SIARC v2.0, §4.4]).
- Theory-Fleet H4 HIGH-confidence theoretical prediction: median
  Écalle resurgence at 5000 coefficients / dps 250 extracts the
  $V_{\mathrm{quad}}$ alien amplitude at $\zeta_*=4/\sqrt 3$ to
  30--50 digits, central forecast ~40 digits (cited from
  `sessions/2026-05-01/THEORY-FLEET/H4/verdict.md`, NOT executed in
  this session).
- $\xi_0$ identity at $d=2$ proven (Prop 3.3.A, 200 dps), at $d=4$
  verified (Prop 3.3.A', spread 0 across 8 representatives at dps 80;
  PCF2-SESSION-Q1).
- v1.3 PDF: 17 pages, 581459 B; v1.3 .tex: 70170 B (1.277× v1.2's
  54961 B, well above the 1.05× anti-deletion threshold).

## Judgment calls made

1. The user prompt cites `[SIARC v2.0, §4.4]` for the
   invariant-triple subsection of the umbrella, but the actual umbrella
   v2.0 source (`tex/submitted/umbrella_program_paper/main.tex`) has
   that material at §3.1--§3.5 by my reading of the TOC. I followed the
   user-supplied cite handle verbatim per the explicit prompt
   instructions and logged the discrepancy in `unexpected_finds.json`
   (UF-V13-3) for downstream reconciliation.

2. The Phase A10 bib entries' `note` fields hit two BibTeX-mangling
   issues on the first build (`\Q` macro undefined; inline math /
   underscores in plain text). Both were resolved by macro-free /
   LaTeX-safe rewrites of the *prose* in the notes (no bibliographic
   substance changed). Logged as UF-V13-1 and UF-V13-2 in
   `unexpected_finds.json`.

3. `op:xi0-d3-direct` was carried forward unchanged: no
   `sessions/2026-05-{01,02}/CHANNEL-XI0-D3-DIRECT/` folder exists on
   disk, so the prompt's default branch ("**Status (v1.3):** Carried
   forward unchanged") was applied.

4. The `siarc_umbrella` legacy bib entry was retained (per A7
   instructions) for v1.0 / v1.1 historical references; the §4 channel
   functor and §1 Position citations now point to `siarc_umbrella_v2`.

## Anomalies and open questions

- **THE main anomaly: H4 is theory, not experiment.**
  `op:cc-median-resurgence-execute` is now the gating step to fully
  discharge the residual Laplace ambiguity in `op:cc-formal-borel`. v1.3
  carefully marks this throughout the document (see
  `rubber_duck_critique.md` §C1), but Claude / the human reviewer
  should double-check that no downstream paper (D1-PAPER, D2-NOTE,
  SIARC-MASTER-V0) accidentally elevates the H4 prediction to an
  asserted result when citing `[CT v1.3, §3.5]`.

- **§-numbering of the umbrella v2.0 cite handle.** The cite handle
  `[SIARC v2.0, §4.4]` is used throughout v1.3 (abstract, §1 What is
  new in v1.3, §3.6, §10 v1.3 subsection) but the umbrella v2.0 main
  source has the invariant-triple material at §3.1–§3.5. If the
  umbrella's section numbering is canonical (and the prompt's `§4.4`
  reference is therefore the wrong handle), v1.3 will need a one-line
  errata patch when the next channel-theory revision lands. Logged at
  UF-V13-3.

- **Bibliography `note` field LaTeX-safety.** The plain.bst style is
  fragile around inline math and underscore-bearing tokens in `note`
  fields. Future bib additions should use macro-free LaTeX in `note`
  (e.g. `V\_quad` not `V$_{\mathrm{quad}}$`; escaped underscores via
  brace pairs `\_{...}` for compound tokens). UF-V13-2 logs the rule
  for future relays.

- **Page count check.** v1.3 lands at 17 pp, comfortably within the
  [15, 22] threshold; the +3 pp growth versus v1.2's 14 pp comes from
  §3.5 + §3.6 (~1.5 pp), §10 v1.3 subsection (~0.7 pp), and
  scattered op-list / abstract / AI-disclosure additions (~0.8 pp).

## What would have been asked (if bidirectional)

1. The umbrella v2.0 cite handle: should v1.3 use `[SIARC v2.0, §3.4]`
   (the actual section number for the $\xi_0$ axis subsection in the
   umbrella source) or `[SIARC v2.0, §4.4]` (the prompt-supplied
   handle)? I followed the prompt verbatim but flagged this in
   `unexpected_finds.json`.

2. PCF2-SESSION-T2 reports two stronger predictors than the Petersson
   height ($\log\|\eta\|$ and $\log\mathrm{Im}\,\tau$ at $\rho = +0.642$,
   $p_{\mathrm{Bonf}} = 7\times 10^{-6}$) alongside
   $\log\|\Delta\|_{\mathrm{Pet}}$ at $+0.638 / 8.6\times 10^{-6}$. The
   prompt explicitly anchors the v1.3 cite at the Petersson-height row,
   so v1.3 quotes only that pair; I did not surface the other two
   correlations to keep the cite-handle clean. If the umbrella v2.0
   itself surfaces $\log\|\eta\|$ as the headline predictor in a future
   revision, v1.3 will need a follow-up cite.

## Recommended next step

Spec a `CHANNEL-CC-MEDIAN-RESURGENCE-EXECUTE` relay session that
implements the H4 recipe end-to-end on $V_{\mathrm{quad}}$:

1. Generate the 5000-coefficient Birkhoff formal pair
   $f_\pm(u) = \exp(\pm 2/(u\sqrt 3))\,u^{-11/6}\,(1 + \sum a_k u^k)$
   at mpmath dps 250 using the existing CC-PIPELINE-G
   `newton_birkhoff.py` (5000-coef generation is the bottleneck).
2. Fit the Borel-plane branch exponent at $\zeta_* = 4/\sqrt 3$ from
   the large-order tail of $a_k$ via Borel--Darboux relations.
3. Apply the median half-Stokes prescription
   $\mathcal S_{\mathrm{med}} = \mathcal S_{0^-} \circ \mathfrak S_0^{1/2}$
   to extract the leading alien amplitude $S_{\zeta_*}$.
4. Cross-check via local Borel singular-germ fitting in a neighbourhood
   of $\zeta_*$.
5. PSLQ the extracted constant against a Gamma-product basis
   ($\Gamma(1/3),\Gamma(1/6),\pi^{-1},\sqrt 3$) at $\geq 100$ digits to
   probe a closed-form candidate (H4 explicitly forecasts only
   precision, not closed form; PSLQ is a stretch goal).
6. Document the result in `sessions/2026-05-XX/CHANNEL-CC-MEDIAN-RESURGENCE-EXECUTE/`
   and trigger a Channel Theory v1.4 release that converts
   `op:cc-median-resurgence-execute` from a theoretical-prediction
   problem into an executed-measurement remark.

If $S_{\zeta_*}$ is recovered at $\geq 30$ digits, this conditionally
closes $V_{\mathrm{quad}} \rightsquigarrow P_{III}(D_6)$ at the
Stokes-data level (modulo a documented normalisation map to the
$P_{III}(D_6)$ isomonodromic Stokes datum).

## Files committed

Under `sessions/2026-05-02/CHANNEL-THEORY-V13-RELEASE/`:

- `archive/channel_theory_outline_v1.2_baseline.tex` (54961 B, verbatim
  v1.2 source pre-edit; SHA-256
  `b60199848f4fe943a4ba0558a6e9168d6ff07109f9f7aa7ebe21ab5544474e48`)
- `channel_theory_outline.tex` (70170 B, v1.3 source; SHA-256
  `59c5352795f8d63dc59ac6ba11e96f91805d424cd6e20d74f52c9a565846f7e5`)
- `channel_theory_outline.pdf` (581459 B, 17 pp v1.3 build; SHA-256
  `df3b90e808e49e84fbba53e5663a851256303496fc1536fefbf962aba2ebdc18`)
- `annotated_bibliography.bib` (28168 B, v1.3 bib + 4 new entries;
  SHA-256
  `c2e3987b2e92befcbf6de252052a83417d13ce58f867c1dd1dfea2519099438a`)
- `build.log` (pdflatex pass-3 log; SHA-256
  `282f49fb4c47beb561858c7121447d3d7b38e32438353a2998d5b4f78d1439c3`)
- `build_diff.txt` (v1.2 → v1.3 git-diff)
- `zenodo_description_v1.3.txt`
- `zenodo_notes_v1.3.txt`
- `submission_log_patch_item19.txt`
- `claims.jsonl` (11 AEAL entries CT-V13-A1..A11)
- `verdict.md` (`CT_V13_BUILT_AND_STAGED`)
- `rubber_duck_critique.md` (9 explicit checks: C1..C9)
- `halt_log.json` (`{}`)
- `discrepancy_log.json` (`{}`)
- `unexpected_finds.json` (3 informational findings UF-V13-1..UF-V13-3)
- `handoff.md` (this file)

Also committed in-place under
`pcf-research/channel/cc_pipeline_v13_2026-05-02/`:
`channel_theory_outline.tex`, `.pdf`, `annotated_bibliography.bib`,
`.bbl`, `.aux`, `.log`, `.out`, `.toc`. (Not pushed to bridge.)

## AEAL claim count

11 entries written to `claims.jsonl` this session
(CT-V13-A1..CT-V13-A11; A11 carries SHA-256 hashes of all session
deliverables and the four reference files cited).
