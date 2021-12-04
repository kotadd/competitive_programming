# dequeを知っていますか？
from collections import deque

q = int(input())

cards = deque()
res = []
for i in range(q):
    t, x = map(int, input().split())
    if t == 1:
        cards.appendleft(x)
    elif t == 2:
        cards.append(x)
    else:
        res.append(cards[x - 1])

print(*res, sep="\n")
