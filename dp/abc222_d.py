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
    for i in range(M):
        dp[i + 1] += dp[i]
        dp[i + 1] %= MOD

print(dp[N])


# 別解
dp = [[0] * M for _ in range(M)]
rui = [0] * M
dp[0][0] = 1
for i in range(N):
    rui[0] = dp[i][0]
    for j in range(1, M):
        rui[j] = rui[j - 1] + dp[i][j]
    for j in range(A[i], B[i] + 1):
        dp[i + 1][j] += rui[j]

ans = 0
for i in range(M):
    ans += dp[N][i]
print(ans)
