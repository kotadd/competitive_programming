# 2^20 = 1048576 = 10**6
Q = int(input())
N = 2**20

A = [-1] * N
# 同じ数値（h）が来たときに、開始位置を一気にずらす
B = list(range(N))

for i in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        h = x % N
        while A[h] != -1:
            h = (B[h] + 1) % N
        A[h] = x
        B[x % N] = h

    else:
        j = x % N
        print(A[j])
