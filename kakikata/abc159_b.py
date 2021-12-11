# B - String Palindrome
# https://atcoder.jp/contests/abc159/tasks/abc159_b
# 回文の判定方法

def is_palindrome(s):
    return s == s[::-1]


S = input()
N = len(S)
na = (N - 1) // 2
A = S[0:na]
nb = (N + 3) // 2 - 1
B = S[nb:]

if is_palindrome(S) and is_palindrome(A) and is_palindrome(B):
    print('Yes')
else:
    print('No')
