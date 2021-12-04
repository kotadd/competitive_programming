# 要素の検索はソートして二分探索
from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))
q = int(input())

res = []
for _ in range(q):
    b = int(input())
    idx = bisect_left(a, b)
    diff = 0
    if idx == 0:
        diff = abs(a[idx] - b)
    elif idx == n:
        diff = abs(a[idx - 1] - b)
    else:
        diff = min(abs(a[idx] - b), abs(a[idx - 1] - b))
    res.append(diff)

print(*res, sep="\n")
