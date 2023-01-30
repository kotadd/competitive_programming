# ★A23 - All Free
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_w
# ビットDP
# M種類のクーポンのうち何枚使えばN種類の品物すべてと交換できるかを求める。

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]

INF = 10**9
# クーポン券1,2,...iの中から何枚かを選び、無料で買える品物の集合がSとなるとき、選んだクーポン券の枚数の最小値を求める
dp = [[INF] * (1 << N) for _ in range(M + 1)]

dp[0][0] = 0

for i in range(1, M + 1):
    for j in range(1 << N):
        already = [None] * N
        for k in range(N):
            if j & (1 << k):
                already[k] = 1
            else:
                already[k] = 0

        v = 0
        for k in range(N):
            if already[k] == 1 or A[i - 1][k] == 1:
                v += 1 << k

        dp[i][j] = min(dp[i][j], dp[i - 1][j])
        dp[i][v] = min(dp[i][v], dp[i - 1][j] + 1)

print(-1 if dp[M][2**N - 1] == INF else dp[M][2**N - 1])
