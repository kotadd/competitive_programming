# C - Many Medians
# https://atcoder.jp/contests/abc094/tasks/arc095_a
N = int(input())
X = list(map(int, input().split()))

A = sorted(X)
less = A[N // 2]
larger = A[N // 2 - 1]

for x in X:
    if x < less:
        print(less)
    else:
        print(larger)
