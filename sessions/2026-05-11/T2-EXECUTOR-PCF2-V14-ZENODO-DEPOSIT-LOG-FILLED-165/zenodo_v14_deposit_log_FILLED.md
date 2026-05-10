# Zenodo deposit log — PCF-2 v1.4 (OPERATOR-FILLED)

**Status**: FILLED at deposit landing (2026-05-11 JST). Source template: slot 137 (bridge SHA `45e236c`; LANDED → immutable; copied here for fill-in).

**Source template**: `sessions/2026-05-09/T2-EXECUTOR-PCF2-V14-M7-V0-AMENDMENT-PREP-137/zenodo_v14_deposit_log.md`
**Deposit-ordering position**: 1st of 3 in cascade-132 Option α (PCF-2 v1.4 → umbrella v2.2 → picture-chain v1.20+).
**Substrate used at deposit time**: paste-source from slot 163+164 (`b936eb0`) `amended_description_block_corrected.md` (umbrella concept-DOI corrected to `19885549`).

---

## §1 Deposit metadata (FILLED)

| Field                                  | Value                                              |
|----------------------------------------|----------------------------------------------------|
| Deposit date / time (UTC)              | 2026-05-10 22:12:12 UTC (= 2026-05-11 07:12 JST)   |
| Operator                               | papanokechi                                        |
| Zenodo concept DOI                     | `10.5281/zenodo.19936297`                          |
| Assigned v1.4 version DOI              | `10.5281/zenodo.20114315`                          |
| Zenodo record URL                      | https://zenodo.org/records/20114315                |
| Zenodo deposit-ID (numeric)            | `20114315`                                         |
| Concept-recid (parent)                 | `19936297`                                         |
| Version-sequence position (API)        | index 4 (5th total; `is_last: true`)               |
| State                                  | `published` / `submitted: true`                    |
| Resource type (main)                   | **Working paper** (`publication / workingpaper`) — **see §6 Note 1** |
| Access right                           | `open`                                             |
| License                                | `cc-by-4.0`                                        |

## §2 Files uploaded (VERIFIED post-deposit)

| Filename                         | Size (B) | SHA-256-16 (local)   | MD5 (local)                          | MD5 (Zenodo-side)                    | Match |
|----------------------------------|----------|----------------------|--------------------------------------|--------------------------------------|-------|
| `pcf2_program_statement_v14.pdf` | 636,049  | `471DC7C7EBF8BD4F`   | `b58c0cfd2359cc540d7d8e9750e09e59`   | `b58c0cfd2359cc540d7d8e9750e09e59`   | ✓     |
| `pcf2_program_statement_v14.tex` | 80,244   | `0CF4E7DC90C1AC2A`   | `10bf7ebfab03adc8007313da059f3e63`   | `10bf7ebfab03adc8007313da059f3e63`   | ✓     |
| `b_amendment_v14.diff`           | 10,486   | `30371C2EBD9885B1`   | `c3aa31de2b5c5618e5d82c9310bc8f45`   | `c3aa31de2b5c5618e5d82c9310bc8f45`   | ✓     |

All 3 files: byte-for-byte integrity verified via MD5 round-trip (local ↔ Zenodo). No source-bundle flatten was applied (the 3-file upload was accepted as-is).

## §3 Related-identifiers row record (VERIFIED via Zenodo record JSON API at `https://zenodo.org/api/records/20114315`)

| Relation         | Identifier (DOI)                          | Resource type           | API confirmed |
|------------------|-------------------------------------------|-------------------------|---------------|
| `isNewVersionOf` | `10.5281/zenodo.19963298` (PCF-2 v1.3)    | `publication-preprint`  | ✓             |
| `isSupplementTo` | `10.5281/zenodo.19931635` (PCF-1 concept) | `publication-preprint`  | ✓             |
| `cites`          | `10.5281/zenodo.19931635` (PCF-1 concept) | `publication-preprint`  | ✓             |
| `isSupplementTo` | `10.5281/zenodo.19885549` (Umbrella concept; **DOI-CORRECTED** per slot 163+164) | `publication-preprint`  | ✓             |
| `cites`          | `10.5281/zenodo.19885549` (Umbrella concept; **DOI-CORRECTED** per slot 163+164) | `publication-preprint`  | ✓             |

**Critical verification**: the two Umbrella rows correctly cite `19885549` (concept), NOT `19885550` (v1.0 version-DOI). The slot 163+164 DOI correction was successfully propagated through Zenodo's deposit form. D-162-1 closure confirmed at the deposited-record level.

## §4 Sidebar cross-check (per operator paste 2026-05-11 ~07:12 JST)

