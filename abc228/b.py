from collections import deque

N, X = map(int, input().split())
A = list(map(int, input().split()))

q = deque([X - 1])
s = set()

while q:
    x = q.popleft()
    if x not in s:
        s.add(x)
        q.append(A[x] - 1)

print(len(s))
