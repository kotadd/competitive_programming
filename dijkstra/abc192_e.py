# E - Train
# https://atcoder.jp/contests/abc192/tasks/abc192_e
# ダイクストラ法の典型例

import heapq
from math import ceil
INF = 1 << 60


N, M, X, Y = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    a, b, t, k = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append((b, t, k))
    G[b].append((a, t, k))

X -= 1
Y -= 1

dist = [INF] * N
dist[X] = 0

que = []
heapq.heappush(que, (dist[X], X))


while que:
    d, u = heapq.heappop(que)

    if d > dist[u]:
        continue

    dist[u] = d
    for b, t, k in G[u]:
        cur = ceil(d / k) * k + t
        if dist[b] > cur:
            heapq.heappush(que, (cur, b))

if dist[Y] == INF:
    print(INF)
else:
    print(dist[Y])
