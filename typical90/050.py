# 漸化式を立ててDP（動的計画法）をしよう
N, L = map(int, input().split())

div = 10**9 + 7

dp = [1] * (N + 1)
for i in range(1, N + 1):
    if i < L:
        dp[i] = dp[i - 1]
    else:
        dp[i] = (dp[i - 1] + dp[i - L]) % div

print(dp[-1])
