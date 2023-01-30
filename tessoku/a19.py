# A19 - Knapsack 1
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_s

N, W = map(int, input().split())

dp = [0] * (W + 1)
for i in range(N):
    w, v = map(int, input().split())
    for j in range(W, w - 1, -1):
        dp[j] = max(dp[j], dp[j - w] + v)

print(dp[W])


# 解答2：二次元配列を使う（こちらの方がわかりやすいかも）
# 品物iまで選択した時の重さwでの価値vの最大値
# N, W = map(int, input().split())

# w = [0] * (N + 1)
# v = [0] * (N + 1)
# for i in range(1, N + 1):
#     w[i], v[i] = map(int, input().split())

# INF = 10**9
# dp = [[-INF] * (W + 1) for _ in range(N + 1)]
# dp[0][0] = 0

# for i in range(1, N + 1):
#     for j in range(W + 1):
#         dp[i][j] = max(dp[i - 1][j], dp[i][j])
#         if j >= w[i]:
#             dp[i][j] = max(dp[i - 1][j - w[i]] + v[i], dp[i][j])

# print(max(dp[N]))
