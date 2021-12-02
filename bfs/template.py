# https://atcoder.jp/contests/abc226/submissions/27081191
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]


# 深さ優先探索（辺の重みが1のときの最短経路） O(N+M)
def bfs():
    dist = [-1] * N
    q = deque()

    dist[0] = 0
    q.append(0)

    while q:
        v = q.popleft()
        for x in G[v]:
            if dist[x] != -1:
                continue
            dist[x] = dist[v] + 1
            q.append(x)
    return dist


for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

dist = bfs()
print(dist)
