# C - Not so Diverse
# https://atcoder.jp/contests/abc081/tasks/arc086_a
from collections import Counter

N, K = map(int, input().split())
A = list(map(int, input().split()))

C = Counter(A)
ans = 0
i = 0
for c in C.most_common():
    if i < K:
        i += 1
        continue
    ans += c[1]

print(ans)
