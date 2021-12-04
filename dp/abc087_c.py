# https://atcoder.jp/contests/abc087/tasks/arc090_a
# C - Candies
N = int(input())
A = [list(map(int, input().split())) for _ in range(2)]

dp = [[0] * N for _ in range(2)]
dp[0][0] = A[0][0]

ans = 0

for i in range(2):
    for j in range(N):
        if j > 0:
            dp[i][j] = max(dp[i][j], dp[i][j - 1] + A[i][j])
        if i > 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j] + A[i][j])

print(dp[1][N - 1])
