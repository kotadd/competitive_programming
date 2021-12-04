#  C - Collinearity
# https://atcoder.jp/contests/abc181/tasks/abc181_c
# 同一直線上にあるもの
N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]

ans = 'No'
for i in range(N):
    x1, y1 = P[i]
    for j in range(i + 1, N):
        x2, y2 = P[j]
        if x2 != x1:
            a1 = (y2 - y1) / (x2 - x1)
        else:
            a1 = 10**10
        for k in range(j + 1, N):
            x3, y3 = P[k]
            if x3 != x2:
                a2 = (y3 - y2) / (x3 - x2)
            else:
                a2 = 10**10
            if a1 == a2:
                ans = 'Yes'

# 別解
# for i in range(N):
#     for j in range(i + 1, N):
#         for k in range(j + 1, N):
#             x1, y1 = P[i]
#             x2, y2 = P[j]
#             x3, y3 = P[k]
#             x1 -= x3
#             x2 -= x3
#             y1 -= y3
#             y2 -= y3
#             if x1 * y2 == x2 * y1:
#                 ans = 'Yes'


print(ans)
