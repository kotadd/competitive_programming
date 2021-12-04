# C - Walk on Multiplication Table
# https://atcoder.jp/contests/abc144/tasks/abc144_c
# 掛け算表のマス移動

from math import sqrt

N = int(input())

ans = 10**13
for i in range(1, int(sqrt(N)) + 1):
    if N % i == 0:
        ans = min(ans, i + N // i - 2)

print(ans)
