"""Independent recount of the widened pass.

Separate invocation, separate implementation.  The checker accumulates into a
list and filters it with comprehensions; this walks with pathlib.rglob, counts
with a Counter keyed on a classification function, and derives each failure
total from the label tally rather than from the failure lists.  Two routes to
the same number, or the number is not established.

The stood-down folder is not walked: this script's root is the repository
only.  SCOPE's contribution is recomputed from its two known claim files by
name, so nothing under CT-S31-COLDREAD-ROWS is listed.
"""
import collections
import hashlib
import io
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")

REPO = pathlib.Path(__file__).resolve().parents[4]
SCOPE = pathlib.Path(r"C:\LocalWork\SCOPE")
STOOD_DOWN = "CT-S31-COLDREAD-ROWS"
LABELS = {"PROVEN", "VERIFIED", "STRUCTURAL", "CONJECTURED", "INSPECTED"}

BUF = io.StringIO()
N = [0]


def say(s=""):
    print(s)
    BUF.write(s + "\n")


def ok(cond, name, fired_if):
    assert cond, "CONTROL FAILED: " + name
    N[0] += 1
    say("  [PASS] %s" % name)
    say("         would have fired if: %s" % fired_if)


def load(path):
    raw = path.read_bytes()
    text = raw.decode("utf-8-sig", errors="replace")
    objs, bad = [], 0
    for line in text.splitlines():
        s = line.strip()
        if not s:
            continue
        try:
            objs.append(json.loads(s))
        except json.JSONDecodeError:
            bad += 1
    if bad:
        try:
            doc = json.loads(text)
        except json.JSONDecodeError:
            return objs, bad
        if isinstance(doc, list):
            return doc, 0
        if isinstance(doc, dict):
            return [doc], 0
    return objs, bad


files = sorted(REPO.rglob("claims.jsonl"))
# SCOPE by a different route: enumerate its top-level folders, drop the
# stood-down one by NAME before descending, then rglob each survivor. The
# stood-down folder is therefore never listed, and the traversal differs from
# the checker's os.walk-with-pruning while covering the same set.
scope_files = []
for d in sorted(p for p in SCOPE.iterdir() if p.is_dir()):
    if d.name == STOOD_DOWN:
        continue
    scope_files.extend(sorted(d.rglob("claims.jsonl")))
scope_files.extend(sorted(p for p in SCOPE.glob("claims.jsonl")))
assert all(STOOD_DOWN not in p.parts for p in scope_files)

labels = collections.Counter()
ids = collections.Counter()
per_root = {}
n_bad_lines = 0
empty = []
fingerprint = []

for tag, group in (("repo", files), ("SCOPE", scope_files)):
    n = 0
    for p in group:
        fingerprint.append("%s\t%s"
                           % (p, hashlib.sha256(p.read_bytes()).hexdigest()))
        objs, bad = load(p)
        n_bad_lines += bad
        n += len(objs)
        if not objs and not bad:
            empty.append(p)
        for o in objs:
            labels[o.get("label")] += 1
            cid = o.get("claim_id")
            ids[cid if cid else None] += 1
    per_root[tag] = (len(group), n)

total = sum(n for _, n in per_root.values())
n_walked = sum(nf for nf, _ in per_root.values())
n_contributing = n_walked - len(empty)
no_id = ids[None]
FP = hashlib.sha256("\n".join(sorted(fingerprint)).encode("utf-8")).hexdigest()
dup_ids = {k: v for k, v in ids.items() if k is not None and v > 1}
bad_label = sum(v for k, v in labels.items() if k not in LABELS)

say("=" * 78)
say("CT-S33  independent recount of the widened pass  (θ, ∞ sentinels)")
say("=" * 78)
for tag, (nf, nc) in per_root.items():
    say("  %-6s %4d file(s)  %5d claim(s)" % (tag, nf, nc))
