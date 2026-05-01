"""Build claims.jsonl with sha256 hashes of the result JSONs."""
import json, hashlib
from pathlib import Path

HERE = Path(__file__).resolve().parent

def sha(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()

CLAIMS = []

def add(claim, dps, script, output_path):
    CLAIMS.append({
        "claim": claim,
        "evidence_type": "computation",
        "dps": dps,
        "reproducible": True,
        "script": script,
        "output_hash": sha(HERE / output_path),
    })

# per-family claims
add("V_quad PAINLEVE-DEEP at depth=3000 dps=400 yields D-A + P-III residual 4.5895e-5 (MARGINAL, h-independent across h in {0.1,0.05,0.025} to <=6e-6 decimal orders); pipeline does NOT recover known P-III(D6) (1/6,0,0,-1/2) at <=1e-20.",
    400, "vquad_painleve_deep.py", "vquad_result.json")
add("QL01 PAINLEVE-DEEP residual 0.0084 (D-A + P-III, NO_FIT); h-spread <=9e-6 decimal orders confirms genuine ansatz misfit not numerical artefact; cold scan over {P-III,P-V,P-VI,P-II,P-IV} found nothing < 1e-4.",
    400, "ql01_painleve_deep.py", "ql01_result.json")
add("QL02 PAINLEVE-DEEP residual 9.389e-4 (D-A + P-III, NO_FIT); h-spread <=2e-6 decimal orders; Session B/C residual essentially unchanged (no improvement at higher precision => rules out P-III, P-V, P-VI, P-II, P-IV at design points).",
    400, "ql02_painleve_deep.py", "ql02_result.json")
add("QL06 PAINLEVE-DEEP residual 1.0635e-4 (D-A + P-V, NO_FIT) at depth=3000 dps=400, best h=0.025; Session C residual 1.0660e-4 -> 1.0635e-4 (drop 0.001 decimal orders) confirms residual is NOT shrinking with precision; cold scan over {P-III,P-V,P-VI,P-II,P-IV} found no improvement.",
    400, "ql06_painleve_deep.py", "ql06_result.json")
add("QL15 PAINLEVE-DEEP residual 0.01873 (D-A + P-III, NO_FIT); h-independent; cold scan over {P-III,P-V,P-VI,P-II,P-IV} found nothing < 1e-4.",
    400, "ql15_painleve_deep.py", "ql15_result.json")
add("QL26 PAINLEVE-DEEP residual 0.024 (D-A + P-III, NO_FIT); fitted P-III delta diverges to -7.13 (not a small rational); cold scan over {P-III,P-V,P-VI,P-II,P-IV} found nothing < 1e-4.",
    400, "ql26_painleve_deep.py", "ql26_result.json")
# omnibus
add("PAINLEVE-DEEP-6X omnibus: 0/6 families admit a Painleve reduction (P-II/P-III/P-V/P-VI/P-IV) at residual <= 1e-4 under the recurrence-parameter deformation L(t) at depth=3000 dps=400 with h-independent 5-pt stencils; V_quad MARGINAL at 4.59e-5 (does not recover known P-III(D6) parameters); FLAG: V_QUAD ANOMALOUS -- Conjecture A part (iv) does NOT extend to a structural family pattern via L(t) deformation.",
    400, "aggregate.py", "summary.json")

with open(HERE / "claims.jsonl", "w", encoding="utf-8") as f:
    for c in CLAIMS:
        f.write(json.dumps(c) + "\n")
print(f"wrote {len(CLAIMS)} claims")
