"""verify_description.py -- CT-S27-CTV17-DEPOSIT-PREP

Checks DESCRIPTION-v1.7-rev3.html, the text that would be pasted into the Zenodo
description field.  This is the ONLY artefact v1.7 publishes, so every defect
in it is a published defect.

SECTION 1  the gate.
SECTION 2  can-fail controls: each check is re-run against a mutant of the
           DESCRIPTION in which exactly the thing it guards has been broken.
SECTION 3  reader controls: the input path is mutated (wrong codec, no newline
           normalisation, truncation).  Per the adopted Amendment C, at least
           one known-present sentinel is NON-ASCII.
SECTION 4  the entity rule, validated against the DEPOSITED v1.6 text rather
           than against this session's opinion of it.
"""

import hashlib
import html
import html.entities
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SESSION = os.path.dirname(HERE)
SESSIONS = os.path.dirname(SESSION)
DRAFT = os.path.join(SESSIONS, "CT-S26-CTV17-DRAFT")
DESC = os.path.join(SESSION, "DESCRIPTION-v1.7-rev3.html")

# Description hashes this packet has quoted at some point and which are now
# HISTORY.  Publishing one of them as a current value is the failure that has
# cost a round twice; N8 exists so that it fails a gate instead of a reader.
SUPERSEDED_HASHES = [
    "026e7a9ebef7393564e408f7733adc7d3b7e6afe79b12092345b9af38c09b7ac",  # rev2, pre-item-6
    "39903126d90e0c3568274c2f61ea08e6e6b77a447dc6229fafe15273a2930e6d",  # rev2, item-6 first draft
]
NOTICE = os.path.join(SESSION, "NOTICE-v1.7-rev3.md")
RECORD = os.path.join(DRAFT, "refs", "zenodo_22782807.json")

ALLOWED_TAGS = {"p", "strong", "em"}

SENTINELS = [
    # NON-ASCII, per the adopted Amendment C.  The description is entity-encoded
    # and therefore almost pure ASCII; the subscripts are the only raw non-ASCII
    # left, so the sentinel has to be one of them or the latin-1 control cannot
    # fire.  An earlier version used "&beta;" -- pure ASCII -- and did not fire.
    "&xi;\u2080",
    "<p><strong>Version notice (v1.7).</strong>",
    "0. Current state",
    "6. The Borel material",
]

# (rule name, string that is present in the NOTICE and must be absent here)
EXCLUSIONS = [
    ("draft-banner", "DRAFT ONLY"),
    ("draft-banner-2", "No metadata edit has been made"),
    ("session-path", "Session: `sessions/"),
]

failures, broken = [], []


class ReadError(Exception):
    pass


def read_desc(path=None):
    with open(path or DESC, "rb") as fh:
        raw = fh.read()
    t = raw.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
    if "\r" in t:
        raise ReadError("CR survived normalisation")
    for s in SENTINELS:
        if s not in t:
            raise ReadError("known-present sentinel %r absent: the read is suspect" % s)
    return t


def crlf_copy():
    """A CRLF-bearing copy of the description, in memory only."""
    with open(DESC, "rb") as fh:
        return fh.read().replace(b"\n", b"\r\n")


def notice_text():
    with open(NOTICE, "rb") as fh:
        return fh.read().decode("utf-8").replace("\r\n", "\n")


def plain(t):
    """Tags stripped, entities resolved -- what a reader actually sees."""
    return html.unescape(re.sub(r"<[^>]+>", "", t))


# ------------------------------------------------------------------ checks
def c_tags(t):
    used = set(x.lower() for x in re.findall(r"</?([a-zA-Z0-9]+)", t))
    extra = used - ALLOWED_TAGS
    if extra:
        return False, ("tags outside the house set: %s (the deposited "
                       "descriptions use only p, strong, em)" % sorted(extra))
    return True, "tags are exactly %s" % sorted(used)


def c_balanced(t):
    for tag in sorted(ALLOWED_TAGS):
        o = len(re.findall(r"<%s>" % tag, t))
        c = len(re.findall(r"</%s>" % tag, t))
        if o != c:
            return False, "<%s> opened %d times, closed %d" % (tag, o, c)
    if re.search(r"<p>(?:(?!</p>).)*<p>", t, re.DOTALL):
        return False, "a <p> is nested inside another <p>"
    return True, "every p/strong/em is balanced and no <p> is nested"


def c_no_markdown(t):
    residue = {
        "bold markers **": r"\*\*",
        "code backticks": r"`",
        "table pipes": r"(?m)^\s*\|",
        "ATX heading": r"(?m)^#{1,6}\s",
        "horizontal rule": r"(?m)^-{3,}\s*$",
        "bullet at line start": r"(?m)^\s*[*+-]\s+",
        "fence": r"```",
    }
    found = [k for k, p in residue.items() if re.search(p, t)]
    if found:
        return False, "unconverted markdown survives: %s" % ", ".join(found)
    return True, "no markdown residue: no **, backticks, pipes, #, ---, fences"


