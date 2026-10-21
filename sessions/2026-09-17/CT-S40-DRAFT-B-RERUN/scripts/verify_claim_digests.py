"""verify_claim_digests.py -- every digest cited in claims.jsonl must resolve
to a file on disk in this session, AND the gate outputs must be stable.

The second half exists because outputs/draft_check.out.txt is produced by
WALKING the corpus that claims.jsonl is written into.  A gate re-run after
emission can change that file and leave the claims citing a digest that
resolves to nothing.  Here the gates are re-run and required to reproduce the
bytes the claims cite.
"""
import hashlib, json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent.parent
CLAIMS = HERE / "claims.jsonl"

raw = CLAIMS.read_bytes()
if not raw.strip():
    print("READER INTEGRITY FAILED: claims.jsonl is empty")
    sys.exit(2)
records = [json.loads(l) for l in raw.decode("utf-8").splitlines() if l.strip()]
if len(records) < 5:
    print("READER INTEGRITY FAILED: only %d records read" % len(records))
    sys.exit(2)

on_disk = {}
for p in HERE.rglob("*"):
    if p.is_file() and ".git" not in p.parts:
        on_disk.setdefault(hashlib.sha256(p.read_bytes()).hexdigest(),
                           []).append(str(p.relative_to(HERE)))

bad = 0
print("[cited digests]")
for r in records:
    h = r["output_hash"]
    hits = on_disk.get(h, [])
    if not hits:
        bad += 1
        print("  BROKEN  %-9s cites %s... matches 0 files"
              % (r["claim_id"], h[:16]))
    else:
        print("  ok      %-9s %s... -> %s" % (r["claim_id"], h[:16], hits[0]))

print("\n[gate output stability]")
gates = [("scripts/draft_check.py", "outputs/draft_check.out.txt", 0),
         ("scripts/mutants_draft_check.py",
          "outputs/mutants_draft_check.out.txt", 0)]
for script, out, exp in gates:
    before = (HERE / out).read_bytes()
    r = subprocess.run([sys.executable, str(HERE / script)],
                       capture_output=True, text=True, encoding="utf-8",
                       errors="replace")
    now = ((r.stdout or "") + (r.stderr or "")).replace("\r\n", "\n")
    same = now.encode("utf-8") == before.decode("utf-8").replace(
        "\r\n", "\n").encode("utf-8")
    if not same or r.returncode != exp:
        bad += 1
        print("  UNSTABLE %s (rc=%s, bytes match=%s)" % (script, r.returncode,
                                                         same))
    else:
        print("  stable   %s rc=%s, output reproduces the cited bytes"
              % (script, r.returncode))

print("\nVERDICT: %s (%d problems)" % ("PASS" if bad == 0 else "FAIL", bad))
sys.exit(0 if bad == 0 else 1)
