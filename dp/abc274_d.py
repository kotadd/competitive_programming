#  D - Robot Arms 2
# https://atcoder.jp/contests/abc274/tasks/abc274_d
# 典型的なdpの問題
# +-の組み合わせがあるので注意

N, x, y = map(int, input().split())
A = list(map(int, input().split()))
M = 10**4

x -= A[0]
xs = A[2::2]
ys = A[1::2]

dpx = [False] * 2 * (M + 1)
dpy = [False] * 2 * (M + 1)
dpx[M + 1] = True
dpy[M + 1] = True
for dx in xs:
    nx = [False] * 2 * (M + 1)
    for i in range(2 * (M + 1)):
        if dpx[i]:
            nx[i - dx] = nx[i + dx] = True
    dpx = nx

for dy in ys:
    ny = [False] * 2 * (M + 1)
    for i in range(2 * (M + 1)):
        if dpy[i]:
            ny[i - dy] = ny[i + dy] = True
    dpy = ny


if dpx[x + M + 1] and dpy[y + M + 1]:
    print('Yes')
else:
    print('No')
