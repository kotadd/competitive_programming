# A30 - Combination
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ad
# nCr = n! / (r! * (n-r)!)
# Mを素数とし、bをMで割り切れない整数であるとする。このとき、Mで割った余りを求める問題では「÷b」を「×b^M-2」に置き換えても計算結果は変わらない
# フェルマーの小定理：p が素数で，a が p の倍数でない正の整数のとき a^(p-1) ≡ 1 (mod p)


M = 1000000007
n, r = map(int, input().split())

# 手順1 分子の値n!をMで割った余りaを求める
a = 1
for i in range(1, n + 1):
    a = (a * i) % M

# 手順2 分母の値r!*(n-r)!をMで割った余りbを求める
b = 1
for i in range(1, r + 1):
    b = (b * i) % M
for i in range(1, n - r + 1):
    b = (b * i) % M

# 手順3 a × b^M-2 をMで割った余りを求める
print(a * pow(b, M - 2, M) % M)
