#  D - Money in Hand
# https://atcoder.jp/contests/abc286/tasks/abc286_d

N, X = map(int, input().split())

dp = [[0 for _ in range(X + 1)] for _ in range(N + 1)]
dp[0][0] = 1
for i in range(1, N + 1):
    a, b = map(int, input().split())
    for j in range(X + 1):
        for k in range(b + 1):
            if j >= a * k:
                dp[i][j] |= dp[i - 1][j - a * k]

print('Yes' if dp[N][X] else 'No')
