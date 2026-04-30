"""
UMB-RES-EXTEND-PROJ — sampled projective rerun.

Stratified sample of degree-(2,1) projective candidates at exact
a_2/b_1^2 = -2/9. Up to N_PER_B1 distinct-L groups per b_1 value,
each run with Stage A (dps=120 PSLQ) and Stage B (dps=400 PSLQ on
Trans candidates) against the 15-element basis with phantom-hit
rejection.
"""
from __future__ import annotations
import math, json, time, sys, random
from itertools import product
import numpy as np
from mpmath import mp, mpf, log, pi, zeta, sqrt, e, euler, pslq

mp.dps = 80
random.seed(42)

H_PROJ = 8
B1_LIST = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
N_PER_B1 = 40             # stratified sample size per b_1
N_SCREEN_F64 = 200
N_STAGE_A = 350
DPS_STAGE_A = 120
N_STAGE_B = 600
DPS_STAGE_B = 400
PSLQ_TOL_A = mpf('1e-30')
PSLQ_TOL_B = mpf('1e-50')
CMAX = 10**8
KEYS = ['1','pi','pi^2','log2','zeta2','zeta3','sqrt2','sqrt3',
        'sqrt5','e','gamma','log3','pi*log2','pi^3']


def gcd_many(*xs):
    g = 0
    for x in xs:
        g = math.gcd(g, abs(int(x)))
    return g if g else 1


def canonical(t):
    a2, a1, a0, b1, b0 = t
    if b1 <= 0:
        return None
    g = gcd_many(a2, a1, a0, b1, b0)
    if g != 1:
        a2, a1, a0, b1, b0 = a2//g, a1//g, a0//g, b1//g, b0//g
    return (a2, a1, a0, b1, b0)


def evaluate_pcf_f64(a2, a1, a0, b1, b0, N):
    Pm1 = 1.0; P0 = float(b0)
    Qm1 = 0.0; Q0 = 1.0
    L_prev = None
    for n in range(1, N+1):
        bn = b1*n + b0
        an = a2*n*n + a1*n + a0
        Pn = bn*P0 + an*Pm1
        Qn = bn*Q0 + an*Qm1
        Pm1, P0 = P0, Pn
        Qm1, Q0 = Q0, Qn
        if n % 16 == 0:
            s = abs(Q0)
            if not np.isfinite(s) or s == 0.0:
                return (None, None, False)
            if s > 1e100 or s < 1e-100:
                Pm1 /= s; P0 /= s; Qm1 /= s; Q0 /= s
        if n == N - 30:
            if Q0 != 0 and np.isfinite(Q0):
                L_prev = P0 / Q0
            else:
                return (None, None, False)
    if Q0 == 0 or not np.isfinite(Q0):
        return (None, None, False)
    return (P0/Q0, L_prev, True)


def evaluate_pcf_mp(a2, a1, a0, b1, b0, N, dps):
    mp.dps = dps
    Pm1 = mpf(1); P0 = mpf(b0)
    Qm1 = mpf(0); Q0 = mpf(1)
    for n in range(1, N+1):
        bn = mpf(b1)*n + mpf(b0)
        an = mpf(a2)*n*n + mpf(a1)*n + mpf(a0)
        Pn = bn*P0 + an*Pm1
        Qn = bn*Q0 + an*Qm1
        Pm1, P0 = P0, Pn
        Qm1, Q0 = Q0, Qn
        if n % 32 == 0:
            scale = abs(Q0)
            if scale > mpf('1e100'):
                Pm1 /= scale; P0 /= scale
                Qm1 /= scale; Q0 /= scale
    if Q0 == 0:
        return None
    return P0 / Q0


def make_basis(dps):
    mp.dps = dps
    pi_v = pi
    return {
        '1': mpf(1), 'pi': pi_v, 'pi^2': pi_v**2,
        'log2': log(2), 'zeta2': zeta(2), 'zeta3': zeta(3),
        'sqrt2': sqrt(2), 'sqrt3': sqrt(3), 'sqrt5': sqrt(5),
        'e': e, 'gamma': euler, 'log3': log(3),
        'pi*log2': pi_v*log(2), 'pi^3': pi_v**3,
    }


def classify(L, basis, tol):
    # Edge case: L is zero (or below precision noise).
    if abs(L) < mpf('1e-50'):
        return ('Rat', [1] + [0]*len(KEYS), None)
    # First check if L is rational (cheap and bullet-proof)
    try:
        rel_rat = pslq([L, mpf(1)], tol=tol, maxcoeff=CMAX)
        if rel_rat is not None and rel_rat[0] != 0:
            return ('Rat', list(rel_rat) + [0]*(len(KEYS)-1), None)
    except Exception:
        pass
    # Full-basis PSLQ
    vec = [L] + [basis[k] for k in KEYS]
    try:
        rel = pslq(vec, tol=tol, maxcoeff=CMAX)
    except Exception:
        return ('Trans', None, None)
    if rel is None:
        return ('Trans', None, None)
    if rel[0] == 0:
        return ('Trans', None, {'phantom': True, 'relation': list(rel),
                                'basis': ['L'] + KEYS})
    nz = {i for i,v in enumerate(rel) if v != 0}
    has_log = any(rel[i] != 0 for i,k in enumerate(['L']+KEYS) if 'log' in k)
    if nz <= {0,1}:
        return ('Rat', list(rel), None)
    if has_log:
        return ('Log', list(rel), None)
    return ('Alg', list(rel), None)


