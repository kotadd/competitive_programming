# D - Div Game
# https://atcoder.jp/contests/abc169/tasks/abc169_d
# 素因数分解
# ある素数pについて、最適な割る操作は、p, p2, p3, ...のようにすること
# https://note.nkmk.me/python-prime-factorization/

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


N = int(input())
c = Counter(prime_factorize(N))

ans = 0
for val in c.values():
    i = 1
    while val:
        if val >= i:
            ans += 1
            val -= i
            i += 1
        else:
            break
print(ans)
