# D - Count Interval
# https://atcoder.jp/contests/abc233/tasks/abc233_d

# 区間和の問題なので、累積和で解ける
# 普通に解くとO(N^2)となるため、工夫が必要。
# (手前から順番に加算した値) - K がすでにdictにある場合、その数をansに加算する

from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))
d = defaultdict(int)

ans = 0
s = 0
d[0] = 1
for a in A:
    s += a
    ans += d[s - K]
    d[s] += 1

print(ans)
