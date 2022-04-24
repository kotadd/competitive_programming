# D - Range Count Query
# https://atcoder.jp/contests/abc248/tasks/abc248_d
# 多重配列だとメモリ消費が大きくなるので、数値ごとに呼び出されたindexを管理するリストを作成する

from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
M = 2 * 10**5 + 1

idx = [[] for _ in range(M)]
for i in range(N):
    idx[A[i]].append(i)

for _ in range(Q):
    L, R, X = map(int, input().split())
    l = bisect_left(idx[X], L - 1)
    r = bisect_left(idx[X], R)
    print(r - l)
