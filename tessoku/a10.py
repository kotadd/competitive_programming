# 累積和 一次元
# A10 - Resort Hotel
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_j

N = int(input())
A = list(map(int, input().split()))

X = [0] * N
Y = [0] * N

X[0] = A[0]
for i in range(1, N):
    X[i] = max(X[i - 1], A[i])

Y[N - 1] = A[N - 1]
for i in range(0, N - 1)[::-1]:
    Y[i] = max(Y[i + 1], A[i])

D = int(input())
for i in range(D):
    l, r = map(lambda x: int(x) - 1, input().split())
    print(max(X[l - 1], Y[r + 1]))
