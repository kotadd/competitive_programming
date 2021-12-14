# D - Water Bottle
# https://atcoder.jp/contests/abc144/tasks/abc144_d
# 数学の問題：水筒から水があふれる角度

from math import atan, pi, tan
a, b, x = map(int, input().split())

# 解法1：二分法
# def f(a, b, theta):
#     if theta > pi / 2:
#         return 0
#     ret = 0
#     if a * tan(theta) <= b:
#         ret = a * a * b - a * a * a * tan(theta) / 2
#     else:
#         ret = b * b / tan(theta) * a / 2

#     return ret


# ok = pi / 2
# ng = 0
# for i in range(100001):
#     mid = (ok + ng) / 2
#     if f(a, b, mid) < x:
#         ok = mid
#     else:
#         ng = mid

# print(ok / pi * 180)

# 解法2：数学的に
half = a * a * b / 2
ans = 0

# 三角柱
if x < half:
    ans = atan(a * b * b / (2 * x))
# 台形の柱
else:
    ans = atan((2 * b - 2 * x / (a * a)) / a)

ans = ans / pi * 180

print(ans)
