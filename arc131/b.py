# B - Grid Repainting 4
# まだ塗られていないマスを色 1, 2, 3, 4, 5 のいずれかで塗る方法
# https://atcoder.jp/contests/arc131/tasks/arc131_b

# 隣接するマスの情報
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

H, W = map(int, input().split())
d = [[0 for j in range(W)] for i in range(H)]

# 入力 + それを整数に変換（d[i][j] はマス (i+1,j+1) に対応）
for i in range(H):
    c = input()
    for j in range(W):
        if c[j] == '.':
            d[i][j] = 0
        else:
            d[i][j] = (int(c[j]) - int('0'))


for i in range(H):
    for j in range(W):
        if d[i][j] == 0:
            # 変数 used[k] は色 k が隣接マスに存在するかを表す
            used = [False, False, False, False, False, False]
            for k in range(4):
                sx = i + dx[k]
                sy = j + dy[k]
                if sx >= 0 and sx < H and sy >= 0 and sy < W:
                    used[d[sx][sy]] = True

            # どの色で塗れるかを探す（このプログラムは、どの隣接するマスとも異なる色のうち番号が最小の色で塗っている）
            for k in range(1, 6):
                if not used[k]:
                    d[i][j] = k
                    break

for i in range(H):
    for j in range(W):
        print(d[i][j], end='')
    print("")
