# D - Factorial and Multiple
# https://atcoder.jp/contests/abc280/tasks/abc280_d

from collections import Counter


def prime_factorize(n: int) -> list:
    return_list = []
    while n % 2 == 0:
        return_list.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            return_list.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        return_list.append(n)
    return return_list


K = int(input())
lst = prime_factorize(K)
C = Counter(lst)
M = 10**12 + 1
X = []

for k, v in C.items():
    total = 0
    for i in range(k, M, k):
        x = i
        while x % k == 0:
            total += 1
            x //= k
        if total >= v:
            break
    X.append(i)

print(max(X))
