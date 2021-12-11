# D - Banned K
# https://atcoder.jp/contests/abc159/tasks/abc159_d
from collections import Counter
from operator import mul
from functools import reduce


def cmb(n, r):
    if n < 2:
        return 0
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


N = int(input())
A = list(map(int, input().split()))

c = Counter(A)
ans = 0
for k, v in c.items():
    ans += cmb(v, 2)

for a in A:
    print(ans - c[a] + 1)
