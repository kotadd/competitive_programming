import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
# G[i] は都市iから道路で直接繋がっている都市のリスト
G = [[] for _ in range(N)]

for i in range(M):
    A, B = map(int, input().split())
    G[A - 1].append(B - 1)


def dfs(v):
    if temp[v]:
        return  # 同じ頂点を2度以上調べないためのreturn
    temp[v] = 1
    for vv in G[v]:
        dfs(vv)


ans = 0
# 都市iからスタートする場合
for i in range(N):
    temp = [0] * N
    # temp[j] は都市jに到達可能かどうかを表す
    dfs(i)
    ans += sum(temp)
print(ans)
