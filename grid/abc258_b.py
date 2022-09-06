# B - Number Box
# https://atcoder.jp/contests/abc258/editorial/4256
# grid
N = int(input())
A = [input() for _ in range(N)]

tmp = 0
pos = []
for i in range(N):
    for j in range(N):
        if int(A[i][j]) > tmp:
            tmp = int(A[i][j])
            pos = [(i, j)]
        elif int(A[i][j]) == tmp:
            pos.append((i, j))

ans = 0
dxy = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (1, -1), (1, 1), (-1, 1)]
for x, y in pos:
    for dx, dy in dxy:
        tmp = A[x][y]
        for i in range(1, N):
            tmp += A[(x + dx * i) % N][(y + dy * i) % N]
        ans = max(ans, int(tmp))

print(ans)
