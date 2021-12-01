# dfs利用するときのおまじない
import sys
sys.setrecursionlimit(10**7)

G = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
ans = []


# 木のオイラーツアー
def dfs_euler(cur, pre):
    ans.append(cur + 1)
    for next in G[cur]:
        if next != pre:
            dfs_euler(next, cur)
            ans.append(cur + 1)


# 深さ優先探索
# seen = [False] * N
# def dfs(G, v):
#     seen[v] = True  # vを訪問済にする
#     for next_v in G:
#         if seen[next_v]:
#             continue
#         dfs(G, next_v)


# for v in range(N):
#     if seen[v]:
#         continue
#     dfs(G, v)
