# D - Bouquet
# https://atcoder.jp/contests/abc156/tasks/abc156_d
# フェルマーの小定理

MOD = 10**9 + 7


def cmb(n, r):
    r = min(n - r, r)
    if r == 0:
        return 1
    x = 1
    y = 1
    for i in range(r):
        x = x * (n - i) % MOD
        y = y * (i + 1) % MOD
    return x * pow(y, MOD - 2, MOD) % MOD


n, a, b = map(int, input().split())

ans = pow(2, n, MOD) - 1
ans -= cmb(n, a)
ans -= cmb(n, b)
print(ans % MOD)
