"""CT-S56 -- give the submitted source a home in the repository record.

Operator ruling 3. The source of the paper under review lives at
C:\\LocalWork\\vq-fix\\src\\base, OUTSIDE the repository, so every pass that
looked for "the paper" in the tree found v1.0 instead. That is the second time
in this run a document was found by LOCATION rather than by CONTENT.

This script does not just copy files. It establishes, from the bytes, that the
staged copy IS the out-of-tree original and that the original IS what LMP
holds, and only then writes a marker whose every figure it has derived. A
marker asserting "this is the submitted version" that nothing checked would be
the same defect one level up.

Exit 0 clean, 1 finding, 2 refusal.
"""
import hashlib
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESS = HERE.parent
ROOT = SESS.parents[1]

EXTERNAL = Path(r"C:\LocalWork\vq-fix\src\base")
STAGED = SESS / "refs" / "src-v1.2"
RECORD = ROOT / "submitted-source" / "MATH-D-26-00523"

# The published v1.2 PDF, as deposited. Hardcoded on purpose: a check that
# re-derives its expectation from the file it is checking cannot fail.
V12_MD5 = "792107efab6317e8ae21e2ca20f092ff"
V12_RECORD = "21412469"
CONCEPT = "20719042"

OUT = SESS / "outputs" / "home_for_s56_01.out.txt"

lines = []


def say(s=""):
    print(s)
    lines.append(s)


def md5(p):
    return hashlib.md5(p.read_bytes()).hexdigest()


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    say("=" * 74)
    say("CT-S56 -- a home for the submitted source (operator ruling 3)")
    say("=" * 74)
    say()

    if not EXTERNAL.is_dir():
        say(f"REFUSED: {EXTERNAL} does not exist.")
        return 2

    findings = 0

    # ---- [1] the staged copy must BE the external original -----------------
    say("[1] THE STAGED COPY IS THE OUT-OF-TREE ORIGINAL")
    say("    Checked file by file. If these differ, everything this session")
    say("    did was done against something other than the submitted source.")
    ext = sorted(p for p in EXTERNAL.iterdir() if p.is_file())
    for p in ext:
        q = STAGED / p.name
        if not q.exists():
            say(f"    [FAIL] {p.name}: not staged")
            findings += 1
            continue
        a, b = sha(p), sha(q)
        ok = a == b
        findings += 0 if ok else 1
        say(f"    [{'PASS' if ok else 'FAIL'}] {p.name:<32} {a[:16]}")
    say()

    # ---- [2] the PDF must be the version LMP holds -------------------------
    say("[2] THE PDF IS THE VERSION LETTERS IN MATHEMATICAL PHYSICS HOLDS")
    pdf = EXTERNAL / "vquad-periodrep-paper.pdf"
    got = md5(pdf)
    ok = got == V12_MD5
    findings += 0 if ok else 1
    say(f"    expected md5 : {V12_MD5}  (Zenodo record {V12_RECORD}, v1.2)")
    say(f"    actual   md5 : {got}")
    say(f"    [{'PASS' if ok else 'FAIL'}] the source directory's own PDF is v1.2")
    say()

    # ---- [3] control: the comparison must be able to fail -------------------
    say("[3] CONTROL -- the md5 comparison must be able to fail")
    wrong = "0" * 32
    say(f"    [{'PASS' if got != wrong else 'FAIL'}] a deliberately wrong md5 "
        "does not match")
    say()

    if findings:
        say(f"FINDINGS: {findings}. No marker written -- a marker is only")
        say("written when what it asserts has been established.")
        OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return 1

    # ---- [4] write the record ----------------------------------------------
    say("[4] WRITING THE RECORD")
    RECORD.mkdir(parents=True, exist_ok=True)
    for p in ext:
        shutil.copy2(p, RECORD / p.name)
    say(f"    copied {len(ext)} file(s) to {RECORD.relative_to(ROOT)}")

    tex = RECORD / "vquad-periodrep-paper.tex"
    marker = RECORD / "README.md"
    marker.write_text(f"""# MATH-D-26-00523 — the source of the submitted manuscript

**This is the version *Letters in Mathematical Physics* holds.**

| | |
|---|---|
| manuscript | MATH-D-26-00523 |
| version | v1.2 |
| Zenodo record | {V12_RECORD} (concept {CONCEPT}) |
| PDF md5 | `{V12_MD5}` |
| PDF sha256 | `{sha(pdf)}` |
| source sha256 | `{sha(tex)}` |
| source bytes | {tex.stat().st_size} |

## Why this directory exists

The source that produced the submitted PDF lived only at
`C:\\LocalWork\\vq-fix\\src\\base`, outside this repository. Every pass that
looked for "the paper" in the tree found **v1.0** instead, and none of them
could tell "this is not the submitted version" from "this is the paper".
CT-S56 found the submitted version by rebuilding candidates and **matching
their content** against the PDF the journal holds, not by trusting a filename
or a location.

The figures above were derived by `home_for_s56_01.py` from these bytes, and
the copy was written only after the check passed. Identify this source by its
hash, not by where it sits.

## What is NOT here

- The revision. It is a separate file in
  `sessions/2026-09-17/CT-S56-REBASE-V12/revision/`, and nothing in it has
  been submitted, uploaded or deposited.
- v1.0, v1.1 and v1.3 sources. v1.3 is published (record 22731371) and covers
  correction items 1 and 2 in different wording; it is **not** the submitted
  version.

*Uncommitted. Nothing here is to be deposited before the editor replies.*
""", encoding="utf-8")
    say(f"    wrote  {marker.relative_to(ROOT)}")
    say()
    say("CLEAN -- the submitted source now has a home in the repository")
    say("record, identified by content.")
    say("=" * 74)
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\n[written] {OUT}")
    print(f"[sha256]  {sha(OUT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
