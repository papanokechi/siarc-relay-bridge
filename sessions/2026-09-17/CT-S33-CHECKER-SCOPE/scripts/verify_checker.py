"""Controls on check_invariants.py itself.

A checker that never fails is indistinguishable from a checker that cannot.
The widened pass reports three failures; these controls establish that the
failures are caused by the corpus and not by the checker, and that a clean
corpus still passes.

Method: the checker's source is read, its ROOTS and EXCLUDE literals are
text-substituted for a synthetic temporary corpus, and the patched copy is run
as a subprocess.  Nothing in the real corpus is touched, and the real checker
file is verified byte-identical afterwards.
"""
import hashlib
import io
import json
import pathlib
import subprocess
import sys
import tempfile

sys.stdout.reconfigure(encoding="utf-8")

HERE = pathlib.Path(__file__).resolve().parents[1]
CHECKER = HERE.parent / "CT-R1-AUDIT" / "check_invariants.py"
OLD = HERE / "refs" / "check_invariants.pre-S33.py"
SRC = CHECKER.read_text(encoding="utf-8")
SRC_HASH = hashlib.sha256(CHECKER.read_bytes()).hexdigest()

ROOTS_LIT = 'ROOTS = [\n    REPO,\n    pathlib.Path(r"C:\\LocalWork\\SCOPE"),\n]'
assert ROOTS_LIT in SRC, "ROOTS literal not found; the patch target moved"
EXC_HEAD = "EXCLUDE = {\n"
assert EXC_HEAD in SRC
EXC_TAIL = SRC.index("}\n", SRC.index(EXC_HEAD)) + 2
EXC_LIT = SRC[SRC.index(EXC_HEAD):EXC_TAIL]

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


GOOD = [
    {"claim_id": "X-01", "label": "PROVEN", "evidence_type": "computation",
     "claim": "a", "review": "self", "review_note": "n"},
    {"claim_id": "X-02", "label": "VERIFIED", "claim": "b"},
]


def run_on(tmp, rows_by_file, exclude=None, raw=None):
    """Write a synthetic corpus under tmp and run a patched checker on it."""
    corpus = tmp / "corpus"
    for rel, rows in rows_by_file.items():
        p = corpus / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("".join(json.dumps(r) + "\n" for r in rows),
                     encoding="utf-8", newline="")
    for rel, blob in (raw or {}).items():
        p = corpus / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(blob)

    new_roots = "ROOTS = [\n    pathlib.Path(r%r),\n]" % str(corpus)
    new_exc = "EXCLUDE = {\n"
    for e in (exclude or []):
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
say("CT-S33  controls on check_invariants.py  (θ, ∞ sentinels)")
say("=" * 78)
say("checker under test: %s" % CHECKER)
say("sha256            : %s" % SRC_HASH)
say()

say("A. HONESTY OF THE DOCSTRING")
doc = SRC[:SRC.index('"""', 3) + 3]
ok("ROOTS" in doc and "EXCLUDE" in doc,
   "the docstring names the two constants that fix its scope",
   "the docstring describing a coverage the code does not have, which is what "
   "let the narrowed scope run undetected")
olddoc = OLD.read_text(encoding="utf-8")
ok("the whole session corpus" in olddoc and "parents[1]" in olddoc,
   "the preserved predecessor does claim 'the whole session corpus' while "
   "rooting at parents[1]",
   "the predecessor not having the defect, which would make this session's "
   "premise wrong")
PHRASE = "the whole session corpus"
ok(doc.count(PHRASE) == 1 and ('claimed coverage of "%s"' % PHRASE) in doc,
   "the new docstring mentions that phrase exactly once, and only inside the "
   "quotation describing the old defect",
   "the phrase appearing anywhere it could be read as an assertion. NOTE: an "
   "earlier form of this control tested `PHRASE not in doc` and fired on the "
   "historical quotation -- a control inventing a defect in correct prose")
say()

say("B. THE SCOPE IS PRINTED, NOT IMPLIED")
art = (HERE / "outputs" / "widened_pass.out.txt").read_text(
    encoding="utf-8", errors="replace")
for needle, what in ((r"C:\LocalWork\siarc-relay-bridge", "repo root"),
                     (r"C:\LocalWork\SCOPE", "SCOPE root"),
                     ("CT-S31-COLDREAD-ROWS", "the stand-down exclusion"),
                     ("input fingerprint:", "the input fingerprint"),
                     ("scope of that verdict:", "the scope of the verdict")):
    ok(needle in art, "the run prints %s" % what,
       "the output omitting it, leaving a reader to infer scope from a "
       "docstring again")
say()

