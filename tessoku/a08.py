# 二次元 累積和
# A08 - Two Dimensional Sum
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_h
H, W = map(int, input().split())

D = [list(map(int, input().split())) for _ in range(H)]
X = [[0] * (W + 2) for _ in range(H + 2)]

for i in range(1, H + 1):
    for j in range(1, W + 1):
        X[i][j] = X[i][j - 1] + D[i - 1][j - 1]

for i in range(1, H + 1):
    for j in range(1, W + 1):
        X[i][j] = X[i - 1][j] + X[i][j]

Q = int(input())
for _ in range(Q):
    a, b, c, d = map(int, input().split())

    print(X[c][d] - X[a - 1][d] - X[c][b - 1] + X[a - 1][b - 1])
