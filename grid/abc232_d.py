# D - Weak Takahashi
# https://atcoder.jp/contests/abc232/tasks/abc232_d
# (1,0),(0,1)の移動を繰り返し、#かgrid外に出られない時に何マス移動できるか？
# #のマスで移動0にして、grid内で移動する => dp
H, W = map(int, input().split())

S = [input() for _ in range(H)]

dxy = [(1, 0), (0, 1)]
dp = [[0] * W for _ in range(H)]
dp[0][0] = 1

ans = 1
for y in range(H):
    for x in range(W):
        if dp[y][x] == 0:
            continue
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not 0 <= nx < W or not 0 <= ny < H:
                continue
            if S[ny][nx] == '.':
                dp[ny][nx] = dp[y][x] + 1
            else:
                dp[ny][nx] = 0
            ans = max(ans, dp[ny][nx])

print(ans)
