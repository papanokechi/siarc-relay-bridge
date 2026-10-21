"""Controls on the four rulings, each able to fail.

The rulings are scoping changes. A scoping change that cannot be distinguished
from a loosening is worthless, so every exemption introduced here gets a
mutant that must still be caught:

  ruling 1  a claim dated one day BEFORE the cutoff (must be a hole) and one
            dated one day AFTER (must FAIL invariant 2)
  ruling 2  a genuine global collision; a counter reused WITHIN one session;
            a mirror that is not at the mirror path
  ruling 3  the known unreadable line reported as a KNOWN HOLE, and a second
            damaged line reported as NEW DAMAGE
  ruling 4  SCOPE absent from the walk, present in EXCLUDE, named in holes

Method: the checker's source is read, ROOTS and EXCLUDE are text-substituted
for a synthetic temporary corpus, and the patched copy runs as a subprocess.
Nothing real is touched; the real checker is hashed before and after.
"""
import hashlib
import io
import json
import pathlib
import re
import subprocess
import sys
import tempfile

sys.stdout.reconfigure(encoding="utf-8")

HERE = pathlib.Path(__file__).resolve().parents[1]
CHECKER = HERE.parent / "CT-R1-AUDIT" / "check_invariants.py"
OLD = HERE / "refs" / "check_invariants.pre-S34.py"
SRC = CHECKER.read_text(encoding="utf-8")
SRC_HASH = hashlib.sha256(CHECKER.read_bytes()).hexdigest()

ROOTS_LIT = "ROOTS = [\n    REPO,\n]"
assert ROOTS_LIT in SRC, "ROOTS literal not found; the patch target moved"
EXC_HEAD = "EXCLUDE = {\n"
EXC_LIT = SRC[SRC.index(EXC_HEAD):SRC.index("}\n", SRC.index(EXC_HEAD)) + 2]
CUTOFF = re.search(r'CONVENTION_DATE = "(\d{4}-\d{2}-\d{2})"', SRC).group(1)

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


def C(cid, label="PROVEN", body="a body", **kw):
    d = {"claim_id": cid, "label": label, "claim": body,
         "evidence_type": "computation"}
    d.update(kw)
    return d


def run_on(tmp, files, exclude=()):
    """files: {relpath: [claim dicts] or bytes}. relpath must contain a date."""
    corpus = tmp / "corpus"
    for rel, rows in files.items():
        p = corpus / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(rows, bytes):
            p.write_bytes(rows)
        else:
            p.write_bytes("".join(json.dumps(r) + "\n"
                                  for r in rows).encode("utf-8"))
    new_roots = "ROOTS = [\n    pathlib.Path(r%r),\n]" % str(corpus)
    new_exc = "EXCLUDE = {\n"
    for e in exclude:
        new_exc += "    pathlib.Path(r%r): 'synthetic control',\n" % str(corpus / e)
    new_exc += "}\n"
    patched = SRC.replace(ROOTS_LIT, new_roots).replace(EXC_LIT, new_exc)
    assert new_roots in patched and "C:\\LocalWork\\SCOPE" not in patched, \
        "patch did not take; the control would have run on the REAL corpus"
    deep = tmp / "a" / "b" / "c"
    deep.mkdir(parents=True, exist_ok=True)
    f = deep / "check.py"
    f.write_text(patched, encoding="utf-8")
    r = subprocess.run([sys.executable, str(f)], capture_output=True,
                       text=True, encoding="utf-8", errors="replace")
    return r.returncode, (r.stdout or "") + (r.stderr or "")


say("=" * 78)
say("CT-S34  controls on the four rulings  (θ, ∞ sentinels)")
say("=" * 78)
say("checker under test: %s" % CHECKER)
say("sha256            : %s" % SRC_HASH)
say("predecessor kept  : %s" % hashlib.sha256(OLD.read_bytes()).hexdigest())
say()

art = (HERE / "outputs" / "rulings_pass.out.txt").read_text(
    encoding="utf-8", errors="replace")

