# E - Fraction Floor Sum
# https://atcoder.jp/contests/abc230/tasks/abc230_e
# N/iの sum を求める
# (N//i - N//i+1) * iを√N-1まで合算し、N//iを√Nまで合算すれば答えが求まる ??
# √N まで合算し、最後に2*N- int(√N)^2を引く （ブロックで考える） ??
# ※詳細な解説記事をまた読む

N = int(input())
ans = 0
B = int(N**0.5)
for q in range(1, B):
    a = N // q
    b = N // (q + 1)
    ans += (a - b) * q
for i in range(1, N // B + 1):
    ans += N // i
print(ans)


# 公式？
# a=int(input())
# b=int(a**.5)
# n=0
# for i in range(1,b+1):
#   n+=a//i
# print(2*n-b*b)
