N = int(input())

P = []
for i in range(N):
    x, y = map(int, input().split())
    P.append((x, y))

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        dx = abs(P[i][0] - P[j][0])
        dy = abs(P[i][1] - P[j][1])
        ans = max(ans, dx**2 + dy**2)

print(ans**(1 / 2))
