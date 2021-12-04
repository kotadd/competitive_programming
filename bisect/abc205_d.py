# D - Kth Excluded
# https://atcoder.jp/contests/abc205/tasks/abc205_d
# 二分探索
# 利用可能な整数の補完の仕方

import bisect

N, Q = map(int, input().split())
A = list(map(int, input().split()))

# C[i]: A[i]のタイミングで利用しても良い整数の数を補完する
C = [0] * N
for i in range(N):
    C[i] = A[i] - i - 1
for i in range(Q):
    k = int(input())
    # 利用可能な整数の数を確認し、番号を見つける（O(logN))
    r = bisect.bisect_left(C, k)
    if r == 0:
        print(k)
    else:
        # r-1: 利用可能な整数の一つ手前
        # (利用できない整数) - (そこまでに利用可能だった数) + (対象の数)
        print(A[r - 1] - C[r - 1] + k)
