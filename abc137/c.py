# C - Green Bin
# https://atcoder.jp/contests/abc137/tasks/abc137_c
# アナグラム anagram

N = int(input())

d = dict()
ans = 0
for i in range(N):
    s = str(sorted(list(input())))
    if s not in d:
        d[s] = 1
    else:
        ans += d[s]
        d[s] += 1

print(ans)
