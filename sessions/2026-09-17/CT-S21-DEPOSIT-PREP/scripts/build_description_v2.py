"""Build the edited v1.3 description for record 22831933.

Source of truth for the two edits is DESCRIPTION-EDIT.md, parsed here, so the
paste sheet cannot drift from the edit sheet or from verify_description_edit.py.

Echoes every derived value: exit 0 proves nothing -- S21-74.
"""
import hashlib
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
SHEET = HERE / "DESCRIPTION-EDIT.md"
LIVE = HERE / "outputs" / "live_desc.html"
OUT_HTML = HERE / "outputs" / "description_v1.3_edited.html"


def fenced_after(text, heading_re):
    """Return the first fenced block following a heading matching heading_re."""
    m = re.search(heading_re, text, re.M)
    if not m:
        raise SystemExit("FAIL: heading not found: %s" % heading_re)
    block = re.search(r"```\n(.*?)```", text[m.end():], re.S)
    if not block:
        raise SystemExit("FAIL: no fenced block after %s" % heading_re)
    return " ".join(block.group(1).split())


def main():
    sheet = SHEET.read_text(encoding="utf-8")
    live = LIVE.read_text(encoding="utf-8")

    label = fenced_after(sheet, r"^## Edit 1 .*$")
    boundary = fenced_after(sheet, r"^## Edit 2 .*$")
    print("edit 1 label    :", label)
    print("edit 2 boundary :", boundary[:60], "...", len(boundary), "chars")

    paras = re.findall(r"<p>(.*?)</p>", live, re.S)
    print("paragraphs read :", len(paras))
    if len(paras) != 10:
        raise SystemExit("FAIL: expected 10 paragraphs, got %d" % len(paras))

    # Assertions, not searches: each anchor is resolved by index and checked.
    anchors = {
        0: "This notice records five items",
        4: "Quotations from the cited literature",
        5: "We study the resurgence",
        8: "<strong>Version 1.1",
        9: "<strong>Version 1.2",
    }
    for idx, opening in anchors.items():
        got = paras[idx].strip()[: len(opening)]
        print("  anchor p%-2d      : %-38s %s" % (idx, opening, "OK" if got == opening else "MISMATCH -> " + got))
        if got != opening:
            raise SystemExit("FAIL: paragraph %d is not the expected anchor" % idx)

    if "<strong>Version 1.3" in live:
        raise SystemExit("FAIL: the v1.3 label is already present -- edit already applied?")
    if boundary in " ".join(live.split()):
        raise SystemExit("FAIL: the boundary paragraph is already present -- edit already applied?")

    new = list(paras)
    new[0] = "<strong>" + label + "</strong> " + paras[0].strip()
    new.insert(5, boundary)
    print("paragraphs out  :", len(new), "(10 + 1 inserted)")

    html = "\n".join("<p>%s</p>" % p.strip() for p in new)
    # Raw U+21A6 survives the API round-trip but not necessarily a paste through
    # an editor or terminal; emit it as a numeric entity. Renders identically.
    n_mapsto = html.count("\u21a6")
    html = html.replace("\u21a6", "&#8614;")
    print("mapsto -> &#8614;:", n_mapsto, "replaced")
    OUT_HTML.write_text(html, encoding="utf-8", newline="\n")
    digest = hashlib.sha256(html.encode("utf-8")).hexdigest()
    print("wrote           :", OUT_HTML.name, len(html), "chars")
    print("sha256          :", digest)

    # The invariants the edit must not disturb. Each C1 phrase appears twice
    # after the edit: once in the retained abstract, once quoted back in the
    # boundary paragraph. A count of 1 would mean the abstract was edited.
    for name, needle, want in [
        ("C1 sentence 1 (p5)", "forces both finite singularities to be apparent", 2),
        ("C1 sentence 2 (p7)", "roots of the Wallis characteristic polynomial", 2),
        ("no 'item 1 above'", "item 1 above", 0),
    ]:
        n = html.count(needle)
        print("  %-20s: %d (want %d) %s" % (name, n, want, "OK" if n == want else "FAIL"))
        if n != want:
            raise SystemExit("FAIL: invariant disturbed: %s" % name)
    return 0


if __name__ == "__main__":
    sys.exit(main())
