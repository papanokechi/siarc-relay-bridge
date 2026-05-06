"""
STEP 6 of relay-047: append the verbatim verdict block to
- cli_log/2026-05-06.md  (under "## SYNTH-TRACK M6 verdict")
- tex/submitted/CMB.txt (append at SYNTH-TRACK section, with timestamp + bridge link)

Both edits are APPENDS, not replacements.  No reflow of existing content.
"""

from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

SESSION_DIR = Path(__file__).parent
WORKSPACE = SESSION_DIR.parents[3]  # 4 levels up: claude-chat
VERDICT_PATH = SESSION_DIR / "m6_verdict.md"
CLI_LOG_PATH = WORKSPACE / "cli_log" / "2026-05-06.md"
CMB_PATH = WORKSPACE / "tex" / "submitted" / "CMB.txt"

BRIDGE_LINK = (
    "https://github.com/papanokechi/siarc-relay-bridge/tree/main/"
    "sessions/2026-05-06/M6-ARBITRATION-W19-FRIDAY/"
)
CLAUDE_FETCH = (
    "https://raw.githubusercontent.com/papanokechi/siarc-relay-bridge/main/"
    "sessions/2026-05-06/M6-ARBITRATION-W19-FRIDAY/handoff.md"
)

NOW_JST_TS = "2026-05-06"  # date stamp; precise time logged in handoff


def append(path: Path, block: str) -> None:
    if not path.exists():
        print(f"!! target does not exist: {path}", file=sys.stderr)
        sys.exit(2)
    # APPEND ONLY -- no read-modify-write of the existing content.
    with open(path, "ab") as f:
        # ensure separation from prior content
        f.write(b"\n")
        f.write(block.encode("utf-8"))
        # final newline
        if not block.endswith("\n"):
            f.write(b"\n")


def main() -> int:
    verdict = VERDICT_PATH.read_text(encoding="utf-8").rstrip("\n")

    # ---------- cli_log/2026-05-06.md append ----------
    cli_block = f"""---

## SYNTH-TRACK M6 verdict

**Time:** {NOW_JST_TS} (relay 047 dispatch; CLI-Synth in-tier under v2026-05-08 RACI; Tier 2)
**Bridge:** sessions/2026-05-06/M6-ARBITRATION-W19-FRIDAY/
**Status:** COMPLETE

The following verdict block is verbatim from `m6_verdict.md` in the
bridge session above. SHA-256 of the verbatim block (from the
`# m6_verdict.md` header to the `## End of m6_verdict.md` marker
inclusive) is recorded in claims.jsonl entry C3 of the same bridge
session.

----- begin verbatim m6_verdict.md -----
{verdict}
----- end verbatim m6_verdict.md -----

- BRIDGE: {BRIDGE_LINK}
- CLAUDE_FETCH: {CLAUDE_FETCH}
"""

    append(CLI_LOG_PATH, cli_block)

    # ---------- CMB.txt SYNTH-TRACK append ----------
    sep = "=" * 64
    cmb_block = f"""

{sep}
SYNTH-TRACK  {NOW_JST_TS}  M6 ARBITRATION VERDICT (relay 047)
{sep}

CLI-Synthesizer in-tier verdict (v2026-05-08 RACI Tier 2),
resolving the M6 ✅-vs-Phase-A/B.5 status flag carried in
this CMB at L1517-1518 + cli_log/2026-05-05.md L1166 + L1234-1235
+ 045 P-008 §7 PENDING SYNTHESIZER ARBITRATION marker.

The following verdict block is verbatim from `m6_verdict.md` in the
bridge session at:

  sessions/2026-05-06/M6-ARBITRATION-W19-FRIDAY/

SHA-256 of the verbatim block recorded in claims.jsonl C3 of that
session.  Diagnosis branch: D1 (split definition).  Both legs
(M6.H4 ✅, M6.CC 🟡 PARTIAL) are correct under their respective
definitions; the M9-gating clause reads M6 as M6.CC.

----- begin verbatim m6_verdict.md -----
{verdict}
----- end verbatim m6_verdict.md -----

Bridge: {BRIDGE_LINK}
"""

    append(CMB_PATH, cmb_block)

    print("Appends written:")
    print(f"  cli_log: {CLI_LOG_PATH}  (+{len(cli_block)} bytes)")
    print(f"  CMB.txt: {CMB_PATH}  (+{len(cmb_block)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
