# PCF2-V13-RELEASE verdict

**Verdict label:** `PCF2_V13_BUILT_AND_STAGED`

**Status:** PARTIAL — the build is clean and all release artefacts are
staged. The Zenodo upload (Phase D) is operator-blocking and has not
been performed in this session. The version DOI placeholder
`__VERSION_DOI__` in `submission_log_patch_item17.txt` is the
operator-fill point.

## Headline numbers

- v1.3 PDF: 22 pages (v1.2: 18 pages); 558,153 bytes; sha256
  `87B845A8E382F3C124906ACE0C1A6763CE54BD14C5F9593BBADC77BDD81D263F`.
- v1.3 source: sha256
  `82FE2315CFDA2047249D4978D7AE487C21D9BE16A35F15827CE132561F2C8541`.
- v1.2 baseline (preserved as
  `archive/pcf2_program_statement_v1.2_baseline.tex`): sha256
  `36A41E646C254701A17E1B69F74F30EBA3F295FDCF2C98BB25EF717B63B9D708`.
- Build: 3-pass pdflatex via MiKTeX; pass 3 grepped to single
  `Output written` line; `! ` (true error) lines = 0; missing
  citations = 0; unresolved cross-references = 0; warnings limited
  to one expected hyperref-PDF-string token warning on the v1.3
  abstract (no impact on output).
- AEAL claims: 9 entries in `claims.jsonl`.

## What v1.3 absorbs

1. **T2 (2026-05-02)** — cubic-modular framing. Petersson modular
   discriminant `‖Δ‖_Pet(τ_b)` beats `log|j(E_b)|` baseline by ~30×
   in p_Bonferroni at n=50 cubic families
   (ρ = +0.638, p_Bonf = 8.6×10⁻⁶ vs ρ = −0.568, p_Bonf = 2.34×10⁻⁴
   on R1.3 deep δ).
2. **R1.3 (2026-05-01)** — CASE B with C-caveat. B5/B6 are
   confirmed d=3-specific in their sharp/deep-WKB form; the d=4
   shallow-N j=0 shift is real but does not extend to deep N.
3. **R1.2 (2026-05-01)** — d=4 deep-WKB null. Spearman
   ρ(log|j|, δ_4) = +0.073, raw p = 0.58 (not significant; opposite
   sign to d=3 signal).
4. **R1.1 (2026-05-01)** — j-invariant signal upgrade. ρ = −0.691,
   p_Bonf = 4×10⁻⁷.

## Edits by section

- A1 (front matter): version line, date, hat-line — done.
- A2 (sec:conjectures): B5/B6 d=3-restriction signpost paragraph
  inserted before sec:B4.
- A3 (sec:R1-finer-split): full rewrite as multi-step narrative
  R1 → R1.1 → R1.2 → R1.3 → T2; drops in `\input` of
  `v13_paragraph_insert_v3_fixed.tex`,
  `phase_B_correlation_table.tex`, and
  `phase_E_v13_paragraph_fixed.tex` from this release folder.
- A4 (sec:openproblems): `op:finer-cubic-split` marked resolved with
  pointer to T2 verdict; `op:j-zero-amplitude-h6` and
  `op:j-1728-wedge` added; `op:shallow-j-effect-d4` and
  `op:b5-degree-d` defined in the inserted v3 file (no duplication).
- A5 (sec:why): `AEAL schema (v1.3 canonical form)` paragraph
  inserted before sec:litrel.
- A6 (bib): 4 new bibitems (T2 / R1.3 / Chowla–Selberg /
  Yu99).
- A7 (Acknowledgements): v1.3 absorption attribution appended.

## Operator next steps (Phase D)

1. Open https://zenodo.org/deposit; select "New version" of the
   existing PCF-2 record (concept DOI 10.5281/zenodo.19936297).
2. Upload `tex/submitted/pcf2_program_statement.pdf`.
3. Paste `zenodo_description_v1.3.txt` into the description field.
4. Paste `zenodo_notes_v1.3.txt` into the version-notes field.
5. Set DataCite relations:
   - `IsNewVersionOf` → `10.5281/zenodo.19951458` (PCF-2 v1.2)
   - `IsSupplementedBy` → `10.5281/zenodo.19941678` (Channel theory concept)
   - `References` → `10.5281/zenodo.19937196` (PCF-1 v1.3 concept)
   - `IsPartOf` → `10.5281/zenodo.19885550` (SIARC umbrella)
6. Publish; capture the new version DOI; pass it to the
   `SUBMISSION-LOG-PATCH` follow-up to fill `__VERSION_DOI__` in
   `submission_log_patch_item17.txt` and append the block to
   `tex/submitted/submission_log.txt`.
