"""Verify OUTLINE.md: every claim id and every cited path must exist.

Control arms are included because a checker that cannot fail is worthless:
each arm asserts the checker REJECTS something it should reject.
"""

import json
import os
import re
import sys
import hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
SESSION = os.path.dirname(HERE)
SESSIONS_2026_09_17 = os.path.dirname(SESSION)
OUTLINE = os.path.join(SESSION, "OUTLINE.md")

# Claim ids in this corpus take several shapes; match them all.
CLAIM_RE = re.compile(
    r"\b("
    r"S5B-C\d{1,2}"
    r"|S6-C\d{1,2}"
    r"|CT-S9-PVPARAMS-C\d{3}"
    r"|S9-PVPARAMS-C\d{3}"
    r"|S\d{1,2}[AB]?-R\d+-\d{2,3}"
    r"|S\d{1,2}[AB]?-\d{2,3}"
    r")\b"
)

# Paths cited in backticks that look like repo paths.
PATH_RE = re.compile(r"`(CT-S[0-9A-Za-z\-]+/[^`]*?)`")


def load_corpus_claim_ids():
    ids = {}
    for root, _dirs, files in os.walk(SESSIONS_2026_09_17):
        for fn in files:
            if fn != "claims.jsonl":
                continue
            p = os.path.join(root, fn)
            for line in open(p, encoding="utf-8"):
                line = line.strip()
                if not line:
                    continue
                try:
                    d = json.loads(line)
                except json.JSONDecodeError:
                    continue
                cid = d.get("claim_id")
                if cid:
                    ids[cid] = os.path.basename(root)
    return ids


def check_text(text, corpus):
    """Return (found, unknown_ids, missing_paths) for a block of text."""
    found = sorted(set(CLAIM_RE.findall(text)))
    unknown = []
    for cid in found:
        if cid in corpus or ("CT-" + cid) in corpus:
            continue
        unknown.append(cid)

    missing = []
    for raw in sorted(set(PATH_RE.findall(text))):
        rel = raw.rstrip("/")
        if " " in rel:
            continue
        # Citations may carry a line number, e.g. foo.py:96 - strip it.
        rel = re.sub(r":\d+$", "", rel)
        full = os.path.join(SESSIONS_2026_09_17, rel.replace("/", os.sep))
        if not os.path.exists(full):
            missing.append(rel)
    return found, unknown, missing


def controls(corpus):
    """Each arm must FAIL the checker. If an arm passes, the checker is broken."""
    arms = [
        ("fake claim id", "see `S99-42` for details", "id"),
        ("fake path", "lives in `CT-S99-NOWHERE/REPORT.md`", "path"),
        ("plausible but absent id", "claim `S16-99` says so", "id"),
        # Guards the ":NN" loosening below: stripping a line number must not
        # disable path checking.
        ("fake path WITH line number", "at `CT-S99-NOWHERE/foo.py:12`", "path"),
        ("real file, fake line-numbered sibling",
         "at `CT-S16-MEMBERSHIP-C/no_such_script.py:96`", "path"),
    ]
    ok = True
    for name, text, kind in arms:
        _found, unknown, missing = check_text(text, corpus)
        caught = bool(unknown) if kind == "id" else bool(missing)
        print(f"  control [{name}]: {'CAUGHT (ok)' if caught else 'MISSED (BROKEN)'}")
        if not caught:
            ok = False
    _f, unknown, missing = check_text(
        "claim `S22-15` in `CT-S22-STOKES/claims.jsonl`", corpus
    )
    good = not unknown and not missing
    print(
        f"  control [real id + real path]: "
        f"{'PASSED (ok)' if good else 'FLAGGED (BROKEN)'}"
    )
    if not good:
        print("    unknown:", unknown, "missing:", missing)
        ok = False
    return ok


def main():
    corpus = load_corpus_claim_ids()
    print(f"corpus claim ids loaded: {len(corpus)}")

    print("\ncontrol arms (each must be caught):")
    if not controls(corpus):
        print("\nCONTROL FAILED - checker cannot be trusted. Halting.")
        return 2

    text = open(OUTLINE, encoding="utf-8").read()
    found, unknown, missing = check_text(text, corpus)

    print(f"\nOUTLINE.md: {len(text)} chars")
    print(f"claim ids cited: {len(found)}")
    print(f"unknown claim ids: {len(unknown)}")
    for c in unknown:
        print("   UNKNOWN:", c)
    print(f"cited paths missing on disk: {len(missing)}")
    for m in missing:
        print("   MISSING:", m)

    sessions = sorted({corpus.get(c, corpus.get("CT-" + c, "?")) for c in found})
    print("\nsessions drawn on (" + str(len(sessions)) + "):", ", ".join(sessions))

    h = hashlib.sha256(open(OUTLINE, "rb").read()).hexdigest()
    print("\nOUTLINE.md sha256:", h)

    verdict = "OK" if not unknown and not missing else "DEFECTS FOUND"
    print("VERDICT:", verdict)
    return 0 if verdict == "OK" else 1


if __name__ == "__main__":
    sys.exit(main())
