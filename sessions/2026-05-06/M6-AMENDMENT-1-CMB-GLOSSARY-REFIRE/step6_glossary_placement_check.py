"""STEP 6 — HALT_GLOSSARY_PLACEMENT self-check."""
from __future__ import annotations

import sys
from pathlib import Path

CMB_PATH = Path("tex/submitted/CMB.txt")

# Insertion sites (post-edit, 1-based)
GLOSSARY_FIRST_LINE = 38
GLOSSARY_LAST_LINE = 59
ANNOTATION_LINES = sorted([427, 965, 1018, 1543])
VERBATIM_BEGIN = 1670  # post-edit L1670

REQUIRED_STRINGS = ["M6.H4 = ", "M6.CC = ", "047", "78c7b16"]


def main():
    raw = CMB_PATH.read_bytes()
    text_lines = raw.decode("utf-8").replace("\r\n", "\n").split("\n")
    print(f"[lines] {len(text_lines)} (last may be empty if file ends in newline)")

    glossary_lines = text_lines[GLOSSARY_FIRST_LINE - 1 : GLOSSARY_LAST_LINE]
    glossary_block = "\n".join(glossary_lines)
    print("--- glossary block (post-edit L{0}..L{1}) ---".format(GLOSSARY_FIRST_LINE, GLOSSARY_LAST_LINE))
    for i, ln in enumerate(glossary_lines, start=GLOSSARY_FIRST_LINE):
        print(f"L{i:4d}: {ln}")
    print("--- end glossary block ---")

    # Check 1: glossary in pre-verbatim region
    if GLOSSARY_LAST_LINE >= VERBATIM_BEGIN:
        print("[FAIL] glossary block extends into verbatim region")
        sys.exit(1)
    print(f"[PASS] glossary block (L{GLOSSARY_FIRST_LINE}..L{GLOSSARY_LAST_LINE}) is fully above verbatim begin (L{VERBATIM_BEGIN}).")

    # Check 2: glossary before any pre-1644 inline annotation
    pre_verbatim_annotations = [n for n in ANNOTATION_LINES if n < VERBATIM_BEGIN]
    earliest_annotation = min(pre_verbatim_annotations) if pre_verbatim_annotations else None
    if earliest_annotation is None:
        print("[NOTE] no pre-verbatim annotations exist (unexpected)")
    elif GLOSSARY_LAST_LINE >= earliest_annotation:
        print(f"[FAIL] glossary block ends at L{GLOSSARY_LAST_LINE} but earliest annotation is L{earliest_annotation}")
        sys.exit(1)
    else:
        print(f"[PASS] glossary block ends at L{GLOSSARY_LAST_LINE}, before earliest annotation L{earliest_annotation}.")

    # Check 3: required strings present in the glossary block
    missing = [s for s in REQUIRED_STRINGS if s not in glossary_block]
    if missing:
        print(f"[FAIL] glossary block missing required strings: {missing}")
        sys.exit(1)
    print(f"[PASS] glossary block contains all required strings: {REQUIRED_STRINGS}")

    print("[PASS] STEP 6 — HALT_GLOSSARY_PLACEMENT self-check.")


if __name__ == "__main__":
    main()
