# https://atcoder.jp/contests/abc150/tasks/abc150_c
# C - Count Order
# P,Qの辞書順の差

from itertools import permutations

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

s = []
for i in range(1, N + 1):
    s.append(i)

cnt = 0
p = 0
q = 0
for v in permutations(s):
    cnt += 1
    for i in range(N):
        if v[i] != P[i]:
            break
    else:
        p = cnt

    for i in range(N):
        if v[i] != Q[i]:
            break
    else:
        q = cnt

print(abs(p - q))
