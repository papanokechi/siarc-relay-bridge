"""Per-round invariant check over an EXPLICIT list of claim roots.

Run at the end of every round, before appending a new AUDIT.md section.
Exit code is nonzero if any invariant fails.

SCOPE -- read this before trusting any "INVARIANTS OK" line.
---------------------------------------------------------------------------
This checker walks the roots named in ROOTS below, minus the paths named in
EXCLUDE, and nothing else.  It prints both lists on every run, together with
the number of files and claims found under each root, so the scope of a
verdict is visible in the output rather than implied by this docstring.

It has not always been so.  Until 2026-09-19 the root was
`pathlib.Path(__file__).resolve().parents[1]`, i.e. `sessions/2026-09-17`
alone, while this docstring claimed coverage of "the whole session corpus".
That reached 29 of the repository's 444 claims.jsonl files.  Every
"INVARIANTS OK" printed before that date was a statement about
`sessions/2026-09-17/` and about nothing else.  The roots list exists so that
widening is a deliberate, reviewable edit to a named constant rather than a
silent property of a relative path.

FILE FORMATS.  A claims file is expected to be JSONL: one JSON object per
line, UTF-8, no BOM.  Deviations are read anyway -- refusing to read them
would reproduce the coverage gap this file was rewritten to remove -- but each
is reported under invariant 5 and each fails the run.  Three kinds are
distinguished, because they are not the same severity: a BOM (mechanical, no
claim lost); a whole valid JSON array or object in the wrong container (no
claim lost); and a line that yields no claim at all (data loss).  A single
unparseable line never aborts the run; the previous version exited on the
first one, which under a widened scope would have stopped the check before it
examined anything.

Invariants
  0     every declared root exists
  1(a)  no `file_inspection` claim carries the label PROVEN
  1(b)  every claim_id is unique across the roots
  2     every claim carries exactly one recognised label
  3     every claim with a `review` field also carries a `review_note`
  4     `review` is one of self | cold | lean
  5     every claims.jsonl is plain JSONL: UTF-8, no BOM, one object per line
"""
import json
import os
import pathlib
import sys
from collections import Counter, defaultdict
from hashlib import sha256

# --- THE SCOPE OF THIS CHECK. Widen deliberately; both lists are printed. ---
REPO = pathlib.Path(__file__).resolve().parents[3]

ROOTS = [
    REPO,
    pathlib.Path(r"C:\LocalWork\SCOPE"),
]

# Each exclusion must carry a reason. An exclusion is a hole in the check.
EXCLUDE = {
    pathlib.Path(r"C:\LocalWork\SCOPE\CT-S31-COLDREAD-ROWS"):
        "operator stand-down 2026-09-19: input packet being assembled for a "
        "separate uncontaminated process; not to be read, listed or written. "
        "Remove this entry once the packet is released.",
}

LABELS = {"PROVEN", "VERIFIED", "STRUCTURAL", "CONJECTURED", "INSPECTED"}
REVIEWS = {"self", "cold", "lean"}


def find_claim_files(root):
    """Walk `root`, pruning EXCLUDE before descending.

    Pruning happens in `dirnames`, so an excluded directory is never listed,
    let alone read.  Returns None if the root does not exist.
    """
    if not root.exists():
        return None
    out = []
    for dirpath, dirnames, filenames in os.walk(root):
        here = pathlib.Path(dirpath)
        dirnames[:] = [d for d in dirnames if (here / d) not in EXCLUDE]
        if "claims.jsonl" in filenames:
            out.append(here / "claims.jsonl")
    return sorted(out)


def read_claims(path):
    """Return (claims, fmt, damaged_lines), reading any of the known formats."""
    raw = path.read_bytes()
    had_bom = raw.startswith(b"\xef\xbb\xbf")
    text = raw.decode("utf-8-sig", errors="replace")

    objs, damaged = [], []
    for lineno, line in enumerate(text.splitlines(), 1):
        s = line.strip()
        if not s:
            continue
        try:
            objs.append((lineno, json.loads(s)))
        except json.JSONDecodeError as exc:
            damaged.append((lineno, str(exc)))

    if not damaged:
        return objs, ("JSONL + BOM" if had_bom else "JSONL"), []

    try:
        doc = json.loads(text)
    except json.JSONDecodeError:
        doc = None
    if isinstance(doc, list):
        return [(0, o) for o in doc], "WRONG CONTAINER (JSON array)", []
    if isinstance(doc, dict):
        return [(0, doc)], "WRONG CONTAINER (single JSON object)", []
    return objs, "DAMAGED", damaged


# --------------------------------------------------------------- collect ---
print("SCOPE OF THIS CHECK")
claims = []
per_root = Counter()
missing_roots = []
formats = {}
damaged_lines = []
fingerprint = []
empty_files = []

for root in ROOTS:
    files = find_claim_files(root)
    if files is None:
        missing_roots.append(root)
        print("  root     %-44s NOT FOUND" % str(root))
        continue
    n_before = len(claims)
    for path in files:
        fingerprint.append("%s\t%s"
                           % (path, sha256(path.read_bytes()).hexdigest()))
        objs, fmt, damaged = read_claims(path)
        if fmt != "JSONL":
            formats[str(path)] = fmt
        if not objs and not damaged:
            empty_files.append(str(path))
        for lineno, why in damaged:
            damaged_lines.append((str(path), lineno, why))
        for lineno, obj in objs:
            claims.append((lineno, obj, path))
    per_root[str(root)] = len(claims) - n_before
    print("  root     %-44s %4d file(s)  %5d claim(s)"
          % (str(root), len(files), per_root[str(root)]))

for ex, why in EXCLUDE.items():
    print("  EXCLUDED %-44s %s" % (str(ex), why))

