# B - Counterclockwise Rotation
# https://atcoder.jp/contests/abc259/tasks/abc259_b
# 回転

import math

a, b, d = map(int, input().split())

rad = math.radians(d)

s = complex(a, b)
r = complex(math.cos(rad), math.sin(rad))
ans = s * r
print(ans.real, ans.imag)
