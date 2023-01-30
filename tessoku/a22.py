# A22 - Sugoroku
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_v
# 配るdpの例
N = int(input())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))

INF = 1 << 60

# dpの初期化をしないとWA
dp = [-INF] * (N + 1)
dp[0] = dp[1] = 0
for i in range(1, N):
    dp[A[i]] = max(dp[i] + 100, dp[A[i]])
    dp[B[i]] = max(dp[i] + 150, dp[B[i]])

print(dp[N])
