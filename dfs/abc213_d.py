# D - Takahashi Tour
# https://atcoder.jp/contests/abc213/tasks/abc213_d
import sys
sys.setrecursionlimit(10**7)

N = int(input())

G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

for i in range(N):
    G[i].sort()

ans = []


# 木のオイラーツアー：深さ優先探索で通りかかった順番に頂点を記述する方法
def dfs(cur, pre):
    ans.append(cur + 1)
    for next in G[cur]:
        if next != pre:
            dfs(next, cur)
            ans.append(cur + 1)


dfs(0, -1)
print(*ans)
