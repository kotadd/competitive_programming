from collections import deque

N = int(input())
A = list(map(int, input().split()))


q = deque([(A[0], 1)])
cnt = 1
print(1)
for i in range(1, N):
    a = A[i]
    if q and q[-1][0] == a:
        cnt += 1
    else:
        cnt = 1
    if cnt == a:
        for i in range(a - 1):
            q.pop()
        if q:
            cnt = q[-1][1]
        else:
            cnt = 0
    else:
        q.append([a, cnt])
    print(len(q))
