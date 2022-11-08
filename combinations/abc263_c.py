#  C - Monotonically Increasing
# https://atcoder.jp/contests/abc263/tasks/abc263_c
# 参考：https://note.nkmk.me/python-math-factorial-permutations-combinations/

import itertools

N, M = map(int, input().split())

L = list(range(1, M + 1))

for v in itertools.combinations(L, N):
    print(*v)
