# https://atcoder.jp/contests/abc129/tasks/abc129_c
# C - Typical Stairs
# 動的計画法

N, M = map(int, input().split())
MOD = 10**9 + 7

d = dict()
for i in range(M):
    a = int(input())
    d[a] = 1

dp = [0] * (N + 1)
dp[0] = 1
if 1 in d:
    dp[1] = 0
else:
    dp[1] = 1

for i in range(2, N + 1):
    if i not in d:
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD

print(dp[N])
