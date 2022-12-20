# Make Bipartite 2
# https://atcoder.jp/contests/abc282/tasks/abc282_d
# 参考：https://atcoder.jp/contests/abc282/submissions/37330422
# 二部グラフ

from collections import deque

N, M = map(int, input().split())
edges = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]

G = [[] for _ in range(N)]
for a, b in edges:
    G[a].append(b)
    G[b].append(a)

dist = [-1] * N
ans = N * (N - 1) // 2 - M
for i in range(N):
    if dist[i] == -1:
        q = deque()
        q.append(i)
        dist[i] = 0
        c0, c1 = 0, 0
        while len(q) >= 1:
            u = q.popleft()
            if dist[u] % 2 == 0:
                c0 += 1
            else:
                c1 += 1
            for i in G[u]:
                if dist[i] == -1:
                    dist[i] = dist[u] + 1
                    q.append(i)
        ans -= c0 * (c0 - 1) // 2
        ans -= c1 * (c1 - 1) // 2

is_bipartite = True
for a, b in edges:
    if dist[a] % 2 == dist[b] % 2:
        is_bipartite = False

if not is_bipartite:
    print(0)
else:
    print(ans)
