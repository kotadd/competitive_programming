# C - Previous Permutation
# https://atcoder.jp/contests/abc276/tasks/abc276_c

N = int(input())
P = list(map(int, input().split()))

j = N - 2
while P[j] < P[j + 1]:
    j -= 1

k = N - 1
while P[j] < P[k]:
    k -= 1

P[j], P[k] = P[k], P[j]
print(*P[:j + 1], *P[:j:-1])
