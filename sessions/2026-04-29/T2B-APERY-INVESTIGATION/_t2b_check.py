from mpmath import mp, mpf, pi
mp.dps = 50

# Brouncker-style CF: 4/pi = 1 + 1^2/(3 + 2^2/(5 + 3^2/(7 + ...)))
# a(n) = n^2, b(n) = 2n+1  =>  a2/b1^2 = 1/4
def brouncker(N):
    x = mpf(0)
    for n in range(N, 0, -1):
        x = mpf(n*n) / (mpf(2*n+1) + x)
    return 1 + x  # 4/pi

val = brouncker(2000)
print('Brouncker 4/pi via degree-(2,1) CF, a(n)=n^2, b(n)=2n+1')
print('  a2/b1^2 =', mpf(1)/mpf(4))
print('  CF value     =', val)
print('  4/pi         =', 4/pi)
print('  diff         =', abs(val - 4/pi))
print()

print('Apery zeta(2) is degree-(4,2): leading ratio a4/b2^2 = -1/121')
print()
print('Classical pi CFs with linear b(n) (degree-(2,1)):')
print('  Brouncker variant: a2/b1^2 = 1/4 (Worpitzky boundary)')
print('  No classical pi or pi^2 CF found with a2/b1^2 = -2/9.')
print()
print('-2/9 =', float(mpf(-2)/9))
print('-1/4 =', float(mpf(-1)/4))
print('|-2/9| < |-1/4|: strictly inside Worpitzky parabolic region.')
print()
# Achievable ratios at D=4: a_2 in {-2, 1}, b_1 in {+/-2, +/-3}
print('Achievable ratios at D=4 with a2 in {-2,1}, b1 in {+/-2,+/-3}:')
for a2 in [-2, 1]:
    for b1 in [2, 3]:
        r = mpf(a2)/(b1*b1)
        print(f'  a2={a2}, b1=+/-{b1}: ratio = {a2}/{b1*b1} = {float(r):+.4f}',
              ' Worpitzky-inside' if abs(r) < mpf(1)/4 else ' OUTSIDE/boundary')
