#!/usr/bin/env python
r"""CT-S56 Stage 2: source-level diffs v1.0 -> v1.2 and v1.2 -> v1.3, and the
question the first diff exists to answer -- which of CT-S52's replacements still
match the v1.2 source exactly once.

CT-S52's replacement list is IMPORTED from its own script rather than
transcribed, so the strings tested here cannot drift from the strings that
session would apply. (A transcribed figure is the defect class CT-S55 found in
its own control harness.)

Exit codes: 0 clean / 1 finding / 2 refusal / 3 crash.
"""
import difflib
import hashlib
import importlib.util
import io
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESS = HERE.parent
REFS = SESS / "refs"
OUTD = SESS / "outputs"
OUT = OUTD / "version_diff.out.txt"
ROOT = SESS.parents[2]

S52 = ROOT / "sessions/2026-09-17/CT-S52-XI0-LOGS-REVISION/scripts/apply_revision.py"

BUF = io.StringIO()


def say(s=""):
    print(s)
    BUF.write(s + "\n")


class Refuse(Exception):
    pass


def load(ver: str) -> str:
    p = REFS / f"src-{ver}" / "vquad-periodrep-paper.tex"
    if not p.exists():
        raise Refuse(f"missing staged source for {ver}: {p}")
    return p.read_bytes().decode("utf-8").replace("\r\n", "\n")


