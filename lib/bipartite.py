# 二部グラフの判定
def dfs(G, v, cur=0):
    color[v] = cur
    for next_v in G[v]:
        # 隣接頂点がすでに色確定していた場合、同じ色が隣接すると二部グラフでない
        if color[next_v] != -1:
            if color[next_v] == cur:
                return False
            # 色が確定していたため探索しない
            continue
        # 隣接頂点の色を変えて、再起的に探索
        if not dfs(G, next_v, 1 - cur):
            return False
    return True


N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)

color = [-1] * N
is_bipartite = True
for v in range(N):
    if color[v] != -1:
        continue
    if not dfs(G, v):
        is_bipartite = False

print(color)
if is_bipartite:
    print('Yes')
else:
    print('No')
