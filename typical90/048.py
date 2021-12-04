# 上界と下界を見積もる
# 部分点を取った後に満点を取るか決める

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

L = []
for i in range(n):
    a, b = map(int, input().split())
    L.append(a - b)
    L.append(b)
L.sort()
print(sum(L[-k:]))
