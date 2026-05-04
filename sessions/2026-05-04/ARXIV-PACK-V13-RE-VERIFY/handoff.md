# Handoff -- ARXIV-PACK-V13-RE-VERIFY
**Date:** 2026-05-04
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~45 minutes
**Status:** COMPLETE (with one annotated caveat -- see "Anomalies and open questions")

## What was accomplished

Rebuilt the v1.3 arXiv-mirror tarball for PCF-1 from the canonical
16pp source preserved at bridge commit `58dfa9e`
(`sessions/2026-05-01/PCF1-V13-UPDATE/`). All Phase A gates green
(commit reachable; tex SHA `e83bb377...74be301` matches 027; pdf
SHA `63420dbf...d9788ff5e` byte-matches Zenodo; pypdf reports 16
pages). Phase B `git archive` extract re-verified byte-identity.
Phase C tarball assembled with `tar -czf` containing exactly
`pcf1_v1.3/{00README.txt, abstract.txt, p12_pcf1_main.tex}`.
Phase D wrote manifest.txt + hash_match.json + abstract.txt +
00README.txt and cross-checked Zenodo via the public API
(record 19937196 returned md5 `fbf5449b...aef5e0` and size 392886,
both byte-equal to the local canonical PDF). Phase F deployed the
verified pack to `sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/
arxiv_pack_pcf1_v1.3_REBUILT/` and added a `REDIRECT_TO_REBUILT.txt`
notice alongside the contaminated 21pp materials in the original
`arxiv_pack_pcf1_v1.3/` (retained for forensic diff per spec).

## Key numerical findings

- TeX SHA-256 (16pp v1.3 canonical):
  `e83bb377f297dbf0837facba257f227df4579e6a3518c139e3146f17174be301`,
  46,349 bytes, 925 lines (script: `Get-FileHash`, dps n/a).
- PDF SHA-256 (16pp v1.3 canonical):
  `63420dbf4abb7124672f522c37fc04ebdb3f6694ac39959456b2890d9788ff5e`,
  392,886 bytes, 16 pages (script: `Get-FileHash` + `pypdf`,
  byte-exact match against Zenodo record 19937196).
- PDF md5 (canonical): `fbf5449b2678834b0204360d49aef5e0`
  (matches Zenodo API response for record 19937196).
- Tarball SHA-256 (this build only -- gzip mtime non-deterministic):
  `93770e03c6ab9324ae1acd256b62c3af79e93a21ab83c653d412a0acab216ec9`,
  17,560 bytes, 3 entries.

## Judgment calls made

- **PDF placement.** Spec §C.2 says "copy tex + pdf" into pack/.
  arXiv-canonical practice is to NOT embed the compiled PDF inside
  the source tarball (arXiv recompiles from source). I matched the
  existing 002 convention: PDF lives **alongside** the tarball in
  the wrapper directory, not inside it. Tarball contents are
  `pcf1_v1.3/{00README, abstract, .tex}` only.
- **Tarball name.** Used `pcf1_v1.3.tar.gz` (matching existing 002
  convention) rather than `arxiv_pcf1_v1.3.tar.gz`. Spec offered
  either.
- **Spec Zenodo IDs.** Spec named DOI 19941678 (concept) and 19963298
  (version) -- both wrong (see Anomalies). Used the correct record
  19937196 (DOI 10.5281/zenodo.19937196), which is what the existing
  002 hash_match.json already documented. Did NOT halt on this; it
  is a low-severity spec-transcription artefact and the byte-equality
  verification is independent of the record-ID question.
- **No `\title` modification.** Title block in the .tex is multi-line
  (`\title[CM Predicate ...]{Complex Multiplication ...}`) and was
  not modified per spec.

## Anomalies and open questions

THIS IS THE MOST IMPORTANT SECTION. Read carefully.

### A1  Spec Zenodo identifiers are incorrect (low severity, action item)

The prompt §0 "frozen DOI" cheat-sheet line and §D.4 spec for
hash_match.json both name `10.5281/zenodo.19941678` (concept) and
`10.5281/zenodo.19963298` (v1.3 version). Neither resolves to the
PCF-1 v1.3 deposit:

| spec id   | actual deposit (per Zenodo API)                                      |
| --------- | -------------------------------------------------------------------- |
| 19941678  | redirected to 19972394 = "Channel Theory for Polynomial Continued    |
|           | Fractions" (a different paper, not PCF-1)                            |
| 19963298  | "PCF-2 program statement" (file pcf2_program_statement.pdf, 558153 B)|

