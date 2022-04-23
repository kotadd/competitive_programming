# This Message Will Self-Destruct in 5s
# https://atcoder.jp/contests/abc166/tasks/abc166_e

from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

d = defaultdict(int)

for i in range(N):
    d[i + A[i]] += 1

ans = 0
for i in range(N):
    ans += d[i - A[i]]

print(ans)
