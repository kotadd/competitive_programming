# D - Powerful Discount Tickets
# https://atcoder.jp/contests/abc141/tasks/abc141_d
# 優先度付きキュー：O(MlogN)
from math import ceil
import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))

que = []
for a in A:
    que.append(-a)

heapq.heapify(que)

for i in range(M):
    x = heapq.heappop(que)
    heapq.heappush(que, ceil(x / 2))

print(abs(sum(que)))
