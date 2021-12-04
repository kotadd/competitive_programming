# B - Almost GCD
# https://atcoder.jp/contests/abc182/tasks/abc182_b
# 正の整数 k の GCD 度を出す。
# ※kは2~1000であれば良く、Aの中から選ぶ必要はない
N = int(input())
A = list(map(int, input().split()))

gcd_ratio = 0
ans = 2
for i in range(2, 1001):
    tmp = 0
    for j in range(N):
        if A[j] % i == 0:
            tmp += 1
    if tmp > gcd_ratio:
        gcd_ratio = tmp
        ans = i
print(ans)
