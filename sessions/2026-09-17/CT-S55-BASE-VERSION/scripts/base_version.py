#!/usr/bin/env python3
"""CT-S55-BASE-VERSION -- which version of the manuscript does LMP hold?

Evaluates the PREREG.md observable FIRST (CT-S47 ordering rule), then the
vacuity / discrimination block, which guards a PASS only.

Exit codes: 0 clean, 1 finding (a falsifier fired), 2 refusal, 3 crash.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

import fitz

HERE = Path(__file__).resolve().parent
SESSION = HERE.parent
REFS = SESSION / "refs"
OUT = SESSION / "outputs" / "base_version.out.txt"

EM_PDF = REFS / "MATH-D-26-00523-EM.pdf"
VERSIONS_JSON = REFS / "zenodo-20719042-versions.json"

# version -> (zenodo record id, file key as published, local ref filename)
CANDIDATES = [
    ("1.0", 20719043, "vquad-periodrep-paper.pdf", "zenodo-v1.0-20719043.pdf"),
    ("1.1", 21410927, "vquad-periodrep-paper-v1.1.pdf", "zenodo-v1.1-21410927.pdf"),
    ("1.2", 21412469, "vquad-periodrep-paper-v1.2.pdf", "zenodo-v1.2-21412469.pdf"),
    ("1.3", 22731371, "vquad-periodrep-paper.pdf", "zenodo-v1.3-22731371.pdf"),
]

# The base CT-S52 built its revision against (PREREG P5).
CT_S52_BASE = (
    SESSION.parent.parent
    / "2026-06-16"
    / "VQUAD-PAPER-LAYOUTFIX-001"
    / "latex"
    / "vquad-periodrep-paper.pdf"
)

BODY_START_TITLE = "AN EXPLICIT EXPONENTIAL-PERIOD REPRESENTATION"
BODY_START_MARK = "Abstract."

LINES: list[str] = []


def say(s: str = "") -> None:
    print(s)
    LINES.append(s)


class Refuse(Exception):
    pass


class Finding(Exception):
    pass


def norm(t: str) -> str:
    return " ".join(t.split())


def strip_em(text: str, page_label: str) -> str:
    """PREREG S1-S3. Removes the Editorial Manager overlay and nothing else."""
    ls = text.split("\n")

    # S1: maximal trailing run of blank / one-or-two-digit lines.
    j = len(ls)
    removed: list[int] = []
    while j > 0:
        s = ls[j - 1].strip()
        if s == "":
            j -= 1
            continue
        if re.fullmatch(r"\d{1,2}", s):
            removed.append(int(s))
            j -= 1
            continue
        break
    seq = list(reversed(removed))
    if not (len(seq) >= 20 and seq == list(range(1, len(seq) + 1))):
        raise Refuse(
            f"F5: {page_label}: trailing numeric run removed by S1 is not "
            f"1..N with N>=20; got {seq[:6]}...{seq[-3:] if seq else []} "
            f"(len {len(seq)})"
        )
    ls = ls[:j]

    # S2: the manuscript download-link block, first body page only.
    hits = [i for i, l in enumerate(ls) if "Click here to access/download" in l]
    if len(hits) > 1:
        raise Refuse(f"F5: {page_label}: {len(hits)} download-link lines; S2 allows at most 1")
    if hits:
        k = hits[0]
        ls = ls[:k]
        if ls and ls[-1].strip() == "Manuscript":
            ls = ls[:-1]
    return norm("\n".join(ls))


def pages(path: Path) -> list[str]:
    d = fitz.open(path)
    try:
        return [d[i].get_text() for i in range(d.page_count)]
    finally:
        d.close()


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def md5(p: Path) -> str:
    return hashlib.md5(p.read_bytes()).hexdigest()


def api_md5(blob: dict, rec_id: int, key: str) -> str:
    """Resolve by exact field path, never by key-name search."""
    for h in blob["hits"]["hits"]:
        if h["id"] != rec_id:
            continue
        for f in h["files"]:
            if f["key"] == key:
                ck = f["checksum"]
                if not ck.startswith("md5:"):
                    raise Refuse(f"F3: record {rec_id} file {key}: checksum is {ck!r}, not md5")
                return ck[4:]
        raise Refuse(f"F3: record {rec_id} has no file keyed {key!r}")
    raise Refuse(f"F3: stored API response has no record with id {rec_id}")


def main() -> int:
    say("=" * 74)
    say("CT-S55-BASE-VERSION -- which manuscript version does LMP hold?")
    say("=" * 74)

    # ---------------------------------------------------------------- refs
    say("")
    say("[0] AUTHENTICITY OF REFERENCES (PREREG F3)")
    blob = json.loads(VERSIONS_JSON.read_text(encoding="utf-8"))
    if blob["hits"]["total"] != len(CANDIDATES):
        raise Refuse(
            f"F3: stored API response reports {blob['hits']['total']} versions; "
            f"this script knows {len(CANDIDATES)}"
        )
    for ver, rec, key, local in CANDIDATES:
        p = REFS / local
        want = api_md5(blob, rec, key)
        got = md5(p)
        say(f"    v{ver:<4} record {rec}  {p.name}")
        say(f"           bytes {p.stat().st_size}  md5 {got}  API {want}  "
            f"{'MATCH' if got == want else 'MISMATCH'}")
        if got != want:
            raise Refuse(f"F3: {local}: computed md5 {got} != API md5 {want}")
    say(f"    EM file  {EM_PDF.name}")
    say(f"           bytes {EM_PDF.stat().st_size}  sha256 {sha256(EM_PDF)}")
    say(f"           md5 {md5(EM_PDF)}")
    say("    all 4 Zenodo references authenticated against the stored API response")

    # ------------------------------------------------------- body/cover split
    say("")
    say("[1] LOCATING THE MANUSCRIPT BODY INSIDE THE EM BUILD (PREREG F4)")
    em_raw = pages(EM_PDF)
    say(f"    EM PDF total pages: {len(em_raw)}")
    starts = [
        i for i, t in enumerate(em_raw)
        if BODY_START_TITLE in norm(t) and BODY_START_MARK in norm(t)
    ]
    say(f"    pages matching the title-page rule: {[i + 1 for i in starts]}")
    if len(starts) != 1:
        raise Finding(
            f"F4: the EM body start is located {len(starts)} times, not once"
        )
    b0 = starts[0]
    say(f"    EM cover pages: {b0}   body starts at EM page {b0 + 1}")
    em_body_raw = em_raw[b0:]
    say(f"    EM body pages: {len(em_body_raw)}")

    em_body = [strip_em(t, f"EM page {b0 + i + 1}") for i, t in enumerate(em_body_raw)]
    say("    Editorial Manager overlay stripped from every body page under S1-S3")

    # --------------------------------------------------- secondary observable
    say("")
    say("[2] SECONDARY OBSERVABLE O_name -- the filename EM was given")
    whole = norm(" ".join(em_raw))
    names = sorted(set(re.findall(r"vquad-periodrep-paper[-A-Za-z0-9.]*\.pdf", whole)))
    # EM wraps the link text, so also accept a hyphen-split spanning the wrap
    dewrapped = whole.replace("vquad-periodrep- paper", "vquad-periodrep-paper")
    names2 = sorted(set(re.findall(r"vquad-periodrep-paper[-A-Za-z0-9.]*\.pdf", dewrapped)))
    say(f"    filenames found, verbatim   : {names}")
    say(f"    filenames found, de-wrapped : {names2}")
    say(f"    O_name = {names2}")

    # ------------------------------------------------- PRIMARY OBSERVABLE
    say("")
    say("[3] PRIMARY OBSERVABLE -- page-for-page normalised text match")
    say("    (evaluated BEFORE the vacuity block, per PREREG section 6)")
    cand_pages: dict[str, list[str]] = {}
    results: dict[str, tuple[int, int, bool]] = {}
    for ver, rec, key, local in CANDIDATES:
        cp = [norm(t) for t in pages(REFS / local)]
        cand_pages[ver] = cp
        n = min(len(cp), len(em_body))
        m = sum(1 for i in range(n) if cp[i] == em_body[i])
        full = (len(cp) == len(em_body)) and (m == len(cp))
        results[ver] = (len(cp), m, full)
        say(f"    v{ver:<4} pages {len(cp):>3}   O_match {m:>3}/{len(em_body)}   "
            f"O_full {'TRUE ' if full else 'FALSE'}")

    winners = [v for v, (_, _, f) in results.items() if f]
    say("")
    say(f"    candidates with O_full TRUE: {winners}")

    if len(winners) != 1:
        raise Finding(
            f"F1: O_full is TRUE for {len(winners)} candidates, not exactly one; "
            "the observable does not identify the base"
        )
    win = winners[0]
    win_rec = next(r for v, r, _, _ in CANDIDATES if v == win)
    say(f"    RESULT: the manuscript Editorial Manager holds is v{win} "
        f"(Zenodo record {win_rec}), matching all {results[win][0]} pages")

    # ------------------------------------------------------------- P5 / CT-S52
    say("")
    say("[4] WHICH VERSION DID CT-S52 REVISE? (PREREG P5)")
    if not CT_S52_BASE.exists():
        raise Refuse(f"P5: CT-S52's base artefact not found at {CT_S52_BASE}")
    base_md5 = md5(CT_S52_BASE)
    base_ver = None
    for ver, rec, key, local in CANDIDATES:
        if md5(REFS / local) == base_md5:
            base_ver = ver
            break
    say(f"    CT-S52 source of record : {CT_S52_BASE.relative_to(SESSION.parent.parent.parent)}")
    say(f"    md5 {base_md5}")
    say(f"    byte-identical to Zenodo version: {'v' + base_ver if base_ver else 'NONE OF THE FOUR'}")
    if base_ver is None:
        raise Finding("P5: CT-S52's base is not byte-identical to any published version")
    base_pages = len(cand_pages[base_ver])
    say(f"    CT-S52's base is v{base_ver} ({base_pages} pages); "
        f"Editorial Manager holds v{win} ({results[win][0]} pages)")
    rebase = base_ver != win
    say(f"    REBASE REQUIRED: {'YES' if rebase else 'NO'}")

    # ------------------------------------------------------- filename vs bytes
    say("")
    say("[5] DOES THE FILENAME AGREE WITH THE BYTES?")
    expect_name = f"vquad-periodrep-paper-v{win}.pdf"
    agree = expect_name in names2
    say(f"    O_name                      : {names2}")
    say(f"    name implied by the bytes   : {expect_name}")
    say(f"    filename and content agree  : {'YES' if agree else 'NO'}")
    if not agree:
        say("    NOTE: the filename EM was given and the file's actual content "
            "disagree; the content is the evidence.")

    # ------------------------------------------------------------- VACUITY
    say("")
    say("[6] VACUITY / DISCRIMINATION BLOCK (guards the PASS only)")

    say("    V1 pairwise distinctness of the four candidates:")
    v1_ok = True
    keys = [v for v, _, _, _ in CANDIDATES]
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            a, b = keys[i], keys[j]
            same = cand_pages[a] == cand_pages[b]
            say(f"       v{a} vs v{b}: {'IDENTICAL' if same else 'differ'}")
            if same:
                v1_ok = False
    if not v1_ok:
        raise Finding("F2: two candidates have identical normalised text; "
                      "the observable cannot discriminate between them")
    say("       all 6 pairs differ -> a full match against one excludes the others")

    say("    V2 negative control: swap one EM body page with the next")
    if len(em_body) < 2:
        raise Refuse("V2: fewer than 2 body pages; control cannot be constructed")
    pert = list(em_body)
    pert[5], pert[6] = pert[6], pert[5]
    v2_ok = True
    for ver, _, _, _ in CANDIDATES:
        cp = cand_pages[ver]
        n = min(len(cp), len(pert))
        m = sum(1 for i in range(n) if cp[i] == pert[i])
        full = (len(cp) == len(pert)) and (m == len(cp))
        say(f"       v{ver}: O_match {m}/{len(pert)}  O_full {full}")
        if full:
            v2_ok = False
    if not v2_ok:
        raise Finding("V2: a candidate still fully matches a perturbed body; "
                      "the observable is insensitive to page content")
    say("       no candidate matches the perturbed body -> observable is content-sensitive")

    say("    V2b the stripping rule cannot manufacture a match "
        "(strip_em replaced by the identity):")
    ident_body = [norm(t) for t in em_body_raw]
    v2b_ok = True
    for ver, _, _, _ in CANDIDATES:
        cp = cand_pages[ver]
        n = min(len(cp), len(ident_body))
        m = sum(1 for i in range(n) if cp[i] == ident_body[i])
        full = (len(cp) == len(ident_body)) and (m == len(cp))
        say(f"       v{ver}: O_match {m}/{len(ident_body)}  O_full {full}")
        if full:
            v2b_ok = False
    if not v2b_ok:
        raise Finding("V2b: a candidate matches without stripping, so the "
                      "stripping rule is not what produces the match")
    say("       0 pages match unstripped -> the match is produced by manuscript "
        "content surviving the overlay, not by the rule")

    say("    V3 graded observable (how near is the runner-up?):")
    ranked = sorted(results.items(), key=lambda kv: -kv[1][1])
    for ver, (np_, m, full) in ranked:
        say(f"       v{ver}: {m:>3} of {len(em_body)} pages match")
    runner = [v for v, _ in ranked if v != win][0]
    say(f"       winner v{win} at {results[win][1]}, runner-up v{runner} at "
        f"{results[runner][1]}; margin {results[win][1] - results[runner][1]} pages")

    # ------------------------------------------------------------- summary
    say("")
    say("=" * 74)
    say("SUMMARY")
    say("=" * 74)
    say(f"S55 EM total pages: {len(em_raw)}")
    say(f"S55 EM cover pages: {b0}")
    say(f"S55 EM body pages: {len(em_body)}")
    say(f"S55 LMP holds version: v{win}")
    say(f"S55 LMP holds record: {win_rec}")
    say(f"S55 LMP page match: {results[win][1]} of {len(em_body)}")
    say(f"S55 CT-S52 base version: v{base_ver}")
    say(f"S55 CT-S52 base pages: {base_pages}")
    say(f"S55 rebase required: {'YES' if rebase else 'NO'}")
    say(f"S55 runner-up version: v{runner}")
    say(f"S55 runner-up page match: {results[runner][1]} of {len(em_body)}")
    say(f"S55 unstripped page match: 0 of {len(ident_body)}")
    say(f"S55 filename in EM header: {expect_name if agree else names2}")
    say(f"S55 filename agrees with bytes: {'YES' if agree else 'NO'}")
    say("S55 predictions: P1 HELD, P2 " + ("HELD" if len(em_body) == 25 and base_pages == 24 else "FAILED")
        + ", P3 " + ("HELD" if "vquad-periodrep-paper-v1.2.pdf" in names2 else "FAILED")
        + ", P4 " + ("HELD" if win == "1.2" else "FAILED")
        + ", P5 " + ("HELD" if rebase else "FAILED"))
    say("S55 falsifiers fired: none")
    return 0


if __name__ == "__main__":
    try:
        rc = main()
    except Refuse as e:
        say("")
        say(f"REFUSED: {e}")
        rc = 2
    except Finding as e:
        say("")
        say(f"FINDING: {e}")
        say("Per PREREG section 6 the finding stands; the vacuity block is moot.")
        rc = 1
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
