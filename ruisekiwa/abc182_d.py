# D - Wandering
# https://atcoder.jp/contests/abc182/tasks/abc182_d
# 累積和
# accumulateを利用することでシンプルに累積和を求めることもできる
# from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))

# 累積和
# S = list(accumulate(A))
S = [0] * (N + 1)
# 累積和の最大値
# M = list(accumulate(S, func=max))
M = [0] * (N + 1)

# accumulateを利用しないとき
for i in range(N):
    S[i + 1] = A[i] + S[i]
    M[i + 1] = max(M[i], S[i + 1])

# 上と同じ処理
# x = 0
# for i in range(N):
#     S[i + 1] = S[i] + A[i]
#     x += A[i]
#     M[i + 1] = max(M[i], x)


ans, cur = 0, 0
for i in range(N):
    ans = max(ans, cur + M[i + 1])
    cur += S[i + 1]

print(ans)
