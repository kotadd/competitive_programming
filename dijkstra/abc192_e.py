# E - Train
# https://atcoder.jp/contests/abc192/tasks/abc192_e
# ダイクストラ法の典型例

import heapq

N, M, X, Y = map(int, input().split())

X -= 1
Y -= 1

G = [[] for _ in range(N)]
for i in range(M):
    a, b, t, k = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append((b, t, k))
    G[b].append((a, t, k))

INF = 1 << 60
dist = [INF] * N
dist[X] = 0

que = []
heapq.heappush(que, (0, X))

while que:
    d, v = heapq.heappop(que)

    if d > dist[v]:
        continue

    for u, t, k in G[v]:
        x = 0
        if dist[v] % k != 0:
            x = k - (dist[v] % k)
        if dist[u] > dist[v] + t + x:
            dist[u] = dist[v] + t + x
            heapq.heappush(que, (dist[u], u))

print(dist[Y] if dist[Y] != INF else -1)
