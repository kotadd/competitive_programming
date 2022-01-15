# D - Handstand 2
# https://atcoder.jp/contests/abc152/tasks/abc152_d

N = int(input())

cnt = [[0] * 10 for _ in range(10)]
for i in range(1, N + 1):
    s = str(i)
    cnt[int(s[0])][int(s[-1])] += 1

ans = 0
for i in range(1, N + 1):
    s = str(i)
    ans += cnt[int(s[-1])][int(s[0])]

print(ans)
