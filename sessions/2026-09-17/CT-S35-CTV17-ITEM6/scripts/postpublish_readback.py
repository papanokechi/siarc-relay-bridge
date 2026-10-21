"""postpublish_readback.py -- CT-S35-CTV17-ITEM6

READ-ONLY.  No token.  Performs one HTTP GET against the public Zenodo API and
writes nothing anywhere except its own stdout.  It cannot modify a record.

    python scripts\\postpublish_readback.py <record_id>

Run this AFTER publishing.  It answers one question -- "is the published record
the packet that was checked?" -- against the record itself, not against this
repository's belief about it.

On the description comparison.  If the browser's rich-text editor was used, the
stored HTML is a RE-SERIALISATION of DESCRIPTION-v1.7-rev3.html and will not be
byte-identical.  So the comparison is made on RENDERED TEXT with whitespace
collapsed: tags stripped, entities resolved, runs of whitespace flattened.  That
is a deliberate loosening, and it is bounded -- the length check and the
truncation check below still fire, and a missing paragraph still fails.
"""

import hashlib
import html
import io
import json
import os
import re
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
SESSION = os.path.dirname(HERE)
SESSIONS = os.path.dirname(SESSION)
DRAFT = os.path.join(SESSIONS, "CT-S26-CTV17-DRAFT")
DESC = os.path.join(SESSION, "DESCRIPTION-v1.7-rev3.html")
V16 = os.path.join(DRAFT, "refs", "zenodo_22782807.json")

EXPECT_CONCEPT_DOI = "10.5281/zenodo.19941678"
EXPECT_FILE_KEY = "channel_theory_outline.pdf"
EXPECT_FILE_MD5 = "aa56a94a9354b5533b04c89461950eb1"
EXPECT_FILE_BYTES = 609300
EXPECT_KEYWORDS = 27

# --- guard: the description compared against the live record must be the one
# the gate passed.  This script was copied forward from CT-S27 still pointing at
# DESCRIPTION-v1.7-rev2.html; run from that session it would have compared the
# published record against the revision WITHOUT the sixth item and reported a
# mismatch on prose that was added deliberately.  Comparing the wrong artefact
# is worse than not comparing, because the answer is believed.  So resolve the
# expected digest from the gate run's own output rather than from a constant
# typed here, and abort before any network call if they disagree.
GATE_OUT = os.path.join(SESSION, "outputs", "preflight_deposit_rev2_s35.out.txt")


def _guard_description_is_gate_verified():
    if not os.path.exists(DESC):
        sys.exit("ABORT: %s does not exist; readback has nothing to compare."
                 % os.path.basename(DESC))
    if not os.path.exists(GATE_OUT):
        sys.exit("ABORT: %s not found; run preflight_deposit_rev2.py first."
                 % os.path.basename(GATE_OUT))
    with io.open(GATE_OUT, encoding="utf-8", errors="replace") as fh:
        gate_txt = fh.read()
    # reader integrity: assert a known-present feature before trusting an absence
    if "GATE:" not in gate_txt:
        sys.exit("ABORT: gate output unreadable or truncated; not trusting it.")
    m = re.search(r"(?m)^sha256\s*:\s*([0-9a-f]{64})", gate_txt)
    if not m:
        sys.exit("ABORT: no sha256 recorded in the gate output.")
    want = m.group(1)
    got = hashlib.sha256(io.open(DESC, "rb").read()).hexdigest()
    if got != want:
        sys.exit("ABORT: %s is not the revision the gate verified.\n"
                 "  on disk : %s\n  gate    : %s" %
                 (os.path.basename(DESC), got, want))
    print("  description under comparison: %s  sha256 %s (gate-verified)"
          % (os.path.basename(DESC), got))


failures = []


def plain(t):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t))).strip()


