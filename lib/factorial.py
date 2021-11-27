from itertools import permutations
from math import sqrt, factorial

N = int(input())

A = []
for i in range(N):
    x, y = map(int, input().split())
    A.append((x, y))

ans = 0
for X in permutations(A):
    tmp = 0
    for j in range(1, len(X)):
        x1, y1 = X[j - 1]
        x2, y2 = X[j]

        tmp += sqrt((x2 - x1)**2 + (y2 - y1)**2)
    ans += tmp

print(ans / factorial(N))
