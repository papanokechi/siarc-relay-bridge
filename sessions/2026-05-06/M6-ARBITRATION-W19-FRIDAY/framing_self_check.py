"""
HALT_047_VERDICT_INCLUDES_FRAMING self-check (relay 047 STEP 8).

Scans m6_verdict.md for the framing word-list outside code-fenced
blocks. The §"Spec-rollback or spec-amendment recommendation" section
is exempt for "should" only (per relay-047 §STEP 8 EXCEPTION clause).

Framing word-list (case-insensitive, word-boundary):
  should, recommend, propose, argue, suggest, we believe, our view, ought

Detection of code-fenced block: lines between matched ``` fences
(both opening and closing on their own line) are excluded.

Exit code 0 => PASS.  Non-zero => HALT_047_VERDICT_INCLUDES_FRAMING.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

VERDICT = Path(__file__).parent / "m6_verdict.md"
SELFCHECK_OUT = Path(__file__).parent / "framing_self_check.json"

# Boundary-anchored regex for each framing string. \b works for "should",
# "recommend", "propose", "argue", "suggest", "ought". For multi-word
# phrases ("we believe", "our view"), use lookaround on whitespace.
FRAMING_PATTERNS = [
    ("should", re.compile(r"\bshould\b", re.IGNORECASE)),
    ("recommend", re.compile(r"\brecommend(?:s|ed|ing|ation|ations)?\b", re.IGNORECASE)),
    ("propose", re.compile(r"\bpropose(?:s|d|ing)?\b", re.IGNORECASE)),
    ("argue", re.compile(r"\bargue(?:s|d|ing|ment|ments)?\b", re.IGNORECASE)),
    ("suggest", re.compile(r"\bsuggest(?:s|ed|ing|ion|ions)?\b", re.IGNORECASE)),
    ("we believe", re.compile(r"\bwe\s+believe\b", re.IGNORECASE)),
    ("our view", re.compile(r"\bour\s+view\b", re.IGNORECASE)),
    ("ought", re.compile(r"\bought\b", re.IGNORECASE)),
]

EXEMPT_HEADING_PATTERN = re.compile(
    r"^##\s*Spec-rollback or spec-amendment recommendation\s*$", re.IGNORECASE
)
NEXT_HEADING_PATTERN = re.compile(r"^##\s+", re.MULTILINE)


def find_section_ranges(text: str) -> list[tuple[str, int, int]]:
    """Return list of (heading, start_line, end_line) for each ## section."""
    lines = text.split("\n")
    sections: list[tuple[str, int, int]] = []
    cur_heading: str | None = None
    cur_start: int | None = None
    for idx, line in enumerate(lines):
        if line.lstrip().startswith("## "):
            if cur_heading is not None and cur_start is not None:
                sections.append((cur_heading, cur_start, idx - 1))
            cur_heading = line.strip()
            cur_start = idx
    if cur_heading is not None and cur_start is not None:
        sections.append((cur_heading, cur_start, len(lines) - 1))
    return sections


def in_code_fence_lines(text: str) -> set[int]:
    """0-indexed line numbers inside ``` fences."""
    inside: set[int] = set()
    fence_open = False
    for idx, line in enumerate(text.split("\n")):
        stripped = line.strip()
        if stripped.startswith("```"):
            fence_open = not fence_open
            inside.add(idx)  # the fence line itself counts as inside
            continue
        if fence_open:
            inside.add(idx)
    return inside


def main() -> int:
    text = VERDICT.read_text(encoding="utf-8")
    lines = text.split("\n")
    code_lines = in_code_fence_lines(text)
    sections = find_section_ranges(text)
    exempt_section_lines: set[int] = set()
    exempt_heading_lines: set[int] = set()
    for heading, start, end in sections:
        if EXEMPT_HEADING_PATTERN.match(heading):
            exempt_heading_lines.add(start)
            for ln in range(start, end + 1):
                exempt_section_lines.add(ln)

    hits: list[dict] = []
    for idx, line in enumerate(lines):
        if idx in code_lines:
            continue
        for label, pat in FRAMING_PATTERNS:
            for m in pat.finditer(line):
                in_exempt = idx in exempt_section_lines
                is_exempt_heading = idx in exempt_heading_lines
                # Per relay-047 §STEP 8: 'should' is permitted inside
                # the exempt section. The exempt section heading itself
                # is a spec-mandated structural label (per relay-047
                # §STEP 5 verdict template) and is not framing OF the
                # verdict; treat the heading line as exempt for ALL
                # word-list entries.
                allowed = (
                    (label == "should" and in_exempt)
                    or is_exempt_heading
                )
                hits.append(
                    {
                        "line": idx + 1,
                        "col": m.start() + 1,
                        "match": m.group(0),
                        "label": label,
                        "in_exempt_section": in_exempt,
                        "is_exempt_heading": is_exempt_heading,
                        "allowed_by_exception": allowed,
                        "line_text": line.rstrip(),
                    }
                )

    forbidden_hits = [h for h in hits if not h["allowed_by_exception"]]
    result = {
        "verdict_path": str(VERDICT.relative_to(VERDICT.parents[3])).replace(
            "\\", "/"
        ),
        "framing_word_list": [label for label, _ in FRAMING_PATTERNS],
        "exception": "'should' only inside the '## Spec-rollback or spec-amendment recommendation' section",
        "all_hits_count": len(hits),
        "forbidden_hits_count": len(forbidden_hits),
        "all_hits": hits,
        "forbidden_hits": forbidden_hits,
        "outcome": "PASS" if len(forbidden_hits) == 0 else "HALT_047_VERDICT_INCLUDES_FRAMING",
    }
    SELFCHECK_OUT.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(f"all hits: {len(hits)}")
    print(f"forbidden hits: {len(forbidden_hits)}")
    print(f"outcome: {result['outcome']}")
    if forbidden_hits:
        for h in forbidden_hits:
            print(
                f"  L{h['line']} col {h['col']} [{h['label']}]: "
                f"{h['match']!r} -- {h['line_text']!r}"
            )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