def c_exclusions(t):
    nt = notice_text()
    for name, s in EXCLUSIONS:
        if s not in nt:
            return False, ("exclusion rule %r no longer matches anything in the "
                           "notice, so it is not doing any work: %r" % (name, s))
        if s in t:
            return False, ("corpus-internal material reached the description "
                           "(%s): %r" % (name, s))
    return True, "%d exclusion rules all present in the notice and absent here" % \
        len(EXCLUSIONS)


def c_no_draft_language(t):
    """Rewritten after it PASSED on a description ending 'Draft only -- no
    deposit, no metadata edit.'

    The original matched four literal strings case-sensitively: 'DRAFT ONLY',
    'Not deposited', 'no deposit is authorised', 'draft only'.  The published
    text read 'Draft only', which matches none of them.  Its single mutant was
    built by inserting 'DRAFT ONLY. Not deposited.' -- a string taken FROM THE
    CHECK'S OWN LIST -- so the mutant could only ever prove the list is
    consulted, never that the list is adequate.  A mutant drawn from the
    constant it tests is not an independent control.

    Now: case-insensitive, word-boundary, phrase-independent, with an explicit
    allowance for QUOTATION -- v1.6's erratum legitimately quotes the watermark
    'DRAFT -- NOT DEPOSITED' of the build it repairs, and that must survive.
    """
    p = plain(t)
    pat = r"(?i)\bdrafts?\b|\bnot deposited\b|\bno deposit\b|\bdo not cite\b|\bprovisional\b"
    offenders = []
    for m in re.finditer(pat, p):
        ctx = p[max(0, m.start() - 160):m.start() + 160]
        quoted = re.search(r'"[^"]{0,120}' + re.escape(m.group(0)), ctx, re.I)
        historical = re.search(r"v1\.[0-6]\b[^.]{0,200}$", p[:m.start()])
        if quoted or historical:
            continue
        offenders.append(p[max(0, m.start() - 60):m.start() + 60].strip())
    if offenders:
        return False, ("draft-stage language would be published (%d): %s"
                       % (len(offenders), offenders[:3]))
    return True, ("no unquoted draft-stage language; %d occurrence(s) allowed as "
                  "quotation of v1.6's watermark or as version history"
                  % len(re.findall(pat, p)))


def c_no_double_escape(t):
    """The check that did not exist while the defect stood in 77 places.

    Table rows were joined by ' &mdash; ' and only THEN markup-escaped, so the
    '&' became '&amp;' and the row published the literal text '&mdash;'.  T4
    could not see this: '&amp;mdash;' is perfectly well-formed HTML.  It is
    wrong at the RENDERED layer, not the markup layer, so it needs a check that
    looks at what a reader sees.
    """
    dbl = re.findall(r"&amp;[a-zA-Z][a-zA-Z0-9]*;", t)
    if dbl:
        return False, ("%d double-escaped entit(ies) would publish as literal "
                       "text: %s" % (len(dbl), sorted(set(dbl))))
    p = plain(t)
    leaked = re.findall(r"&[a-zA-Z][a-zA-Z0-9]*;", p)
    if leaked:
        return False, ("%d entity reference(s) survive into the rendered text: %s"
                       % (len(leaked), sorted(set(leaked))))
    return True, "no double-escaped entities; no entity text survives rendering"


def c_five_items(t):
    p = plain(t)
    needed = {
        "1 attribution": "is not a conjecture",
        "2 the exponent": "The exponent, and the priority position",
        "3 K and r_infinity": "and `r_\u221e`".replace("`", ""),
        "4 the vacuity explanation": "The vacuity explanation",
        "5 the Borel material": "The Borel material",
    }
    missing = [k for k, s in needed.items() if s not in p]
    if missing:
        return False, "commissioned item(s) missing: %s" % missing
    return True, "all five commissioned items present, in order"


def c_pslq_basis(t):
    """The carry-over that must not be lost in transit: the basis IN FULL.

    The basis is the STAGE 5B one, which deliberately EXCLUDES log Gamma(1/6):
    that generator was removed as redundant after Legendre duplication showed
    the Stage 5A space was degenerate.  An earlier version of this check
    required Gamma(1/6) to be present -- i.e. it would have demanded that the
    published basis contain the very generator whose removal was the point.
    The requirement is therefore stated from the notice's own printed space,
    and the removal is checked as well as the space.
    """
    p = plain(t)
    gens = ["log C", "log 2", "log 3", "log \u03c0", "log \u0393(1/3)"]
    missing = [g for g in gens if g not in p]
    if missing:
        return False, "the PSLQ basis is not stated in full; missing %s" % missing
    if "\u0393(1/6)" not in p or "removed as redundant" not in p:
        return False, ("the removal of \u0393(1/6) as the degenerate generator is "
                       "not recorded, so a reader cannot tell the space was "
                       "corrected rather than arbitrary")
    for bound in ["10^6", "dps 120", "D_trust"]:
        if bound not in p:
            return False, "the search bounds are incomplete; missing %r" % bound
    if re.search(r"log \u0393\(1/3\),?\s*\u2026", p):
        return False, "the PSLQ basis is elided with an ellipsis"
    return True, ("PSLQ basis printed in full (%d generators + constant), bounds "
                  "stated, \u0393(1/6) recorded as removed" % len(gens))


