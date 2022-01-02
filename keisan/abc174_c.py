# C - Repsept
# https://atcoder.jp/contests/abc174/tasks/abc174_c
# 7,77,777,… という数列の中に初めて K の倍数が登場するのは何項目

K = int(input())
cur = 7

for i in range(1, K + 1):
    if cur % K == 0:
        print(i)
        exit()
    else:
        cur = (cur * 10 + 7) % K

print(-1)
