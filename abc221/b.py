# 配列は copy() を使う
S = list(input())
T = list(input())

if S == T:
    print('Yes')
    exit()

for i in range(len(S) - 1):
    s = S.copy()
    tmp = s[i]
    s[i] = s[i + 1]
    s[i + 1] = tmp
    if s == T:
        print('Yes')
        exit()

print('No')
