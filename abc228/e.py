# 1 以上 K 以下の整数からなる長さ N の整数列
# 1 以上 M 以下の整数の点数をつけます

# from itertools import product
# N, K, M = map(int, input().split())
# MOD = 998244353
# L = list(range(1, K + 1))
# cnt = len(list(product(L, repeat=N)))
# print(M**cnt % MOD)

# 「1以上K以下の整数からなる長さNの整数列」はK^N個
# 審査対象となる数列それぞれに対して 1 以上 M 以下の整数の点数を与える方法」は M^(K^N)通り

N, K, M = map(int, input().split())
MOD = 998244353

if M % MOD == 0:
    print(0)
    exit()

p = pow(K, N, MOD - 1)
print(pow(M, p, MOD))
