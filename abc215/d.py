N, M = map(int, input().split())
A = list(map(int, input().split()))
limit = max(max(A), M)

can_use_prime = [True] * (limit + 1)
prime_factors = []

for a in A:
    can_use_prime[a] = False

is_prime = [True] * (limit + 1)
for p in range(2, limit + 1):
    if not is_prime[p]:
        continue
    for q in range(p * 2, limit + 1, p):
        is_prime[q] = False
        can_use_prime[p] &= can_use_prime[q]
    if not can_use_prime[p]:
        prime_factors.append(p)

for p in prime_factors:
    for q in range(p * 2, M + 1, p):
        can_use_prime[q] &= can_use_prime[p]

ans = [1]
for p in range(2, M + 1):
    if can_use_prime[p]:
        ans.append(p)

print(len(ans))
for p in ans:
    print(p)
