# 区間の総和は累積和
# 「L番からR番までの合計得点は S[R] - S[L-1]」

import sys
input = sys.stdin.readline

n = int(input())

rui1 = [0] * (n + 1)
rui2 = [0] * (n + 1)

for i in range(1, n + 1):
    c, p = map(int, input().split())
    if c == 1:
        rui1[i] += rui1[i - 1] + p
        rui2[i] = rui2[i - 1]
    elif c == 2:
        rui1[i] = rui1[i - 1]
        rui2[i] += rui2[i - 1] + p


q = int(input())

for i in range(q):
    l, r = map(int, input().split())
    print(rui1[r] - rui1[l - 1], rui2[r] - rui2[l - 1])
