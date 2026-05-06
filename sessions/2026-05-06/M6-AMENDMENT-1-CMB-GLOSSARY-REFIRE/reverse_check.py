"""
Reverse-validation of 052R amendment.

Loads post-edit CMB.txt, surgically removes the known insertions:
- glossary block (22 lines: 21 content + 1 trailing blank) after original-L37
- 4 annotation lines after original-L404/L941/L993/L1517
Then compares the resulting bytes to the expected pre-edit SHA-256.

If they match bit-for-bit, then the patch was a PURE INSERTION (no deletions,
no modifications) — equivalent to `git diff` showing zero `-` lines.
"""
from __future__ import annotations

import hashlib
from pathlib import Path

CMB_PATH = Path("tex/submitted/CMB.txt")
EXPECTED_PRE_SHA = "04F2A0405F7DF5566D6720D6670AAFC26D5E157E78CD51B4B537E95FB689771A"

# Post-edit insertion-line numbers (from patch script output)
# original L37 → 22 inserted lines starting at post-edit L38..L59
# original L404 → 1 inserted at post-edit L427  (orig+22-1+1=423? let me recompute)
# Actually patch script reported insert positions:
#   L37  -> insertion at post-edit L38 (22 lines: L38..L59)
#   L404 -> insertion at post-edit L427  (i.e., one line at L427)
#   L941 -> insertion at post-edit L965
#   L993 -> insertion at post-edit L1018
#   L1517-> insertion at post-edit L1543

INSERTED_RANGES = [
    (38, 59),     # 22 lines: 21 glossary content + 1 trailing blank
    (427, 427),   # annotation after original-L404
    (965, 965),   # annotation after original-L941
    (1018, 1018), # annotation after original-L993
    (1543, 1543), # annotation after original-L1517
]


def parse_lines(raw: bytes):
    lines = []
    i = 0
    line_start = 0
    while i < len(raw):
        if raw[i] == 0x0A:
            if i > 0 and raw[i - 1] == 0x0D:
                text = raw[line_start : i - 1]
                eol = b"\r\n"
            else:
                text = raw[line_start : i]
                eol = b"\n"
            lines.append((text, eol))
            line_start = i + 1
            i += 1
        else:
            i += 1
    if line_start < len(raw):
        lines.append((raw[line_start:], b""))
    return lines


def main():
    raw = CMB_PATH.read_bytes()
    post_sha = hashlib.sha256(raw).hexdigest().upper()
    print(f"[post] SHA = {post_sha}")
    lines = parse_lines(raw)
    print(f"[post] line count = {len(lines)}")

    drop = set()
    for lo, hi in INSERTED_RANGES:
        for n in range(lo, hi + 1):
            drop.add(n)

    kept = [t + e for n, (t, e) in enumerate(lines, start=1) if n not in drop]
    reconstructed = b"".join(kept)
    rec_sha = hashlib.sha256(reconstructed).hexdigest().upper()
    print(f"[reconstructed pre-edit] SHA = {rec_sha}")
    print(f"[reconstructed pre-edit] bytes = {len(reconstructed)}")
    print(f"[expected pre-edit]      SHA = {EXPECTED_PRE_SHA}")
    if rec_sha == EXPECTED_PRE_SHA:
        print("[PASS] HALT_DEPOSIT_TIME_PRESERVATION — pre-existing bytes preserved bit-for-bit.")
    else:
        print("[FAIL] HALT_DEPOSIT_TIME_PRESERVATION — reconstruction does not match expected pre-edit SHA.")
        # Diagnostic: dump the first differing region
        # (kept off by default; re-enable if needed)


if __name__ == "__main__":
    main()
