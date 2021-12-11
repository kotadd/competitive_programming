# D - Hachi
# https://atcoder.jp/contests/abc181/tasks/abc181_d
# 下三桁が8の倍数かどうかを調べる（1000=8*125であることから自明）

from collections import Counter

S = input()

if len(S) <= 2:
    if int(S) % 8 == 0 or int(S[::-1]) % 8 == 0:
        print('Yes')
    else:
        print('No')
    exit()

cnt = Counter(S)

for i in range(112, 1000, 8):
    s = str(i)
    if not Counter(str(i)) - cnt:
        print('Yes')
        exit()

print('No')
