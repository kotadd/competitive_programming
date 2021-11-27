# https://atcoder.jp/contests/abc192/tasks/abc192_c
#  C - To 3
# bit全探索での解法

S = input()
n = len(S)
if int(S) % 3 == 0:
    print(0)
    exit()

ans = 10**10
for i in range(1 << n):
    tmp = ''
    cnt = 0
    for j in range(n):
        if i & (1 << j):
            tmp += S[j]
        else:
            cnt += 1

    if len(tmp) > 0 and int(tmp) % 3 == 0:
        ans = min(cnt, ans)

if ans == 10**10:
    ans = -1
print(ans)
