# D - Divide by 2 or 3
# https://atcoder.jp/contests/abc276/tasks/abc276_d
# lru_cacheのためPyPyではなくPython3.8.2で提出

from functools import lru_cache, reduce
from math import gcd


def gcd_list(num_list: list) -> int:
    return reduce(gcd, num_list)


N = int(input())
A = list(map(int, input().split()))

ans = 0

x = gcd_list(A)


@lru_cache
def f(n):
    res = 0
    while n > x:
        if n % x == 0 and n // x % 2 == 0:
            n //= 2
            res += 1
        elif n % x == 0 and n // x % 3 == 0:
            n //= 3
            res += 1
        else:
            print(-1)
            exit()
    if n != x:
        print(-1)
        exit()
    return res


for a in A:
    ans += f(a)
print(ans)
