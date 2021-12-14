# dfs利用するときのおまじない
import sys
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())

G = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
ans = []


# 深さ優先探索
# seen = [False] * N
# order = []　# トポロジカルソート用

# def dfs(G, v):
#     seen[v] = True  # vを訪問済にする
#     for next_v in G[v]:
#         if seen[next_v]:
#             continue
#         dfs(G, next_v)
#     order.append(v + 1) # トポロジカルソート用

# for v in range(N):
#     if seen[v]:
#         continue
#     dfs(G, v)

# print(order[::-1]) # トポロジカルソートの出力


# 木のオイラーツアー：深さ優先探索で通りかかった順番に頂点を記述する方法
def dfs_euler(cur, pre):
    ans.append(cur + 1)
    for next in G[cur]:
        if next != pre:
            dfs_euler(next, cur)
            ans.append(cur + 1)
