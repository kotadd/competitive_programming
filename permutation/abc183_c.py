#  C - Travel
# 順列全探索 permutations

from itertools import permutations

N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]

A = list(range(1, N))
ans = 0
for X in permutations(A):
    X = [0] + list(X) + [0]
    t = 0
    for j in range(N):
        t += T[X[j]][X[j + 1]]
    if K == t:
        ans += 1

print(ans)
