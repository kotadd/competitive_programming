# https://atcoder.jp/contests/abc096/tasks/abc096_c
# 上下左右しか動けないパターン

H, W = map(int, input().split())

S = [input() for _ in range(H)]

dxy = [(-1, 0), (0, -1), (1, 0), (0, 1)]
for y in range(H):
    for x in range(W):
        if S[y][x] == '.':
            continue
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not 0 <= nx < W or not 0 <= ny < H:
                continue
            if S[ny][nx] == '#':
                break
        else:
            print('No')
            exit()

print('Yes')