- [x] Concept DOI on the PCF-2 page sidebar = `10.5281/zenodo.19936297` ✓
- [x] PCF-2 v1.3 version DOI on the page sidebar = `19963298` ✓ (matches paste-source)
- [x] Full version chain (5 versions; v1.4 latest):
  - v1.4: `10.5281/zenodo.20114315` (2026-05-11) ← THIS DEPOSIT
  - v1.3: `10.5281/zenodo.19963298` (2026-05-02)
  - v1.2: `10.5281/zenodo.19951458` (2026-05-01)
  - v1.1: `10.5281/zenodo.19939463` (2026-05-01)
  - v1.0: `10.5281/zenodo.19936298` (2026-05-01) — **NB**: ONE DIGIT off from concept `19936297` (third confirmed instance of the v1.0-vs-concept single-digit anti-pattern; see UF-165-2)
- [x] PCF-1 concept DOI on PCF-1 page sidebar = `10.5281/zenodo.19931635` ✓ (cross-link target intact)
- [x] Umbrella concept DOI on Umbrella page sidebar = `10.5281/zenodo.19885549` ✓ (cross-link target intact; D-162-1 substrate-side closure confirmed)

No sidebar mismatch detected. Deposit cleared §4 sidebar gate.

## §5 Post-deposit follow-on actions (status as of this fire)

1. [x] Capture assigned v1.4 version DOI from Zenodo confirmation page → `20114315` (this log).
2. [ ] Update `cross_link_update_log.md` (sibling template) with the v1.4 version DOI. *(Deferred — sibling template not yet created at slot 137; this log entry serves as the canonical record.)*
3. [x] Splice `submission_log_v14_splice.diff` into `tex/submitted/submission_log.txt` → see `submission_log_v14_splice_applied.md` in this same slot folder; committed to `claude-chat` repo branch `vquad/handoff-2026-04-16` at SHA `<filled at apply time>`.
4. [ ] Splice v1.4 version DOI `20114315` into umbrella v2.2's `zenodo_v22_description_block.md` `IsSupplementTo` row → requires NEW slot 166 OVERLAY-COPY (slot 162 amended block currently has concept-granularity `19936297`; verify whether v1.4 version-DOI is required by the row OR whether concept-granularity is intended). **Operator decision pending**: keep concept granularity, OR add v1.4-specific `IsSupplementTo` row?
5. [ ] Picture-chain v1.20+ substrate (slot 136 / bridge SHA `b9aa881`) deposit: per cascade-132 Option α step 3 — pending Branch Z step 2 (umbrella v2.2) landing.

## §6 Notes

**Note 1 — Resource type discontinuity (operator-deliberate)**: PCF-2 v1.4 was deposited with main Resource type = **Working paper** (`publication/workingpaper`). PCF-2 v1.0..v1.3 are all stored as **Preprint** (`publication-preprint`). This creates a v1.3→v1.4 metadata discontinuity along the PCF-2 chain. The change aligns with slot 137 paste-source recommendation (`zenodo_v14_metadata_field_table.md` proposed "Working paper") rather than slot 116/133 chain-consistency (which used "Preprint"). The 5 Related-identifier rows all correctly cite cross-link targets as `publication-preprint` (the target records themselves remain Preprint). The discontinuity is forward-documented here; back-edit to Preprint NOT recommended (avoids DOI metadata flux on a freshly-published record).

**Note 2 — Description body Markdown not rendered**: the description was pasted as Markdown (with `**bold**`, `*italic*`, `|table|` syntax) but Zenodo's description editor stored it with literal Markdown characters wrapped in `<p>` tags. Bold, italic, and the 13-row M1–M12 axis-coverage table all display as raw characters on the public record page. Cosmetic only; content fully preserved. HTML-converted replacement description prepared at `session-state files/pcf2_v14_description_HTML.html` (~4.2 KB); operator can apply via Zenodo Edit → Description without DOI version bump.

**Note 3 — Keywords**: stored as ONE comma-concatenated string instead of 9 separate keyword tags. Trailing comma. Suggested cleanup at operator-discretion via Zenodo Edit.

**Note 4 — ORCID**: API `creators[0]` shows `name + affiliation` but no `orcid` field. Paste-source specified ORCID `0009-0000-6192-8273`. Suggested addition at operator-discretion via Zenodo Edit.

**Note 5 — `dates` field anomaly**: stored as `{"type": "updated", "description": "minor amendment to v1.3..."}` — the description field of the dates array was populated with the dates-section description text. Cosmetic; LOW priority cleanup.

**Note 6 — Communities membership**: not visible in this JSON API response (may require authenticated /me endpoint). Operator to verify v1.3 community memberships carried over to v1.4 via the Zenodo UI sidebar.

---

**END OF DEPOSIT LOG — PCF-2 v1.4 (deposit-ID 20114315; concept 19936297; landed 2026-05-11 JST)**
