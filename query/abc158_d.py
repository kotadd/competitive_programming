# D - String Formation
# https://atcoder.jp/contests/abc158/tasks/abc158_d
from collections import deque
S = input()
Q = int(input())

tmp = 0
q = deque(S)
for i in range(Q):
    X = list(input().split())
    if X[0] == '1':
        tmp += 1
        tmp %= 2
    else:
        _, f, c = X
        if f == '1':
            if tmp == 0:
                q.appendleft(c)
            else:
                q.append(c)
        else:
            if tmp == 1:
                q.appendleft(c)
            else:
                q.append(c)

if tmp == 0:
    print(*q, sep='')
else:
    q.reverse()
    print(*q, sep='')
