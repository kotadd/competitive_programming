# https://atcoder.jp/contests/abc179/tasks/abc179_c
# A×B+C=N を満たす正整数の組 (A,B,C) はいくつありますか？
# Cは一意に決まるので、正整数(A,B)の組み合わせを考えるのみ
# Aを固定するとBは (N-1)//A 個ある
N = int(input())
ans = 0
for a in range(1, N):
    ans += (N - 1) // a

print(ans)
