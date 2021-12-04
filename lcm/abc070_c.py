# C - Multiple Clocks
# https://atcoder.jp/contests/abc070/tasks/abc070_c

from math import gcd
N = int(input())

ans = int(input())
for _ in range(N - 1):
    t = int(input())
    ans = ans * t // gcd(ans, t)

print(ans)
