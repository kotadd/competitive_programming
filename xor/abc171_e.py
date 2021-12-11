# E - Red Scarf
# https://atcoder.jp/contests/abc171/tasks/abc171_e
N = int(input())

A = list(map(int, input().split()))

ans = 0
for a in A:
    ans ^= a

for a in A:
    print(ans ^ a, end=' ')
