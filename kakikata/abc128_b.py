# B - Guidebook
# https://atcoder.jp/contests/abc128/tasks/abc128_b
# 2つ目以降のkeyに対するsortの方法

N = int(input())
X = []
for i in range(N):
    s, p = input().split()
    p = int(p)
    X.append([i + 1, s, p])

X.sort(key=lambda x: (x[1], -x[2]))
for i in range(N):
    print(X[i][0])
