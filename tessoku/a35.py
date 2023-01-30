# A35 - Game 4
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ai
# 奇数ではmax, 偶数ではminを取るdp

N = int(input())
A = list(map(int, input().split()))

dp = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    dp[N][i] = A[i - 1]

for i in reversed(range(1, N)):
    for j in range(1, N):
        if i % 2 == 1:
            dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1])
        else:
            dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1])

print(dp[1][1])