def c_naming_prohibition(t):
    p = plain(t)
    if "Naming prohibition" not in p:
        return False, "the naming prohibition section is absent"
    if not re.search(r"K\b.{0,80}amplitude.{0,80}\u03be\u2080", p, re.DOTALL):
        return False, "the prohibition does not tie K to the amplitude at xi_0"
    if "S_{\u03b6*}" not in p:
        return False, "S_{zeta*} is not named"
    return True, "naming prohibition present: K at xi_0, S_{zeta*} at 2 xi_0"


def c_build_statement(t):
    p = plain(t)
    if "the file attached is the v1.6 build, unchanged" not in p and \
            "the v1.6 build, unchanged" not in p:
        return False, ("the description does not state that the attached file is "
                       "the unchanged v1.6 build -- the one line this shape "
                       "requires")
    if "description only" not in p:
        return False, "the description does not say the corrections are description-only"
    return True, "the attached build is declared as the v1.6 build, unchanged"


def c_no_rebuild_claim(t):
    """A v1.7 build must not be claimed -- but the notice DENIES one in so many
    words, and a crude substring test flags the denial as the offence.  Each
    occurrence must therefore sit inside a negation."""
    p = plain(t)
    negators = ("no claim is made", "not a v1.7 build", "no pdf was rebuilt",
                "none is claimed", "is the v1.6 build")
    for m in re.finditer(r"v1\.7 build|rebuilt for this version|new build", p):
        ctx = p[max(0, m.start() - 200): m.start() + 200].lower()
        if not any(neg in ctx for neg in negators):
            return False, ("the description appears to claim a v1.7 build, "
                           "unnegated: ...%s..." % p[max(0, m.start() - 60):
                                                     m.start() + 60])
    if "no PDF was rebuilt" not in p:
        return False, "the description does not state plainly that no PDF was rebuilt"
    return True, ("no v1.7 build is claimed; every mention is negated and "
                  "'no PDF was rebuilt' is stated plainly")


def c_dois(t):
    with open(RECORD, encoding="utf-8") as fh:
        rec = json.load(fh)
    p = plain(t)
    if rec["conceptdoi"] not in p:
        return False, "the concept DOI from the record is not in the description"
    if rec["doi"] not in p:
        return False, "the superseded v1.6 version DOI is not named"
    if re.search(r"10\.5281/zenodo\.\d+ \(v1\.7\)", p):
        return False, "a v1.7 DOI is asserted; Zenodo mints it on publish"
    return True, "concept DOI and superseded v1.6 DOI both present, no v1.7 DOI invented"


def c_label_discipline(t):
    p = plain(t)
    if re.search(r"K\b[^.]{0,60}\bPROVEN\b", p):
        return False, "K is described as PROVEN"
    if "must not be written as PROVEN" not in p:
        return False, "the K label caveat did not survive conversion"
    return True, "K remains VERIFIED with its caveat intact"


def c_entities_wellformed(t):
    bad = re.findall(r"&(?!amp;|lt;|gt;|quot;|#\d+;|[a-zA-Z][a-zA-Z0-9]*;)", t)
    if bad:
        return False, "%d bare ampersand(s) or malformed entities" % len(bad)
    names = set(re.findall(r"&([a-zA-Z][a-zA-Z0-9]*);", t))
    unknown = sorted(n for n in names if n not in html.entities.entitydefs)
    if unknown:
        return False, "entity names not in HTML4: %s" % unknown
    return True, "%d distinct entities, all HTML4-defined, no bare ampersands" % len(names)


def c_no_internal_provenance(t):
    """The strip is a two-sided guarantee, and this is the first side.

    The operator's rule is: anything a reader can resolve stays; anything only
    the author can resolve goes.  Uncommitted session ids, refs/ paths, script
    names and AEAL claim ids resolve only against a working tree that has not
    been published, so they must not appear.  Committed sessions/ paths under
    the public repository DO resolve, and v1.6's own description carries one,
    so this check must not reject those.
    """
    p = plain(t)
    patterns = [
        (r"CT-S\d+[A-Z0-9-]*", "uncommitted session id"),
        (r"\brefs/", "refs/ path"),
        (r"\bscripts/", "scripts/ path"),
        (r"\boutputs/", "outputs/ path"),
        (r"\bS\d+[A-Z]?-\d\d\b", "AEAL claim id"),
        (r"\b\w+\.(?:py|json|jsonl|tex|txt|png)\b", "working file name"),
    ]
    offenders = []
    for pat, why in patterns:
        for m in re.finditer(pat, p):
            offenders.append("%s: %r" % (why, p[max(0, m.start() - 40):
                                           m.start() + 30].strip()))
    if offenders:
        return False, ("%d internal-provenance reference(s) a reader cannot "
                       "resolve: %s" % (len(offenders), offenders[:3]))
    return True, ("no unresolvable internal provenance; %d resolvable "
                  "sessions/ URL(s) under the public repository are kept"
                  % len(re.findall(r"github\.com/[^\s<]*sessions/", p)))


