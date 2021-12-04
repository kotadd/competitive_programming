# B - Alcoholic
# https://atcoder.jp/contests/abc189/tasks/abc189_b
# 細かい計算はDecimalを使う か 整数で行う
import decimal

N, X = map(int, input().split())

ans = -1
total = 0
for i in range(N):
    v, p = map(decimal.Decimal, input().split())
    total += v * p / 100
    if total > X and ans == -1:
        ans = i + 1

print(ans)
