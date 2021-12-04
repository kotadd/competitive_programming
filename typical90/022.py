# 最大公約数はユークリッドの互除法
# gcd(a, gcd(b,c)) = (a/r-1) + (b/r-1) + (c/r-1)
# 例）20 24 30
# => gcd(24,30) = 6
# => gcd(20,6) = 2
# なので、20/2-1 + 24/2-1 + 30/2-1 = 9 + 11 + 14 =34

import sys
from math import gcd


def main():
    input = sys.stdin.readline
    a, b, c = map(int, input().split())
    r = gcd(a, gcd(b, c))
    print((a // r - 1) + (b // r - 1) + (c // r - 1))


if __name__ == '__main__':
    main()
