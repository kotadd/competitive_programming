# E - Σ[k=0..10^100]floor(X／10^k)
# https://atcoder.jp/contests/abc233/tasks/abc233_e
# Xを整数型で管理すると10^500000桁が大きすぎるので注意

from collections import deque
X = input()

q = deque()
cur = 0
for x in X:
    cur += int(x)
    q.append(cur)

ans = []
cur = 0
while q:
    val = q.pop()
    total = val + cur
    ans.append(total % 10)
    cur = total // 10
if cur > 0:
    ans.append(cur)
print(*reversed(ans), sep='')


# 無限等比級数で考えると簡単に解ける
# https://mathwords.net/mugenwa
# https://atcoder.jp/contests/abc233/editorial/3193
# I = input()
# s = sum((int(a) for a in I))
# X = int(I)
# print((X * 10 - s) // 9)
