"""Compute SHA-256 hashes of all session deliverables for claims.jsonl."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).parent
FILES = [
    "verify_vquad_ode.py",
    "verify_vquad_ode.log",
    "vquad_hamiltonian.tex",
    "pIII_canonical.tex",
    "phi_change_of_variables.tex",
    "canonical_S_zeta_star.txt",
    "literature_crosscheck.md",
]


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    out: dict[str, str] = {}
    for name in FILES:
        p = HERE / name
        if p.exists():
            out[name] = sha256(p)
        else:
            out[name] = "MISSING"
    (HERE / "_hashes.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
    for k, v in out.items():
        print(f"{v}  {k}")


if __name__ == "__main__":
    main()
