# D - Ki
# https://atcoder.jp/contests/abc138/tasks/abc138_d

# pypy3はTLEだったが、pythonだとACになった。dfsはpythonの方が高速。

import sys
sys.setrecursionlimit(10**7)

N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

tmp = [0] * N
for i in range(Q):
    p, x = map(int, input().split())
    tmp[p - 1] += x

ans = [0] * N
ans[0] = tmp[0]


def dfs(cur, total):
    seen[cur] = True
    for v in G[cur]:
        if seen[v]:
            continue
        s = total + tmp[v]
        ans[v] += s
        dfs(v, s)


seen = [False] * N
dfs(0, tmp[0])

print(*ans)
