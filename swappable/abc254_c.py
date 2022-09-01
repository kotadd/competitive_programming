# C - K Swap
# https://atcoder.jp/contests/abc254/tasks/abc254_c
# 独立に昇順に並び替えた上で元の位置に戻す
N, K = map(int, input().split())
A = list(map(int, input().split()))

for i in range(K):
    A[i::K] = sorted(A[i::K])
print('Yes' if sorted(A) == A else 'No')
