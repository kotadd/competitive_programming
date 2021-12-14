# D - Triangles
# 三角形は何種類あるのか？
# 2本の棒を固定し、3本目を2分探索で求める
from bisect import bisect_left

N = int(input())
L = sorted(list(map(int, input().split())))

ans = 0
for a in range(N):
    for b in range(a + 1, N):
        r = bisect_left(L, L[a] + L[b])
        l = b + 1
        print(l, r)
        ans += max(0, r - l)

print(ans)


# 解法1： N^3で間に合うケース
# N = int(input())
# A = sorted(list(map(int, input().split())))

# ans = 0
# for i in range(N):
#     for j in range(i + 1, N):
#         for k in range(j + 1, N):
#             ans += (A[k] < A[i] + A[j])

# print(ans)
