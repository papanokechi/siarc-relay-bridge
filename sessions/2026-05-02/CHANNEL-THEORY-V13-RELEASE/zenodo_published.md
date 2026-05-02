# Zenodo publication record — Channel Theory v1.3

**Status:** PUBLISHED (post-handoff addendum to commit `d2b3f88`)
**Published:** 2026-05-02 ~17:00 JST
**Operator action time:** ~30 min (Edit-metadata polish pass pending; see TIER 1 below)

## Identifiers

| Field | Value |
|-------|-------|
| Version DOI | `10.5281/zenodo.19972394` |
| Concept DOI | `10.5281/zenodo.19941678` (preserved across versions) |
| isNewVersionOf | `10.5281/zenodo.19951331` (CT v1.2) |
| Title | Channel Theory for Polynomial Continued Fractions: Asymptotic Channels, the ξ₀ = 2/√β₂ Identity, and a Bridge Conjecture |
| Version field | `1.3` |
| Publication date | `2026-05-02` |
| Resource type | Preprint |
| Record URL | https://zenodo.org/records/19972394 |
| Concept-DOI URL | https://doi.org/10.5281/zenodo.19941678 (resolves to latest, currently this record) |
| Files-archive URL | https://zenodo.org/api/records/19972394/files-archive |
| PDF download | https://zenodo.org/records/19972394/files/channel_theory_outline.pdf?download=1 |

## File hash verification

| | Value |
|---|---|
| File name | `channel_theory_outline.pdf` |
| Size (bytes) | `581459` ✓ matches staged build artefact |
| SHA-256 (published) | `df3b90e808e49e84fbba53e5663a851256303496fc1536fefbf962aba2ebdc18` |
| SHA-256 (anchor, claims.jsonl A8) | `df3b90e808e49e84fbba53e5663a851256303496fc1536fefbf962aba2ebdc18` |
| Match | **✓ byte-identical** |
| Zenodo-side md5 | `e58951de5cbf1be7cdd26f335bc359af` |

Verification command (PowerShell):
```powershell
$ProgressPreference='SilentlyContinue'
$tmp = Join-Path $env:TEMP 'ct_v13_published.pdf'
Invoke-WebRequest -Uri 'https://zenodo.org/records/19972394/files/channel_theory_outline.pdf?download=1' -OutFile $tmp -UseBasicParsing
(Get-FileHash $tmp -Algorithm SHA256).Hash.ToLower()
# expect: df3b90e808e49e84fbba53e5663a851256303496fc1536fefbf962aba2ebdc18
```

The byte-identical match closes the AEAL chain on the file-content side:
the PDF that Zenodo serves is the same one that this session built and that
`claims.jsonl` claim CT-V13-A8 anchors. New claim `CT-V13-A12` records
the verification.

## Related identifiers as published (17 total)

`isNewVersionOf` `10.5281/zenodo.19951331` (CT v1.2)

`references` (7 ✓ — all targeted in `zenodo_description_v1.3.txt`):
- `10.5281/zenodo.19885549` (SIARC umbrella concept)
- `10.5281/zenodo.19965041` (SIARC umbrella v2.0)
- `10.5281/zenodo.19936297` (PCF-2 concept)
- `10.5281/zenodo.19963298` (PCF-2 v1.3)
- `10.5281/zenodo.19931635` (PCF-1 concept)
- `10.5281/zenodo.19937196` (PCF-1 v1.3)
- `10.5281/zenodo.19783311` (T2B concept)

`isDocumentedBy` (4 — 3 v1.3-targeted + 1 v1.2 carry-forward):
- `https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-05-02/CHANNEL-THEORY-V13-RELEASE/` ✓
- `https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-05-01/THEORY-FLEET/H4/` ✓
- `https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-05-02/PCF2-SESSION-T2/` ✓
- `https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-05-01/PCF2-SESSION-Q1/` (v1.2 carry; defensible to keep)
- `https://github.com/papanokechi/siarc-relay-bridge` (v1.2 carry; redundant — flagged for removal)

`isSupplementTo` (3 — all v1.2 carry-forward; flagged for removal):
- `10.5281/zenodo.19937196` (PCF-1 v1.3) — duplicates `references` entry
- `10.5281/zenodo.19939463` (PCF-2 v1.1) — superseded by PCF-2 v1.3 in `references`
- `10.5281/zenodo.19885550` (umbrella v1) — superseded by umbrella v2.0 in `references`

`cites` (2 — both v1.2 carry-forward):
- `10.5281/zenodo.19915689` (T2B v3.0) — redundant with `references` T2B concept
- `10.5281/zenodo.19783312` (T2B v1.0) — stale; superseded by T2B v3.0

## Outstanding metadata items (post-publish-editable, no DOI change)

### TIER 1 — CRITICAL: description supersede line

The "New version" flow auto-prefilled the v1.2 description body and only the
v1.3 update section was appended. The supersede sentence in the second
paragraph still reads:

```
v1.1 (10.5281/zenodo.19941679) is superseded by v1.2.
```

It must be replaced with the v1.3-correct line (already in
`zenodo_description_v1.3.txt` line 9):

```
v1.1 (10.5281/zenodo.19941679) and v1.2 (10.5281/zenodo.19951331) are superseded by v1.3.
```

### TIER 2 — OPTIONAL: stale related identifiers

Six carry-forward entries can be removed (see table above and full runbook
at `tex/submitted/control center/zenodo_postpublish_edits_ct_v13.md`).

### TIER 3 — DO NOT CHANGE: Method paragraph wording

The published `Method.` paragraph uses the v1.2 wording and is bracketed
by the verbatim-v1.2 description block per the design comment in
`zenodo_description_v1.3.txt` line 5
(`<!-- v1.0 / v1.1 / v1.2 description (preserved verbatim from v1.2) -->`).
The v1.3 update section already documents v1.3-specific AI use. No action.

## AEAL claim added

`claims.jsonl` line 12 (CT-V13-A12): records the published-DOI fact, the
isNewVersionOf chain, the file-size and SHA-256 verification, and the
Zenodo-side md5. `output_hash` is the PDF SHA-256
(`df3b90e808e49e84fbba53e5663a851256303496fc1536fefbf962aba2ebdc18`).

## Next steps

1. Operator runs the TIER 1 description fix on Zenodo `Edit metadata`.
2. Operator (optional) runs the TIER 2 related-identifier cleanup.
3. Operator fires Prompt 001 (`tex/submitted/control center/prompt/001_submission_log_patch_item19.txt`)
   in a fresh VS Code Copilot agent with `10.5281/zenodo.19972394` pasted as
   chat line 1. Agent splices Item 19 into `tex/submitted/submission_log.txt`
   and pushes to bridge.
4. Operator (parallel-able with 001) fires Prompts 002 and 003 per
   `tex/submitted/control center/prompt/_INDEX.txt`.
