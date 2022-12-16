# 二次元 累積和
# A09 - Winter in ALGO Kingdom
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_i

H, W, N = map(int, input().split())

D = [[0] * (W + 2) for _ in range(H + 2)]
X = [[0] * (W + 2) for _ in range(H + 2)]

for i in range(N):
    a, b, c, d = map(int, input().split())
    D[a][b] += 1
    D[a][d + 1] -= 1
    D[c + 1][b] -= 1
    D[c + 1][d + 1] += 1

for i in range(1, H + 1):
    for j in range(1, W + 1):
        X[i][j] = X[i][j - 1] + D[i][j]

for i in range(1, H + 1):
    for j in range(1, W + 1):
        X[i][j] = X[i - 1][j] + X[i][j]

for i in range(1, H + 1):
    print(*X[i][1:-1])
