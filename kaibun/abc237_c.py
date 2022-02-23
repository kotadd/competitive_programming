#  C - kasaka
# https://atcoder.jp/contests/abc237/tasks/abc237_c
# 先頭に a をいくつか（ 0 個でも良い）つけ加えて回文にすることができるか判定

def is_palindrome(s):
    return s == s[::-1]


S = input()

cnt_a = 0
for s in reversed(S):
    if s != 'a':
        break
    cnt_a += 1

cnt = 0
for s in S:
    if s != 'a':
        break
    cnt += 1
    if cnt > cnt_a:
        print('No')
        exit()

S = S.strip('a')

if is_palindrome(S):
    print('Yes')
else:
    print('No')
