N, M, X = map(int, input().split())

C = [0] * N
A = []
for i in range(N):
    C[i], *a = map(int, input().split())
    A.append(a)


ans = 10**10
for i in range(1 << N):
    c = 0
    s = [0] * M
    for j in range(N):
        if i & (1 << j):
            c += C[j]
            a = A[j]
            for k in range(M):
                s[k] += a[k]
    for x in s:
        if x < X:
            break
    else:
        ans = min(ans, c)

if ans == 10**10:
    print(-1)
else:
    print(ans)
