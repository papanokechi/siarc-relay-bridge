"""Finalize the corrections-final V_quad Zenodo metadata for VQUAD-ZENODO-READY-001 (re-run / run-2).

Reads the PREP-001 provisional zenodo_metadata.md, folds the two operator-resolved
changes (L-3 abstract clause; F-AFFIL Option C affiliation), preserves every other
byte (encoding + newlines), writes run-2/zenodo_metadata.md, and prints the new
metadata anchor SHA-256. PREP-001 is NOT modified.
"""
import os, hashlib, re, json

HERE = os.path.dirname(os.path.abspath(__file__))
PREP = os.path.normpath(os.path.join(
    HERE, "..", "..", "VQUAD-ZENODO-PREP-001", "zenodo_metadata.md"))

raw = open(PREP, "rb").read()
text = raw.decode("utf-8")
nl = "\r\n" if "\r\n" in text else "\n"


def rep(t, old, new, label):
    c = t.count(old)
    assert c == 1, f"{label}: expected 1 match, got {c}"
    return t.replace(old, new)


# R1 markdown description clause (real Unicode glyphs)
text = rep(
    text,
    "holonomic of order 4 with coefficients in the real quadratic field \u211a(\u221a3); \u03b3 is an explicit Hankel",
    "holonomic of order 4 (the Borel\u2013Laplace dual of the order-2 operator annihilating the series) with coefficients in the real quadratic field \u211a(\u221a3); \u03b3 is an explicit Hankel",
    "R1-md-desc",
)

# R2 JSON description clause (literal backslash-u escapes in the file text)
text = rep(
    text,
    r"holonomic of order 4 with coefficients in the real quadratic field \u211a(\u221a3); \u03b3 is an explicit Hankel",
    r"holonomic of order 4 (the Borel\u2013Laplace dual of the order-2 operator annihilating the series) with coefficients in the real quadratic field \u211a(\u221a3); \u03b3 is an explicit Hankel",
    "R2-json-desc",
)

# R3 creators affiliation (inline, newline-free)
text = rep(
    text,
    '"name": "Papanokechi",',
    '"name": "Papanokechi", "affiliation": "Independent Researcher, Yokohama, Japan",',
    "R3-creators-affil",
)

# R5 _affiliation_decision annotation -> RESOLVED
text = rep(
    text,
    '"_affiliation_decision": "brief Stage 3.1 requests \'Independent Researcher, Yokohama, Japan\'; corpus convention (template PINNED, latest record 20694841 null, prior v1-spec error) is BLANK. Operator decides at deposit; creators block kept ORCID-only as the safe default."',
    '"_affiliation_decision": "RESOLVED 2026-06-16 (operator) \u2192 Option C: affiliation \'Independent Researcher, Yokohama, Japan\' wired into the creators block. Corpus default was BLANK; operator chose the brief value for this deposit."',
    "R5-affil-decision",
)

# R6 _related_identifiers_pointer -> Scenario B (isSupplementTo dropped, 11 ids)
text = rep(
    text,
    "mint (12 ids; bundle isSupplementTo is a placeholder)",
    "mint (11 ids; Scenario B \u2014 bundle isSupplementTo dropped, paper+bundle = one record)",
    "R6-relid-pointer",
)

# Line-based edits: affiliation table row + finalization banner
lines = text.split(nl)
tbl = 0
banner_at = None
for i, l in enumerate(lines):
    if l.startswith("| Creator affiliation |"):
        lines[i] = "| Creator affiliation | Independent Researcher, Yokohama, Japan | **RESOLVED \u2192 Option C** |"
        tbl += 1
    if l.startswith("> **Current-draft caveat") and banner_at is None:
        banner_at = i
assert tbl == 1, f"table row matches: {tbl}"
assert banner_at is not None, "caveat anchor not found"

banner = [
    "> **RE-RUN FINALIZATION (VQUAD-ZENODO-READY-001 run-2, 2026-06-16).** This file is the",
    "> corrections-final deposit metadata. Changes folded vs the PREP-001 provisional: (1) the",
    "> abstract/description now matches the corrections-final paper verbatim \u2014 the L-3 clause",
    "> \u201c(the Borel\u2013Laplace dual of the order-2 operator annihilating the series)\u201d was added after",
    "> \u201cholonomic of order 4\u201d; (2) **F-AFFIL RESOLVED \u2192 Option C**: affiliation \u201cIndependent",
    "> Researcher, Yokohama, Japan\u201d is wired into the creators block. Keywords, MSC, version",
    "> (1.0.0), and the bundle/SIARC description addendum are unchanged (Scenario B: the bundle",
    "> rides in this same record). The metadata anchor is **re-pinned** (new SHA-256 recorded in",
    "> this slot\u2019s metadata-anchor-current.txt; supersedes the provisional dee9195c\u2026). The",
    "> \u201ccurrent-draft caveat\u201d and \u201cF-AFFIL \u2014 operator decides\u201d notes below are **retained for",
    "> provenance but superseded by this finalization.**",
    "",
]
lines = lines[:banner_at] + banner + lines[banner_at:]
text = nl.join(lines)

out = os.path.join(HERE, "zenodo_metadata.md")
data = text.encode("utf-8")
open(out, "wb").write(data)
h = hashlib.sha256(data).hexdigest()

print("WROTE:", out)
print("BYTES:", len(data))
print("NEWLINE:", repr(nl))
print("NEW_ANCHOR_SHA256:", h)
print("OLD_ANCHOR_SHA256: dee9195c7957f25fc57f497d6875cdd2b63d97d24f55f36b5e54e388ec003eb8")

m = re.search(r"```json\s*(\{.*?\})\s*```", text, re.S)
md = json.loads(m.group(1))
print("JSON_PARSES: True")
print("DESC_LEN:", len(md["metadata"]["description"]))
print("AFFILIATION:", md["metadata"]["creators"][0].get("affiliation"))
print("CLAUSE_IN_DESC:", "Borel\u2013Laplace dual of the order-2 operator annihilating the series" in md["metadata"]["description"])
print("TITLE:", md["metadata"]["title"])
print("VERSION:", md["metadata"]["version"])
print("KEYWORDS_N:", len(md["metadata"]["keywords"]))
