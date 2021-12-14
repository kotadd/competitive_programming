# D - Online games
# https://atcoder.jp/contests/abc221/tasks/abc221_d
# ×いもす法 ○ listを用いた方法

N = int(input())

events = []
for _ in range(N):
    a, b = map(int, input().split())
    events.append((a, 1))
    events.append((a + b, - 1))

events.sort()
ans = [0] * (N + 1)
num = 0
pre_day = 0
for next_day, v in events:
    ans[num] += next_day - pre_day
    num += v
    pre_day = next_day

print(*ans[1:])
