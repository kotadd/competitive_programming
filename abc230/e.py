# E - Fraction Floor Sum
# https://atcoder.jp/contests/abc230/tasks/abc230_e
# N/iの sum を求める
# (N//i - N//i+1) * iを√N-1まで合算し、N//iを√Nまで合算すれば答えが求まる ??
# √N まで合算し、最後に2*N- int(√N)^2を引く （ブロックで考える） ??
# ※詳細な解説記事をまた読む

N = int(input())
ans = 0
i = 1
while i <= N:
    x = N // i
    ni = N // x + 1
    ans += x * (ni - i)
    i = ni
print(ans)


# 動画公式解説
# 同じ値になるiをまとめて計算する O(√N)
# N = int(input())
# ans = 0
# i = 1
# while i <= N:
#     x = N // i # ある値になる
#     ni = (N // x) + 1 # 一つ上の式でxとiを入れ替えて、次のiにするために+1する
#     ans += x * (ni - i) # ある値×個数
#     i = ni
# print(ans)


# 公式？
# a=int(input())
# b=int(a**.5)
# n=0
# for i in range(1,b+1):
#   n+=a//i
# print(2*n-b*b)
