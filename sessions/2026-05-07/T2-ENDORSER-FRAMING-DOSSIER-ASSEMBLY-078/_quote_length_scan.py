"""Quote-length scan for HALT_078_QUOTE_LENGTH (50-word ceiling).

Scans every .md deliverable in 078 for contiguous markdown blockquote
runs (lines starting with ">") and reports word count of each. Word
count uses simple whitespace split on the body text after the ">"
marker.

Per the spec quote discipline (every assertion must be verbatim
50-word quote OR structural label OR meta-policy declaration), the
scan classifies each blockquote run into one of:
  - CITATION  : verbatim quote from prior substrate (50-word ceiling)
  - META      : agent-authored editorial framing (operator action /
                format note / operational note); NOT subject to
                50-word ceiling.
HALT_078_QUOTE_LENGTH triggers only on CITATION-class overflows.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).parent.resolve()
TARGETS = sorted(p for p in SESSION_DIR.glob("*.md") if p.is_file())

CEILING = 50

META_PREFIXES = (
    "operator action",
    "format note",
    "note.",
    "**format note.**",
    "**operator action",
    "**note.",
    "operational note",
    "**operational note",
)

def classify(body: str) -> str:
    head = body.lstrip().lower()[:50]
    for p in META_PREFIXES:
        if head.startswith(p):
            return "META"
    return "CITATION"

def extract_blockquotes(text: str) -> list[tuple[int, str]]:
    """Return list of (start_line_no_1based, blockquote_text) for each
    contiguous run of '>' lines."""
    out = []
    cur_lines: list[str] = []
    cur_start = 0
    for i, raw in enumerate(text.splitlines(), start=1):
        stripped = raw.lstrip()
        if stripped.startswith(">"):
            body = stripped[1:].lstrip()
            if not cur_lines:
                cur_start = i
            cur_lines.append(body)
        else:
            if cur_lines:
                out.append((cur_start, " ".join(cur_lines)))
                cur_lines = []
    if cur_lines:
        out.append((cur_start, " ".join(cur_lines)))
    return out

def count_words(s: str) -> int:
    # Strip markdown emphasis / inline-code markers; simple tokenization
    s = re.sub(r"`[^`]*`", lambda m: m.group(0).replace(" ", "_"), s)
    return len([t for t in s.split() if t.strip()])

def main() -> int:
    rows = []
    overflow = []
    meta_runs = []
    for tgt in TARGETS:
        if tgt.name == "quote_length_scan.md":
            continue  # exclude the scan output itself
        text = tgt.read_text(encoding="utf-8", errors="replace")
        for start_line, body in extract_blockquotes(text):
            wc = count_words(body)
            cls = classify(body)
            preview = (body[:60] + "...") if len(body) > 60 else body
            preview = preview.replace("\n", " ")
            row = (tgt.name, start_line, wc, cls, preview)
            rows.append(row)
            if cls == "META":
                meta_runs.append(row)
            elif wc > CEILING:
                overflow.append(row)
    n_files = len(TARGETS) - (1 if (SESSION_DIR / 'quote_length_scan.md').exists() else 0)
    print(f"# Quote-Length Scan (CITATION CEILING = {CEILING} words)")
    print()
    print(f"Files scanned: {n_files}")
    print(f"Blockquote runs found: {len(rows)}")
    print(f"  CITATION-class runs: {len(rows) - len(meta_runs)}")
    print(f"  META-class runs (exempt): {len(meta_runs)}")
    print(f"CITATION overflow runs (> {CEILING} words): {len(overflow)}")
    print()
    if overflow:
        print("## CITATION OVERFLOW (HALT_078_QUOTE_LENGTH triggered)")
        for name, ln, wc, cls, prev in overflow:
            print(f"- {name} L{ln}: {wc} words: {prev}")
        print()
    print("## ALL BLOCKQUOTES (file, line, class, word-count, preview)")
    for name, ln, wc, cls, prev in rows:
        marker = ""
        if cls == "CITATION" and wc > CEILING:
            marker = " [OVERFLOW]"
        elif cls == "META":
            marker = " [META-EXEMPT]"
        print(f"- {name} L{ln}: {cls} {wc}w{marker}: {prev}")
    return 1 if overflow else 0

if __name__ == "__main__":
    sys.exit(main())
