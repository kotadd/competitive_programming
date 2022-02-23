# E - Peddler
# https://atcoder.jp/contests/abc188/tasks/abc188_e
# Xi<Yi のため、DAG (Directed Acyclic Graph, 閉路を含まない有向グラフ)
# DAG => 動的計画法で解ける

INF = 1 << 60

N, M = map(int, input().split())
A = list(map(int, input().split()))

G = [[] for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    G[x].append(y)

ans = -INF

# dp[i] : 街iに到達できる街(街i自身を含まない) における金の最安値 O(N+M)
dp = [INF] * N
for i in range(N):
    ans = max(ans, A[i] - dp[i])
    for j in G[i]:
        dp[j] = min(dp[j], dp[i], A[i])

print(ans)
