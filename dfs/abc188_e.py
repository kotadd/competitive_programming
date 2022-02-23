# E - Peddler
# https://atcoder.jp/contests/abc188/tasks/abc188_e
# Xi<Yi のため、DAG (Directed Acyclic Graph, 閉路を含まない有向グラフ)
# DAGなのでdpで解くべきだが、dfsはXi<Yiの制約がなくても解けるはず
# （bfsを利用して、金の取引価格が低い順に実施すれば制約なしで解ける）

import sys
sys.setrecursionlimit(10**7)

INF = 1 << 60

N, M = map(int, input().split())
A = list(map(int, input().split()))

G = [[] for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    G[x].append(y)


def dfs(i, m):
    cur = m

    if mem[i] != -1:
        return mem[i]

    for v in G[i]:
        x = dfs(v, A[v])
        mem[i] = max(mem[i], x, A[v])
        cur = max(cur, mem[v])

    return mem[i]


ans = -INF

mem = [-1] * N
for i in range(N):
    if len(G[i]) > 0:
        ans = max(ans, dfs(i, -1) - A[i])

print(ans)
