"""Extract the deposited description from a fetched Zenodo record JSON.

Writes a plain-text rendering next to the JSON and echoes the byte counts so the
extraction can be read back rather than trusted.
"""
import html
import json
import re
import sys
from pathlib import Path

REFS = Path(__file__).resolve().parent.parent / "refs"


def to_text(h: str) -> str:
    t = re.sub(r"(?i)<br\s*/?>", "\n", h)
    t = re.sub(r"(?i)</p\s*>", "\n\n", t)
    t = re.sub(r"(?i)</li\s*>", "\n", t)
    t = re.sub(r"(?i)<li\s*>", "  - ", t)
    t = re.sub(r"(?i)</(h\d|div|ul|ol|table|tr)\s*>", "\n", t)
    t = re.sub(r"(?i)</td\s*>|</th\s*>", " | ", t)
    t = re.sub(r"<[^>]+>", "", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t]+\n", "\n", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip() + "\n"


def main(names):
    for name in names:
        p = REFS / name
        rec = json.loads(p.read_text(encoding="utf-8"))
        md = rec["metadata"]
        desc = md["description"]
        assert isinstance(desc, str) and desc, "description missing or not a string"
        out = p.with_suffix(".description.txt")
        txt = to_text(desc)
        out.write_text(txt, encoding="utf-8", newline="\n")
        back = out.read_text(encoding="utf-8")
        assert back == txt, "read-back mismatch"
        print(f"{p.name}: version {md.get('version')!r}  html {len(desc)} B  "
              f"text {len(txt)} B -> {out.name}")


if __name__ == "__main__":
    main(sys.argv[1:])
