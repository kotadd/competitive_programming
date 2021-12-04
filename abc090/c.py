# C - Flip,Flip, and Flip......
# https://atcoder.jp/contests/abc090/tasks/arc091_a
# パリティ
# 図示すれば簡単

N, M = map(int, input().split())

if N > M:
    N, M = M, N

if N == 1:
    if M == 1:
        print(1)
    else:
        print(M - 2)
else:
    print((N - 2) * (M - 2))
