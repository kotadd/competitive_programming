# 小さい制約は順列全探索
# permutations

from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

bad_pair = set()
for i in range(m):
    x, y = map(int, input().split())
    bad_pair.add((x - 1, y - 1))
    bad_pair.add((y - 1, x - 1))

inf = 10**18
ans = inf

for X in list(permutations([i for i in range(n)])):
    a = sum(A[X[j]][j] for j in range(n))
    for j in range(n - 1):
        if (X[j], X[j + 1]) in bad_pair:
            break
    else:
        ans = min(ans, a)

if ans == inf:
    ans = -1

print(ans)
