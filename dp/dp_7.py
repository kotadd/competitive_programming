# https://qiita.com/drken/items/a5e6fe22863b7992efdb
# 個数制限付き部分和問題

N, M = map(int, input().split())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

INF = 10 ** 10
# dpテーブル作成
dp = [[INF for _ in range(M + 1)] for _ in range(N + 1)]

# i:何も選ばない時に j:合計が0になる
dp[0][0] = 0
for i in range(N):
    for j in range(M + 1):
        if dp[i][j] < INF:
            dp[i + 1][j] = 0
        if j >= A[i]:
            if dp[i][j - A[i]] < INF:
                dp[i + 1][j] = min(dp[i + 1][j], 1)
            if dp[i + 1][j - A[i]] < B[i]:
                dp[i + 1][j] = min(dp[i + 1][j - A[i]] + 1, dp[i + 1][j])

if dp[N][M] == INF:
    print('No')
else:
    print('Yes')
