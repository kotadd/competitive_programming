# D - FG operation
# https://atcoder.jp/contests/abc220/tasks/abc220_d
# 動的計画法（配るDP）

N = int(input())
A = list(map(int, input().split()))

dp = [[0 for _ in range(10)] for _ in range(N)]

dp[0][A[0]] = 1
mod = 998244353

for i in range(N - 1):
    for j in range(10):
        a = (j + A[i + 1]) % 10
        dp[i + 1][a] += dp[i][j]
        dp[i + 1][a] %= mod
        b = (j * A[i + 1]) % 10
        dp[i + 1][b] += dp[i][j]
        dp[i + 1][b] %= mod

for i in range(10):
    print(dp[N - 1][i] % mod)
