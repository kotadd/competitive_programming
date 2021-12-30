# D - aab aba baa
# https://atcoder.jp/contests/abc202/tasks/abc202_d
from operator import mul
from functools import reduce


def cmb(n, r):
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


A, B, K = map(int, input().split())
K -= 1

ans = ''
for i in range(A + B):
    if 0 < A:
        if K < cmb(A + B - 1, B):
            ans += 'a'
            A -= 1
        else:
            ans += 'b'
            K -= cmb(A + B - 1, B)
            B -= 1
    else:
        ans += 'b'
        B -= 1

print(ans)
