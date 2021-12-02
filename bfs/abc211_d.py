# D - Number of Shortest paths
# https://atcoder.jp/contests/abc211/tasks/abc211_d
# 最短経路の個数 ＝> bfsの変形

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
MOD = 10**9 + 7


def bfs():
    dist = [-1] * N
    visits = [0] * N
    q = deque()

    dist[0] = 0
    q.append(0)
    visits[0] = 1

    while q:
        v = q.popleft()
        for x in G[v]:
            # 訪問済みの場合は、遷移元への訪問回数を加算
            if dist[x] == dist[v] + 1:
                visits[x] += visits[v]
            if dist[x] != -1:
                continue
            dist[x] = dist[v] + 1
            # 初回訪問時も、遷移元への訪問回数を加算
            visits[x] += visits[v]
            q.append(x)
    return visits[N - 1] % MOD


for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

print(bfs())
