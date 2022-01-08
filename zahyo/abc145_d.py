# D - Knight
# https://atcoder.jp/contests/abc145/tasks/abc145_d

MOD = 10**9 + 7
X, Y = map(int, input().split())


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


n = (2 * Y - X) // 3
m = (2 * X - Y) // 3


if (X + Y) % 3 != 0 or n < 0 or m < 0:
    print(0)
    exit()

print(cmb(n + m, n))
