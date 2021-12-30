# C - One Quadrillion and One Dalmatians
# https://atcoder.jp/contests/abc171/tasks/abc171_c
# 1000000000000001 匹の犬の名前
# 26進数なので %26と //26 を繰り返す
# alpbhabetを調べるときは chr(ord('a')+i)

N = int(input())
ans = ''
while N > 0:
    N -= 1
    ans += chr(ord('a') + N % 26)
    N //= 26
print(ans[::-1])