The actual PCF-1 v1.3 deposit is record **19937196**
(DOI `10.5281/zenodo.19937196`, version 1.3, file p12_pcf1_main.pdf
md5 `fbf5449b...aef5e0`, size 392886). This is what the existing
002 `hash_match.json` (written 2026-05-02) already had encoded as
the URL `https://zenodo.org/records/19937196/files/p12_pcf1_main.pdf`.

Operator/Claude-side action: update the RESUME_AFTER_REBOOT
cheat-sheet and any picture v1.14 strategic-row reference that
quotes 19941678 / 19963298 for PCF-1; the correct id is 19937196.
Logged in `unexpected_finds.json` UF-030-1.

### A2  Tarball SHA is non-deterministic (informational)

`tar -czf` uses gzip which embeds a build-time mtime in the header.
The recorded tarball SHA `93770e03...216ec9` is for THIS build only;
re-running produces byte-identical contents but a different SHA.
Re-verification should be done at the per-file level (manifest.txt
SHAs are deterministic). Logged as UF-030-2.

### A3  No HALT conditions triggered

`halt_log.json` is empty. All §4 gates green.

## What would have been asked (if bidirectional)

- "The cheat-sheet says 19941678 / 19963298 but those records are
  Channel Theory and PCF-2 program statement, not PCF-1 v1.3. Is the
  correct id 19937196 (which the existing 002 hash_match.json
  already uses)? Should I update the cheat-sheet, or proceed with
  19937196 silently?"  -- Resolved by autonomous judgment in favour
  of the existing 002 evidence + Zenodo API truth-source. Flagged
  here for review.

## Recommended next step

Operator one-click: dispatch the 3 Tier-1 endorsement emails (G14,
ENDORSER-HANDLE-ACQUISITION 2026-05-04). When at least one
endorsement lands, fire Prompt 002 re-fire (RUNBOOK_pcf1.md) using
`sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_pcf1_v1.3_REBUILT/
pcf1_v1.3.tar.gz` as the upload payload + the rebuilt `00README.txt`
+ `abstract.txt` for the arXiv web-form abstract field. The other
4 mirror records (umbrella v2.0, PCF-2 v1.3, CT v1.3, T2B v3.0)
were not audited this session; a parallel audit prompt would be
prudent if any of them have similar page-count drift symptoms.

## Files committed

```
sessions/2026-05-04/ARXIV-PACK-V13-RE-VERIFY/
  prompt_spec_used.md
  source_verification.md         (Phase A log)
  tarball_construction.md        (Phase B + C + D.5 log)
  claims.jsonl                   (10 AEAL claims)
  halt_log.json                  ({})
  discrepancy_log.json           ({})
  unexpected_finds.json          (UF-030-1 spec-id, UF-030-2 tar-determinism)
  handoff.md                     (this file)
  extract/sessions/2026-05-01/PCF1-V13-UPDATE/p12_pcf1_main.{tex,pdf}
                                 (git-archive raw extract; for traceability)
  pack/
    p12_pcf1_main.pdf            (canonical 16pp PDF, 392886 B)
    pcf1_v1.3.tar.gz             (rebuilt tarball, 17560 B)
    manifest.txt                 (per-file SHA-256 manifest)
    hash_match.json              (verification record)
    pcf1_v1.3/
      00README.txt
      abstract.txt
      p12_pcf1_main.tex

sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/
  arxiv_pack_pcf1_v1.3/
    REDIRECT_TO_REBUILT.txt      (NEW -- forensic redirect notice)
  arxiv_pack_pcf1_v1.3_REBUILT/  (NEW directory -- mirrors pack/ above)
    p12_pcf1_main.pdf
    pcf1_v1.3.tar.gz
    manifest.txt
    hash_match.json
    pcf1_v1.3/
      00README.txt
      abstract.txt
      p12_pcf1_main.tex
```

## AEAL claim count

10 entries written to claims.jsonl this session.

## Verdict

**UPGRADE_ARXIV_PACK_V13_REBUILT_PARTIAL_SPEC_ZENODO_IDS_CORRECTED**
(per §7 outcome ladder: pack rebuilt cleanly, all Phase A-F gates
green, Zenodo md5/size/sha256 byte-matches confirmed; one caveat
= spec's Zenodo concept/version IDs were transcription errors and
the canonical record is 19937196, not 19941678 / 19963298).

Pack is **READY for Prompt 002 re-fire** after operator-side
endorsement obtained (G14, ENDORSER-HANDLE-ACQUISITION).
