# C - GeT AC
# https://atcoder.jp/contests/abc122/tasks/abc122_c
# dp 動的計画法
N, Q = map(int, input().split())
S = input()

dp = [0] * (N + 1)
dp[0] = 0

for i in range(1, N):
    if S[i] == 'C' and S[i - 1] == 'A':
        dp[i] = dp[i - 1] + 1
    else:
        dp[i] = dp[i - 1]

ans = 0
for _ in range(Q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    print(dp[r] - dp[l])
