# D - Cooking
# https://atcoder.jp/contests/abc204/tasks/abc204_d
# 解説：https://blog.hamayanhamayan.com/entry/2021/06/07/024420
N = int(input())
T = list(map(int, input().split()))
M = 10**5
INF = 10**9
# DP[i][t] := i番目まで料理作成が終わっていて、オーブンAの使用時間がtであるときのオーブンBの使用時間の最小値
DP = [[INF] * (M + 1001) for i in range(N + 1)]
DP[0][0] = 0
for i in range(N):
    for j in range(M + 1):
        DP[i + 1][j] = min(DP[i + 1][j], DP[i][j] + T[i])  # オーブンBを使う
        DP[i + 1][j + T[i]] = min(DP[i + 1][j + T[i]], DP[i][j])  # オーブンAを使う


ANS = INF
for i in range(M + 1):
    ANS = min(ANS, max(i, DP[N][i]))
print(ANS)
