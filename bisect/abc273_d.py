# D - LRUD Instructions
# https://atcoder.jp/contests/abc273/tasks/abc273_d
# 二分探索

from bisect import bisect_left

H, W, sx, sy, = map(int, input().split())
R = {}
C = {}
N = int(input())

for i in range(N):
    r, c = map(int, input().split())
    if r not in R:
        R[r] = []
    R[r].append(c)
    if c not in C:
        C[c] = []
    C[c].append(r)

for r in R:
    R[r].sort()
for c in C:
    C[c].sort()

Q = int(input())
r, c = sx, sy

for _ in range(Q):
    d, l = input().split()
    l = int(l)
    if d == 'U':
        if c not in C:
            r -= l
        else:
            p = bisect_left(C[c], r) - 1
            if p == -1:
                r -= l
            else:
                r = max(r - l, C[c][p] + 1)
    elif d == 'D':
        if c not in C:
            r += l
        else:
            p = bisect_left(C[c], r)
            if p == len(C[c]):
                r += l
            else:
                r = min(r + l, C[c][p] - 1)
    elif d == 'L':
        if r not in R:
            c -= l
        else:
            p = bisect_left(R[r], c) - 1
            if p == -1:
                c -= l
            else:
                c = max(c - l, R[r][p] + 1)
    else:
        if r not in R:
            c += l
        else:
            p = bisect_left(R[r], c)
            if p == len(R[r]):
                c += l
            else:
                c = min(c + l, R[r][p] - 1)
    r = max(r, 1)
    r = min(r, H)
    c = max(c, 1)
    c = min(c, W)
    print(r, c)
