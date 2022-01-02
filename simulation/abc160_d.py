# D - Line++
# https://atcoder.jp/contests/abc160/tasks/abc160_d
# 制約：3 <= N <= 2*10^3 であるため、規則を考えるのではなく、ただシミュレーションをすれば良い

N, X, Y = map(int, input().split())

ans = [0] * N
for i in range(1, N):
    for j in range(i + 1, N + 1):
        k = min(j - i, abs(i - X) + 1 + abs(j - Y))
        ans[k] += 1

for i in range(1, N):
    print(ans[i])
