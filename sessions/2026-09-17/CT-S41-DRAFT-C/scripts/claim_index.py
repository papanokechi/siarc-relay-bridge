"""claim_index.py -- build a corpus-wide index of AEAL claims.

Scans every claims.jsonl under sessions/ and indexes claim_id -> record.
Used by draft_check.py to resolve the claim ids cited in the drafted prose and
to compare the label asserted in the prose against the label in the corpus.

Supersession: a claim is treated as superseded if any record carries a
'superseded_by' / 'supersedes' field naming it, or if its own record says so.
Both directions are indexed, because a drafter needs to know that the id they
are about to cite has been replaced, not merely that it exists.
"""
import collections, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[3]   # .../sessions
if ROOT.name != "sessions":
    ROOT = pathlib.Path(__file__).resolve().parents[2]

# This session writes a claims.jsonl into the corpus this function walks, so a
# claim citing the gate's output digest would go stale the moment the gate ran
# again (the CT-S34 ordering defect).  The file is excluded BY CONSTRUCTION
# rather than by running the gate first, and the exclusion is asserted
# non-vacuously by draft_check: SELF must EXIST and be ABSENT from the walk.
SELF = pathlib.Path(__file__).resolve().parents[1] / "claims.jsonl"


def corpus_files():
    """Every claims.jsonl under sessions/ except this session's own."""
    return [p for p in sorted(ROOT.rglob("claims.jsonl"))
            if p.resolve() != SELF]


def build():
    index, dupes, files, bad = {}, collections.defaultdict(list), 0, []
    for p in corpus_files():
        files += 1
        for ln, line in enumerate(p.read_text(encoding="utf-8-sig").splitlines(), 1):
            line = line.strip()
            if not line:
                continue
            try:
                c = json.loads(line)
            except json.JSONDecodeError as e:
                bad.append("%s:%d %s" % (p, ln, e))
                continue
            cid = c.get("claim_id")
            if not cid:
                continue
            c["_file"] = str(p.relative_to(ROOT))
            c["_session"] = p.relative_to(ROOT).parts[1] if len(
                p.relative_to(ROOT).parts) > 1 else "?"
            if cid in index:
                dupes[cid].append(c["_file"])
            else:
                index[cid] = c
    # supersession, both directions
    superseded = {}
    for cid, c in index.items():
        for key in ("superseded_by", "supersedes", "replaces", "replaced_by"):
            v = c.get(key)
            if not v:
                continue
            for other in re.findall(r"[A-Z0-9]+-[A-Z0-9\-]*\d+", str(v)):
                if key in ("superseded_by", "replaced_by"):
                    superseded[cid] = "%s (%s)" % (other, key)
                else:
                    superseded[other] = "%s (%s)" % (cid, key)
        txt = (str(c.get("claim", "")) + " " + str(c.get("review_note", ""))).lower()
        if "superseded" in txt or "withdrawn" in txt or "retracted" in txt:
            superseded.setdefault(cid, "self-declared in claim/review_note")
    return index, dupes, files, bad, superseded


def main():
    index, dupes, files, bad, superseded = build()
    print("claim_index: %d files, %d unique claim ids" % (files, len(index)))
    if bad:
        print("UNPARSEABLE LINES (%d):" % len(bad))
        for b in bad:
            print("  " + b)
    if dupes:
        print("DUPLICATE claim ids (%d):" % len(dupes))
        for cid, fs in sorted(dupes.items()):
            print("  %-22s also in %s" % (cid, ", ".join(fs)))
    if superseded:
        print("SUPERSEDED / WITHDRAWN (%d):" % len(superseded))
        for cid, why in sorted(superseded.items()):
            print("  %-22s %s" % (cid, why))
    if len(sys.argv) > 1:
        for pat in sys.argv[1:]:
            rx = re.compile(pat)
            print("\n--- matching %r ---" % pat)
            for cid in sorted(index):
                if rx.match(cid):
                    c = index[cid]
                    print("%-22s %-12s %s" % (cid, c.get("label", "?"),
                                              c["_session"]))
                    print("    %s" % str(c.get("claim", ""))[:400])
                    if c.get("review_note"):
                        print("    note: %s" % str(c["review_note"])[:200])


if __name__ == "__main__":
    main()
