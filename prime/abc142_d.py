#  D - Disjoint Set of Common Divisors
# https://atcoder.jp/contests/abc142/tasks/abc142_d
# 素因数分解 + 最大公約数
# prime

from math import gcd


def prime_factorize(n: int):
    return_set = {1}
    while n % 2 == 0:
        return_set.add(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            return_set.add(f)
            n //= f
        else:
            f += 2
    if n != 1:
        return_set.add(n)
    return return_set


A, B = map(int, input().split())
x = gcd(A, B)
prime_set = prime_factorize(x)
print(len(prime_set))
