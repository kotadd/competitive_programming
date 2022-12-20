# D - Union of Interval
# https://atcoder.jp/contests/abc256/tasks/abc256_d
N = int(input())

area = [0] * (2 * 10**5 + 1)
for _ in range(N):
    l, r = map(int, input().split())
    area[l] += 1
    area[r] -= 1

l = 2 * 10**5 + 1
cnt = 0
is_enabled = False
for i in range(1, 2 * 10**5 + 1):
    cnt += area[i]
    if cnt > 0:
        l = min(l, i)
        is_enabled = True
    elif cnt == 0 and is_enabled:
        print(l, i)
        l = 2 * 10**5 + 1
        is_enabled = False