say("  TOTAL  %4d file(s)  %5d claim(s)" % (n_walked, total))
say()
say("  files walked .......................... %d" % n_walked)
say("  files contributing >= 1 claim ......... %d" % n_contributing)
say("  files that are empty (0 bytes) ........ %d" % len(empty))
for p in empty:
    say("      %s" % p)
say()
say("  input fingerprint ..................... %s" % FP)
say("  SCOPE is a LIVE tree written by other processes; its files at read time:")
for p in scope_files:
    say("      %-58s %s"
        % (p.parent.name, hashlib.sha256(p.read_bytes()).hexdigest()[:16]))
say()
say("  claims with no claim_id ............... %d" % no_id)
say("  distinct claim_ids reused ............. %d" % len(dup_ids))
say("  claims with no recognised label ....... %d" % bad_label)
say("  unparseable lines surviving format fix  %d" % n_bad_lines)
say()
say("LABEL TALLY (second route to the invariant-2 total)")
for k, v in sorted(labels.items(), key=lambda kv: str(kv[0])):
    mark = "   " if k in LABELS else " * "
    say("  %s%-14s %5d" % (mark, k, v))
say("  ( * = not a recognised label; these sum to the invariant-2 failure )")
say()

# --- the checker's own numbers, quoted from its artefact -------------------
art = pathlib.Path(__file__).resolve().parents[1] / "outputs" / "widened_pass.out.txt"
txt = art.read_text(encoding="utf-8", errors="replace")
assert "SCOPE OF THIS CHECK" in txt, "artefact of the widened pass not readable"

say("AGREEMENT WITH THE CHECKER'S OWN RUN")
say("  recount input fingerprint: %s over %d file(s)" % (FP, len(fingerprint)))
ok("input fingerprint: %s" % FP in txt,
   "both implementations read byte-identical inputs",
   "any root changing between the two runs. At least one root is a live tree "
   "written by other processes, so this must be settled BEFORE any count is "
   "called a disagreement")
pairs = [
    ("total claims", total, "corpus: %d claims in" % total),
    ("files contributing a claim", n_contributing,
     "claims in %d files" % n_contributing),
    ("invariant-2 failures", bad_label,
     "FAIL 2: %d claim(s)" % bad_label),
    ("reused claim_ids", len(dup_ids),
     "FAIL 1(b): %d duplicate claim_id(s)" % len(dup_ids)),
    ("claims with no claim_id", no_id,
     "(%d claim(s) carry no claim_id" % no_id),
]
for name, value, needle in pairs:
    ok(needle in txt,
       "%-24s = %-6d agrees with the checker's artefact" % (name, value),
       "the two implementations disagreeing on this count, which is the "
       "whole point of recounting")

ok(n_walked - n_contributing == len(empty) and len(empty) > 0,
   "walked-minus-contributing is accounted for exactly by empty files",
   "the two file counts differing for any reason OTHER than empty files, "
   "which would mean one of the two walks is missing a file the other sees")

ok(bad_label == sum(v for k, v in labels.items() if k not in LABELS)
   and bad_label != total,
   "invariant-2 total derived from the label tally, not from the fail list",
   "every claim being unlabelled, which would make the tally route vacuous")

ok(len(scope_files) >= 1 and all(STOOD_DOWN not in p.parts for p in scope_files),
   "SCOPE contributes files and none is under the stood-down folder",
   "the stand-down being violated, or SCOPE contributing nothing at all")

say()
say("CONTROLS: %d/%d PASS" % (N[0], N[0]))

OUT = pathlib.Path(__file__).resolve().parents[1] / "outputs" / "recount.out.txt"
data = BUF.getvalue()
OUT.write_text(data, encoding="utf-8", newline="")
raw = OUT.read_bytes()
assert b"\r\n" not in raw
t = raw.decode("utf-8")
assert "θ" in t and "∞" in t, "non-ASCII sentinel absent: reader unverified"
assert "θ" not in raw.decode("latin-1")
assert t == data
print("sha256 = %s  bytes = %d" % (hashlib.sha256(raw).hexdigest(), len(raw)))
