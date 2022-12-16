# 二分探索（答えがx秒以下か？）
# A12 - Printer
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_l
N, K = map(int, input().split())
A = list(map(int, input().split()))

l = 1
r = 10**9

while l < r:
    m = (l + r) // 2
    total = 0
    for a in A:
        total += m // a
    if total >= K:
        r = m
    else:
        l = m + 1

print(l)
