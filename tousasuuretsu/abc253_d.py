# D - FizzBuzz Sum Hard
# https://atcoder.jp/contests/abc253/tasks/abc253_d
# 等差数列の和の公式
from math import gcd


def f(x):
    return x * (x + 1) // 2


n, a, b = map(int, input().split())
c = a * b // gcd(a, b)


print(f(n) - (a * f(n // a)) - (b * f(n // b)) + (c * f(n // c)))
