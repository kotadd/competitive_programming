# D - Strange Lunchbox
# https://atcoder.jp/contests/abc219/tasks/abc219_d

N = int(input())
X, Y = map(int, input().split())

INF = 10**10
dp = [[[INF] * 301 for _ in range(301)] for _ in range(301)]
dp[0][0][0] = 0

for i in range(N):
    a, b = map(int, input().split())
    for j in range(X + 1):
        for k in range(Y + 1):
            x = min(j + a, X)
            y = min(k + b, Y)
            dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
            dp[i + 1][x][y] = min(dp[i + 1][x][y], dp[i][j][k] + 1)

ans = dp[N][X][Y]

if ans == INF:
    print(-1)
else:
    print(ans)
