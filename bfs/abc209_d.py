# https://atcoder.jp/contests/abc209/tasks/abc209_d
# D - Collision
# bfs：二部グラフでも解ける
from collections import deque
N, Q = map(int, input().split())

G = [[] for _ in range(N)]


def bfs():
    dist = [-1] * N
    dist[0] = 0
    q = deque([0])

    while q:
        v = q.popleft()
        for x in G[v]:
            if dist[x] != -1:
                continue
            dist[x] = dist[v] + 1
            # color[x] = 1 - color[v]  # 二部グラフではこのように解く
            q.append(x)
    return dist


for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

dist = bfs()
for i in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if abs(dist[c] - dist[d]) % 2 == 1:
        print('Road')
    else:
        print('Town')
