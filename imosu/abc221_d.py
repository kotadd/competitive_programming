# D - Online games
# https://atcoder.jp/contests/abc221/tasks/abc221_d
# ×いもす法 ○ listを用いた方法

from collections import defaultdict
N = int(input())

d = defaultdict(int)
for i in range(N):
    a, b = map(int, input().split())
    a -= 1
    d[a] += 1
    d[a + b] -= 1

# dict 辞書をkey順でsort
d = sorted(d.items(), key=lambda x: x[0])

ans = [0] * (N + 1)
cur_num = 0
cur_date = 0
pre_date = 0
for k, v in d:
    cur_date = k
    ans[cur_num] += cur_date - pre_date
    cur_num += v
    pre_date = k


print(*ans[1:])


# 公式解答
# N = int(input())

# events = []
# for _ in range(N):
#     a, b = map(int, input().split())
#     events.append((a, 1))
#     events.append((a + b, - 1))

# events.sort()
# ans = [0] * (N + 1)
# num = 0
# pre_day = 0
# for next_day, v in events:
#     ans[num] += next_day - pre_day
#     num += v
#     pre_day = next_day

# print(*ans[1:])
