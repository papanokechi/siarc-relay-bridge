"""CT-R1-AUDIT R6: record the independent check of CT-S8-LITCHECK (deposit gate 3)."""
import hashlib
import json
from pathlib import Path

ROOT = Path(r"C:\LocalWork\siarc-relay-bridge\sessions\2026-09-17")
S = ROOT / "CT-R1-AUDIT"
img = S / "refs" / "gautschi_p34_bot.png"
h = hashlib.sha256(img.read_bytes()).hexdigest()
hpdf = hashlib.sha256((ROOT / "CT-S8-LITCHECK" / "refs" / "gautschi1967.pdf").read_bytes()).hexdigest()

NEW = [
    ("R1-36",
     "Gautschi, SIAM Review 9(1) 1967, hypothesis (2.8) on journal p.34 reads EXACTLY: 'a_n ~ a n^alpha, "
     "b_n ~ b n^beta, ab != 0; alpha, beta real; n -> infinity', with Newton-Puiseux points P0(0,0), "
     "P1(1,alpha), P2(2,beta). The reality condition is on the EXPONENTS, not on the coefficients. Verified "
     "by re-rendering the page from the PDF at 3x (refs/gautschi_p34_bot.png) because the OCR layer rendered "
     "this as 'ab 0; a, real', which would have wrongly suggested the leading coefficient must be real and "
     "hence that Perron-Kreuser does not cover complex beta_d. It does cover it.",
     "INSPECTED", "file_inspection", h),
    ("R1-37",
     "Result 1 (the radius / nth-root theorem, theorem.tex part (i)) is PRIOR ART: it is a corollary of the "
     "Perron-Kreuser theorem as stated in Gautschi Theorem 2.3(a), p.35. Writing Q_{n+1} - b(n+1)Q_n - "
     "Q_{n-1} = 0 in Gautschi's form (2.1) gives a_n ~ -beta_d n^d and b_n = -1, so alpha=d, beta=0, "
     "hypotheses (2.2) and (2.8) hold, and P1(1,d) lies above the segment (0,0)-(2,0) for every d >= 1, so "
     "case (a) applies and Q_{n+1}/Q_n ~ beta_d n^d. Stirling then gives |Q_n/(dn)!|^(1/n) -> "
     "|beta_d|/d^d. CT-S8-LITCHECK's finding is CONFIRMED by independent re-derivation from the verified "
     "page images.", "STRUCTURAL", "computation", h),
    ("R1-38",
     "The decomposition of Result 1 into classical parts is complete, leaving no new residue: Perron-Kreuser "
     "supplies the ratio law for the dominant solution and applies to our recurrence UNCONDITIONALLY (it "
     "needs no analogue of (H)); hypothesis (H) is exactly the statement that Q_n is not the minimal "
     "solution, which is Pincherle's theorem (Gautschi Thm 1.1 p.31, DLMF 3.6(ii)); and the passage from the "
     "ratio law to the radius is routine Stirling.", "STRUCTURAL", "computation", h),
    ("R1-39",
     "Whether the explicit growth exponent s = beta_{d-1}/beta_d + (d-1)/2 is already in print is NOT "
     "ESTABLISHED. DLMF 2.9 gives explicit exponents only for bounded coefficients and explicitly defers the "
     "case of eq. 2.9.14 (ours: P=d, Q=0) to Wong & Li, Stud. Appl. Math. 87(4) 1992, 289-324, which is "
     "paywalled (Wiley HTTP 403) and was NOT OBTAINED. Recorded as NOT FOUND in the sources obtained by the "
     "methods used, NOT as new. This is the single blocking item for deposit gate 3 and cannot be closed "
     "from open sources; it requires operator action.", "INSPECTED", "file_inspection", None),
    ("R1-40",
     "CT-S8-LITCHECK independently derived and numerically verified (60 dps, N=4000, four polynomials "
     "d=1,2,3) the closed form K = r_inf (2pi)^((d-1)/2) / (sqrt(d) prod_i Gamma(1-r_i)), reproducing P3's "
     "amplitude without access to P3's derivation. This materially strengthens the K result at the same time "
     "as Result 1 is demoted.", "VERIFIED", "computation", None),
    ("R1-41",
     "The NOT FOUND verdict on K carries less weight than it appears to, pending R1-39. Result 1 was found "
     "to be classical only once the search term 'Perron-Kreuser' surfaced, and Wong & Li -- the source most "
     "likely to contain Result 2 and plausibly related to K -- was never read. The K novelty claim should "
     "not be relied upon until the Wong & Li gap is closed.", "STRUCTURAL", "file_inspection", None),
    ("R1-42",
     "Deposit gate 3 is RETURNED but NOT CLOSED. The note's contribution claim as drafted is no longer "
     "supportable: Result 1 must be presented as a corollary of Perron-Kreuser with attribution, Result 2's "
     "status is undetermined pending Wong & Li, and Result 3 (K) is the strongest remaining candidate. The "
     "vacuity explanation is unaffected and was NOT FOUND in the literature searched.",
     "INSPECTED", "file_inspection", None),
]
with (S / "claims.jsonl").open("a", encoding="utf-8") as f:
    for cid, claim, label, ev, oh in NEW:
        f.write(json.dumps({"claim_id": cid, "task_id": "CT-R1-AUDIT-R6", "claim": claim, "label": label,
                            "evidence_type": ev, "dps": None, "reproducible": True,
                            "script": "sessions/2026-09-17/CT-R1-AUDIT/VERIFY-S8.md",
                            "output_hash": oh}, ensure_ascii=False) + "\n")

import collections
lab, rev, bad = collections.Counter(), collections.Counter(), []
for p in ROOT.glob("*/claims.jsonl"):
    for l in p.read_text(encoding="utf-8").splitlines():
        if not l.strip():
            continue
        r = json.loads(l)
        lab[r.get("label")] += 1
        if r.get("evidence_type") == "proof":
            rev[r.get("review")] += 1
        if r.get("evidence_type") == "file_inspection" and r.get("label") == "PROVEN":
            bad.append(r["claim_id"])
print("gautschi p34 image sha256:", h)
print("gautschi1967.pdf sha256:", hpdf)
print("corpus:", sum(lab.values()), dict(lab))
print("proof review:", dict(rev))
print("rule 1(a) violations:", bad or "none")
