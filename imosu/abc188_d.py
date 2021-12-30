# D - Snuke Prime
# https://atcoder.jp/contests/abc188/tasks/abc188_d

from collections import defaultdict
N, C = map(int, input().split())

d = defaultdict(int)
for i in range(N):
    a, b, c = map(int, input().split())
    d[a] += c
    d[b + 1] -= c


events = sorted(d.items(), key=lambda x: x[0])

pre_date = 0
current_value = 0
ans = 0
for k, v in events:
    ans += min(current_value, C) * (k - 1 - pre_date)
    current_value += v
    ans += min(current_value, C)
    pre_date = k

print(ans)


# 公式解答
# aの一日前に料金が上がり、bの一日後に料金が下がるので、計算としてはa-1でOK
N, C = map(int, input().split())
event = []
for i in range(N):
    a, b, c = map(int, input().split())
    a -= 1
    event.append((a, c))
    event.append((b, -c))

event.sort()
ans = 0
fee = 0
t = 0
for x, y in event:
    if x != t:
        ans += min(C, fee) * (x - t)
        t = x
    fee += y

print(ans)
