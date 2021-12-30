# B - Caesar Cipher
# https://atcoder.jp/contests/abc232/tasks/abc232_b
# SとTがk文字ずらした時に一致するか？

S = input()
T = input()

se = set()
for s, t in zip(S, T):
    se.add((ord(s) - ord(t)) % 26)

if len(se) == 1:
    print('Yes')
else:
    print('No')
