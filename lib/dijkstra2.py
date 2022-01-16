# ダイクストラ法（Dijkstra) 2
# すべての辺の重みが非負であることがわかっている場合

# 疎グラフの場合の解法：O(|E|log|V|)
# |E|=O(|V|)のとき

# ヒープを用いたダイクストラ法

import heapq
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

dist = [INF] * N
s -= 1
dist[s] = 0

que = []
heapq.heappush(que, (dist[s], s))


while (que):
    d, v = heapq.heappop()

    if d > dist[v]:
        continue

    for e in G[v]:
        if dist[e[0]] > dist[v] + e[1]:
            dist[e[0]] = dist[v] + e[1]
            heapq.heappush(que, (dist[e[0]], e[0]))

for v in range(N):
    if dist[v] < INF:
        print(dist[v])
