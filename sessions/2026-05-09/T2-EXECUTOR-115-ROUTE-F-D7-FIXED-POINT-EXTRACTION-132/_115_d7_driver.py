"""
Driver for prompt 115 Phase B numerical re-derivation.

Bypasses the pre-existing module-level dependency
``vquad_p3d6_recovery`` -> ``cc_pipeline`` -> ``borel_channel`` (the
last is not vendored under ``pcf-research/channel/cc_pipeline_2026-05-01/``;
it lives only in ``siarc-relay-bridge/sessions/2026-05-01/BOREL-CHANNEL-5X/``).
Logged as UF-115-BOREL-CHANNEL-DEP. To execute the new agent-side function
``compute_d6_to_d7_reduction_at_v_quad`` AEAL-anchored at
``vquad_p3d6_recovery.py::compute_d6_to_d7_reduction_at_v_quad`` without
triggering the broken import chain, we exec only that function's source
slice from the canonical module.
"""
from __future__ import annotations
import ast
import hashlib
import json
import sys
import textwrap
from pathlib import Path

from mpmath import mp, mpf

HERE = Path(__file__).resolve().parent
CANONICAL_SRC = HERE / "vquad_p3d6_recovery.py"
TARGET_FN = "compute_d6_to_d7_reduction_at_v_quad"


def _extract_function_source(src_path: Path, fn_name: str) -> str:
    src = src_path.read_text(encoding="utf-8")
    tree = ast.parse(src)
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == fn_name:
            return ast.get_source_segment(src, node)
    raise RuntimeError(f"function {fn_name} not found in {src_path}")


def _sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    h.update(p.read_bytes())
    return h.hexdigest()


def _sha256_text(text: str) -> str:
    h = hashlib.sha256()
    h.update(text.encode("utf-8"))
    return h.hexdigest()


def main() -> int:
    fn_src = _extract_function_source(CANONICAL_SRC, TARGET_FN)
    # Execute in a namespace with mpmath bound (mirrors module env).
    ns: dict = {"mp": mp, "mpf": mpf}
    exec(compile(textwrap.dedent(fn_src), str(CANONICAL_SRC), "exec"), ns)
    compute = ns[TARGET_FN]

    out = compute(dps=300)

    # Expected synth values:
    expected = {
        "alpha": mpf(0),
        "beta": mpf(0),
        "gamma": mpf(1) / 9,
        "delta": mpf(0),
        "alpha_1": mpf(0),
    }

    residuals = {k: abs(out[k] - v) for k, v in expected.items()}
    tol = mpf("1e-200")
    pass_flags = {k: (r < tol) for k, r in residuals.items()}
    fixed_point_ok = bool(out["fixed_point"]) and (out["s1_alpha_1"] == out["alpha_1"])

    serialised = {
        "task_id": "T2-EXECUTOR-115-ROUTE-F-D7-FIXED-POINT-EXTRACTION-132",
        "phase": "B numerical re-derivation",
        "anchor_function": f"{CANONICAL_SRC.name}::{TARGET_FN}",
        "dps": int(out["dps"]),
        "inputs": {
            "eta_inf": mp.nstr(out["eta_inf"], 20),
            "eta_0": mp.nstr(out["eta_0"], 20),
            "theta_inf": mp.nstr(out["theta_inf"], 20),
            "theta_0": mp.nstr(out["theta_0"], 20),
        },
        "outputs": {
            "alpha": mp.nstr(out["alpha"], 20),
            "beta": mp.nstr(out["beta"], 20),
            "gamma": mp.nstr(out["gamma"], 25),
            "delta": mp.nstr(out["delta"], 20),
            "alpha_1": mp.nstr(out["alpha_1"], 20),
            "s1_alpha_1": mp.nstr(out["s1_alpha_1"], 20),
        },
        "expected": {k: mp.nstr(v, 25) for k, v in expected.items()},
        "residuals": {k: mp.nstr(r, 6) for k, r in residuals.items()},
        "tol": mp.nstr(tol, 6),
        "pass_components": pass_flags,
        "fixed_point_ok": fixed_point_ok,
        "all_pass": all(pass_flags.values()) and fixed_point_ok,
        "canonical_src_sha256": _sha256_file(CANONICAL_SRC),
        "extracted_fn_sha256": _sha256_text(fn_src),
    }

    print(json.dumps(serialised, indent=2))

    if not serialised["all_pass"]:
        print("HALT_115_NUMERICAL_MISMATCH or HALT_115_FIXED_POINT_FAIL", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
