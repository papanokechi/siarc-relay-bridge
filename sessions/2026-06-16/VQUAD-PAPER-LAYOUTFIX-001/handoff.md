# handoff.md — VQUAD-PAPER-LAYOUTFIX-001

## Outcome
Systematic right-margin overflow **fixed**. Root cause was a **MIX** — unbreakable
monospace `\texttt{…\_…}` script names + several wide display equations / one wide
table (paper sizes were already consistent letterpaper; **not** a geometry mismatch).
Fixed globally (`\emergencystretch=3em` + breakable `\_`) and with local
display/table reflow. **20 → 0 overfull hboxes.** Rebuilt byte-reproducibly; proven
content-unchanged (reflow-only). **HALT GATE CLEARED.**

## New pins (every downstream must switch to these)
| | OLD (retire) | NEW |
|---|---|---|
| PDF SHA-256 | `4ca12a35…82fe` | **`33f339edd17c5405bfd24a85ba1a5df65aeeb836e25fb525d778599aa7ba3eea`** |
| PDF MD5 | `028a1a5d…6a38` | **`99faea5b0f4095788e4ee932436beeda`** |
| bytes / pages | 714771 / 24 | **773171 / 24** |

## Verification summary
- **Overfull:** 20 → **0** (`vquad-periodrep-paper.log` grep = 0 matches).
- **Byte-reproducible:** pristine temp-dir rebuild → identical SHA `33f339ed…`.
- **Content-diff = REFLOW-ONLY:** whitespace-stripped character-multiset diff =
  **−2 ASCII hyphens, 0 other characters** (line-end hyphenation only). No digit,
  symbol, word, or equation changed.
- **Wrong-venue (Gate 2.2):** PASS (Compositio/AAECC/ETNA/… absent).
- **p4 factor:** `ξ(ξ+2/√3)` is correct — **not** a typo.
- **Page count:** 24 (unchanged).

## Cascade (operator) — see `cascade-plan.md`
1. **BUNDLE-002 re-run:** swap new PDF `33f339ed…` into `paper/`, update
   `paper/build.py` TARGET_SHA + header (773171 B), re-run `verify_bundle.py`
   (13/13 still PASS — scripts/data unchanged), re-zip → **new bundle-zip SHA**
   (supersedes `8752d7c7…`).
2. **READY-001 run-3:** stage2-pdf-pin → `33f339ed…`/`99faea5b…`/773171;
   stage7-runner-pins `PDF_SHA256_PIN` → `33f339ed…`. Metadata anchor `4a75234f…`:
   re-pin **only if** `zenodo_metadata.md` embeds the PDF hash (grep for `4ca12a35`;
   abstract/affiliation/keywords/MSC are unchanged → if the hash isn't in the file,
   the anchor is unaffected).
3. **ZENODO-DEPOSIT-001:** update `MANUAL-UPLOAD.md` PDF pins to `33f339ed…`/
   `99faea5b…` before the manual web-UI upload.

## HELD — standing meta-rule
This slot is **git add-staged only**. **No commit, no push.** HEAD is the operator's
to advance. Parents (CORRECTIONS-001 `d4fc87a`, BUNDLE-002 `a33ff59`, READY-001 run-2
`2a7f969`) and `EBR3-REVISION-001` are untouched.

**Operator commit message (records the layout fix):**
```
VQUAD-PAPER-LAYOUTFIX-001 — fixed systematic right-margin overflow (A.3/A.5/§5.2 + others);
root cause MIX (breakable \_ + \emergencystretch global, local display/table reflow);
rebuilt byte-repro, 20->0 overfull; text diff reflow-only (multiset -2 hyphen / 0 other);
new SHA 33f339ed…; cascade re-pin required

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>
```

## Slot artifacts
`preamble-audit.md`, `overfull-inventory.md`, `layout-fixes-applied.md`,
`build-result.md`, `cascade-plan.md`, `ledger.json`, `claims.jsonl`, this `handoff.md`;
working evidence `_ORIGINAL_build.log`, `_textdiff_report.txt`, `_multiset_report.txt`,
`_wrongvenue_report.txt`; the fixed `latex/` + `sections/`; baseline
`OLD-vquad-periodrep-paper-4ca12a35.pdf`; the new
`latex/vquad-periodrep-paper.pdf` (`33f339ed…`).
