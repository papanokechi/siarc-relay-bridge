"""selftest_readback.py -- CT-S27-CTV17-DEPOSIT-PREP

postpublish_readback.py runs once, after an irreversible publish, against a
record that does not exist yet.  So it cannot be debugged when it matters.
This builds fixtures from the HELD v1.6 record and runs the readback against
each, so the checker is exercised before it is needed.

Arm 1 is the GOOD fixture: v1.6's record with version 1.7, a new id/doi, and
the v1.7 description substituted.  It must pass.

Arms 2..n are NEGATIVE fixtures, one per failure mode the readback exists to
catch.  Each must FAIL, and must fail on the EXPECTED check -- a negative
fixture that fails for the wrong reason has not tested anything.
"""

import copy
import io
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SESSION = os.path.dirname(HERE)
SESSIONS = os.path.dirname(SESSION)
V16 = os.path.join(SESSIONS, "CT-S26-CTV17-DRAFT", "refs", "zenodo_22782807.json")
DESC = os.path.join(SESSION, "DESCRIPTION-v1.7-rev3.html")
TMP = os.path.join(SESSION, "outputs", "_fixtures")
READBACK = os.path.join(HERE, "postpublish_readback.py")

FAKE_ID = 23000001
FAKE_DOI = "10.5281/zenodo.23000001"


def good_fixture():
    with io.open(V16, encoding="utf-8") as fh:
        rec = json.load(fh)
    with io.open(DESC, encoding="utf-8") as fh:
        desc = fh.read()
    rec = copy.deepcopy(rec)
    rec["id"] = FAKE_ID
    rec["doi"] = FAKE_DOI
    rec["metadata"]["version"] = "1.7"
    rec["metadata"]["description"] = desc
    return rec


MUTATIONS = [
    ("files not imported (the step most easily missed)",
     "exactly one file is published",
     lambda r: r.update({"files": []}) or r),
    ("a second file uploaded by accident",
     "exactly one file is published",
     lambda r: r.update({"files": r["files"] + [dict(r["files"][0], key="extra.pdf")]}) or r),
    ("a DRAFT- filename published",
     "no draft marker or record id in the filename",
     lambda r: r["files"][0].update({"key": "DRAFT-channel_theory_outline.pdf"}) or r),
    ("the wrong build attached (v1.6's own defect 1)",
     "the file bytes are v1.6's, unchanged",
     lambda r: r["files"][0].update({"checksum": "md5:" + "0" * 32}) or r),
    ("version left at 1.6",
     "version is 1.7",
     lambda r: r["metadata"].update({"version": "1.6"}) or r),
    ("description truncated by the editor",
     "the description is not truncated",
     lambda r: r["metadata"].update(
         {"description": r["metadata"]["description"][:20000]}) or r),
    ("a load-bearing sentence lost in the paste",
     "the load-bearing sentences survived",
     lambda r: r["metadata"].update(
         {"description": r["metadata"]["description"].replace(
             "the v1.6 build, unchanged", "the build")}) or r),
    ("affiliation drifted (the v1 record's real defect)",
     "affiliation unchanged",
     lambda r: r["metadata"]["creators"][0].update(
         {"affiliation": "Independent researcher"}) or r),
    ("a keyword dropped",
     "keyword count is 27",
     lambda r: r["metadata"].update(
         {"keywords": r["metadata"]["keywords"][:-1]}) or r),
    ("the concept DOI overwritten with the version DOI",
     "concept DOI unchanged, read from the conceptdoi field",
     lambda r: r.update({"conceptdoi": FAKE_DOI}) or r),
    # Added 2026-09-20.  The whitespace-normalised comparison replaced an exact
    # one on the v1.7 publish; these two prove it still rejects real content
    # loss.  Neither string is load-bearing and neither is at the tail, so no
    # other check can fire on them -- each must fail on its own check.
    ("a qualification silently dropped by the editor",
     "published text matches the checked description, character for "
     "character (whitespace-normalised)",
     lambda r: r["metadata"].update(
         {"description": r["metadata"]["description"].replace(
             "necessary condition", "")}) or r),
    ("a value altered by the editor",
     "published text matches the checked description, character for "
     "character (whitespace-normalised)",
     lambda r: r["metadata"].update(
         {"description": r["metadata"]["description"].replace(
             "Katz invariant 1/2", "Katz invariant 3/2")}) or r),
]


