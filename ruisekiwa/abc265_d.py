# D - Iroha and Haiku (New ABC Edition)
# https://atcoder.jp/contests/abc265/tasks/abc265_d
# 累積和+set（二分探索でも可）
N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))

se = {0}
total = 0
for a in A:
    total += a
    if total - R in se and total - R - Q in se and total - R - Q - P in se:
        print('Yes')
        exit()
    se.add(total)
print('No')
