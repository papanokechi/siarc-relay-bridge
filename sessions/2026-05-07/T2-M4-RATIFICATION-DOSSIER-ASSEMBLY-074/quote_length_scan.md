# [QUOTE-LENGTH-SCAN] — Relay 074 Phase F.2 self-check

**Task ID:** `T2-M4-RATIFICATION-DOSSIER-ASSEMBLY-074`
**Phase:** F.2 (quote-length scan)
**Date:** 2026-05-07 (W20)
**Result:** `PASS 36/36` (zero violations of §6 + §7
`HALT_074_QUOTE_LENGTH` 50-word ceiling across all 5 agent-authored
deliverables)

---

## F.2.1 Ceiling rule

Per §6 NON-NEGOTIABLE DISCIPLINE: every assertion in deliverables is
either (a) a verbatim ≤ 50-word quote with file + line/page anchor +
SHA-256 substrate anchor, OR (b) a structural label, OR (c) a
meta-policy declaration.

Per §7 envelope: `HALT_074_QUOTE_LENGTH` triggers if any quote
exceeds 50 words.

## F.2.2 Block-quote enumeration (Markdown `>` blocks)

Total block-quotes detected across 5 deliverables: **36**.

| File | Blocks | Max words | Min words | Total OK |
|---|---|---|---|---|
| `m4_substrate_inventory.md` | 10 | 42 | 4 | 10/10 |
| `m4_substrate_anchor_shas.md` | 0 | — | — | — (no block-quotes; SHA tables only) |
| `m4_claim_chain.md` | 8 | 44 | 9 | 8/8 |
| `m4_residual_questions.md` | 17 | 48 | 8 | 17/17 |
| `w21_lane1_m4_dispatch_packet.md` | 1 | 40 | 40 | 1/1 |

## F.2.3 Per-block detail (line ranges + word counts)

### F.2.3.1 `m4_substrate_inventory.md`

| Line range | Words |
|---|---|
| L28-L33 | 40 |
| L54-L54 | 4 |
| L56-L59 | 35 |
| L71-L71 | 4 |
| L73-L74 | 14 |
| L87-L89 | 27 |
| L110-L113 | 42 |
| L128-L130 | 21 |
| L137-L140 | 37 |
| L151-L151 | 5 |

### F.2.3.2 `m4_claim_chain.md`

| Line range | Words |
|---|---|
| L33-L38 | 40 |
| L62-L65 | 26 |
| L92-L93 | 9 |
| L122-L125 | 37 |
| L151-L154 | 44 |
| L161-L163 | 21 |
| L184-L186 | 27 |
| L211-L215 | 33 |

### F.2.3.3 `m4_residual_questions.md`

| Line range | Words |
|---|---|
| L28-L32 | 48 |
| L45-L49 | 43 |
| L62-L65 | 45 |
| L77-L81 | 42 |
| L93-L97 | 46 |
| L117-L120 | 43 |
| L132-L135 | 27 |
| L147-L150 | 38 |
| L164-L166 | 27 |
| L188-L192 | 46 |
| L207-L210 | 36 |
| L224-L226 | 24 |
| L240-L242 | 29 |
| L257-L259 | 25 |
| L283-L287 | 33 |
| L302-L303 | 8 |
| L330-L331 | 11 |

### F.2.3.4 `w21_lane1_m4_dispatch_packet.md`

| Line range | Words |
|---|---|
| L38-L43 | 40 |

## F.2.4 Word-count methodology

PowerShell scan; per-block word count is `($text -split '\s+' |
Where-Object { $_ -ne '' }).Count`. The Markdown `>` block-quote
delimiter is stripped via `-replace '^>\s?',''` before joining.
Multi-line block-quotes are concatenated as space-delimited single
strings before counting.

The 50-word ceiling is enforced strictly: a quote with 50 words is
OK; 51 words triggers `HALT_074_QUOTE_LENGTH`.

## F.2.5 Halt-evaluation summary

| Halt code | Triggered? |
|---|---|
| `HALT_074_QUOTE_LENGTH` | NO (0 violations) |

Phase F.2 self-check **PASS**.

---

*End of `quote_length_scan.md`.*
