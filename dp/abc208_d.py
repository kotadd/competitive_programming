# D - Shortest Path Queries 2
# ワーシャル フロイド法
# 動的計画法
# クエリ問題でもあるので、差分計算という観点から動的計画法を導く

N, M = map(int, input().split())
INF = 1 << 60
dp = [[INF] * (N) for _ in range(N)]
for i in range(N):
    dp[i][i] = 0
for i in range(M):
    a, b, c = map(int, input().split())
    dp[a - 1][b - 1] = c


ans = 0
for k in range(N):
    # nxt = [[0] * N for i in range(N)] #nxtを利用することで、2回forを回さなくてもいける
    for i in range(N):
        for j in range(N):
            # nxt[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    for i in range(N):
        for j in range(N):
            if dp[i][j] < INF:
                ans += dp[i][j]

print(ans)
