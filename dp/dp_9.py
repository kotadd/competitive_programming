# https://qiita.com/drken/items/a5e6fe22863b7992efdb
# 最小コスト弾性マッチング 問題

N, M = map(int, input().split())

C = [list(map(int, input().split())) for _ in range(N)]

INF = 10**10
# dpテーブル作成
dp = [[INF for _ in range(M + 1)] for _ in range(N + 1)]
dp[0][0] = 0
for i in range(N):
    for j in range(M):
        if i + 1 <= N:
            dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j + 1] + C[i][j])
        if j + 1 <= M:
            dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i + 1][j] + C[i][j])
        if i + 1 <= N and j + 1 <= M:
            dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j] + C[i][j])

print(dp[N][M])
