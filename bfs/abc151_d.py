# D - Maze Master
# https://atcoder.jp/contests/abc151/tasks/abc151_d
# 移動回数が最小になるように求めるので、BFSを利用する

from collections import deque

INF = 10 ** 10
H, W = map(int, input().split())
maze = [list(input()) for _ in range(H)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
q = deque()
ans = 0

for i in range(H):
    for j in range(W):
        if maze[i][j] == "#":
            continue
        q.append((i, j))
        d = [[INF] * W for _ in range(H)]
        d[i][j] = 0
        while len(q):
            cur = q.popleft()
            ans = max(ans, d[cur[0]][cur[1]])
            for k in range(4):
                dx, dy = cur[0] + dxy[k][0], cur[1] + dxy[k][1]
                if 0 <= dx < H and 0 <= dy < W and maze[dx][dy] == "." and d[dx][dy] > d[cur[0]][cur[1]] + 1:
                    d[dx][dy] = d[cur[0]][cur[1]] + 1
                    q.append((dx, dy))

print(ans)