def sha(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def import_s52_reps():
    """Import CT-S52's (item, tag, old, new) list from its own module."""
    if not S52.exists():
        raise Refuse(f"CT-S52 apply_revision.py not found at {S52}")
    spec = importlib.util.spec_from_file_location("s52_apply", S52)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["s52_apply"] = mod
    spec.loader.exec_module(mod)
    R = getattr(mod, "R", None)
    if not R:
        raise Refuse("CT-S52 module exposed no replacement list R")
    return [(i, t, o.replace("\r\n", "\n"), n.replace("\r\n", "\n")) for i, t, o, n in R]


def write_diff(a: str, b: str, na: str, nb: str, path: Path) -> dict:
    al, bl = a.splitlines(keepends=True), b.splitlines(keepends=True)
    ud = list(difflib.unified_diff(al, bl, fromfile=na, tofile=nb, n=3))
    path.write_text("".join(ud), encoding="utf-8")
    added = sum(1 for l in ud if l.startswith("+") and not l.startswith("+++"))
    removed = sum(1 for l in ud if l.startswith("-") and not l.startswith("---"))
    hunks = sum(1 for l in ud if l.startswith("@@"))
    return {"added": added, "removed": removed, "hunks": hunks,
            "lines": len(ud), "path": path}


def section_titles(t: str):
    return re.findall(r"\\(?:sub)*section\*?\{([^}]*)\}", t)


def main():
    say("=" * 78)
    say("CT-S56 STAGE 2 -- source-level version diffs")
    say("=" * 78)
    say("")

    v10, v11, v12, v13 = (load("v1.0"), load("v1.1"), load("v1.2"), load("v1.3"))
    for nm, t in [("v1.0", v10), ("v1.1", v11), ("v1.2", v12), ("v1.3", v13)]:
        say(f"    {nm}: {len(t):>6} chars  {t.count(chr(10))+1:>5} lines  sha256={sha(t)[:16]}")
    say("")

    OUTD.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------- [1] diffs
    say("[1] DIFFS")
    d1 = write_diff(v10, v12, "v1.0", "v1.2", OUTD / "diff-v1.0-to-v1.2.patch")
    d2 = write_diff(v12, v13, "v1.2", "v1.3", OUTD / "diff-v1.2-to-v1.3.patch")
    d0 = write_diff(v10, v11, "v1.0", "v1.1", OUTD / "diff-v1.0-to-v1.1.patch")
    for nm, d in [("v1.0 -> v1.1", d0), ("v1.0 -> v1.2", d1), ("v1.2 -> v1.3", d2)]:
        say(f"    {nm}: {d['hunks']:>3} hunks, +{d['added']} / -{d['removed']} lines"
            f"  -> {d['path'].name}")
    say("")

    say("    section headings present in each version (count):")
    for nm, t in [("v1.0", v10), ("v1.2", v12), ("v1.3", v13)]:
        say(f"      {nm}: {len(section_titles(t))}")
    s12 = set(section_titles(v12))
    s10 = set(section_titles(v10))
    s13 = set(section_titles(v13))
    say(f"      headings in v1.2 not in v1.0: {sorted(s12 - s10)}")
    say(f"      headings in v1.0 not in v1.2: {sorted(s10 - s12)}")
    say(f"      headings in v1.3 not in v1.2: {sorted(s13 - s12)}")
    say(f"      headings in v1.2 not in v1.3: {sorted(s12 - s13)}")
    say("")

    # ------------------------------------- [2] do CT-S52's edits still apply?
    say("[2] DO CT-S52's REPLACEMENTS STILL APPLY TO v1.2?")
    say("    (the list is imported from CT-S52's own apply_revision.py, not")
    say("     transcribed, so it cannot drift from what that session applies)")
    say("")
    reps = import_s52_reps()
    say(f"    CT-S52 defines {len(reps)} replacements.")
    say("")
    ok, broken, odd = [], [], []
    for item, tag, old, new in reps:
        n10 = v10.count(old)
        n12 = v12.count(old)
        n13 = v13.count(old)
        status = "APPLIES" if n12 == 1 else ("BROKEN" if n10 == 1 else "ODD")
        if status == "APPLIES":
            ok.append((item, tag))
        elif status == "BROKEN":
            broken.append((item, tag, n10, n12, old, new))
        else:
            odd.append((item, tag, n10, n12))
        say(f"    item {item:<2} [{status:<7}] v1.0={n10} v1.2={n12} v1.3={n13}  {tag[:58]}")
    say("")
    say(f"    APPLIES to v1.2 unchanged : {len(ok)}")
    say(f"    BROKEN by v1.0->v1.2      : {len(broken)}")
    say(f"    ODD (not found in v1.0)   : {len(odd)}")
    say("")

    if broken:
        say("    BROKEN replacements -- the text they target changed between v1.0")
        say("    and v1.2, so they cannot be applied as written. For each, the")
        say("    v1.2 wording that replaced it is located below by anchoring on")
        say("    the longest stable fragment of the old string.")
        say("")
        for item, tag, n10, n12, old, new in broken:
            say(f"      --- item {item}: {tag}")
            frag = None
            for line in sorted(old.split("\n"), key=len, reverse=True):
                cand = line.strip()
                if len(cand) >= 25 and v12.count(cand) == 1:
                    frag = cand
                    break
            if frag is None:
                say("          no unique anchor fragment found in v1.2;")
                say("          this edit needs to be re-authored against v1.2 by hand.")
                continue
            i = v12.index(frag)
            lo = v12.rfind("\n\n", 0, i)
            hi = v12.find("\n\n", i)
            ctx = v12[max(lo, 0):hi if hi > 0 else len(v12)].strip()
            say(f"          anchor (unique in v1.2): {frag[:70]!r}")
            say("          v1.2 paragraph containing it:")
            for l in ctx.split("\n")[:14]:
                say(f"            | {l}")
            say("")

    # ------------------------------------------ [3] what v1.3 already changed
    say("[3] WHAT v1.3 ALREADY CHANGED RELATIVE TO v1.2")
    say("    (reusable text; the revision's base stays v1.2)")
    say("")
    al, bl = v12.splitlines(), v13.splitlines()
    sm = difflib.SequenceMatcher(None, al, bl, autojunk=False)
    nblocks = 0
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        nblocks += 1
        say(f"    [{tag}] v1.2 lines {i1+1}-{i2}  ->  v1.3 lines {j1+1}-{j2}")
        for l in bl[j1:j2][:6]:
            if l.strip():
                say(f"        + {l[:100]}")
        if j2 - j1 > 6:
            say(f"        + ... ({j2-j1-6} more lines)")
    say("")
    say(f"    {nblocks} changed blocks v1.2 -> v1.3")
    say("")

    say("=" * 78)
    rc = 1 if broken else 0
    say(f"STAGE 2 {'FINDING: some CT-S52 edits do not apply to v1.2' if rc else 'CLEAN'}")
    say("=" * 78)
    return rc


if __name__ == "__main__":
    try:
        rc = main()
    except Refuse as e:
        say("")
        say(f"REFUSED: {e}")
        rc = 2
    except Exception:
        import traceback
        say("")
        say("CRASH:")
        say(traceback.format_exc())
        rc = 3
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(BUF.getvalue(), encoding="utf-8")
    print(f"\n[written] {OUT}")
    print(f"[sha256]  {hashlib.sha256(OUT.read_bytes()).hexdigest()}")
    sys.exit(rc)
