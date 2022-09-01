# C - Choose Elements
# https://atcoder.jp/contests/abc245/tasks/abc245_c
from functools import lru_cache
import sys
sys.setrecursionlimit(10**7)

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


@lru_cache(maxsize=10000000)
def dfs(i, x):
    if i == N:
        print('Yes')
        exit()

    a = A[i]
    b = B[i]
    if abs(x - a) <= K:
        dfs(i + 1, a)
    if abs(x - b) <= K:
        dfs(i + 1, b)


dfs(1, A[0])
dfs(1, B[0])
print('No')
