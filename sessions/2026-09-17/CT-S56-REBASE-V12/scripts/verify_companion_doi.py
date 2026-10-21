"""CT-S56 -- the companion reference, checked against Zenodo rather than assumed.

Open question 4 of REPORT.md. TWO papers in this corpus each have a "v1.3":

  this paper    concept 20719042, v1.3 = record 22731371
  the companion concept 20455089, v1.3 = record 22831933  <- what we cite

A concept DOI is not a version DOI, and neither equals the record number of the
other. The failure mode is not hypothetical: citing this paper's own v1.3 in
place of the companion's would produce a reference that resolves, looks right,
and is wrong.

So every field of the new bibitem is read from the API -- in particular the
concept DOI from the response's own `conceptdoi` field, never inferred -- and
compared against the LaTeX.

Exit 0 clean, 1 finding, 2 refusal (including when Zenodo is unreachable: an
unchecked citation must not be recorded as a checked one).
"""
import hashlib
import json
import re
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESS = HERE.parent
REV = SESS / "revision" / "vquad-periodrep-paper.tex"
OUT = SESS / "outputs" / "companion_doi.out.txt"

RECORD = "22831933"
EXPECT_VERSION_DOI = "10.5281/zenodo.22831933"
EXPECT_CONCEPT_DOI = "10.5281/zenodo.20455089"
EXPECT_VERSION = "1.3"

# This paper's own v1.3 -- must NOT appear in the companion's reference.
THIS_PAPER_V13_RECORD = "22731371"
THIS_PAPER_CONCEPT = "20719042"

L = []


def say(s=""):
    print(s)
    L.append(s)


def main():
    if not REV.exists():
        say(f"REFUSED: {REV} missing")
        return 2

    say("=" * 74)
    say("CT-S56 -- the companion reference against Zenodo")
    say("=" * 74)
    say()

    try:
        url = f"https://zenodo.org/api/records/{RECORD}"
        with urllib.request.urlopen(url, timeout=60) as fh:
            rec = json.loads(fh.read().decode("utf-8"))
    except Exception as e:  # noqa: BLE001
        say(f"REFUSED: could not query Zenodo: {type(e).__name__}: {e}")
        say("An unchecked citation is not recorded as a checked one.")
        OUT.write_text("\n".join(L) + "\n", encoding="utf-8")
        return 2

    doi = rec.get("doi")
    concept = rec.get("conceptdoi")
    version = (rec.get("metadata") or {}).get("version")
    title = (rec.get("metadata") or {}).get("title", "")

    say("[1] WHAT ZENODO SAYS")
    say(f"    record      : {rec.get('id')}")
    say(f"    version doi : {doi}")
    say(f"    concept doi : {concept}   <- read from the `conceptdoi` field")
    say(f"    version     : {version}")
    say(f"    title       : {title[:70]}...")
    say()

    findings = 0
    say("[2] THE API AGREES WITH WHAT THE BIBITEM CLAIMS")
    for got, want, what in ((doi, EXPECT_VERSION_DOI, "version DOI"),
                            (concept, EXPECT_CONCEPT_DOI, "concept DOI"),
                            (version, EXPECT_VERSION, "version")):
        ok = got == want
        findings += 0 if ok else 1
        say(f"    [{'PASS' if ok else 'FAIL'}] {what:<12} {got}")
    say()

    tex = REV.read_bytes().decode("utf-8")
    m = re.search(r"\\bibitem\{VquadV13\}(.*?)(?=\\bibitem|\\end\{thebibliography\})",
                  tex, re.S)
    if not m:
        say("REFUSED: the VquadV13 bibitem was not found in the revision")
        OUT.write_text("\n".join(L) + "\n", encoding="utf-8")
        return 2
    entry = m.group(1)

    say("[3] THE BIBITEM CARRIES BOTH DOIs, EXPLICITLY")
    for want, what in ((EXPECT_VERSION_DOI, "version DOI"),
                       (EXPECT_CONCEPT_DOI, "concept DOI")):
        ok = want in entry
        findings += 0 if ok else 1
        say(f"    [{'PASS' if ok else 'FAIL'}] {what} present in the entry")
    say()

    say("[4] IT IS NOT THIS PAPER'S OWN v1.3")
    say("    The confusable object. If either of these appears in the")
    say("    companion's entry the reference names the wrong paper.")
    for bad, what in ((THIS_PAPER_V13_RECORD, "this paper's v1.3 record"),
                      (THIS_PAPER_CONCEPT, "this paper's concept id")):
        ok = bad not in entry
        findings += 0 if ok else 1
        say(f"    [{'PASS' if ok else 'FAIL'}] {what} ({bad}) absent")
    say()

    say("[5] THE TITLE IS THE COMPANION'S, NOT THIS PAPER'S")
    key = "surface classification and resurgent Stokes data"
    ok_t = key.lower() in re.sub(r"\s+", " ", entry).lower()
    ok_api = key.lower() in title.lower()
    findings += 0 if (ok_t and ok_api) else 1
    say(f"    [{'PASS' if ok_t else 'FAIL'}] the bibitem's title ends '{key}'")
    say(f"    [{'PASS' if ok_api else 'FAIL'}] so does Zenodo's")
    say()

    say("[6] CONTROL -- the comparison must be able to fail")
    c1 = doi != "10.5281/zenodo.00000000"
    c2 = concept != doi
    for ok, txt in ((c1, "a fabricated DOI does not match the API's"),
                    (c2, "the concept DOI and the version DOI are DIFFERENT "
                         "strings -- the whole point")):
        findings += 0 if ok else 1
        say(f"    [{'PASS' if ok else 'FAIL'}] {txt}")
    say()

    say("CLEAN -- the companion reference is the companion's v1.3."
        if not findings else f"FINDINGS: {findings}")
    say("=" * 74)
    OUT.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"\n[written] {OUT}")
    print(f"[sha256]  {hashlib.sha256(OUT.read_bytes()).hexdigest()}")
    return 0 if not findings else 1


if __name__ == "__main__":
    sys.exit(main())
