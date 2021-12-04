# https://atcoder.jp/contests/abc211/tasks/abc211_c
# 教訓
# 1. dp[0]=1, dpの配列は一つ大きめ
# 2. 何かを選ぶ/選ばないの両方の考慮が必要なものは、動的計画法に当てはまりやすそう

import sys
input = sys.stdin.readline

S = input().strip()
T = 'chokudai'
MOD = (10 ** 9) + 7

dp = [0] * 9
dp[0] = 1
for s in S:
    for i in range(len(T)):
        if T[i] == s:
            dp[i + 1] += dp[i]
            dp[i + 1] %= MOD

print(dp[8])
