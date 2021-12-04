# 円環 動的計画法
N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

dp = [10**10] * N
dp[0] = T[0]
for i in range(1, N * 2):
    if i >= N:
        i -= N
    dp[i] = min(T[i], dp[i - 1] + S[i - 1])

print(*dp, sep="\n")
