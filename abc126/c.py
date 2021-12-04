# C - Dice and Coin
# サイコロ＋コイン
# https://atcoder.jp/contests/abc126/tasks/abc126_c

N, K = map(int, input().split())

ans = 0

for i in range(1, N + 1):
    now = i
    tmp = 1 / N
    while now < K:
        now *= 2
        tmp /= 2
    ans += tmp
print(ans)
