# A - Batting Average
# https://atcoder.jp/contests/abc274/tasks/abc274_a
# 四捨五入
from decimal import Decimal


a, b = map(int, input().split())

d = Decimal(str(b / a))
r = d.quantize(Decimal('0.000'))
print(r)
