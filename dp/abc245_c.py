# C - Choose Elements
# https://atcoder.jp/contests/abc245/tasks/abc245_c
# dpを2つ用意する

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp_a = [False] * N
dp_b = [False] * N

dp_a[0] = True
dp_b[0] = True

for i in range(1, N):
    if dp_a[i - 1]:
        if abs(A[i] - A[i - 1]) <= K:
            dp_a[i] = True
        if abs(B[i] - A[i - 1]) <= K:
            dp_b[i] = True
    if dp_b[i - 1]:
        if abs(A[i] - B[i - 1]) <= K:
            dp_a[i] = True
        if abs(B[i] - B[i - 1]) <= K:
            dp_b[i] = True

if dp_a[N - 1] or dp_b[N - 1]:
    print('Yes')
else:
    print('No')
