# C - Simple path
# https://atcoder.jp/contests/abc270/tasks/abc270_c
# 幅優先探索 bfs
# 単純パス上の頂点を列挙する

from collections import deque

N, X, Y = map(int, input().split())
G = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

# 一つ前の頂点を記録する
bef = [-1] * (N + 1)
bef[X] = -2
que = deque([X])

while que:
    v = que.pop()
    for x in G[v]:
        if bef[x] != -1:
            continue
        bef[x] = v
        que.append(x)


ans = []
while Y != -2:
    ans.append(Y)
    Y = bef[Y]

print(*ans[::-1])
