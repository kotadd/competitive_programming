# C - Monsters Battle Royale
# https://atcoder.jp/contests/abc118/tasks/abc118_c
# ユークリッドの互除法（モンスターAとBが体力を削りあう）

from math import gcd

N = int(input())
A = list(map(int, input().split()))

ans = A[0]
for i in range(1, N):
    ans = gcd(A[i], ans)

print(ans)
