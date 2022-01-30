# C Peaks
# グラフの問題

N, M = map(int, input().split())
H = list(map(int, input().split()))

G = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

ans = 0
for i in range(N):
    for g in G[i]:
        if H[i] <= H[g]:
            break
    else:
        ans += 1

print(ans)
