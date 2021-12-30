# C - Graph Isomorphism
# https://atcoder.jp/contests/abc232/tasks/abc232_c
# Pは(1,...,N)を並べ替えて得られる + 1<=N<=8 => 順列全探索

from itertools import permutations

N, M = map(int, input().split())

A = []

for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    A.append([a, b])

A.sort()
B = []
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    B.append([a, b])

B.sort()

X = list(i for i in range(N))
for d in permutations(X):
    tmp = []
    for j in range(M):
        a = d[A[j][0]]
        b = d[A[j][1]]
        if a > b:
            a, b = b, a
        tmp.append([a, b])

    tmp.sort()
    if tmp == B:
        print('Yes')
        exit()


print('No')
