# A16 - Dungeon 1
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_p

N = int(input())
A = [0] + list(map(int, input().split()))
B = [0, 0] + list(map(int, input().split()))

dp = [0] * (N + 1)

for i in range(1, N):
    if i >= 2:
        dp[i] = min(dp[i - 1] + A[i], dp[i - 2] + B[i])
    else:
        dp[i] = dp[i - 1] + A[i]

print(dp[N - 1])

# 解法2
# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# INF = 1 << 60
# dp = [INF] * N
# dp[0] = 0
# dp[1] = A[0]

# for i in range(2, N):
#     dp[i] = min(dp[i - 1] + A[i - 1], dp[i], dp[i - 2] + B[i - 2])

# print(dp[N - 1])
