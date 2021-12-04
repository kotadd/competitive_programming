# https://atcoder.jp/contests/abc216/tasks/abc216_c
# C - Many Balls
# ある操作を繰り返してNにする→Nに対して操作を行なって逆順にする
# pythonの誤差の問題かはわからないが、N%2==1でN-=1, elseでN/=2を繰り返すとWAとなった
N = int(input())

ans = ''
while N > 0:
    if N % 2 == 1:
        ans += 'A'
    if N > 1:
        ans += 'B'
    N //= 2

print(ans[::-1])
