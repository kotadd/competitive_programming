# D - Sum of difference
# https://atcoder.jp/contests/abc186/tasks/abc186_d
# 累積和
N = int(input())
A = sorted(list(map(int, input().split())))

B = []
tmp = 0
for a in A:
    tmp += a
    B.append(tmp)

ans = 0
for i in range(1, N):
    ans += A[i] * i - B[i - 1]

print(ans)
