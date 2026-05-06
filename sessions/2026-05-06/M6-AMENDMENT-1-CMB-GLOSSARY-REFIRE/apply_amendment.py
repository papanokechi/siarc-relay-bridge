"""
052R — M6 spec-amendment #1 patch script.

Applies the 4 inline annotations (L404/L941/L993/L1517) and the glossary block
(after L37, between existing `---` and `## P11 ACTIVE BLOCKERS` section header)
to tex/submitted/CMB.txt, byte-exact, deposit-time preserving.

Verification:
- Pre-edit + post-edit SHA-256 of full file
- Pre-edit + post-edit SHA-256 of verbatim m6_verdict.md block (L1644-L1837)
- All inserted bytes use EOL matching surrounding line (CRLF for L37/L404/L941/L993, LF for L1517)
- No bytes in pre-existing content are modified (pure insertions)
"""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path

CMB_PATH = Path("tex/submitted/CMB.txt")

EXPECTED_PRE_SHA = "04F2A0405F7DF5566D6720D6670AAFC26D5E157E78CD51B4B537E95FB689771A"

# Glossary block — exact text from relay 052R STEP 3 (verbatim).
# 21 content lines.
GLOSSARY_BLOCK_LINES = [
    "================================================================",
    "GLOSSARY — M6 leg disambiguation (added 2026-05-06 per 047",
    "M6-ARBITRATION verdict; bridge 78c7b16; operator+Claude assent",
    "in-tier 2026-05-06)",
    "================================================================",
    "M6.H4 = alien-amplitude / H4 leg = `op:cc-median-resurgence-",
    "        execute` slot. ✅ DONE 2026-05-02 (verdict",
    "        `H4_EXECUTED_PASS_108_DIGITS`, prompt 005).",
    "M6.CC = canonical-form / CC-VQUAD-PIII-NORMALIZATION-MAP slot",
    "        = the M9-gating clause leg. 🟡 PARTIAL: Phase B",
    "        PINNED 2026-05-02; Phase B.5 INDEX-2 EMBEDDING grade",
    "        (bridge a9d34fd) pending operator+Claude pivot review;",
    "        Phase A/C/D/E/F NOT_YET_FIRED.",
    "Reading rule (047 verdict):",
    "  - Unqualified `M6` in a GATING context = M6.CC",
    "  - Unqualified `M6 ✅` in an ANNOUNCEMENT-FORMAT pattern-",
    "    match context = M6.H4",
    "  - Unqualified `M6` in entries written BEFORE 2026-05-06",
    "    retains its deposit-time ambiguity; inline annotations",
    "    below resolve specific cited cases.",
    "================================================================",
]
assert len(GLOSSARY_BLOCK_LINES) == 21, len(GLOSSARY_BLOCK_LINES)

# Annotations — exact text from relay 052R STEP 4 (verbatim, including leading whitespace).
ANNOTATIONS = {
    404:  "        [M6 → M6.H4 per 047 verdict 2026-05-06, bridge 78c7b16; announcement-format pattern-match reading]",
    941:  "[M6 → M6.CC per 047 verdict 2026-05-06, bridge 78c7b16; M9-gating-clause reading]",
    993:  "    [M6 → M6.CC per 047 verdict 2026-05-06, bridge 78c7b16; M9-gating recommendation reading]",
    1517: "    [M6 → M6.CC per 047 verdict 2026-05-06, bridge 78c7b16; arbitration-flag-carrier reading; verdict's own §1 cite \"L1518\" is off-by-one — token is at L1517]",
}