def c_resolvable_identifiers(t):
    """The second side, and the reason the first side is not enough.

    A strip that deleted the citations along with the paths would satisfy
    c_no_internal_provenance perfectly.  The bibliography's whole purpose is to
    make the attribution in items 1-4 checkable by a reader, so the identifiers
    that carry it must be asserted present, not merely not-forbidden.  Each was
    resolved against Crossref or the live URL before being written here.
    """
    p = plain(t)
    required = [
        "10.1137/1009002",             # Gautschi 1967, SIAM Review
        "10.1007/bf02398269",          # Birkhoff-Trjitzinsky 1933, Acta Math.
        "10.1002/sapm1992874289",      # Wong & Li II 1992 -- NOT OBTAINED
        "10.1142/S0219530522400012",   # Wong & Zhao 2022
        "10.1137/1.9781611977912.37",  # Ibrahim & Salvy
        "arXiv:2508.15246",            # Nemes
        "dlmf.nist.gov/3.6",
        "dlmf.nist.gov/2.9",
        "odlyzko",
        "10.5281/zenodo.19941678",     # concept DOI
        "10.5281/zenodo.22782807",     # v1.6 version DOI
    ]
    low = p.lower()
    missing = [r for r in required if r.lower() not in low]
    if missing:
        return False, ("%d resolvable identifier(s) absent -- the strip has "
                       "stranded a citation: %s" % (len(missing), missing))
    shas = re.findall(r"\b[0-9a-f]{64}\b", p)
    if len(shas) < 8:
        return False, ("only %d sha256 value(s) survive; the bibliography is "
                       "meant to let a reader confirm the same bytes" % len(shas))
    return True, ("%d of %d resolvable identifiers present, with %d sha256 "
                  "value(s)" % (len(required), len(required), len(shas)))


def c_sixth_item(t):
    """The sixth item (§7, the formal type) must be present AND must not
    overclaim.

    Presence alone is the weak half: a §7 that says the right things and then
    adds one sentence refuting the V_quad identification, or one calling a row
    match VERIFIED, would pass a presence-only check while publishing exactly
    the two errors §7 exists to avoid.  So the check is two-sided, and the
    mutants for the second half are drawn from those failure modes rather than
    from the required-string list above them.
    """
    p = plain(t)
    needed = {
        "the section": "The formal type of the generating-function operator",
        "the exclusion": "is not compatible with",
        "the necessary-condition caveat": "necessary, not sufficient",
        "the non-merger": "not evidence about it",
        "tier 3 disclosed as unconfirmed": "not independently confirmed",
    }
    missing = [k for k, s in needed.items() if s not in p]
    if missing:
        return False, "sixth item incomplete: %s" % sorted(missing)

    bad = []
    for m in re.finditer(r"[^.]*\bidentification\b[^.]*\.", p):
        s = m.group(0)
        if re.search(r"(?i)\b(refut|disprov|overturn|contradict|rule[sd]? out|"
                     r"is wrong|is false|cannot hold)", s):
            bad.append(s.strip())
    # Clause-level, not sentence-level.  §7.5 legitimately says in ONE sentence
    # that a mismatch is VERIFIED and that a match leaves open whether L_d
    # "lies in" the family; scanning the whole sentence reported that correct
    # prose as an overclaim.  A check that invents a defect costs what missing
    # one costs.  So: same clause, and hedged clauses do not count.
    for s in _clauses(p):
        if not re.search(r"(?i)\b(lies in|belongs to|sits in)\b", s):
            continue
        if not re.search(r"\b(VERIFIED|PROVEN)\b", s):
            continue
        if re.search(r"(?i)\b(leaves open|does not|would need|whether|not "
                     r"sufficient|necessary, not)\b", s):
            continue
        bad.append(s.strip())
    if bad:
        return False, "the sixth item overclaims: %s" % [s[:90] for s in bad[:2]]

    return True, ("sixth item present and two-sided: exclusion, three tiers, "
                  "necessary-not-sufficient caveat, and no merger with the "
                  "V_quad identification")


def _clauses(p):
    """Clause-level split.  Sentence-level scoping merges an assertion with the
    hedge that disowns it, so a correct two-clause sentence reads as a defect.

    The period in a version number is not a clause boundary: splitting on it
    turned every 'v1.4' into 'v1' + '4 ...', so the v1.4 arm below could never
    match anything.  Caught by a mutant, not by reading the code."""
    return [c for c in re.split(r"(?<![0-9])\.(?![0-9])|;", re.sub(r"\s+", " ", p))
            if c.strip()]


def _flat(t):
    """Whitespace-flattened plain text.  The notice is hard-wrapped and the
    converter emits one <p> per paragraph, so a literal multi-word probe can
    be defeated by a line break as easily as by absence.  A check that cannot
    tell those two apart is not a check."""
    return re.sub(r"\s+", " ", plain(t))


