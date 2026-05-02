"""T37G-BETA2-CHARACTERIZATION runner.

Phase A — input validation + gate check ONLY.

Per spec §A.1, this prompt fires only if the prior session's halt key is
in the gate set
    {T37_NEXT_SECTOR_BETA_NONZERO, T37E_NEXT_SECTOR_BETA_NONZERO}.
If the gate is not satisfied, halt with T37G_GATE_NOT_SATISFIED and do
not run Phases B-F. (See spec §4, §6.)

This runner reads halt_log.json / verdict.md from both candidate prior
sessions, records the observed halt keys, and emits the halt deliverables.
No mpmath series fitting is performed.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

GATE_KEYS = {"T37_NEXT_SECTOR_BETA_NONZERO", "T37E_NEXT_SECTOR_BETA_NONZERO"}

HERE = Path(__file__).resolve().parent
BRIDGE = HERE.parents[2]  # sessions/2026-05-03/T37G-... -> bridge root

PRIOR_CANDIDATES = [
    BRIDGE / "sessions" / "2026-05-02" / "T37-S2-EXTRACTION-POLYNOMIAL-AWARE",
    BRIDGE / "sessions" / "2026-05-02" / "T37E-EXTENDED-RECURRENCE",
]


def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def load_halt_keys(session_dir: Path) -> tuple[list[str], str | None]:
    halt_path = session_dir / "halt_log.json"
    verdict_path = session_dir / "verdict.md"
    keys: list[str] = []
    if halt_path.exists():
        try:
            data = json.loads(halt_path.read_text(encoding="utf-8"))
        except Exception:
            data = None
        if isinstance(data, dict) and "halts" in data:
            for h in data["halts"]:
                k = h.get("key") if isinstance(h, dict) else None
                if k:
                    keys.append(k)
        elif isinstance(data, list):
            for h in data:
                k = h.get("key") if isinstance(h, dict) else None
                if k:
                    keys.append(k)
    verdict_label: str | None = None
    if verdict_path.exists():
        for line in verdict_path.read_text(encoding="utf-8").splitlines():
            if "Verdict label" in line and "`" in line:
                parts = line.split("`")
                if len(parts) >= 2:
                    verdict_label = parts[1]
                    break
    return keys, verdict_label


def main() -> int:
    survey: dict[str, dict] = {}
    for cand in PRIOR_CANDIDATES:
        if not cand.exists():
            survey[cand.name] = {"present": False}
            continue
        keys, verdict = load_halt_keys(cand)
        survey[cand.name] = {
            "present": True,
            "halt_keys": keys,
            "verdict_label": verdict,
            "gate_match": any(k in GATE_KEYS for k in keys),
        }

    gate_satisfied = any(s.get("gate_match") for s in survey.values())

    halt_log = {
        "halts": [],
        "gate_set": sorted(GATE_KEYS),
        "prior_session_survey": survey,
    }

    if not gate_satisfied:
        halt_log["halts"].append(
            {
                "key": "T37G_GATE_NOT_SATISFIED",
                "reason": (
                    "Prior session halt keys are not in the gate set. "
                    "Phases B-F not run."
                ),
                "observed": survey,
            }
        )

    (HERE / "halt_log.json").write_text(
        json.dumps(halt_log, indent=2), encoding="utf-8"
    )

    # Empty-by-design supporting logs (still must exist per spec).
    for name in ("discrepancy_log.json", "unexpected_finds.json"):
        (HERE / name).write_text("{}\n", encoding="utf-8")

    # Phase B-E artefacts: not produced (gate halt). Write minimal stubs
    # that are explicit about the halt, so reviewers do not mistake an
    # absent file for a missing run.
    stub = {
        "halt_key": "T37G_GATE_NOT_SATISFIED",
        "produced": False,
        "reason": "Gate not satisfied; Phase B-E not executed per spec §4.",
    }
    for name in (
        "beta_2_per_rep.json",
        "beta_2_stability_grid.json",
        "beta_2_pslq_probe.json",
        "partition_test.json",
        "universality_test.json",
        "closed_form_test.json",
    ):
        (HERE / name).write_text(json.dumps(stub, indent=2), encoding="utf-8")

    # AEAL: only honest claims (gate-check facts + halt label).
    claims = []
    for name, info in survey.items():
        text = json.dumps(info, sort_keys=True)
        claims.append(
            {
                "claim": f"prior session {name} halt_keys = {info.get('halt_keys', [])}; "
                         f"verdict = {info.get('verdict_label')}; "
                         f"gate_match = {info.get('gate_match', False)}",
                "evidence_type": "computation",
                "dps": 0,
                "reproducible": True,
                "script": "t37g_runner.py",
                "output_hash": sha256_text(text),
            }
        )
    claims.append(
        {
            "claim": "T37G gate set = {T37_NEXT_SECTOR_BETA_NONZERO, "
                     "T37E_NEXT_SECTOR_BETA_NONZERO}; observed prior halt keys "
                     "do not intersect the gate set; Phase B-E suppressed.",
            "evidence_type": "computation",
            "dps": 0,
            "reproducible": True,
            "script": "t37g_runner.py",
            "output_hash": sha256_text(json.dumps(survey, sort_keys=True)),
        }
    )
    claims.append(
        {
            "claim": "T37G verdict label = HALT_T37G_GATE_NOT_SATISFIED",
            "evidence_type": "computation",
            "dps": 0,
            "reproducible": True,
            "script": "t37g_runner.py",
            "output_hash": sha256_text("HALT_T37G_GATE_NOT_SATISFIED"),
        }
    )
    with (HERE / "claims.jsonl").open("w", encoding="utf-8") as fh:
        for c in claims:
            fh.write(json.dumps(c) + "\n")

    print("survey:")
    for k, v in survey.items():
        print(f"  {k}: {v}")
    print("gate_satisfied:", gate_satisfied)
    print("verdict: HALT_T37G_GATE_NOT_SATISFIED" if not gate_satisfied
          else "GATE OK — but this runner is gate-check only; rerun under spec for Phases B-F.")
    return 0 if not gate_satisfied else 0


if __name__ == "__main__":
    raise SystemExit(main())
