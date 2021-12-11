# D - Staircase Sequences
# https://atcoder.jp/contests/abc190/tasks/abc190_d
# 数学 + パリティ
# 等差数列の和：S = 1/2 * n(2*a+(n-1)d) ⇔ 2N/n -d = 奇数 ⇔ これらの偶奇が異なる
# https://manabitimes.jp/math/1120

def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


N = int(input())

divisors = make_divisors(2 * N)
ans = 0
for d in divisors:
    m = 2 * N / d
    if m % 2 != d % 2:
        ans += 1
print(ans)
