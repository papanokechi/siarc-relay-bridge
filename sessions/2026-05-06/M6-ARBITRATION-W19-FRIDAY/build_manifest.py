"""
STEP 1 helper: build m6_substrate_manifest.json with {id, path, sha256, size, mtime}
for each M6-relevant substrate file.

Run from workspace root:
    python siarc-relay-bridge/sessions/2026-05-06/M6-ARBITRATION-W19-FRIDAY/build_manifest.py
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

WORKSPACE = Path(
    "C:/Users/shkub/OneDrive/Documents/archive/admin/VSCode/claude-chat"
).resolve()

# Each entry: (id, label, relative_path)
SUBSTRATES = [
    (
        "S1-038-HANDOFF",
        "038 Milestone Residual Gap Survey handoff (M6 caveat profile bundled "
        "in M9-announcement-format note L102)",
        "siarc-relay-bridge/sessions/2026-05-04/MILESTONE-RESIDUAL-GAP-SURVEY-"
        "M4-M7-M8B-M9/handoff.md",
    ),
    (
        "S2-W19-WSB",
        "W19 Weekly Strategy Brief (Fri 05-08 M6 Phase A or B.5 schedule + "
        "L78 calendar row)",
        "cli_log/2026-W19_wsb.md",
    ),
    (
        "S3-W19-MASTER-PROMPT",
        "W19 master prompt (M6 PHASE A or B.5 dispatch instructions L194-201; "
        "AEAL >= 16 R6 rule)",
        "cli_log/2026-W19_master_prompt.md",
    ),
    (
        "S4-CLI-LOG-2026-05-05",
        "Day-2 cli_log: M9 gating {M4, M6} (L324), M6 inconsistency to be "
        "resolved (L1166), CLI in-tier upcoming (L1234-1235)",
        "cli_log/2026-05-05.md",
    ),
    (
        "S5-CMB-TXT",
        "Claude Morning Briefing: SYNTH-TRACK section (no prior M6 verdict "
        "row); current SYNTH-TRACK rows include 2026-05-05 RACI absorbed and "
        "2026-05-06 P-009 caveat",
        "tex/submitted/CMB.txt",
    ),
    (
        "S6-PICTURE-V118",
        "PICTURE v1.18 (current ground-truth substrate): M6 row L42 "
        "STILL_PARTIAL_PENDING_PIVOT_DECISION; v1.15 amendment L979-980 M9 "
        "gating reduces to {M4, M6} unconditionally; row 005 H4 = M6 done "
        "L1049; row 015 = M6 canonical-form full closure DRAFTED L1059",
        "siarc-relay-bridge/sessions/2026-05-04/PICTURE-V18-AMENDMENT-DRAFTING/"
        "picture_v1.18.md",
    ),
    (
        "S7-CC-VQUAD-SPEC",
        "CC-VQUAD-PIII-NORMALIZATION-MAP prompt_spec.md (M6 9-phase spec; "
        "Phase A = formal Birkhoff series at z=0; Phase B = canonical map; "
        "Phase B.5 = B_2 <-> D_6 affine-Weyl cross-walk MANDATORY pre-step; "
        "verdict ladder UPGRADE_V1_0_FULL or UPGRADE_V1_0_PARTIAL_*; 8 HALT "
        "codes; AEAL >= 16)",
        "siarc-relay-bridge/sessions/2026-05-04/CC-VQUAD-PIII-NORMALIZATION-"
        "MAP-PROMPT-SPEC/prompt_spec.md",
    ),
    (
        "S8-SIARC-PRIMARY-W",
        "SIARC-PRIMARY-W-HOMOMORPHISM-DERIVATION handoff.md verdict "
        "CLOSED_M6_PHASE_B5_W_CROSSWALK_BY_SIARC_PRIMARY_DERIVATION with "
        "INDEX-2 EMBEDDING qualifier (L162); recommendation (1)-(3) "
        "operator+Claude review pending (L167-175)",
        "siarc-relay-bridge/sessions/2026-05-04/SIARC-PRIMARY-W-HOMOMORPHISM-"
        "DERIVATION/handoff.md",
    ),
    (
        "S9-SAKAI-2001",
        "SAKAI-2001-ACQUISITION handoff.md verdict "
        "UPGRADE_SAKAI_ACQUIRED_W_HOMOMORPHISM_NOT_IN_SAKAI: D_6^(1) surface "
        "+ W((2A_1)^(1)) generators extracted; W(B_2) <-> W((2A_1)^(1)) "
        "homomorphism NOT stated in Sakai 2001 (M6 Phase B.5 anchor PARTIAL)",
        "siarc-relay-bridge/sessions/2026-05-04/SAKAI-2001-ACQUISITION/"
        "handoff.md",
    ),
    (
        "S10-NOUMI-YAMADA-2004",
        "NOUMI-YAMADA-2004-ACQUISITION handoff verdict "
        "UPGRADE_NY04_NIA_ILL_RECOMMENDED: NY 2004 TOC reveals NO P_III "
        "chapter; W(B_2) <-> W((2A_1)^(1)) homomorphism NOT stated in any "
        "post-Sakai PIII OA paper surveyed",
        "siarc-relay-bridge/sessions/2026-05-04/NOUMI-YAMADA-2004-ACQUISITION/"
        "handoff.md",
    ),
    (
        "S11-045-P008-PACKAGE",
        "045 P-008 input package for MSB 2026-06: section S6 "
        "'M6 ✅-vs-Phase-A/B.5 inconsistency status' = PENDING SYNTHESIZER "
        "ARBITRATION (L484-486 of p008_input_package_for_msb_2026-06.md)",
        "siarc-relay-bridge/sessions/2026-05-08/P008-INPUT-PACKAGE-FOR-MSB-"
        "2026-06/p008_input_package_for_msb_2026-06.md",
    ),
    (
        "S12-M9-DEP-AUDIT",
        "M9-MAIN-THEOREM-S2-DEPENDENCY-AUDIT verdict "
        "INDETERMINATE_NO_FORMAL_STATEMENT (4ffcc8c): F4 audit row CT v1.3 "
        "§Implications (L1336-1349) classified as SOFT precondition; M9 "
        "gating retained {M4, M6}",
        "siarc-relay-bridge/sessions/2026-05-05/M9-MAIN-THEOREM-S2-"
        "DEPENDENCY-AUDIT/handoff.md",
    ),
]


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    out: list[dict] = []
    missing: list[str] = []
    for sid, label, rel in SUBSTRATES:
        p = (WORKSPACE / rel).resolve()
        if not p.exists():
            missing.append(f"{sid}: {rel}")
            out.append(
                {
                    "id": sid,
                    "label": label,
                    "path": rel,
                    "sha256": None,
                    "size": None,
                    "mtime_utc": None,
                    "exists": False,
                }
            )
            continue
        st = p.stat()
        out.append(
            {
                "id": sid,
                "label": label,
                "path": rel,
                "sha256": sha256_file(p),
                "size": st.st_size,
                "mtime_utc": datetime.fromtimestamp(
                    st.st_mtime, tz=timezone.utc
                ).strftime("%Y-%m-%d %H:%M:%S UTC"),
                "exists": True,
            }
        )

    out_dir = (
        WORKSPACE
        / "siarc-relay-bridge"
        / "sessions"
        / "2026-05-06"
        / "M6-ARBITRATION-W19-FRIDAY"
    )
    manifest = {
        "task_id": "M6-ARBITRATION-W19-FRIDAY",
        "today_date_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "fire_time_utc": datetime.now(timezone.utc).strftime(
            "%Y-%m-%d %H:%M:%S UTC"
        ),
        "workspace_root": str(WORKSPACE).replace("\\", "/"),
        "substrates": out,
        "missing_count": len(missing),
        "missing": missing,
    }
    out_path = out_dir / "m6_substrate_manifest.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    print(f"Wrote {out_path}")
    print(f"Substrates indexed: {len(out)}; missing: {len(missing)}")
    if missing:
        for m in missing:
            print(f"  MISSING: {m}")

    # Aggregate manifest SHA for AEAL claim C1.
    agg = hashlib.sha256()
    with open(out_path, "rb") as f:
        agg.update(f.read())
    print(f"manifest_sha256: {agg.hexdigest()}")
    return 0 if not missing else 0  # missing recorded but does not block


if __name__ == "__main__":
    sys.exit(main())
