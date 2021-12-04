# C - March
# https://atcoder.jp/contests/abc089/tasks/abc089_c
# 途中
from itertools import combinations
from collections import defaultdict

N = int(input())
d = defaultdict(int)

for i in range(N):
    d[input()[0]] += 1

ans = 0
for v in combinations('MARCH', 3):
    ans += d[v[0]] * d[v[1]] * d[v[2]]

print(ans)
