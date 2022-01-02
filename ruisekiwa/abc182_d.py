# D - Wandering
# https://atcoder.jp/contests/abc182/tasks/abc182_d
# 累積和
N = int(input())
A = list(map(int, input().split()))

# 累積和
S = [0] * (N + 1)
# 累積和の最大値
M = [0] * (N + 1)

for i in range(N):
    S[i + 1] = A[i] + S[i]
    M[i + 1] = max(M[i], S[i + 1])

# accumulateを利用することでシンプルに累積和を求められる
# from itertools import accumulate
# S = list(accumulate(A))
# M = list(accumulate(A, func=max))

ans, cur = 0, 0
for i in range(N):
    ans = max(ans, cur + M[i + 1])
    cur += S[i + 1]

print(ans)