say("C. SENSITIVITY — a clean corpus passes, each injected defect fails")
with tempfile.TemporaryDirectory() as td:
    tmp = pathlib.Path(td)

    rc, out = run_on(tmp / "clean", {"s1/claims.jsonl": GOOD})
    ok(rc == 0 and "INVARIANTS OK" in out,
       "a clean synthetic corpus passes (exit 0)",
       "the checker failing unconditionally, which would make the three real "
       "failures uninformative")

    rc, out = run_on(tmp / "dup", {"s1/claims.jsonl": GOOD,
                                   "s2/claims.jsonl": [dict(GOOD[0])]})
    ok(rc == 1 and "FAIL 1(b)" in out and "X-01" in out,
       "a claim_id reused across two files fails 1(b)",
       "1(b) not noticing a reuse, which is exactly the real 84-id finding")

    bad = [dict(GOOD[0], label="PROCEED")]
    rc, out = run_on(tmp / "lab", {"s1/claims.jsonl": bad})
    ok(rc == 1 and "FAIL 2" in out and "PROCEED" in out,
       "an unrecognised label fails 2",
       "2 accepting any string, which would void the real 3488-claim finding")

    nn = [{"claim_id": "Y", "label": "PROVEN", "review": "self"}]
    rc, out = run_on(tmp / "note", {"s1/claims.jsonl": nn})
    ok(rc == 1 and "FAIL 3" in out,
       "review without review_note fails 3",
       "3 being vacuous, which matters because 3 PASSED on the real corpus")

    rv = [{"claim_id": "Y", "label": "PROVEN", "review": "hearsay",
           "review_note": "n"}]
    rc, out = run_on(tmp / "rev", {"s1/claims.jsonl": rv})
    ok(rc == 1 and "FAIL 4" in out,
       "an unrecognised review value fails 4",
       "4 being vacuous, which matters because 4 PASSED on the real corpus")

    pf = [{"claim_id": "Y", "label": "PROVEN",
           "evidence_type": "file_inspection"}]
    rc, out = run_on(tmp / "fi", {"s1/claims.jsonl": pf})
    ok(rc == 1 and "FAIL 1(a)" in out,
       "PROVEN on file_inspection fails 1(a)",
       "1(a) being vacuous, which matters because 1(a) PASSED on the real "
       "corpus")

    rc, out = run_on(tmp / "bom", {},
                     raw={"s1/claims.jsonl":
                          b"\xef\xbb\xbf" + json.dumps(GOOD[1]).encode() + b"\n"})
    ok(rc == 1 and "FAIL 5" in out and "BOM" in out
       and "1 claims in 1 files" in out,
       "a BOM fails 5 and the claim behind it is still read",
       "the BOM either passing unnoticed or costing the claim")

    rc, out = run_on(tmp / "arr", {},
                     raw={"s1/claims.jsonl": json.dumps(GOOD, indent=2).encode()})
    ok(rc == 1 and "WRONG CONTAINER" in out and "2 claims in 1 files" in out,
       "a JSON array fails 5 and both claims are still read",
       "the wrong container costing claims, which is the truncation "
       "hypothesis the survey found unsupported")

    rc, out = run_on(tmp / "dmg", {},
                     raw={"s1/claims.jsonl": b'{"a":"\\(x\\)"}\n'})
    ok(rc == 1 and "DAMAGED LINE" in out,
       "a bad backslash escape is reported as a DAMAGED LINE",
       "the single genuinely damaged line in the corpus going unreported")

    rc, out = run_on(tmp / "many", {"s1/claims.jsonl": GOOD,
                                    "s2/claims.jsonl": GOOD},
                     exclude=["s2"])
    ok(rc == 0 and "2 claims in 1 files" in out and "EXCLUDED" in out,
       "an EXCLUDE entry prunes its folder and is printed",
       "the exclusion being ignored, which would breach the stand-down, or "
       "being silent, which would hide a hole in the check")

say()
say("D. THE PREDECESSOR'S SCOPE, MEASURED")
old_root = CHECKER.parent.parent            # sessions/2026-09-17
n_old = len(list(old_root.rglob("claims.jsonl")))
n_new = art.count("claims.jsonl") or 0
tot = int(art.split("corpus: ")[1].split(" claims in ")[1].split(" files")[0])
say("  files under sessions/2026-09-17 (the old root) .. %d" % n_old)
say("  files under the declared roots now .............. %d" % tot)
ok(n_old < tot / 10,
   "the old root reached under a tenth of the files now reached",
   "the widening being immaterial, i.e. the reported coverage gap not being "
   "real")
say()

ok(hashlib.sha256(CHECKER.read_bytes()).hexdigest() == SRC_HASH,
   "the real checker is byte-identical after all controls",
   "a control having written to the file under test")
say()
say("CONTROLS: %d/%d PASS" % (N[0], N[0]))

OUT = HERE / "outputs" / "verify_checker.out.txt"
data = BUF.getvalue()
OUT.write_text(data, encoding="utf-8", newline="")
raw = OUT.read_bytes()
assert b"\r\n" not in raw
t = raw.decode("utf-8")
assert "θ" in t and "∞" in t, "non-ASCII sentinel absent: reader unverified"
assert "θ" not in raw.decode("latin-1")
assert t == data
print("sha256 = %s  bytes = %d" % (hashlib.sha256(raw).hexdigest(), len(raw)))
