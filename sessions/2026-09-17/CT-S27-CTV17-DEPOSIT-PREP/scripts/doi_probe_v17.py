"""doi_probe_v17.py -- CT-S27-CTV17-DEPOSIT-PREP

READ-ONLY.  Resolves every external source that will appear in the v1.7
description's bibliography, and records what the resolver ACTUALLY returned.

Why this exists: the corpus has already caught one hallucinated DOI --
discrepancy_log.json records that 10.1007/BF02547452, offered for Birkhoff
1930, resolves to a 1995 chemistry paper.  So no identifier here is written
from memory.  Each is either

  (a) carried forward from a corpus record that already verified it, and
      RE-VERIFIED here against Crossref, or
  (b) discovered here by a title query and reported with the resolver's own
      title so a reader can see the match was not assumed.

A row is only fit to publish if this script prints RESOLVED for it.
"""

import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
SESSION = os.path.dirname(HERE)
UA = "siarc-relay-bridge/CT-S27 (read-only citation check; mailto:papanokechi@users.noreply.github.com)"

# (slot, known DOI or None, expected-title fragment, provenance of the DOI)
KNOWN = [
    ("gautschi1967", None, "Computational Aspects of Three-Term Recurrence",
     "not recorded in the corpus -- discovered here by title query"),
    ("birkhoff_trjitzinsky1933", "10.1007/bf02398269",
     "Analytic theory of singular difference equations",
     "CT corpus doi_resolution_probe.md, Crossref-canonical, marked YES"),
    ("wong_li_II_1992", "10.1002/sapm1992874289",
     "Asymptotic Expansions for Second-Order Linear Difference Equations",
     "CT corpus AUDIT.md; paywalled, NOT OBTAINED"),
]

# Sources whose identifier is a stable URL rather than a DOI.
URLS = [
    ("dlmf_3_6", "https://dlmf.nist.gov/3.6", "Existence"),
    ("dlmf_2_9", "https://dlmf.nist.gov/2.9", "Difference Equations"),
    ("nemes2025", "https://arxiv.org/abs/2508.15246", "connection"),
    ("wong_zhao2022", "https://arxiv.org/abs/2204.09305", "difference equation"),
    ("ibrahim_salvy2023", "https://arxiv.org/abs/2306.05930", "ositivity"),
    ("odlyzko_asymptotic", "https://www-users.cse.umn.edu/~odlyzko/doc/asymptotic.enum.pdf",
     None),
]

# The DOI the corpus caught as hallucinated.  Probed deliberately: if this
# script ever reports it RESOLVED to a Birkhoff paper, the probe is broken.
POISON = ("10.1007/BF02547452", "Birkhoff 1930 -- KNOWN BAD, must NOT match Birkhoff")

results = []


def get(url, accept=None, timeout=45):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    if accept:
        req.add_header("Accept", accept)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.read(), r.geturl()


def crossref_by_doi(doi):
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="")
    try:
        st, body, _ = get(url, "application/json")
    except Exception as exc:
        return None, "resolver error: %s" % exc
    d = json.loads(body.decode("utf-8"))["message"]
    return {
        "doi": d.get("DOI"),
        "title": (d.get("title") or [""])[0],
        "author": "; ".join(
            "%s %s" % (a.get("given", ""), a.get("family", "")) for a in d.get("author", [])
        ).strip(),
        "container": (d.get("container-title") or [""])[0],
        "volume": d.get("volume"), "issue": d.get("issue"),
        "page": d.get("page"),
        "year": (d.get("issued", {}).get("date-parts") or [[None]])[0][0],
    }, None


def crossref_by_title(frag):
    url = ("https://api.crossref.org/works?rows=3&query.bibliographic="
           + urllib.parse.quote(frag))
    try:
        st, body, _ = get(url, "application/json")
    except Exception as exc:
        return None, "resolver error: %s" % exc
    items = json.loads(body.decode("utf-8"))["message"]["items"]
    if not items:
        return None, "no Crossref hit"
    d = items[0]
    return {
        "doi": d.get("DOI"),
        "title": (d.get("title") or [""])[0],
        "author": "; ".join(
            "%s %s" % (a.get("given", ""), a.get("family", "")) for a in d.get("author", [])
        ).strip(),
        "container": (d.get("container-title") or [""])[0],
        "volume": d.get("volume"), "issue": d.get("issue"),
        "page": d.get("page"),
        "year": (d.get("issued", {}).get("date-parts") or [[None]])[0][0],
    }, None


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()


