# A18 - Subset Sum
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_r
# 部分和問題
N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0] * (S + 1) for _ in range(N + 1)]
dp[0][0] = 1

for i in range(1, N + 1):
    for j in range(S + 1):
        dp[i][j] |= dp[i - 1][j]
        if j >= A[i - 1]:
            dp[i][j] |= dp[i - 1][j - A[i - 1]]

print('Yes' if dp[N][S] else 'No')
