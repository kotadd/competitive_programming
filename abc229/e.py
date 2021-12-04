from collections import deque

N, M = map(int, input().split())

G = [set() for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    G[a - 1].add(b - 1)

print(G)
ans = 0

A = []

for i in range(1, N):
    q = deque([i])
    s = set([i])
    while q:
        x = q.popleft()
        for y in G[x]:
            if y not in s:
                s.add(y)
                q.append(y)

    A.append(s)
    # print((N - i) - len(s) + 1)

print(A)
