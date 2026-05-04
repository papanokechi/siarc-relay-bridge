# Row mapping table — v1.17 → v1.18 (PICTURE-V18-AMENDMENT-DRAFTING)

**Source v1.17 file:** `tex/submitted/control center/picture_revised_20260504.md`
**Source SHA-256:** `5DC76D9F459D340006F23D11F165FCDB32E479AECB9222DE33979A14DA9F4255`
**Source size:** 322 666 bytes / 3 193 lines

**Working v1.18 file:** `picture_v1.18.md` (this folder)
**v1.18 SHA-256:** `4D852C978DD82275B7B5DBA4F458F10FB6C669E5E2638E7C75414E74CDBAC750`
**v1.18 size:** 349 145 bytes / 3 335 lines (Δ = +26 479 bytes / +142 lines)

## Per-delta row mapping

| # | Spec delta | v1.17 row(s) touched | v1.18 amendment locus | Edit type |
|---|------------|----------------------|------------------------|-----------|
| 1 | G24 PCF-2 v1.3 §6 Phase-2 anomaly | New v1.16 row §_change_list / §28 (NEW) | "🆕 Updates since v1.17" superblock + §28 cascade row 1 | INSERT row in superblock + table |
| 2 | G3b (i) Wasow §X.3 | L972 G-row table (top-level G3b status) preserved verbatim; status sharpening additive in superblock | "🆕 Updates since v1.17" superblock + §28 cascade row 2 | INSERT row only (top-level G-row text preserved per cumulative-amendment style) |
| 3 | G3b (ii) Adams 1928 | L972 + spec PII typo (NOT IN v1.17 — 0 occurrences) | "🆕 Updates since v1.17" superblock + §28 cascade row 3 | INSERT row only; PII typo recorded as informational-only |
| 4 | G3b (iii) Conte–Musette ch. 7 | L972 (G3b row); Costin substitute already cited at L520 / L1101 contexts | "🆕 Updates since v1.17" superblock + §28 cascade row 4 | INSERT row only |
| 5 | G12 PCF-1 v1.3 source state | L415 (Zenodo ID table) + L1767 (cheat-sheet) — both ALREADY cite `19937196` correctly | "🆕 Updates since v1.17" superblock + §28 cascade row 5 | INSERT row only (no edit to L415 / L1767 — already correct) |
| 6 | G14 endorser handle acquisition | L339 anomaly 002-B + bridge tracking | "🆕 Updates since v1.17" superblock + §28 cascade row 6 | INSERT row only |
| 7 | G17 CT v1.4 §3.5 amendment | Existing operator todo `ct-v14-sec35-reading-decision` | "🆕 Updates since v1.17" superblock + §28 cascade row 7 | INSERT row only (G17 text in v1.17 preserved) |
| 8 | G18 Birkhoff–Trjitzinsky 1933 anchor (4-source triangulation + Okamoto pin) | M6 spec slot anchors (L1880-1945 area) | "🆕 Updates since v1.17" superblock + §28 cascade row 8 | INSERT row only |
| 9 | M6 Q36 / Phase B.5 W cross-walk (literature path Case 3) | L31 v1.17 Phase B.5 surfacing + M6 spec | "🆕 Updates since v1.17" superblock + §28 cascade row 9 + methodology footnote (row 11) | INSERT row + methodology amendment |
| 10 | arxiv-pack inventory §11 update | L415-419 Zenodo ID table | "🆕 Updates since v1.17" superblock + §28 cascade row 10 | INSERT row only (table preserved) |
| 11 | Methodology footnote (NEW) | None (NEW) | "🆕 Updates since v1.17" superblock + §28 cascade row 11 | INSERT NEW |
| 12 | PII typo correction | None in v1.17 (0 occurrences of `1501457-9`) | "🆕 Updates since v1.17" superblock + §28 cascade row 12 | INSERT informational-only row (no v1.17 edit needed) |
| 13 | Version bump + Updated timestamp | L2 Revision header + L9-L12 Updated lines | L2 Revision header rewrite + INSERT new Updated line | EDIT header + INSERT timestamp |

## Rows flagged as MISSING in v1.17 (per PICTURE-V18 §A.3)

None. All 13 deltas absorb cleanly into the existing v1.17 cumulative-amendment
scaffolding (header bump + new "Updates since v1.17" superblock + new §28
Amendment Log block). G-row text in the L972-area top-level table is preserved
verbatim per the v1.16→v1.17 precedent ("No §5 G-row insert; ... absorbed as
M6 spec Phase B.5, not surfaced as a new gap"); v1.18 status sharpening is
additive in the superblock + §28 sections. v1.19 may re-surface G18 / M6 / G17
row text inline once Case 3 (M6 Phase B.5) resolves.
