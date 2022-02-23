# E - Skiing
# https://atcoder.jp/contests/abc237/tasks/abc237_e

def dijkstra(G, s):
    from heapq import heappush, heappop

    INF = 1 << 60
    dist = [INF] * len(G)
    dist[s] = 0
    que = [(0, s)]
    while que:
        d, v = heappop(que)
        if d > dist[v]:
            continue
        for u, w in G[v]:
            nd = d + w
            if dist[u] > nd:
                dist[u] = nd
                heappush(que, (nd, u))
    return dist


N, M = map(int, input().split())
H = list(map(int, input().split()))

G = [[] for _ in range(N)]
for i in range(M):
    u, v = map(lambda x: int(x) - 1, input().split())
    if H[u] <= H[v]:
        G[u].append((v, (H[v] - H[u])))
        G[v].append((u, 0))
    elif H[u] > H[v]:
        G[u].append((v, 0))
        G[v].append((u, (H[u] - H[v])))

dist = dijkstra(G, 0)

print(G)
# print(max(H[0] - H[i] - dist[i] for i in range(N)))