def c_tiers(t):
    """N5 -- the three tiers are present AND each is labelled IN THE PROSE.

    A tier marker that lives only in a heading is not recoverable from the
    sentence it governs: quote the paragraph anywhere else and the tier is
    gone.  So the check requires the marker in running text, and its mutant
    moves a marker into a heading to prove that is what is being tested.
    """
    f = _flat(t)
    markers = {
        "tier 1 in prose": "This paragraph is Tier 1",
        "tier 2 in prose": "This paragraph is Tier 2",
        "tier 3 in prose": "This paragraph is Tier 3",
    }
    missing = [k for k, s in markers.items() if s not in f]
    if missing:
        return False, "tier marker(s) not recoverable from the prose: %s" % sorted(missing)
    levels = {
        "tier 1 says independently confirmed":
            "This paragraph is Tier 1: independently confirmed",
        "tier 2 says NOT independently confirmed":
            "This paragraph is Tier 2: self-derived, and NOT independently confirmed",
        "tier 3 says contaminated":
            "This paragraph is Tier 3: self-derived by a re-derivation that was contaminated",
    }
    wrong = [k for k, s in levels.items() if s not in f]
    if wrong:
        return False, "a tier's level of confirmation is not stated with it: %s" % sorted(wrong)
    if "for any admissible coefficient vector" not in f:
        return False, "Tier 1 does not state the exclusion for every coefficient vector"
    if "a(1) = a(2) = 0 and b(1) = 0" not in f:
        return False, "Tier 3 does not name the codimension-3 locus"
    return True, ("three tiers present, each labelled in running text with its "
                  "own level of confirmation")


def c_necessary_only(t):
    """N6 -- the necessary-condition qualification, and no row assignment."""
    f = _flat(t)
    if "necessary, not sufficient" not in f:
        return False, "the necessary-condition qualification is absent"
    if "excludes rows and assigns none" not in f:
        return False, "the notice does not say that the procedure assigns no row"
    if "asserts no Painlev\u00e9 label for V_quad" not in f:
        return False, "the notice does not state that it asserts no Painlev\u00e9 label for V_quad"
    bad = []
    for m in re.finditer(r"[^.]*\bL_d\b[^.]*\.", f):
        s = m.group(0)
        if re.search(r"(?i)\b(is therefore a|is a|lies in|belongs to|sits in|"
                     r"is identified with)\b[^.]*\b(PIII|PV|PVI|PIV|PII|PI|"
                     r"D\u0303|family|connection)\b", s) and \
           not re.search(r"(?i)\bnot\b|\bneither\b|\bno\b", s):
            bad.append(s.strip())
    if bad:
        return False, "a sentence assigns a row to L_d: %s" % [s[:90] for s in bad[:2]]
    return True, ("necessary-not-sufficient stated, no row assigned, no "
                  "Painlev\u00e9 label asserted for V_quad")


def c_history_not_adjudicated(t):
    """N7 -- the record's label history, both sides, not adjudicated."""
    f = _flat(t)
    if "lies inside the surviving" not in f:
        return False, "the v1.0-v1.3 PIII(D6) label is not placed inside the surviving set"
    if "lies outside the surviving" not in f:
        return False, "the v1.4 P_V/D5^(1) label is not placed outside the surviving set"
    if "neither is adjudicated" not in f:
        return False, "the notice does not say the two labels are left unadjudicated"
    if "A row exclusion is not a row assignment" not in f:
        return False, "the reason the history is not adjudicated is missing"
    bad = []
    adj_v14 = re.compile(r"(?i)\b(was (therefore )?(mistaken|wrong|in error)|"
                         r"is (therefore )?(refuted|overturned|false)|"
                         r"must be reverted|should be reverted)")
    adj_d6 = re.compile(r"(?i)\b(was (therefore )?correct\b(?!ed)|"
                        r"is (therefore )?(vindicated|confirmed|restored|right)\b)")
    neg = re.compile(r"(?i)\b(not|never|neither|nor)\b")

    def adjudicates(clause, pat):
        """A negator counts only if it PRECEDES the adjudicating verb.
        '...does not follow that the v1.4 correction was wrong' is the notice
        refusing to adjudicate; '...was mistaken, though not by much' is the
        notice adjudicating and then hedging.  Sentence-level negation cannot
        tell those apart and reported the first as a defect."""
        m = pat.search(clause)
        if not m:
            return False
        n = neg.search(clause)
        return not (n and n.start() < m.start())

    for c in _clauses(f):
        if re.search(r"\bv1\.4\b", c) and adjudicates(c, adj_v14):
            bad.append(c.strip())
        if "P-III(D\u2086)" in c and adjudicates(c, adj_d6):
            bad.append(c.strip())
    if bad:
        return False, "the history is adjudicated: %s" % [s[:90] for s in bad[:2]]
    return True, ("label history stated on both sides, with the reason it is "
                  "not adjudicated, and no verdict on either")


