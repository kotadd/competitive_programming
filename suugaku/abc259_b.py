# B - Counterclockwise Rotation
# https://atcoder.jp/contests/abc259/tasks/abc259_b
# 回転、三角関数、逆三角関数

import math
a, b, d = map(int, input().split())
s = complex(a, b)
rad = math.radians(d)
r = complex(math.cos(rad), math.sin(rad))
ans = s * r
print(ans.real, ans.imag)


# 複素数
# from math import sin, cos, radians

# a, b, d = map(int, input().split())
# d = radians(d)
# print(a * cos(d) - b * sin(d), a * sin(d) + b * cos(d))
