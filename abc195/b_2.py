# B - Many Oranges
# https://atcoder.jp/contests/abc195/tasks/abc195_b
# 動的計画法を用いた解法

A, B, W = map(int, input().split())
W *= 1000

lower = min(A, B)
N = W // lower + 1


# max化
dp = [0] * (W + 1)

for i in range(A, B + 1):
    for w in reversed(range(W + 1)):
        if w - i >= 0:
            dp[w - i] = max(dp[w] + 1, dp[w - i])

    if dp[0] != 0:
        break
ans_max = dp[0]

# min化
dp = [10**7] * (W + 1)
dp[W] = 0

for i in reversed(range(A, B + 1)):
    for w in reversed(range(W + 1)):
        if w - i >= 0:
            dp[w - i] = min(dp[w] + 1, dp[w - i])

    if dp[0] != 10**7:
        break
ans_min = dp[0]

if ans_min == 10**7 or ans_max == 0:
    print('UNSATISFIABLE')
else:
    print(ans_min, ans_max)
