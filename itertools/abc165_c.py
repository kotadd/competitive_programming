# C - Many Requirements
# https://atcoder.jp/contests/abc165/tasks/abc165_c
# 重複単調増加の組み合わせ combinations_with_replacement

import itertools

N, M, Q = map(int, input().split())

X = []
for _ in range(Q):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    X.append((a, b, c, d))

ans = 0
for comb in itertools.combinations_with_replacement(list(range(1, M + 1)), N):
    A = list(comb)
    tmp = 0
    for a, b, c, d in X:
        if A[b] - A[a] == c:
            tmp += d

    ans = max(ans, tmp)

print(ans)
