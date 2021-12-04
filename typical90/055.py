n, p, q = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(n):
    a = A[i] % p
    for j in range(i + 1, n):
        b = a * A[j] % p
        for k in range(j + 1, n):
            c = b * A[k] % p
            for l in range(k + 1, n):
                d = c * A[l] % p
                for m in range(l + 1, n):
                    if d * A[m] % p == q:
                        ans += 1

print(ans)
