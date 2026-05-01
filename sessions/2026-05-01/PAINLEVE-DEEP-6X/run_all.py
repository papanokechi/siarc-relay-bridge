"""Run all 6 family deep probes sequentially at production precision."""
import json, subprocess, sys, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
PY = str(Path(__file__).resolve().parents[3] / ".venv" / "Scripts" / "python.exe")

# Order: V_quad first (cross-validation), then by ascending |Delta|.
SCRIPTS = [
    "vquad_painleve_deep.py",
    "ql01_painleve_deep.py",
    "ql02_painleve_deep.py",
    "ql06_painleve_deep.py",
    "ql15_painleve_deep.py",
    "ql26_painleve_deep.py",
]

def main():
    t_outer = time.time()
    for s in SCRIPTS:
        log = HERE / (s.replace(".py", ".log"))
        print(f"\n[run_all] launching {s} -> {log.name}", flush=True)
        t0 = time.time()
        with open(log, "w", encoding="utf-8") as f:
            r = subprocess.run([PY, str(HERE / s)], cwd=str(HERE),
                               stdout=f, stderr=subprocess.STDOUT)
        dt = time.time() - t0
        print(f"[run_all] {s} exit={r.returncode}  ({dt:.1f}s)", flush=True)
    print(f"\n[run_all] total {time.time()-t_outer:.1f}s")

if __name__ == "__main__":
    main()
