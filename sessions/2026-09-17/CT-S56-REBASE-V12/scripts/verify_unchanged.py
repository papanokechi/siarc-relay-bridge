"""CT-S56 -- prove the submitted artefacts are byte-unchanged by this session.

The operator's check list requires 'the submitted v1.2 files byte-unchanged'.
That is only evidence if the comparison is against values recorded independently
of this run, so the expected hashes are the published md5s the operator supplied
and CT-S55 confirmed, hardcoded here, not re-read from the files themselves.

A control is included: a deliberately wrong expectation must FAIL, or the
comparison proves nothing.
"""
import hashlib
import io
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESS = HERE.parent
REFS = SESS / "refs"
OUT = SESS / "outputs" / "verify_unchanged.out.txt"

BUF = io.StringIO()


def say(s=""):
    print(s)
    BUF.write(s + "\n")


PUBLISHED = {
    "zenodo-v1.0-20719043.pdf": "99faea5b0f4095788e4ee932436beeda",
    "zenodo-v1.1-21410927.pdf": "7feaf94c05a1815a9e8a0ea04561f834",
    "zenodo-v1.2-21412469.pdf": "792107efab6317e8ae21e2ca20f092ff",
    "zenodo-v1.3-22731371.pdf": "943545955c2951a9592759862230e46a",
}

V12_SRC_SHA = "2529da49e377b9ddba905d3fde65e639c676ef9f7029810b09e091e948feb790"


def md5(p: Path) -> str:
    return hashlib.md5(p.read_bytes()).hexdigest()


def main() -> int:
    say("=" * 78)
    say("CT-S56 -- submitted artefacts byte-unchanged")
    say("=" * 78)
    say("")
    say("Expected values are the published md5s, hardcoded, not re-read from")
    say("the files under test. Re-reading them would compare a file with")
    say("itself and pass unconditionally.")
    say("")

    fails = 0
    say("[1] THE FOUR PUBLISHED VERSION PDFs")
    for name, want in PUBLISHED.items():
        p = REFS / name
        if not p.exists():
            say(f"    [FAIL] {name}: missing")
            fails += 1
            continue
        got = md5(p)
        ok = got == want
        fails += (not ok)
        say(f"    [{'PASS' if ok else 'FAIL'}] {name:<28} {got}")
        if not ok:
            say(f"           expected                 {want}")
    say("")

    say("[2] THE STAGED v1.2 SOURCE")
    src = REFS / "src-v1.2" / "vquad-periodrep-paper.tex"
    if not src.exists():
        say(f"    [FAIL] {src} missing")
        fails += 1
    else:
        got = hashlib.sha256(src.read_bytes()).hexdigest()
        ok = got == V12_SRC_SHA
        fails += (not ok)
        say(f"    [{'PASS' if ok else 'FAIL'}] sha256 {got}")
        if not ok:
            say(f"           expected      {V12_SRC_SHA}")
    say("")

    say("[3] THE REVISION IS A SEPARATE FILE, NOT AN EDIT IN PLACE")
    rev = SESS / "revision" / "vquad-periodrep-paper.tex"
    if not rev.exists():
        say("    [FAIL] revision source missing")
        fails += 1
    else:
        same = rev.read_bytes() == src.read_bytes()
        say(f"    [{'PASS' if not same else 'FAIL'}] the revision differs from the "
            f"staged base (it must, or nothing was edited)")
        fails += same
        say(f"           base     {src.stat().st_size:>7} B")
        say(f"           revision {rev.stat().st_size:>7} B")
    say("")

    say("[4] CONTROL -- a wrong expectation must FAIL")
    bad = md5(REFS / "zenodo-v1.2-21412469.pdf") == "0" * 32
    say(f"    [{'PASS' if not bad else 'FAIL'}] a deliberately wrong md5 does not "
        f"match; the comparison can fail")
    fails += bad
    say("")

    say("=" * 78)
    if fails:
        say(f"FAIL: {fails} check(s) failed -- a submitted artefact has CHANGED")
    else:
        say("PASS: every submitted artefact is byte-unchanged by this session")
    say("=" * 78)
    OUT.write_text(BUF.getvalue(), encoding="utf-8")
    print(f"\n[written] {OUT}")
    print(f"[sha256]  {hashlib.sha256(OUT.read_bytes()).hexdigest()}")
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