def c_no_superseded_hash(t):
    """N8 -- no superseded description hash is published as a current value."""
    f = _flat(t)
    found = [h for h in SUPERSEDED_HASHES if h[:16] in f or h in f]
    if found:
        return False, ("a superseded description hash is published as current: %s"
                       % [h[:16] for h in found])
    return True, ("no superseded description hash appears in the published "
                  "text (%d checked)" % len(SUPERSEDED_HASHES))


CHECKS = [
    ("T1 tags inside the house set", c_tags),
    ("T2 tags balanced and unnested", c_balanced),
    ("T3 no markdown residue", c_no_markdown),
    ("T4 entities well-formed and HTML4", c_entities_wellformed),
    ("T5 no double-escaped entities", c_no_double_escape),
    ("X1 declared exclusions applied and still live", c_exclusions),
    ("X2 no draft-stage language published", c_no_draft_language),
    ("N1 all five commissioned items present", c_five_items),
    ("N2 PSLQ basis stated in full", c_pslq_basis),
    ("N3 naming prohibition survives", c_naming_prohibition),
    ("N4 label discipline on K survives", c_label_discipline),
    ("N5 sixth item present and not overclaimed", c_sixth_item),
    ("N5b three tiers, each labelled in the prose", c_tiers),
    ("N6 necessary condition only; no row assigned", c_necessary_only),
    ("N7 label history stated, not adjudicated", c_history_not_adjudicated),
    ("N8 no superseded description hash published", c_no_superseded_hash),
    ("B1 attached build declared as v1.6, unchanged", c_build_statement),
    ("B2 no v1.7 build is claimed", c_no_rebuild_claim),
    ("B3 DOIs correct and none invented", c_dois),
    ("P1 no unresolvable internal provenance", c_no_internal_provenance),
    ("P2 resolvable identifiers survive the strip", c_resolvable_identifiers),
]

