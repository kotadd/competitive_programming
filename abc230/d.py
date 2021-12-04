# D - Destroyer Takahashi
# https://atcoder.jp/contests/abc230/tasks/abc230_d
# 貪欲法
# 区間スケジューリング問題：区間の終端が小さい順にsortを行い、手前から処理していく
# 類題：AGC009A
N, D = map(int, input().split())

X = []
for i in range(N):
    l, r = map(int, input().split())
    X.append([l, r])

X.sort(key=lambda x: x[1])

ans = 0
cur = -10**9
for i in range(N):
    if cur + D - 1 >= X[i][0]:
        continue
    if cur + D - 1 < X[i][0]:
        ans += 1
        cur = X[i][1]

print(ans)
