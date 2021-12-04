# B - Billiards
# https://atcoder.jp/contests/abc183/tasks/abc183_b
# sy:gyに内分される
# 内分の公式：https://manabitimes.jp/math/1243

sx, sy, gx, gy = map(float, input().split())
print((sx * gy + gx * sy) / (sy + gy))
