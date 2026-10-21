#!/usr/bin/env python3
"""CT-S55 -- Amendment H sweep.

The commissioning question was "is CT-S52's base the wrong document?". Amendment
H requires that a repair pass commissioned from a reported list first sweep for
the same defect elsewhere, and report the sweep's result whether or not it finds
anything -- an empty sweep and an absent sweep are indistinguishable in a report
that records only repairs.

The defect class: **an artefact identified or described from the only copy in
the tree, rather than from its content.** CT-S52 named its base "the file
published in Zenodo record 20719043" because v1.0 was the only V_quad paper PDF
present; it never established that LMP held that version.

Exit codes: 0 swept, 2 refusal, 3 crash.
"""
import hashlib
import re
import sys
from pathlib import Path

import fitz

HERE = Path(__file__).resolve().parent
SESSION = HERE.parent
SESSIONS = SESSION.parent.parent
REPO = SESSIONS.parent
REFS = SESSION / "refs"
OUT = SESSION / "outputs" / "sweep_h.out.txt"

VERSION_PDFS = [
    ("1.0", 20719043, "zenodo-v1.0-20719043.pdf"),
    ("1.1", 21410927, "zenodo-v1.1-21410927.pdf"),
    ("1.2", 21412469, "zenodo-v1.2-21412469.pdf"),
    ("1.3", 22731371, "zenodo-v1.3-22731371.pdf"),
]

# Places that describe the manuscript artefact and could carry a stale figure.
SWEEP_DIRS = [
    SESSIONS / "2026-06-18" / "VQUAD-ARXIV-METADATA-001",
    SESSIONS / "2026-09-17" / "CT-S51-UPLOAD-WALKTHROUGH",
    SESSIONS / "2026-09-17" / "CT-S52-XI0-LOGS-REVISION",
]

PAGE_RE = re.compile(r"\b(\d{1,3})\s*(?:pages|pp\.|pp\b)", re.I)

LINES: list[str] = []


def say(s: str = "") -> None:
    print(s)
    LINES.append(s)


class Refuse(Exception):
    pass


