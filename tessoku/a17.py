# A17 - Dungeon 2
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_q
# 動的計画法の復元

N = int(input())
A = [0] + list(map(int, input().split()))
B = [0, 0] + list(map(int, input().split()))

dp = [0] * (N + 1)
dp[1] = A[1]
for i in range(2, N):
    dp[i] = min(dp[i - 1] + A[i], dp[i - 2] + B[i])

ans = []
cur = N
while True:
    ans.append(cur)
    if cur == 1:
        break
    if dp[cur - 1] == dp[cur - 2] + A[cur - 1]:
        cur -= 1
    else:
        cur -= 2


print(len(ans))
print(*reversed(ans))
