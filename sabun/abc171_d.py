# D - Replacing
# https://atcoder.jp/contests/abc171/tasks/abc171_d
# 差分計算

from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
Q = int(input())

d = defaultdict(int)

for a in A:
    d[a] += 1

total = sum(A)

for i in range(Q):
    b, c = map(int, input().split())
    num = d[b]
    d[b] = 0
    d[c] += num
    total = total - b * num + c * num
    print(total)
