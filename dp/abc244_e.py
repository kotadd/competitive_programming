# E - King Bombee
# https://atcoder.jp/contests/abc244/tasks/abc244_e
# 三重配列の作り方

from collections import deque
MOD = 998244353

N, M, K, S, T, X = map(int, input().split())

S -= 1
T -= 1
X -= 1

G = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)

dp = [[[0] * N for _ in range(K + 1)] for _ in range(2)]

dp[0][0][S] = 1

que = deque([S])
for i in range(1, K + 1):
    se = set()
    while que:
        x = que.popleft()
        for v in G[x]:
            for j in range(2):
                if v == X:
                    dp[j][i][v] += dp[(j + 1) % 2][i - 1][x]
                else:
                    dp[j][i][v] += dp[j][i - 1][x]
                dp[j][i][v] %= MOD
            se.add(v)
    que = deque(se)


print(dp[0][K][T])
