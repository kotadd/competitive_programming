# 全点対間最短経路問題：フロイド・ワーシャル法（ワーシャルフロイド法） O(|V|^3)
# dp[k+1][i][j] = min(dp[k][i][j], dp[k][i][k] + dp[k][k][j]

N, M = map(int, input().split())
INF = 1 << 60
dp = [[INF] * N for _ in range(N)]

# a,b間の辺が存在し、距離がw
for i in range(M):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    dp[a][b] = w

# 同一点への距離は0
for i in range(N):
    dp[i][i] = 0

# dp遷移（フロイド・ワーシャル法）
for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

exists_negative_cycle = False

for v in range(N):
    if dp[v][v] < 0:
        exists_negative_cycle = True

ans = 0
if exists_negative_cycle:
    print('負閉路が存在します')
else:
    for i in range(N):
        for j in range(N):
            if dp[i][j] < INF // 2:
                ans += dp[i][j]

print(ans)