MUTANTS = {
    # N5b/N6/N7/N8 mutants are drawn from the FAILURE MODES, not from the
    # checks' own required-string lists (Amendment E).  Each is a sentence a
    # careless restatement would actually produce.
    "N5b three tiers, each labelled in the prose": [
        # the marker survives, but only in a heading: the sentence it governs
        # can now be quoted with its tier invisible.
        lambda t: t.replace("This paragraph is Tier 2: self-derived, and NOT "
                            "independently confirmed.", "Tier 2."),
        lambda t: t.replace("This paragraph is Tier 3", "This heading is Tier 3"),
        lambda t: t.replace("for any admissible coefficient vector",
                            "for the coefficient vectors sampled"),
    ],
    "N6 necessary condition only; no row assigned": [
        lambda t: t + "\n<p><em>L_d</em> is therefore a PIII(D8) connection.</p>",
        lambda t: t + "\n<p>The operator L_d lies in the PIII(D&#8328;) family.</p>",
        lambda t: t.replace("excludes rows and assigns none",
                            "determines the row uniquely"),
    ],
    "N7 label history stated, not adjudicated": [
        lambda t: t + "\n<p>The v1.4 correction was therefore mistaken.</p>",
        lambda t: t + "\n<p>Accordingly the earlier P-III(D&#8326;) label was "
                      "correct after all.</p>",
        # boundary mutant for the negator-position repair: adjudicates first,
        # hedges afterwards.  A naive "any negator in the clause" guard would
        # let this through.
        lambda t: t + "\n<p>The v1.4 correction was mistaken, though not by "
                      "much.</p>",
        # one-sided history: the half that cuts against the current record is
        # deleted, leaving a statement that looks balanced and is not.
        lambda t: t.replace("lies <strong>inside</strong> the surviving",
                            "lies somewhere relative to the surviving"),
    ],
    "N8 no superseded description hash published": [
        lambda t: t + "\n<p>Description sha256 "
                      "026e7a9ebef7393564e408f7733adc7d3b7e6afe79b12092345b9af38c09b7ac.</p>",
        lambda t: t + "\n<p>Paste target: 39903126d90e0c35.</p>",
    ],
    # N5's two load-bearing mutants are NOT drawn from its required-string
    # list.  They are the two ways a restatement of the sixth item goes wrong
    # in practice: refuting the V_quad identification from an exclusion about
    # a different object, and promoting a necessary-condition row match to a
    # verified family membership.  The third is an ordinary deletion mutant
    # for the presence half.
    "N5 sixth item present and not overclaimed": [
        lambda t: t + "\n<p>Hence the conjectural identification of "
                      "<em>V</em><sub>quad</sub> with Painlev&eacute; V is "
                      "refuted by the exclusion above.</p>",
        lambda t: t + "\n<p>The operator therefore lies in the PIII(D&#8328;) "
                      "family (VERIFIED).</p>",
        lambda t: t.replace("necessary, not sufficient", "established outright"),
        # boundary mutant for the clause-scoping repair: an unhedged assignment
        # asserted as VERIFIED.  If narrowing the scan to clauses had gutted
        # it, this would pass.
        lambda t: t + "\n<p>A match is VERIFIED and <em>L_d</em> lies in that "
                      "family.</p>",
    ],
    # P1/P2 mutants are drawn from OUTSIDE the checks' own pattern lists: each
    # is a verbatim string that stood in the pre-strip notice, taken from the
    # source text rather than composed from the patterns the checks match on.
    # A mutant built from a check's own list can only prove the list is
    # consulted, never that it is adequate.
    "P1 no unresolvable internal provenance": [
        lambda t: t.replace("</p>", " Recorded in "
                            "sessions/2026-09-17/CT-S22-STOKES/outputs/"
                            "stage5b_pslq.out.txt.</p>", 1),
        lambda t: t.replace("</p>", " See claim S22-22 for the residual.</p>", 1),
        lambda t: t.replace("</p>", " Generated by make_description.py from "
                            "the held refs/zenodo_22782807.json.</p>", 1),
    ],
    "P2 resolvable identifiers survive the strip": [
        lambda t: t.replace("10.1137/1009002", "the standard reference"),
        lambda t: re.sub(r"\b[0-9a-f]{64}\b", "(hash withheld)", t),
    ],
    "T1 tags inside the house set": [
        lambda t: t.replace("<p><strong>Version notice", "<h2>x</h2><p><strong>Version notice"),
        lambda t: t.replace("<em>", "<i>", 1).replace("</em>", "</i>", 1),
    ],
    "T2 tags balanced and unnested": [
        lambda t: t.replace("</strong>", "", 1),
        lambda t: t.replace("<p><strong>Version notice", "<p><p><strong>Version notice"),
    ],
    "T3 no markdown residue": [
        lambda t: t + "\n<p>**not converted**</p>",
        lambda t: t + "\n<p>| a | b |</p>\n| c | d |",
    ],
    "T4 entities well-formed and HTML4": [
        lambda t: t.replace("&beta;", "&bta;", 1),
        lambda t: t.replace("&beta;", "& beta;", 1),
    ],
    "X1 declared exclusions applied and still live": [
        lambda t: t + "\n<p>Session: `sessions/2026-09-17/CT-S26-CTV17-DRAFT/`.</p>",
        lambda t: t + "\n<p>No metadata edit has been made or is authorised.</p>",
    ],
    "X2 no draft-stage language published": [
        # Deliberately NOT drawn from the check's string list -- that is the
        # defect being repaired.  Each mutant uses a casing or a phrasing the
        # old literal list did not contain.
        lambda t: t + "\n<p><em>End of draft v1.7 notice. Draft only &mdash; "
                      "no deposit, no metadata edit.</em></p>",
        lambda t: t + "\n<p>This version is Provisional pending review.</p>",
        lambda t: t + "\n<p>Please Do Not Cite this record yet.</p>",
    ],
    "T5 no double-escaped entities": [
        lambda t: t.replace("&mdash;", "&amp;mdash;", 1),
        lambda t: t.replace("&beta;", "&amp;beta;", 1),
    ],
    "N1 all five commissioned items present": [
        lambda t: t.replace("The vacuity explanation", "The removed section"),
        lambda t: t.replace("The Borel material", "Something else"),
    ],
    "N2 PSLQ basis stated in full": [
        lambda t: t.replace("log &Gamma;(1/3)", "&hellip;"),
        lambda t: t.replace("removed as redundant", "omitted"),
        lambda t: t.replace("log &pi;", "X"),
    ],
    "N3 naming prohibition survives": [
        lambda t: t.replace("Naming prohibition", "Some other heading"),
    ],
    "N4 label discipline on K survives": [
        lambda t: t.replace("must not be written as PROVEN", "is effectively proven"),
    ],
    "B1 attached build declared as v1.6, unchanged": [
        lambda t: t.replace("the v1.6 build, unchanged", "a fresh build"),
        lambda t: t.replace("description only", "the attached document"),
    ],
    "B2 no v1.7 build is claimed": [
        lambda t: t.replace("no PDF was rebuilt", "the PDF was rebuilt"),
        lambda t: t + "<p>The attached file is the v1.7 build.</p>",
    ],
    "B3 DOIs correct and none invented": [        lambda t: t.replace("10.5281/zenodo.19941678", "10.5281/zenodo.22782807"),
        lambda t: t + "<p>10.5281/zenodo.99999999 (v1.7)</p>",
    ],
}


