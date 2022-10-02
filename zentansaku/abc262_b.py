# B - Triangle (Easier)
# https://atcoder.jp/contests/abc262/tasks/abc262_b

N, M = map(int, input().split())
adj = [[False] * N for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u][v] = True
    adj[v][u] = True

ans = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if adj[i][j] and adj[j][k] and adj[k][i]:
                ans += 1


print(ans)
