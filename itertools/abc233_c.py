# C - Product
# https://atcoder.jp/contests/abc233/tasks/abc233_c
# 取り出したボールに書かれた数の総積が X になるような取り出し方

# 解法1: productの計算なので、itertoolsのproductを利用する
from itertools import product

N, X = map(int, input().split())

A = []
for _ in range(N):
    l, *a = map(int, input().split())
    A.append(a)

ans = 0

for a in product(*A):
    mul = 1
    for x in a:
        mul *= x
    if mul == X:
        ans += 1

print(ans)


# 解法2: dfsを利用して解く
# import sys
# sys.setrecursionlimit(10 ** 7)

# def dfs(pos, seki):
#     global ans
#     if pos == N:
#         if seki == X:
#             ans += 1
#         return

#     for a in A[pos]:
#         dfs(pos + 1, seki * a)


# dfs(0, 1)
# print(ans)