def squeeze(t):
    """plain() with every whitespace run removed.

    Correction, 2026-09-20.  plain() substitutes a SPACE for each tag, so an
    inline tag between two non-space characters manufactures a space that is
    not in the text.  Zenodo's editor re-serialises inline markup on save, so
    the two sides disagree by exactly those manufactured spaces -- 10 of them
    on the v1.7 publish, every one adjacent to punctuation or inside S_{zeta}.
    Comparing on plain() therefore fails on a record that is character-for-
    character correct, which is the check's own stated expectation
    ("re-serialisation is expected") contradicting its own test.

    Squeezing whitespace removes the artefact and removes NOTHING else: any
    missing paragraph, lost sentence, truncation or altered word changes a
    non-whitespace character and is still caught.  The two negative fixtures
    that exercise this check (truncation, lost load-bearing sentence) both
    still fire.
    """
    return re.sub(r"\s+", "", plain(t))


def report(name, ok, detail):
    print("  [%s] %s -- %s" % ("PASS" if ok else "FAIL", name, detail))
    if not ok:
        failures.append(name)


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    arg = sys.argv[1].strip()

    _guard_description_is_gate_verified()

    if arg.startswith("--fixture="):
        # Offline self-test.  A checker that has never run against anything is
        # not a checker.  The live record does not exist yet, so the only way
        # to test this before it is needed is a locally built fixture.
        path = arg.split("=", 1)[1]
        url = "(fixture) " + path
        with open(path, "rb") as fh:
            body = fh.read()
    else:
        rid = arg
        if not rid.isdigit():
            print("record id must be digits, got %r" % rid)
            return 2
        url = "https://zenodo.org/api/records/%s" % rid
        with urllib.request.urlopen(url, timeout=60) as r:
            body = r.read()

    print("=" * 76)
    print("postpublish_readback.py -- READ-ONLY, no token")
    print("source: %s" % url)
    print("=" * 76)
    print()

    rec = json.loads(body.decode("utf-8"))

    # ---- reader integrity: assert known-present structure before any absence
    for key in ("metadata", "doi", "conceptdoi"):
        if key not in rec:
            print("  [FAIL] the fetched record has no %r key: the read is suspect" % key)
            return 2
    md = rec["metadata"]
    print("  [PASS] record fetched and structurally sound (%d bytes)" % len(body))
    print()

    print("SECTION 1 -- IDENTITY")
    print("-" * 76)
    report("version is 1.7", md.get("version") == "1.7",
           "version = %r" % md.get("version"))
    report("concept DOI unchanged, read from the conceptdoi field",
           rec.get("conceptdoi") == EXPECT_CONCEPT_DOI,
           "conceptdoi = %r" % rec.get("conceptdoi"))
    report("version DOI differs from the concept DOI",
           rec.get("doi") and rec.get("doi") != rec.get("conceptdoi"),
           "doi = %r" % rec.get("doi"))
    report("the version DOI was not guessed from the record number",
           rec.get("doi", "").endswith(str(rec.get("id", ""))),
           "doi %r corresponds to record id %r -- recorded, not derived"
           % (rec.get("doi"), rec.get("id")))
    print()

    print("SECTION 2 -- THE CARRIED FILE")
    print("-" * 76)
    files = rec.get("files") or []
    report("exactly one file is published", len(files) == 1,
           "%d file(s): %s" % (len(files), [f.get("key") for f in files]))
    if files:
        f = files[0]
        key = f.get("key")
        md5 = (f.get("checksum") or "").split(":")[-1]
        report("the file key is the carried-over name", key == EXPECT_FILE_KEY,
               "key = %r" % key)
        report("no draft marker or record id in the filename",
               key and "draft" not in key.lower() and not re.search(r"\d{6,}", key),
               "filename is clean: %r" % key)
        report("the file bytes are v1.6's, unchanged",
               f.get("size") == EXPECT_FILE_BYTES and md5 == EXPECT_FILE_MD5,
               "size = %s, md5 = %s" % (f.get("size"), md5))
    print()

    print("SECTION 3 -- THE DESCRIPTION")
    print("-" * 76)
    published = md.get("description") or ""
    with open(DESC, encoding="utf-8") as fh:
        local = fh.read()
    p_pub, p_loc = plain(published), plain(local)
    report("a description is present and substantial", len(p_pub) > 10000,
           "%d rendered chars published, %d locally" % (len(p_pub), len(p_loc)))
    report("the description is not truncated",
           p_loc[-60:] in p_pub,
           "the last 60 rendered chars of the local file are%s present"
           % ("" if p_loc[-60:] in p_pub else " NOT"))
    s_pub, s_loc = squeeze(published), squeeze(local)
    # Non-vacuity: two empty strings compare equal.  Refuse to report a match
    # on a comparison that has nothing in it.
    report("the text being compared is substantial (comparison not vacuous)",
           len(s_loc) > 10000 and len(s_pub) > 10000,
           "%d non-whitespace chars published, %d locally" % (len(s_pub), len(s_loc)))
    report("published text matches the checked description, character for "
           "character (whitespace-normalised)",
           s_pub == s_loc,
           ("every non-whitespace character matches"
            + ("" if len(p_pub) == len(p_loc) else
               "; %+d whitespace chars, from Zenodo re-serialising inline tags"
               % (len(p_pub) - len(p_loc))))
           if s_pub == s_loc else
           "DIFFERS IN CONTENT, not merely whitespace: %d vs %d non-whitespace "
           "chars -- a missing paragraph or altered word, repaired by a further "
           "version, never by an edit" % (len(s_pub), len(s_loc)))
    missing = [s for s in ["the v1.6 build, unchanged", "no PDF was rebuilt",
                           "Naming prohibition", "removed as redundant",
                           "must not be written as PROVEN"] if s not in p_pub]
    report("the load-bearing sentences survived", not missing,
           "all present" if not missing else "MISSING: %s" % missing)
    for banned in ["DRAFT ONLY", "Not deposited"]:
        report("no draft-stage language published (%r)" % banned,
               banned not in p_pub, "absent" if banned not in p_pub else "PRESENT")
    print()

    print("SECTION 4 -- METADATA, AGAINST THE HELD v1.6 RECORD")
    print("-" * 76)
    with open(V16, encoding="utf-8") as fh:
        v16 = json.load(fh)["metadata"]
    report("title unchanged", md.get("title") == v16.get("title"),
           "match" if md.get("title") == v16.get("title") else "DRIFTED")
    c_new = (md.get("creators") or [{}])[0]
    c_old = (v16.get("creators") or [{}])[0]
    report("creator name unchanged", c_new.get("name") == c_old.get("name"),
           "%r" % c_new.get("name"))
    report("affiliation unchanged", c_new.get("affiliation") == c_old.get("affiliation"),
           "%r" % c_new.get("affiliation"))
    lic = md.get("license")
    lic_id = lic.get("id") if isinstance(lic, dict) else lic
    old_lic = v16.get("license")
    old_id = old_lic.get("id") if isinstance(old_lic, dict) else old_lic
    report("licence unchanged", lic_id == old_id, "%r" % lic_id)
    kws = md.get("keywords") or []
    report("keyword count is %d" % EXPECT_KEYWORDS, len(kws) == EXPECT_KEYWORDS,
           "%d keywords" % len(kws))
    report("keyword set unchanged", set(kws) == set(v16.get("keywords") or []),
           "match" if set(kws) == set(v16.get("keywords") or []) else "DRIFTED")
    print()

    print("=" * 76)
    print("checks failed : %d%s" % (len(failures),
                                    ("  -> " + "; ".join(failures)) if failures else ""))
    print()
    if failures:
        print("VERDICT: the published record is NOT the packet that was checked.")
        print("  Files and filenames are frozen after publishing. A defect here is")
        print("  repaired by a further version, never by an edit -- which is what")
        print("  v1.6 itself did for the same class.")
    else:
        print("VERDICT: the published record is the packet that was checked.")
        print("  Store the record JSON and description under refs/ with bytes and")
        print("  sha256 now. From this moment the DEPOSITED TEXT IS AUTHORITATIVE")
        print("  and this repository's copy is the one that may go stale.")
    print("=" * 76)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
