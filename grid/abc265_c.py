# C - Belt Conveyor
# https://atcoder.jp/contests/abc265/tasks/abc265_c

H, W = map(int, input().split())
G = [list(input()) for _ in range(H)]

cur = [0, 0]

# 空配列に追加する形にすると速度が落ちるため、最初に二次元配列で用意するべき
used = [[False] * W for _ in range(H)]

while 0 <= cur[0] < H and 0 <= cur[1] < W:
    if used[cur[0]][cur[1]]:
        print(-1)
        exit()

    used[cur[0]][cur[1]] = True

    direction = G[cur[0]][cur[1]]
    if direction == 'U':
        cur[0] -= 1
    elif direction == 'D':
        cur[0] += 1
    elif direction == 'L':
        cur[1] -= 1
    else:
        cur[1] += 1

cur[0] += 1
cur[1] += 1
if cur[0] == 0:
    cur[0] = 1
if cur[0] > H:
    cur[0] = H
if cur[1] == 0:
    cur[1] = 1
if cur[1] > W:
    cur[1] = W


print(cur[0], cur[1])
