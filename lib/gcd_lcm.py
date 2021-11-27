# 複数の数の最大公約数・最小公倍数
from functools import reduce
from math import gcd


# 最大公約数
def gcd_list(num_list: list) -> int:
    return reduce(gcd, num_list)


# 最小公倍数
def lcm_list(num_list: list):
    return reduce(lcm_base, num_list, 1)


# 最小公倍数
# a * b // gcd(a, b))
