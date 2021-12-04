# https://qiita.com/drken/items/a5e6fe22863b7992efdb
# 最小個数部分和問題

N, M = map(int, input().split())
A = list(map(int, input().split()))

INF = 10 ** 10
# dpテーブル作成
dp = [[INF for _ in range(M + 1)] for _ in range(N + 1)]

# i:何も選ばない時に j:合計が0になる
dp[0][0] = 0
for i in range(N):
    for j in range(M + 1):
        if j >= A[i]:
            dp[i + 1][j] = min(dp[i][j - A[i]] + 1, dp[i][j])
        else:
            dp[i + 1][j] = dp[i][j]

if dp[N][M] == INF:
    print(-1)
else:
    print(dp[N][M])
