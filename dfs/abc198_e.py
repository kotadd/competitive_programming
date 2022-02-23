# E - Unique Color
# https://atcoder.jp/contests/abc198/tasks/abc198_e
# ■ 問題
# 頂点 1 から頂点 x への最短パスに、
# 頂点 x と同じ色で塗られた頂点が頂点 x 以外に存在しないとき、
# 頂点 x は よい頂点 であるといいます。
# 良い頂点を全て求める → dfs

import sys
sys.setrecursionlimit(10**7)

N = int(input())
C = list(map(int, input().split()))

G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)


def dfs(cur):
    seen[cur] = True
    for v in G[cur]:
        if seen[v]:
            continue
        if not cnt[C[v]]:
            ans.append(v + 1)
        cnt[C[v]] += 1
        seen[v] = 1
        dfs(v)
        cnt[C[v]] -= 1


seen = [False] * N
cnt = [0] * (10**5 + 1)
cnt[C[0]] = 1
ans = [1]
dfs(0)

ans.sort()
for a in ans:
    print(a)
