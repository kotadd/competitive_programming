# B - Grid Repainting 4
# まだ塗られていないマスを色 1, 2, 3, 4, 5 のいずれかで塗る方法
# https://atcoder.jp/contests/arc131/tasks/arc131_b

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

H, W = map(int, input().split())
d = [[0 for _ in range(W)] for _ in range(H)]

for i in range(H):
    c = input()
    for j in range(W):
        if c[j] != '.':
            d[i][j] = int(c[j])

for i in range(H):
    for j in range(W):
        if d[i][j] != 0:
            continue

        used = [False, False, False, False, False, False]
        for k in range(4):
            sx = i + dx[k]
            sy = j + dy[k]
            if sx >= 0 and sy >= 0 and sx < H and sy < W:
                used[d[sx][sy]] = True

        for k in range(1, 6):
            if not used[k]:
                d[i][j] = k
                break

for i in range(H):
    for j in range(W):
        print(d[i][j], end='')
    print()
