# D - Even Relation
# https://atcoder.jp/contests/abc126/tasks/abc126_d
# 二部グラフ
from collections import deque
N = int(input())

G = [[] for _ in range(N)]
d = dict()


def bfs():
    color = [-1] * N
    color[0] = 0
    q = deque([0])

    while q:
        v = q.popleft()
        for x in G[v]:
            if color[x] != -1:
                continue
            if x > v:
                dist = d[str(v) + str(x)]
            else:
                dist = d[str(x) + str(v)]
            if dist % 2 == 0:
                color[x] = color[v]
            else:
                color[x] = 1 - color[v]
            q.append(x)
    return color


for i in range(N - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)
    if u > v:
        u, v = v, u
    d[str(u) + str(v)] = w  # dictではなく、Graphに対するsetでも良かったかも

color = bfs()

print(*color, sep='\n')