n_files = len({str(p) for _, _, p in claims})
FP = sha256("\n".join(sorted(fingerprint)).encode("utf-8")).hexdigest()
print("\ninput fingerprint: %s  over %d file(s) read"
      % (FP, len(fingerprint)))
print("  (sha256 of the sorted path+content hashes. At least one root is a "
      "live tree\n   written by other processes; two runs that disagree on a "
      "count should be\n   compared on this line first, before either is "
      "called wrong.)")
if empty_files:
    print("  %d file(s) read but empty, so absent from the per-file count below:"
          % len(empty_files))
    for f in empty_files:
        print("      %s" % f)
print("\ncorpus: %d claims in %d files across %d reachable root(s)\n"
      % (len(claims), n_files, len(ROOTS) - len(missing_roots)))

fails = 0

# --- 0 roots exist ----------------------------------------------------------
if missing_roots:
    fails += 1
    print("FAIL 0: %d declared root(s) do not exist" % len(missing_roots))
    for r in missing_roots:
        print("   ", r)
else:
    print("ok   0: all %d declared root(s) exist" % len(ROOTS))

# --- 1(b) duplicate claim_id ------------------------------------------------
seen = defaultdict(list)
no_id = 0
for lineno, c, path in claims:
    cid = c.get("claim_id")
    if cid:
        seen[cid].append("%s:%s" % (path, lineno))
    else:
        no_id += 1
dups = {k: v for k, v in seen.items() if len(v) > 1}
if dups:
    fails += 1
    print("FAIL 1(b): %d duplicate claim_id(s)" % len(dups))
    for k, v in sorted(dups.items())[:20]:
        print("   %s: %s" % (k, v))
    if len(dups) > 20:
        print("   ... and %d more" % (len(dups) - 20))
else:
    print("ok   1(b): all %d claim_ids unique" % len(seen))
print("     (%d claim(s) carry no claim_id at all and are outside 1(b))"
      % no_id)

# --- 1(a) PROVEN must not rest on file inspection ---------------------------
bad = ["%s:%s %s" % (p, n, c.get("claim_id")) for n, c, p in claims
       if c.get("label") == "PROVEN"
       and c.get("evidence_type") == "file_inspection"]
if bad:
    fails += 1
    print("FAIL 1(a): %d PROVEN claims with evidence_type=file_inspection"
          % len(bad))
    for b in bad[:20]:
        print("  ", b)
else:
    print("ok   1(a): no PROVEN claim rests on file_inspection")

# --- 2 exactly one recognised label ----------------------------------------
bad = ["%s:%s %s -> %r" % (p, n, c.get("claim_id"), c.get("label"))
       for n, c, p in claims if c.get("label") not in LABELS]
if bad:
    fails += 1
    print("FAIL 2: %d claim(s) with an unrecognised or missing label" % len(bad))
    for b in bad[:20]:
        print("  ", b)
    if len(bad) > 20:
        print("   ... and %d more" % (len(bad) - 20))
else:
    print("ok   2: every claim carries exactly one recognised label")

# --- 3/4 review field well-formed ------------------------------------------
missing_note = ["%s:%s %s" % (p, n, c.get("claim_id")) for n, c, p in claims
                if c.get("review") and not c.get("review_note")]
bad_val = ["%s:%s %s -> %r" % (p, n, c.get("claim_id"), c.get("review"))
           for n, c, p in claims
           if c.get("review") and c.get("review") not in REVIEWS]
if missing_note:
    fails += 1
    print("FAIL 3: %d reviewed claim(s) with no review_note" % len(missing_note))
    for b in missing_note[:20]:
        print("  ", b)
    if len(missing_note) > 20:
        print("   ... and %d more" % (len(missing_note) - 20))
else:
    print("ok   3: every reviewed claim carries a review_note")
if bad_val:
    fails += 1
    print("FAIL 4: %d claim(s) with an unrecognised review value" % len(bad_val))
    for b in bad_val[:20]:
        print("  ", b)
    if len(bad_val) > 20:
        print("   ... and %d more" % (len(bad_val) - 20))
else:
    print("ok   4: every review value is one of self|cold|lean")

# --- 5 file format ----------------------------------------------------------
if formats or damaged_lines:
    fails += 1
    print("FAIL 5: %d claims file(s) are not plain JSONL" % len(formats))
    for f, fmt in sorted(formats.items()):
        print("   %-38s %s" % (fmt, f))
    for f, lineno, why in damaged_lines:
        print("   DAMAGED LINE %s:%d  %s" % (f, lineno, why))
    print("   (all of the above were READ anyway; only a DAMAGED line loses"
          " a claim)")
else:
    print("ok   5: every claims.jsonl is plain JSONL, UTF-8, no BOM")

# --- summary ----------------------------------------------------------------
tally = defaultdict(int)
rev = defaultdict(int)
for _, c, _ in claims:
    tally[c.get("label")] += 1
    rev[c.get("review", "(none)")] += 1
print("\nlabels: " + "  ".join(
    "%s=%d" % (k, v) for k, v in sorted(tally.items(), key=lambda kv: str(kv[0]))))
print("review: " + "  ".join(
    "%s=%d" % (k, v) for k, v in sorted(rev.items(), key=lambda kv: str(kv[0]))))
print("\n" + ("INVARIANTS OK" if not fails else "%d INVARIANT(S) FAILED" % fails))
print("scope of that verdict: " + "; ".join(
    "%s = %d claims" % (r, n) for r, n in per_root.items()))
if EXCLUDE:
    print("holes in that verdict: " + "; ".join(str(e) for e in EXCLUDE))
sys.exit(1 if fails else 0)
