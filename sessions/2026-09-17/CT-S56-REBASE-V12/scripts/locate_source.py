#!/usr/bin/env python
r"""CT-S56 Stage 1 GATE: locate the LaTeX source that rebuilds to v1.2.

Pre-registered in PREREG.md sections 3-7. Rebuilds every candidate source in a
SCRATCH COPY (never in place: earlier sessions are not modified, and a build in
the real directory would overwrite the very PDF the comparison cites) and scores
the result against the four published versions at two tiers:

  byte tier    : md5 / byte equality against the published file
  content tier : page-for-page normalised text equality

The positive control is the point of the design. If C3 does not reproduce v1.0,
then "nothing rebuilds to v1.2" is indistinguishable from "nothing rebuilds to
anything on this machine", and the script HALTS with the gate INDETERMINATE
rather than reporting an absence it cannot see (F1).

Exit codes: 0 gate passed / 1 gate failed with a valid instrument / 2 refusal
            or indeterminate instrument / 3 crash.
"""
import hashlib
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import fitz  # PyMuPDF

HERE = Path(__file__).resolve().parent
SESS = HERE.parent
REFS = SESS / "refs"
OUT = SESS / "outputs" / "locate_source.out.txt"
ROOT = SESS.parents[2]  # repository root

BUF = io.StringIO()


def say(s=""):
    print(s)
    BUF.write(s + "\n")


class Refuse(Exception):
    pass


# ----------------------------------------------------------------- candidates
CANDIDATES = [
    ("C1", "sessions/2026-06-15/VQUAD-PERIODREP-PAPER-001"),
    ("C2", "sessions/2026-06-16/VQUAD-PAPER-CORRECTIONS-001"),
    ("C3", "sessions/2026-06-16/VQUAD-PAPER-LAYOUTFIX-001"),
    ("C4", "sessions/2026-06-16/VQUAD-REPRO-BUNDLE-001/vquad-periodrep-bundle"),
    ("C5", "sessions/2026-06-16/VQUAD-REPRO-BUNDLE-002/vquad-periodrep-bundle"),
    ("C6", "sessions/2026-06-16/VQUAD-REPRO-BUNDLE-002/run-2/vquad-periodrep-bundle"),
]

# PREREG section 12a (Amendment 1): candidates outside the repository, added
# after the in-tree gate returned FAILED. Absolute paths; the decision rule,
# normalisation and thresholds are unchanged.
PF = "C:/LocalWork/project-fingerprint/sectorial/vquad_connection_coefficient"
EXT_CANDIDATES = [
    ("D1", f"{PF}/v1.1-draft/paper"),
    ("D2", f"{PF}/v1.2-draft/paper"),
    ("D3", f"{PF}/vquad-periodrep-bundle/paper"),
    ("D4", "C:/LocalWork/vq-fix/src/base"),
    ("D5", "C:/LocalWork/vq-fix/src/control"),
    ("D6", "C:/LocalWork/vq-fix/src/v_next"),
    ("D7", "C:/LocalWork/vq-fix/src/v_next_deposit"),
]

VERSIONS = [
    ("v1.0", "zenodo-v1.0-20719043.pdf", "99faea5b0f4095788e4ee932436beeda"),
    ("v1.1", "zenodo-v1.1-21410927.pdf", "7feaf94c05a1815a9e8a0ea04561f834"),
    ("v1.2", "zenodo-v1.2-21412469.pdf", "792107efab6317e8ae21e2ca20f092ff"),
    ("v1.3", "zenodo-v1.3-22731371.pdf", "943545955c2951a9592759862230e46a"),
]

# The control: which candidate must reproduce which version for the instrument
# to be considered working at all (PREREG P1 / F1).
CONTROL_CANDIDATE = "C3"
CONTROL_VERSION = "v1.0"


def md5(b: bytes) -> str:
    return hashlib.md5(b).hexdigest()


def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def norm_pages(pdf_bytes: bytes):
    """Normalised per-page text. PREREG section 4, applied identically to both sides."""
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    pages = []
    for pg in doc:
        lines = []
        for ln in pg.get_text().splitlines():
            ln = re.sub(r"\s+", " ", ln).strip()
            if ln:
                lines.append(ln)
        pages.append("\n".join(lines))
    doc.close()
    return pages


