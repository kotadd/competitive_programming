#  C - Maximal Value
# https://atcoder.jp/contests/abc140/tasks/abc140_c
# B_i >= max(A_i, A_i+1)  ⇔ A_i = min(B_i,B_i+1)
INF = 10 ** 9
N = int(input())
B = [INF] + list(map(int, input().split())) + [INF]
A = []
for i in range(N):
    A.append(min(B[i], B[i + 1]))

print(sum(A))
