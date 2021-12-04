# 二次元座標圧縮（大小関係を保ったまま、値を小さくせよ）
# C - Reorder Cards
H, W, N = map(int, input().split())

X, Y = [], []
for i in range(N):
    a, b = map(int, input().split())
    X.append(a)
    Y.append(b)

Xdict = {x: i + 1 for i, x in enumerate(sorted(list(set(X))))}
Ydict = {y: i + 1 for i, y in enumerate(sorted(list(set(Y))))}

for i in range(N):
    print(Xdict[X[i]], Ydict[Y[i]])
