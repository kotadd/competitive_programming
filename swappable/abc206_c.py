# https://atcoder.jp/contests/abc206/tasks/abc206_c
#  C - Swappable
# 制約： 2 <= N <= 3×10^5
from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

C = Counter(A)

ans = 0
for c in C:
    ans += C[c] * (N - C[c])

print(ans // 2)
