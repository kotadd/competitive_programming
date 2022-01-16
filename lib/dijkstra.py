# ダイクストラ法（Dijkstra)
# すべての辺の重みが非負であることがわかっている場合
# 密グラフの場合の解法：O(|V|^2

INF = 1 << 60

# sは始点
N, M, s = map(int, input().split())
G = [[] for _ in range(N)]

# wは距離
for i in range(M):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append((b, w))

used = [False] * N
dist = [INF] * N
s -= 1
dist[s] = 0

for i in range(N):
    min_dist = INF
    min_v = -1
    for v in range(N):
        if not used[v] and dist[v] < min_dist:
            min_dist = dist[v]
            min_v = v

    if min_v == -1:
        break

    for e in G[min_v]:
        if dist[e[0]] > dist[min_v] + e[1]:
            dist[e[0]] = dist[min_v] + e[1]

    used[min_v] = True

for v in range(N):
    if dist[v] < INF:
        print(dist[v])
