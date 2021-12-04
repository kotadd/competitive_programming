N = int(input())
A = list(map(int, input().split()))
X = int(input())

sumA = sum(A)

p = X // sumA
X %= sumA
ans = N * p

for a in A:
    X -= a
    ans += 1
    if X < 0:
        break

print(ans)
