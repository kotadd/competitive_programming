# D - Cooking
# https://atcoder.jp/contests/abc204/tasks/abc204_d
# 解説：https://blog.hamayanhamayan.com/entry/2021/06/07/024420
N = int(input())
T = list(map(int, input().split()))
M = 10**5
INF = 10**9
# dp[i][t] := i番目まで料理作成が終わっていて、オーブンAの使用時間がtであるときのオーブンBの使用時間の最小値
dp = [[INF] * (M + 1001) for i in range(N + 1)]
dp[0][0] = 0
for i in range(N):
    for j in range(M + 1):
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + T[i])  # オーブンBを使う
        dp[i + 1][j + T[i]] = min(dp[i + 1][j + T[i]], dp[i][j])  # オーブンAを使う


ans = INF
for i in range(M + 1):
    ans = min(ans, max(i, dp[N][i]))
print(ans)


# for i in range(6):
#     for j in range(26):
#         print(dp[i][j], end=' ')
#     print()
