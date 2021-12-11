# 約数列挙をlistで
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


# 約数列挙をsetで
def set_divisors(n):
    d = set()
    m = 2
    while m * m <= n:
        while n % m == 0:
            n //= m
            d.add(m)
        m += 1
    if n > 1:
        d.add(n)
    return d
