# D - Index Trio
# https://atcoder.jp/contests/abc249/tasks/abc249_d

from math import ceil
from collections import defaultdict


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


N = int(input())
A = list(map(int, input().split()))

d = defaultdict(int)

for a in A:
    d[a] += 1

A = list(set(A))

ans = 0
for a in A:
    tmp = 0
    divisors = make_divisors(a)
    for i in range(ceil(len(divisors) / 2)):
        j = -i - 1
        tmp = d[divisors[i]] * d[divisors[j]]
        if divisors[i] != divisors[j]:
            tmp *= 2
        tmp *= d[a]

        # print(a, tmp, divisors[i], divisors[j])

        ans += tmp

print(ans)
