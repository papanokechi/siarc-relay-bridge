"""Run all Borel-channel probes + V_quad K-scan + aggregate."""
import subprocess, sys
from pathlib import Path
D = Path(__file__).parent
PY = sys.executable

scripts = [
    "v_quad_borel_validation.py",
    "ql01_borel.py",
    "ql02_borel.py",
    "ql06_borel.py",
    "ql15_borel.py",
    "ql26_borel.py",
    "v_quad_kscan.py",
    "aggregate.py",
]
for s in scripts:
    print(f"\n### Running {s} ###")
    r = subprocess.run([PY, str(D / s)], cwd=D.parent.parent.parent)
    if r.returncode != 0:
        print(f"  -> FAILED rc={r.returncode}")
print("\nrun_all complete.")
