# D - Longest X
# https://atcoder.jp/contests/abc229/tasks/abc229_d
# 尺取り法

S = list(input())
K = int(input())

ans = 0
cur = 0
l = 0

for r in range(len(S)):
    if S[r] == '.':
        cur += 1
    while cur > K:
        if S[l] == '.':
            cur -= 1
        l += 1
    ans = max(ans, r - l + 1)
print(ans)
