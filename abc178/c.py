# https://drken1215.hatenablog.com/entry/2020/10/09/162600
# ~が含まれる = 全体 - （~が含まれない）
# 包除原理
# 10^N - (2*9^N -8^N)
# a - b + c

n = int(input())
MOD = 10**9 + 7

if n == 1:
    print(0)
elif n == 2:
    print(2)
else:
    a = 10
    b = 9
    c = 8
    for _ in range(n - 1):
        a *= 10
        a %= MOD
        b *= 9
        b %= MOD
        c *= 8
        c %= MOD
    print((a - 2 * b + c) % MOD)
