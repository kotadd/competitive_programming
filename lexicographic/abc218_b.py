# B - qwerty
# https://atcoder.jp/contests/abc218/tasks/abc218_b
# string.ascii_lowercaseを知っているかの問題
import string

P = list(map(int, input().split()))

ans = []
for p in P:
    # string.ascii_lowercase[0] == 'a'
    ans.append(string.ascii_lowercase[p - 1])

print(*ans, sep="")
