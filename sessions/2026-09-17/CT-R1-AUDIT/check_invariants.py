"""Per-round invariant check over an EXPLICIT list of claim roots.

Run at the end of every round, before appending a new AUDIT.md section.
Exit code is nonzero if any invariant fails.

SCOPE -- read this before trusting any "INVARIANTS OK" line.
---------------------------------------------------------------------------
This checker walks the roots named in ROOTS, minus the paths named in
EXCLUDE, and nothing else. It prints both lists on every run, together with
per-root file and claim counts and an input fingerprint, so the scope of a
verdict is visible in the output rather than implied by this docstring.

It has not always been so. Until 2026-09-19 the root was
`pathlib.Path(__file__).resolve().parents[1]`, i.e. `sessions/2026-09-17`
alone, while this docstring claimed coverage of "the whole session corpus".
That reached 30 of 447 claims.jsonl files. Every "INVARIANTS OK" printed
before that date was a statement about `sessions/2026-09-17` and nothing else.

SCOPING IS NOT LOOSENING. Invariants 2 and 1(b) are scoped, not weakened.
The corpus predates several of its own conventions, and a claim written before
a convention existed cannot violate it. Every claim taken out of an
invariant's scope is COUNTED AND PRINTED under "holes in that verdict"; none
is silently dropped. Retrofitting a label onto a claim nobody re-read would be
inventing evidence, so it is not done here or anywhere else.

Invariants
  0     every declared root exists
  1(a)  no `file_inspection` claim carries the label PROVEN
  1(b)  claim_id uniqueness, in three parts:
          (i)   ids that are neither session-local counters nor deposit
                mirrors must be globally unique
          (ii)  session-local counters must be unique WITHIN a session
          (iii) claims with no id are counted and printed, not silently
                outside the check
  2     every claim dated on or after CONVENTION_DATE carries exactly one
        recognised label; older claims are counted with their date range
  3     every claim with a `review` field also carries a `review_note`
  4     `review` is one of self | cold | lean
  5     every claims.jsonl is plain JSONL: UTF-8, no BOM, one object per line
"""
import json
import os
import pathlib
import re
import sys
from collections import Counter, defaultdict
from hashlib import sha256

# --- THE SCOPE OF THIS CHECK. Widen deliberately; both lists are printed. ---
REPO = pathlib.Path(__file__).resolve().parents[3]

ROOTS = [
    REPO,
]

# Each exclusion must carry a reason. An exclusion is a hole in the check.
EXCLUDE = {
    pathlib.Path(r"C:\LocalWork\SCOPE"):
        "REMOVED FROM ROOTS 2026-09-19. Three reasons, all open: (a) the "
        "operator stand-down on CT-S31-COLDREAD-ROWS, an input packet being "
        "assembled for a separate uncontaminated process; (b) the tree is "
        "written by other processes WHILE THE CHECK RUNS -- one file gained "
        "three claims between two runs minutes apart, so any verdict over it "
        "has a race in it; (c) Window B's status is unsettled. Restore to "
        "ROOTS when all three are closed, not before.",
    pathlib.Path(r"C:\LocalWork\SCOPE\CT-S31-COLDREAD-ROWS"):
        "operator stand-down 2026-09-19: not to be read, listed or written. "
        "Retained explicitly so that restoring the parent does not silently "
        "restore this folder too.",
}

LABELS = {"PROVEN", "VERIFIED", "STRUCTURAL", "CONJECTURED", "INSPECTED"}
REVIEWS = {"self", "cold", "lean"}

# --- Invariant 2 scope -----------------------------------------------------
# Derivation rule, applied to the record on 2026-09-19: the earliest date D
# such that EVERY claim dated on or after D carries a recognised label.
# Measured result 2026-09-17. Labelling is not monotone before it: it appears
# on 2026-05-13 (6 of 89) and 2026-05-14 (9 of 18), then lapses to zero on
# every date from 2026-05-18 to 2026-06-18, and is universal (578 of 578) only
# from 2026-09-17. A cut at the first labelled date would leave 661 unlabelled
# claims in scope and would simply fail.
#
# The date is PINNED, not recomputed, and that is deliberate. A cutoff derived
# at run time from the same claims it then judges is self-fulfilling: no claim
# on or after it could ever be unlabelled, and invariant 2 could never fail.
# A check that cannot fire is not a check. The derived value is recomputed
# below and REPORTED when it disagrees, which catches drift without disarming
# the invariant.
CONVENTION_DATE = "2026-09-17"

