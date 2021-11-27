N = int(input())

T = [int(input()) for _ in range(N)]

ans = 1000
for i in range(1 << N):
    tmp_a = 0
    tmp_b = 0
    for j in range(N):
        if i & (1 << j):
            tmp_a += T[j]
        else:
            tmp_b += T[j]
    res = max(tmp_a, tmp_b)
    ans = min(ans, res)

print(ans)
