# # https://qiita.com/drken/items/a5e6fe22863b7992efdb
# 部分和数え上げ問題

N, M = map(int, input().split())
A = list(map(int, input().split()))

# dpテーブル作成
dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

# i:何も選ばない時に j:合計が0になる
dp[0][0] = 1
for i in range(N):
    for j in range(M + 1):
        if j >= A[i]:
            dp[i + 1][j] = dp[i][j - A[i]] + dp[i][j]
        else:
            dp[i + 1][j] = dp[i][j]

print(dp[N][M])
