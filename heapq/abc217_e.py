# E - Sorting Queries
# https://atcoder.jp/contests/abc217/tasks/abc217_e
# heapqとdequeの組み合わせ

from collections import deque
import heapq
import sys

# クエリ系で有効（数値を一つずつ取得できる）
it = map(int, sys.stdin.buffer.read().split())

A1 = deque()
A2 = []

Q = next(it)
for _ in range(Q):
    q = next(it)
    if q == 1:
        x = next(it)
        A1.append(x)
    elif q == 2:
        if len(A2) == 0:
            print(A1.popleft())
        else:
            print(heapq.heappop(A2))
    else:
        while A1:
            heapq.heappush(A2, A1.pop())
        # こうすると間に合わないので注意。
        #     A2.append(A1.popleft())
        # heapq.heapify(A2)
