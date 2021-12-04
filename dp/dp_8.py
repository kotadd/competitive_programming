# https://qiita.com/drken/items/a5e6fe22863b7992efdb
# 最長共通部分列 (LCS) 問題

S = input()
T = input()

# dpテーブル作成
dp = [[0 for _ in range(len(T) + 1)] for _ in range(len(S) + 1)]

for i in range(len(S)):
    for j in range(len(T)):
        if S[i] == T[j]:
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1], dp[i][j] + 1)
        else:
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

print(dp[len(S)][len(T)])
