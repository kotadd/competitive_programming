# C - Good Sequence
# https://atcoder.jp/contests/abc082/tasks/arc087_a

from collections import Counter

N = int(input())
A = list(map(int, input().split()))

C = Counter(A)

ans = 0
for k, v in C.items():
    if k > v:
        ans += v
    else:
        ans += v - k

print(ans)