def parse_lines(raw: bytes):
    """Return list of (line_text_bytes_without_eol, eol_bytes) tuples plus end_offsets per line."""
    lines = []  # list of (text_bytes, eol_bytes)
    end_offsets = []  # absolute byte offset just after each line (incl its EOL)
    i = 0
    line_start = 0
    while i < len(raw):
        b = raw[i]
        if b == 0x0A:
            # found LF
            if i > 0 and raw[i - 1] == 0x0D:
                text = raw[line_start : i - 1]
                eol = b"\r\n"
            else:
                text = raw[line_start : i]
                eol = b"\n"
            lines.append((text, eol))
            end_offsets.append(i + 1)
            line_start = i + 1
            i += 1
        else:
            i += 1
    if line_start < len(raw):
        # last line w/o trailing newline
        lines.append((raw[line_start:], b""))
        end_offsets.append(len(raw))
    return lines, end_offsets


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def main():
    raw = CMB_PATH.read_bytes()
    pre_sha = sha256_hex(raw)
    pre_size = len(raw)
    print(f"[pre] SHA256 = {pre_sha}")
    print(f"[pre] size   = {pre_size} bytes")
    if pre_sha != EXPECTED_PRE_SHA:
        print(f"[FATAL] pre-edit SHA mismatch (expected {EXPECTED_PRE_SHA})")
        sys.exit(2)

    lines, _ = parse_lines(raw)
    print(f"[pre] line count = {len(lines)}")

    # Verbatim block: L1644..L1837 inclusive (1-based) → indices 1643..1836.
    L1644_idx = 1643
    L1837_idx = 1836
    assert lines[L1644_idx][0].decode("utf-8") == "----- begin verbatim m6_verdict.md -----", lines[L1644_idx][0]
    assert lines[L1837_idx][0].decode("utf-8") == "----- end verbatim m6_verdict.md -----", lines[L1837_idx][0]
    pre_verbatim_bytes = b"".join(t + e for (t, e) in lines[L1644_idx : L1837_idx + 1])
    pre_verbatim_sha = sha256_hex(pre_verbatim_bytes)
    print(f"[pre] verbatim block (L1644..L1837) SHA256 = {pre_verbatim_sha}")
    print(f"[pre] verbatim block bytes = {len(pre_verbatim_bytes)}")

    # ---- Build edited line list ----
    # All edits are pure INSERTIONS. Strategy:
    #   - copy original lines verbatim
    #   - inject (a) glossary block + 1 trailing blank line AFTER L37 (between
    #     existing `---` separator at L36 + L37 blank and L38 `## P11 ACTIVE
    #     BLOCKERS` section header); inserted line ends use CRLF (matching local
    #     style at L35..L38 = CRLF)
    #   - inject (b) annotation line AFTER each of L404, L941, L993, L1517,
    #     using EOL matching that line's EOL (CRLF for L404/941/993, LF for
    #     L1517).
    # Because inserts are processed in original-line-number space, simplest
    # approach: walk through `lines` and build `new_lines` list; whenever we
    # finish copying line N (1-based), check if N is an insertion site and
    # append the inserted line(s) right after.
    new_lines: list[tuple[bytes, bytes]] = []

    # Glossary block lines (CRLF EOL throughout, matching surrounding L35-L38).
    # Pattern: <after L37 blank>, then 21-line glossary block, then 1 trailing
    # blank line (separator between glossary block and the next existing
    # section). This adds 22 lines total (21 + 1 blank).
    glossary_inserts: list[tuple[bytes, bytes]] = []
    for txt in GLOSSARY_BLOCK_LINES:
        glossary_inserts.append((txt.encode("utf-8"), b"\r\n"))
    glossary_inserts.append((b"", b"\r\n"))  # trailing blank line

    # Annotation inserts: site → (text bytes, eol bytes)
    eol_for_site = {404: b"\r\n", 941: b"\r\n", 993: b"\r\n", 1517: b"\n"}
    annot_inserts = {n: (ANNOTATIONS[n].encode("utf-8"), eol_for_site[n]) for n in ANNOTATIONS}

    insert_after_logged: dict[int, int] = {}  # original line N → 1-based post-edit line where insertion sits

    for n, (text, eol) in enumerate(lines, start=1):
        new_lines.append((text, eol))
        if n == 37:
            insert_after_logged[37] = len(new_lines) + 1  # first inserted line is at post-edit line N+1
            new_lines.extend(glossary_inserts)
        if n in annot_inserts:
            insert_after_logged[n] = len(new_lines) + 1
            new_lines.append(annot_inserts[n])

    # Sanity counts
    expected_delta = 22 + 4  # 21 glossary lines + 1 trailing blank + 4 annotations
    actual_delta = len(new_lines) - len(lines)
    print(f"[delta] expected line delta = +{expected_delta}, actual = +{actual_delta}")
    assert actual_delta == expected_delta, (actual_delta, expected_delta)

    # Locate the post-edit indices of L1644 and L1837 of the verbatim block.
    # The verbatim block was at original L1644..L1837 (indices 1643..1836).
    # Insertions BEFORE L1644 in original space:
    #   - 22 lines after L37 (glossary)
    #   - 1 line after L404
    #   - 1 line after L941
    #   - 1 line after L993
    #   - 1 line after L1517
    #   = 26 lines inserted before L1644
    # So new L1644 is at original line 1644 + 26 = post-edit line 1670.
    expected_post_L1644 = 1644 + 26
    expected_post_L1837 = 1837 + 26
    post_verbatim_text_at_1670 = new_lines[expected_post_L1644 - 1][0].decode("utf-8")
    post_verbatim_text_at_1863 = new_lines[expected_post_L1837 - 1][0].decode("utf-8")
    assert post_verbatim_text_at_1670 == "----- begin verbatim m6_verdict.md -----", (expected_post_L1644, post_verbatim_text_at_1670)
    assert post_verbatim_text_at_1863 == "----- end verbatim m6_verdict.md -----", (expected_post_L1837, post_verbatim_text_at_1863)
    post_verbatim_bytes = b"".join(
        t + e for (t, e) in new_lines[expected_post_L1644 - 1 : expected_post_L1837]
    )
    post_verbatim_sha = sha256_hex(post_verbatim_bytes)
    print(f"[post] verbatim block (L{expected_post_L1644}..L{expected_post_L1837}) SHA256 = {post_verbatim_sha}")
    print(f"[post] verbatim block bytes = {len(post_verbatim_bytes)}")
    if post_verbatim_sha != pre_verbatim_sha:
        print("[FATAL] verbatim block SHA changed — HALT_VERBATIM_BLOCK_MODIFIED")
        sys.exit(3)

    # Glossary block SHA-256 (UTF-8, LF as canonical) — NO trailing blank.
    glossary_canonical = "\n".join(GLOSSARY_BLOCK_LINES) + "\n"
    glossary_sha = sha256_hex(glossary_canonical.encode("utf-8"))
    print(f"[glossary] canonical (LF) SHA256 = {glossary_sha}")
    print(f"[glossary] canonical (LF) bytes  = {len(glossary_canonical.encode('utf-8'))}")

    # Concatenate and write.
    out = b"".join(t + e for (t, e) in new_lines)
    post_sha = sha256_hex(out)
    post_size = len(out)
    print(f"[post] SHA256 = {post_sha}")
    print(f"[post] size   = {post_size} bytes (delta = +{post_size - pre_size})")
    print(f"[post] line count = {len(new_lines)}")

    # Self-check that no PRE-existing line was modified — every original line's
    # (text, eol) tuple must appear in new_lines in order.
    j = 0
    for orig in lines:
        while j < len(new_lines) and new_lines[j] != orig:
            j += 1
        if j >= len(new_lines):
            print("[FATAL] original line not found in post-edit sequence — HALT_DEPOSIT_TIME_PRESERVATION")
            sys.exit(4)
        j += 1
    print("[self-check] all original lines preserved in order (pure insertions)")

    # Per-site insertion line numbers in post-edit indexing
    for site_n in sorted(insert_after_logged):
        print(f"[site] L{site_n} (orig) → annotation/insertion sits at post-edit L{insert_after_logged[site_n]}")

    # Write.
    CMB_PATH.write_bytes(out)
    print("[write] CMB.txt updated.")


if __name__ == "__main__":
    main()
