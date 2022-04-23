#  E - Red and Green Apples
# https://atcoder.jp/contests/abc160/tasks/abc160_e

X, Y, A, B, C = map(int, input().split())
P = sorted(list(map(int, input().split())), reverse=True)[0:X]
Q = sorted(list(map(int, input().split())), reverse=True)[0:Y]
R = list(map(int, input().split()))

A = sorted(P + Q + R, reverse=True)

ans = sum(A[i] for i in range(X + Y))

print(ans)
