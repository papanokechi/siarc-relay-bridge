# D2 Zenodo Metadata Fix — LANDED 2026-05-13 07:51:28 JST

**Record:** https://zenodo.org/records/19491768
**DOI:** 10.5281/zenodo.19491768 (preserved; metadata-only edit)
**Concept DOI:** 10.5281/zenodo.19491767 (preserved)
**Modified:** 2026-05-13 07:51:28 JST (~5 min after walkthrough delivered)

## Content-fix status: ✅ COMPLETE

All defects in the original PDF-text-extracted abstract resolved:

| Defect | Pre-fix | Post-fix |
|---|---|---|
| Missing ligatures | "di ers", "unclassi ed" | "differs", "unclassified" |
| Smashed words | "andPCF", "Thekeytool", "yield1500+", etc. | All word boundaries restored |
| Math typesetting | "O(2−N/N7/2)", "kn2" | "O(2^{−N}/N^{7/2})", "kn²" |
| Subscripts | "2F1", "2F3" | "₂F₁", "₂F₃" (unicode) |
| Missing punctuation | "Q(√5)Code" | "ℚ(√5).<br><br>Code" |
| Repo coverage | only pcf-research | both pcf-research + pcf-casoratian-identities |

## Cosmetic residual: ⚠️ soft-wrap `<br>` tags

Operator pasted Option A (the wrapped paste-ready block from the walkthrough);
Zenodo's TinyMCE-class editor converted each terminal soft-wrap into a `<br>` tag.
Result: mid-sentence forced line breaks visible in rendered HTML at all viewport
widths. Cosmetic only; does not affect content correctness or endorser readability.

Examples in current live HTML:
- `respectively<br>to 1/ln(...)`
- `identity<br>&nbsp;for π/4`
- `the<br>underlying three-term recurrence`
- `the resulting series.<br>&nbsp;<br>&nbsp;As a computational application` (paragraph break as `<br><br>` instead of `</p><p>`)

## Optional polish-pass (~3 min)

Documented in chat-log for this turn: paste-ready clean HTML block using `<p>...</p>`
paragraph tags and clickable `<a href="...">` URLs, deliverable via Zenodo editor's
"Source code" view (TinyMCE `<>` icon or Tools → Source code).

Operator decision pending: accept-as-is (D2 substantively closed) OR polish-pass.

## Endorsement-readiness state

| Defect | Status |
|---|---|
| D1 (repo-side: GitHub URL + scripts) | ✅ RESOLVED 2026-05-13 morning (commits 8459b5d + 1c0b37e) |
| D2 (Zenodo metadata) | ✅ RESOLVED 2026-05-13 07:51:28 JST (content-level) |
| A-STEP1-1 (dedicated-repo README cited ExpMath) | ✅ RESOLVED 2026-05-13 morning (1c0b37e) |

**April-10 PCF paper is now endorsement-ready.**

Next: Carneiro endorsement fire (Q-208-3 γ) or DECISION 3 Tier-1 pick per
`RESUME_NEW_CLI_20260513_DAY_START_CONSOLIDATED.txt` (bridge 9074757).
