N, W = map(int, input().split())

A = []
for i in range(N):
    a, b = map(int, input().split())
    A.append([a, b])

A.sort(reverse=True)

ans = 0

for i in range(N):
    w = min(W, A[i][1])
    ans += A[i][0] * w
    W -= w
    if W <= 0:
        break

print(ans)
