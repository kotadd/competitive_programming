# C - Anti-Division
# https://atcoder.jp/contests/abc131/tasks/abc131_c
# 整数 A,B,C,D において A 以上 B 以下の整数のうち、C でも D でも割り切れないものの個数

# 区間[a,b]の個数は区間[1,b]の個数-区間[1,a)の個数

from math import gcd

A, B, C, D = map(int, input().split())

diff = B - A + 1

lcm = C * D // gcd(C, D)

A -= 1
large_mods = B // C + B // D - B // lcm
small_mods = A // C + A // D - A // lcm

ans = diff - (large_mods - small_mods)

print(ans)
