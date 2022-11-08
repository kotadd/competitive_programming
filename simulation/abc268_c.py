# C - Chinese Restaurant
# https://atcoder.jp/contests/abc268/tasks/abc268_c
# 料理iが初め人jの前にあるとし、回転させる
N = int(input())
P = list(map(int, input().split()))

C = [0] * N
for i in range(N):
    for j in range(3):
        C[(P[i] - 1 - i + j) % N] += 1

ans = 0
for c in C:
    ans = max(ans, c)
print(C)
