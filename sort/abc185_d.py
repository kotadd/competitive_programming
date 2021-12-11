# D - Stamp
# https://atcoder.jp/contests/abc185/tasks/abc185_d
from math import ceil
N, M = map(int, input().split())
# O(Mlog(M))
A = sorted([0] + list(map(int, input().split())))

k = 10**10
if N == M:
    print(0)
elif M == 0:
    print(1)
else:
    for i in range(1, M + 1):
        diff = A[i] - A[i - 1] - 1
        if diff > 0:
            k = min(k, diff)

    ans = 0
    for i in range(1, M + 1):
        ans += ceil((A[i] - A[i - 1] - 1) / k)
    ans += ceil((N - A[M]) / k)
    print(ans)
