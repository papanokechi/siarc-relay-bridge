import mpmath as mp
mp.mp.dps = 80
rs = [mp.mpf(1)/3, mp.mpf('-2.5'), mp.mpf(2), mp.mpc(3,2)]
ns = [20, 100, 1000, 10000]
for r in rs:
    print(f'r={mp.nstr(r,30)}')
    expected = r*(r-1)/2
    print(' expected leading n*(h-1) ~', mp.nstr(expected,30))
    for n in ns:
        h = mp.gamma(n+1-r) * (mp.mpf(n) ** r) / mp.gamma(n+1)
        diff = h-1
        print(f' n={n:5d} h-1={mp.nstr(diff,20)} n*(h-1)={mp.nstr(n*diff,20)}')
    print()
