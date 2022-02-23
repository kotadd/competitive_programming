# D - Between Two Arrays
# https://atcoder.jp/contests/abc222/tasks/abc222_d
# 動的計画法＋累積和
# 広義単調増加

# 公式回答
MOD = 998244353
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = 3000

dp = [1] * (M + 1)
for i in range(N):
    nx = [0] * (M + 1)
    for j in range(A[i], B[i] + 1):
        nx[j] = dp[j]
    dp = nx
    for j in range(M):
        dp[j + 1] += dp[j]
        dp[j + 1] %= MOD

print(dp[M])
