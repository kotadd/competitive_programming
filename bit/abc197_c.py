#  C - ORXOR
# https://atcoder.jp/contests/abc197/tasks/abc197_c
# 隣り合う要素の間にそれぞれに仕切りを入れるか入れないかの 2^N-1通り

N = int(input())
A = list(map(int, input().split()))

ans = 1 << 30

for i in range(1 << N - 1):
    xored = 0
    ored = 0
    for j in range(N + 1):
        if j < N:
            ored |= A[j]
        if j == N or (i & (1 << j)):
            xored ^= ored
            ored = 0
    ans = min(ans, xored)

print(ans)
