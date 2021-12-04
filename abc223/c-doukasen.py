N = int(input())

A = []
B = []
t = 0
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    t += a / b

t /= 2
ans = 0

for i in range(N):
    ans += min(A[i], t * B[i])
    t -= min(A[i] / B[i], t)

print(ans)
