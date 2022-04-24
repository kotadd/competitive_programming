# https://atcoder.jp/contests/abc248/tasks/abc248_c
# C - Dice Sum
# dp[i][j]:=数列の先頭から i 項まで決めた際に、総和が j であるような数列の決め方の総数

MOD = 998244353

N, M, K = map(int, input().split())

dp = [[0] * (K + 1) for _ in range(N + 1)]
dp[0][0] = 1
for i in range(1, N + 1):
    for j in range(K + 1):
        for k in range(j):
            if j - k <= M:
                dp[i][j] += dp[i - 1][k]

ans = 0
for i in range(K + 1):
    ans += dp[N][i]
    ans %= MOD
print(ans)
