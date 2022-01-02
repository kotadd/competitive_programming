# D - Opposite
# https://atcoder.jp/contests/abc197/tasks/abc197_d

import math
N = int(input())
x0, y0 = list(map(int, input().split()))
xh, yh = list(map(int, input().split()))
s = complex(x0, y0)
t = complex(xh, yh)
o = (s + t) / 2

# 回転させたい角度θ
rad = 2 * math.pi / N
# 角度θで長さ1のベクトル
r = complex(math.cos(rad), math.sin(rad))
# sをoを原点としてθ分回転させて、もとに戻す
ans = o + (s - o) * r
print(ans.real, ans.imag)
