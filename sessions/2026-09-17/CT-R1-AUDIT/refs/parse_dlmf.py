import re, html, hashlib, pathlib

p = pathlib.Path(r"C:\LocalWork\siarc-relay-bridge\sessions\2026-09-17\CT-R1-AUDIT\refs\dlmf_5.11.html")
src = p.read_text(encoding="utf-8", errors="replace")
print("sha256:", hashlib.sha256(p.read_bytes()).hexdigest())

# strip tags, keep the alt/title text that carries the equation labels
txt = re.sub(r"<script.*?</script>", " ", src, flags=re.S | re.I)
txt = re.sub(r"<style.*?</style>", " ", txt, flags=re.S | re.I)
# pull alt attributes (MathML/img alt often holds the readable formula)
alts = re.findall(r'alt="([^"]{5,400})"', txt)
plain = html.unescape(re.sub(r"<[^>]+>", " ", txt))
plain = re.sub(r"[ \t\xa0]+", " ", plain)

for tag in ("5.11.11", "5.11.12", "5.11.13", "5.11.14", "5.11(iii)", "5.11(i)"):
    idxs = [m.start() for m in re.finditer(re.escape(tag), plain)]
    print(f"\n==== {tag}: {len(idxs)} occurrence(s) ====")
    for i in idxs[:3]:
        print(repr(plain[max(0, i - 420):i + 420]))
        print("   ---")

print("\n==== alt texts mentioning G_k or ph z ====")
for a in alts:
    if "G" in a and ("ph" in a or "Γ" in a or "Gamma" in a):
        print(" *", a[:300])