def content_score(a_pages, b_pages) -> int:
    n = min(len(a_pages), len(b_pages))
    return sum(1 for i in range(n) if a_pages[i] == b_pages[i])


def rebuilds_to(built_bytes, built_pages, ver_bytes, ver_pages):
    """PREREG section 5 decision rule. Returns (verdict, score, note)."""
    if built_bytes == ver_bytes:
        return True, len(ver_pages), "byte-identical"
    score = content_score(built_pages, ver_pages)
    if len(built_pages) == len(ver_pages) and score >= len(ver_pages) - 1:
        diff = [i + 1 for i in range(len(ver_pages)) if built_pages[i] != ver_pages[i]]
        return True, score, f"content threshold; differing pages={diff or 'none'}"
    return False, score, ""


def build_candidate(cid: str, rel: str, scratch: Path):
    """Copy to scratch, run build.py, return (pdf_bytes, pages_from_log, stdout, stored_md5)."""
    p = Path(rel)
    src = p if p.is_absolute() else (ROOT / rel)
    if not src.is_dir():
        raise Refuse(f"{cid}: candidate directory absent: {rel}")
    dst = scratch / cid
    shutil.copytree(src, dst)

    bps = sorted(dst.rglob("build.py"))
    if len(bps) != 1:
        raise Refuse(f"{cid}: expected exactly one build.py in the copy, found {len(bps)}")
    bp = bps[0]

    # Remove any pre-existing PDF from the copy, so a stale artefact can never be
    # mistaken for a fresh build product. Record its hash first (PREREG F5).
    pre = list(bp.parent.glob("*.pdf"))
    stored = md5(pre[0].read_bytes()) if pre else None
    for q in pre:
        q.unlink()

    env = dict(os.environ)
    env["SOURCE_DATE_EPOCH"] = "1718409600"
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run([sys.executable, "build.py"], cwd=str(bp.parent), env=env,
                       capture_output=True, text=True, timeout=900)
    log = (r.stdout or "") + (r.stderr or "")

    pdfs = list(bp.parent.glob("*.pdf"))
    if not pdfs:
        return None, None, log, stored
    pdf_bytes = pdfs[0].read_bytes()
    m = re.search(r"PAGES=(\d+)", log)
    pages_logged = int(m.group(1)) if m else None
    return pdf_bytes, pages_logged, log, stored


