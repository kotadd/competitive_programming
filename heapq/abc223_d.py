# D - Restricted Permutation
# https://atcoder.jp/contests/abc223/tasks/abc223_d
# いくつかの辺の順序が決まっており、辞書順最小の数列
# トポロジカルソートの解説：https://qiita.com/drken/items/996d80bcae64649a6580
# topological sort
# 小さい順（辞書順）を求められたときは、heapq

# 8 12
# 4 1
# 4 6
# 4 2
# 1 6
# 1 3
# 6 7
# 2 7
# 2 5
# 3 7
# 3 0
# 7 0
# 0 5
# 5 2 3 4 7 8 1 6

import heapq
N, M = map(int, input().split())
G = [[] for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)


# トポロジカルソート（BFS）
def bfs(N, G):
    deg = [0] * N  # 入次数のリスト

    for g in G:
        for v in g:
            deg[v] += 1

    S = []
    que = [i for i in range(N) if deg[i] == 0]  # 入次数が0の頂点(シンク)リスト

    heapq.heapify(que)  # 入次数が0の頂点を昇順に取り出せるように

    while que:
        v = heapq.heappop(que)
        S.append(v)
        for u in G[v]:
            deg[u] -= 1
            if deg[u] == 0:
                heapq.heappush(que, u)

    return S


ans = bfs(N, G)
if len(ans) != N:
    print(-1)
else:
    print(*map(lambda x: x + 1, ans))
