# E - Dist Max
# https://atcoder.jp/contests/abc178/tasks/abc178_e
# マンハッタン距離の典型例
# 45度回転を利用する

N = int(input())

INF = 1 << 60
max_z = -INF
min_z = INF
max_w = -INF
min_w = INF

ans = -INF
for _ in range(N):
    x, y = map(int, input().split())
    z = x + y
    w = x - y

    max_z = max(max_z, z)
    min_z = min(min_z, z)
    max_w = max(max_w, w)
    min_w = min(min_w, w)

    ans = max(max_z - min_z, max_w - min_w)

print(ans)
