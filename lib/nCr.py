# nCrの計算（コンビネーション） nCm
MOD = 10**9 + 7


# フェルマーの小定理を利用している。素数で割る時に速い
def cmb(n, r):
    r = min(n - r, r)
    if r == 0:
        return 1
    x = 1
    y = 1
    for i in range(r):
        x = x * (n - i) % MOD
        y = y * (i + 1) % MOD
    return x * pow(y, MOD - 2, MOD) % MOD


a = cmb(4, 2)


# 計算量が少ない時に使える方
#
# from operator import mul
# from functools import reduce
# def cmb(n, r):
#     r = min(n - r, r)
#     if r == 0:
#         return 1
#     over = reduce(mul, range(n, n - r, -1))
#     under = reduce(mul, range(1, r + 1))
#     return over // under