DATE_IN_PATH = re.compile(r"sessions[\\/](\d{4}-\d{2}-\d{2})[\\/]")

# A session-local counter: C1..C9 and similar, optionally prefixed by a
# session number, e.g. "121-C1". Deliberately narrow -- it must not match a
# real id such as S33-01 or DF-T0-LOCK, or 1(b)(i) would be disabled wholesale.
SESSION_LOCAL_ID = re.compile(r"^(?:\d+-)?C\d+$")

# A deposit mirror: an intentional copy of another session's claims under a
# `deposit/` PATH COMPONENT. Anchored to separators so it cannot match
# "deposited" or "DEPOSIT-FORM".
MIRROR_PATH = re.compile(r"[\\/]deposit[\\/]")

# A known hole, left unrepaired by ruling. Editing a historical record to
# satisfy a checker is the wrong direction.
KNOWN_UNREADABLE = {
    ("sessions/2026-04-30/SIARC-COHERENCE-AUDIT/claims.jsonl", 3):
        "raw LaTeX \\(2,2\\) inside a JSON string; one line in 4066; "
        "left unrepaired by ruling 2026-09-19",
}


def find_claim_files(root):
    """Walk `root`, pruning EXCLUDE before descending.

    Pruning happens in `dirnames`, so an excluded directory is never listed,
    let alone read. Returns None if the root does not exist.
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
    """Return (claims, fmt, damaged_lines), reading any of the known formats.

    Non-JSONL files are read anyway. Refusing them would reproduce the very
    coverage gap this checker was rewritten to remove. The deviation is
    reported under invariant 5.
    """
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


def claim_date(path):
    m = DATE_IN_PATH.search(str(path))
    return m.group(1) if m else None


def body_of(c):
    b = c.get("claim") or c.get("statement") or c.get("text") or ""
    return " ".join(str(b).split())


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
    print("  EXCLUDED %s" % str(ex))
    for i in range(0, len(why), 92):
        print("           %s" % why[i:i + 92])

FP = sha256("\n".join(sorted(fingerprint)).encode("utf-8")).hexdigest()
print("\ninput fingerprint: %s  over %d file(s) read" % (FP, len(fingerprint)))
print("  (sha256 of the sorted path+content hashes. Compare two runs on this "
      "line\n   before calling any count difference a disagreement.)")
if empty_files:
    print("  %d file(s) read but empty, absent from the per-file count below:"
          % len(empty_files))
    for f in empty_files:
        print("      %s" % f)

n_files = len({str(p) for _, _, p in claims})
print("\ncorpus: %d claims in %d files across %d reachable root(s)"
      % (len(claims), n_files, len(ROOTS) - len(missing_roots)))
print("invariant 2 cutoff (pinned): %s\n" % CONVENTION_DATE)

fails = 0
holes = []

# --- 0 roots exist ----------------------------------------------------------
if missing_roots:
    fails += 1
    print("FAIL 0: %d declared root(s) do not exist" % len(missing_roots))
    for r in missing_roots:
        print("   ", r)
else:
    print("ok   0: all %d declared root(s) exist" % len(ROOTS))

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

# --- 1(b) claim_id uniqueness, split three ways -----------------------------
by_id = defaultdict(list)          # id -> [(path, lineno, body)]
idless = []
for lineno, c, p in claims:
    cid = c.get("claim_id")
    if cid:
        by_id[cid].append((p, lineno, body_of(c)))
    else:
        idless.append((p, lineno))

reused = {k: v for k, v in by_id.items()
          if len({str(p) for p, _, _ in v}) > 1}

# (ii) session-local counters: unique WITHIN a session, not globally
local_ids, local_dups = [], []
for cid, occ in by_id.items():
    if not SESSION_LOCAL_ID.match(cid):
        continue
    local_ids.append(cid)
    per_file = Counter(str(p) for p, _, _ in occ)
    for f, n in per_file.items():
        if n > 1:
            local_dups.append((cid, f, n))

# (i) everything else must be globally unique, unless it is a deposit mirror
mirrors, collisions = [], []
for cid, occ in sorted(reused.items()):
    if SESSION_LOCAL_ID.match(cid):
        continue
    paths = [p for p, _, _ in occ]
    matched = [str(p) for p in paths if MIRROR_PATH.search(str(p))]
    if matched:
        mirrors.append((cid, matched))
    else:
        collisions.append((cid, occ))

if local_dups:
    fails += 1
    print("FAIL 1(b)(ii): %d session-local counter(s) reused WITHIN one session"
          % len(local_dups))
    for cid, f, n in local_dups[:20]:
        print("   %s x%d in %s" % (cid, n, f))
else:
    print("ok   1(b)(ii): %d session-local counter id(s), each unique within "
          "its own session" % len(local_ids))
    n_local_reused = sum(1 for cid in reused if SESSION_LOCAL_ID.match(cid))
    print("               %d of them recur across sessions, which is what a "
          "session-local" % n_local_reused)
    print("               counter is for, and is not checked globally")
    holes.append("%d session-local counter id(s) are exempt from GLOBAL "
                 "uniqueness by pattern %s" % (n_local_reused,
                                               SESSION_LOCAL_ID.pattern))

if collisions:
    fails += 1
    print("FAIL 1(b)(i): %d id(s) reused across sessions and matching no "
          "exemption" % len(collisions))
    shown = 0
    for cid, occ in collisions:
        bodies = {b for _, _, b in occ}
        tag = ("identical claim text in all %d places" % len(occ)
               if len(bodies) == 1 else
               "DIFFERENT claim text -- a true collision")
        if shown < 12:
            print("   %-22s %s" % (cid, tag))
            shown += 1
    n_same = sum(1 for _, occ in collisions if len({b for _, _, b in occ}) == 1)
    print("   of the %d: %d carry IDENTICAL claim text in every place they "
          "appear," % (len(collisions), n_same))
    print("   i.e. they are restatements (an aggregator or a verifier citing "
          "the id it")
    print("   verified), and %d carry different text. Text identity is NOT "
          "accepted here" % (len(collisions) - n_same))
    print("   as an exemption: no pattern was invented to absorb them. They "
          "are reported")
    print("   in full so the convention can be ruled on.")
else:
    print("ok   1(b)(i): every non-exempt id is globally unique")

if mirrors:
    print("ok   1(b)(i): %d id(s) exempt as deposit mirrors, pattern %s"
          % (len(mirrors), MIRROR_PATH.pattern))
    for cid, matched in mirrors[:8]:
        print("               %-16s matched %s" % (cid, matched[0]))
    if len(mirrors) > 8:
        print("               ... and %d more" % (len(mirrors) - 8))
    holes.append("%d id(s) exempt from uniqueness as deposit mirrors, "
                 "pattern %s" % (len(mirrors), MIRROR_PATH.pattern))

print("     1(b)(iii): %d claim(s) carry no claim_id at all and are outside "
      "every" % len(idless))
print("                uniqueness check. This is a hole, not a pass.")
holes.append("%d claim(s) have no claim_id and are outside 1(b) entirely"
             % len(idless))

# --- 2 exactly one recognised label, scoped to the convention ---------------
in_scope, pre_scope = [], []
for lineno, c, p in claims:
    d = claim_date(p)
    (in_scope if (d is None or d >= CONVENTION_DATE) else pre_scope).append(
        (lineno, c, p, d))

bad = ["%s:%s %s -> %r" % (p, n, c.get("claim_id"), c.get("label"))
       for n, c, p, _ in in_scope if c.get("label") not in LABELS]
if bad:
    fails += 1
    print("FAIL 2: %d claim(s) dated on/after %s with an unrecognised or "
          "missing label" % (len(bad), CONVENTION_DATE))
    for b in bad[:20]:
        print("  ", b)
    if len(bad) > 20:
        print("   ... and %d more" % (len(bad) - 20))
else:
    print("ok   2: all %d claim(s) dated on/after %s carry exactly one "
          "recognised label" % (len(in_scope), CONVENTION_DATE))

if pre_scope:
    dates = sorted(d for _, _, _, d in pre_scope if d)
    n_lab = sum(1 for _, c, _, _ in pre_scope if c.get("label") in LABELS)
    n_any = sum(1 for _, c, _, _ in pre_scope if c.get("label"))
    print("     2: %d claim(s) dated before %s are OUT OF SCOPE, range %s .. %s"
          % (len(pre_scope), CONVENTION_DATE, dates[0], dates[-1]))
    print("        %d carry a recognised label; %d carry a label field of any "
          "kind." % (n_lab, n_any))
    if n_any > n_lab:
        print("        The %d difference is an earlier attempt at the "
              "convention that lapsed" % (n_any - n_lab))
        print("        (values such as PROCEED and REFINED). Not judged "
              "either way.")
    holes.append("%d claim(s) dated %s .. %s predate the label convention and "
                 "are outside invariant 2" % (len(pre_scope), dates[0],
                                              dates[-1]))

# drift check: recompute the cutoff and report, never act on it
labelled_by_date = defaultdict(lambda: [0, 0])
for lineno, c, p, d in in_scope + pre_scope:
    if d:
        labelled_by_date[d][0 if c.get("label") in LABELS else 1] += 1
derived = None
for d in sorted(labelled_by_date, reverse=True):
    if labelled_by_date[d][1]:
        break
    derived = d
if derived != CONVENTION_DATE:
    print("     2: NOTE the cutoff derived from the record today is %s, not "
          "the pinned %s." % (derived, CONVENTION_DATE))
    print("        Reported, not applied. A cutoff recomputed from the claims "
          "it judges")
    print("        could never fail.")

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
else:
    print("ok   3: every reviewed claim carries a review_note")
if bad_val:
    fails += 1
    print("FAIL 4: %d claim(s) with an unrecognised review value" % len(bad_val))
    for b in bad_val[:20]:
        print("  ", b)
else:
    print("ok   4: every review value is one of self|cold|lean")

# --- 5 file format ----------------------------------------------------------
unknown_damage = []
for f, lineno, why in damaged_lines:
    rel = str(pathlib.Path(f)).replace("\\", "/")
    key = next((k for k in KNOWN_UNREADABLE
                if rel.endswith(k[0]) and k[1] == lineno), None)
    if key is None:
        unknown_damage.append((f, lineno, why))

if formats or damaged_lines:
    fails += 1
    print("FAIL 5: %d claims file(s) are not plain JSONL" % len(formats))
    for f, fmt in sorted(formats.items()):
        print("   %-38s %s" % (fmt, f))
    for f, lineno, why in damaged_lines:
        rel = str(pathlib.Path(f)).replace("\\", "/")
        key = next((k for k in KNOWN_UNREADABLE
                    if rel.endswith(k[0]) and k[1] == lineno), None)
        mark = "KNOWN HOLE" if key else "NEW DAMAGE"
        print("   %s %s:%d  %s" % (mark, f, lineno, why))
        if key:
            print("      left unrepaired: %s" % KNOWN_UNREADABLE[key])
            holes.append("1 claim unreadable at %s:%d, left unrepaired by "
                         "ruling" % (key[0], key[1]))
    print("   (all of the above were READ anyway; only a DAMAGED line loses "
          "a claim)")
    if unknown_damage:
        print("   %d damaged line(s) are NOT on the known-hole list"
              % len(unknown_damage))
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
print("holes in that verdict:")
for e in EXCLUDE:
    print("  - not walked at all: %s" % e)
for h in holes:
    print("  - %s" % h)
sys.exit(1 if fails else 0)
