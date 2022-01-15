# D - Prefix K-th Max
# https://atcoder.jp/contests/abc234/tasks/abc234_d
import heapq

N, K = map(int, input().split())
P = list(map(int, input().split()))
que = P[0:K]
heapq.heapify(que)
print(que[0])
for i in range(K, N):
    x = heapq.heappop(que)
    x = max(x, P[i])
    heapq.heappush(que, x)
    print(que[0])
