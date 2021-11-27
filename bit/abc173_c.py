# https://atcoder.jp/contests/abc173/tasks/abc173_c
# C - H and V
from copy import deepcopy

H, W, K = map(int, input().split())
C = [list(input()) for _ in range(H)]

ans = 0
for i in range(1 << H):
    for j in range(1 << W):
        m = deepcopy(C)
        for k in range(H):
            if i & (1 << k):
                for x in range(W):
                    m[k][x] = 'R'
        for l in range(W):
            if j & (1 << l):
                for x in range(H):
                    m[x][l] = 'R'

        cnt = 0
        for k in range(H):
            for l in range(W):
                if m[k][l] == '#':
                    cnt += 1
        if cnt == K:
            ans += 1

print(ans)
