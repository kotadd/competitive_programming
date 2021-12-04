# 階差を考えよう
import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = [0] * (N - 1)
ans = 0
for i in range(N - 1):
    B[i] = A[i + 1] - A[i]
    ans += abs(B[i])

for _ in range(Q):
    l, r, v = map(int, input().split())
    l -= 1
    r -= 1
    if l > 0:
        ans -= abs(B[l - 1])
        B[l - 1] += v
        ans += abs(B[l - 1])
    if r < N - 1:
        ans -= abs(B[r])
        B[r] -= v
        ans += abs(B[r])
    print(ans)
