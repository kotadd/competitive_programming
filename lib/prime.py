# 素因数分解
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


# 素数判定
def is_prime(x: int):
    if x <= 1:
        return False
    for i in range(2, int(x**1 / 2) + 1):
        if x % i == 0:
            return False
    return True


# 素数をリストで返す：エラトステネスのふるい Sieve of Eratosthenes  O(NloglogN)
def list_primes(limit: int):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False

    for p in range(2, limit + 1):
        if not is_prime[p]:
            continue

        primes.append(p)
        q = p * 2
        while q <= limit:  # for q in range(p * 2, limit + 1, p):
            is_prime[q] = False
            q += p

    # is_primeを返せば、True/Falseのリストを渡す
    return primes
