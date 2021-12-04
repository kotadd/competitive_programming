# 辞書順の対応表を作成し、名前を入れ替える問題
# Neo-lexicographic Ordering
# https://atcoder.jp/contests/abc219/tasks/abc219_c

import string

X = input()
N = int(input())
S = [input() for _ in range(N)]

d = dict()

# a-zの辞書順の対応表作成
# chr利用する場合
# for i in range(97, 123):
#     d[chr(i)] = X[i - 97]

# string.ascii_lowercaseを利用する場合
for i, s in enumerate(X):
    d[s] = string.ascii_lowercase[i]

res = []
for i in range(N):
    tmp = ""
    for s in S[i]:
        tmp += d[s]
    res.append((tmp, i))

res.sort()
ans = []
for a in res:
    _, i = a
    ans.append(S[i])

print(*ans, sep="\n")
