# ★A20 - LCS
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_t
# 最長共通部分列問題

S = input()
T = input()
N = len(S)
M = len(T)

dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(N):
    for j in range(M):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        if S[i] == T[j]:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)

print(max(dp[N - 1]))