def run(rec, name):
    os.makedirs(TMP, exist_ok=True)
    path = os.path.join(TMP, re.sub(r"[^a-z0-9]+", "_", name.lower())[:40] + ".json")
    with io.open(path, "w", encoding="utf-8") as fh:
        json.dump(rec, fh)
    p = subprocess.run([sys.executable, READBACK, "--fixture=" + path],
                       capture_output=True, text=True, encoding="utf-8")
    return p.returncode, (p.stdout or "") + (p.stderr or "")


def main():
    print("=" * 76)
    print("selftest_readback.py -- exercising the post-publish checker offline")
    print("=" * 76)
    print()

    broken = []

    print("ARM 1 -- GOOD FIXTURE (must PASS)")
    print("-" * 76)
    rc, out = run(good_fixture(), "good")
    ok = rc == 0 and "VERDICT: the published record is the packet" in out
    print("  [%s] the good fixture passes (rc=%d)" % ("PASS" if ok else "BROKEN", rc))
    if not ok:
        broken.append("good fixture rejected")
        print("\n".join("    | " + l for l in out.splitlines() if "FAIL" in l))
    print()

    print("ARM 2 -- NEGATIVE FIXTURES (each must FAIL, on its OWN check)")
    print("-" * 76)
    for name, expected, mutate in MUTATIONS:
        rec = mutate(good_fixture())
        rc, out = run(rec, name)
        # The first version of this line was r"\[FAIL\] ([^-]+?) --", which
        # stops at the first hyphen -- so it could not read the name of any
        # check containing one, e.g. "the load-bearing sentences survived".
        # The check fired; the HARNESS could not see it, and reported BROKEN.
        # A harness that cannot read its own subject is not a control.
        failed = sorted(set(re.findall(r"\[FAIL\] (.+?) -- ", out)))
        failed = [f.strip() for f in failed]
        caught = rc != 0 and any(expected in f for f in failed)
        print("  [%s] %s" % ("PASS" if caught else "BROKEN", name))
        print("         expected: %s" % expected)
        print("         fired   : %s" % (failed if failed else "NOTHING"))
        if not caught:
            broken.append(name)
    print()

    # Added 2026-09-20.  P2, the two-sided guarantee: ARM 2 alone is satisfied
    # by a check that rejects everything.  This arm holds the other side --
    # the editor's re-serialisation of inline markup, which is what actually
    # happened on publishing v1.7, must be ACCEPTED.  Stripping <em>/<strong>
    # changes no text, but it removes the spaces plain() manufactures from
    # those tags, which is precisely what made the exact comparison fail.
    print("ARM 3 -- RE-SERIALISATION (must be ACCEPTED, not rejected)")
    print("-" * 76)
    rec = good_fixture()
    before = rec["metadata"]["description"]
    after = re.sub(r"</?(?:em|strong)>", "", before)
    moved = len(re.findall(r"</?(?:em|strong)>", before))
    rec["metadata"]["description"] = after
    rc, out = run(rec, "reserialised")
    ok = rc == 0 and moved > 0
    print("  [%s] %d inline tags removed; record still accepted (rc=%d)"
          % ("PASS" if ok else "BROKEN", moved, rc))
    if not ok:
        broken.append("re-serialised fixture rejected (the check is one-sided)")
        print("\n".join("    | " + l for l in out.splitlines() if "FAIL" in l))
    print()

    print("=" * 76)
    print("negative fixtures: %d" % len(MUTATIONS))
    print("broken           : %d%s" % (len(broken),
                                       ("  -> " + "; ".join(broken)) if broken else ""))
    print()
    if broken:
        print("VERDICT: BROKEN -- the readback cannot be relied on after publishing.")
    else:
        print("VERDICT: OK -- the readback accepts the packet and rejects every")
        print("  failure mode it claims to cover, each on its own check.")
    print("=" * 76)
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
