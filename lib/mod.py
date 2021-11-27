# MOD用組み合わせ
def mod_cmb(n: int, k: int, p: int) -> int:
    if n < 0 or k < 0 or n < k:
        return 0
    if n == 0 or k == 0:
        return 1
    if (k > n - k):
        return mod_cmb(n, n - k, p)
    c = d = 1
    for i in range(k):
        c *= (n - i)
        d *= (k - i)
        c %= p
        d %= p
    return c * pow(d, p - 2, p) % p
