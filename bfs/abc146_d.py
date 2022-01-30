# D - Coloring Edges on Tree
# https://atcoder.jp/contests/abc146/tasks/abc146_d
# 幅優先探索（深さ優先探索でも解ける）

from collections import deque

N = int(input())
adj = [[] for _ in range(N + 1)]
edge = {}
for i in range(N - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
    edge[(a, b)] = i
    edge[(b, a)] = i

que = deque()
que.append(1)
seen = [-1] * (N + 1)
seen[1] = 0
ans = [0] * (N - 1)
while que:
    v = que.pop()
    j = 1
    for u in adj[v]:
        if seen[u] == -1:
            if j == seen[v]:
                j += 1
            seen[u] = j
            ans[edge[(u, v)]] = j
            que.appendleft(u)
            j += 1

print(max(ans))
for a in ans:
    print(a)
