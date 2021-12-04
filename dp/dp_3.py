# https://qiita.com/drken/items/a5e6fe22863b7992efdb
# 部分和問題

N, M = map(int, input().split())
A = list(map(int, input().split()))

# dpテーブル作成
dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

# i:何も選ばない時に j:合計が0になるのは あり得る
dp[0][0] = 1
for i in range(N):
    for j in range(M + 1):
        if j >= A[i]:
            dp[i + 1][j] = dp[i][j - A[i]] | dp[i][j]
        else:
            dp[i + 1][j] = dp[i][j]

print('Yes' if dp[N][M] else 'No')
