# 単一始点最短路問題：ベルマン・フォード法（O(|V||E|)
# 始点sから到達できる負閉路が存在するならばその旨を報告し、存在しないならば各頂点への最短路を求めるアルゴリズム。

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

exist_negative_cycle = False
dist = [INF] * N
s -= 1
dist[s] = 0

for i in range(N):
    update = False
    for v in range(N):
        if dist[v] == INF:
            continue
        for e in G[v]:
            if dist[e[0]] > dist[v] + e[1]:
                dist[e[0]] = dist[v] + e[1]
                update = True

    if not update:
        break

    if i == N - 1 and update:
        exist_negative_cycle = True

    if exist_negative_cycle:
        print('負閉路が存在します')
    else:
        for v in range(N):
            if dist[v] < INF:
                print(dist[v])
