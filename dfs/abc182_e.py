# E - Akari
# https://atcoder.jp/contests/abc182/tasks/abc182_e
# マス目上のブロックの置かれていないマスのうち電球の光が届くものの数

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

H, W, N, M = map(int, input().split())

room = [[''] * W for _ in range(H)]
seen = [[0] * W for _ in range(H)]

L = []
for i in range(N):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    L.append((a, b))
    room[a][b] = 'L'

for i in range(M):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    room[c][d] = 'B'


def dfs(x, y, direction=0):
    if 0 <= x < H and 0 <= y < W and room[x][y] != 'B':
        if direction == 0:
            seen[x][y] = 1111
            dfs(x + 1, y, 1)
            dfs(x - 1, y, 2)
            dfs(x, y + 1, 3)
            dfs(x, y - 1, 4)
        elif direction == 1:
            if seen[x][y] % 100 == 10 or seen[x][y] % 100 == 11:
                return
            seen[x][y] += 10
            dfs(x + 1, y, 1)
        elif direction == 2:
            if seen[x][y] % 100 == 10 or seen[x][y] % 100 == 11:
                return
            seen[x][y] += 10
            dfs(x - 1, y, 2)
        elif direction == 3:
            if seen[x][y] % 10 == 1:
                return
            seen[x][y] += 1

            dfs(x, y + 1, 3)
        elif direction == 4:
            if seen[x][y] % 10 == 1:
                return
            seen[x][y] += 1
            dfs(x, y - 1, 4)


for x, y in L:
    dfs(x, y)

ans = 0
for i in range(H):
    ans += len(list(filter(lambda x: x > 0, seen[i])))

print(ans)
