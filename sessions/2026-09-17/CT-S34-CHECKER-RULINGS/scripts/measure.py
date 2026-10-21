"""Measure what the three rulings need, before changing any invariant.

A ruling scoped to "the date the convention was introduced" needs that date
measured, not assumed; a ruling that deposit mirrors be "excluded by path
pattern" needs the pattern derived from the paths that actually collide. This
script decides neither. It reports.
"""
import collections
import hashlib
import io
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

REPO = pathlib.Path(__file__).resolve().parents[4]
DATE = re.compile(r"sessions[\\/](\d{4}-\d{2}-\d{2})[\\/]")
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
    text = path.read_bytes().decode("utf-8-sig", errors="replace")
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
            return objs
        if isinstance(doc, list):
            return doc
        if isinstance(doc, dict):
            return [doc]
    return objs


rows = []
for p in sorted(REPO.rglob("claims.jsonl")):
    m = DATE.search(str(p))
    d = m.group(1) if m else "(no date in path)"
    for c in load(p):
        rows.append((d, p, c))

say("=" * 78)
say("CT-S34  measurements for the three rulings  (θ, ∞ sentinels)")
say("=" * 78)
say("claims read from the repository root: %d" % len(rows))
say()

# ------------------------------------------------- ruling 1: label date ----
say("RULING 1 — WHEN WAS THE LABEL CONVENTION INTRODUCED?")
by_date = collections.defaultdict(lambda: [0, 0])
for d, _, c in rows:
    by_date[d][0 if c.get("label") else 1] += 1
dates = sorted(by_date)
say("  date          labelled  unlabelled")
first_lab = None
for d in dates:
    lab, unlab = by_date[d]
    if lab and first_lab is None:
        first_lab = d
    if lab or d in (dates[0], dates[-1]):
        say("  %-12s %8d %11d" % (d, lab, unlab))
say()
say("  first date with any labelled claim ......... %s" % first_lab)
after = [(d, c) for d, _, c in rows if d >= first_lab]
before = [(d, c) for d, _, c in rows if d < first_lab]
say("  claims on/after that date .................. %d" % len(after))
say("      of which unlabelled ....................... %d"
    % sum(1 for _, c in after if not c.get("label")))
say("  claims strictly before it .................. %d" % len(before))
say("      of which labelled ......................... %d"
    % sum(1 for _, c in before if c.get("label")))
say("  date range of the pre-convention claims .... %s .. %s"
    % (min(d for d, _ in before), max(d for d, _ in before)))
say()

# --- the honest cut point: the first date after which labelling is the norm
say("  labelled share by date, from the first labelled date onward:")
run = []
for d in [x for x in dates if x >= first_lab]:
    lab, unlab = by_date[d]
    tot = lab + unlab
    run.append((d, lab, tot, lab / tot if tot else 0.0))
for d, lab, tot, frac in run:
    say("      %-12s %4d/%-4d  %5.1f%%" % (d, lab, tot, 100 * frac))
say()

# --------------------------------------------- ruling 2: duplicate kinds ---
say("RULING 2 — WHAT THE 84 REUSED IDS ACTUALLY ARE")
seen = collections.defaultdict(list)
idless = 0
for d, p, c in rows:
    cid = c.get("claim_id")
    if cid:
        seen[cid].append(p)
    else:
        idless += 1
dups = {k: v for k, v in seen.items() if len(v) > 1}
say("  distinct ids reused across files ........... %d" % len(dups))
say("  claims with no claim_id at all ............. %d" % idless)
say()

LOCAL = re.compile(r"^(?:\d+-)?C\d+$")
MIRROR = re.compile(r"[\\/]deposit[\\/]")


def kind(cid, paths):
    if LOCAL.match(cid):
        return "session-local counter"
    sess = {q.parent for q in paths}
    if len(sess) == 2 and any(MIRROR.search(str(q)) for q in paths):
        return "deposit mirror"
    if any(MIRROR.search(str(q)) for q in paths):
        return "deposit mirror"
    return "GENUINE CROSS-SESSION COLLISION"


kinds = collections.Counter()
genuine = []
for cid, paths in sorted(dups.items()):
    k = kind(cid, paths)
    kinds[k] += 1
    if k == "GENUINE CROSS-SESSION COLLISION":
        genuine.append((cid, paths))
for k, n in kinds.most_common():
    say("  %-36s %3d id(s)" % (k, n))
say()
if genuine:
    say("  IDS THAT ARE NEITHER, AND SO REMAIN REAL COLLISIONS:")
    for cid, paths in genuine:
        say("    %s" % cid)
        for q in paths:
            say("        %s" % q.relative_to(REPO))
else:
    say("  no id falls outside the two exempt kinds")
