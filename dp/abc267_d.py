# D - Index × A(Not Continuous ver.)
# https://atcoder.jp/contests/abc267/editorial/4728
N, M = map(int, input().split())
A = list(map(int, input().split()))

INF = 1 << 60
dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
dp[0][1] = -INF
for i in range(N + 1):
    for j in range(M + 1):
        if j == 0:
            dp[i][0] = 0
        elif j > i:
            dp[i][j] = -INF
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + A[i - 1] * j)

print(dp[N][M])
