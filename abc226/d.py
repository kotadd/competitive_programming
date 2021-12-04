# gcd（最大公約数）の利用
from math import gcd

N = int(input())

ps = [tuple(map(int, input().split())) for _ in range(N)]

s = set()

for i in range(N):
    for j in range(N):
        if i == j:
            continue

        p1, p2 = ps[i], ps[j]
        x = p1[0] - p2[0]
        y = p1[1] - p2[1]
        g = gcd(x, y)
        x //= g
        y //= g
        s.add((x, y))

print(s)
print(len(s))
