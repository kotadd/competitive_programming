# E - Transformable Teacher
# https://atcoder.jp/contests/abc181/tasks/abc181_e
# 二分探索 + 累積和
import bisect

N, M = map(int, input().split())
H = sorted(list(map(int, input().split())))
W = list(map(int, input().split()))

A = [0] * (N // 2 + 1)
B = [0] * (N // 2 + 1)
for i in range(1, N, 2):
    A[i // 2 + 1] = A[i // 2] + H[i] - H[i - 1]
    B[i // 2 + 1] = B[i // 2] + H[i + 1] - H[i]

ans = 1 << 60

for w in W:
    r = bisect.bisect_left(H, w)
    if r % 2:
        r -= 1
    ans = min(ans, A[r // 2] + B[-1] - B[r // 2] + abs(H[r] - w))

print(ans)
