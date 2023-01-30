# A29 - Power
# https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_aq
# 繰り返し二乗法
# 例えば 2^10 の場合、2^2 * 2^8 を計算すれば良い（10は2進数で1010なので、2^2 * 2^8 となるとも言い換えられる）

MOD = 1000000007
a, b = map(int, input().split())


def power(a, b, m):
    p = a
    ret = 1
    for i in range(30):
        # 2^i
        wari = 1 << i
        #  if b & wari: でも同じ
        if b // wari % 2 == 1:
            ret = ret * p % m
        p = p * p % m
    return ret


print(power(a, b, MOD))
