# B - Prefix?
# https://atcoder.jp/contests/abc268/tasks/abc268_b
# 接頭語の一致かどうか

S = input()
T = input()

if T.startswith(S):
    print('Yes')
else:
    print('No')
