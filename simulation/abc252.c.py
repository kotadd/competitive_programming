# C - Slot Strategy
# https://atcoder.jp/contests/abc252/tasks/abc252_c

N = int(input())
S = [input() for _ in range(N)]

cnt = [[0 for j in range(10)] for i in range(10)]

for i in range(N):
    for j in range(10):
        cnt[int(S[i][j])][j] = cnt[int(S[i][j])][j] + 1

mx = [0 for i in range(10)]
for i in range(10):
    for j in range(10):
        mx[i] = max(mx[i], 10 * (cnt[i][j] - 1) + j)

print(min(mx))
