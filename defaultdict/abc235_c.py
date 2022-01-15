# C - The Kth Time Query
# https://atcoder.jp/contests/abc235/tasks/abc235_c
# 数 xi がki 回目に登場するのは A の前から何番目の要素を見たときか
# defaultdict(list) の 連想配列 を利用する

from collections import defaultdict
N, Q = map(int, input().split())
A = list(map(int, input().split()))

d = defaultdict(list)

for i in range(N):
    d[A[i]].append(i + 1)

for i in range(Q):
    x, k = map(int, input().split())
    if k <= len(d[x]):
        print(d[x][k - 1])
    else:
        print(-1)
