# https://atcoder.jp/contests/abc186/tasks/abc186_c
# C - Unlucky 7
# 10 進法で表しても 8 進法で表しても 7 を含まない

N = int(input())
ans = 0
for i in range(1, N + 1):
    if ('7' not in str(i)) and ('7' not in oct(i)):
        ans += 1
print(ans)
