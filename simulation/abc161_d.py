# D - Lunlun Number
# https://atcoder.jp/contests/abc161/tasks/abc161_d

from collections import deque
K = int(input())

q = deque(i for i in range(1, 10))

for i in range(K):
    x = q.popleft()
    y = 10 * x + x % 10
    if x % 10 != 0:
        q.append(y - 1)
    q.append(y)
    if x % 10 != 9:
        q.append(y + 1)
print(x)
