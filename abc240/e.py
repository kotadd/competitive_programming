import sys
sys.setrecursionlimit(10**7)

N = int(input())
G = [[] for _ in range(N)]
ans = [0] * N

for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)


def dfs(cur, pre):
    global leaf
    ans[cur] = [leaf, leaf]
    for nxt in G[cur]:
        if nxt == pre:
            continue
        dfs(nxt, cur)
        ans[cur][1] = max(ans[cur][1], ans[nxt][1])

    if ans[cur][1] == leaf:
        leaf += 1


leaf = 1
dfs(0, -1)

for i in range(N):
    print(*ans[i])
