# https://atcoder.jp/contests/abc146/tasks/abc146_c
# C - Buy an Integer
# 値段に単調性 (大きい整数ほど値段も高い) ので、二分探索を利用する

def check(N):
    dN = len(str(N))
    return A * N + B * dN


A, B, X = map(int, input().split())

ok = 0
ng = 10**9 + 1

while ok + 1 != ng:
    md = (ok + ng) // 2
    if check(md) <= X:
        ok = md
    else:
        ng = md

print(ok)
