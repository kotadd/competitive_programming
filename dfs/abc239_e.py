# E - Subtree K-th Max
# https://atcoder.jp/contests/abc239/tasks/abc239_e
# dfs（木のオイラーツアーの変形）
# 部分木の降順 x番目の値

import sys
sys.setrecursionlimit(10 ** 7)

N, Q = map(int, input().split())
X = list(map(int, input().split()))
G = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

query = [[] for _ in range(N)]
for i in range(Q):
    v, k = map(int, input().split())
    v -= 1
    query[v].append((i, k))

ans = [-1] * Q


def dfs(cur, pre):
    ret = [0] * 20
    ret[0] = X[cur]
    for next in G[cur]:
        if pre == next:
            continue
        tmp = dfs(next, cur)
        ret += tmp
        ret.sort(reverse=True)
        ret = ret[:20]
    for i, k in query[cur]:
        ans[i] = ret[k - 1]
    return ret


dfs(0, -1)
print(*ans, sep="\n")
