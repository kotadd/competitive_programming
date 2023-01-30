# A25 - Number of Routes
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_y

H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]

dp = [[0] * W for _ in range(H)]
dp[0][0] = 1
for i in range(H):
    for j in range(W):
        if C[i][j] == '#':
            continue
        if i > 0 and j > 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j] + dp[i][j - 1])
        if i > 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j])
        if j > 0:
            dp[i][j] = max(dp[i][j], dp[i][j - 1])

print(dp[H - 1][W - 1])
