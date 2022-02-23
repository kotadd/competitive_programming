def list_primes(limit: int):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False

    for p in range(2, limit + 1):
        if not is_prime[p]:
            continue

        primes.append(p)
        q = p * 2
        while q <= limit:
            is_prime[q] = False
            q += p

    return is_prime


# a, b, c, d = map(int, input().split())

# for x in range(a, b + 1):
#     for y in range(c, d + 1):
#         if is_prime(x + y):
#             break
#     else:
#         print('Takahashi')
#         exit()
# print('Aoki')

print(list_primes(200))
