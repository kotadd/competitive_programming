# E - Arithmetic Number
# https://atcoder.jp/contests/abc234/tasks/abc234_e

# 等差数列 : an = c0 + d(n-1)
# 初項(c0)が 1 以上 9 以下である。
# 公差(d)が −9 以上 8 以下である。
# 数列の長さ(len(X))は 1 以上 18 以下である。
# 第 2 項以降が全て 0 以上 9 以下である。

X = input()

ans = '9' * len(X)
for c0 in range(1, 10):
    for d in range(-9, 9):
        end = c0 + d * (len(X) - 1)
        if end >= 10 or end < 0:
            continue
        s = ''
        for k in range(len(X)):
            s += str(c0 + d * k)
        if s >= X:
            ans = min(ans, s)
print(ans)