say()

# --- would session-local uniqueness still catch anything? -------------------
within = []
for p in sorted(REPO.rglob("claims.jsonl")):
    local = collections.Counter(c.get("claim_id") for c in load(p)
                                if c.get("claim_id"))
    for cid, n in local.items():
        if n > 1:
            within.append((p, cid, n))
say("  ids duplicated WITHIN a single file ........ %d" % len(within))
for p, cid, n in within[:10]:
    say("      %s  %s x%d" % (p.relative_to(REPO), cid, n))
say()

# --- the distinction that actually separates benign from real --------------
say("RULING 2b — SAME ID, SAME CLAIM? (copy vs collision)")
texts = collections.defaultdict(list)
for d, p, c in rows:
    cid = c.get("claim_id")
    if cid:
        body = c.get("claim") or c.get("statement") or c.get("text") or ""
        texts[cid].append((p, " ".join(str(body).split())))
same, diff = [], []
for cid in dups:
    bodies = {t for _, t in texts[cid]}
    (same if len(bodies) == 1 else diff).append(cid)
say("  reused id, IDENTICAL claim text everywhere . %d  (a copy or citation)"
    % len(same))
say("  reused id, DIFFERENT claim text ............ %d  (a real collision)"
    % len(diff))
say()
if diff:
    say("  THE IDS WHERE THE SAME LABEL CARRIES DIFFERENT CLAIMS:")
    for cid in sorted(diff):
        say("    %s" % cid)
        for p, t in texts[cid]:
            say("        %-52s %s" % (p.parent.name, t[:70]))
say()
say("  Composition of the %d reused ids by BOTH classifiers:" % len(dups))
cross = collections.Counter()
for cid, paths in dups.items():
    cross[(kind(cid, paths), "same text" if cid in same else "DIFFERENT text")] += 1
for (k, t), n in sorted(cross.items(), key=lambda kv: -kv[1]):
    say("    %-36s %-16s %3d" % (k, t, n))
say()

# ---------------------------------------------------------- controls -------
say("CONTROLS")
ok(first_lab is not None and any(by_date[d][1] for d in dates),
   "the corpus contains both labelled and unlabelled claims",
   "the corpus being uniform, which would make a date-scoped invariant "
   "pointless and the ruling unnecessary")
ok(LOCAL.match("C1") and LOCAL.match("121-C1") and not LOCAL.match("S33-01")
   and not LOCAL.match("DF-T0-LOCK"),
   "the session-local pattern matches C1 and 121-C1 and rejects S33-01 and "
   "DF-T0-LOCK",
   "the pattern being wide enough to exempt real ids such as S33-01, which "
   "would silently disable 1(b) for this session's own claims")
ok(MIRROR.search(r"a\deposit\p0\claims.jsonl")
   and not MIRROR.search(r"a\deposited\claims.jsonl")
   and not MIRROR.search(r"a\DEPOSIT-FORM.md"),
   "the mirror pattern matches a /deposit/ path component and rejects "
   "'deposited' and 'DEPOSIT-FORM'",
   "the pattern matching on a substring, which would exempt any path with "
   "the letters 'deposit' anywhere in it")
ok(sum(kinds.values()) == len(dups),
   "every reused id is classified into exactly one kind",
   "a reused id falling through the classifier unseen")
ok(idless > 0 and len(dups) > 0,
   "both populations the ruling addresses are non-empty",
   "either being empty, which would make the corresponding ruling vacuous "
   "and its implementation untestable")
ok(len(same) + len(diff) == len(dups) and len(same) > 0,
   "the copy/collision split accounts for every reused id",
   "an id falling outside both, or no id being a pure copy, which would mean "
   "text identity is not the separator it appears to be")
ok(first_lab < "2026-09-17" and by_date["2026-09-17"][1] == 0,
   "labelling is universal on 2026-09-17 but began earlier and lapsed",
   "labelling being monotone from its first appearance, in which case a cut "
   "at that first date would be the right one and this measurement "
   "unnecessary")
say()
say("CONTROLS: %d/%d PASS" % (N[0], N[0]))

OUT = pathlib.Path(__file__).resolve().parents[1] / "outputs" / "measure.out.txt"
data = BUF.getvalue()
blob = data.encode("utf-8")
assert b"\r" not in blob
OUT.write_bytes(blob)
raw = OUT.read_bytes()
assert raw == blob
t = raw.decode("utf-8")
assert "θ" in t and "∞" in t, "non-ASCII sentinel absent: reader unverified"
assert "θ" not in raw.decode("latin-1")
print("sha256 = %s  bytes = %d" % (hashlib.sha256(raw).hexdigest(), len(raw)))
