# A 深さ優先探索 https://atcoder.jp/contests/atc001/tasks/dfs_a
import sys
sys.setrecursionlimit(10**7)

h, w = map(int, input().split())
reached = [[0] * w for _ in range(h)]
maze = [list(input()) for _ in range(h)]


def dfs(x, y):
    if x < 0 or h <= x or y < 0 or w <= y or maze[x][y] == '#':
        return
    if reached[x][y] == 1:
        return
    reached[x][y] = 1

    dfs(x + 1, y)
    dfs(x - 1, y)
    dfs(x, y + 1)
    dfs(x, y - 1)


for row in range(h):
    for col in range(w):
        if maze[row][col] == "s":
            s = [row, col]
        elif maze[row][col] == "g":
            g = [row, col]

dfs(s[0], s[1])
if reached[g[0]][g[1]] == 1:
    print('Yes')
else:
    print('No')
