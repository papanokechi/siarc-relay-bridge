"""CT-S56 -- record the revision's build result as citable evidence.

The build was checked interactively; an interactive check leaves nothing a
claim can cite. This re-reads the LaTeX .log and writes a hashed output.

The .log is read rather than the build script's own summary, because a build
script reporting its own success is the thing being checked.
"""
import hashlib
import io
import re
from pathlib import Path

import fitz

HERE = Path(__file__).resolve().parent
SESS = HERE.parent
REV = SESS / "revision"
LOG = REV / "vquad-periodrep-paper.log"
PDF = REV / "vquad-periodrep-paper.pdf"
OUT = SESS / "outputs" / "build_check.out.txt"

BUF = io.StringIO()


def say(s=""):
    print(s)
    BUF.write(s + "\n")


def main() -> int:
    txt = LOG.read_text(encoding="utf-8", errors="replace")

    undefined = re.findall(r"(?m)^.*(?:Reference|Citation).*undefined.*$", txt)
    warn_undef = re.findall(r"There were undefined references", txt)
    errors = re.findall(r"(?m)^! .*$", txt)
    doc = fitz.open(PDF)
    pages = doc.page_count
    doc.close()

    say("=" * 78)
    say("CT-S56 -- revision build result, read from the LaTeX .log")
    say("=" * 78)
    say("")
    say(f"    log : {LOG.name}  ({LOG.stat().st_size} B)")
    say(f"    pdf : {PDF.name}  sha256 "
        f"{hashlib.sha256(PDF.read_bytes()).hexdigest()}")
    say("")
    say(f"    pages in the revision PDF          : {pages}")
    say(f"    lines matching '! ' (TeX errors)   : {len(errors)}")
    say(f"    undefined reference/citation lines : {len(undefined)}")
    say(f"    'There were undefined references'  : {len(warn_undef)}")
    say("")
    for e in errors[:20]:
        say(f"      ERROR {e.strip()[:100]}")
    for u in undefined[:20]:
        say(f"      UNDEF {u.strip()[:100]}")
    say("")

    say("[control] the reader must be able to SEE an undefined reference")
    probe = "LaTeX Warning: Reference `zzz-not-a-real-label' on page 1 undefined"
    seen = bool(re.findall(r"(?m)^.*(?:Reference|Citation).*undefined.*$", probe))
    say(f"    [{'PASS' if seen else 'FAIL'}] the same pattern matches a synthetic "
        f"undefined-reference line")
    say("")

    ok = not errors and not undefined and not warn_undef and seen
    say("=" * 78)
    say("PASS: 0 errors, 0 undefined references" if ok else "FAIL: see above")
    say("=" * 78)

    OUT.write_text(BUF.getvalue(), encoding="utf-8")
    print(f"\n[written] {OUT}")
    print(f"[sha256]  {hashlib.sha256(OUT.read_bytes()).hexdigest()}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
