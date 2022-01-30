# 素因数分解（set)：1を含む
def prime_factorize_set(n: int):
    return_set = {1}
    while n % 2 == 0:
        return_set.add(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            return_set.add(f)
            n //= f
        else:
            f += 2
    if n != 1:
        return_set.add(n)
    return return_set


# 素因数分解(list)
def prime_factorize(n: int):
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