print("=" * 78)
print("doi_probe_v17.py -- READ-ONLY citation resolution")
print("Nothing here is written from memory.  Each identifier is resolved and")
print("the RESOLVER'S OWN title is printed so the match can be seen, not assumed.")
print("=" * 78)
print()

print("SECTION 1 -- DOIs")
print("-" * 78)
for slot, doi, expect, prov in KNOWN:
    if doi:
        meta, err = crossref_by_doi(doi)
        how = "by DOI"
    else:
        meta, err = crossref_by_title(expect)
        how = "by TITLE QUERY"
    time.sleep(1)
    if err:
        print("  [UNRESOLVED] %-26s %s" % (slot, err))
        results.append((slot, "UNRESOLVED", None))
        continue
    ok = norm(expect) in norm(meta["title"])
    print("  [%s] %s  (%s)" % ("RESOLVED  " if ok else "MISMATCH  ", slot, how))
    print("       provenance : %s" % prov)
    print("       doi        : %s" % meta["doi"])
    print("       title      : %s" % meta["title"])
    print("       author     : %s" % meta["author"])
    print("       venue      : %s %s(%s) %s, %s"
          % (meta["container"], meta["volume"] or "", meta["issue"] or "",
             meta["page"] or "", meta["year"]))
    if not ok:
        print("       EXPECTED   : ...%s..." % expect)
    results.append((slot, "RESOLVED" if ok else "MISMATCH", meta))
print()

print("SECTION 2 -- POISON CONTROL (a known-bad DOI the corpus already caught)")
print("-" * 78)
bad_doi, why = POISON
meta, err = crossref_by_doi(bad_doi)
time.sleep(1)
if err:
    print("  [INCONCLUSIVE] %s did not resolve: %s" % (bad_doi, err))
else:
    fires = "birkhoff" not in norm(meta["author"])
    print("  [%s] %s" % ("PASS" if fires else "BROKEN", why))
    print("       resolves to: %r by %s (%s)"
          % (meta["title"], meta["author"], meta["year"]))
    print("       -> the probe reports what the DOI IS, not what it was claimed")
    print("          to be; a title check on this row would reject it.")
    results.append(("poison-control", "PASS" if fires else "BROKEN", meta))
print()

print("SECTION 3 -- URL-IDENTIFIED SOURCES")
print("-" * 78)
for slot, url, expect in URLS:
    try:
        st, body, final = get(url)
        text = body[:200000].decode("utf-8", "replace")
        ok = (st == 200) and (expect is None or expect.lower() in text.lower())
        title = re.search(r"<title>(.*?)</title>", text, re.S | re.I)
        print("  [%s] %-18s %s" % ("REACHED  " if ok else "CHECK    ", slot, url))
        print("       http %s, %d bytes%s" % (st, len(body),
              (", title: " + re.sub(r"\s+", " ", title.group(1)).strip()[:90]) if title else ""))
        if expect and expect.lower() not in text.lower():
            print("       expected text %r NOT found on the page" % expect)
        results.append((slot, "REACHED" if ok else "CHECK", url))
    except Exception as exc:
        print("  [UNREACHED] %-18s %s -- %s" % (slot, url, exc))
        results.append((slot, "UNREACHED", url))
    time.sleep(1)
print()

bad = [r for r in results if r[1] in ("MISMATCH", "UNRESOLVED", "UNREACHED", "BROKEN")]
print("=" * 78)
print("rows probed : %d" % len(results))
print("not fit to publish: %d%s"
      % (len(bad), ("  -> " + ", ".join("%s(%s)" % (r[0], r[1]) for r in bad)) if bad else ""))
print()
print("Any row above that is not RESOLVED or REACHED must NOT be written into")
print("the description as a resolvable citation.  Report it as unobtained.")
print("=" * 78)
sys.exit(0)