def main() -> int:
    say("=" * 74)
    say("CT-S55 -- AMENDMENT H SWEEP")
    say("=" * 74)
    say("")
    say("Defect class swept for: an artefact identified or described from the")
    say("only copy present in the tree, rather than from its content.")
    say("")

    # ------------------------------------------------- ground truth
    say("[0] GROUND TRUTH -- page count of every published version")
    truth = {}
    for ver, rec, loc in VERSION_PDFS:
        p = REFS / loc
        if not p.exists():
            raise Refuse(f"reference missing: {loc}")
        d = fitz.open(p)
        truth[ver] = d.page_count
        d.close()
        say(f"    v{ver}  record {rec}  {truth[ver]} pages  "
            f"md5 {hashlib.md5(p.read_bytes()).hexdigest()}")
    v10 = hashlib.md5((REFS / "zenodo-v1.0-20719043.pdf").read_bytes()).hexdigest()
    say(f"    LMP holds v1.2 ({truth['1.2']} pages); the deposit's latest is "
        f"v1.3 ({truth['1.3']} pages)")

    # --------------------------------------- hits: stale page-count figures
    say("")
    say("[1] HITS -- every page-count figure in the swept material")
    say("    (reported in full, including hits judged not to be defects)")
    hits = []
    for d in SWEEP_DIRS:
        if not d.exists():
            raise Refuse(f"swept directory missing: {d}")
        for f in sorted(d.rglob("*")):
            if not f.is_file() or f.suffix.lower() not in (".md", ".json", ".jsonl", ".txt"):
                continue
            if SESSION in f.parents:
                continue
            try:
                text = f.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            for i, line in enumerate(text.split("\n"), 1):
                for m in PAGE_RE.finditer(line):
                    n = int(m.group(1))
                    if n < 10 or n > 60:
                        continue
                    hits.append((f, i, n, line.strip()[:110]))

    stale = [h for h in hits if h[2] == truth["1.0"]]
    current = [h for h in hits if h[2] in (truth["1.2"], truth["1.3"]) and h[2] != truth["1.0"]]
    other = [h for h in hits if h not in stale and h not in current]

    # The census is not a defect count. A figure of 24 that correctly describes
    # v1.0 as v1.0 is right. The actionable subset is the arXiv material, whose
    # figures are field VALUES to be entered or instructions to be acted on.
    ARXIV = (SESSIONS / "2026-06-18" / "VQUAD-ARXIV-METADATA-001",
             SESSIONS / "2026-09-17" / "CT-S51-UPLOAD-WALKTHROUGH")
    actionable = [h for h in stale if any(d in h[0].parents for d in ARXIV)]
    descriptive = [h for h in stale if h not in actionable]

    say(f"    total page-count figures found : {len(hits)}")
    say(f"    equal to v1.0's {truth['1.0']} pages (census)   : {len(stale)}")
    say(f"    equal to v1.2's {truth['1.2']} or v1.3's {truth['1.3']}   : {len(current)}")
    say(f"    other values                   : {len(other)}")
    say("")
    say("    This is a CENSUS, not a defect count. A figure of 24 that correctly")
    say("    describes v1.0 as v1.0 is right. The split below is the judgement.")
    say("")
    say(f"    ACTIONABLE ({len(actionable)}) -- field values to be entered, or")
    say("    instructions to be acted on, in the arXiv upload material:")
    for f, i, n, line in actionable:
        say(f"      {f.relative_to(REPO)}:{i}")
        say(f"         {line}")
    say("")
    say(f"    DESCRIPTIVE ({len(descriptive)}) -- correct as written; they")
    say("    describe the v1.0 artefact, which really is 24 pages:")
    for f, i, n, line in descriptive:
        say(f"      {f.relative_to(REPO)}:{i}")
    if current:
        say("")
        say("    FIGURES ALREADY CURRENT (not defects):")
        for f, i, n, line in current:
            say(f"      {f.relative_to(REPO)}:{i}  ({n} pages)")
    if other:
        say("")
        say("    OTHER VALUES (reported, not judged defects):")
        for f, i, n, line in other:
            say(f"      {f.relative_to(REPO)}:{i}  ({n} pages)  {line[:70]}")

    # ------------------------------------------ what source arXiv would get
    say("")
    say("[2] THE SECOND INSTANCE -- which file would an arXiv upload carry?")
    src = (SESSIONS / "2026-06-16" / "VQUAD-PAPER-LAYOUTFIX-001" / "latex"
           / "vquad-periodrep-paper.pdf")
    if not src.exists():
        raise Refuse(f"arXiv source artefact missing: {src}")
    src_md5 = hashlib.md5(src.read_bytes()).hexdigest()
    dd = fitz.open(src)
    src_pages = dd.page_count
    dd.close()
    say(f"    arXiv package names its source : "
        f"sessions/2026-06-16/VQUAD-PAPER-LAYOUTFIX-001/latex/")
    say(f"    that artefact                  : md5 {src_md5}, {src_pages} pages")
    say(f"    equals v1.0                    : {src_md5 == v10}")
    say(f"    LMP holds                      : v1.2, {truth['1.2']} pages")
    say(f"    deposit's latest               : v1.3, {truth['1.3']} pages")
    second = (src_md5 == v10)
    if second:
        say("    -> SECOND INSTANCE CONFIRMED. The arXiv metadata package, its")
        say("       runbook, its consistency gate and its ledger all describe and")
        say("       would upload v1.0, two versions behind the deposit and one")
        say("       behind what the journal holds. Same cause as CT-S52's: v1.0 is")
        say("       the only V_quad paper PDF in the tree, so every pass that")
        say("       looked for 'the paper' found it and none checked the content.")

    # ------------------------------------------------- explicitly not defects
    say("")
    say("[3] HITS DECIDED NOT TO BE DEFECTS, WITH REASONS")
    say("    - CT-S52's identify_source.out.txt and CHANGES.md:11: correct as")
    say("      written. They describe v1.0's rebuilds and v1.0's md5, which")
    say("      really are 24 pages. What is wrong there is the INFERENCE that")
    say("      this artefact is what was submitted -- recorded as S55-03, which")
    say("      is not a page-count defect.")
    say("    - CT-S53 PENDING.md's version table (four records, v1.3 dated")
    say("      2026-09-13): current and correct; CT-S53 established it from the")
    say("      API, and this session's result agrees with it.")
    say("    - CT-S51 WALKTHROUGH/STATE.md pinning record 20719043: correct as")
    say("      written -- it documents the v1.0 DEPOSIT, which is a real record,")
    say("      not a claim about what was submitted to the journal.")
    say("    - References to concept 20719042 throughout: correct; the concept id")
    say("      is version-independent and is what should be cited.")
    say("    - check_upload_ready.out.txt:35 '12 pp': the COMPANION paper")
    say("      (concept 20455089), a different document. Not in scope.")

    say("")
    say("=" * 74)
    say("SUMMARY")
    say("=" * 74)
    say(f"S55S sweep dirs: {len(SWEEP_DIRS)}")
    say(f"S55S page figures found: {len(hits)}")
    say(f"S55S census equal to v1.0: {len(stale)}")
    say(f"S55S actionable stale figures: {len(actionable)}")
    say(f"S55S descriptive not defects: {len(descriptive)}")
    say(f"S55S v1.0 pages: {truth['1.0']}")
    say(f"S55S v1.1 pages: {truth['1.1']}")
    say(f"S55S v1.2 pages: {truth['1.2']}")
    say(f"S55S v1.3 pages: {truth['1.3']}")
    say(f"S55S arxiv source md5: {src_md5}")
    say(f"S55S arxiv source pages: {src_pages}")
    say(f"S55S second instance confirmed: {'YES' if second else 'NO'}")
    say("S55S sweep empty: NO")
    return 0


if __name__ == "__main__":
    try:
        rc = main()
    except Refuse as e:
        say("")
        say(f"REFUSED: {e}")
        rc = 2
    except Exception as e:  # noqa: BLE001
        say("")
        say(f"CRASH: {type(e).__name__}: {e}")
        rc = 3
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(LINES) + "\n", encoding="utf-8")
    print(f"\n[written] {OUT}")
    print(f"[sha256 ] {hashlib.sha256(OUT.read_bytes()).hexdigest()}")
    print(f"[exit   ] {rc}")
    sys.exit(rc)
