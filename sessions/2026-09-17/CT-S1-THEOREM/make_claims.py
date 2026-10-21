import hashlib, json, os
H=os.path.dirname(os.path.abspath(__file__))
def sha(n):
    return hashlib.sha256(open(os.path.join(H,n),"rb").read()).hexdigest()
C=[
 ("S1-01","P4-A","PROVEN","file_inspection","theorem.tex",
  "r_n = Q_n / prod_{k<=n} b(k) converges for every b of degree d>=1 with b(k)!=0 for k>=1, with no hypothesis on the limit; moreover r_inf - r_n = O(n^{-(2d-1)}). Proposition prop:exists in theorem.tex; all sub-steps complete."),
 ("S1-02","P4-A","PROVEN","file_inspection","theorem.tex",
  "If b(n)>0 for all n>=1 then r_n is strictly increasing with r_n>=1, hence r_inf>=1>0 and hypothesis (H) holds automatically. Proposition prop:positive."),
 ("S1-03","P4-A","PROVEN","file_inspection","theorem.tex",
  "Part (i): under (A1) and (H), lim |Q_n/(dn)!|^(1/n) = |beta_d|/d^d, so Sum Q_n w^n/(dn)! has radius d^d/|beta_d| in w and xi_0 = d/|beta_d|^(1/d) in zeta=w^(1/d). Proved WITHOUT Gamma asymptotics: Step 3 uses a combinatorial multinomial sandwich, not Stirling. Theorem thm:radius; all five steps complete."),
 ("S1-04","P4-A","STRUCTURAL","file_inspection","theorem.tex",
  "Part (ii): Q_n/Gamma(dn+1) = K (beta_d/d^d)^n n^s (1+O(1/n)) with s = beta_{d-1}/beta_d + (d-1)/2 and K as derived in CT-S3B-RINF. Theorem thm:growth. Steps 1,2,5 complete; Steps 3,4 rest on Gap G1 (the classical ratio Gamma(n+1-r)/Gamma(n+1) ~ n^-r is quoted, not proved). Hence STRUCTURAL, not PROVEN."),
 ("S1-05","P4-A","STRUCTURAL","file_inspection","theorem.tex",
  "Pincherle interpretation: (H) states exactly that Q_n is not the minimal solution of the three-term recurrence; the minimal subspace has codimension one, so (H) is generic. Pincherle's theorem cited as standard (Gautschi 1967; Lorentzen-Waadeland Ch.IV). Interpretive only; no other result depends on it."),
 ("S1-06","P4-B","VERIFIED","build","lean/XiZero/Basic.lean",
  "lake build on sessions/2026-09-17/CT-S1-THEOREM/lean succeeds: 'Build completed successfully (8477 jobs)' with 7 'declaration uses sorry' warnings and ZERO errors, against Mathlib v4.30.0. This establishes that the Lean statements TYPECHECK and that every Mathlib name used exists; it establishes nothing about provability. No sorry was discharged."),
 ("S1-07","P4-B","VERIFIED","file_inspection","lean/.lake/packages/mathlib",
  "Mathlib inventory by direct search of the installed source tree: CONFIRMED FormalMultilinearSeries.radius_eq_liminf (Analysis/Analytic/RadiusLiminf.lean:36), radius_inv_eq_limsup, ofScalars_radius_eq_of_tendsto (Analysis/Analytic/OfScalars.lean:237), Stirling.factorial_isEquivalent_stirling, Stirling.tendsto_stirlingSeq_sqrt_pi (Stirling.lean:231), Stirling.le_factorial_stirling, Real.multipliable_one_add_of_summable (SpecificLimits/Summable.lean:49), Real.multipliable_of_summable_log, tendsto_pow_atTop_nhds_zero_of_lt_one. NOT FOUND: a c^(1/n)->1 lemma, multinomial (dn)!/(n!)^d bounds, and a directly usable non-vanishing-infinite-product lemma."),
]
out=[]
for cid,tid,lab,ev,scr,txt in C:
    out.append(dict(claim_id=cid,task_id=tid,claim=txt,evidence_type=ev,dps=None,
                    reproducible=True,script=scr,output_hash=sha(scr) if os.path.isfile(os.path.join(H,scr)) else None,
                    label=lab))
open(os.path.join(H,"claims.jsonl"),"w").write("\n".join(json.dumps(c) for c in out)+"\n")
print("wrote",len(out),"claims")
for c in out: print(" ",c["claim_id"],c["label"],(c["output_hash"] or "-")[:16])
