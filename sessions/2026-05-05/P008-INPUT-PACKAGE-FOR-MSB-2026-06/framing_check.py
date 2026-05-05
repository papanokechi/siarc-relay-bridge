"""HALT_045_PACKAGE_INCLUDES_FRAMING self-check.

Strip ```...``` fenced blocks (verbatim quotes) and blockquotes (>) that
quote substrate, then grep the remainder (compiler prose) for the
forbidden opinion-words list.
"""
import os
import re

SD = r"C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\siarc-relay-bridge\sessions\2026-05-05\P008-INPUT-PACKAGE-FOR-MSB-2026-06"
md = os.path.join(SD, "p008_input_package_for_msb_2026-06.md")
text = open(md, "r", encoding="utf-8").read()

# Strip 4-tilde fenced verbatim blocks
stripped = re.sub(r"~~~~[^\n]*\n.*?\n~~~~", "", text, flags=re.DOTALL)

# Forbidden words (case-insensitive whole-word)
forbidden = [r"\bshould\b", r"\brecommend(?:s|ed|ation)?\b",
             r"\bpropose(?:s|d)?\b", r"\bargue(?:s|d)?\b",
             r"\bsuggest(?:s|ed|ion)?\b", r"\bwe believe\b",
             r"\bour view\b", r"\bought\b"]

hits = []
for pat in forbidden:
    for m in re.finditer(pat, stripped, flags=re.IGNORECASE):
        # find line number
        ln = stripped.count("\n", 0, m.start()) + 1
        # show ~80 chars context
        start = max(0, m.start() - 40)
        end = min(len(stripped), m.end() + 40)
        ctx = stripped[start:end].replace("\n", " ")
        hits.append((pat, ln, m.group(0), ctx))

if not hits:
    print("PASS: no forbidden opinion words in compiler-prose regions.")
else:
    print(f"INSPECT: {len(hits)} potential hits:")
    for pat, ln, w, ctx in hits:
        print(f"  L{ln} {pat!r} match={w!r}: ...{ctx}...")
