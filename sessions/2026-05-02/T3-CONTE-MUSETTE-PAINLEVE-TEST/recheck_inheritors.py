"""Re-derive consumers of the retracted V_quad P_III(D6) label.

Changes nothing. Prints the inheritor set with its as-of date.
Written 2026-09-13 by FILTRATION-NOGO; see README_catalog_d2_STATUS.md.
"""
import os, re, sys, datetime

ROOT = sys.argv[1] if len(sys.argv) > 1 else r"C:\LocalWork"
SKIP = {".git", "node_modules", "__pycache__", ".venv", "venv", ".mypy_cache"}
EXT  = (".md", ".tex", ".txt", ".py", ".json", ".jsonl", ".csv", ".yml", ".yaml")

LABEL  = re.compile(r"P[_\s-]*III\s*\(?\s*D[_\s]*6", re.I)
CTX    = re.compile(r"known_reduction|\bten\b.{0,40}famil|all\s*(10|ten)\b|"
                    r"10/10|10 of 10|conte[\s\-\u2013]*musette", re.I)
# 'necessary-criterion' is required: omitting it caused a false positive
CAVEAT = re.compile(r"necessar\w*[\s\-]*(condition|criterion|criteria)|not a proof|"
                    r"without independent confirmation|anchored case|CONJECTUR|"
                    r"retract|supersed|not sufficient|does not prove", re.I)

def main():
    bare, scanned = [], 0
    for dp, dns, fns in os.walk(ROOT):
        dns[:] = [x for x in dns if x not in SKIP]
        for fn in fns:
            if not fn.lower().endswith(EXT):
                continue
            p = os.path.join(dp, fn)
            try:
                t = open(p, encoding="utf-8", errors="replace").read()
            except OSError:
                continue
            scanned += 1
            if len(t) > 4_000_000:
                continue
            for m in LABEL.finditer(t):
                w = t[max(0, m.start() - 900): m.end() + 900]
                if not CTX.search(w):
                    continue
                if CAVEAT.search(w):
                    break
                bare.append((p, t[:m.start()].count("\n") + 1))
                break
    # control: the predicate must flag a bare line and spare a caveated one
    assert LABEL.search("P_III(D6) known_reduction") and \
           not CAVEAT.search("P_III(D6) known_reduction")
    assert CAVEAT.search("necessary-criterion"), "regression: hyphenated form"
    print("as-of:", datetime.date.today().isoformat(), "| root:", ROOT,
          "| files scanned:", scanned)
    print("inheritors carrying the label without caveat or retraction note:",
          len(bare))
    for p, ln in sorted(bare):
        print("   ", p, ":", ln)
    print("\nRead every hit before treating this count as a finding.")

if __name__ == "__main__":
    main()
