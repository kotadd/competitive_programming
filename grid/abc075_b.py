# https://atcoder.jp/contests/abc075/tasks/abc075_b
# 斜め含む周辺に移動できるパターン

H, W = map(int, input().split())

S = [input() for _ in range(H)]

for y in range(H):
    for x in range(W):
        if S[y][x] == '#':
            continue
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if not 0 <= y + dy < H or not 0 <= x + dx < W:
                    continue
                if S[y + dy][x + dx] == '#':
                    count += 1
        S[y][x] = str(count)

for s in S:
    print("".join(s))
