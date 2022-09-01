# A - A to Z String 2
# https://atcoder.jp/contests/abc257/tasks/abc257_a

import string
import math

n, x = map(int, input().split())
a = math.ceil(x / n)
print(string.ascii_uppercase[a - 1])


# 解答1
# n, x = map(int, input().split())
# s = []
# for i in range(ord('A'), ord('Z') + 1):
#     for j in range(n):
#         s.append(chr(i))
# print(s[x - 1])

# 解答2
# n, x = map(int, input().split())
# print(chr(ord('A') + (x - 1) // n))
