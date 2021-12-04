# C - Five Transportations
# https://atcoder.jp/contests/abc123/tasks/abc123_c
# ボトルネックを探す

from math import ceil

N = int(input())
transportations = [int(input()) for _ in range(5)]

ans = ceil(N / min(transportations)) + 4

print(ans)