with tempfile.TemporaryDirectory() as td:
    tmp = pathlib.Path(td)

    # ---- ruling 1: the cutoff, one day either side ------------------------
    say("RULING 1 — INVARIANT 2 SCOPED TO THE LABEL CONVENTION")
    rc, out = run_on(tmp / "r1a", {
        "sessions/2026-09-16/OLD/claims.jsonl": [C("A-1", label=None)],
        "sessions/2026-09-18/NEW/claims.jsonl": [C("A-2")],
    })
    ok(rc == 0 and "OUT OF SCOPE" in out and "1 claim(s) dated before" in out,
       "an unlabelled claim dated one day BEFORE the cutoff is a hole, not a "
       "failure",
       "invariant 2 judging claims written before the convention existed, "
       "which is what the ruling forbids")

    rc, out = run_on(tmp / "r1b", {
        "sessions/2026-09-18/NEW/claims.jsonl": [C("A-2", label=None)],
    })
    ok(rc == 1 and "FAIL 2" in out and CUTOFF in out,
       "an unlabelled claim dated one day AFTER the cutoff FAILS invariant 2",
       "the scoping having disarmed invariant 2 altogether, i.e. a scoping "
       "change that is really a loosening")

    rc, out = run_on(tmp / "r1c", {
        "sessions/2026-09-17/ON/claims.jsonl": [C("A-3", label=None)],
    })
    ok(rc == 1 and "FAIL 2" in out,
       "the cutoff is inclusive: a claim dated ON the cutoff is in scope",
       "an off-by-one at the boundary, leaving the cutoff date itself "
       "unchecked")

    ok("invariant 2 cutoff (pinned): %s" % CUTOFF in art,
       "the real run prints the cutoff date",
       "the cutoff being applied without being visible in the output")
    say()

    # ---- ruling 2: the three-way split ------------------------------------
    say("RULING 2 — INVARIANT 1(b) SPLIT THREE WAYS")
    rc, out = run_on(tmp / "r2a", {
        "sessions/2026-09-18/S1/claims.jsonl": [C("X-9", body="first")],
        "sessions/2026-09-18/S2/claims.jsonl": [C("X-9", body="second")],
    })
    ok(rc == 1 and "FAIL 1(b)(i)" in out and "DIFFERENT claim text" in out,
       "a genuine global collision still FAILS 1(b)(i) and is named a true "
       "collision",
       "the split having exempted ordinary ids, which would make 1(b) "
       "unable to catch the thing it exists for")

    rc, out = run_on(tmp / "r2b", {
        "sessions/2026-09-18/S1/claims.jsonl": [C("C1", body="one"),
                                                C("C1", body="two")],
    })
    ok(rc == 1 and "FAIL 1(b)(ii)" in out and "C1 x2" in out,
       "a session-local counter reused WITHIN one session FAILS 1(b)(ii)",
       "session-local scoping being read as 'never checked', which would let "
       "a session collide with itself")

    rc, out = run_on(tmp / "r2c", {
        "sessions/2026-09-18/S1/claims.jsonl": [C("C1", body="one")],
        "sessions/2026-09-18/S2/claims.jsonl": [C("C1", body="two")],
    })
    ok(rc == 0 and "session-local counter id(s)" in out,
       "the same counter in TWO sessions is exempt from global uniqueness",
       "the exemption not applying, which would re-flag the 10 counters the "
       "ruling exempts")

    rc, out = run_on(tmp / "r2d", {
        "sessions/2026-06-11/A/deposit/p0/claims.jsonl": [C("DF-1", body="m")],
        "sessions/2026-06-11/A-SOURCE/claims.jsonl": [C("DF-1", body="m")],
    })
    ok(rc == 0 and "exempt as deposit mirrors" in out and "DF-1" in out,
       "a mirror AT the deposit path is exempt and is listed with the pattern "
       "that matched",
       "the mirror exemption being silent, which would hide a hole in the "
       "check")

    rc, out = run_on(tmp / "r2e", {
        "sessions/2026-06-11/A/mirror/p0/claims.jsonl": [C("DF-2", body="m")],
        "sessions/2026-06-11/A-SOURCE/claims.jsonl": [C("DF-2", body="m")],
    })
    ok(rc == 1 and "FAIL 1(b)(i)" in out and "DF-2" in out,
       "a mirror NOT at the deposit path is still reported — identical text "
       "is not an exemption",
       "text identity having been accepted as an exemption, which would "
       "absorb the 59 restatements without a ruling")

    rc, out = run_on(tmp / "r2f", {
        "sessions/2026-09-18/S1/claims.jsonl": [
            {"label": "PROVEN", "claim": "no id here",
             "evidence_type": "computation"}],
    })
    ok(rc == 0 and "1(b)(iii): 1 claim(s) carry no claim_id" in out
       and "This is a hole, not a pass" in out,
       "an idless claim gets its own printed line and is called a hole",
       "idless claims sitting silently outside 1(b), which is how 2641 of "
       "them went unremarked")

    for needle, what in (("1(b)(iii): 2641", "the idless count"),
                         ("exempt as deposit mirrors, pattern", "the mirror pattern"),
                         ("^(?:\\d+-)?C\\d+$", "the counter pattern")):
        ok(needle in art, "the real run prints %s" % what,
           "an exemption being applied without its pattern being printed")
    say()

    # ---- ruling 3: the known hole -----------------------------------------
    say("RULING 3 — THE UNREADABLE CLAIM LEFT UNREPAIRED")
    ok("KNOWN HOLE" in art
       and "sessions/2026-04-30/SIARC-COHERENCE-AUDIT/claims.jsonl:3" in
       art.replace("\\", "/"),
       "the real run names the known hole by path and line",
       "the damaged line being reported without being identified, or being "
       "silently tolerated")

    rc, out = run_on(tmp / "r3", {
        "sessions/2026-09-18/S1/claims.jsonl": b'{"a":"\\(x\\)"}\n'})
    ok(rc == 1 and "NEW DAMAGE" in out and "KNOWN HOLE" not in out,
       "a DIFFERENT damaged line is reported as NEW DAMAGE, not absorbed by "
       "the known-hole entry",
       "the known-hole list being a blanket amnesty for any damage, which "
       "would hide the next truncation")
    say()

    # ---- ruling 4: SCOPE out of ROOTS -------------------------------------
    say("RULING 4 — SCOPE REMOVED FROM ROOTS")
    ok("C:\\LocalWork\\SCOPE" not in art.split("input fingerprint")[0]
       .split("EXCLUDED")[0],
       "SCOPE is not among the walked roots",
       "SCOPE still being walked, leaving the race and the stand-down inside "
       "the verdict")
    ok("EXCLUDED C:\\LocalWork\\SCOPE" in art
       and "Window B" in art and "race in it" in art,
       "SCOPE appears in EXCLUDE with all three reasons printed",
       "the removal being undocumented, so nobody could tell what would have "
       "to be settled to restore it")
    ok("not walked at all: C:\\LocalWork\\SCOPE" in art,
       "SCOPE is named on the holes line",
       "the exclusion being invisible in the verdict summary")
    ok("input fingerprint:" in art,
       "the input fingerprint is kept",
       "the fingerprint being dropped along with the live root it was "
       "introduced for")

    # The fingerprint is only useful if it is printed on EVERY run, including
    # the runs you would least expect to compare: a failing one and an empty
    # one. Two runs cannot be reconciled if one of them printed nothing.
    rc, out = run_on(tmp / "r4a", {
        "sessions/2026-09-18/S1/claims.jsonl": [C("A-9", label=None)],
    })
    ok(rc == 1 and "input fingerprint:" in out,
       "the fingerprint is printed on a FAILING run, not only a passing one",
       "the fingerprint sitting after an early exit, so the one run you most "
       "need to reconcile is the one that printed no fingerprint")

    rc, out = run_on(tmp / "r4b", {"sessions/2026-09-18/S1/notes.md": b"x\n"})
    ok("input fingerprint:" in out and "over 0 file(s) read" in out,
       "the fingerprint is printed over an EMPTY corpus, stating 0 files",
       "an empty read being silently indistinguishable from a read that "
       "found nothing wrong")

    fp = [l for l in art.splitlines() if l.startswith("input fingerprint:")]
    ok(len(fp) == 1 and len(fp[0].split()[2]) == 64,
       "the real run prints exactly one full 64-hex fingerprint",
       "a truncated or duplicated fingerprint, which cannot be compared "
       "between runs")
    say()

ok(hashlib.sha256(CHECKER.read_bytes()).hexdigest() == SRC_HASH,
   "the real checker is byte-identical after all controls",
   "a control having written to the file under test")
say()
say("CONTROLS: %d/%d PASS" % (N[0], N[0]))

OUT = HERE / "outputs" / "verify_rulings.out.txt"
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
