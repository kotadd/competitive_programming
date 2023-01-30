# C - abc285_brutmhyhiizp
# https://atcoder.jp/contests/abc285/tasks/abc285_c

S = input()
len = len(S)

ans = 0
for i in range(len):
    ans += (ord(S[-i - 1]) - ord('A') + 1) * (pow(26, i))

print(ans)
