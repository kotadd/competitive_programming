import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))

s = 0

ans = []
for _ in range(Q):
    T, X, Y = map(int, input().split())

    x = (X - 1 - s) % N
    y = (Y - 1 - s) % N

    if T == 1:
        A[x], A[y] = A[y], A[x]
    elif T == 2:
        s += 1
    else:
        ans.append(A[x])

print(*ans, sep="\n")
