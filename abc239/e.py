import sys
sys.setrecursionlimit(10 ** 7)

N, Q = map(int, input().split())
X = list(map(int, input().split()))
edges = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

query = [[] for _ in range(N)]
for i in range(Q):
    v, k = map(int, input().split())
    v -= 1
    query[v].append((i, k))

ans = [-1] * Q


def dfs(pos, bpos):
    ret = [0] * 20
    ret[0] = X[pos]
    for npos in edges[pos]:
        if bpos == npos:
            continue
        tmp = dfs(npos, pos)
        ret += tmp
        ret.sort(reverse=True)
        ret = ret[:20]
    for i, k in query[pos]:
        ans[i] = ret[k - 1]
    return ret


dfs(0, -1)
print(*ans, sep="\n")
