# C - Jumping Takahashi
# https://atcoder.jp/contests/abc240/tasks/abc240_c

from functools import lru_cache

import sys
sys.setrecursionlimit(10 ** 7)

N, X = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

cnt = [0] * 10000


@lru_cache(maxsize=10000000)
def dfs(cur, jump):
    next = cur + 1

    if next == N:
        if jump == X:
            print('Yes')
            exit()
        return

    dfs(next, A[next][0] + jump)
    dfs(next, A[next][1] + jump)


dfs(-1, 0)

print('No')
