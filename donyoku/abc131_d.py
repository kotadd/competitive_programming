# D - Megalomania
# https://atcoder.jp/contests/abc131/tasks/abc131_d
# 区間スケジューリング（貪欲法）
N = int(input())

X = [list(map(int, input().split())) for _ in range(N)]

X.sort(key=lambda x: x[1])

total = 0
ans = 'Yes'
for i in range(N):
    total += X[i][0]
    if total > X[i][1]:
        ans = 'No'

print(ans)
