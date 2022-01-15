# C - Happy New Year!
# https://atcoder.jp/contests/abc234/tasks/abc234_c
# 0,2 の 2進数でK番目のもの
# binで表示した時の1を2にすれば良いだけ
K = int(input())
b = bin(K)[2:]
b = b.replace('1', '2')
print(b)
