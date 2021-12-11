# D - Project Planning
# https://atcoder.jp/contests/abc227/tasks/abc227_d
# 二分探索
# 「N個の値を最大値を最小化したい」「N人の作業員の働き時間の最大値がなるべく最小になるようにしたい」
# 上記の反対の問題。
# 「N個のチームからある一定人数(P)以下で最大の人数を出してもらい、その合計がP×Kより大きい最大値を調べる」

N, K = map(int, input().split())
A = list(map(int, input().split()))

ok = 0
ng = 10**18 // K

# okが2、ngが3のようになるため、ng-ok>1である限り繰り返す O(Nlog(M))
while ng - ok > 1:
    mid = (ok + ng) // 2
    total = 0
    for a in A:
        total += min(a, mid)

    if total >= K * mid:
        ok = mid
    else:
        ng = mid

print(ok)