def main():
    say("=" * 78)
    say("CT-S56 STAGE 1 GATE -- locate the source that rebuilds to v1.2")
    say("=" * 78)
    say("")
    say("Pre-registered: PREREG.md sections 3-7. Decision rule: section 5.")
    say("Builds run in scratch copies; no earlier session is modified.")
    say("")

    # ---------------------------------------------------------- [0] references
    say("[0] PUBLISHED VERSIONS (re-verified against the md5s CT-S55 resolved)")
    vers = {}
    for name, fn, want in VERSIONS:
        p = REFS / fn
        if not p.exists():
            raise Refuse(f"missing reference {fn}")
        b = p.read_bytes()
        got = md5(b)
        if got != want:
            raise Refuse(f"{name}: md5 {got} != expected {want}")
        pages = norm_pages(b)
        vers[name] = (b, pages)
        say(f"    {name}  {len(b):>7} B  md5={got}  pages={len(pages)}")
    say("")

    # ------------------------------------------------- [1] observable FIRST
    say("[1] OBSERVABLE -- rebuild every candidate and score it")
    say("    (evaluated BEFORE the vacuity block, per PREREG section 8)")
    say("")

    results = {}
    ALL = CANDIDATES + EXT_CANDIDATES
    with tempfile.TemporaryDirectory(prefix="ct-s56-build-") as td:
        scratch = Path(td)
        for cid, rel in ALL:
            if cid == "D1":
                say("    " + "-" * 66)
                say("    WIDENED SET (PREREG 12a, Amendment H) -- outside the repository")
                say("    " + "-" * 66)
            say(f"    --- {cid}  {rel}")
            try:
                pdf_bytes, pages_logged, log, stored = build_candidate(cid, rel, scratch)
            except subprocess.TimeoutExpired:
                say(f"        BUILD-FAILED: timeout")
                results[cid] = {"failed": "timeout"}
                continue
            if pdf_bytes is None:
                errs = [l for l in log.splitlines() if l.startswith("!")][:3]
                say(f"        BUILD-FAILED: no PDF produced. {errs}")
                results[cid] = {"failed": "no pdf"}
                continue

            built_pages = norm_pages(pdf_bytes)
            if pages_logged is not None and pages_logged != len(built_pages):
                raise Refuse(f"{cid}: log says {pages_logged} pages, PDF has {len(built_pages)}")

            row = {"md5": md5(pdf_bytes), "bytes": len(pdf_bytes), "stored": stored,
                   "pages": len(built_pages), "scores": {}, "verdicts": {}}
            say(f"        built: {len(pdf_bytes):>7} B  md5={row['md5']}  pages={row['pages']}")
            if stored is not None:
                fresh = "same as stored" if stored == row["md5"] else f"STALE: stored was {stored}"
                say(f"        stored PDF beside the source: {fresh}")
            for name, _, _ in VERSIONS:
                vb, vp = vers[name]
                ok, score, note = rebuilds_to(pdf_bytes, built_pages, vb, vp)
                row["scores"][name] = score
                row["verdicts"][name] = ok
                flag = "  <== REBUILDS TO" if ok else ""
                extra = f"  [{note}]" if note else ""
                say(f"          vs {name}: {score}/{len(vp)} pages{extra}{flag}")
            results[cid] = row
            say("")

    # ------------------------------------------------ [2] instrument control
    say("[2] INSTRUMENT CONTROL (PREREG P1 / F1)")
    say(f"    {CONTROL_CANDIDATE} must reproduce {CONTROL_VERSION}, or every negative")
    say("    result below is uninterpretable.")
    ctl = results.get(CONTROL_CANDIDATE, {})
    if ctl.get("failed"):
        say(f"    F1 FIRED: control candidate failed to build ({ctl['failed']}).")
        say("    GATE = INDETERMINATE.")
        return 2
    ctl_bytes_ok = ctl.get("md5") == dict((v[0], v[2]) for v in VERSIONS)[CONTROL_VERSION]
    ctl_ok = ctl.get("verdicts", {}).get(CONTROL_VERSION, False)
    say(f"    byte-identical to {CONTROL_VERSION}: {ctl_bytes_ok}")
    say(f"    rebuilds-to {CONTROL_VERSION} (decision rule): {ctl_ok}")
    if not ctl_ok:
        say("    F1 FIRED: the build is not reproducible on this machine.")
        say("    GATE = INDETERMINATE. Absence of a v1.2 source is NOT established.")
        return 2
    tier = "byte" if ctl_bytes_ok else "content-only (F1b)"
    say(f"    control PASSED. Instrument valid at tier: {tier}")
    say("")

    # ------------------------------------------------------ [3] copy relation
    say("[3] COPY RELATION (PREREG F3)")
    for a, b in [("C3", "C6"), ("C1", "C4"), ("C2", "C5"), ("D2", "D4"), ("D4", "D5")]:
        ra, rb = results.get(a, {}), results.get(b, {})
        same = ra.get("md5") == rb.get("md5") and ra.get("md5") is not None
        say(f"    {a} vs {b}: same build output = {same}  ({ra.get('md5')} / {rb.get('md5')})")
        if not same:
            say(f"    F3 FIRED: {a} and {b} are not copies of each other.")
    say("")

    # -------------------------------------------------------- [3b] stale check
    say("[3b] STALE-SOURCE CHECK (PREREG F5)")
    say("     a stored PDF that its own source no longer rebuilds means the source")
    say("     was edited afterwards; such a pair is not adoptable as a base.")
    stale = []
    for cid, _ in ALL:
        r = results.get(cid, {})
        if r.get("failed") or r.get("stored") is None:
            continue
        if r["stored"] != r["md5"]:
            stale.append(cid)
            say(f"     F5 FIRED for {cid}: stored={r['stored']} built={r['md5']}")
    if not stale:
        say("     no candidate is stale: every source rebuilds to the PDF stored beside it.")
    say("")

    # ------------------------------------------------------------ [4] verdict
    say("[4] GATE VERDICT")
    in_tree = [c for c, _ in CANDIDATES if results.get(c, {}).get("verdicts", {}).get("v1.2")]
    widened = [c for c, _ in EXT_CANDIDATES if results.get(c, {}).get("verdicts", {}).get("v1.2")]
    say("    (a) IN-TREE (the question as posed):")
    if in_tree:
        say(f"        PASSED -- {in_tree}")
    else:
        say("        FAILED -- no source in the repository rebuilds to v1.2.")
        say("        The instrument control passed, so this is a real absence.")
        say("        This finding STANDS on its own and is not erased by (b).")
    say("")
    say("    (b) WIDENED (Amendment H sweep, PREREG 12a):")
    if widened:
        say(f"        PASSED -- source(s) rebuilding to v1.2: {widened}")
        for c in widened:
            rel = dict(EXT_CANDIDATES)[c]
            say(f"          {c}  {rel}")
        gate = 0
    else:
        say("        FAILED -- no source anywhere searched rebuilds to v1.2.")
        gate = 1
    say("")
    say("    OTHER VERSIONS LOCATED (what each source actually produces):")
    for cid, rel in ALL:
        r = results.get(cid, {})
        if r.get("failed"):
            continue
        hits = [n for n, _, _ in VERSIONS if r["verdicts"][n]]
        say(f"      {cid:<4} -> {hits if hits else 'no published version'}")
    say("")
    say("    scoreboard (pages matched / target pages):")
    header = "      cand  built_pages  " + "  ".join(f"{n:>9}" for n, _, _ in VERSIONS)
    say(header)
    for cid, _ in ALL:
        r = results[cid]
        if r.get("failed"):
            say(f"      {cid:<5} BUILD-FAILED ({r['failed']})")
            continue
        cells = []
        for name, _, _ in VERSIONS:
            s = r["scores"][name]
            t = len(vers[name][1])
            cells.append(f"{s:>4}/{t:<4}")
        say(f"      {cid:<5} {r['pages']:>11}  " + "  ".join(f"{c:>9}" for c in cells))
    say("")

    # ------------------------------------------------------- [5] vacuity LAST
    say("[5] VACUITY (recorded after the observable; cannot convert a fired")
    say("    falsifier into a pass -- PREREG section 8)")
    say("")
    say("    V1 -- the four versions must be pairwise distinct under this comparator:")
    v1_ok = True
    names = [n for n, _, _ in VERSIONS]
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            a, b = names[i], names[j]
            ok, score, _ = rebuilds_to(vers[a][0], vers[a][1], vers[b][0], vers[b][1])
            if ok:
                v1_ok = False
            say(f"        {a} vs {b}: {score}/{len(vers[b][1])} pages, indistinguishable={ok}")
    say(f"        V1 {'PASS' if v1_ok else 'FAIL'}")
    say("")
    say("    V2 -- page-swap perturbation of v1.2 must fall below threshold:")
    vb, vp = vers["v1.2"]
    sw = list(vp)
    sw[9], sw[10] = sw[10], sw[9]
    s2 = content_score(sw, vp)
    v2_ok = s2 < len(vp) - 1
    say(f"        swapped pages 10/11: {s2}/{len(vp)}  responds={v2_ok}")
    say("")
    say("    V3 -- positive baseline, v1.2 against itself must be a full match:")
    s3 = content_score(vp, vp)
    v3_ok = s3 == len(vp)
    say(f"        {s3}/{len(vp)}  full match={v3_ok}")
    say("        (without this, a comparator that matches nothing against anything")
    say("         looks exactly like a tree containing no v1.2 source)")
    say("")
    if not (v1_ok and v2_ok and v3_ok):
        say("    VACUITY FAILED -- verdict above is void.")
        return 2
    say("    VACUITY PASSED.")
    say("")

    say("=" * 78)
    say(f"GATE = {'PASSED' if gate == 0 else 'FAILED'}")
    say("=" * 78)
    return gate


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
    print(f"[sha256]  {sha256_file(OUT)}")
    sys.exit(rc)
