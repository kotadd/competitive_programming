# D - Factorial and Multiple
# https://atcoder.jp/contests/abc280/editorial/5333
import math


K = int(input())

for i in range(1, 2000001):
    K //= math.gcd(K, i)
    if K == 1:
        print(i)
        exit()

print(K)
