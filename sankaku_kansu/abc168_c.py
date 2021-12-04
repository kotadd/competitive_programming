#  C - : (Colon)
from math import sqrt, cos, radians

A, B, H, M = map(int, input().split())

# 時針が分針の分も進むことに注意
# 例：10時40分だと、30度*10 + 30度*(40/60) まで回転する
h_needle = H * 30 + (M / 60) * 30
m_needle = M * 6
# 時針と分針の差の角度を出す
theta = abs(h_needle - m_needle)
# 角度をradianに変換する
r = radians(theta)

# 余弦定理
print(sqrt(A**2 + B**2 - 2 * A * B * cos(r)))
