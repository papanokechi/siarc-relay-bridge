"""Emit claims.jsonl for CT-S3B-RINF with sha256 of each output file."""
import hashlib, json, os

HERE = os.path.dirname(os.path.abspath(__file__))


def sha(name):
    with open(os.path.join(HERE, name), "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


CLAIMS = [
    dict(claim_id="S3B-01", task_id="P3-A",
         claim=("The prompt's Part A acceptance threshold is ill-posed: the tail "
                "Sum_{k>N} |r|/|b(k)b(k-1)| for V_quad (b(n)=3n^2+n+1) decays like "
                "1/(27 N^3), so a 1e-3000 bound requires N ~ 10^999.5 and is "
                "unreachable. Reported as finding S3B-F1; a Neville extrapolation "
                "in 1/n was pre-registered as the substitute before any run."),
         evidence_type="computation", dps=400, reproducible=True,
         script="rinf_amplitude.py", output_hash=sha("rinf.json"),
         label="PROVEN"),
    dict(claim_id="S3B-02", task_id="P3-A",
         claim=("For V_quad, b(n)=3n^2+n+1, r_inf = lim Q_n / prod_{k<=n} b(k) "
                "= 1.016604441058510936337097213267657686917983514389... , "
                "nonzero. N-vs-2N agreement 180.25 digits at dps 400 "
                "(N=60000, L=40)."),
         evidence_type="computation", dps=400, reproducible=True,
         script="rinf_amplitude.py", output_hash=sha("rinf.json"),
         label="VERIFIED"),
    dict(claim_id="S3B-03", task_id="P3-A",
         claim=("No root of b(n)=3n^2+n+1 is a positive integer (the roots are a "
                "complex-conjugate pair), so Gamma(1-r_i) is finite and the "
                "Part A halt condition does not fire."),
         evidence_type="computation", dps=400, reproducible=True,
         script="rinf_amplitude.py", output_hash=sha("rinf.json"),
         label="PROVEN"),
    dict(claim_id="S3B-04", task_id="P3-B",
         claim=("Closed form derived for the leading amplitude: with "
                "b(n)=beta_d prod_i (n-r_i), "
                "Q_n/Gamma(dn+1) = K (beta_d/d^d)^n n^s (1+O(1/n)) where "
                "s = beta_{d-1}/beta_d + (d-1)/2 and "
                "K = r_inf (2pi)^((d-1)/2) d^(-1/2) / prod_i Gamma(1-r_i). "
                "Full derivation in DERIVATION.md; one classical ingredient "
                "(Gamma(n+1-r)/Gamma(n+1) ~ n^-r) is quoted, recorded as Gap G1."),
         evidence_type="file_inspection", dps=None, reproducible=True,
         script="DERIVATION.md", output_hash=sha("DERIVATION.md"),
         label="STRUCTURAL"),
    dict(claim_id="S3B-05", task_id="P3-B",
         claim=("The closed form for K agrees with the numerically computed "
                "Q_n/Gamma(dn+1) limit to between 109.66 and 114.69 decimal "
                "digits for all 8 test polynomials spanning d=2,3,4, including "
                "cases with negative K and with sign-changing b. Pre-registered "
                "falsifier F-B (agreement below 20 digits) did NOT fire."),
         evidence_type="computation", dps=160, reproducible=True,
         script="rinf_amplitude.py", output_hash=sha("amplitude.json"),
         label="VERIFIED"),
    dict(claim_id="S3B-06", task_id="P3-B",
         claim=("Vacuity control passes: recomputing K with the prod_i "
                "Gamma(1-r_i) factor omitted collapses agreement from ~110 "
                "digits to at most 0.75 digits in every case, so the test is "
                "sensitive to the quantity the hypothesis is about."),
         evidence_type="computation", dps=160, reproducible=True,
         script="rinf_amplitude.py", output_hash=sha("amplitude.json"),
         label="VERIFIED"),
    dict(claim_id="S3B-07", task_id="P3-B",
         claim=("Leading Borel-singular germ, stated in the P1-established "
                "normalisation: B(w) = Sum Q_n w^n / Gamma(dn+1) has its "
                "radius-of-convergence singularity at w* = d^d/beta_d with "
                "B(w) ~ K Gamma(s+1) (1 - w/w*)^{-(s+1)}, i.e. germ coefficient "
                "A = K Gamma(s+1) and exponent -(s+1) = rho_d. Per the P1 "
                "verdict this singularity is at xi_0, NOT the zeta*=4/sqrt(3) "
                "singularity, so A must not be called S_{zeta*}."),
         evidence_type="file_inspection", dps=None, reproducible=True,
         script="DERIVATION.md", output_hash=sha("DERIVATION.md"),
         label="STRUCTURAL"),
    dict(claim_id="S3B-08", task_id="P3-C",
         claim=("PSLQ probe on r_inf(V_quad) over the basis frozen in PREREG.md "
                "Sec.5 (1, pi, sqrt3, Gamma(1/3), Gamma(2/3), log2, log3, "
                "|Gamma(1-r1)|, Re Gamma(1-r1)) returns NULL at dps 500, 1000 "
                "and 2000, with maxcoeff 1e6. NULL result: no integer relation "
                "of height <= 1e6 exists over this 10-element basis."),
         evidence_type="computation", dps=2000, reproducible=True,
         script="partC_pslq.py", output_hash=sha("pslq.json"),
         label="VERIFIED"),
    dict(claim_id="S3B-09", task_id="P3-C",
         claim=("r_inf(V_quad) computed to 2317.8 confirmed digits (N-vs-2N "
                "agreement, N=20000, L=640, stride=520, dps 2800), superseding "
                "the 180-digit Part A value and the ~13.5-digit d=2 value "
                "recorded in CT-S2-RHO-D4/d2_anchor.json. All three are "
                "mutually consistent."),
         evidence_type="computation", dps=2800, reproducible=True,
         script="partC_pslq.py", output_hash=sha("rinf_highprec.txt"),
         label="VERIFIED"),
]

with open(os.path.join(HERE, "claims.jsonl"), "w") as f:
    for c in CLAIMS:
        f.write(json.dumps(c) + "\n")
print(f"wrote claims.jsonl with {len(CLAIMS)} claims")
for c in CLAIMS:
    print(f"  {c['claim_id']}  {c['label']:<11} {c['output_hash'][:16]}")
