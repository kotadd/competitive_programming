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
