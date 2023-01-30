#  D - Happy New Year 2023
# https://atcoder.jp/contests/abc284/tasks/abc284_d
# 2つの異なる素数p,qを求める（N=p^2*q）
# 1<=N<=9*10^18 のため、試し割りだけだとTLE
# 小さい方の素数が N^(1/3) 以下であることを利用する
# p=i, q=N//i^2
# p=(N//i)^(1/2), q=i

T = int(input())
for _ in range(T):
    N = int(input())
    for i in range(2, int(N**(1 / 3)) + 1):
        if N % i != 0:
            continue
        if (N // i) % i == 0:
            p = i
            q = N // i**2
        else:
            p = int((N // i)**(1 / 2))
            q = i
        break
    print(p, q)
