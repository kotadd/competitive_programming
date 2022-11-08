# C - Adjacent Swaps
# https://atcoder.jp/contests/abc250/tasks/abc250_c

N, Q = map(int, input().split())
A = list(range(1, N + 1))
pos = [i - 1 for i in range(N + 1)]
for _ in range(Q):
    x = int(input())
    p = pos[x]
    if p != N - 1:
        A[p], A[p + 1] = A[p + 1], A[p]
        pos[x] = p + 1
        pos[A[p]] = p
    else:
        A[p], A[p - 1] = A[p - 1], A[p]
        pos[x] = p - 1
        pos[A[p]] = p

print(*A)
