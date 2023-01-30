# ★A21 - Block Game
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_u
# 左右から取り崩すブロックゲーム
# 区間dpの例

N = int(input())
P = [0] * (N + 1)
A = [0] * (N + 1)
for i in range(1, N + 1):
    P[i], A[i] = map(int, input().split())

dp = [[0] * (N + 1) for _ in range(N + 1)]

for LEN in reversed(range(N - 1)):
    for l in range(1, N - LEN + 1):
        r = l + LEN

        score_l = 0
        if l >= 2 and l <= P[l - 1] <= r:
            score_l = A[l - 1]

        score_r = 0
        if r <= N - 1 and l <= P[r + 1] <= r:
            score_r = A[r + 1]

        if l == 1:
            dp[l][r] = dp[l][r + 1] + score_r
        elif r == N:
            dp[l][r] = dp[l - 1][r] + score_l
        else:
            dp[l][r] = max(dp[l - 1][r] + score_l, dp[l][r + 1] + score_r)

ans = 0
for i in range(N + 1):
    ans = max(ans, dp[i][i])
print(ans)
