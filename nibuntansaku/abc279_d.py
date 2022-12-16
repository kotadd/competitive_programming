# D - Freefall
# https://atcoder.jp/contests/abc279/tasks/abc279_d
# 相対誤差：(測定値 - 真値) / 真値
# 二分探索

import math

A, B = map(int, input().split())

l = 0
r = 10**18

ans = A

while r - l > 1:
    n = (l + r) // 2
    if (A / math.sqrt(n) - A / math.sqrt(n + 1)) < B:
        r = n
    else:
        l = n

    ans = min(ans, A / math.sqrt(n + 1) + B * n)

print(ans)
