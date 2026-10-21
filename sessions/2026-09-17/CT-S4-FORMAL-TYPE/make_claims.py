import hashlib, json, os
H=os.path.dirname(os.path.abspath(__file__))
sha=lambda n: hashlib.sha256(open(os.path.join(H,n),"rb").read()).hexdigest()
FT=sha("formal_type.json")
C=[
("S4-01","P5-1","STRUCTURAL","file_inspection","REPORT.md",
 "No 'Conjecture 4.1' exists in the V_quad companion materials. Searching all of sessions/2026-06-15/VQUAD-PERIODREP-PAPER-001 returns only Fresan-Jossen Conjecture 1.3.2 and the descriptively-referenced 'master conjecture of the Sakai-stratification program' part (ii)(a) in section-7.md; section 4 is 'The main identity and its normalisation' and contains a theorem, not a conjecture. The D5^(1) attribution rests on VQ-N1/verdict.md (2026-05-29) and section-7.md. Finding S4-F1: operator must supply the correct pointer."),
("S4-02","P5-1","STRUCTURAL","file_inspection","REPORT.md",
 "The D5^(1) conjecture is NOT about the f(z)=Sum Q_n z^n ODE. Per section-2.md L54-57 and rmk:provenance, L_phi is 'the scalar (Schroedinger) reduction of the V_quad Painleve-V linear problem' and annihilates phi(z)=Sum a_n z^n, the Riccati/WKB series seeded by sigma=-1/sqrt3 -- a different series from the PCF numerator generating function. Both systems were therefore analysed, as P5 step 1 directs."),
("S4-03","P5-2","PROVEN","computation","formal_type.py",
 "System A derived and certified: f(z)=Sum Q_n z^n for b(n)=3n^2+n+1 satisfies 3z^3 f'' + 10 z^2 f' + (z^2+5z-1) f = -1. The residual against the exact integer sequence Q=1,5,76,2361,125209,10144290,... vanishes identically at every order z^0..z^38 in exact arithmetic. Falsifier F2 did not fire."),
("S4-04","P5-2","PROVEN","computation","formal_type.py",
 "System B transcription certified two independent ways: (a) the paper's factorisation q2 = 4(2sqrt3-3) z^2 (z^2+z+3) expands exactly to the listed q2; (b) recomputing r = a^2/4 + a'/2 - b from (q0,q1,q2) reproduces the paper's printed r(z) = (11z^4+4z^2+4z+12)/(4 z^4 (z^2+z+3)^2) exactly. This validates the transcription and independently confirms the paper's eq:r. Falsifier F1 did not fire."),
("S4-05","P5-2","PROVEN","computation","formal_type.json",
 "System A formal type (exact, from normal form r_A = (-3z^2-5z+3)/(9z^3)): at z=0 the pole order is 3 (odd) => irregular RAMIFIED, ramification index 2, Katz invariant 1/2, exponential parts exp(-+(2/sqrt3) z^(-1/2)); z=0 is the only finite singular point; at z=infinity the pole order is 3 => irregular RAMIFIED, Katz invariant 1/2. Confirms the P5 premise that Channel Theory has a slope-1/2 ramified edge at z=0. Calibration: in u=sqrt(z) the actions are +-2/sqrt3, matching c=+2/sqrt(3) hard-coded in CC-PIPELINE-G2/g2_pade_borel.py."),
("S4-06","P5-2","PROVEN","computation","formal_type.json",
 "System B formal type (exact): at z=0 pole order 4 (even) => irregular UNRAMIFIED, Poincare rank 1, Katz invariant 1, exponential parts exp(-+(1/sqrt3)/z); at rho_pm = (-1 +- i sqrt11)/2 pole order 2 => regular singular; at z=infinity pole order 2 => regular singular. Every entry independently reproduces the paper's own prose in section-2.md L78-84 and tab:config. Confirms the P5 premise that the D5^(1) object is unramified."),
("S4-07","P5-2","PROVEN","computation","formal_type.json",
 "Action differences, obtained from the ODEs alone with no convention to interpret: System A in u=sqrt(z) has single action 2/sqrt3 = xi_0 and action DIFFERENCE 4/sqrt3 = zeta*; System B in z has single action 1/sqrt3 and action difference 2/sqrt3 = xi_0. This independently confirms P1's classification (b) that zeta* = 2 xi_0 is an action difference, not a change of variables. It also shows the Borel singularity sits at the action difference in both systems, consistent with L_V's exact factor p4 proportional to xi (xi + 2/sqrt3)."),
("S4-08","P5-3","STRUCTURAL","file_inspection","PREREG.md",
 "Step 3 HALTED and NOT executed, as P5 itself mandates: no Ohyama-Kawamuko-Sakai-Okamoto-type classification table of rank-2 linear systems exists in this repository (CT-S0-INVENTORY/REPORT.md section 3 item 7). VQ-N1 cites Sakai 2001, KNY 2017, Jimbo 1982, Okamoto 1987 but reproduces no table and records 'Okamoto 1987 pages PENDING'. No table was reconstructed from memory anywhere in this session."),
("S4-09","P5-4","STRUCTURAL","computation","formal_type.json",
 "VERDICT (c) INCONCLUSIVE. Within a fixed base coordinate the formal types are incompatible (Katz 1/2 ramified vs Katz 1 unramified), and no gauge or unramified change of variable can reconcile them. However the ramified double cover pi: w -> z = w^2 (equivalently Channel Theory's own uniformiser u = sqrt z) doubles the Katz invariant, sending System A's 1/2 to 1, exactly System B's value, with ramification index dropping 2 -> 1. So the slope-1/2 edge alone does NOT refute the D5^(1) attribution; it shows the two z-coordinates differ by a square. Verdict (a) is unavailable because step 3 could not run and the global singular configurations visibly differ (System A: one finite singular point, infinity ramified irregular; System B: three regular singular points plus one unramified irregular). Verdict (b) is unavailable because naming compatible Painleve types requires the missing table."),
("S4-10","P5-1","STRUCTURAL","file_inspection","REPORT.md",
 "Finding S4-F2: VQ-N1/verdict.md and the period-rep paper describe the linear system in INVERTED coordinates. VQ-N1: z=0 ordinary with exponents {0,1} and no z^(1/2) ramification, finite apparent Fuchsian points at (-1 +- i sqrt11)/6, infinity rank-1 unramified irregular with sigma_pm = +-1/sqrt3. L_phi: z=0 irregular Poincare rank 1 with exponential parts +-1/sqrt3, finite regular singular points at (-1 +- i sqrt11)/2, infinity regular singular. The finite points differ by a factor 3 (benign rescaling) but 0 and infinity are exchanged. Plausibly related by z -> 1/z, since VQ-N1's sigma_pm at infinity equals L_phi's exponential coefficients at 0, but this was NOT verified; VQ-N1's system is not written down in any readable file."),
]
out=[]
for cid,tid,lab,ev,scr,txt in C:
    out.append(dict(claim_id=cid,task_id=tid,claim=txt,evidence_type=ev,dps=None,
                    reproducible=True,script=scr,output_hash=sha(scr),label=lab))
open(os.path.join(H,"claims.jsonl"),"w").write("\n".join(json.dumps(c) for c in out)+"\n")
print("wrote",len(out),"claims; formal_type.json sha256:",FT)
for c in out: print(" ",c["claim_id"],c["label"])
