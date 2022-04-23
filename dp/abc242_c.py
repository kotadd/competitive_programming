# C - 1111gal password
# https://atcoder.jp/contests/abc242/tasks/abc242_c
MOD = 998244353

N = int(input())
dp = [[0] * 10 for _ in range(N)]

for i in range(1, 10):
    dp[0][i] = 1

for i in range(1, N):
    for j in range(1, 10):
        if 2 <= j <= 8:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] + dp[i - 1][j + 1]
        elif j == 1:
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j + 1]
        elif j == 9:
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
        dp[i][j] %= MOD

ans = 0
for i in range(1, 10):
    ans += dp[N - 1][i]
    ans %= MOD

print(ans)
