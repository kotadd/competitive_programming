# C - ±1 Operation 1
# https://atcoder.jp/contests/abc255/tasks/abc255_c
X, A, D, N = map(int, input().split())

B = A + D * (N - 1)
# 単調減少していたら、単調増加する形にする
if A > B:
    A, B = B, A
    D = -D

# 最小〜最大の間にある場合は、等差数列のいずれかの値との差分を求める
if A < X < B:
    Y = (X - A) % D
    ans = min(Y, D - Y)
else:
    ans = min(abs(A - X), abs(B - X))

print(ans)
