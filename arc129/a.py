N, L, R = map(int, input().split())
R += 1
ans = 0
for i in range(64):
    if N >> i & 1:
        p, q = 1 << i, 1 << i + 1
        upper = min(q, R)
        lower = max(p, L)
        ans += max(0, upper - lower)
print(ans)