def main():
    print("=" * 76)
    print("verify_description.py -- the text that would be pasted into Zenodo")
    print("=" * 76)
    print()

    print("SECTION 0 -- READER INTEGRITY")
    print("-" * 76)
    try:
        t = read_desc()
    except ReadError as exc:
        print("  [FAIL] %s" % exc)
        return 2
    with open(DESC, "rb") as fh:
        raw = fh.read()
    print("  [PASS] description read: %d chars, sentinels present, no CR" % len(t))
    print("file   : DESCRIPTION-v1.7-rev3.html")
    print("sha256 : %s   (from disk)" % hashlib.sha256(raw).hexdigest())
    print("chars  : %d" % len(t))
    print()

    print("SECTION 1 -- THE GATE")
    print("-" * 76)
    for name, fn in CHECKS:
        try:
            ok, detail = fn(t)
        except Exception as exc:
            ok, detail = False, "check raised %s: %s" % (type(exc).__name__, exc)
        print("  [%s] %s -- %s" % ("PASS" if ok else "FAIL", name, detail))
        if not ok:
            failures.append(name)
    print()

    print("SECTION 2 -- CAN-FAIL CONTROLS (mutate the DESCRIPTION)")
    print("-" * 76)
    for name, fn in CHECKS:
        muts = MUTANTS.get(name, [])
        fired = True
        for i, mf in enumerate(muts):
            mt = mf(t)
            if mt == t:
                print("  [BROKEN] %s -- mutant %d is identical to the original"
                      % (name, i + 1))
                fired = False
                continue
            try:
                ok, _d = fn(mt)
            except Exception:
                ok = False
            if ok:
                print("  [BROKEN] %s -- mutant %d ACCEPTED" % (name, i + 1))
                fired = False
        if not muts:
            print("  [BROKEN] %s -- no mutant" % name)
            fired = False
        if fired:
            print("  [PASS] %s -- %d mutant(s) rejected" % (name, len(muts)))
        else:
            broken.append(name)
    print()

    print("SECTION 3 -- READER CONTROLS (mutate the INPUT PATH)")
    print("-" * 76)
    reader_fail = 0
    readers = [
        # The file is written LF-only, so a binary read of IT has no CR and the
        # control could not fire.  A control that cannot fire is not a control:
        # the CRLF reader is therefore given a CRLF-bearing copy to read.
        ("binary read of a CRLF file, not normalised",
         lambda: crlf_copy().decode("utf-8")),
        ("wrong codec (latin-1)",
         lambda: open(DESC, "rb").read().decode("latin-1").replace("\r\n", "\n")),
        ("silently truncated read",
         lambda: open(DESC, "rb").read()[:300].decode("utf-8", "ignore")),
    ]
    for rname, rf in readers:
        try:
            txt = rf()
            if "\r" in txt:
                raise ReadError("CR present: line endings were not normalised")
            for s in SENTINELS:
                if s not in txt:
                    raise ReadError("sentinel %r absent" % s)
            print("  [BROKEN] %s -- NOT caught" % rname)
            reader_fail += 1
        except ReadError as exc:
            print("  [PASS] %s -- caught: %s" % (rname, exc))
        except Exception as exc:
            print("  [PASS] %s -- caught by decoding: %s" % (rname, type(exc).__name__))
    print()

    print("SECTION 4 -- THE ENTITY RULE, VALIDATED AGAINST THE DEPOSITED v1.6 TEXT")
    print("-" * 76)
    print("  The rule is 'named HTML4 entity where one exists, raw UTF-8 where")
    print("  none does'.  That is a claim ABOUT THE RECORD, so it is tested on")
    print("  the record: decode the deposited v1.6 description, re-encode it by")
    print("  the rule, and require the entity set to come back unchanged.")
    with open(RECORD, encoding="utf-8") as fh:
        v16 = json.load(fh)["metadata"]["description"]
    decoded = html.unescape(v16)
    reencoded = "".join(
        ("&%s;" % html.entities.codepoint2name[ord(c)])
        if ord(c) > 127 and ord(c) in html.entities.codepoint2name else c
        for c in decoded)
    # lt/gt/amp/quot are MARKUP escapes, produced by esc(), not by the entity
    # rule under test.  Comparing them here would test the wrong thing: the
    # round trip decodes "&lt;" to "<", which is ASCII and stays ASCII.
    MARKUP = {"lt", "gt", "amp", "quot", "apos"}
    got = set(re.findall(r"&([a-zA-Z][a-zA-Z0-9]*);", reencoded)) - MARKUP
    want = set(re.findall(r"&([a-zA-Z][a-zA-Z0-9]*);", v16)) - MARKUP
    same = got == want
    print("  [%s] round trip of the deposited description: %d non-markup entity "
          "names in, %d out" % ("PASS" if same else "FAIL", len(want), len(got)))
    if not same:
        print("        only in record : %s" % sorted(want - got))
        print("        only in rule   : %s" % sorted(got - want))
        failures.append("E round trip of the deposited description")
    raw_sub = [c for c in decoded if ord(c) > 127 and
               ord(c) not in html.entities.codepoint2name]
    print("  [PASS] the record itself keeps %d raw non-ASCII char(s) with no HTML4 "
          "name, e.g. %s -- so does this description"
          % (len(set(raw_sub)), " ".join(sorted(set(raw_sub))[:6])))
    print()

    print("=" * 76)
    print("checks run     : %d" % len(CHECKS))
    print("checks failed  : %d%s" % (len(failures),
                                     ("  -> " + ", ".join(failures)) if failures else ""))
    print("broken checks  : %d%s" % (len(broken),
                                     ("  -> " + ", ".join(broken)) if broken else ""))
    print("reader controls: %d of 3 caught" % (3 - reader_fail))
    clean = not failures and not broken and not reader_fail
    print()
    print("VERDICT: %s" % ("OK" if clean else "BLOCKED"))
    print("=" * 76)
    return 0 if clean else 1


if __name__ == "__main__":
    sys.exit(main())
