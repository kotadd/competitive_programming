# D - .. (Double Dots)
# https://atcoder.jp/contests/abc168/tasks/abc168_d
# bfsの典型問題
# 出力に注意：
# 目標を達成できる道しるべの配置が存在する場合は Yes かつ 部屋 i の道しるべが指す部屋の番号を出力

from collections import deque

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)


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
            dist[x] = v + 1
            q.append(x)
    return dist


print("Yes")
dist = bfs()
for i in dist[1:]:
    print(i)
