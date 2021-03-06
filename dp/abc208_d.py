# D - Shortest Path Queries 2
# ワーシャルフロイド法（dp[k+1][i][j] = min(dp[k][i][j], dp[k][i][k] + dp[k][k][j])

# 問題
# 都市 s を出発して都市 t に到着するまでの最短時間を計算してください。ただし、通ってよい都市は s,t および番号が k 以下の都市のみとします。

N, M = map(int, input().split())
INF = 1 << 60
dp = [[INF] * N for _ in range(N)]

# a,b間の辺が存在し、距離がw
for i in range(M):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    dp[a][b] = w

# 同一点への距離は0
for i in range(N):
    dp[i][i] = 0

ans = 0
# dp遷移（フロイド・ワーシャル法）
for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
            if dp[i][j] < INF // 2:
                ans += dp[i][j]

print(ans)
