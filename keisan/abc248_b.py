# B - Slimes
# https://atcoder.jp/contests/abc248/tasks/abc248_b
# logの利用
import math

a, b, k = map(int, input().split())

print(math.ceil(math.log(b / a, k)))
