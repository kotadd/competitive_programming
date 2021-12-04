# 因数分解しよう
mod = 10**9 + 7

N = int(input())

total = 1
for _ in range(N):
    A = sum(list(map(int, input().split()))) % mod
    total = total * A % mod

print(total)