def main():
    t0 = time.time()
    by_b1 = {b1: [] for b1 in B1_LIST}
    seen = set()
    for b1 in B1_LIST:
        if (2*b1*b1) % 9 != 0:
            continue
        a2 = -2*b1*b1 // 9
        for a1, a0, b0 in product(range(-H_PROJ, H_PROJ+1), repeat=3):
            c = canonical((a2, a1, a0, b1, b0))
            if c is None or c in seen:
                continue
            seen.add(c)
            if b1 + b0 == 0:
                continue
            by_b1[b1].append(c)
    total_cands = sum(len(v) for v in by_b1.values())
    print(f"step1 candidates: {total_cands} ({ {b1: len(v) for b1,v in by_b1.items()} })", flush=True)

    # Convergence-screen + L_f64 dedup, stratified per b_1.
    sample = []
    for b1 in B1_LIST:
        cands = by_b1[b1]
        random.shuffle(cands)
        seen_L = set()
        chosen = []
        for c in cands:
            a2,a1,a0,b1_,b0 = c
            L,Lp,ok = evaluate_pcf_f64(a2,a1,a0,b1_,b0, N_SCREEN_F64)
            if not ok:
                continue
            denom = abs(L) if abs(L) > 1e-12 else 1.0
            if abs(L - Lp)/denom > 1e-10:
                continue
            key = float(f"{L:.10g}")
            if key in seen_L:
                continue
            seen_L.add(key)
            chosen.append((c, L))
            if len(chosen) >= N_PER_B1:
                break
        sample.extend(chosen)
        print(f"  b1={b1}: sampled {len(chosen)} (from {len(cands)} candidates)", flush=True)
    print(f"step2 stratified sample size: {len(sample)} (t={time.time()-t0:.1f}s)", flush=True)

    basis_lo = make_basis(DPS_STAGE_A)
    basis_hi = make_basis(DPS_STAGE_B)
    classified = []
    rejections = []

    for j,(c,Lf64) in enumerate(sample):
        a2,a1,a0,b1,b0 = c
        try:
            L_lo = evaluate_pcf_mp(a2,a1,a0,b1,b0, N_STAGE_A, DPS_STAGE_A)
            mp.dps = DPS_STAGE_A
            lab_lo, rel_lo, rej_lo = classify(L_lo, basis_lo, PSLQ_TOL_A)
            if rej_lo is not None:
                rejections.append({'family': list(c), 'stage':'A', **rej_lo})

            entry = {'family': list(c), 'L_f64': Lf64,
                     'class_stage_A': lab_lo, 'relation_A': rel_lo}

            if lab_lo == 'Trans':
                # Stage B confirmation
                L_hi = evaluate_pcf_mp(a2,a1,a0,b1,b0, N_STAGE_B, DPS_STAGE_B)
                mp.dps = DPS_STAGE_B
                lab_hi, rel_hi, rej_hi = classify(L_hi, basis_hi, PSLQ_TOL_B)
                if rej_hi is not None:
                    rejections.append({'family': list(c), 'stage':'B', **rej_hi})
                entry['L_hi'] = mp.nstr(L_hi, 40)
                entry['class_stage_B'] = lab_hi
                entry['relation_B'] = rel_hi
                entry['class'] = lab_hi
            else:
                entry['L_hi'] = None
                entry['class_stage_B'] = None
                entry['class'] = lab_lo
            classified.append(entry)
        except Exception as ex:
            classified.append({'family': list(c), 'class':'error', 'error':str(ex)})

        if (j+1) % 25 == 0 or j == len(sample)-1:
            cnt = {'Trans':0,'Log':0,'Alg':0,'Rat':0,'error':0}
            for x in classified:
                cnt[x.get('class','error')] = cnt.get(x.get('class','error'),0)+1
            print(f"  {j+1}/{len(sample)} -> {cnt} t={time.time()-t0:.1f}s", flush=True)

    counts = {'Trans':0,'Log':0,'Alg':0,'Rat':0,'error':0}
    for x in classified:
        counts[x.get('class','error')] = counts.get(x.get('class','error'),0)+1

    summary = {
        'parameters': {
            'H_proj': H_PROJ, 'b1_list': B1_LIST,
            'N_per_b1_target': N_PER_B1,
            'N_screen_f64': N_SCREEN_F64,
            'N_stage_A': N_STAGE_A, 'dps_stage_A': DPS_STAGE_A, 'pslq_tol_A': '1e-30',
            'N_stage_B': N_STAGE_B, 'dps_stage_B': DPS_STAGE_B, 'pslq_tol_B': '1e-50',
            'CMAX': CMAX,
            'phantom_rule': 'reject any relation with L-coefficient = 0',
            'basis': KEYS,
            'sampling': 'stratified random per b_1 (seed=42); deduped by L_f64 to 10 sig figs',
        },
        'step1_total_candidates': total_cands,
        'step2_sample_size': len(sample),
        'class_counts': counts,
        'phantom_rejections': rejections,
        'classified': classified,
        'elapsed_sec': time.time()-t0,
    }
    out = sys.argv[1] if len(sys.argv) > 1 else 'umb_res_proj_results.json'
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, default=str)
    print('-'*60, flush=True)
    print('class_counts:', counts, flush=True)
    print(f"phantom rejections: {len(rejections)}", flush=True)
    print(f"elapsed: {summary['elapsed_sec']:.1f}s -> {out}", flush=True)


if __name__ == '__main__':
    main()
